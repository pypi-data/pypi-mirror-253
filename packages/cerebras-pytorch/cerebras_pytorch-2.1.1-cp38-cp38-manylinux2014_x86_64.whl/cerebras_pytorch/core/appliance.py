# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Appliance Support For Pytorch"""
import functools
import itertools
import logging
import multiprocessing
import multiprocessing.dummy
import multiprocessing.pool
import sys
from collections import defaultdict
from contextlib import ExitStack
from pathlib import Path
from typing import Any, Callable, List, Literal, Optional, Tuple, Union

import dill
import grpc
import torch
from tqdm import tqdm

import cerebras_pytorch as cstorch
from cerebras_appliance.appliance_client import (
    ApplianceClient,
    construct_compile_request,
)
from cerebras_appliance.appliance_manager import (
    ApplianceManager,
    TensorGrouper,
    TensorTransferTracker,
)
from cerebras_appliance.cluster.client import ClusterManagementClient
from cerebras_appliance.CSConfig import CSConfig
from cerebras_appliance.errors import (
    ApplianceClientException,
    register_grpc_error_pickler,
)
from cerebras_appliance.pb.workflow.appliance.common.common_config_pb2 import (
    DebugArgs,
    FrameworkType,
)
from cerebras_appliance.pb.workflow.appliance.common.message_queue_pb2 import (
    ValidTopics,
)
from cerebras_appliance.run_utils import set_ini
from cerebras_appliance.utils import limit_mp_threads, short_temp_dir
from cerebras_pytorch.backend import current_backend_impl
from cerebras_pytorch.core.modes import map_mode_to_modekey
from cerebras_pytorch.saver.checkpoint_reader import CheckpointReader
from cerebras_pytorch.saver.pt_h5_saver import PyTorchH5Saver
from cerebras_pytorch.saver.storage import lazy_tensor_data_wrapper
from cerebras_pytorch.utils.nest import serialize_visit_fns


class ApplianceMode(ApplianceManager):
    """Manage pytorch interactions with the appliance"""

    # pylint: disable=signature-differs
    def __init__(
        self,
        artifact_dir: str,
        compile_dir: str,
        cs_config: CSConfig,
        use_cs_grad_accum: bool = True,
        micro_batch_size: Optional[Union[int, Literal["explore"]]] = None,
        checkpoint_reader_cls=CheckpointReader,
    ):
        super().__init__(
            cs_config,
            Path(compile_dir),
            Path(artifact_dir),
            FrameworkType.PYTORCH,
            use_cs_grad_accum,
            micro_batch_size,
        )

        if cstorch.amp._amp_state.half_dtype_str == "cbfloat16":
            set_ini(self._debug_args, ws_treat_f16_as_cb16=True)

        self._last_fetched_iteration = 0
        self._compile_resp = None
        self.output_names = []
        self.weight_names = {}
        self._output_name_to_idx = {}
        self.auxilliary_state_names = {}

        self.tracker_execute = current_backend_impl().appliance_tracker

        self.checkpoint_reader_cls = checkpoint_reader_cls

    def receive_activations(self, iteration: int):
        """Get activations from appliance.

        Args:
            iteration: Iteration to receive activations for. Note that
                activations are received sequentially. So, if this number is
                a few steps ahead of the last iteration that was received, then
                it counts from last fetched iteration up to this iteration, but
                only returns activations for the requested iteration.
        """
        for i in range(iteration, iteration + 1):
            activations = super().receive_activations(i)

            activation_map = dict()
            received_activations = dict()
            for name, tensor in activations.items():
                if name not in self._output_name_to_idx:
                    raise RuntimeError(
                        f"Received activation with name {name} at iteration {i}"
                        f", but no such name has been registered. Expected "
                        f"activation names are: "
                        f"{self._output_name_to_idx.values()}"
                    )
                activation = cstorch.from_numpy(tensor)
                activation_map[self._output_name_to_idx[name]] = activation
                received_activations[name] = activation

        return received_activations

    # pylint: disable=arguments-differ
    def compile(
        self, batch_size: int, cirh_str: str, validate_only: bool = False
    ):
        """
        Send a compile request to the coordinator
        """
        self.tracker_execute.stop("Initialization", ignore_not_running=True)
        with self.tracker_execute.entry("compile"):
            with self.tracker_execute.entry("pt_cirh"):
                compile_request = construct_compile_request(
                    batch_size=batch_size,
                    num_csx=self._num_csx,
                    max_wgt_servers=self._max_wgt_servers,
                    num_workers_per_csx=self._num_workers_per_csx,
                    cirh_str=cirh_str,
                    compile_dir=str(self._compile_dir),
                    max_act_per_csx=self._max_act_per_csx,
                )
                if validate_only:
                    logging.info("Compile validated locally")
                    with self._artifact_dir.joinpath("cirh.mlir").open(
                        "w"
                    ) as f:
                        f.write(compile_request.compile_info.cirh_content)
                    return None
            self._compile_resp = super().compile(compile_request)
        return self._compile_resp

    def execute(
        self,
        input_fn: Callable,
        input_fn_params: Any,
        batch_size: int,
        total_steps: int,
        checkpoint_steps: int,
        mode: str,
        initial_checkpoint_file: str,
        cleanup_stack: ExitStack,
        send_weights_grouper: Optional[TensorGrouper] = None,
        activation_steps: int = 1,
    ):
        """Run a model on the appliance"""
        mode_key = map_mode_to_modekey(mode)

        with self.tracker_execute.entry("execute_till_recv_loss"):
            self.tracker_execute.start("execute_prep_details")

            mgmt_client = cleanup_stack.enter_context(
                ClusterManagementClient(
                    server=self._mgmt_address,
                    crt_file=self._cs_config.credentials_path,
                    namespace=self._mgmt_namespace,
                    job_timer=self._cs_config.job_timer,
                    workdir=self._artifact_dir,
                )
            )
            response = self.request_execute_job(mgmt_client, self._compile_resp)
            self.stage_execute_coordinator(response)

            cleanup_stack.enter_context(self.subscribe(ValidTopics.STALL))

            # From this point on, if we error out, we try to do a clean exit
            cleanup_stack.enter_context(
                self.clean_shutdown(mgmt_client, response['job_id'])
            )

            self.tracker_execute.stop("execute_prep_details")
            self.initialize_execute_coordinator(
                input_fn,
                input_fn_params,
                total_steps,
                checkpoint_steps,
                self._compile_resp,
                batch_size,
                mode_key,
                [initial_checkpoint_file],
                send_weights_grouper,
                activation_steps=activation_steps,
            )

    def construct_debug_args(self) -> DebugArgs:
        debug_args = super().construct_debug_args()

        # Populate the visit_fn_map in the debug_args so that they
        # can be propagated to the workers
        for (
            serialized_types,
            serialized_visit_fn,
        ) in serialize_visit_fns().items():
            debug_args.debug_worker.visit_fn_map[
                serialized_types
            ] = serialized_visit_fn

        return debug_args

    @property
    def _checkpoint_reader_cls(self):
        return self.checkpoint_reader_cls

    def _map_wgt_name_fw_to_rt(self, tensor_name):
        if tensor_name in self.weight_names:
            return self.weight_names[tensor_name]
        if tensor_name in self.auxilliary_state_names:
            return self.auxilliary_state_names[tensor_name]
        return tensor_name

    def save_weights(
        self,
        weights: List[Tuple[str, Union[torch.Tensor, Any]]],
        file_name: str,
        iteration: int,
    ) -> None:
        """Request weights from appliance and save to the file_name.

        Args:
            weights: List of weights to save. Each weight is a tuple of the
                weight name and the tensor (or other objects) to fetch from
                the appliance and save.
            file_name: Name of the file to save the weights to.
            iteration: Appliance iteration number to save the weights for.
        """

        def get_parameter_name(tensor):
            if (
                isinstance(tensor, torch.Tensor)
                and tensor.device.type == "lazy"
            ):
                from cerebras_pytorch import cerebras_pytorch_lib

                # pylint: disable=c-extension-no-member
                # pylint: disable=no-member
                return cerebras_pytorch_lib.get_tensor_name(tensor)
            return getattr(tensor, "_parameter_name", None)

        def get_tensors():
            seen_weights = set()

            # Create a map between the weight name and the external name
            # to handle duplicate weights
            alias_map = defaultdict(list)
            for external_name, obj in weights:
                parameter_name = get_parameter_name(obj)
                if parameter_name is not None:
                    # pylint: disable=protected-access
                    alias_map[parameter_name].append(external_name)

            # external_name: The name seen by the user (what's saved in ckpt)
            # weight_name: The name of the weight in the model
            # tensor_name: The name of the weight seen by the appliance
            for external_name, obj in weights:
                ckpt_indices = [external_name]

                weight_name = get_parameter_name(obj)
                if weight_name is not None:
                    ckpt_indices.extend(
                        alias
                        for alias in alias_map[weight_name]
                        if alias != external_name
                    )
                else:
                    weight_name = external_name

                if weight_name in seen_weights:
                    continue
                else:
                    seen_weights.add(weight_name)

                tensor_name = None

                if isinstance(obj, torch.Tensor):
                    tensor_name = self.weight_names.get(weight_name)

                    if weight_name in self.skipped_weights:
                        logging.debug(f"Not fetching skipped: {weight_name}")
                        if obj.device.type == "lazy":
                            obj = lazy_tensor_data_wrapper(obj)
                        tensor_name = None
                    elif tensor_name is None and obj.device.type == "lazy":
                        tensor_name = weight_name

                    if tensor_name is None:
                        logging.debug(
                            f"Saving tensor {external_name} to indices: {ckpt_indices}"
                        )
                        # Save the object as is
                        yield None, ckpt_indices, obj
                    else:
                        logging.debug(
                            f"Fetching {tensor_name} and saving to indices: {ckpt_indices}"
                        )
                        # Fetch tensor before saving
                        yield tensor_name, ckpt_indices, None

                else:
                    logging.debug(
                        f"Saving object {external_name} to indices: {ckpt_indices}"
                    )
                    # Save the object as is
                    yield None, ckpt_indices, obj

        recv_tensors = list(get_tensors())

        # Build unique tensor names for validating.
        recv_tensor_names = {name for name, _, _ in recv_tensors}

        # Some related tensors should be requested together to minimize peak
        # memory. Each tensor is independent from the other tensors; the
        # grouping is just to control the fetch order.
        recv_groups = []

        # self.recv_groups is a (possibly empty) list of list of tensor names.
        if self.recv_groups:

            # Build a lookup from tensor_name->(tensor_name, indices, obj)
            # the `None` key will have overlaps, but thats fine. All tensors
            # with a name are guaranteed unique.
            recv_tensor_dict = {t[0]: t for t in recv_tensors}

            # For each group of tensor names, build a matching "group" of
            # recv_tensor input (tuples of (name, indices, obj) )
            for group in self.recv_groups:
                recv_group = []
                for tensor_name in group:
                    inputs = recv_tensor_dict.get(tensor_name, None)
                    if inputs is not None:
                        # Move from global recv list to this group.
                        recv_tensors.remove(inputs)
                        recv_group.append(inputs)
                recv_groups.append(recv_group)

        # Each remaining tensor (maybe all of them) is its own group.
        recv_groups.extend([t] for t in recv_tensors)

        transfer_tracker = TensorTransferTracker()

        with self.tracker_execute.entry(
            "Retrieve and Save weights"
        ), limit_mp_threads():
            if self._transfer_threads > 1:
                ctx = multiprocessing.get_context('spawn')
                pool_cls = functools.partial(
                    multiprocessing.pool.Pool, context=ctx,
                )
            else:
                ctx = multiprocessing.get_context()
                pool_cls = multiprocessing.dummy.Pool
            with short_temp_dir():
                m = ctx.Manager()
            lock = m.Lock()
            with cstorch.saver.storage.use_cstorch_types(True), pool_cls(
                processes=self._transfer_threads,
                initializer=WeightReceiver.initializer,
                initargs=(
                    self._coord_address,
                    self._certificate_bytes,
                    self._default_authority,
                    file_name,
                    iteration,
                    lock,
                ),
            ) as pool:
                try:
                    iter_recv = itertools.chain.from_iterable(
                        pool.imap_unordered(WeightReceiver.runner, recv_groups)
                    )
                    for pkl in tqdm(
                        iter_recv,
                        total=len(recv_tensor_names),
                        desc="Transferring weights from server",
                        dynamic_ncols=True,  # Match console width
                        unit="tensors",
                        file=sys.stdout,
                        disable=None,  # Disable on non-TTY
                    ):
                        tensor_name, outcome = WeightReceiver.deserialize(pkl)
                        transfer_tracker.add(tensor_name, outcome)
                except ApplianceClientException as ex:
                    raise ex

            transfer_tracker.validate(recv_tensor_names)


class WeightReceiver:
    """A class to use in a multiprocessing context for receiving weights."""

    impl: Optional["WeightReceiver"] = None

    def __init__(
        self,
        coord_address,
        certificate_bytes: Optional[bytes],
        default_authority,
        file_name,
        iteration,
        lock,
    ):
        """Constructs a `WeightReceiver` instance.

        Args:
            coord_address: Address of the coordinator to send to.
            certificate_bytes: Optional PEM encoded certificate byte string for
                grpc secure channel setup.
            default_authority: Authority to authorize communication.
        """
        credentials = None
        if certificate_bytes:
            credentials = grpc.ssl_channel_credentials(certificate_bytes)

        self._grpc_client = ApplianceClient(
            coord_address,
            credentials=credentials,
            default_authority=default_authority,
        )

        self._file_name = file_name
        self._iteration = iteration
        self._writer_lock = lock

        # Add pickling support to exceptions so that they include their
        # traceback
        from tblib import pickling_support

        pickling_support.install()

        # gRPC exceptions are not picklable by default. Register custom picklers
        # so they can be properly pickled to be sent across processes.
        register_grpc_error_pickler()

    def __call__(self, inputs):
        """Sends the given tensor through gRPC to appliance service."""
        tensor_name = "Unknown"
        ckpt_indices = []
        try:
            tensor_name, ckpt_indices, tensor = inputs
            if tensor_name is not None:
                tensor = self._grpc_client.recv_output(
                    self._iteration, tensor_name
                )

                try:
                    # Make the tensor writable so that we don't have to copy it
                    # in `cstorch.from_numpy()`. Some arrays cannot be modified
                    # so we ignore the error and copy the array instead.
                    tensor.flags.writeable = True
                except Exception:  # pylint: disable=broad-except
                    pass

                tensor = cstorch.from_numpy(tensor)
            with self._writer_lock:
                # we do not update ckpt_info here so max_store does not matter
                saver = PyTorchH5Saver()
                saver.save_tensor(self._file_name, ckpt_indices[0], tensor)
                saver.create_links(
                    self._file_name, ckpt_indices[0], ckpt_indices[1:]
                )

            return WeightReceiver.serialize((tensor_name, True))
        except Exception as e:  # pylint: disable=broad-except
            return WeightReceiver.serialize((tensor_name, e))

    @staticmethod
    def serialize(val):
        """Generic serialization using dill."""
        return dill.dumps(val)

    @staticmethod
    def deserialize(pkl_val):
        """Generic de-serialization method using dill."""
        return dill.loads(pkl_val)

    @staticmethod
    def initializer(*args, **kwargs):
        """The initializer to use in multiprocessing."""
        WeightReceiver.impl = WeightReceiver(*args, **kwargs)

    @staticmethod
    def runner(group):
        """The runner method to use in multiprocessing."""
        assert WeightReceiver is not None, "Initializer must be called."
        # pylint: disable=not-callable
        return [WeightReceiver.impl(inputs) for inputs in group]

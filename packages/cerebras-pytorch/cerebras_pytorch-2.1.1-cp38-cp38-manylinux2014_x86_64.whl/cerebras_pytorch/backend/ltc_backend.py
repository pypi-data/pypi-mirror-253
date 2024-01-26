# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

""" The PyTorch/LTC backend implementation """
import atexit
import inspect
import os
import sys
from pathlib import Path
from typing import Dict, List, Literal, Optional, Set, Union

import torch
import torch._lazy  # pylint: disable=import-error

import cerebras_pytorch as cstorch
from cerebras_appliance import register_deps
from cerebras_appliance.log import ClassLogger, named_class_logger
from cerebras_pytorch.amp import init as amp_init
from cerebras_pytorch.amp._amp_state import _amp_state
from cerebras_pytorch.backend.base_backend import (
    COMPILE_ONLY_MSG,
    COMPILE_SUCCESS_MSG,
    PROGRAMMING_CS_MSG,
    BaseBackend,
)
from cerebras_pytorch.core.appliance import ApplianceMode
from cerebras_pytorch.core.constants import INPUT_NAME_PREFIX, STATE_NAME_PREFIX
from cerebras_pytorch.core.device import LazyDevice
from cerebras_pytorch.core.modes import EVAL
from cerebras_pytorch.core.name_scope import ScopeName
from cerebras_pytorch.lib import cerebras_pytorch_lib
from cerebras_pytorch.saver.checkpoint_reader import CheckpointReader
from cerebras_pytorch.saver.pt_h5_saver import PyTorchH5Saver
from cerebras_pytorch.saver.storage import lazy_tensor_data_wrapper
from cerebras_pytorch.utils.nest import visit_device_tensors


@named_class_logger("LtcBackend")
class PyTorchLtcBackendImpl(BaseBackend, ClassLogger):
    """ The backend subclass for PyTorch/LTC runs """

    def __init__(
        self,
        backend_type,
        artifact_dir: str = None,
        compile_dir: str = None,
        compile_only: bool = False,
        validate_only: bool = False,
        drop_data: bool = False,
        max_checkpoints: Optional[int] = None,
        log_initialization: bool = True,
        use_cs_grad_accum: bool = True,
        micro_batch_size: Optional[Union[int, Literal["explore"]]] = None,
        retrace_every_iteration: bool = False,
    ):
        super().__init__(backend_type, LazyDevice())
        if artifact_dir is None:
            self.config.artifact_dir = Path.cwd().joinpath("cerebras_logs")
        else:
            self.config.artifact_dir = Path(artifact_dir)

        self.config.artifact_dir.mkdir(parents=True, exist_ok=True)

        if compile_dir is not None:
            self.config.compile_dir = compile_dir

        self.config.compile_only = compile_only
        self.config.validate_only = validate_only
        self.config.max_checkpoints = max_checkpoints
        self.config.log_initialization = log_initialization
        self.config.use_cs_grad_accum = use_cs_grad_accum
        self.config.micro_batch_size = micro_batch_size

        if compile_only or validate_only:
            # No need to initialize the weights if we are only compiling or
            # validating, so disable tracing the initialization altogether.
            # Note: technically, we don't actually skip tracing the
            # initialization, but we do skip the actual initialization of the
            # weights if this is set to False. This is so that we can still
            # trace and initialize the weights if the user wants to save the
            # initial checkpoint.
            self.device.config.lazy_initialization = False
            # We can drop any tensor data that already exists as soon as it's
            # moved to the device
            self.device.config.drop_data = True
        elif drop_data:
            # Trace the initialization, but don't actually initialize the weights
            self.device.config.lazy_initialization = True
            self.device.config.drop_data = True

        if micro_batch_size == "explore" and not compile_only:
            raise RuntimeError(
                "Setting micro_batch_size == 'explore' is only "
                "supported in compile_only mode"
            )

        self.appliance = None

        self.initial_state_file = None

        # To avoid repeated access to the same tensor in appliance we cache
        # all intermediate tensor captured by step closures within compile step
        # inside activations dictionary.
        self.activations: Dict[str, torch.Tensor] = dict()

        self._param_names = set()

        # verbose = bool(int(os.environ.get("CSTORCH_VERBOSE", "0")))
        debug = bool(int(os.environ.get("CSTORCH_DEBUG", "1")))

        cerebras_pytorch_lib.initialize(ir_debug=debug)
        atexit.register(cerebras_pytorch_lib.shutdown)

        register_deps(
            {
                "cerebras-pytorch": "cerebras_pytorch",
                "torch": "torch",
                "torchvision": "torchvision",
            },
        )

        if debug:
            os.environ["LTC_IR_DEBUG_ROOT_PATH"] = ":".join(
                # sys.path entries in order from longest to shortest
                sorted(
                    (path + "/" for path in sys.path if path),
                    key=lambda x: -len(x),
                )
            )

        # Set the number of OMP threads to 1 to avoid issues with
        # multiprocessing/forking
        os.environ["OMP_NUM_THREADS"] = "1"
        os.environ["OPENBLAS_NUM_THREADS"] = "1"
        torch.set_num_threads(1)

        # pylint: disable=import-error
        # Seed the ltc backend for e.g. dropout. This doesn't influence model
        # initialization or dataloader shuffling.
        # Use the initial seed value set via torch.manual_seed()
        cerebras_pytorch_lib.set_rng_state(torch.initial_seed())

        self.logger.verbose("Running using LTC backend")

        # Start initialization tracker
        self.appliance_tracker.start("Initialization")

        # Disable retrace every iteration
        self._retrace_every_iteration = retrace_every_iteration
        cerebras_pytorch_lib.retrace_every_iteration(
            self._retrace_every_iteration
        )

    def _generate_tensor_names(
        self, prefix: str, tensors: list, delimiter: str
    ):
        for scope, tensor in visit_device_tensors(
            data_structure=tensors,
            device_type=self.torch_device.type,
            scope=[prefix] if prefix else None,
        ):
            yield delimiter.join(scope), tensor

    def _generate_state_names(self, tensors: list):
        yield from self._generate_tensor_names(
            STATE_NAME_PREFIX, tensors, '.',
        )

    def _generate_input_names(self, tensors: list):
        yield from self._generate_tensor_names(
            INPUT_NAME_PREFIX, tensors, '_',
        )

    def _generate_output_names(self, tensors: list):
        yield from self._generate_tensor_names(
            "output", tensors, '_',
        )

    def mark_output(self, struct, force=False):
        name_mapping = {}
        for name, tensor in self._generate_output_names(struct):
            name_mapping[id(tensor)] = name

        def map_fn(arg):
            if isinstance(arg, torch.Tensor) and (
                arg.device.type == self.torch_device.type
            ):
                name = name_mapping[id(arg)]

                # This might return a new tensor
                # pylint: disable=c-extension-no-member
                return cerebras_pytorch_lib.mark_output_tensor(
                    arg, name=name, force=force
                )

            return arg

        return torch.utils._pytree.tree_map(map_fn, struct)

    ################################################
    #               DataLoader hooks               #
    ################################################

    def initial_mark_step(self, async_compute: bool = True):
        """Run the initial mark step"""
        # Set the rng state back to what it was when the first parameter was registered
        if self.device._rng_state is not None:
            self.logger.debug("Setting initial rng state")
            torch.set_rng_state(self.device._rng_state)

        prev_async = self.device.config.async_parallel_compute
        try:
            self.device.config.async_parallel_compute = async_compute

            if self.device.config.drop_data:
                msg = "Skipping weight initialization"
                if not self.is_e2e_execution:
                    msg += " as the backend was configured for compile/validation only."
                self.logger.info(msg)

            # Sync all functional tensors so that if any of their views
            # were updated inplace, the updates are visible to the original tensor
            for name, tensor in self._generate_state_names(self.state_dict()):
                # pylint: disable=protected-access,c-extension-no-member
                cerebras_pytorch_lib.sync_functional_tensor(tensor)

            self.logger.trace("Calling initial mark step")

            # Call initial mark_step to trigger asynchronous lazy initialization
            # pylint: disable=protected-access
            with self.device:
                torch._lazy.mark_step()

            self.logger.trace("Finished initial mark step")

        finally:
            self.device.config.async_parallel_compute = prev_async

    def on_run_start(self):
        self.appliance_tracker.stop("Initialization")

        super().on_run_start()

        if self.cs_config.precision_opt_level is None:
            self.cs_config.precision_opt_level = 1

        cerebras_pytorch_lib.set_pol(self.cs_config.precision_opt_level)

        # TODO: only call this if not already initialized
        # initialize automatic mixed precision
        amp_init(verbose=(_amp_state.verbosity == 2),)

        self.logger.verbose(
            f"Appliance total steps:  {self.run_context.num_steps}"
        )
        self.logger.verbose(f"Appliance mode: {self.mode}")

        checkpoint_steps = self.run_context.checkpoint_steps
        if checkpoint_steps is None:
            # TODO: handle case where last checkpoint shouldn't be
            # saved if checkpoint steps was explicitly given to be 0
            # in checkpoint closure
            checkpoint_steps = 0

        self.appliance = ApplianceMode(
            self.config.artifact_dir,
            self.config.compile_dir,
            self.cs_config,
            checkpoint_reader_cls=CheckpointReader,
            use_cs_grad_accum=self.config.use_cs_grad_accum,
            micro_batch_size=self.config.micro_batch_size,
        )

        cerebras_pytorch_lib.set_fp16_type(
            cstorch.amp._amp_state.half_dtype_str
        )

        # pylint: disable=redefined-builtin
        def compile(batch_size: int, cirh_str: str) -> bool:
            self.logger.info(COMPILE_ONLY_MSG)

            with self.appliance.build_worker_image(
                should_skip=self.compile_only or self.validate_only
            ):
                self.appliance.compile(batch_size, cirh_str, self.validate_only)

            self.logger.info(COMPILE_SUCCESS_MSG)
            return True

        def execute(batch_size: int, weights) -> Set[str]:
            if not self.is_e2e_execution:
                return set()

            self.logger.info(PROGRAMMING_CS_MSG)

            if self.mode is None:
                # This means that the user did not call optimizer.step()
                # So, assume that the user wants to run eval
                self.mode = EVAL

                if self.model.training:
                    self.logger.warning(
                        "Model is in training mode but no optimizer.step() "
                        "call was detected. The model will be compiled for "
                        "eval mode but numerics may be affected if ops "
                        "like dropout are present in the model."
                    )

            with self.appliance_tracker.entry(
                "Initialization"
            ), self.appliance_tracker.entry("wait_for_init"):
                self.initial_state_file = os.path.join(
                    self.device.device_data_dir, f"initial_state.hdf5",
                )

                ini_state_dict = {}
                try:
                    for weight in weights:
                        if isinstance(
                            weight, cerebras_pytorch_lib.ApplianceDataInfo
                        ):
                            data = weight
                        else:
                            data = cerebras_pytorch_lib.get_appliance_data(
                                weight
                            )

                        # Call to wait will raise an exception if file write failed
                        data.wait()
                        if data.is_tensor_available:
                            ini_state_dict[
                                weight.name
                            ] = lazy_tensor_data_wrapper(weight)

                    ini_wgt_names = set(ini_state_dict.keys())

                    with cstorch.saver.storage.use_external_link(value=True):
                        saver = PyTorchH5Saver(
                            max_store=self.config.max_checkpoints
                        )
                        saver.save(self.initial_state_file, ini_state_dict)
                finally:
                    # Delete the reference to the weights to release memory (even vms),
                    # otherwise OS will fail to allocate enough memory when forking in
                    # subsequent calls.
                    del ini_state_dict

            self.appliance.execute(
                self.input_fn,
                self.input_fn_params,
                batch_size,
                self.run_context.num_steps,
                checkpoint_steps,
                self.mode,
                self.initial_state_file,
                cleanup_stack=self.run_context.cleanup_stack,
                send_weights_grouper=None,
                activation_steps=self.run_context.activation_steps,
            )

            # Manually update the skipped weights
            self.appliance.skipped_weights.update(
                self._param_names - ini_wgt_names
            )
            self.logger.debug(
                f"Assigning skipped weights: {self.appliance.skipped_weights}"
            )

            return self.appliance.skipped_weights

        # pylint: disable=c-extension-no-member
        cerebras_pytorch_lib.set_callbacks(
            compile_callback=compile, execute_callback=execute,
        )

        self.initial_mark_step()

        self.run_step_closures()

        self._param_names = set()

    def on_run_end(self):
        # pylint: disable=import-error
        from torch._lazy.closure import AsyncClosureHandler

        async_closure_handler = AsyncClosureHandler()
        if async_closure_handler._closure_queue.qsize() > 0:
            self.logger.info("Waiting for async closures to finish running")
            async_closure_handler._closure_queue.join()

    def on_batch_start(self, batch):
        batch = super().on_batch_start(batch)

        # Clear amp cache for the next iteration
        # pylint: disable=protected-access
        _amp_state.handle._clear_cache()

        def set_tensor_name(tensors: list, names_generator, is_param):
            for name, tensor in names_generator(tensors):
                # pylint: disable=protected-access,c-extension-no-member
                if cerebras_pytorch_lib.set_parameter_name(tensor, name):
                    if is_param:
                        self._param_names.add(name)
                elif self.run_context.activation_steps == 1:
                    raise RuntimeError(
                        f"Failed to set name \"{name}\" for tensor: "
                        f"{cerebras_pytorch_lib.get_tensor_info(tensor)}"
                    )
                else:
                    # We have a case when some of the tensors in state dict are not accessable
                    # because they store some intermediate lazy tensor but not model parameter.
                    # This is the case for `lr` tensor which we set on every lr_scheduler step and
                    # in case activation frequency > 1 we skip `update_groups` step closure which
                    # sets the CPU `lr` tensor to the optimizer.param_group.
                    self.logger.debug(
                        f"Tensor: ({name}) {cerebras_pytorch_lib.get_tensor_info(tensor)} is not "
                        f"accessible at iteration {self.run_context.user_iteration}"
                    )

        set_tensor_name(batch, self._generate_input_names, False)
        set_tensor_name(self.state_dict(), self._generate_state_names, True)

        return batch

    def on_batch_end(self):
        for optimizer in self.optimizer_registry:
            for lr_scheduler in optimizer._lr_scheduler_registry:
                # The lr_scheduler step should always be one greater than the optimizer
                # step if the lr_scheduler was stepped.
                # If the lr_scheduler was not stepped, we still need to update the group
                # with the scalar values.
                # If an lr_scheduler was not stepped, its probably a user error.
                # But we should still support this behaviour anyways as its
                # supported in eager mode
                if optimizer._step_count >= lr_scheduler._step_count:
                    lr_scheduler.update_groups(lr_scheduler._last_lr)

        for name, tensor in self._generate_state_names(self.state_dict()):
            if name not in self._param_names:
                continue
            # The following set_alias call also marks the tensor as an output.
            # pylint: disable=protected-access,c-extension-no-member
            assert cerebras_pytorch_lib.set_alias(tensor, name), (
                f"failed to set alias {name} for tensor: "
                f"{cerebras_pytorch_lib.get_tensor_info(tensor)}"
            )

        self._is_tracing = False

        # pylint: disable=protected-access
        if self.retrace_every_iteration or self.run_context.is_initial_step:
            torch._lazy.mark_step()

        # Update the profiler as we have processed a batch. Note that this is
        # done after mark_step so that we don't jump the gun and updated samples
        # processed before compile/execute is actually done.
        if self.run_context.profiler is not None:
            self.run_context.profiler.step(
                self.run_context.dataloader.batch_size
            )

        self.run_step_closures()

        # Clear activations for the next step
        self.activations.clear()

    def setup_model(self, model):
        super().setup_model(model)

    def forward(self, model, *args, **kwargs):  # pylint: disable=no-self-use
        """Runs the forward pass for the model"""
        return model(*args, **kwargs)

    def set_scope_name(self, scope_name):
        old_scope = super().set_scope_name(scope_name)
        if scope_name is None:
            scope_name = ScopeName()
        cerebras_pytorch_lib.set_scope_name(str(scope_name))
        return old_scope

    ###################################################
    #               Training Loop hooks               #
    ###################################################

    def pre_backward(self, loss):
        """Run just before the call to loss.backward()"""
        if self.grad_scaler is not None:
            self.mark_output({"grad_scalar": self.grad_scaler.state_dict()})
        return loss

    #######################################################
    #               Optimizer related hooks               #
    #######################################################

    def setup_optimizer(self, optimizer):
        super().setup_optimizer(optimizer)
        self.post_optimizer_load_state_dict(optimizer)

    def post_optimizer_load_state_dict(self, optimizer):
        def tensor_cast(value):
            if isinstance(value, torch.Tensor) and value.device.type == "lazy":
                # When we load the optimizer state dict, tensors are moved to
                # device. But we don't want to trace param groups. So we move
                # them back to CPU here.
                value = lazy_tensor_data_wrapper(value).to("cpu")
            elif isinstance(value, int):
                value = torch.tensor(value, dtype=torch.int32)
            elif isinstance(value, float):
                value = torch.tensor(value, dtype=torch.float32)
            elif isinstance(value, (list, tuple)):
                value = type(value)(map(tensor_cast, value))
            return value

        # Convert all python scalars in the param groups to 32 bit torch tensors
        # This is because python int/float are represented as 64-bit scalars,
        # whereas compile can only handle 32-bit scalars.
        for param_group in optimizer.param_groups:
            keys = list(param_group.keys())
            for key in keys:
                if key == "params":
                    continue
                value = param_group.pop(key)
                param_group[key] = tensor_cast(value)

        # Make optimizer state tensors into appliance tensors. When we load a
        # normal torch checkpoint, it's loaded onto CPU. But optimizer state
        # needs to be on the device. Note that loading an optimizer state dict
        # replaces the state variables. This is in constrast to loading a model
        # state dict, which updates the state variables using `param.copy_()`.
        def make_appliance(value):
            if isinstance(value, torch.Tensor) and value.device.type != "lazy":
                return value.to(self.device.torch_device)
            return None

        with self.device:
            optimizer.visit_state(make_appliance)

    def pre_optimizer_step(self, optimizer):
        """Set of actions before the optimizer step has been performed"""
        super().pre_optimizer_step(optimizer)

        # pylint: disable=protected-access
        # Set the lr value to be the tensor
        for lr_scheduler in optimizer._lr_scheduler_registry:
            lr_scheduler.update_last_lr()

    def setup_grad_scaler(self, grad_scaler):
        super().setup_grad_scaler(grad_scaler)

        with self.device:
            state_dict = {
                name: tensor.to(self.torch_device)
                if isinstance(tensor, torch.Tensor)
                else tensor
                for name, tensor in grad_scaler.state_dict().items()
            }
        grad_scaler.load_state_dict(state_dict)

    def _get_cpu_tensor(self, arg: torch.Tensor):
        """Get a CPU tensor from the appliance"""
        # pylint: disable=c-extension-no-member
        name = cerebras_pytorch_lib.get_tensor_name(arg)

        if name not in self.activations:
            if cerebras_pytorch_lib.is_weight_tensor(arg):
                raise RuntimeError(
                    f"Attempting to get weight tensor \"{name}\" with info "
                    f"{cerebras_pytorch_lib.get_tensor_info(arg)} in a step "
                    f"closure but this is not supported yet. Please use "
                    f"\"cstorch.save()\" API to save model weights."
                )
            else:
                tensor = self.appliance.receive_output(
                    self.run_context.iteration, name
                )
                try:
                    # Make the tensor writable so that we don't have to copy it
                    # in `cstorch.from_numpy()`. Some arrays cannot be modified
                    # so we ignore the error and copy the array instead.
                    tensor.flags.writeable = True
                except Exception:  # pylint: disable=broad-except
                    pass

            self.activations[name] = cstorch.from_numpy(tensor)

        return self.activations[name]

    def set_attribute(
        self,
        tensor: torch.Tensor,
        attribute: str,
        value: Union[bool, int, float, str, list, dict],
    ):
        """
        Adds an attribute to the traced tensor at compile time to communicating
        with the Cerebras Compiler Stack.

        Args:
            tensor: A tensor on the backend device.
            attribute: Name of the attribute to set
            value: Value of the attribute to set.
        """

        # These attributes eventally land in MLIR attributes, potentially on
        # the arguments to the main function. MLIR requires such attributes be
        # scoped to a dialect, so ensure the attribute name is prefixed with
        # `cs.`
        name = "cs." + attribute

        from cerebras_pytorch.lib import cerebras_pytorch_lib

        cerebras_pytorch_lib.set_attribute(tensor, name, value)

    #################################################
    #               Appliance related               #
    #################################################

    def add_step_closure(
        self,
        closure,
        args,
        kwargs,
        run_async: bool = False,
        repeat: bool = False,
    ):
        if hasattr(closure, "__wrapped__"):
            pos_arg_names = inspect.getfullargspec(closure.__wrapped__).args
        else:
            pos_arg_names = inspect.getfullargspec(closure).args

        if len(pos_arg_names) == len(args) and not any(
            pos_arg_name in kwargs for pos_arg_name in pos_arg_names
        ):
            # Use the names of the positional arguments in the step closure as
            # the output name.
            kwargs.update(dict(zip(pos_arg_names, args)))
            kwargs = self.mark_output(kwargs, force=True)
            # Strip positional arguments back out
            args = type(args)(
                kwargs.pop(arg_name) for arg_name in pos_arg_names
            )
        else:
            # Use anonymous positional arguments
            args, kwargs = self.mark_output((args, kwargs), force=True)

        self.step_closures.append((closure, args, kwargs, run_async, repeat))

    def run_step_closures(self):
        step_closures = self.step_closures
        self.step_closures = []

        if self.compile_only or self.validate_only:
            self.logger.debug(
                f"Skipping runnning step closures since backend is configured "
                f"for {'compile' if self.compile_only else 'validate'}_only "
                f"mode."
            )
            return

        # pylint: disable=import-error
        from torch._lazy.closure import AsyncClosureHandler

        async_closure_handler = AsyncClosureHandler()

        for closure, args, kwargs, run_async, repeat in step_closures:
            if self.run_context.is_activation_step:
                # fetching tensors from appliance here
                # pylint: disable=protected-access
                cpu_args, cpu_kwargs = torch.utils._pytree.tree_map(
                    lambda arg: (
                        self._get_cpu_tensor(arg)
                        if isinstance(arg, torch.Tensor)
                        and arg.device.type == self.torch_device.type
                        else arg
                    ),
                    (args, kwargs),
                )

                if run_async:
                    async_closure_handler.run(
                        lambda c=closure, a=cpu_args, k=cpu_kwargs: c(*a, **k)
                    )
                else:
                    closure(*cpu_args, **cpu_kwargs)
            else:
                self.logger.trace(
                    f"Skipping step closure at iteration {self.run_context.user_iteration} as it "
                    f"is not an activation step."
                )

            if repeat:
                self.step_closures.append(
                    (closure, args, kwargs, run_async, repeat)
                )

    def save(self, state_dict, checkpoint_file):
        saver = PyTorchH5Saver(max_store=self.config.max_checkpoints)
        flattened, spec = saver.flatten_state_dict(state_dict)
        # save the spec before saving tensors so we know what was
        # intended to be saved, even if something fails
        saver.save_spec(checkpoint_file, spec)

        if not self.data_executor_stack or self.run_context.is_pre_initial_step:
            # If we are on the first step, we don't need to fetch the
            # tensor from the appliance since it is already the initial
            # tensor value (initial weights).
            # pylint: disable=protected-access,c-extension-no-member
            for key, val in flattened.items():
                if isinstance(val, torch.Tensor):
                    val = lazy_tensor_data_wrapper(val)
                saver.save_tensor(checkpoint_file, key, val)
        else:
            self.appliance.save_weights(
                flattened.items(), checkpoint_file, self.run_context.iteration,
            )
        saver.update_ckpt_info(checkpoint_file)

        # Now do some verification that all the tensors in spec were saved
        saved_tensors = PyTorchH5Saver.tensor_names(checkpoint_file)
        missing = set(flattened.keys()) - set(saved_tensors)

        if (
            self.data_executor_stack
            and not self.run_context.is_pre_initial_step
        ):
            # Don't throw an error for known skipped weights
            missing -= set(self.appliance.skipped_weights)

        if missing:
            missing = ', '.join(missing)
            extras = ", ".join(set(saved_tensors) - set(flattened.keys()))
            if extras:
                extra_str = (
                    f"\nUnexpected weights found in checkpoint are: "
                    f"{extras}."
                )
            else:
                extra_str = ""
            raise RuntimeError(
                f"Not all weights from the state dict were saved to the "
                f"checkpoint file `{checkpoint_file}`. This may point to "
                f"an internal error."
                f"\nWeights missing in checkpoint are: {missing}."
                f"{extra_str}"
            )

    def run_implicit_autoregressive_loop(
        self,
        input_tensor: torch.IntTensor,
        output_tensor: torch.IntTensor,
        loop_dim: int,
        start_token: Union[int, List[int]],
        stop_token: Union[int, List[int]],
        max_tokens: Optional[int] = None,
    ) -> torch.IntTensor:
        """
        Experimental implcit autoregressive loop. Configures the runtime inner
        loop via attributes.
        """
        if not isinstance(input_tensor, torch.Tensor):
            raise TypeError(
                f"Expected input_tensor to be a torch Tensor. "
                f"Got: {type(input_tensor)}"
            )
        if not isinstance(output_tensor, torch.Tensor):
            raise TypeError(
                f"Expected output_tensor to be a torch Tensor. "
                f"Got: {type(output_tensor)}"
            )

        if not isinstance(loop_dim, int):
            raise TypeError(
                f"loop_dim must be an integer. Got: {type(loop_dim)}"
            )
        elif not ((1 - input_tensor.dim()) <= loop_dim < input_tensor.dim()):
            raise ValueError(
                f"Expected {1 - input_tensor.dim()} <= loop_dim < "
                f"{input_tensor.dim()}. Got: {loop_dim}"
            )
        if loop_dim < 0:
            loop_dim = input_tensor.dim() - loop_dim
            # This is a sanity check
            assert loop_dim >= 0

        NNI = "must be non-negative integer or list of non-negative integers."
        if isinstance(start_token, list):
            if len(start_token) == 0:
                raise ValueError(f"start_token {NNI} Got empty list")
            for t in start_token:
                if not isinstance(t, int) or t < 0:
                    raise ValueError(f"start_token {NNI} One element was {t}")
        elif not isinstance(start_token, int) or start_token < 0:
            raise ValueError(f"start_token {NNI} Got: {start_token}")
        else:
            start_token = [start_token]

        if isinstance(stop_token, list):
            if len(stop_token) == 0:
                raise ValueError(f"stop_token {NNI} Got empty list")
            for t in stop_token:
                if not isinstance(t, int) or t < 0:
                    raise ValueError(f"stop_token {NNI} One element was {t}")
        elif not isinstance(stop_token, int) or stop_token < 0:
            raise ValueError(f"stop_token {NNI} Got: {stop_token}")
        else:
            stop_token = [stop_token]

        if (
            max_tokens is not None
            and not isinstance(max_tokens, int)
            or max_tokens < 0
        ):
            raise ValueError(
                f"max_tokens must be a non-negative integer. Got: {max_tokens}"
            )

        autoregressive = {}
        for name, value in (
            ("loop_dim", loop_dim),
            ("start_token", start_token),
            ("stop_token", stop_token),
            ("max_tokens", max_tokens),
        ):
            if value is not None:
                autoregressive[name] = value
            elif name != "max_tokens":
                raise ValueError(
                    f"Expected {name} to be an integer but got None"
                )
        self.set_attribute(input_tensor, "autoregressive", autoregressive)

        input_name = cerebras_pytorch_lib.get_tensor_name(input_tensor)
        output_name = input_name.replace("input", "autoregressive", 1)
        output_tensor = cerebras_pytorch_lib.mark_output_tensor(
            output_tensor, output_name, force=True
        )
        assert cerebras_pytorch_lib.set_alias(
            output_tensor, input_name, is_weight=False
        ), "Failed to set alias between output and input for autoregressive loop"
        return output_tensor

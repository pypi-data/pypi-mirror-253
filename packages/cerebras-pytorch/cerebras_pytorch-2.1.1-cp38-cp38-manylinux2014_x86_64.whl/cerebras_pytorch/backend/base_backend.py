# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

""" Contains the abstract base backend class """
import contextlib
import os
import time
from abc import ABC, abstractmethod
from collections import OrderedDict, defaultdict
from dataclasses import dataclass
from functools import cached_property, wraps
from pathlib import Path
from types import MethodType
from typing import Dict, Literal, Optional, Union
from warnings import warn

import torch
from tqdm import tqdm

import cerebras_pytorch.metrics as metrics
from cerebras_appliance import DEFAULT_COMPILE_DIR
from cerebras_appliance.CSConfig import CSConfig
from cerebras_appliance.log import ClassLogger, named_class_logger
from cerebras_appliance.utils import CurrentTracker, Tracker
from cerebras_pytorch.backend import BackendType
from cerebras_pytorch.core.device import Device
from cerebras_pytorch.core.modes import EVAL, TRAIN
from cerebras_pytorch.core.name_scope import (
    ScopeName,
    add_debug_name,
    get_debug_name,
)
from cerebras_pytorch.utils.nest import visit_torch_tensors

COMPILE_ONLY_MSG = "Compiling the model. This may take a few minutes."
COMPILE_SUCCESS_MSG = "Compile was successful!"
PROGRAMMING_CS_MSG = (
    "Programming Cerebras Wafer Scale Cluster for execution. "
    "This may take a few minutes."
)


@named_class_logger
class BaseBackend(ABC, ClassLogger):
    """
    The abstract base backend.
    Contains the logic common to all backends.
    """

    @dataclass
    class Config:
        """Dataclass with all configurable backend options"""

        artifact_dir: str = "./"
        compile_dir: str = DEFAULT_COMPILE_DIR
        compile_only: bool = False
        validate_only: bool = False
        max_checkpoints: Optional[int] = None
        log_initialization: bool = True
        use_cs_grad_accum: bool = True
        micro_batch_size: Optional[Union[int, Literal["explore"]]] = None

    # pylint: disable=super-init-not-called
    def __init__(self, backend_type: BackendType, device: Device):
        self.backend_type = backend_type
        self.device = device

        self.config = BaseBackend.Config()

        self.mode = None

        self.input_fn = None
        self.input_fn_params = None

        self.model: Optional[torch.nn.Module] = None
        self.optimizer_registry = []
        self.grad_scaler = None

        self.model_params_duplicates_map = None

        self.data_executor_stack = []

        self.current_scope_name = ScopeName()

        # queue of step closures
        self.step_closures = []

        # detached here means that the metric is not a part of any module
        # and needs to be handled separately
        self.detached_metrics: Optional[torch.nn.Module] = None

        # progress tracker
        self._progress_tracker = None

        # flag to indicate if we're in tracing mode
        self._is_tracing = False

        # flag to indicate whether we should allow retracing
        self._retrace_every_iteration = True

        # For debug_names that are invoked multiple times in the model's
        # forward(), this tracks the call number and is reset each batch.
        self._debug_name_call_counters = defaultdict(int)
        self._pre_fwd_scope_names = defaultdict(list)

    # alias properties from backend type
    is_cpu = property(lambda self: self.backend_type.is_cpu)
    is_gpu = property(lambda self: self.backend_type.is_gpu)
    is_csx = property(lambda self: self.backend_type.is_csx)

    @property
    def artifact_dir(self):  # pylint: disable=no-self-use
        """Returns the artifact directory"""
        return self.config.artifact_dir

    @property
    def retrace_every_iteration(self) -> bool:
        """
        If True, retrace the compute graph every iteration.
        If False, trace only once.
        """
        return self._retrace_every_iteration

    @property
    def is_tracing(self) -> bool:
        """Returns True if the backend is currently tracing the model."""
        return self._is_tracing

    @property
    def compile_only(self):
        """Returns True if compile only is set to True in the config"""
        return self.config.compile_only

    @property
    def validate_only(self):
        """Returns True if validate only is set to True in the config"""
        return self.config.validate_only

    @property
    def is_e2e_execution(self) -> bool:
        """Returns True if the backend is configured for end-to-end execution"""
        return not (self.compile_only or self.validate_only)

    @property
    def torch_device(self) -> torch.device:
        """Returns the corresponding torch device"""
        return self.device.torch_device

    @property
    def in_run_context(self):
        return len(self.data_executor_stack) > 0

    @property
    def data_executor(self):
        """
        Get the current data executor which will be used to configure the
        appliance run
        """
        if len(self.data_executor_stack) == 0:
            raise RuntimeError(
                "Detected that a data executor was not used.\n"
                "Please wrap your dataloader in a Cerebras DataExecutor:\n\n"
                "\texecutor = cstorch.utils.data.DataExecutor(dataloader, ...)\n\n"
                "Which can be used in the execution loop as follows:\n\n"
                "\tfor i, batch in enumerate(executor):\n\t\t...\n\n"
                "For more details, please see the documentation for "
                "cstorch.utils.data.DataExecutor."
            )

        return self.data_executor_stack[-1]

    @property
    def run_context(self):
        """
        Get the current run context which will be used to configure the
        appliance run
        """
        return self.data_executor.run_context

    @property
    def cs_config(self) -> CSConfig:
        """Get the current CSConfig which will be passed to the appliance"""
        return self.run_context.cs_config

    @property
    def progress_tracker(self) -> tqdm:
        """Used to update users on the progress of weight initialization"""
        if self._progress_tracker is None and self.config.log_initialization:
            self._progress_tracker = tqdm(
                ncols=0, bar_format="{desc}[{elapsed}{postfix}]"
            )

        return self._progress_tracker

    @cached_property
    def appliance_tracker(self) -> Tracker:
        key = "compile" if self.config.compile_only else "execute"
        _artifact_dir = Path(self.config.artifact_dir)
        if _artifact_dir.parent.parent.name == "cerebras_logs":
            track_dir = str(_artifact_dir.parent.parent.joinpath("track"))
        else:
            track_dir = str(_artifact_dir.joinpath("track"))
        os.makedirs(track_dir, exist_ok=True)
        return CurrentTracker.get_tracker(
            file_name=os.path.join(track_dir, f"{key}_{time.time()}.json"),
            key=key,
        )

    def move_to_device(self, struct):
        """Moves all tensors in the provided structure to the torch device"""
        return self.device.move_to_device(struct)

    def state_dict(self) -> Dict[str, Dict[str, torch.Tensor]]:
        """State dict of the backend that contains all state tensors.

        This method is not to be used with checkpoints and is mainly for marking
        tensors as outputs/aliases of the model.
        """
        s = {}
        if self.model is not None:
            s["model"] = full_state_dict(self.model)

        # pylint: disable=protected-access
        if len(self.optimizer_registry) == 1:
            optimizer = self.optimizer_registry[0]
            s["optimizer"] = optimizer.state_dict()
            s["lr_scheduler"] = [
                lr_scheduler.state_dict()
                for lr_scheduler in optimizer._lr_scheduler_registry
            ]
        else:
            s["optimizers"] = []
            for o in self.optimizer_registry:
                state_dict = o.state_dict()
                state_dict["lr_scheduler"] = [
                    lr_scheduler.state_dict()
                    for lr_scheduler in o._lr_scheduler_registry
                ]
                s["optimizers"].append(state_dict)

        if self.grad_scaler is not None:
            s["grad_scaler"] = self.grad_scaler.state_dict()

        if self.detached_metrics is not None:
            s["metrics"] = full_state_dict(self.detached_metrics)

        return s

    def setup_model(self, model):
        """
        Moves the model to the torch device and tracks the duplicate tensors
        """
        self.model = model

        # Set the backend's mode via calls to model.train and model.eval
        model_train = self.model.train

        @wraps(model_train)
        def _train(_self, is_training: bool = True):
            self.mode = TRAIN if is_training else EVAL
            self.logger.debug(f"Setting mode to {self.mode}")
            return model_train(is_training)

        self.model.train = MethodType(_train, self.model)

        def named_members(model, get_member_fn, prefix=""):
            """
            Helper method which returns a map of param_name -> set of duplicate param names
            """
            memo = dict()  # dict from tensor -> str name of tensor
            names = defaultdict(
                set
            )  # dict from str name of tensor -> set of duplicates
            modules = model.named_modules(prefix=prefix, remove_duplicate=False)
            for module_prefix, module in modules:
                for k, v in get_member_fn(module):
                    if v is None:
                        continue

                    name = module_prefix + ('.' if module_prefix else '') + k
                    if v in memo:
                        # whenever a duplicate is found
                        # update the existing list of duplicate
                        # names corresponding to the first name
                        names[memo[v]] |= {memo[v], name}
                        # also add a key for new name with
                        # value as the duplicates list
                        names[name] = names[memo[v]]
                    else:
                        memo[v] = name

            return names

        # pylint: disable=protected-access
        # set duplicate params for params and buffers in the model
        self.model_params_duplicates_map = named_members(
            model, lambda module: module._parameters.items()
        )
        self.model_params_duplicates_map.update(
            named_members(model, lambda module: module._buffers.items())
        )

        self.move_to_device(model)
        model.device = self.torch_device

        # Add _debug_name attribute to module and its children
        add_debug_name(model)

        def retie_weights(module, scope, duplicates_map):
            # pylint: disable=protected-access
            for tensor_dict in (module._parameters, module._buffers):
                tensor_names = list(tensor_dict.keys())
                for name in tensor_names:
                    tensor_name = ".".join(scope + [name])
                    if tensor_name not in self.model_params_duplicates_map:
                        continue

                    if tensor_name in duplicates_map:
                        setattr(module, name, duplicates_map.pop(tensor_name))
                        continue

                    for duplicate_name in self.model_params_duplicates_map[
                        tensor_name
                    ]:
                        duplicates_map[duplicate_name] = tensor_dict[name]

            for name, child in module.named_children():
                retie_weights(child, scope + [name], duplicates_map)

        if self.model_params_duplicates_map:
            retie_weights(model, [], {})

        self._add_name_scope_hooks()

    def _add_name_scope_hooks(self):
        # Helper for hooks
        def get_name(module, counter_increment=0):
            # TODO: need to reset _num_instances on batch start. Otherwise we will get
            # different names between itertions.
            name = get_debug_name(module)

            counter = self._debug_name_call_counters[name]
            self._debug_name_call_counters[name] += counter_increment
            if counter:
                name = f"{name}.call{counter}"
            return name

        def fwd_pre_name_scope(
            module, inputs
        ):  # pylint: disable=redefined-builtin
            scope_name = ScopeName(get_name(module), "fwd")
            self._pre_fwd_scope_names[module].append(
                self.set_scope_name(scope_name)
            )

        def fwd_post_name_scope(
            module, input, output
        ):  # pylint: disable=redefined-builtin
            # Exit FWD scope
            # Restore name_scope we saved during `fwd_pre_name_scope`
            pre_fwd_scopes = self._pre_fwd_scope_names[module]
            pre_fwd_scope = ScopeName()
            if pre_fwd_scopes:
                pre_fwd_scope = pre_fwd_scopes.pop()
            self.set_scope_name(pre_fwd_scope)

            # Set up the BWD scope.

            # This will actually be the name for the bwd pass entered from
            # the module's output's grad hook.
            # Also, increment the counter for the next fwd_pre to hit.
            bwd_name_scope = ScopeName(get_name(module, 1), "bwd")

            for _, tensor in visit_torch_tensors(output):
                # In case a module returns a tensor unmodifed, don't change its
                # scope.
                has_bwd_name_scope = getattr(
                    tensor, "_has_bwd_name_scope", False
                )
                if tensor.requires_grad and not has_bwd_name_scope:
                    # pylint: disable=protected-access
                    tensor._has_bwd_name_scope = True

                    def hook(x):
                        self.set_scope_name(bwd_name_scope)

                    tensor.register_hook(lambda x: hook(x))

        from torch.nn.modules import module

        module.register_module_forward_pre_hook(fwd_pre_name_scope)
        module.register_module_forward_hook(fwd_post_name_scope)

    def set_scope_name(self, scope_name: ScopeName) -> ScopeName:
        """ Set new scope name and return the old one """
        old_name = self.current_scope_name
        self.current_scope_name = scope_name or ScopeName()
        return old_name

    def serialize_input_fn(self, input_fn, input_fn_params):
        """Save the input function and its args/kwargs for serialization"""
        self.input_fn = input_fn
        self.input_fn_params = input_fn_params

    def on_run_start(self):  # pylint: disable=no-self-use
        """Runs once at the beginning of the run

        Used by cstorch.utils.data.DataLoader
        """
        self._setup_optimizers()
        self._setup_detached_metrics()

        # Clean up the progress bar if it exists
        if self._progress_tracker is not None:
            self._progress_tracker.close()
            self._progress_tracker = None

    def on_run_end(self):  # pylint: disable=no-self-use
        """Runs once at the end of the run"""

    def on_batch_start(self, batch):
        """Used by cstorch.utils.data.DataExecutor"""

        # Clear debug_name call counters.
        self._debug_name_call_counters = defaultdict(int)
        self._pre_fwd_scope_names = defaultdict(list)

        batch_on_device = self.move_to_device(batch)
        self._is_tracing = True
        return batch_on_device

    def on_batch_end(self):
        """Used by cstorch.utils.data.DataExecutor"""
        self._is_tracing = False

        # Update the profiler as we have processed a batch. Note that this is
        # done after mark_step so that we don't jump the gun and updated samples
        # processed before compile/execute is actually done.
        if self.run_context.profiler is not None:
            self.run_context.profiler.step(
                self.run_context.dataloader.batch_size
            )

        self.run_step_closures()

    def mark_output(self, struct, force=False):  # pylint: disable=no-self-use
        """Marks the tensors in the struct as outputs of the model"""

    def forward(self, model, *args, **kwargs):  # pylint: disable=no-self-use
        """Runs the forward pass for the model"""
        return model(*args, **kwargs)

    def pre_backward(self, loss):  # pylint: disable=no-self-use
        """Run just before the call to loss.backward()"""
        return loss

    @contextlib.contextmanager
    def name_scope(self, name: str):
        """Context manager for setting the name scope for the current context"""
        old_name = self.set_scope_name(ScopeName(name))
        yield
        self.set_scope_name(old_name)

    def register_optimizer(self, optimizer):
        """
        Adds the optimizer to the registry to be wrapped when a run starts.
        """
        # Need to keep track of optimizers for amp loss scaling
        self.optimizer_registry.append(optimizer)

        # pylint: disable=protected-access
        optimizer._lr_scheduler_registry = []

    def unregister_optimizer(self, optimizer):
        """
        Removes a previously registered optimizer.
        """
        if optimizer in self.optimizer_registry:
            self.optimizer_registry.remove(optimizer)

    def _setup_optimizers(self):
        for optimizer in self.optimizer_registry:
            if getattr(optimizer, "_cstorch_setup", False):
                # Don't double setup.
                continue
            # pylint: disable=protected-access
            optimizer._cstorch_setup = True

            self.setup_optimizer(optimizer)

    def setup_optimizer(self, optimizer):
        """
        Wraps an optimizer in the registry with zero_grad/step to be used in
        the cstorch.GradScaler.
        """

        optimizer_zero_grad = optimizer.zero_grad
        optimizer_step = optimizer.step

        @wraps(optimizer_zero_grad)
        def wrapped_optimizer_zero_grad(_self, set_to_none: bool = True):
            # This is only needed in PyTorch versions < 2.0
            # TODO: Remove this when we drop support for PyTorch/XLA
            self.pre_optimizer_zero_grad(optimizer, set_to_none)
            return optimizer_zero_grad(set_to_none)

        @wraps(optimizer_step)
        def wrapped_optimizer_step(_self, *args, **kwargs):
            with self.name_scope("optimizer"):
                self.pre_optimizer_step(optimizer)
                output = optimizer_step(*args, **kwargs)
                self.post_optimizer_step(optimizer)
                return output

        optimizer.zero_grad = MethodType(wrapped_optimizer_zero_grad, optimizer)
        optimizer.step = MethodType(wrapped_optimizer_step, optimizer)

    def post_optimizer_load_state_dict(self, optimizer):
        """
        Post-process the optimizer param groups and state
        after loading the state dict
        """

    def pre_optimizer_zero_grad(  # pylint: disable=no-self-use
        self, optimizer, set_to_none: bool = True
    ):
        """
        Checks that `set_to_none` is set to True and raises a warning otherwise
        """
        if not set_to_none:
            warn(
                "Calling optimizer.zero_grad(set_to_none=False) can prevent "
                "the construction of a static graph which can cause multiple "
                "compiles"
            )

    def pre_optimizer_step(self, optimizer):  # pylint: disable=no-self-use
        """ Action to perform just before optimizer step is called"""

    def post_optimizer_step(self, optimizer):
        """ Action to perform just after optimizer step is called"""
        # The fact that we performed an optimizer step must mean that we are training
        if self.mode == EVAL:
            warn(
                "Detected a call to model.eval() as well as a call to "
                "optimizer.step(). If you are intending to train the model, "
                "please call model.train() instead of model.eval(). If you "
                "are not intending to train the model, please remove the call "
                "to optimizer.step()."
            )
        self.mode = TRAIN
        self.logger.debug(
            "Setting mode to train as optimizer.step() was called."
        )

    def setup_lr_scheduler(self, lr_scheduler):  # pylint: disable=no-self-use
        """Set up the learning rate scheduler """
        # pylint: disable=protected-access
        optimizer = lr_scheduler.optimizer
        if lr_scheduler not in optimizer._lr_scheduler_registry:
            # Only add the lr_scheduler if it hasn't already been added
            optimizer._lr_scheduler_registry.append(lr_scheduler)

        lr_scheduler.device = self.torch_device
        with self.device:
            if not isinstance(lr_scheduler.last_epoch, torch.Tensor):
                # The tensor representation of last_epoch
                lr_scheduler.last_epoch = torch.tensor(
                    lr_scheduler.last_epoch, dtype=torch.int64
                )

            lr_scheduler.last_epoch = lr_scheduler.last_epoch.to(
                self.torch_device
            )

    def setup_grad_scaler(self, grad_scaler):
        """ Set up the grad scaler """
        self.grad_scaler = grad_scaler

    def _setup_detached_metrics(self):
        """Find all detached metrics."""

        attached_metrics = set()
        if self.model is not None:
            for submodule in self.model.modules():
                if isinstance(submodule, metrics.Metric):
                    attached_metrics.add(id(submodule))

        # Compile replaces "/" with "_" in parameters, so we need to do the same
        # here to avoid mismatches
        self.detached_metrics = torch.nn.ModuleDict(
            {
                metric_name.replace("/", "_"): torch.nn.ModuleList(
                    filter(
                        lambda metric: id(metric) not in attached_metrics,
                        metric_list,
                    )
                )
                for metric_name, metric_list in metrics.Metric.registry.items()
            }
        )

        self.move_to_device(self.detached_metrics)

    def set_attribute(
        self,
        tensor: torch.Tensor,
        attribute: str,
        value: Union[bool, int, float, str, list, dict],
    ):
        """
        On supported backends, adds an attribute to the traced tensor at
        compile time to communicating with the Cerebras Compiler Stack.
        """

    def add_step_closure(
        self,
        closure,
        args,
        kwargs,
        run_async: bool = False,
        repeat: bool = False,
    ):
        """
        Adds the provided function to a queue of closures to be run at the end
        of the step
        """
        if run_async:
            self.logger.warning(
                f"Asynchronous step closures not supported by "
                f"{self.backend_type} backend. "
                f"Will run `{closure.__name__}` synchronously"
            )

        # There is no guarantee that the tensors in args and kwargs aren't
        # mutated in place after being added to a step closure. To avoid reading
        # future values when the step closure runs, we pass a copy of the tensor
        # to the closure.
        args, kwargs = torch.utils._pytree.tree_map_only(
            torch.Tensor, lambda t: t.detach().clone(), (args, kwargs)
        )

        self.step_closures.append((closure, args, kwargs, repeat))

    def run_step_closures(self):  # pylint: disable=no-self-use
        """ Run all the queued closures """
        step_closures = self.step_closures
        self.step_closures = []

        for closure, args, kwargs, repeat in step_closures:
            closure(*args, **kwargs)

            if repeat:
                self.step_closures.append((closure, args, kwargs, repeat))

    def run_implicit_autoregressive_loop(
        self,
        input_tensor: torch.IntTensor,
        output_tensor: torch.IntTensor,
        loop_dim: int,
        start_token: int,
        stop_token: int,
        max_tokens: Optional[int] = None,
    ):
        """ Experimental implcit autoregressive loop. """
        raise NotImplementedError(
            "Implicit autoregressive loop is not supported on "
            f"{self.backend_type} backend"
        )

    @abstractmethod
    def save(self, state_dict, checkpoint_file):  # pylint: disable=no-self-use
        """
        Save the provided state dict to a checkpoint at the provided filepath
        """

    # Distributed Data Parallel
    def spawn(self, func):  # pylint: disable=no-self-use
        """Spawns a process on each GPU

        Raises:
            A RuntimeError if called on a non-GPU backend
        """
        raise RuntimeError("Spawning is only supported on GPU backends")


def full_state_dict(module: torch.nn.Module) -> Dict[str, torch.Tensor]:
    """Returns the full state dict of a module, including persistent buffers.

    This helper method is used to collect all buffers, parameters, and other
    extra states of a module, mostly for marking them as outputs/aliases in
    the graph. It is not to be used for checkpointing.
    """
    if not isinstance(module, torch.nn.Module):
        raise TypeError(f"Expected a torch.nn.Module, got {type(module)}")

    # Persistent buffers are not included in the state dict but we need
    # to mark them as outputs/aliases, otherwise they won't show up in
    # the graph. `named_buffers` returns all buffers (including
    # non-persistent ones). Updating with `state_dict` will override
    # non-persistent buffers again with the same name, which is ok.
    state_dict = OrderedDict(module.named_buffers())
    state_dict.update(module.state_dict(keep_vars=True))
    return state_dict

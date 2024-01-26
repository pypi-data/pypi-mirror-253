# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Cerebras device class"""
import atexit
import os
import sys
from functools import cached_property, wraps
from pathlib import Path
from shutil import rmtree
from tempfile import mkdtemp
from types import MethodType
from typing import List
from warnings import warn
from weakref import finalize

import torch
import tqdm
from torch.nn.modules.module import (
    register_module_buffer_registration_hook,
    register_module_module_registration_hook,
    register_module_parameter_registration_hook,
)
from torch.utils.hooks import RemovableHandle

import cerebras_pytorch as cstorch
from cerebras_pytorch.backend import current_backend_impl


class Device:
    """Base Cerebras device class"""

    def __init__(self, device_type: str):
        # for cpu and lazy we only have 1 device, and C++/python have
        # different defaults for index (C++ is -1, python is None)
        # the gpu/cuda implementation uses a different torch.device constructor
        self.torch_device = torch.device(device_type, index=0)

    @property
    def artifact_dir(self):
        return current_backend_impl().artifact_dir

    @property
    def type(self):
        """Returns the type of the torch device"""
        return self.torch_device.type

    def move_to_device(self, struct):
        """Moves all tensors in the provided structure to the torch device."""

        def move(tensor):
            if isinstance(tensor, (torch.nn.Module, torch.Tensor)):
                return tensor.to(self.torch_device)
            return tensor

        with self:
            # pylint: disable=protected-access
            return torch.utils._pytree.tree_map(move, struct)

    def __str__(self):
        return str(self.type)

    def __repr__(self):
        return f"device(type='{str(self)}')"

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


class CPUDevice(Device):
    """Cerebras CPU device subclass"""

    def __init__(self):
        super().__init__("cpu")


class GPUDevice(Device):
    """Cerebras GPU device subclass"""

    def __init__(
        self,
        enable_distributed: bool = False,
        dist_backend: str = "nccl",
        init_method: str = None,
    ):
        if not torch.cuda.is_available():
            raise RuntimeError(
                f"GPU was specified as the target device, but "
                f"CUDA is not available. Please make sure you have a "
                f"PyTorch installation with CUDA enabled to run on "
                "GPU"
            )

        if enable_distributed:
            import torch.distributed as dist

            # This environment variable is provided by torchrun
            if "LOCAL_RANK" not in os.environ:
                raise RuntimeError(
                    "Distibuted training was enabled, "
                    "but the script was not run using torchrun. "
                    "Please invoke the training script using torchrun, e.g.\n\n"
                    "\ttorchrun run.py <cli_arguments>"
                )

            dist.init_process_group(
                backend=dist_backend, init_method=init_method
            )

            import logging

            logging.info(
                f"Initialized distributed process group for rank {dist.get_rank()}"
            )

            world_size = dist.get_world_size()
            if world_size == 1:
                warn(
                    "Distributed training was enabled, but only "
                    "1 GPU was detected."
                )
            rank = dist.get_rank()
            self.torch_device = torch.device(rank)
            # call destroy_process_group when the device is destructed
            self._finalizer = finalize(self, dist.destroy_process_group)
        else:
            if torch.cuda.device_count() > 1:
                warn(
                    "Distributed training was not enabled even though "
                    "more than 1 GPU is available."
                )
            self.torch_device = torch.device('cuda')


class LazyDevice(Device):
    """ Cerebras Lazy device subclass """

    def __init__(self):
        super().__init__("lazy")

        from cerebras_pytorch.lib import cerebras_pytorch_lib

        # pylint: disable=c-extension-no-member
        self.config = cerebras_pytorch_lib.appliance_file_config

        self._handles: List[RemovableHandle] = []
        # Number of contexts that have been entered
        self._stack_size = 0

        # The RNG state of the device when the first parameter is registered
        # This is used to restore the RNG state when we lazily initialize
        # the parameters
        # This does assume that the seed is never set in the middle of model
        # initialization. This assumption should hold for most cases, but
        # not all.
        # TODO: Figure out how to capture if seed is set in the middle of
        #       model initialization
        self._rng_state = None

        # If True, clean up any artifacts on clean exit
        # This includes the device data directory and any appliance data
        # files that were created during the run
        # The only time we would want this to be False is when we are
        # inspecting the initial state after a run in a test.
        self._clean_on_exit = True

    @cached_property
    def device_data_dir(self):
        """The directory where data of file-backed tensors are stored"""
        try:
            device_data_dir = Path(
                mkdtemp(prefix="device_data_", dir=self.artifact_dir)
            )

            @atexit.register
            def delete_atexit():
                exc_type, exc_value, traceback = sys.exc_info()
                if exc_type is None and self._clean_on_exit:
                    # Only delete the directory if no exception was raised
                    rmtree(device_data_dir, ignore_errors=True)

            return device_data_dir
        except PermissionError as err:
            raise RuntimeError(
                f"Failed to initialize Cerebras device. "
                f"Please ensure that you have write permissions at "
                f"{self.artifact_dir}"
            ) from err

    def __copy__(self):
        assert self.device_data_dir.exists()
        return super().__copy__()

    def __eq__(self, other):
        return self.device_data_dir == other.device_data_dir

    def __str__(self) -> str:
        return "CSX"

    @cached_property
    def tracker_entry(self):
        return current_backend_impl().appliance_tracker.entry(
            "weight_initialization"
        )

    @property
    def tracker(self) -> tqdm:
        """Returns the progress tracker"""
        return current_backend_impl().progress_tracker

    def reset_parameter_hook(self, module: torch.nn.Module):
        """
        Updates the progress tracker when a module's reset_parameters is called
        """
        # Only wrap when the module has a reset_parameters method which is the
        # default implementation coming from the class. We can't just call
        # getattr(module, "reset_parameters") in the wrapper because that will
        # use the wrong method when the module is deep copied.
        reset_parameters = getattr(module.__class__, "reset_parameters", None)
        if reset_parameters is None or (
            getattr(module, "reset_parameters")
            != MethodType(reset_parameters, module)
        ):
            return

        @wraps(reset_parameters)
        def wrapper(_self, *args, **kwargs):
            if self.tracker is not None:
                self.tracker.set_postfix(
                    note=f"Calling {module.__full_name__}.reset_parameters"
                )
                self.tracker.update()

            return reset_parameters(_self, *args, **kwargs)

        module.reset_parameters = MethodType(wrapper, module)

    def module_hook(self, module, submodule_name, submodule):
        """The hook to run on module registration.

        This hook moves the module parameters to lazy device and wraps them in a
        Cerebras custom parameter. It then creates a CPU view of the data that
        is potentially file-backed and replaces the original parameter with
        the CPU view. As such, further writes to the parameter are directly
        written to (potentially) file and avoid OOM issues.

        Note that we currently don't do the above for module buffers. Buffers
        are typically small and don't cause OOM issues. This may change in the
        future if we encounter issues with buffers.
        """
        if not isinstance(submodule, torch.nn.Module):
            return

        # Set the full name of the module and submodule
        # The full name is comprised of the full structure
        if not hasattr(module, "__full_name__"):
            module.__full_name__ = module.__class__.__name__

        submodule.__full_name__ = f"{module.__full_name__}.{submodule_name}"

        if self.tracker is not None:
            self.tracker.set_description(
                f"Initializing module {submodule.__full_name__}"
            )
            self.tracker.set_postfix(note=f"Initializing parameters")
            self.tracker.update()

        # Move the module parameters to the device
        self._move_module_to_device(submodule)

        if not self.config.drop_data:
            # If the data was not dropped we need to create a CPU view of the data
            for iterator, accessor in [
                (submodule.named_parameters, submodule._parameters),
                (submodule.named_buffers, submodule._buffers),
            ]:
                parameter_names = [name for name, _ in iterator(recurse=False)]

                for param_name in parameter_names:
                    # pylint: disable=protected-access
                    parameter = accessor.pop(param_name)
                    accessor[param_name] = parameter.to("cpu")

                    if self.tracker is not None:
                        self.tracker.set_postfix(
                            note=f"Initialized parameter {param_name}"
                        )
                        self.tracker.update()

                self.reset_parameter_hook(submodule)

    def parameter_hook(self, module, name, param):
        """Wraps parameter in a Cerebras parameter

        Note: Only used if tracing initialization
        """
        if not isinstance(param, cstorch.nn.Parameter):
            assert param.device.type == self.type

            if self._rng_state is None:
                self._rng_state = torch.get_rng_state()

            return cstorch.nn.Parameter(param)
        return param

    def buffer_hook(self, module, name, buffer):
        """Wraps buffer in a Cerebras buffer

        Note: Only used if tracing initialization
        """
        if isinstance(buffer, torch.Tensor) and not isinstance(
            buffer, cstorch.nn.Buffer
        ):
            assert buffer.device.type == self.type

            if self._rng_state is None:
                self._rng_state = torch.get_rng_state()

            return cstorch.nn.Buffer(buffer)
        return buffer

    def move_to_device(self, struct):
        if isinstance(struct, torch.nn.Module):
            with self:
                struct.apply(self._move_module_to_device)
            return struct

        return super().move_to_device(struct)

    def _move_module_to_device(self, module: torch.nn.Module):
        # pylint: disable=protected-access
        for iterator, accessor, cstorch_type in [
            (module.named_parameters, module._parameters, cstorch.nn.Parameter),
            (module.named_buffers, module._buffers, cstorch.nn.Buffer),
        ]:
            parameter_names = [name for name, _ in iterator(recurse=False)]
            for param_name in parameter_names:
                param = accessor.pop(param_name)

                if not isinstance(param, cstorch_type):
                    from cerebras_pytorch.saver.storage import (
                        has_lazy_tensor_data_impl,
                    )

                    if (
                        param.device == self.torch_device
                        and not self.config.lazy_initialization
                    ):
                        # The following applies only during "eager" initialization
                        # Lazy device behaves differently when creating tensors:
                        #   1. cpu_tensor.to("lazy"): This creates a lazy tensor
                        #       backed by device data, which eventually becomes an
                        #       input to the graph.
                        #   2. torch.tensor(..., device="lazy"): This traces the
                        #       creation op and doesn't add an input to the graph.
                        # We expect parameters, which are inputs to the graph, to be
                        # created using the first method on CPU, and then moved to
                        # the device using this hook. This is the general flow as
                        # users are not expected to explicitly pass a device
                        # argument when creating parameters. However, there are
                        # cases where users may want to create a new parameters
                        # using another parameter's device during the initialization
                        # phase. In drop_data mode, since we're tracing
                        # initialization ops, the device argument will be the lazy
                        # device, which ends up creating a lazy tensor using the
                        # second method which breaks the flow. To handle this case,
                        # we check if the device is the lazy device and create an
                        # empty cpu tensor instead and move that to the lazy device.
                        # Initialization ops are not needed in drop_data mode
                        # anyways so this doesn't change the resulting graph.
                        if self.config.drop_data:
                            param = torch.empty_like(param, device="cpu")
                        # If the tensor has been moved properly, it will have
                        # a device data, so check for that here and error out
                        # only if it doesn't.
                        elif not has_lazy_tensor_data_impl(param):
                            raise RuntimeError(
                                f"Module parameter/buffer `{param_name}` was "
                                f"directly initialized on the device. This is "
                                f"currently not supported. Please create the "
                                f"tensor without specifying a device as cstorch "
                                f"backend will take care of moving to the "
                                f"appropriate device as needed."
                            )

                    device_param = param.to(self.torch_device)
                    del param  # Remove the in-memory copy
                    param = cstorch_type(device_param)
                else:
                    param = param.to(self.torch_device)
                accessor[param_name] = param

    def __enter__(self) -> "LazyDevice":
        """Enables appliance data.

        `tensor.to("lazy")` will copy the tensor to the Cerebras backend which
        is stored in an ApplianceData struct. This tensor is either backed by
        host memory or file. However, if the config is not enabled and
        `tensor.to("lazy")` is called, the tensor content is immediately dropped
        since we don't expect to use the tensor content.

        For example, as we don't support initialization inside a
        `cstorch.trace`, we don't expect to use the tensor content and
        drop the tensors as we don't wrap that function in a `with device`
        context. But for model parameters or optimizer state, we need to keep
        the tensor content (which contains initialization values) and hence we
        wrap those in a `with device` context.
        """
        self._stack_size += 1

        # If this is the first time we are entering the context manager,
        # we need to enable appliance data and register the module hook.
        if self._stack_size == 1:
            from cerebras_pytorch.lib import cerebras_pytorch_lib

            # pylint: disable=protected-access,c-extension-no-member
            cerebras_pytorch_lib.set_artifact_dirs(
                artifact_dir=str(self.artifact_dir),
                device_data_dir=str(self.device_data_dir),
            )

            # Enable appliance data
            self.config.enabled = not self.config.drop_data

            if self.config.lazy_initialization:
                self.torch_device.__enter__()

                self._handles = [
                    register_module_parameter_registration_hook(
                        self.parameter_hook
                    ),
                    register_module_buffer_registration_hook(self.buffer_hook),
                ]
            else:
                self.tracker_entry.__enter__()

                self._handles = [
                    register_module_module_registration_hook(self.module_hook)
                ]

        return self

    def __exit__(self, *args) -> None:
        """Disables appliance data."""
        self._stack_size -= 1

        # If this is the last time we are exiting the context manager,
        # we need to disable appliance data and remove the module hook.
        if self._stack_size == 0:
            # Restore the previous state
            self.config.enabled = False

            if self.config.lazy_initialization:
                self.torch_device.__exit__(*args)
            else:
                self.tracker_entry.__exit__(*args)

            for handle in self._handles:
                handle.remove()

            self._handles = []

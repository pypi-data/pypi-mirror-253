# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Provides the fundamental and helper functions
required to compile a model for a Cerebras system
"""
from contextlib import nullcontext
from functools import wraps
from inspect import ismethod
from typing import Union

import torch

import cerebras_pytorch as cstorch
from cerebras_pytorch.backend import (
    Backend,
    current_backend,
    current_backend_impl,
)
from cerebras_pytorch.core.function_mode import CerebrasFunctionMode
from cerebras_pytorch.utils.step_closures import RepeatStepClosure


def compile(  # pylint: disable=redefined-builtin
    model: torch.nn.Module, backend: Union[str, Backend, None] = None,
):
    """Prepares the PyTorch module for tracing.

    This method prepares the module by moving it to the device so that it can be
    compiled after the first trace. Note that parameter initialization must be
    done before calling this method since post this call, the parameters are
    moved to the device.

    Args:
        model: The PyTorch module to be compiled.
        backend: The Cerebras backend to use to compile. If None, the current
            backend is used. If not current backend is set, the CPU backend is
            initialized and used. Defaults to None.
    Returns:
        A pseudo-module that almost acts like the original module but does not
        have any of the property accessor or private methods of the original
        module. It can be called `module(*args, **kwargs)` to run the forward
        pass, similar to the original module.
    """
    if backend is None:
        backend = current_backend(raise_exception=False)
        if backend is None:
            backend = cstorch.backend("cpu")
    elif isinstance(backend, str):
        backend = cstorch.backend(backend)
    elif isinstance(backend, Backend):
        curr_backend = current_backend(raise_exception=False)
        if backend is not curr_backend:
            raise RuntimeError(
                f"Compile got a different backend than the currently "
                f"initialized backend. "
            )
    else:
        raise TypeError(
            f"Expected backend to be one of str, Backend or None. "
            f"Got: {type(backend)}"
        )

    if (
        hasattr(model, "cerebras_device")
        and model.cerebras_device != backend.device
    ):
        raise RuntimeError(
            f"Attempting to compile a model using a different backend "
            f"than what was used to initialize its parameters. "
            f"Please make sure that you are using the same backend "
            f"in initialization and compilation. "
        )

    # pylint: disable=protected-access
    cs_backend_impl = backend._impl
    cs_backend_impl.setup_model(model)

    @wraps(model.__call__)
    def compiled_forward(*args, **kwargs):
        return cs_backend_impl.forward(model, *args, **kwargs)

    # Add aliases to the compiled forward
    for name in dir(model):
        method = getattr(model, name)
        if not name.startswith("_") and ismethod(method):
            setattr(compiled_forward, name, method)

    compiled_forward.device = cs_backend_impl.torch_device

    return compiled_forward


def trace(step_fn: callable) -> callable:
    """A decorator that wraps the training/evaluation step function for tracing.

    Any operation that is meant to be executed on the Cerebras Wafer-Scale
    Cluster must be wrapped with this decorator. This includes the forward pass,
    backward pass, optimizer steps, and more.

    For example, the following code snippet shows how to wrap a training step
    that does the forward and backward pass and optimizer step:

    ::

        @cstorch.trace
        def training_step(batch, model, optimizer, loss_fn):
            features, labels = batch
            outputs = model(features)
            loss = loss_fn(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            return loss

    Args:
        step_fn: The training/evaluation step function to be wrapped.
    Returns:
        The wrapped training/evaluation step function.
    """
    outputs = None

    @wraps(step_fn)
    def generated_trace_fn(*args, **kwargs):
        nonlocal outputs

        backend = current_backend_impl()
        if (
            not backend.in_run_context
            or not backend.run_context.traced.is_set()
        ):
            if backend.retrace_every_iteration:
                ctx = nullcontext()
            else:
                ctx = RepeatStepClosure()

            with ctx:
                with CerebrasFunctionMode():
                    outputs = step_fn(*args, **kwargs)

                # Set force=True to mark the outputs as if they were added to a
                # step closure. This ensures that if caller passes these outputs
                # to a step closure, we don't get duplicates.
                backend.mark_output(outputs, force=True)

            if backend.in_run_context:
                backend.run_context.traced.set()

        return outputs

    return generated_trace_fn

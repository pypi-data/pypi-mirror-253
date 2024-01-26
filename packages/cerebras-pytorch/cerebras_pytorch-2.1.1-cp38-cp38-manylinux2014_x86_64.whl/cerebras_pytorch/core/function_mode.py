# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from abc import ABC
from collections import OrderedDict
from typing import Any, Callable, Dict, Optional, Sequence

from torch.overrides import TorchFunctionMode
from torch.utils.hooks import RemovableHandle

_global_function_mode_forward_pre_hooks: Dict[int, Callable] = OrderedDict()
_global_function_mode_forward_hooks: Dict[int, Callable] = OrderedDict()


def register_function_mode_forward_pre_hook(
    hook: Callable[..., None]
) -> RemovableHandle:
    """
    Register pre forward hook for the function mode.
    Args:
        hook: a callback that is being called before operation execution.
        For the callback signature see `__function_mode__`.
    Returns:
        handle: a handle that can be used to delete registered hook.
    Example:
        def forward_pre_hook(func, types, args, kwargs) -> None:
            ...
        handle = register_function_mode_forward_pre_hook(forward_pre_hook)
        ...
        handle.remove()
    """
    handle = RemovableHandle(_global_function_mode_forward_pre_hooks)
    _global_function_mode_forward_pre_hooks[handle.id] = hook
    return handle


def register_function_mode_forward_hook(
    hook: Callable[..., None]
) -> RemovableHandle:
    """
    Register forward hook for the function mode.
    Args:
        hook: a callback that is being called after operation execution.
        For the callback signature see `__function_mode__`.
    Returns:
        handle: a handle that can be used to delete registered hook.
    Example:
        def forward_hook(func, types, args, kwargs, res) -> None:
            ...
        handle = register_function_mode_forward_hook(forward_hook)
        ...
        handle.remove()
    """
    handle = RemovableHandle(_global_function_mode_forward_hooks)
    _global_function_mode_forward_hooks[handle.id] = hook
    return handle


class CerebrasFunctionMode(TorchFunctionMode, ABC):
    """
    Function Mode allows to capture tensor operations on
    the python-level. The main goal of this class is to
    provide a single function mode which is running on
    `step_fn` and allows to register hooks.
    Note: function mode doesn't capture operations from
    the bwd pass, since these ops are being created on
    C++ level, so they are not visible to the pytorch
    function mode.
    """

    def __torch_function__(
        self,
        func: Callable,
        types: Sequence,
        args: Sequence[Any] = (),
        kwargs: Optional[Dict] = None,
    ):
        """ Hook operations from the forward pass """
        if not kwargs:
            kwargs = {}

        for fwd_pre_hook in _global_function_mode_forward_pre_hooks.values():
            fwd_pre_hook(func, types, args, kwargs)

        res = func(*args, **kwargs)

        for fwd_hook in _global_function_mode_forward_hooks.values():
            fwd_hook(func, types, args, kwargs, res)

        return res

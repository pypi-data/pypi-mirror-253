# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Provide an "optimizer" implementing static sparsity.
"""
import warnings

import torch
from torch.optim.optimizer import required

from .base import BaseSparsityOptimizer, InitMethodType


class StaticSparsityOptimizer(BaseSparsityOptimizer):
    r"""Implements a static sparsity optimizer.

    Args:
        params (iterable): iterable of parameters to sparsify or dicts defining
            parameter groups to sparsify
        sparsity (float): target sparsity
        init_method: Method to initialize sparsity pattern. Can either be the
            name of a built-in method or a lambda.

    Example:
        >>> optimizer = torch.optim.SGD(
                model.parameters(), lr=0.1, momentum=0.9
            )
        >>> sparsity_opt = StaticSparsityOptimizer(
                [p for n,p in model.named_parameters() if should_sparsify(n,p)],
                sparsity=0.5,
            )
        >>> sparsity_opt.hook_module(model)
        >>> sparsity_opt.initialize_sparsity()
        >>> optimizer.zero_grad()
        >>> loss_fn(model(input), target).backward()
        >>> optimizer.step()
        >>> sparsity_opt.step()

    """

    def __init__(
        self,
        params,
        sparsity=required,
        init_method: InitMethodType = "random",
        **kwargs,
    ):
        if kwargs:
            warnings.warn(f"Unused arguments: {kwargs}")

        defaults = {
            'sparsity': sparsity,
        }
        super().__init__(
            params=params, init_method=init_method, defaults=defaults
        )

    def add_param_group(self, param_group):
        # Verify all required values are specified.
        param_group = super().add_param_group(param_group)

        # Do static sparsity specific verification.
        sparsity = param_group["sparsity"]
        if not isinstance(sparsity, float):
            raise ValueError(
                "StaticSparsityOptimizer only supports constant sparsity"
            )
        if not 0.0 <= sparsity < 1.0:
            raise ValueError(
                f"Invalid sparsity level {sparsity}. Must be 0.0 <= s < 1.0"
            )
        param_group["csx_annotated_sparsity"] = (sparsity, sparsity, sparsity)

    def _get_target_sparsity_level_of_group(self, group) -> torch.FloatTensor:
        # Always the same static sparsity level
        return torch.tensor(group["sparsity"])

    @torch.no_grad()
    def step(self, closure=None):
        # Ensure we've called apply_sparsity before step
        self._ensure_sparsity_applied()

        # Merely apply the mask to maintain initial sparsity pattern.
        self.apply_sparsity()

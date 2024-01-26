# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Provide an optimizer implementing SET for use with the WSE.
"""

import torch
from torch.optim.optimizer import required

from .dynamic import DynamicSparsityOptimizer, InitMethodType, ScheduleType
from .utils import (
    HyperParameterType,
    make_mask_drop_minimum,
    make_mask_grow_maximum,
    set_param_group_hyperparam,
)


class SETSparsityOptimizer(DynamicSparsityOptimizer):
    r"""Implements Sparse Evolutionary Training (SET)

    Sparsity levels stay constant throughout training, but the lowest
    magnitude weights are pruned and then regrown randomly.

    See: https://arxiv.org/abs/1707.04780

    Args:
        params (iterable): iterable of parameters to sparsify or dicts defining
            parameter groups to sparsify
        init_method: Method to initialize sparsity pattern. Can either be the
            name of a built-in method or a lambda.
        sparsity: Sparsity, either constant or step-aware hyperparameter
        schedule: Sparsity update schedule. May be one of:

            * ``int``: Single regular update frequency.
            * ``list``: Irregular update on the given steps.
            * ``dict``: Containing ``{"start": start, "freq": freq, "stop":
              stop}`` for regular updates with start & stop.
            * ``ScheduleCallable`` : User function accepting a rankless
              ``torch.LongTensor`` and returning a rankless
              ``torch.BoolTensor``
        drop_fraction: Fraction of non-pruned weights to drop each update step.
            Either a constant or a step-aware hyperparamter.

    Example:
        >>> optimizer = torch.optim.SGD(
                model.parameters(), lr=0.1, momentum=0.9
            )
        >>> sparsity_opt = SETSparsityOptimizer(
                [p for n,p in model.named_parameters() if should_sparsify(n,p)],
                sparsity=0.9,
                schedule={"freq": 100, "stop": 1000},
                drop_fraction={"type": "cosine", "init": 0.3, "half_period": 1000},
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
        init_method: InitMethodType = "random",
        sparsity: HyperParameterType = required,
        schedule: ScheduleType = required,
        drop_fraction: HyperParameterType = 0.3,
        **kwargs,
    ):
        # drop_fraction is a required value for SET though it has a default
        # value. Pass it as dynamic optimizer kwarg. It will be configured
        # on each param_group.
        kwargs["drop_fraction"] = drop_fraction

        super().__init__(
            params,
            init_method=init_method,
            sparsity=sparsity,
            schedule=schedule,
            **kwargs,
        )

    def add_param_group(self, param_group):
        # Verify all required values are specified.
        param_group = super().add_param_group(param_group)
        set_param_group_hyperparam(param_group, "drop_fraction")

    @torch.no_grad()
    def update_mask(self, p, mask, sparsity, group):
        drop_fraction = group["drop_fraction"](
            self._step, group["is_update_step"]
        )

        # Keep the connections of highest magnitude weights but drop some.
        p_score = p.abs()
        mask, k = make_mask_drop_minimum(p_score, mask, drop_fraction)

        # Regrow randomly.
        regrow_score = torch.rand_like(p)
        return make_mask_grow_maximum(regrow_score, mask, sparsity, k)

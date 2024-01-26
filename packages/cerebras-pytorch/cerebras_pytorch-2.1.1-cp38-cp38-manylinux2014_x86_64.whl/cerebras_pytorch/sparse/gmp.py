# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Provide an optimizer implementing GMP for use with the WSE.
"""
import torch
from torch.optim.optimizer import required

from .dynamic import DynamicSparsityOptimizer, InitMethodType, ScheduleType
from .utils import (
    HyperParameterType,
    initialize_tiebreak,
    make_mask_topk_sparsity,
)


class GMPSparsityOptimizer(DynamicSparsityOptimizer):
    r"""Implements Gradual Magnitude Pruning

    Sparsity increases monotonically based on weight magnitude.

    See: https://arxiv.org/abs/1710.01878

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

    Example:
        >>> optimizer = torch.optim.SGD(
                model.parameters(), lr=0.1, momentum=0.9
            )
        >>> sparsity_opt = GMPSparsityOptimizer(
                [p for n,p in model.named_parameters() if should_sparsify(n,p)],
                sparsity={"type": "exp", "init": 0, "gamma": 1000*math.log(0.3)
                schedule=1000,
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
        tiebreak=None,
        **kwargs,
    ):
        if isinstance(sparsity, (int, float)):
            # Currently, constant sparisty is not supported for GMP, but a
            # cycling schedule with equal value is a workaround. Not that
            # you'd want this anyway, you might as well use static sparsity.
            sparsity = [sparsity]

        # tiebreak is optional for GMP
        kwargs["tiebreak"] = tiebreak

        super().__init__(
            params,
            init_method=init_method,
            sparsity=sparsity,
            schedule=schedule,
            **kwargs,
        )

    def add_param_group(self, param_group):
        sparsity = param_group.get("sparsity")
        if isinstance(sparsity, (int, float)):
            raise ValueError(
                f"Configured with {sparsity=}. This is not valid, because "
                f"the sparsity pattern would not change during training. "
                f"For a static sparsity pattern, use `type=\"static\".`"
            )

        # Verify all required values are specified.
        param_group = super().add_param_group(param_group)
        # If no tiebreak is specified, this will be a No-Op
        param_group["tiebreak"] = initialize_tiebreak(
            param_group.get("tiebreak")
        )

    @torch.no_grad()
    def update_mask(self, p, mask, sparsity, group):
        tiebreak = group["tiebreak"]
        score = tiebreak(p.abs())
        return make_mask_topk_sparsity(score, sparsity)

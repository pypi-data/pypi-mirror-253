# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Provide an optimizer implementing RigL for use with the WSE.
"""
from functools import partial

import torch
from torch.optim.optimizer import required

from .dynamic import DynamicSparsityOptimizer, InitMethodType, ScheduleType
from .utils import (
    HyperParameterType,
    InputGroupScoreShaper,
    OutputGroupScoreShaper,
    make_mask_drop_minimum,
    make_mask_grow_maximum,
    set_param_group_hyperparam,
)


class RigLSparsityOptimizer(DynamicSparsityOptimizer):
    r"""Implements Rigging the Lottery (RigL)

    Sparsity levels stay constant throughout training, but the lowest magnitude
    weights are pruned and then regrown using a proxy measure of where a pruned
    connection  would have had the most impact by finding the highest magnitude
    (dense) gradients of pruned weights.

    See: https://arxiv.org/abs/1911.11134

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
        >>> sparsity_opt = RigLSparsityOptimizer(
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
        # drop_fraction is a required value for RigL though it has a default
        # value. Pass it as dynamic optimizer kwarg. It will be configured
        # on each param_group.
        kwargs["drop_fraction"] = drop_fraction

        self._dense_grads = {}
        super().__init__(
            params,
            init_method=init_method,
            sparsity=sparsity,
            schedule=schedule,
            **kwargs,
        )

    def add_param_group(self, param_group):
        param_group = super().add_param_group(param_group)
        set_param_group_hyperparam(param_group, "drop_fraction")

        # RigL may need per-head balancing of attention projection weights
        in_groups = param_group.pop("balance_in_groups", None)
        out_groups = param_group.pop("balance_out_groups", None)

        def validate_balance(groups, err_key):
            for name, param in zip(
                param_group["param_names"], param_group["params"]
            ):
                for dim in param.shape:
                    if dim % groups == 0:
                        break
                else:
                    raise ValueError(
                        f"Sparsity group configured with `{err_key}`={groups} "
                        f"but parameter {name} does not have a dimension with "
                        f"a multiple of {groups}: {param.shape}"
                    )

        if out_groups:
            if in_groups:
                raise ValueError(
                    "Only one of `balance_in_groups` and `balance_out_groups` "
                    "can be specified at a time."
                )
            validate_balance(out_groups, "balance_out_groups")
            score_shaper = OutputGroupScoreShaper(out_groups)
        elif in_groups:
            validate_balance(in_groups, "balance_in_groups")
            score_shaper = InputGroupScoreShaper(in_groups)
        else:
            score_shaper = None
        param_group["score_shaper"] = score_shaper

        # Also add score shaping to the init_method.
        param_group["init_method"] = partial(
            param_group["init_method"], score_shaper=score_shaper
        )

    def _grad_hook(self, p, grad):
        # Save a copy of the dense gradients before masking.
        if p in self._dense_grads:
            # GPU gradient accumulation mode.
            self._dense_grads[p] += grad
        else:
            self._dense_grads[p] = grad.clone()

        return super()._grad_hook(p, grad)

    def zero_grad(self, set_to_none: bool = True):
        """
        Clears the accumulated dense gradients.
        """
        if set_to_none:
            self._dense_grads = {}
        else:
            for g in self._dense_grads.values():
                g.zero_()

    @torch.no_grad()
    def update_mask(self, p, mask, sparsity, group):
        if p not in self._dense_grads:
            raise RuntimeError(
                "RigL requires dense gradients, ensure you have called "
                "sparsity_optimizer.apply_sparsity()"
            )

        # RigL may need per-head balancing of attention projection weights
        score_shaper = group["score_shaper"]

        drop_fraction = group["drop_fraction"](
            self._step, group["is_update_step"]
        )

        # Keep the connections of highest magnitude weights but drop some.
        p_score = p.abs()
        mask, k = make_mask_drop_minimum(
            p_score, mask, drop_fraction, score_shaper=score_shaper
        )

        # Regrow where the gradient magnitude is the largest.
        regrow_score = self._dense_grads[p].abs()
        return make_mask_grow_maximum(
            regrow_score, mask, sparsity, k, score_shaper=score_shaper,
        )

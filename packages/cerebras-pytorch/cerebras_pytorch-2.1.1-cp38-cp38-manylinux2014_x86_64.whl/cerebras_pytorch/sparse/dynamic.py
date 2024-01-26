# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Base class for all dynamic sparsity optimizer, plus dynamic schedule helpers.
"""
import inspect
from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Union

import torch
from torch.optim.optimizer import required

import cerebras_pytorch as cstorch
from cerebras_pytorch.utils.typing import signature_matches_type_hint

from .base import BaseSparsityOptimizer, InitMethodType
from .utils import set_param_group_hyperparam


class BaseSchedule(ABC):
    TYPE_REGISTRY = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if hasattr(cls, "TYPE"):
            cls.TYPE_REGISTRY[cls.TYPE] = cls
        cls.TYPE_REGISTRY[cls.__name__] = cls

    @staticmethod
    def get_cls(typename: str):
        """
        Looks up the class by its typename in the registry.

        Raises a ValueError if none exist with that name.
        """
        tr = BaseSchedule.TYPE_REGISTRY
        if typename in tr:
            return tr[typename]
        raise ValueError(
            f"Uknown scheduler `type`:\"{typename}\". Valid options are "
            f"{list(tr.keys())}"
        )

    @abstractmethod
    def __call__(self, step: torch.LongTensor) -> torch.BoolTensor:
        """
        Given a training step rankless tensor, return a rankless bool tensor if
        this is a sparsity update step.
        """


class FreqSchedule(BaseSchedule):
    """
    When schedulding sparsity update steps on a regular interval, this class
    allows configuring the start and stop step in addition to the update
    frequency.
    """

    def __init__(self, start=None, freq=1000, stop=None):
        self.start = start
        self.freq = freq
        self.stop = stop

    def __call__(self, step: torch.LongTensor) -> torch.BoolTensor:
        """
        Returns a boolean rankless tensor if this step is an update step.
        """

        # First, check if this is (after offsetting from start) an update step
        # based on the frequency
        check_step = step
        if self.start is not None:
            check_step = step - self.start
        is_update_step = check_step % self.freq == 0

        # Next add the bounds checking if applicable
        if self.start is not None:
            is_update_step &= step >= self.start
        if self.stop is not None:
            is_update_step &= step < self.stop

        return is_update_step


class ListSchedule(BaseSchedule):
    """
    When schedulding requires an irregular update cadence, explicit steps can
    be provided as a list.
    """

    def __init__(self, steps: Union[List[int], torch.Tensor]):
        steps = tuple(steps)
        self.steps = steps
        self.start = min(steps)
        self.stop = max(steps)

    def __call__(self, step: torch.LongTensor) -> torch.BoolTensor:
        """
        Returns a boolean rankless tensor if this step is an update step.
        """
        is_update_step = torch.tensor(False, device=step.device)
        for s in self.steps:
            is_update_step |= step == s
        return is_update_step


ScheduleCallable = Callable[
    # torch.tensor(shape=[], dtype=int64) -> torch.tensor(shape=[], dtype=bool)
    [torch.LongTensor],
    torch.BoolTensor,
]
ScheduleType = Union[int, List[int], Dict, ScheduleCallable]


def make_schedule(schedule: ScheduleType) -> ScheduleCallable:
    """
    Instantiate a supported schedule type.
    """
    if isinstance(schedule, int):
        # Single update frequency
        return FreqSchedule(freq=schedule)
    elif isinstance(schedule, dict):
        schedule = schedule.copy()
        typename = schedule.pop("type", None)
        if typename:
            return BaseSchedule.get_cls(typename)(**schedule)
        if "freq" in schedule:
            return FreqSchedule(**schedule)
    elif isinstance(schedule, (list, tuple)):
        return ListSchedule(schedule)
    elif callable(schedule):
        signature = inspect.signature(schedule)
        if signature_matches_type_hint(signature, ScheduleCallable):
            return schedule
    valid_types = list(BaseSchedule.TYPE_REGISTRY.keys())
    raise ValueError(
        f"Invalid `schedule`: {schedule}. Valid options are:\n"
        f"* int: Regularly updating sparsity at fixed interval\n"
        f"* list[int]: List of specific update steps\n"
        f'* {{"start": start, "freq": freq, "stop": stop}}\n'
        f"* Callable: Used as-is\n"
        f"* {{\"type\": ...}} as one of {valid_types}"
    )


class DynamicSparsityOptimizer(BaseSparsityOptimizer, ABC):
    r"""Abstract base class for a dynamic sparsity optimizer.

    Subclasses must implement :meth:`update_mask`.

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
    """

    def __init__(
        self,
        params,
        sparsity=required,
        schedule: ScheduleType = required,
        init_method: InitMethodType = "random",
        **kwargs,
    ):
        defaults = {"sparsity": sparsity, "schedule": schedule, **kwargs}

        # When using CS, we execute the initial step 0 schedule and initialize
        # the masks on CPU, though during training it all happens on device:

        # |      Training Device | GPU | CS  |
        # | Operation            |           |
        # | ---------------------------------|
        # | step 0 schedule      | CPU | CPU |
        # | initial mask         | GPU | CPU |
        # | training schedule    | GPU | CS  |
        # | training mask update | GPU | CS  |

        self._step = torch.tensor(0, dtype=torch.int64)

        super().__init__(
            params=params, init_method=init_method, defaults=defaults,
        )

    def add_param_group(self, param_group):
        param_group = super().add_param_group(param_group)
        param_group["schedule"] = make_schedule(param_group["schedule"])
        set_param_group_hyperparam(param_group, "sparsity")
        return param_group

    def _init_sparsity_of_group(self, group):
        # Called from __init__ via BaseSparsityOptimizer.init_sparsity
        starts_sparse = group["schedule"](self._step)
        if not starts_sparse:
            # Then use the all 1's "mask".
            for p in group['params']:
                self.state[p]['mask'] = cstorch.ones_like(p, dtype=torch.bool)
        else:
            # Base implementation calls _get_target_sparsity_level_of_group,
            # which needs group["is_update_step"] set.

            group["is_update_step"] = starts_sparse
            super()._init_sparsity_of_group(group)
            group.pop("is_update_step")

        if self.backend.is_csx:
            # To provide a hint to the CSX compiler for performance
            # optimization, annotate the (min, max, ending) sparsity.

            begin_step = getattr(group["schedule"], "start", None) or 0
            # If the schedule has a `stop` step use that, otherwise pick
            # 100,000 arbitrarily.
            end_step = getattr(group["schedule"], "stop", None) or 100000

            # This simple scalar computation does not need to be traced
            with torch.device("cpu"):
                min_max_end = group["sparsity"].get_min_max_end(
                    begin_step, end_step
                )
                if min_max_end and not starts_sparse:
                    # If we we don't start sparse, there is a period of dense
                    # training, or 0% sparsity.
                    _, max_v, end_v = min_max_end
                    min_max_end = (0.0, max_v, end_v)
                group["csx_annotated_sparsity"] = min_max_end

    def _get_target_sparsity_level_of_group(self, group) -> torch.FloatTensor:
        """
        Returns the target sparsity level at the current step, including during
        _init_sparsity_of_group
        """

        is_update_step = group["is_update_step"]
        sparsity = group["sparsity"](self._step, is_update_step)
        # Ensure dynamic sparsity stays between [0, 1)
        sparsity = torch.clamp(sparsity, min=0.0, max=1.0)
        return sparsity

    def state_dict(self):
        state_dict = super(DynamicSparsityOptimizer, self).state_dict()
        state_dict["step"] = self._step
        return state_dict

    def visit_state(self, fn):
        """
        Applies a lambda to each stateful value.
        """
        super().visit_state(fn)
        new_val = fn(self._step)
        if new_val is not None:
            self._step = new_val

    def load_state_dict(self, state_dict):
        super(DynamicSparsityOptimizer, self).load_state_dict(state_dict)

        with self.backend.device:
            self._step = state_dict['step'].to(self.backend.torch_device)

    @abstractmethod
    @torch.no_grad()
    def update_mask(self, p, mask, sparsity, group):
        """
        Compute an updated sparsity pattern.

        Args:
            p (torch.Tensor): the parameter to sparsify
            mask (torch.tensor(dtype=torch.bool)): the current mask
                of param p
            sparsity (torch.tensor(dtype=torch.float32)): the desired
                sparsity level
            group (dict): The param group dict with any additional options
        Returns:
            The updated sparsity pattern on parameter p
        """

    @torch.no_grad()
    def step(self, closure=None):
        # Ensure we've called apply_sparsity before step
        self._ensure_sparsity_applied()

        # The weights and optimizer state were just updated. In case we
        # _decrease_ sparsity here instead of increasing it, apply the current
        # sparsity pattern.
        self.apply_sparsity()

        # By convention, `step` counts number of fwd/bwd/gradient evaluations of
        # the model (`step==0` is model initialization time). If
        # `sparsity_optimizer.step()` is called after weights have been updated
        # (which is recommended), we are effectively setting up the sparsity
        # pattern for the next step. Thus, increment step here so
        # self.process_schedule can indicate if this is a step to update.
        self._step.add_(1)

        for group in self.param_groups:

            is_update_step = group["schedule"](self._step)
            #  cache this group's is_update_step for use by update_mask
            group["is_update_step"] = is_update_step
            sparsity = self._get_target_sparsity_level_of_group(group)

            add_summaries = group.get("add_summaries", False)
            if add_summaries:
                if len(self.param_groups) > 1:
                    name = "/" + group["name"]
                else:
                    name = ""
                cstorch.summarize_scalar(f"sparsity/target{name}", sparsity)

            for name, p in zip(group["param_names"], group["params"]):
                if p.grad is None:
                    # If the gradient is None, then the parameter is unused
                    # and there is no need to update the mask
                    continue

                # In case there are multiple devices, ensure the sparsity is
                # on the parameter's device; it comes from the device we
                # evaluated the schedule on, usually the device of step.
                sparsity = sparsity.to(p.device)

                mask = self.state[p]['mask']

                updated_mask = self.update_mask(p, mask, sparsity, group)
                # Rewrite into the existing mask tensor for state tracking
                new_mask = torch.where(is_update_step, updated_mask, mask)
                self.state[p]['mask'] = new_mask
                if add_summaries:
                    cstorch.summarize_scalar(
                        f"sparsity/{name}",
                        1 - new_mask.sum() / new_mask.numel(),
                    )

            # Remove is_update_step, this shouldn't be stateful.
            group.pop("is_update_step")

        self.apply_sparsity()

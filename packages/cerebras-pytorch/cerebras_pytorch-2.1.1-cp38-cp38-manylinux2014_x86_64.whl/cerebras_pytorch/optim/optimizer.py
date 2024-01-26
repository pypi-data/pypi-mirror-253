# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""The Cerebras base optimizer class"""
from abc import ABC, abstractmethod

import torch

from cerebras_pytorch.backend import current_backend_impl


class Optimizer(torch.optim.Optimizer, ABC):
    """
    The abstract Cerebras base optimizer class.

    Enforces that the `preinitialize` method is implemented
    wherein the optimizer state should be initialized ahead of time
    """

    def __init__(self, *args, enable_global_step: bool = False, **kwargs):
        """
        Args:
            enable_global_step: If True, the optimizer will keep track of the
                global step for each parameter.
        """
        super().__init__(*args, **kwargs)
        self.enable_global_step = enable_global_step

        self.backend = current_backend_impl()

        with self.backend.device:
            self.preinitialize()

            if enable_global_step:
                for group in self.param_groups:
                    for p in group["params"]:
                        self.state[p]["step"] = torch.tensor(
                            0.0, dtype=torch.float32
                        ).to(p.device)

        self._lr_scheduler_registry = []

        self.backend.register_optimizer(self)

    def increment_global_step(self, p):
        """
        Increases the global steps by 1 and returns the current
        value of global step tensor in torch.float32 format.
        """
        if "step" not in self.state[p]:
            raise RuntimeError(
                "No global step in the state. "
                "Please pass in `enable_global_step=True` "
                "to initialize the global step"
            )

        self.state[p]["step"] += 1.0
        return self.state[p]["step"]

    def state_dict(self, *args, **kwargs):
        s = super().state_dict(*args, **kwargs)

        return s

    def load_state_dict(self, state_dict):
        with self.backend.device:
            super().load_state_dict(state_dict)

        self.backend.post_optimizer_load_state_dict(self)

    def visit_state(self, fn):
        """
        Applies a lambda to each stateful value.
        """
        for state in self.state.values():
            for key, val in state.items():
                new_val = fn(val)
                if new_val is not None:
                    state[key] = new_val

    @abstractmethod
    def state_names_to_sparsify(self):
        """
        Return the names of of per-parameter states that need to be sparsified
        when applying sparsity to the underlying parameters.
        """

    @abstractmethod
    def preinitialize(self):
        """
        The optimizer state must be initialized ahead of time in order
        to capture the full compute graph in the first iteration. This method
        must be overriden to perform the state preinitialization
        """

    @abstractmethod
    def step(self, closure=None):
        """
        Perform the optimizer step itself. Note, there should be no new state
        being created in this function. All state must be created ahead of time in
        `preinitialize` and only updated in this method.
        """

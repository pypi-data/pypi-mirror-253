# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Wrap a regular optimizer with a sparsity optimizer for auto-stepping.
"""

from torch.optim.optimizer import Optimizer


class SparsityWrapperOptimizer(Optimizer):
    """
    Helper Optimizer that can be used as a drop-in replacement for the main
    optimizer that also takes care of updating and applying sparsity.
    """

    def __init__(self, optimizer, sparsity_optimizer):
        if hasattr(optimizer, "state_names_to_sparsify"):

            # Determine which optimizer states need sparsification
            opt_states_to_sparsify = optimizer.state_names_to_sparsify()
            sparsity_optimizer.manage_optimizer_state_sparsity(
                optimizer, opt_states_to_sparsify
            )

        self.optimizer = optimizer
        self.sparsity_optimizer = sparsity_optimizer

        backend = sparsity_optimizer.backend
        backend.unregister_optimizer(optimizer)
        backend.unregister_optimizer(sparsity_optimizer)
        backend.register_optimizer(self)

    @property
    def state(self):
        # Merge the states, including nested merging for shared params
        o = self.optimizer.state
        s = self.sparsity_optimizer.state

        def merge(k):
            ov = o.get(k)
            os = s.get(k)
            if ov and os:
                return {**ov, **os}
            elif ov:
                return ov
            return os

        return {k: merge(k) for k in o.keys() | s.keys()}

    @property
    def param_groups(self):
        # Only expose the param groups of the main optimizer, otherwise there
        # would appear to be duplicates in the param_groups[i]["params"]
        return self.optimizer.param_groups

    def zero_grad(self, set_to_none: bool = True):
        self.optimizer.zero_grad(set_to_none)
        self.sparsity_optimizer.zero_grad(set_to_none)

    def state_dict(self):
        state_dict = self.optimizer.state_dict()
        state_dict["sparsity"] = self.sparsity_optimizer.state_dict()
        return state_dict

    def load_state_dict(self, state_dict):
        sparsity = state_dict.pop("sparsity", None)
        if sparsity is not None:
            self.sparsity_optimizer.load_state_dict(sparsity)
        self.optimizer.load_state_dict(state_dict)

    def visit_state(self, fn):
        """
        Applies a lambda to each stateful value.
        """
        self.optimizer.visit_state(fn)
        self.sparsity_optimizer.visit_state(fn)

    def step(self, closure=None):
        self.optimizer.step(closure)
        self.sparsity_optimizer.step()

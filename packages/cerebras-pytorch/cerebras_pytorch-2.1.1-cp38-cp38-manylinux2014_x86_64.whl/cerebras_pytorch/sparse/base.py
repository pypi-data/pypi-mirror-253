# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

import functools
from abc import ABC, abstractmethod
from collections import defaultdict
from collections.abc import Iterable
from typing import List

import torch
from torch.optim.optimizer import Optimizer

from .init import InitMethodType, make_init_method


class BaseSparsityOptimizer(Optimizer, ABC):
    r"""
    Abstract base class for a dynamic sparsity optimizer.

    Subclasses must implement :meth:`_get_target_sparsity_level_of_group` and
    :meth:`step`.

    Args:
        params (iterable): iterable of parameters to sparsify or dicts defining
            parameter groups to sparsify
        init_method (InitMethodType): method by which sparsity is initialized
        defaults (dict): Additional defaults for param_groups
    """

    def __init__(
        self, params, init_method: InitMethodType = 'random', defaults=None
    ):
        defaults = defaults or {}
        defaults['init_method'] = init_method
        super().__init__(params, defaults)

        self.optimizers_and_state_names = []
        self._init_sparsity_called = False
        self._hook_module_called = False
        self._apply_sparsity_called = False
        self._param_grad_hooks = {}

        from cerebras_pytorch.backend import current_backend_impl

        self.backend = current_backend_impl()
        self.backend.register_optimizer(self)

    def initialize_sparsity(self):
        """
        Compute the initial sparsity pattern for each parameter.
        """
        if self._init_sparsity_called:
            # Don't re-initialize
            return

        self._init_sparsity_called = True
        num_params = sum(len(group["params"]) for group in self.param_groups)

        # Set up intiailization progress bar
        if self.backend.progress_tracker is not None:
            self.backend.progress_tracker.reset(total=num_params)
            self.backend.progress_tracker.set_postfix()
            self.backend.progress_tracker.set_description(
                "Initializing sparsity patterns"
            )

        with self.backend.device:
            for group in self.param_groups:
                self._init_sparsity_of_group(group)
            self.visit_state(lambda x: x.to(self.backend.torch_device))

        # After initializing new masks, we'll need to double check that
        # apply_sparsity() gets called once before step()
        self._apply_sparsity_called = False

    def _init_sparsity_of_group(self, group):
        """
        Compute the initial sparsity pattern for each of the parameters in the
        given group.
        """
        # This simple scalar computation does not need to be traced
        with torch.device("cpu"):
            sparsity = self._get_target_sparsity_level_of_group(group)

        # Use the CPU device if doing eager initialization on CSX.
        # Otherwise, use the parameter's device.
        # This allows us to trace the mask initialization during
        # lazy initialization.
        device = None
        if (
            self.backend.is_csx
            and not self.backend.device.config.lazy_initialization
        ):
            device = "cpu"

        initializer = group['init_method']
        for p in group['params']:
            self.state[p]["mask"] = initializer(p, sparsity, device=device)

            if self.backend.progress_tracker is not None:
                self.backend.progress_tracker.update()

    @abstractmethod
    def _get_target_sparsity_level_of_group(self, group) -> torch.FloatTensor:
        """
        Returns the target sparsity level for parameters in the group.

        Returns:
            sparsity_level: a rankless FloatTensor holding the sparsity level
        """

    def manage_optimizer_state_sparsity(
        self, optimizer: Optimizer, state_names: List[str]
    ):
        """
        Manage the sparsity of an optimizer's state. For any parameters that
        this SparsityOptimizer manages, apply the sparsity pattern to all
        states named `state_names`
        """
        self.optimizers_and_state_names.append((optimizer, state_names))

    def _yield_optimizer_states(self, p):
        """
        Yield the given parameter's optimizer states which need sparsity
        applied.
        """
        for opt, state_names in self.optimizers_and_state_names:
            if p in opt.state:
                state = opt.state[p]
                for s_name in state_names:
                    if s_name in state:
                        yield state[s_name]

    def annotate_sparsity(self):
        """
        Annotate sparsity as performance hints for the cerebras compiler
        """
        for group in self.param_groups:
            sparsity = group.get("csx_annotated_sparsity")
            if sparsity is None:
                continue
            min_v, max_v, ending_v = sparsity
            for p in group['params']:
                self.backend.set_attribute(p, "min_sparsity", min_v)
                self.backend.set_attribute(p, "max_sparsity", max_v)
                self.backend.set_attribute(p, "sparsity", ending_v)
                for state in self._yield_optimizer_states(p):
                    self.backend.set_attribute(state, "min_sparsity", min_v)
                    self.backend.set_attribute(state, "max_sparsity", max_v)
                    self.backend.set_attribute(state, "sparsity", ending_v)

    def hook_module(self, module: torch.nn.Module):
        """
        Hook the given module such that the sparsity pattern is applied to both
        the parameters before forward() and gradients after backward()
        """
        self._hook_module_called = True

        def forward_pre_hook(module, input):
            self.annotate_sparsity()
            self.apply_sparsity()

        module.register_forward_pre_hook(forward_pre_hook)

    def _ensure_sparsity_applied(self):
        if not self._apply_sparsity_called:
            error = (
                "apply_sparsity() must be called before forward() to apply "
                "sparsity to parameters and optimizer state. "
            )

            if self._hook_module_called:
                error += (
                    "A module hook was installed which should have taken care "
                    "of calling it, but did not. Check that you have not "
                    "disabled module hooks."
                )
            else:
                error += (
                    "For your convenience, the SparsityOptimizer method "
                    "``.hook_module()`` can add a torch.nn.Module forward_pre "
                    "hook to automatically apply sparsity."
                )

            raise RuntimeError(error)

    def zero_grad(self, set_to_none: bool = True):
        """
        Override default torch.optim.Optimizer to never zero gradients: This
        optimizer is slightly unique in that it isn't responsible for the
        `main` weight update of the params it manages (and thus doesn't consult
        or "maintain" their gradients), but it does manage the sparsity pattern
        of the params.

        Can be further overriden in other SparsityOptimizers if they deal with
        gradients (like RigL).
        """

    def state_dict(self):
        # Adapted from torch.optim.Optimizer, but we use param_names

        # param_names used in place of params
        param_groups = []

        # map parameter -> name
        name_map = {}
        for group in self.param_groups:
            name_map.update(dict(zip(group["params"], group["param_names"])))
            group = group.copy()
            del group["params"]

            # Some objects may themselves be stateful, so we store their state
            # instead of them
            for k, v in list(group.items()):
                if hasattr(v, "state_dict"):
                    group[k] = v.state_dict()
                elif callable(v):
                    # Don't serialize callable objects
                    del group[k]

            param_groups.append(group)

        state = {name_map[p]: v for p, v in self.state.items()}

        return {"state": state, "param_groups": param_groups}

    def load_state_dict(self, state_dict):
        # Adapted from torch.optim.Optimizer, but we use param_names

        # Validate the state_dict
        groups = self.param_groups
        saved_groups = state_dict['param_groups']

        if len(groups) != len(saved_groups):
            raise ValueError(
                "loaded state dict has a different number of parameter groups"
            )

        # map name -> parameter
        name_map = {}
        for group in self.param_groups:
            name_map.update(dict(zip(group["param_names"], group["params"])))

        for group, saved_group in zip(groups, saved_groups):
            if group["param_names"] != saved_group["param_names"]:
                raise ValueError(
                    "loaded state dict contains different parameters than "
                    "the current optimizer"
                )

        def to_device(param, value):
            """
            Transfer each value to the same device as param.
            """
            if isinstance(value, torch.Tensor):
                return value.to(param.device)
            elif isinstance(value, dict):
                return {k: to_device(param, v) for k, v in value.items()}
            elif isinstance(value, Iterable):
                return type(value)(to_device(param, v) for v in value)
            else:
                return value

        # Copy state associated with params (moving tensors to param device).
        state = defaultdict(dict)
        for param_name, v in state_dict['state'].items():
            param = name_map[param_name]
            state[param] = to_device(param, v)

        # Update parameter groups, resetting their 'params' value
        def update_group(group, new_group):
            new_group['params'] = group['params']
            # Some Sparsity param_group entries are complex and need to be
            # serialized specially.
            for k, v in group.items():
                if hasattr(v, "load_state_dict"):
                    # Use the old object, but with loaded state.
                    v.load_state_dict(new_group[k])
                    new_group[k] = v
                elif k not in new_group:
                    # Some items were omitted from the state_dict. Keep their
                    # old value.
                    new_group[k] = v

            return new_group

        param_groups = [
            update_group(g, ng) for g, ng in zip(groups, saved_groups)
        ]
        self.__setstate__({'state': state, 'param_groups': param_groups})
        # Loading state counts as initializing it, don't re-init
        self._init_sparsity_called = True

    def visit_state(self, fn):
        """
        Applies a lambda to each stateful value.
        """
        for state in self.state.values():
            for key, val in state.items():
                new_val = fn(val)
                if new_val is not None:
                    state[key] = new_val

        for group in self.param_groups:
            for v in group.values():
                if hasattr(v, "visit_state"):
                    v.visit_state(fn)

    def add_param_group(self, param_group):

        # SparsityOptimizer accepts named_params tuples instead
        named_params = param_group["params"]
        if isinstance(named_params, list):
            # list of tuples
            names, params = zip(*named_params)
        elif isinstance(named_params, tuple):
            # single tuple
            names, params = named_params
            params = [params]
            names = [names]

        param_group["params"] = params
        param_group["param_names"] = names
        super().add_param_group(param_group)

        # Hydrate the initializer
        param_group["init_method"] = make_init_method(
            param_group["init_method"]
        )

        # Ensure every group has a name
        if "name" not in param_group:
            if len(names) == 1:
                # Single weight group
                param_group["name"] = names[0]
            else:
                param_group["name"] = f"group_{len(self.param_groups)}"

        # Return the newly added param_group
        return self.param_groups[-1]

    @torch.no_grad()
    def apply_sparsity(self):
        """
        Apply the sparsity pattern to the parameters and optimizer states.
        """
        if not self._init_sparsity_called:
            if self.backend.is_csx:
                raise RuntimeError(
                    "Sparsity must be initialized before execution"
                )
            # We can init lazily on CPU/GPU though.
            self.initialize_sparsity()
        self._apply_sparsity_called = True
        self._apply_masks_to_params()
        self._apply_masks_to_opt_state()

    def _grad_hook(self, p, grad):
        # In the case there any NaNs in the unused gradients that correspond to
        # zero'd out weights, we use a selection to replace these NaNs with
        # zeros. (multiplying with the mask would preserve them).
        # DLS will skip a weight update if there is a NaN in the gradient, but
        # we only want this to happen if there is a NaN in gradients
        # corresponding to non-zero weights. This is the behavior of the CS2
        # which doesn't even compute the full gradients on most steps.
        zero = torch.zeros_like(grad)

        mask = self.state[p]['mask']
        # Return modified gradient.
        return torch.where(mask, grad, zero)

    @torch.no_grad()
    def _apply_masks_to_params(self):
        for group in self.param_groups:
            for p in group['params']:
                # Apply sparsity.
                p.mul_(self.state[p]['mask'])
                # Set up autograd to apply sparsity to gradients too.
                if p not in self._param_grad_hooks:
                    self._param_grad_hooks[p] = p.register_hook(
                        functools.partial(self._grad_hook, p)
                    )

    @torch.no_grad()
    def _apply_masks_to_opt_state(self):
        for group in self.param_groups:
            for p in group['params']:
                for state in self._yield_optimizer_states(p):
                    state.mul_(self.state[p]['mask'])

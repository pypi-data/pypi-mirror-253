# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""
Configuration helpers for constructing SparsityOptimizer objects.
"""

import inspect
import logging
import re
from typing import Callable, Dict, List, Optional, Tuple, Union

import torch

from .base import BaseSparsityOptimizer
from .wrapper import SparsityWrapperOptimizer

SparseParamFilterType = Callable[[str, torch.nn.Parameter], bool]
# Can be a single regex, a list of regex, or a dict of regex -> config
ParamNamePatternsType = Union[str, List[str], Dict[str, dict]]

LOGGER = logging.getLogger("cerebras.sparsity")


def default_sparse_param_filter(name: str, param: torch.nn.Parameter) -> bool:
    """
    Return True if the given parameter should be sparse.

    Args:
        name: Name of the parameter
        param: The parameter itself
    """

    # By default, sparsify params that are > 1D and not embedding or norm.
    name = name.lower()
    if (
        len(param.shape) <= 1
        or "embedding" in name
        or "norm" in name
        or "lm_head" in name
        or "pe_helper" in name
    ):
        return False
    return True


def validate_options(options: Dict):
    """
    Validate and handle options given to a sparsity optimizer.
    """

    if "sparsity_schedule" in options:
        options["schedule"], options["sparsity"] = zip(
            *options.pop("sparsity_schedule")
        )
    # TODO: handle more validation


def sparsity_param_groups(
    named_parameters: List[Tuple[str, torch.nn.Parameter]],
    param_name_patterns: Optional[ParamNamePatternsType] = None,
    sparse_param_filter: Optional[SparseParamFilterType] = None,
):
    """
    Returns a list of parameters or a list of tuple of (param, dict) for
    passing to the sparsity optimizer's param_groups, if configured.

    Three yaml examples:

        sparsity:
          type: gmp
          sparsity_schedule:
          - [0, 0.1]
          - [6, 0.3]
          - [8, 0.5]
          param_name_patterns: "fc_layers.*weight"

        sparsity:
          type: gmp
          sparsity_schedule:
          - [0, 0.1]
          - [6, 0.3]
          - [8, 0.5]
          param_name_patterns:
          - "fc_layers.*weight"
          - "final_layer.*weight"

        sparsity:
          type: gmp
          param_name_patterns:
            fc_layers.*weight:
              sparsity_schedule:
              - [0, 0.1]
              - [6, 0.3]
              - [8, 0.5]
            final_layer.*weight:
              sparsity_schedule:
              - [0, 0.2]
              - [6, 0.5]
              - [8, 0.7]

    Args:
        named_parameters: List of (name, param) from model.named_parameters()
        param_name_patterns: Filter to select which parameters are sparse and
                             optionally if any more specific config should be
                             applied to certain parameters.
        sparse_param_filter: Callable to provide fallback selection of which
                             parameters are sparse if no param_name_patterns
                             are provided.
    """
    if not sparse_param_filter:
        sparse_param_filter = default_sparse_param_filter

    # Check if there is a yaml specified param name pattern
    if isinstance(param_name_patterns, str):
        # Just a single config changing which params the defaults apply to.
        pattern = re.compile(param_name_patterns)

        def sparse_param_filter(
            name, param
        ):  # pylint: disable=function-redefined
            return pattern.search(name)

    elif isinstance(param_name_patterns, list):
        # A list of several patterns, all of which get the default setting.
        patterns = list(map(re.compile, param_name_patterns))

        def sparse_param_filter(
            name, param
        ):  # pylint: disable=function-redefined
            return any(map(lambda patt: patt.search(name), patterns))

    elif isinstance(param_name_patterns, dict):
        # An entire param_group per pattern.
        param_groups = []
        for pattern, param_group in param_name_patterns.items():
            # To allow yaml syntax of adding extra name patterns without
            # customizing their group options.
            if param_group is None:
                param_name_patterns[pattern] = param_group = {}
            if not isinstance(param_group, dict):
                raise ValueError(
                    f"To specify param groups, each `param_name_patterns` "
                    f"should be a dict containing the group's options. "
                    f"Instead, got `{param_group}` for `{pattern}`. "
                    f"To specify multiple patterns whose matching params "
                    f"all get default options, define "
                    f"`param_name_patterns` as a list instead."
                )
            param_group["params"] = []
            validate_options(param_group)
            param_groups.append(param_group)

        patterns = [
            (re.compile(pattern), param_group["params"])
            for pattern, param_group in param_name_patterns.items()
        ]
        # Go add each parameter to at most one group.
        for name, param in named_parameters:
            for pattern, param_list in patterns:
                if pattern.search(name):
                    param_list.append((name, param))
                    break

        for pattern, param_list in patterns:
            if len(param_list) == 0:
                raise ValueError(
                    f"{pattern} did not match any parameter names!"
                )
        return param_groups

    # Not returning param_groups, just list of params all getting defaults.
    return [(n, p) for n, p in named_parameters if sparse_param_filter(n, p)]


def configure_sparsity_optimizer(
    sparsity_type: str,
    named_parameters: List[Tuple[str, torch.nn.Parameter]],
    param_name_patterns: Optional[ParamNamePatternsType] = None,
    sparse_param_filter: Optional[SparseParamFilterType] = None,
    **kwargs,
) -> BaseSparsityOptimizer:
    """
    Construct a SparsityOptimizer of the appropriate sparsity_type according to
    ``param_name_patterns`` or ``sparse_param_filter`` of the given
    ``named_parameters``.

    ``**kwargs`` are passed along to the SparsityOptimizer ``__init__``

    Args:
        sparsity_type: Type of sparsity optimizer to construct.
        named_parameters: List of (name, param) from model.named_parameters()
        param_name_patterns: Filter to select which parameters are sparse and
                             optionally if any more specific config should be
                             applied to certain parameters.
        sparse_param_filter: Callable to provide fallback selection of which
                             parameters are sparse if no param_name_patterns
                             are provided.
        kwargs: Passed along to the chosen sparsity optimizer ``__init__``.
    """

    # Allow user dervied sparsity optimizer to be configured using helper.
    def _retrieve_all_subclasses(cls):
        for subcls in cls.__subclasses__():
            yield subcls
            yield from _retrieve_all_subclasses(subcls)

    supported_sparsity_types = {}
    for cls in _retrieve_all_subclasses(BaseSparsityOptimizer):
        if inspect.isabstract(cls):
            continue
        key = cls.__name__.lower().replace("sparsityoptimizer", "")
        supported_sparsity_types[key] = cls

    # Ensure we have a known sparsity optimizer.
    sparsity_opt_cls = supported_sparsity_types.get(sparsity_type)

    if not sparsity_opt_cls:
        raise ValueError(
            f"Unsupported sparsity optimizer type: {sparsity_type}. "
            f"Supported types: {list(supported_sparsity_types.keys())}"
        )

    # Determine which parameters need sparsification.
    params_to_sparsify = sparsity_param_groups(
        named_parameters, param_name_patterns, sparse_param_filter,
    )

    if len(params_to_sparsify) == 0:
        LOGGER.warning("Sparsity configured, but no parameters were sparse")
    else:

        def log(opts, names):
            base_msg = f"Will apply \"{sparsity_type}\" sparsity {opts} to"
            if not LOGGER.isEnabledFor(logging.INFO - 5):
                LOGGER.info(
                    f"{base_msg} {len(names)} tensor{'s'[:len(names)^1]}"
                )
            else:
                LOGGER.verbose(f"{base_msg} {names}")

        defnames = []
        for param in params_to_sparsify:
            if isinstance(param, tuple):
                name, param = param
                defnames.append(name)
            else:
                opts = {**kwargs, **param}
                names, params = zip(*opts.pop("params"))
                # Log the param group with extra options
                log(opts, names)

        if defnames:
            # For all params which only have default options, log them.
            log(kwargs, defnames)

    # Adapt sparsity_schedule -> (sparsity, schedule)
    validate_options(kwargs)

    return sparsity_opt_cls(
        params=params_to_sparsify,
        # Pass yaml config along to sparsity optimizer as its defaults.
        **kwargs,
    )


def configure_sparsity_wrapper(
    model: torch.nn.Module,
    optimizer: torch.optim.Optimizer,
    sparsity_type: str,
    param_name_patterns: Optional[ParamNamePatternsType] = None,
    sparse_param_filter: Optional[SparseParamFilterType] = None,
    **kwargs,
) -> SparsityWrapperOptimizer:
    """
    Returns a SparsityWrapperOptimizer ready to be a drop-in replacement for
    the given ``optimizer``, while also constructing a SparsityOptimizer of the
    appropriate ``sparsity_type`` according to ``param_name_patterns`` or
    ``sparse_param_filter`` of the given ``model.named_parameters()``.

    ``**kwargs`` are passed along to the SparsityOptimizer ``__init__``

    Args:
        model: Root module to extract parameters and hook the FWD pass
        optimizer: Optimizer to wrap to sparsify the optimizer state.
        sparsity_type: Type of sparsity optimizer to construct.
        param_name_patterns: Filter to select which parameters are sparse and
                             optionally if any more specific config should be
                             applied to certain parameters.
        sparse_param_filter: Callable to provide fallback selection of which
                             parameters are sparse in case no
                             param_name_patterns are provided.
        kwargs: Passed along to the sparsity optimizer ``__init__``.
    """

    sparsity_optimizer = configure_sparsity_optimizer(
        sparsity_type,
        list(model.named_parameters()),
        param_name_patterns,
        sparse_param_filter,
        **kwargs,
    )
    sparsity_optimizer.hook_module(model)

    return SparsityWrapperOptimizer(optimizer, sparsity_optimizer)

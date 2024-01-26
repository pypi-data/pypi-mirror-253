# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

import inspect
from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Optional, Tuple, Union

import torch

import cerebras_pytorch as cstorch
from cerebras_pytorch.utils.typing import signature_matches_type_hint


class ScoreTiebreaker:
    """
    Base class for all "tiebreaking" of score for deterministic execution. The
    default tiebreaking is "none", leaving ties non-deterministic across
    systems. In particular, torch.topk has different behavior on CPU, GPU, and
    WSE. It isn't stable and doesn't guarantee anything around ties.
    """

    def __call__(self, score: torch.Tensor):
        """
        Return score unmodified.
        """
        return score


class RandomScoreTiebreaker(ScoreTiebreaker):
    TYPE = "random"

    def __init__(self, eps):
        self.eps = eps

    def __call__(self, score: torch.Tensor):
        """
        Add small (eps) random offset.
        """
        return score + score.new_empty(score.shape).uniform_(to=self.eps)


class FirstScoreTiebreaker(ScoreTiebreaker):
    TYPE = "first"

    def __init__(self, eps):
        self.eps = eps

    def __call__(self, score: torch.Tensor):
        """
        Add a small, linearly increasing epsilon to the score. Positions with
        unraveled indices of higher value will be chosen before earlier entries
        with equal score.
        """

        iota = torch.arange(score.numel(), device=score.device)
        eps = torch.tensor(
            self.eps / score.numel(), dtype=score.dtype, device=score.device
        )
        return score + (iota * eps).view(score.shape)


def initialize_tiebreak(kwargs):
    if not kwargs:
        # No tiebreaking
        return ScoreTiebreaker()
    TYPE = kwargs.pop("type")
    for cls in ScoreTiebreaker.__subclasses__():
        if cls.TYPE == TYPE:
            return cls(**kwargs)
    raise ValueError(f"Couldn't construct a ScoreTiebreaker {TYPE}")


class BaseHyperParameter(ABC):
    """
    Base class for step-aware hyperparameters used in Sparsity Optimizers.
    """

    __state_slots__ = []
    """
    Subclasses should provide their own definition of __state_slots__ holding
    which attributes are stateful
    """

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
        tr = BaseHyperParameter.TYPE_REGISTRY
        if typename in tr:
            return tr[typename]
        raise ValueError(
            f"Unknown hyper parameter `type`:\"{typename}\". Valid options "
            f"are {list(tr.keys())}"
        )

    @abstractmethod
    def __call__(self, step: torch.Tensor, is_update_step: torch.Tensor):
        """
        Return a torch.Tensor with the value of the hyperparatmer at the given
        step.

        Args:
            step: int64 tensor holding current step
            is_update_step: bool tensor indicating whether sparsity will be
                updated on this step.

        Returns:
            torch.Tensor on the device of step with the value of the
                hyperparamter
        """

    def visit_state(self, fn):
        """
        Applies a lambda to each stateful value.
        """
        for slot in self.__state_slots__:
            new_val = fn(getattr(self, slot))
            if new_val is not None:
                setattr(self, slot, new_val)

    def state_dict(self):
        return {k: getattr(self, k) for k in self.__state_slots__}

    def load_state_dict(self, state):
        for k, v in state.items():
            setattr(self, k, v)

    def get_min_max_end(
        self, begin: int, end: int
    ) -> Tuple[float, float, float]:
        """
        Given a beginning and ending step, compute the statistics of this
        step-aware hyper parameter. Used for estimating memory requirements for
        dynamic sparsity.

        Return [min, max, ending]
        """
        # By default, assume monotonic behavior and sample the callable
        begin_value = self(torch.tensor(begin), torch.tensor(False)).item()
        end_value = self(torch.tensor(end), torch.tensor(False)).item()
        if begin_value < end_value:
            return (begin_value, end_value, end_value)
        else:
            return (end_value, begin_value, end_value)


class ConstantHyperParameter(BaseHyperParameter):
    """
    Constant at every step.
    """

    TYPE = "constant"

    def __init__(self, value):
        self.value = torch.tensor(value)

    def __call__(self, step: torch.Tensor, is_update_step: torch.Tensor):
        return self.value


class LinearHyperParameter(BaseHyperParameter):
    """
    Linear change from an initial value.

    :math:`y(step) = init + step * slope`
    """

    TYPE = "linear"

    def __init__(self, init, slope):
        self.init = torch.tensor(init)
        self.slope = torch.tensor(slope)

    def __call__(self, step: torch.Tensor, is_update_step: torch.Tensor):
        return self.init + step.float() * self.slope


class ExpHyperParameter(BaseHyperParameter):
    """
    Exponential, approaching an asymptotic final value

    :math:`y(step) = final + (init-final) e^{step \cdot gamma}`
    """

    TYPE = "exp"

    def __init__(self, init, gamma, final=1):
        self.final = torch.tensor(final)
        self.scale = self.final - torch.tensor(init)
        self.gamma = torch.tensor(gamma)

    def __call__(self, step: torch.Tensor, is_update_step: torch.Tensor):
        return self.final - self.scale * torch.exp(step.float() * self.gamma)


class PowerHyperParameter(BaseHyperParameter):
    """
    Power law.

    :math:`y(step) = init \cdot beta^{step}`
    """

    TYPE = "power"

    def __init__(self, init, beta):
        self.init = torch.tensor(init)
        self.beta = torch.tensor(beta)

    def __call__(self, step: torch.Tensor, is_update_step: torch.Tensor):
        return self.init * torch.pow(self.beta, step.float())


class CosineHyperParameter(BaseHyperParameter):
    """
    Cosine function for oscilating between an initial (maximum) value down to a
    minimum and back to the maximum every period.

    :math:`y(step) = o + a \cdot \cos(step \cdot \pi / half\_period)`, where
    :math:`o = (init + minimum)/2` and :math:`a = init - o`.
    """

    TYPE = "cosine"

    def __init__(self, init, half_period, minimum=0.0):
        # cos(x) mean is 0, compute mean of (init+min)/2
        o = (minimum + init) / 2
        # cos(pi) max is 1, remove offset
        a = init - o

        self.amp = torch.tensor(a)
        self.offset = torch.tensor(o)
        self.freq = torch.tensor(torch.pi / half_period)

    def __call__(self, step: torch.Tensor, is_update_step: torch.Tensor):
        return self.amp * torch.cos(step.float() * self.freq) + self.offset

    def get_min_max_end(
        self, begin: int, end: int
    ) -> Tuple[float, float, float]:
        min_value = (-self.amp + self.offset).item()
        max_value = (self.amp + self.offset).item()
        end_value = self(torch.tensor(end), torch.tensor(False)).item()
        if max_value < min_value:
            # swap, amp must be negative
            min_value, max_value = max_value, min_value
        return (min_value, max_value, end_value)


class CyclingHyperParameter(BaseHyperParameter):
    """
    Hyper parameter cycling between discrete values at update steps.
    """

    TYPE = "cycling"

    __state_slots__ = ["step"]

    def __init__(self, values):
        self.values = values
        self.step = torch.tensor(0)

    def __call__(self, step: torch.Tensor, is_update_step: torch.Tensor):
        # Terrible unrolled version to work around stack limitations
        v = torch.tensor(self.values[0], device=step.device)
        for i, vi in enumerate(self.values):
            vi = torch.tensor(vi, device=step.device)
            step_is_i = self.step == i
            v = torch.where(step_is_i, vi, v)
        self.step = torch.where(
            is_update_step, torch.where(step_is_i, 0, self.step + 1), self.step
        )

        return v

    def get_min_max_end(
        self, begin: int, end: int
    ) -> Tuple[float, float, float]:
        # Technically not an "end" since it cycles, so assume its cycled
        # completely by the end of dynamic updates.
        return (min(self.values), max(self.values), self.values[-1])


class LambdaHyperParameter(BaseHyperParameter):
    """
    Invoke a user's lambda function of step to obtain the hyper parameter.
    """

    TYPE = "lambda"

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, step: torch.Tensor, is_update_step: torch.Tensor):
        return self.fn(step)

    def get_min_max_end(
        self, begin: int, end: int
    ) -> Tuple[float, float, float]:
        # Can't asses any statistics of a user provided lambda
        return None


HyperParameterCallable = Callable[[torch.Tensor, torch.Tensor], torch.Tensor]
HyperParameterType = Union[
    int,
    float,
    List[int],
    List[float],
    Tuple,
    Dict,
    HyperParameterCallable,
    BaseHyperParameter,
]


def initialize_hyperparam(param):
    """
    Given some user specified configuration, construct a BaseHyperParameter
    class that is step aware.
    """
    if isinstance(param, BaseHyperParameter):
        return param
    if isinstance(param, (int, float)):
        return ConstantHyperParameter(param)
    if isinstance(param, (list, tuple)):
        return CyclingHyperParameter(param)
    if callable(param):
        signature = inspect.signature(param)
        if signature_matches_type_hint(signature, HyperParameterCallable):
            return LambdaHyperParameter(param)
    if isinstance(param, dict):
        param = param.copy()
        typename = param.pop("type")
        if not typename:
            raise ValueError("Must specify `type`")
        return BaseHyperParameter.get_cls(typename)(**param)
    valid_types = list(BaseHyperParameter.TYPE_REGISTRY.keys())
    raise ValueError(
        f"Unhandled {param}. Options are:\n"
        f"* int/float: ConstantHyperParameter\n"
        f"* list[int/float]: CyclingHyperParameter\n"
        f"* Callable: LambdaHyperParameter\n"
        f"* BaseHyperParameter: used as-is\n"
        f"* {{\"type\": ...}} as one of {valid_types}"
    )


def set_param_group_hyperparam(param_group, name):
    """
    Updates the param_group option inplace as a hyperparam.
    """
    try:
        param_group[name] = initialize_hyperparam(param_group[name])
    except ValueError as e:
        raise ValueError(
            f"While constructing {name} from {param_group[name]}: {e.args[0]}"
        )


UnshaperCallable = Callable[[torch.Tensor], torch.Tensor]
ShaperReturn = Tuple[torch.Tensor, UnshaperCallable]
ShaperCallable = Callable[[torch.Tensor], ShaperReturn]


class ScoreShaper(ABC):
    @abstractmethod
    def __call__(self, tensor: torch.Tensor) -> ShaperReturn:
        """
        Given a tensor, such as a score or mask, reshape it so that the inner
        dimension is the one over which magnitudes should be compared.

        Args:
            tensor: Will be reshaped so that the inner dimension
        Returns:
            tuple containing:
                - reshaped ``tensor``
                - Callable to reverse this shaper.

        """


class ScoreFlattener(ScoreShaper):
    """
    Default ScoreShaper which everything is flattened, providing a global
    competition for magnitude. If only sub-portions of the weight should
    compete for magnitude, provide an alternative shaper object.
    """

    def __call__(self, tensor: torch.Tensor) -> ShaperReturn:
        def unshaper(ret: torch.Tensor) -> torch.Tensor:
            return ret.view(tensor.shape)

        return tensor.view(-1), unshaper


class OutputGroupScoreShaper(ScoreShaper):
    """
    A ScoreShaper interface when weights are logically shaped as
    [num_groups*out_per_group, insize], but need to be scored in a "balanced"
    fashion as [num_groups, out_per_group*insize]

    Examples:

        >>> # Common score used for the following examples
        >>> score=torch.tensor([[1.0, 2.0],
        ...                     [0.0, -1.0]])

        >>> # 50% sparsity, drops the 2 lowest magnitude
        >>> make_mask_topk_sparsity(
        ...     score=score,
        ...     sparsity=torch.tensor(0.5),
        ... )
        tensor([[ True,  True],
                [False, False]])

        >>> # 50% sparsity, but computed rowwise
        >>> make_mask_topk_sparsity(
        ...     score=score,
        ...     sparsity=torch.tensor(0.5),
        ...     score_shaper=OutputGroupScoreShaper(num_groups=2)
        ... )
        tensor([[False,  True],
                [ True, False]])
    """

    def __init__(self, num_groups):
        self.num_groups = num_groups

    def __call__(self, tensor: torch.Tensor) -> ShaperReturn:
        def unshaper(ret: torch.Tensor) -> torch.Tensor:
            return ret.view(tensor.shape)

        return tensor.view(self.num_groups, -1), unshaper


class InputGroupScoreShaper(ScoreShaper):
    """
    A ScoreShaper interface when weights are logically shaped as
    [outsize, num_groups*in_per_group], but need to be scored in a "balanced"
    fashion as [num_groups, outsize*in_per_group]

    Examples:

        >>> # Common score used for the following examples
        >>> score=torch.tensor([[1.0, 0.0],
        ...                     [2.0, -1.0]])

        >>> # 50% sparsity, drops the 2 lowest magnitude
        >>> make_mask_topk_sparsity(
        ...     score=score,
        ...     sparsity=torch.tensor(0.5),
        ... )
        tensor([[ True, False],
                [ True, False]])

        >>> # 50% sparsity, but computed columnwise
        >>> make_mask_topk_sparsity(
        ...     score=score,
        ...     sparsity=torch.tensor(0.5),
        ...     score_shaper=InputGroupScoreShaper(num_groups=2)
        ... )
        tensor([[False,  True],
                [ True, False]])
    """

    def __init__(self, num_groups):
        self.num_groups = num_groups

    def __call__(self, tensor: torch.Tensor) -> ShaperReturn:
        O, I = tensor.shape
        # Swap [O,I] -> [I, O] and flatten [N, I/N*O]
        ret = tensor.permute(1, 0).reshape(self.num_groups, -1)

        def unshaper(ret: torch.Tensor) -> torch.Tensor:
            # flatten [N, I/N*O] -> [I, O] then swap to [O, I]
            return ret.view(I, O).permute(1, 0).contiguous()

        return ret, unshaper


def make_mask_drop_minimum(
    score: torch.FloatTensor,
    mask: torch.BoolTensor,
    drop_fraction: torch.FloatTensor,
    score_shaper: Optional[ShaperCallable] = None,
) -> torch.BoolTensor:
    """
    Given a sparse ``score`` (with ``mask``), return a new ``torch.BoolTensor``
    the same shape as `mask` where a ``drop_fraction`` portion of the currently
    present (``mask==True``) connections are dropped (``mask==False``).

    The connections are dropped at positions corresponding to the `lowest`
    values of ``score``.

    Equivalently, a subset of ``mask`` is returned corresponding to the
    `highest` magnitude elements of ``score``.

    Args:
        score: Values used to evaluate which positions to drop
        mask: Current connections, same shape as ``score``
        drop_fraction: What fraction of current connections to drop
        score_shaper: If given, ``score`` (and ``mask``) will be interpreted as
            multiple independent subtensors. This can be used to ensure
            sparsity distribution is "balanced" or to produce blockwise
            sparsity. By default, ``score`` and ``mask`` are reinterpreted as
            1D tensors, yielding completely unstructured sparsity.

    Returns:
        New mask that has existing connections dropped. No connections will be
        regrown (unless drop_fraction is negative).
    """
    if not score_shaper:
        score_shaper = ScoreFlattener()
    score, unshape = score_shaper(score)

    # Compute total remaining dense elements kept after dropping a certain
    # fraction of current connections.
    keep_fraction = 1 - drop_fraction
    current_k = mask.sum().float()

    # Divide the dropping evenly among groups if the score has them.
    groups = 1
    for dim in score.size()[:-1]:
        groups *= dim
    current_k /= groups
    num_dense_elem = (keep_fraction * current_k).int()
    # Return the new mask and the number of dense elements (often needed for
    # make_mask_grow_maximum with target sparsity)
    new_mask = unshape(_make_mask_topk_k(score, num_dense_elem))
    return new_mask, num_dense_elem


def make_mask_grow_maximum(
    score: torch.FloatTensor,
    mask: torch.BoolTensor,
    sparsity: torch.FloatTensor,
    mask_nonzero: Optional[torch.IntTensor] = None,
    score_shaper: Optional[ShaperCallable] = None,
) -> torch.BoolTensor:
    """
    Given a sparse ``score`` (with ``mask``), return a new torch.BoolTensor the
    same shape as ``mask`` where some currently pruned connections are regrown
    (from those positions with the highest score) such that the returned mask
    has the given target sparsity.

    If ``mask`` is already less sparse (has more connections) than the target,
    none are regrown and the original mask is returned as-is. That is, the
    given ``mask`` should be `more` sparse than the target sparsity.

    Args:
        score: Values used to evaluate which positions to regrow
        mask: Current connections, same shape as ``score``
        drop_fraction: What fraction of current connections to drop
        mask_nonzero: If given, the number of nonzero elements currently in the
            mask, used to control the number of connections needing regrowth.
            If it is not given, will be computed as ``mask.nonzero().int()``.
            Since ``make_mask_grow_maximum`` is often used in conjunction with
            ``make_mask_drop_minimum``, this value is commonly available.
        score_shaper: If given, ``score`` (and ``mask``) will be interpreted as
            multiple independent subtensors. This can be used to ensure
            sparsity distribution is "balanced" or to produce blockwise
            sparsity. By default, ``score`` and ``mask`` are reinterpreted as
            1D tensors, yielding completely unstructured sparsity.

    Returns:
        New mask that has connections regrown necessary to reach (decrease to)
        the target sparsity.
    """
    # Ensure mask and grow_mask are in fact disjoint (i.e. this function _only_
    # grows) by disqualifying any non-pruned score elements.
    score = torch.where(mask, float('-inf'), score)

    if not score_shaper:
        score_shaper = ScoreFlattener()
    score, unshape = score_shaper(score)

    # Regrow connections to reach the target sparsity.
    density = 1 - sparsity
    numel = torch.tensor(score.size(dim=-1), dtype=torch.float)
    num_dense_elem = (density * numel).int()

    # The final mask needs a total of num_dense_elem connections and will be
    # the union of 2 disjoint masks mask|grow_mask, so compute the size of
    # grow_mask.
    if mask_nonzero is None:
        mask_nonzero = mask.sum().int()
    num_grow_elem = torch.clamp(num_dense_elem - mask_nonzero, min=0)

    # Find the positions of the highest magnitude score needed to reach the
    # target sparsity after regrowing.
    grow_mask = unshape(_make_mask_topk_k(score, num_grow_elem))

    # Return the combined mask and grow_mask
    return mask.logical_or(grow_mask)


def make_mask_topk_sparsity(
    score: torch.FloatTensor,
    sparsity: torch.FloatTensor,
    score_shaper: Optional[ShaperCallable] = None,
) -> torch.BoolTensor:
    """
    Given a dense ``score``, return a ``torch.BoolTensor`` which is True at
    positions corresponding to values in the top ``k =
    (1-sparsity)*score.numel()`` of ``score``.

    Args:
        score: Values used to evaluate which positions to keep.
        sparisty: rankless tensor in range [0,1] controlling fraction of the
            resulting mask that will be pruned.
        score_shaper: If given, ``score`` will be interpreted as multiple
            independent subtensors. This can be used to ensure sparsity
            distribution is "balanced" or to produce blockwise sparsity. By
            default, ``score`` is reinterpreted as a 1D tensor, yielding
            completely unstructured sparsity.

    Returns:
        ``mask`` with given ``sparsity``, keeping only the highest values from
        ``score``.

    Examples:

        >>> # Common score used for the following examples
        >>> score=torch.tensor([[1.0, 2.0],
        ...                     [0.0, -1.0]])

        >>> # 25% sparsity, drops the one lowest magnitude
        >>> make_mask_topk_sparsity(
        ...     score=score,
        ...     sparsity=torch.tensor(0.25),
        ... )
        tensor([[ True,  True],
                [ True, False]])

        >>> # 75% sparsity, drops the 3 lowest magnitude
        >>> make_mask_topk_sparsity(
        ...     score=score,
        ...     sparsity=torch.tensor(0.75),
        ... )
        tensor([[False,  True],
                [False, False]])
    """
    if not score_shaper:
        score_shaper = ScoreFlattener()
    score, unshape = score_shaper(score)

    density = 1 - sparsity
    numel = torch.tensor(score.size(dim=-1), dtype=torch.float)
    num_dense_elem = (density * numel).int()
    new_mask = _make_mask_topk_k(score, num_dense_elem)
    return unshape(new_mask)


def _make_mask_topk_k(
    score: torch.FloatTensor, num_dense_elem: torch.IntTensor,
) -> torch.BoolTensor:
    if cstorch.use_cs():
        # `torch.topk` uses a python integer for the `k` operand, which will
        # change throughout training. Even though this integer is computed from
        # tensors (the sparsity schedule), calling .item() on it breaks the
        # ability to trace the dataflow.
        # Since we only trace the program once, this prevents us from using
        # `torch.topk. Although even if it somehow did accept a traceable
        # tensor for `k`, the result would not be statically shaped, causing
        # other issues.

        # Instead, sort the whole tensor...
        indices = torch.sort(score, dim=-1, descending=True).indices
        # .. and mask off all but the first k indices, replacing them with the
        # largest(0th) index. This works even if num_dense_elem == numel.
        iota = torch.arange(
            indices.shape[-1],
            dtype=num_dense_elem.dtype,
            device=num_dense_elem.device,
        )
        in_topk = iota < num_dense_elem
        indices = torch.where(in_topk, indices, indices[..., 0:1])
    else:
        # CPU/GPU
        _, indices = torch.topk(score, num_dense_elem.item(), dim=-1)

    mask = torch.zeros_like(score, dtype=torch.bool)
    # expand necessary due to bug in TorchScript
    src_opt = torch.tensor(True, dtype=mask.dtype, device=mask.device).expand(
        mask.shape
    )
    mask = mask.scatter(-1, indices, src_opt)
    return mask

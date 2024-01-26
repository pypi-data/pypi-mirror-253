# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

""" Tensor related utilities """
from contextlib import contextmanager

import torch


@contextmanager
def conditional_update(tensor, condition):
    """Update the tensor on context manager exit if the condition is true"""
    unchanged = tensor.clone()
    yield  # go change tensor
    with torch.no_grad():
        tensor.copy_(torch.where(condition, tensor, unchanged))

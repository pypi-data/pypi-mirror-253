# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

from contextlib import contextmanager


class BooleanContext:
    def __init__(self, default: bool):
        self.value = default

    def __bool__(self):
        return self.value

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value}) @ {id(self):#x}"

    @contextmanager
    def __call__(self, value: bool):
        """Temporarily set the value of the context manager"""
        old_value = self.value
        self.value = value
        try:
            yield
        finally:
            self.value = old_value

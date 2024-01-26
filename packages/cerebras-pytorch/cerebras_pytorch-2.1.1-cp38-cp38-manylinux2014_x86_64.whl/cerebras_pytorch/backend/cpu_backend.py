# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

""" Contains the CPU backend subclass """
from collections import defaultdict
from contextlib import nullcontext
from pathlib import Path
from typing import Optional

from cerebras_appliance.log import ClassLogger, named_class_logger
from cerebras_pytorch.amp.autocast import autocast
from cerebras_pytorch.backend.base_backend import BaseBackend
from cerebras_pytorch.core.device import CPUDevice
from cerebras_pytorch.saver.pt_h5_saver import PyTorchH5Saver


@named_class_logger("CpuBackend")
class CpuBackendImpl(BaseBackend, ClassLogger):
    """ The CPU backend subclass """

    def __init__(
        self,
        backend_type,
        artifact_dir: str = None,
        max_checkpoints: Optional[int] = None,
        mixed_precision: bool = False,
    ):
        super().__init__(backend_type, CPUDevice())
        if artifact_dir is not None:
            self.config.artifact_dir = Path(artifact_dir)
            self.config.artifact_dir.mkdir(parents=True, exist_ok=True)

        self.config.max_checkpoints = max_checkpoints
        self.mixed_precision = mixed_precision

    def on_run_start(self):
        """Runs once at the beginning of the run

        Used by cstorch.utils.data.DataLoader
        """
        super().on_run_start()
        self.run_step_closures()

    def on_batch_start(self, batch):
        """Used by cstorch.utils.data.DataLoader"""
        # Clear debug_name call counters.
        self._debug_name_call_counters = defaultdict(int)
        self._pre_fwd_scope_names = defaultdict(list)

        self._is_tracing = True
        return batch

    def forward(self, *args, **kwargs):
        if self.mixed_precision:
            ctx = autocast()
        else:
            # no-op if cstorch.amp.bfloat16(True) was not called
            ctx = nullcontext()

        with ctx:
            return super().forward(*args, **kwargs)

    def save(self, state_dict, checkpoint_file):  # pylint: disable=no-self-use
        """
        Save the provided state dict to a checkpoint at the provided filepath
        """
        saver = PyTorchH5Saver(max_store=self.config.max_checkpoints)
        saver.save(checkpoint_file, state_dict)

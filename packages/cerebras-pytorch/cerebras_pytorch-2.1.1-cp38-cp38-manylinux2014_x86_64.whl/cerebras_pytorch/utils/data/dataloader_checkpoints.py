# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""Defines the Cerebras DataLoaderCheckpoint dataclass and DataCheckpointManager class."""
import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import dill

from cerebras_appliance import logger


@dataclass
class DataLoaderCheckpoint:
    """Dataclass representing the Cerebras internal dataloader checkpoint format.
    Each CSX Worker captures its state information via this class at a checkpoint
    step.

    Attributes:
        global_worker_id:
            ID of this worker amongst all other workers across all boxes
        local_worker_id:
            ID of this worker amongst all other workers across the same box
        total_num_workers:
            The total number of workers for the run across all boxes
        num_workers_per_csx:
            The total number of workers per box for the run
        num_csx:
            The total number of CSXs (boxes) for the run
        wse_id:
            ID of the Wafer-Scale Engine (CSX) to which this worker streams data
        appliance_step:
            The appliance step at which this checkpoint state info is captured
        worker_step:
            The worker step at which this state info is captured. Note that this
            is simply equal to `appliance_step` if `num_workers_per_csx = 1`;
            for the multi-worker scenario, the appliance step is distributed
            across workers on a single box in a round-robin fashion based on
            the local worker id
        samples_streamed:
            The total number of samples streamed by this worker at checkpoint
            step. This is simply `worker_step` * `per_box_batch_size`

    .. note::
        `appliance_step`, `worker_step` and `samples_streamed` are the attributes
        that vary across different steps; whereas the other attributes provide
        constant state information for the current run.
    """

    global_worker_id: int
    local_worker_id: int
    total_num_workers: int
    num_workers_per_csx: int
    num_csx: int
    wse_id: int
    appliance_step: int
    worker_step: int
    samples_streamed: int

    # User-defined state dict for the CSX Worker. This object must be picklable.
    user_state_dict: Dict[str, Any]

    def save_to_file(self, file_path: str) -> None:
        """Pickles the object and saves it to a file."""
        try:
            with open(file_path, 'wb') as f:
                dill.dump(self, f)
        except Exception as e:
            raise RuntimeError(
                f"Failed to save dataloader checkpoint file {file_path} "
                f"due to error: {e}. Please ensure that the provided state is "
                f"picklable using the `dill` package."
            ) from e

    @classmethod
    def load_from_file(cls, file_path: str,) -> "DataLoaderCheckpoint":
        """Loads the object from a file."""
        try:
            with open(file_path, 'rb') as f:
                return dill.load(f)
        except Exception as e:
            raise RuntimeError(
                f"Failed to read dataloader checkpoint file {file_path} "
                f"due to error: {e}"
            )


class DataCheckpointManager:
    """Class facilitating interactions with dataloader checkpoints."""

    WRK_CKPT_FILE_FMT: str = "dataloader_ckpt_wrk_{worker_id}_step_{step}.pkl"

    def __init__(self, worker_id, data_ckpts_dir_path):
        assert os.path.exists(
            data_ckpts_dir_path
        ), "Invalid path for data loader ckpts dir."
        self.worker_id = worker_id
        self.data_checkpoints_dir_path = data_ckpts_dir_path

    @staticmethod
    def worker_checkpoint_file(
        checkpoints_dir: str, worker_id: int, step: int
    ) -> str:
        """Helper method to construct and return the string literal path
        for the individual worker checkpoint file.

        Args:
            checkpoints_dir: Path of the mounted dir where data checkpoints are saved
            worker_id: The id representing the worker
            step: The step associated with the checkpoint

        Returns:
            A string literal path of the individual worker data checkpoint file.
        """
        worker_ckpt_file = os.path.join(
            checkpoints_dir,
            DataCheckpointManager.WRK_CKPT_FILE_FMT.format(
                worker_id=worker_id, step=step,
            ),
        )
        return worker_ckpt_file

    def save_checkpoint(
        self, worker_ckpt: DataLoaderCheckpoint, step: int
    ) -> None:
        """Saves state for this CSX worker in a checkpoint file. State corresponds
        to the ckpt info held in WRK checkpoint object of type :py:class:`DataLoaderCheckpoint`

        Args:
            worker_ckpt: The worker checkpoint object to save
            step: The step at which the checkpoint is being saved
        """
        worker_ckpt_file = DataCheckpointManager.worker_checkpoint_file(
            checkpoints_dir=self.data_checkpoints_dir_path,
            worker_id=self.worker_id,
            step=step,
        )

        worker_ckpt.save_to_file(worker_ckpt_file)

    def fetch_checkpoint(
        self, step: int, wait: bool = False
    ) -> Optional[DataLoaderCheckpoint]:
        """Fetches state for this CSX worker via reading the checkpoint file.

        Args:
            worker_id: ID of the CSX Worker
            step: The step for the checkpoint
            wait: bool indicating whether to buffer for checkpoint file

        Returns:
            :py:class:`DataLoaderCheckpoint` object corresponding to WRK state
        """
        worker_ckpt_file = DataCheckpointManager.worker_checkpoint_file(
            checkpoints_dir=self.data_checkpoints_dir_path,
            worker_id=self.worker_id,
            step=step,
        )

        # Buffer for WRK ckpt to be written
        if wait:
            start = time.time()
            timeout = 10
            while (
                not os.path.isfile(worker_ckpt_file)
                and (time.time() - start) < timeout
            ):
                time.sleep(0.5)

        if os.path.isfile(worker_ckpt_file):
            return DataLoaderCheckpoint.load_from_file(
                file_path=worker_ckpt_file
            )

        logger.warning(
            f"WRK checkpoint file `{worker_ckpt_file}` at step {step} does not "
            "exist. Returning an empty dataloader checkpoint."
        )
        return None

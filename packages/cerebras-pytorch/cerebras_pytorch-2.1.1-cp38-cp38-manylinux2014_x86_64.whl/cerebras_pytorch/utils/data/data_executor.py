# Copyright 2016-2023 Cerebras Systems
# SPDX-License-Identifier: BSD-3-Clause

"""The executor used to configure the run"""
import math
import os
from contextlib import ExitStack, nullcontext
from threading import Event
from typing import List, Optional, Type

from cerebras_appliance.CSConfig import CSConfig
from cerebras_appliance.log import ClassLogger, named_class_logger
from cerebras_pytorch.backend import current_backend_impl
from cerebras_pytorch.experimental.listener import (
    BaseTensorListener,
    ListenerMode,
)
from cerebras_pytorch.utils.tensorboard import SummaryWriter

from ..profiler import Activity, Profiler
from .dataloader import DataLoader


@named_class_logger
class DataExecutor(ClassLogger):
    """Defines a single execution run on a Cerebras wafer scale cluster"""

    # pylint: disable=super-init-not-called
    def __init__(
        self,
        dataloader: DataLoader,
        num_steps: Optional[int] = None,
        checkpoint_steps: Optional[int] = None,
        activation_steps: Optional[int] = None,
        cs_config: Optional[CSConfig] = None,
        writer: Optional[SummaryWriter] = None,
        profiler_activities: Optional[List[Type[Activity]]] = None,
        listeners: Optional[List[BaseTensorListener]] = None,
    ):
        """
        Args:
            dataloader: the dataloader to use for the run
            num_steps: the number of steps to run. Defaults to 1 if the backend
                was configured for compile or validate only
            checkpoint_steps: the interval at which to schedule fetching
                checkpoints from the cluster
            activation_steps: the interval at which to schedule fetching
                activations from the cluster
            cs_config: optionally, a
                :py:class:`~cerebras_pytorch.utils.CSConfig` object can be passed
                in to configure the cerebras wafer-scale cluster. if none provided
                the default configuration values will be used.
            writer: The summary writer to be used to write any summarized
                scalars or tensors to tensorboard
            profiler_activities: The list of activities to profile.
                By default the total samples, the client side rate and global
                rate are tracked and accessible via the profiler attribute
        """
        self.dataloader = dataloader

        self.backend = current_backend_impl()

        self.listener_mode = ListenerMode(listeners)

        if cs_config and not isinstance(cs_config, CSConfig):
            raise TypeError(
                f"Expected cs_config to be a CSConfig object. "
                f"Got: {type(cs_config)}"
            )

        if writer is not None and not isinstance(writer, SummaryWriter):
            raise TypeError(
                f"Expected writer to be a "
                f"cstorch.utils.tensorboard.SummaryWriter object. "
                f"Got: {type(writer)}"
            )

        if not self.backend.is_e2e_execution:
            if num_steps and num_steps > 1:
                self.logger.warning(
                    "Specified num_steps > 1 when backend was configured "
                    "for compile/validate only. Setting num_steps to 1."
                )
            num_steps = 1
        elif num_steps is None:
            # If num_steps is not specified, we will try to infer the number of
            # steps from the dataloader.
            try:
                num_steps = len(dataloader)
            except TypeError:
                # Dataset length is not known
                raise RuntimeError(
                    "Could not infer the number of steps as the length of the "
                    "dataloader is not known. Please provide num_steps to the data executor"
                )
        elif num_steps < 1:
            raise RuntimeError(f"Expected num_steps >= 1, but got {num_steps}.")

        def check_steps(name, value, lowerbound):
            if value is not None:
                if not isinstance(value, int):
                    raise TypeError(
                        f"Expected {name} to be have \"int\" or \"None\" type. "
                        f"Got: \"{type(activation_steps)}\""
                    )
                if not (
                    value >= lowerbound
                ):  # pylint: disable=superfluous-parens
                    raise RuntimeError(
                        f"Expected {name} to be an integer >= {lowerbound} or \"None\". "
                        f"Got: {value}"
                    )

        # Validate steps parameters
        check_steps("activation_steps", activation_steps, 1)
        check_steps("checkpoint_steps", checkpoint_steps, 0)

        # Sync activation steps with checkpoint steps.
        if activation_steps and checkpoint_steps:
            aligned_activation_steps = math.gcd(
                checkpoint_steps, activation_steps
            )
            if aligned_activation_steps != activation_steps:
                self.logger.warning(
                    f"Activation frequency was reduced from {activation_steps} to "
                    f"{aligned_activation_steps} because of checkpoint_steps ({checkpoint_steps}). "
                    f"This is because some activations may be accessed at checkpoint steps."
                    f"To avoid the reduction make sure that checkpoint_step % log_steps == 0"
                )
                activation_steps = aligned_activation_steps

        # Disable DL state capture if checkpoint_steps is 0 or None
        if not checkpoint_steps:
            self.dataloader.disable_dataloader_checkpointing()

        self.run_context = RunContext(
            dataloader,
            num_steps,
            checkpoint_steps,
            activation_steps,
            cs_config,
            writer,
            profiler_activities,
        )

    def __len__(self) -> int:
        return len(self.run_context)

    @property
    def iteration(self) -> int:
        """Returns the current step that the executor is on"""
        return self.run_context.iteration

    @property
    def on_final_iteration(self) -> bool:
        """Returns whether the executor is on the final step"""
        return self.run_context.is_final_step

    @property
    def profiler(self) -> Optional[Profiler]:
        """Returns the profiler object, if it exists."""
        return self.run_context.profiler

    @property
    def cs_config(self) -> CSConfig:
        """Returns CsConfig object"""
        return self.run_context.cs_config

    def __enter__(self):
        self.backend.serialize_input_fn(
            self.dataloader.input_fn, self.dataloader.input_fn_params
        )

        self.backend.data_executor_stack.append(self)
        self.run_context.__enter__()

        # Load DL state for data checkpointing
        self.dataloader.serialize_state_dict()

        # Communicate DL checkpointing status to appliance
        if self.backend.backend_type.is_csx:
            self.backend.appliance.enable_dataloader_checkpointing = (
                self.dataloader.enable_dataloader_checkpointing
            )

    def __exit__(self, *args):
        self.backend.data_executor_stack.pop()
        self.run_context.__exit__(*args)

    def __iter__(self):
        with self:

            def get_batches():
                while True:
                    iterable = iter(self.dataloader)
                    try:
                        batch = next(iterable)
                    except StopIteration:
                        raise RuntimeError(
                            "Iterating the dataloader did not return any values. "
                            "This is possibly because the dataset is too small "
                            "for the specified batch_size or drop_last settings. "
                            "Please make sure that the dataloader is able to generate "
                            "at least one batch."
                        )

                    yield batch

                    if self.backend.backend_type.is_csx:
                        while True:
                            yield batch

                    try:
                        while True:
                            yield next(iterable)
                    except StopIteration:
                        # If the iterable is exhausted, we need to start again
                        pass

            for _step, batch in zip(self.run_context, get_batches()):
                ctx = self.listener_mode or nullcontext()
                with ctx:
                    yield self.backend.on_batch_start(batch)
                self.backend.on_batch_end()


def current_executor() -> DataExecutor:
    """ Returns current data executor """
    return current_backend_impl().data_executor


class RunContext:
    """Defines a single run of the appliance"""

    def __init__(
        self,
        dataloader: DataLoader,
        num_steps: int,
        checkpoint_steps: Optional[int] = None,
        activation_steps: Optional[int] = None,
        cs_config: Optional[CSConfig] = None,
        writer: Optional[SummaryWriter] = None,
        profiler_activities: Optional[List[Type[Activity]]] = None,
    ):
        self.backend = current_backend_impl()

        if not isinstance(dataloader, DataLoader):
            raise TypeError(
                "Detected that dataloader was not wrapped using a "
                "cstorch.utils.data.DataLoader.\n"
                "Please wrap your dataloader in a Cerebras Dataloader:\n\n"
                "\tdataloader = cstorch.utils.data.DataLoader(input_fn, ...)\n\n"
                "where `input_fn` is a callable that returns a PyTorch dataloader. "
                "For more details, please see the documentation for "
                "cstorch.utils.data.DataLoader."
            )

        self.dataloader = dataloader
        self.num_steps = num_steps
        self.checkpoint_steps = checkpoint_steps or 0
        self.activation_steps = activation_steps or 1

        # Event that keeps track of whether tracing has occurred
        self.traced = Event()

        self.cs_config = cs_config if cs_config else CSConfig()

        self.writer = writer

        self.step = -1
        self.cleanup_stack = None

        self.profiler: Optional[Profiler] = None
        self.profiler_activities = profiler_activities

    @property
    def is_pre_initial_step(self) -> bool:
        """Returns true if the current step less than zero"""
        return self.step < 0

    @property
    def is_initial_step(self) -> bool:
        """Returns true if the current step is zero"""
        return self.step == 0

    @property
    def is_final_step(self) -> bool:
        """Returns true if the current step is the final step"""
        return self.user_iteration >= self.num_steps

    @property
    def is_checkpoint_step(self) -> bool:
        """Returns true if the current step is a checkpoint step"""
        return self.checkpoint_steps and (
            self.user_iteration % self.checkpoint_steps == 0
            or self.is_final_step
        )

    @property
    def is_activation_step(self) -> bool:
        """Returns true if the current step is an activation step

        Technically when iteration = 0 the condition iteration % freq == 0 is true, however on the
        appliance side the activation is not available. To have correct iteration indexing we need
        to check that user_iteration % activation_steps == 0, where user_itaration = iteration + 1,
        otherwise in case we have 4 iterations [0, 1, 2, 3] and activation_steps = 2 we will get
        only one activation from the iteration=2, however we should return activations from
        iterations [1, 3].
        """
        assert self.activation_steps > 0  # Already validated in the constructor
        return (
            self.user_iteration % self.activation_steps == 0
            or self.is_final_step
        )

    @property
    def iteration(self) -> int:
        """Returns current step"""
        return self.step

    @property
    def user_iteration(self) -> int:
        """Returns user facing iteration number """
        return self.step + 1

    def __len__(self) -> int:
        return self.num_steps

    def __enter__(self):
        self.step = -1  # set step < 0 before the run starts
        self.backend.on_run_start()
        self.step = 0  # set step to 0 as we enter the context
        self.cleanup_stack = ExitStack()
        self.cleanup_stack.__enter__()

        if self.backend.is_e2e_execution:
            self.profiler = Profiler(
                outdir=os.path.join(
                    self.backend.config.artifact_dir, "performance"
                ),
                activities=self.profiler_activities,
            )
            self.profiler.__enter__()

    def __exit__(self, *args):
        self.cleanup_stack.__exit__(*args)
        self.backend.on_run_end()
        self.cleanup_stack = None

        if self.profiler is not None:
            self.profiler.__exit__(*args)

    def __iter__(self):
        # sanity check as the user should never use RunContext directly
        assert self.cleanup_stack is not None

        while self.step < self.num_steps:
            yield self.step
            self.step += 1

            if self.backend.retrace_every_iteration:
                self.traced.clear()

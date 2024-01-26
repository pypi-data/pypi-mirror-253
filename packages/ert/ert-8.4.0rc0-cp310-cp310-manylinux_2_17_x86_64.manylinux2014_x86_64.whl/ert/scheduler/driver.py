from __future__ import annotations

import asyncio
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Tuple


class JobEvent(Enum):
    STARTED = 0
    COMPLETED = 1
    FAILED = 2
    ABORTED = 3


class Driver(ABC):
    """Adapter for the HPC cluster."""

    def __init__(self) -> None:
        self._event_queue: Optional[asyncio.Queue[Tuple[int, JobEvent]]] = None

    @property
    def event_queue(self) -> asyncio.Queue[Tuple[int, JobEvent]]:
        if self._event_queue is None:
            self._event_queue = asyncio.Queue()
        return self._event_queue

    @abstractmethod
    async def submit(self, iens: int, executable: str, /, *args: str, cwd: str) -> None:
        """Submit a program to execute on the cluster.

        Args:
          iens: Realization number. (Unique for each job)
          executable: Program to execute.
          args: List of arguments to send to the program.
          cwd: Working directory.
        """

    @abstractmethod
    async def kill(self, iens: int) -> None:
        """Terminate execution of a job associated with a realization.

        Args:
          iens: Realization number.
        """

    @abstractmethod
    async def poll(self) -> None:
        """Poll for new job events"""

    @abstractmethod
    async def finish(self) -> None:
        """make sure that all the jobs / realizations are complete."""

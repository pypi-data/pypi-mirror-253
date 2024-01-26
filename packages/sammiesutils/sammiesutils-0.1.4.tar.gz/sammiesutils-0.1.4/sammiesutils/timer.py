"""A simple timer context manager."""

from __future__ import annotations

import time
from types import TracebackType


class Timer:
    """A simple timer."""

    def __init__(self, print_elapsed: bool = False) -> None:
        """Create a Timer."""
        self.print_elapsed = print_elapsed
        self._elapsed: float | None = None

    def __repr__(self) -> str:
        """Represent Timer as string."""
        return f"Timer(elapsed={self.elapsed})"

    def __enter__(self) -> Timer:
        """Start timer."""
        self._start_time = time.perf_counter()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Stop timer."""
        self._elapsed = time.perf_counter() - self._start_time
        if self.print_elapsed:
            print(f"{self._elapsed} seconds elapsed.")

    @property
    def elapsed(self) -> float:
        """Seconds elapsed."""
        return (
            self._elapsed
            if self._elapsed is not None
            else time.perf_counter() - self._start_time
        )

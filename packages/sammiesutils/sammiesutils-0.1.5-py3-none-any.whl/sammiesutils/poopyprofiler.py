"""Shitty profiler."""

import functools
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, ParamSpec, TypeVar, cast

from .timer import Timer

P = ParamSpec("P")
R = TypeVar("R")


@dataclass
class Profile:
    """Profiler results for decorated functions."""

    func: Callable[[Any], Any]
    calls: int = 0
    execution_times: list[float] = field(default_factory=list)

    def __repr__(self) -> str:
        """Represent profile as string."""
        return (
            f"Profile(func={self.func.__name__}, calls={self.calls}, "
            f"time_per_call={self.time_per_call:.4f}, total_time={self.total_time:.4f})"
        )

    @property
    def total_time(self) -> float:
        """Total time spent in function across all calls."""
        return sum(self.execution_times)

    @property
    def time_per_call(self) -> float:
        """Average time spent in function per call."""
        return (
            self.total_time / length if (length := len(self.execution_times)) > 0 else 0
        )


class PoopyProfiler:
    """
    A shitty profiler that just times and records calls of functions decorated with
    PoopyProfiler.register.
    """

    def __init__(self) -> None:
        """Create a PoopyProfiler."""
        self._funcs: dict[Callable[[Any], Any], Profile] = {}


    def __getitem__(self, item: Callable[[Any], Any]) -> Profile:
        """Retrieve profiling data for a decorated/registered function."""
        return self._funcs[item]

    def register(self, func: Callable[P, R]) -> Callable[P, R]:
        """Register decorated function with profiler."""

        @functools.wraps(func)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            profile = self._funcs[_wrapper]
            profile.calls += 1
            with Timer() as timer:
                result = func(*args, **kwargs)
            profile.execution_times.append(timer.elapsed)
            return result

        self._funcs[_wrapper] = Profile(_wrapper)
        return _wrapper

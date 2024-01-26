"""Typed wrappers for functools.cache and functools.lru_cache decorators."""

import functools
from collections.abc import Callable
from typing import ParamSpec, TypeVar, cast

P = ParamSpec("P")
R = TypeVar("R")


def cache(func: Callable[P, R]) -> Callable[P, R]:
    """functools.cache wrapper with typed signature."""

    @functools.wraps(func)
    @functools.cache
    def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)

    return cast(Callable[P, R], _wrapper)


def lru_cache(
    maxsize: int = 128, typed: bool = False
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """functools.lru_cache wrapper with typed signature."""

    def _lru_cache(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        @functools.lru_cache(maxsize, typed)
        def _wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            return func(*args, **kwargs)

        return cast(Callable[P, R], _wrapper)

    return _lru_cache

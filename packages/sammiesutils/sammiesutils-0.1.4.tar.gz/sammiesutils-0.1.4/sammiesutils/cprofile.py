"""Shitty pstats."""

import functools
import re
from typing import TypedDict

_READ_TABLE_LINE_PATTERN = (
    r"\s*(?P<ncalls_total>\d+)(?:/(?P<ncalls_primitive>\d+))?\s*"
    r"(?P<tottime>\d+\.\d+)\s*(?P<tottime_percall>\d+\.\d+)\s*(?P<cumtime>\d+\.\d+)\s*"
    r"(?P<cumtime_percall>\d+\.\d+)\s*(?P<filename>[^:]+):(?P<lineno>\d+)\((?P<function>.+)\)"
)


class FieldNotFoundError(Exception):
    """Raised when a regex capture fails to find a field from CProfile output."""


class CProfileRow(TypedDict):
    """A table row from a CProfile output table."""

    ncalls_total: int
    ncalls_primitive: int | None
    tottime: float
    tottime_percall: float
    cumtime: float
    cumtime_percall: float
    filename: str
    lineno: int
    function: str
    cumtime_to_elapsed_proportion: float


class _UnprocessedRow(TypedDict):
    ncalls_total: str
    ncalls_primitive: str | None
    tottime: str
    tottime_percall: str
    cumtime: str
    cumtime_percall: str
    filename: str
    lineno: str
    function: str


class CProfileStats:
    """
    Analyze CProfile outputs from a string.
    To get outputs as string, see: https://stackoverflow.com/questions/51536411/saving-cprofile-results-to-readable-external-file.
    """

    def __init__(self, cp_output: str) -> None:
        """Create a CProfileStats object."""
        self._text = cp_output

    def _convert_row_types(self, row_dict: _UnprocessedRow) -> CProfileRow:
        output: CProfileRow = {
            "ncalls_total": int(row_dict["ncalls_total"]),
            "ncalls_primitive": int(val)
            if (val := row_dict["ncalls_primitive"])
            else None,
            "tottime": float(row_dict["tottime"]),
            "tottime_percall": float(row_dict["tottime_percall"]),
            "cumtime": (cumtime := float(row_dict["cumtime"])),
            "cumtime_percall": float(row_dict["cumtime_percall"]),
            "filename": row_dict["filename"],
            "lineno": int(row_dict["lineno"]),
            "function": row_dict["function"],
            "cumtime_to_elapsed_proportion": cumtime / self.elapsed,
        }
        return output

    @property
    def text(self) -> str:
        """Get original input text."""
        return self._text

    @functools.cached_property
    def elapsed(self) -> float:
        """Seconds elapsed."""
        if match := re.search(r"(\d+\.\d+) seconds elapsed.", self._text):
            return float(match.group(1))
        else:
            raise FieldNotFoundError

    @functools.cached_property
    def function_calls(self) -> int:
        """Number of total function calls."""
        if match := re.search(r"(\d+) function calls", self._text):
            return int(match.group(1))
        else:
            raise FieldNotFoundError

    @functools.cached_property
    def primitive_function_calls(self) -> int:
        """Number of primitive function calls."""
        if match := re.search(r"\((\d+) primitive calls\)", self._text):
            return int(match.group(1))
        else:
            raise FieldNotFoundError

    @functools.cached_property
    def dicts(self) -> list[CProfileRow]:
        """Convert table text to a list of dictionaries."""
        rows = []
        for line in self._text.splitlines():
            if match := re.search(_READ_TABLE_LINE_PATTERN, line):
                rows.append(self._convert_row_types(match.groupdict()))  # type: ignore
        return rows

"""Some tools."""

from importlib.metadata import PackageNotFoundError, version

__version__: str | None

try:
    __version__ = version("sammiesutils")
except PackageNotFoundError:
    __version__ = None

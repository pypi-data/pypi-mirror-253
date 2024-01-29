# pylint: disable=wrong-import-position
"""Synthesized SDK3."""
try:
    from .version import __version__
except ModuleNotFoundError:
    from importlib_metadata import version as _get_version

    __version__ = _get_version("synthesized3")

from synthesized3.utils import warnings_utils

warnings_utils.apply_third_party_warnings_env_var()  # before any other synthesized3 imports

from synthesized3 import _licence

from .column_type import ColumnType
from .data_interface import DataInterfaceFactory, PandasDataInterface, SparkDataInterface
from .nature import Nature
from .synthesizer import TableSynthesizer

__all__ = [
    "ColumnType",
    "DataInterfaceFactory",
    "Nature",
    "PandasDataInterface",
    "TableSynthesizer",
    "SparkDataInterface",
    "_licence",
]

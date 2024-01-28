"""Synthesized data interfaces."""
from . import pandas_utils
from .pandas_data_interface import PandasDataInterface
from .spark_data_interface import SparkDataInterface

__all__ = [
    "PandasDataInterface",
    "SparkDataInterface",
    "pandas_utils",
]

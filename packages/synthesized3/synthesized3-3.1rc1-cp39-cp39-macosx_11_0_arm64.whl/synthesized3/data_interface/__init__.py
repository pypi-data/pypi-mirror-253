"""Module for data interfaces."""
from .data_interface import DataInterface, _replace_spaces
from .data_interface_factory import DataInterfaceFactory
from .data_interfaces import PandasDataInterface, SparkDataInterface

__all__ = [
    "DataInterface",
    "PandasDataInterface",
    "SparkDataInterface",
    "DataInterfaceFactory",
    "_replace_spaces",
]

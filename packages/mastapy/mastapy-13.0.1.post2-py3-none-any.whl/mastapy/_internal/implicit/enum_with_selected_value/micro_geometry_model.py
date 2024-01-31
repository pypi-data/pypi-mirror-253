"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears import _337
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_MicroGeometryModel",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_MicroGeometryModel")


class EnumWithSelectedValue_MicroGeometryModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryModel

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryModel' types.
    """

    __qualname__ = "MicroGeometryModel"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_337.MicroGeometryModel":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _337.MicroGeometryModel

    @classmethod
    def implicit_type(cls) -> "_337.MicroGeometryModel.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _337.MicroGeometryModel.type_()

    @property
    def selected_value(self: Self) -> "_337.MicroGeometryModel":
        """mastapy.gears.MicroGeometryModel

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_337.MicroGeometryModel]":
        """List[mastapy.gears.MicroGeometryModel]

        Note:
            This property is readonly.
        """
        return None

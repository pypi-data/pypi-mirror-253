"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis import _91
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ValueInputOption",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ValueInputOption")


class EnumWithSelectedValue_ValueInputOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ValueInputOption

    A specific implementation of 'EnumWithSelectedValue' for 'ValueInputOption' types.
    """

    __qualname__ = "ValueInputOption"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_91.ValueInputOption":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _91.ValueInputOption

    @classmethod
    def implicit_type(cls) -> "_91.ValueInputOption.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _91.ValueInputOption.type_()

    @property
    def selected_value(self: Self) -> "_91.ValueInputOption":
        """mastapy.nodal_analysis.ValueInputOption

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_91.ValueInputOption]":
        """List[mastapy.nodal_analysis.ValueInputOption]

        Note:
            This property is readonly.
        """
        return None

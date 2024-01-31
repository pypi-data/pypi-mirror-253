"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.utility.enums import _1822
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection",)


Self = TypeVar(
    "Self", bound="EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection"
)


class EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionFirstSelection' types.
    """

    __qualname__ = "ThreeDViewContourOptionFirstSelection"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1822.ThreeDViewContourOptionFirstSelection":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1822.ThreeDViewContourOptionFirstSelection

    @classmethod
    def implicit_type(cls) -> "_1822.ThreeDViewContourOptionFirstSelection.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1822.ThreeDViewContourOptionFirstSelection.type_()

    @property
    def selected_value(self: Self) -> "_1822.ThreeDViewContourOptionFirstSelection":
        """mastapy.utility.enums.ThreeDViewContourOptionFirstSelection

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(
        self: Self,
    ) -> "List[_1822.ThreeDViewContourOptionFirstSelection]":
        """List[mastapy.utility.enums.ThreeDViewContourOptionFirstSelection]

        Note:
            This property is readonly.
        """
        return None

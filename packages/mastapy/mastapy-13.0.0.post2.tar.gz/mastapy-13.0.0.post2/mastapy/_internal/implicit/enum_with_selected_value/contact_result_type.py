"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.gears.ltca import _827
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_ContactResultType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_ContactResultType")


class EnumWithSelectedValue_ContactResultType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ContactResultType

    A specific implementation of 'EnumWithSelectedValue' for 'ContactResultType' types.
    """

    __qualname__ = "ContactResultType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_827.ContactResultType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _827.ContactResultType

    @classmethod
    def implicit_type(cls) -> "_827.ContactResultType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _827.ContactResultType.type_()

    @property
    def selected_value(self: Self) -> "_827.ContactResultType":
        """mastapy.gears.ltca.ContactResultType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_827.ContactResultType]":
        """List[mastapy.gears.ltca.ContactResultType]

        Note:
            This property is readonly.
        """
        return None

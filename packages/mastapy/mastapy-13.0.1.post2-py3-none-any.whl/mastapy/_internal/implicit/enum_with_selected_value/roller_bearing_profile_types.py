"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.bearings import _1891
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_RollerBearingProfileTypes",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_RollerBearingProfileTypes")


class EnumWithSelectedValue_RollerBearingProfileTypes(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_RollerBearingProfileTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RollerBearingProfileTypes' types.
    """

    __qualname__ = "RollerBearingProfileTypes"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1891.RollerBearingProfileTypes":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1891.RollerBearingProfileTypes

    @classmethod
    def implicit_type(cls) -> "_1891.RollerBearingProfileTypes.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1891.RollerBearingProfileTypes.type_()

    @property
    def selected_value(self: Self) -> "_1891.RollerBearingProfileTypes":
        """mastapy.bearings.RollerBearingProfileTypes

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1891.RollerBearingProfileTypes]":
        """List[mastapy.bearings.RollerBearingProfileTypes]

        Note:
            This property is readonly.
        """
        return None

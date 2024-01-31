"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1411
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_SplineFitClassType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_SplineFitClassType")


class EnumWithSelectedValue_SplineFitClassType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineFitClassType

    A specific implementation of 'EnumWithSelectedValue' for 'SplineFitClassType' types.
    """

    __qualname__ = "SplineFitClassType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_1411.SplineFitClassType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1411.SplineFitClassType

    @classmethod
    def implicit_type(cls) -> "_1411.SplineFitClassType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1411.SplineFitClassType.type_()

    @property
    def selected_value(self: Self) -> "_1411.SplineFitClassType":
        """mastapy.detailed_rigid_connectors.splines.SplineFitClassType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_1411.SplineFitClassType]":
        """List[mastapy.detailed_rigid_connectors.splines.SplineFitClassType]

        Note:
            This property is readonly.
        """
        return None

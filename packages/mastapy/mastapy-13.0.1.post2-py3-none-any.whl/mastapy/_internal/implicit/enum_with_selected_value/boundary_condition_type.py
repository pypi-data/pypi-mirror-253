"""Implementations of 'EnumWithSelectedValue' in Python.

As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""
from __future__ import annotations

from enum import Enum
from typing import List, TypeVar

from mastapy.nodal_analysis.fe_export_utility import _165
from mastapy._internal import mixins
from mastapy._internal.python_net import python_net_import

_ARRAY = python_net_import("System", "Array")
_ENUM_WITH_SELECTED_VALUE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "EnumWithSelectedValue"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnumWithSelectedValue_BoundaryConditionType",)


Self = TypeVar("Self", bound="EnumWithSelectedValue_BoundaryConditionType")


class EnumWithSelectedValue_BoundaryConditionType(
    mixins.EnumWithSelectedValueMixin, Enum
):
    """EnumWithSelectedValue_BoundaryConditionType

    A specific implementation of 'EnumWithSelectedValue' for 'BoundaryConditionType' types.
    """

    __qualname__ = "BoundaryConditionType"

    @classmethod
    def wrapper_type(cls) -> "_ENUM_WITH_SELECTED_VALUE":
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> "_165.BoundaryConditionType":
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _165.BoundaryConditionType

    @classmethod
    def implicit_type(cls) -> "_165.BoundaryConditionType.type_()":
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _165.BoundaryConditionType.type_()

    @property
    def selected_value(self: Self) -> "_165.BoundaryConditionType":
        """mastapy.nodal_analysis.fe_export_utility.BoundaryConditionType

        Note:
            This property is readonly.
        """
        return None

    @property
    def available_values(self: Self) -> "List[_165.BoundaryConditionType]":
        """List[mastapy.nodal_analysis.fe_export_utility.BoundaryConditionType]

        Note:
            This property is readonly.
        """
        return None

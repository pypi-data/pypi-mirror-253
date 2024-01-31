"""CylindricalGearSetLoadCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.load_case import _874
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Cylindrical", "CylindricalGearSetLoadCase"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetLoadCase",)


Self = TypeVar("Self", bound="CylindricalGearSetLoadCase")


class CylindricalGearSetLoadCase(_874.GearSetLoadCaseBase):
    """CylindricalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetLoadCase")

    class _Cast_CylindricalGearSetLoadCase:
        """Special nested class for casting CylindricalGearSetLoadCase to subclasses."""

        def __init__(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
            parent: "CylindricalGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case_base(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ):
            return self._parent._cast(_874.GearSetLoadCaseBase)

        @property
        def gear_set_design_analysis(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ):
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_load_case(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
        ) -> "CylindricalGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetLoadCase._Cast_CylindricalGearSetLoadCase":
        return self._Cast_CylindricalGearSetLoadCase(self)

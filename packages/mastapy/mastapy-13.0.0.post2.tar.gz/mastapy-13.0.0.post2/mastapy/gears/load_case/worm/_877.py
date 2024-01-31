"""WormGearSetLoadCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.load_case import _874
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Worm", "WormGearSetLoadCase"
)


__docformat__ = "restructuredtext en"
__all__ = ("WormGearSetLoadCase",)


Self = TypeVar("Self", bound="WormGearSetLoadCase")


class WormGearSetLoadCase(_874.GearSetLoadCaseBase):
    """WormGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearSetLoadCase")

    class _Cast_WormGearSetLoadCase:
        """Special nested class for casting WormGearSetLoadCase to subclasses."""

        def __init__(
            self: "WormGearSetLoadCase._Cast_WormGearSetLoadCase",
            parent: "WormGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case_base(
            self: "WormGearSetLoadCase._Cast_WormGearSetLoadCase",
        ):
            return self._parent._cast(_874.GearSetLoadCaseBase)

        @property
        def gear_set_design_analysis(
            self: "WormGearSetLoadCase._Cast_WormGearSetLoadCase",
        ):
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "WormGearSetLoadCase._Cast_WormGearSetLoadCase",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def worm_gear_set_load_case(
            self: "WormGearSetLoadCase._Cast_WormGearSetLoadCase",
        ) -> "WormGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "WormGearSetLoadCase._Cast_WormGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "WormGearSetLoadCase._Cast_WormGearSetLoadCase":
        return self._Cast_WormGearSetLoadCase(self)

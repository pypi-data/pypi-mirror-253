"""BevelSetLoadCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.load_case.conical import _886
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Bevel", "BevelSetLoadCase"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelSetLoadCase",)


Self = TypeVar("Self", bound="BevelSetLoadCase")


class BevelSetLoadCase(_886.ConicalGearSetLoadCase):
    """BevelSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelSetLoadCase")

    class _Cast_BevelSetLoadCase:
        """Special nested class for casting BevelSetLoadCase to subclasses."""

        def __init__(
            self: "BevelSetLoadCase._Cast_BevelSetLoadCase", parent: "BevelSetLoadCase"
        ):
            self._parent = parent

        @property
        def conical_gear_set_load_case(self: "BevelSetLoadCase._Cast_BevelSetLoadCase"):
            return self._parent._cast(_886.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case_base(self: "BevelSetLoadCase._Cast_BevelSetLoadCase"):
            from mastapy.gears.load_case import _874

            return self._parent._cast(_874.GearSetLoadCaseBase)

        @property
        def gear_set_design_analysis(self: "BevelSetLoadCase._Cast_BevelSetLoadCase"):
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(self: "BevelSetLoadCase._Cast_BevelSetLoadCase"):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def bevel_set_load_case(
            self: "BevelSetLoadCase._Cast_BevelSetLoadCase",
        ) -> "BevelSetLoadCase":
            return self._parent

        def __getattr__(self: "BevelSetLoadCase._Cast_BevelSetLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelSetLoadCase._Cast_BevelSetLoadCase":
        return self._Cast_BevelSetLoadCase(self)

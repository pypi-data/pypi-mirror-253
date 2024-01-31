"""BevelLoadCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.load_case.conical import _885
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Bevel", "BevelLoadCase"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelLoadCase",)


Self = TypeVar("Self", bound="BevelLoadCase")


class BevelLoadCase(_885.ConicalGearLoadCase):
    """BevelLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelLoadCase")

    class _Cast_BevelLoadCase:
        """Special nested class for casting BevelLoadCase to subclasses."""

        def __init__(
            self: "BevelLoadCase._Cast_BevelLoadCase", parent: "BevelLoadCase"
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(self: "BevelLoadCase._Cast_BevelLoadCase"):
            return self._parent._cast(_885.ConicalGearLoadCase)

        @property
        def gear_load_case_base(self: "BevelLoadCase._Cast_BevelLoadCase"):
            from mastapy.gears.load_case import _873

            return self._parent._cast(_873.GearLoadCaseBase)

        @property
        def gear_design_analysis(self: "BevelLoadCase._Cast_BevelLoadCase"):
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(self: "BevelLoadCase._Cast_BevelLoadCase"):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def bevel_load_case(
            self: "BevelLoadCase._Cast_BevelLoadCase",
        ) -> "BevelLoadCase":
            return self._parent

        def __getattr__(self: "BevelLoadCase._Cast_BevelLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelLoadCase._Cast_BevelLoadCase":
        return self._Cast_BevelLoadCase(self)

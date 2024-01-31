"""ConceptGearLoadCase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.load_case import _873
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Concept", "ConceptGearLoadCase"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearLoadCase",)


Self = TypeVar("Self", bound="ConceptGearLoadCase")


class ConceptGearLoadCase(_873.GearLoadCaseBase):
    """ConceptGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearLoadCase")

    class _Cast_ConceptGearLoadCase:
        """Special nested class for casting ConceptGearLoadCase to subclasses."""

        def __init__(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
            parent: "ConceptGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_load_case_base(self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase"):
            return self._parent._cast(_873.GearLoadCaseBase)

        @property
        def gear_design_analysis(self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase"):
            from mastapy.gears.analysis import _1218

            return self._parent._cast(_1218.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def concept_gear_load_case(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase",
        ) -> "ConceptGearLoadCase":
            return self._parent

        def __getattr__(
            self: "ConceptGearLoadCase._Cast_ConceptGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConceptGearLoadCase._Cast_ConceptGearLoadCase":
        return self._Cast_ConceptGearLoadCase(self)

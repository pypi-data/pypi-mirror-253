"""FEPartModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5118
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "FEPartModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.static_loads import _6887


__docformat__ = "restructuredtext en"
__all__ = ("FEPartModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="FEPartModalAnalysisAtASpeed")


class FEPartModalAnalysisAtASpeed(_5118.AbstractShaftOrHousingModalAnalysisAtASpeed):
    """FEPartModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _FE_PART_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartModalAnalysisAtASpeed")

    class _Cast_FEPartModalAnalysisAtASpeed:
        """Special nested class for casting FEPartModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
            parent: "FEPartModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5118.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def fe_part_modal_analysis_at_a_speed(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
        ) -> "FEPartModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6887.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[FEPartModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.FEPartModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FEPartModalAnalysisAtASpeed._Cast_FEPartModalAnalysisAtASpeed":
        return self._Cast_FEPartModalAnalysisAtASpeed(self)

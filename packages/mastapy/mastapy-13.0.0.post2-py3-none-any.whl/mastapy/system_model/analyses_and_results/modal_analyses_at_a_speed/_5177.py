"""GuideDxfModelModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5141
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "GuideDxfModelModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.static_loads import _6896


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="GuideDxfModelModalAnalysisAtASpeed")


class GuideDxfModelModalAnalysisAtASpeed(_5141.ComponentModalAnalysisAtASpeed):
    """GuideDxfModelModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelModalAnalysisAtASpeed")

    class _Cast_GuideDxfModelModalAnalysisAtASpeed:
        """Special nested class for casting GuideDxfModelModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
            parent: "GuideDxfModelModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def component_modal_analysis_at_a_speed(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5141.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def guide_dxf_model_modal_analysis_at_a_speed(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
        ) -> "GuideDxfModelModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "GuideDxfModelModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6896.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GuideDxfModelModalAnalysisAtASpeed._Cast_GuideDxfModelModalAnalysisAtASpeed":
        return self._Cast_GuideDxfModelModalAnalysisAtASpeed(self)

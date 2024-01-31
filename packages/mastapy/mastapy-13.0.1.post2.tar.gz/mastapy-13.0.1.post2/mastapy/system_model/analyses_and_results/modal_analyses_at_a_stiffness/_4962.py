"""SpringDamperHalfModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4895,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SpringDamperHalfModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601
    from mastapy.system_model.analyses_and_results.static_loads import _6958


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SpringDamperHalfModalAnalysisAtAStiffness")


class SpringDamperHalfModalAnalysisAtAStiffness(
    _4895.CouplingHalfModalAnalysisAtAStiffness
):
    """SpringDamperHalfModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperHalfModalAnalysisAtAStiffness"
    )

    class _Cast_SpringDamperHalfModalAnalysisAtAStiffness:
        """Special nested class for casting SpringDamperHalfModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
            parent: "SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4895.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(_4936.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(_4882.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
        ) -> "SpringDamperHalfModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "SpringDamperHalfModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2601.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6958.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

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
    ) -> "SpringDamperHalfModalAnalysisAtAStiffness._Cast_SpringDamperHalfModalAnalysisAtAStiffness":
        return self._Cast_SpringDamperHalfModalAnalysisAtAStiffness(self)

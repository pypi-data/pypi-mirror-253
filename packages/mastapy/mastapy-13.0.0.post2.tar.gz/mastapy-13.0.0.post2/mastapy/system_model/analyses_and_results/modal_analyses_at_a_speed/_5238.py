"""UnbalancedMassModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5239
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "UnbalancedMassModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477
    from mastapy.system_model.analyses_and_results.static_loads import _6980


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="UnbalancedMassModalAnalysisAtASpeed")


class UnbalancedMassModalAnalysisAtASpeed(_5239.VirtualComponentModalAnalysisAtASpeed):
    """UnbalancedMassModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassModalAnalysisAtASpeed")

    class _Cast_UnbalancedMassModalAnalysisAtASpeed:
        """Special nested class for casting UnbalancedMassModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
            parent: "UnbalancedMassModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5239.VirtualComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
        ) -> "UnbalancedMassModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "UnbalancedMassModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6980.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

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
    ) -> (
        "UnbalancedMassModalAnalysisAtASpeed._Cast_UnbalancedMassModalAnalysisAtASpeed"
    ):
        return self._Cast_UnbalancedMassModalAnalysisAtASpeed(self)

"""WormGearModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5176
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "WormGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.static_loads import _6983


__docformat__ = "restructuredtext en"
__all__ = ("WormGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="WormGearModalAnalysisAtASpeed")


class WormGearModalAnalysisAtASpeed(_5176.GearModalAnalysisAtASpeed):
    """WormGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearModalAnalysisAtASpeed")

    class _Cast_WormGearModalAnalysisAtASpeed:
        """Special nested class for casting WormGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
            parent: "WormGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5176.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(_5195.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
        ) -> "WormGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6983.WormGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase

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
    ) -> "WormGearModalAnalysisAtASpeed._Cast_WormGearModalAnalysisAtASpeed":
        return self._Cast_WormGearModalAnalysisAtASpeed(self)

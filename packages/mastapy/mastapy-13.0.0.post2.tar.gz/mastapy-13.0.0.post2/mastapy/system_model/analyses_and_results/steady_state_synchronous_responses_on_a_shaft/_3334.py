"""RingPinsSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3322,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "RingPinsSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2570
    from mastapy.system_model.analyses_and_results.static_loads import _6943


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="RingPinsSteadyStateSynchronousResponseOnAShaft")


class RingPinsSteadyStateSynchronousResponseOnAShaft(
    _3322.MountableComponentSteadyStateSynchronousResponseOnAShaft
):
    """RingPinsSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _RING_PINS_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_RingPinsSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting RingPinsSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
            parent: "RingPinsSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3322.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_steady_state_synchronous_response_on_a_shaft(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
        ) -> "RingPinsSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft",
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
        self: Self,
        instance_to_wrap: "RingPinsSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2570.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6943.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

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
    ) -> "RingPinsSteadyStateSynchronousResponseOnAShaft._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_RingPinsSteadyStateSynchronousResponseOnAShaft(self)

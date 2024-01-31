"""FaceGearSteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3564,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "FaceGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.static_loads import _6884


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="FaceGearSteadyStateSynchronousResponseAtASpeed")


class FaceGearSteadyStateSynchronousResponseAtASpeed(
    _3564.GearSteadyStateSynchronousResponseAtASpeed
):
    """FaceGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_FaceGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting FaceGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
            parent: "FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(_3564.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(
                _3581.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(_3583.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "FaceGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "FaceGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2528.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6884.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

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
    ) -> "FaceGearSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_FaceGearSteadyStateSynchronousResponseAtASpeed(self)

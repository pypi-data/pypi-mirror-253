"""TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3283,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6975


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft"
)


class TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft(
    _3283.CouplingHalfSteadyStateSynchronousResponseOnAShaft
):
    """TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
            parent: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3283.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
        ) -> "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6975.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

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
    ) -> "TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft(
            self
        )

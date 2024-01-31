"""FEPartSteadyStateSynchronousResponseOnAShaft"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3246,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "FEPartSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.static_loads import _6887


__docformat__ = "restructuredtext en"
__all__ = ("FEPartSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="FEPartSteadyStateSynchronousResponseOnAShaft")


class FEPartSteadyStateSynchronousResponseOnAShaft(
    _3246.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
):
    """FEPartSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _FE_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FEPartSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_FEPartSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting FEPartSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
            parent: "FEPartSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
        ):
            return self._parent._cast(
                _3246.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
        ) -> "FEPartSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "FEPartSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
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
    def planetaries(self: Self) -> "List[FEPartSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.FEPartSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "FEPartSteadyStateSynchronousResponseOnAShaft._Cast_FEPartSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_FEPartSteadyStateSynchronousResponseOnAShaft(self)

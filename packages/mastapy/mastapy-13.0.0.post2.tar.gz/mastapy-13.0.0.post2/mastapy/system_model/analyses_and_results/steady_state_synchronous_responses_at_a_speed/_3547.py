"""CycloidalAssemblySteadyStateSynchronousResponseAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3602,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2568
    from mastapy.system_model.analyses_and_results.static_loads import _6857


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="CycloidalAssemblySteadyStateSynchronousResponseAtASpeed")


class CycloidalAssemblySteadyStateSynchronousResponseAtASpeed(
    _3602.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
):
    """CycloidalAssemblySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting CycloidalAssemblySteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
            parent: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            return self._parent._cast(
                _3602.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3504,
            )

            return self._parent._cast(
                _3504.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(_3583.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
        ) -> "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2568.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6857.CycloidalAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalAssemblySteadyStateSynchronousResponseAtASpeed._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed":
        return self._Cast_CycloidalAssemblySteadyStateSynchronousResponseAtASpeed(self)

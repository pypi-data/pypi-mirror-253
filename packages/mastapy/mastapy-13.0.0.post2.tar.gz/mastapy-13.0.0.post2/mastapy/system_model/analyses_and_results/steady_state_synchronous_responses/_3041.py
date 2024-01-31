"""FlexiblePinAssemblySteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3082,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "FlexiblePinAssemblySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.static_loads import _6888


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblySteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="FlexiblePinAssemblySteadyStateSynchronousResponse")


class FlexiblePinAssemblySteadyStateSynchronousResponse(
    _3082.SpecialisedAssemblySteadyStateSynchronousResponse
):
    """FlexiblePinAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblySteadyStateSynchronousResponse"
    )

    class _Cast_FlexiblePinAssemblySteadyStateSynchronousResponse:
        """Special nested class for casting FlexiblePinAssemblySteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
            parent: "FlexiblePinAssemblySteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3082.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2983,
            )

            return self._parent._cast(
                _2983.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
        ) -> "FlexiblePinAssemblySteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse",
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
        instance_to_wrap: "FlexiblePinAssemblySteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2454.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6888.FlexiblePinAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase

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
    ) -> "FlexiblePinAssemblySteadyStateSynchronousResponse._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse":
        return self._Cast_FlexiblePinAssemblySteadyStateSynchronousResponse(self)

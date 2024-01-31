"""PowerLoadSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3109,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "PowerLoadSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6939


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PowerLoadSteadyStateSynchronousResponse")


class PowerLoadSteadyStateSynchronousResponse(
    _3109.VirtualComponentSteadyStateSynchronousResponse
):
    """PowerLoadSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadSteadyStateSynchronousResponse"
    )

    class _Cast_PowerLoadSteadyStateSynchronousResponse:
        """Special nested class for casting PowerLoadSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
            parent: "PowerLoadSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3109.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(
                _3061.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3008,
            )

            return self._parent._cast(_3008.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def power_load_steady_state_synchronous_response(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
        ) -> "PowerLoadSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "PowerLoadSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

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
    ) -> "PowerLoadSteadyStateSynchronousResponse._Cast_PowerLoadSteadyStateSynchronousResponse":
        return self._Cast_PowerLoadSteadyStateSynchronousResponse(self)

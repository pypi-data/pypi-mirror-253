"""OilSealCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3152,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "OilSealCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3062,
    )


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="OilSealCompoundSteadyStateSynchronousResponse")


class OilSealCompoundSteadyStateSynchronousResponse(
    _3152.ConnectorCompoundSteadyStateSynchronousResponse
):
    """OilSealCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OilSealCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_OilSealCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting OilSealCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
            parent: "OilSealCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connector_compound_steady_state_synchronous_response(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3152.ConnectorCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_compound_steady_state_synchronous_response(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
        ) -> "OilSealCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "OilSealCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3062.OilSealSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.OilSealSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3062.OilSealSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.OilSealSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "OilSealCompoundSteadyStateSynchronousResponse._Cast_OilSealCompoundSteadyStateSynchronousResponse":
        return self._Cast_OilSealCompoundSteadyStateSynchronousResponse(self)

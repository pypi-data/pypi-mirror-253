"""CVTCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3126,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "CVTCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3025,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CVTCompoundSteadyStateSynchronousResponse")


class CVTCompoundSteadyStateSynchronousResponse(
    _3126.BeltDriveCompoundSteadyStateSynchronousResponse
):
    """CVTCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_CVTCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting CVTCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
            parent: "CVTCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3126.BeltDriveCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3116,
            )

            return self._parent._cast(
                _3116.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
        ) -> "CVTCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CVTCompoundSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3025.CVTSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CVTSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3025.CVTSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.CVTSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CVTCompoundSteadyStateSynchronousResponse._Cast_CVTCompoundSteadyStateSynchronousResponse":
        return self._Cast_CVTCompoundSteadyStateSynchronousResponse(self)

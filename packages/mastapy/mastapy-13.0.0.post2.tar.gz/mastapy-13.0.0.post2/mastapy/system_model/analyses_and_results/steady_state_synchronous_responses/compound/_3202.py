"""PointLoadCompoundSteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3238,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PointLoadCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3070,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="PointLoadCompoundSteadyStateSynchronousResponse")


class PointLoadCompoundSteadyStateSynchronousResponse(
    _3238.VirtualComponentCompoundSteadyStateSynchronousResponse
):
    """PointLoadCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PointLoadCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_PointLoadCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PointLoadCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
            parent: "PointLoadCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
        ):
            return self._parent._cast(
                _3238.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def point_load_compound_steady_state_synchronous_response(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
        ) -> "PointLoadCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PointLoadCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PointLoad":
        """mastapy.system_model.part_model.PointLoad

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
    ) -> "List[_3070.PointLoadSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PointLoadSteadyStateSynchronousResponse]

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
    ) -> "List[_3070.PointLoadSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PointLoadSteadyStateSynchronousResponse]

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
    ) -> "PointLoadCompoundSteadyStateSynchronousResponse._Cast_PointLoadCompoundSteadyStateSynchronousResponse":
        return self._Cast_PointLoadCompoundSteadyStateSynchronousResponse(self)

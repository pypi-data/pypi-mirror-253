"""SteadyStateSynchronousResponse"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7536
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3091,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SteadyStateSynchronousResponse")


class SteadyStateSynchronousResponse(_7536.CompoundAnalysisCase):
    """SteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SteadyStateSynchronousResponse")

    class _Cast_SteadyStateSynchronousResponse:
        """Special nested class for casting SteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse",
            parent: "SteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def compound_analysis_case(
            self: "SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse",
        ):
            return self._parent._cast(_7536.CompoundAnalysisCase)

        @property
        def static_load_analysis_case(
            self: "SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.AnalysisCase)

        @property
        def context(
            self: "SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def steady_state_synchronous_response(
            self: "SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse",
        ) -> "SteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SteadyStateSynchronousResponse.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def steady_state_analysis_options(
        self: Self,
    ) -> "_3091.SteadyStateSynchronousResponseOptions":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.SteadyStateSynchronousResponseOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SteadyStateAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SteadyStateSynchronousResponse._Cast_SteadyStateSynchronousResponse":
        return self._Cast_SteadyStateSynchronousResponse(self)

"""SteadyStateSynchronousResponseAtASpeedAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results import _2620
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "SteadyStateSynchronousResponseAtASpeedAnalysis",
)


__docformat__ = "restructuredtext en"
__all__ = ("SteadyStateSynchronousResponseAtASpeedAnalysis",)


Self = TypeVar("Self", bound="SteadyStateSynchronousResponseAtASpeedAnalysis")


class SteadyStateSynchronousResponseAtASpeedAnalysis(_2620.SingleAnalysis):
    """SteadyStateSynchronousResponseAtASpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SteadyStateSynchronousResponseAtASpeedAnalysis"
    )

    class _Cast_SteadyStateSynchronousResponseAtASpeedAnalysis:
        """Special nested class for casting SteadyStateSynchronousResponseAtASpeedAnalysis to subclasses."""

        def __init__(
            self: "SteadyStateSynchronousResponseAtASpeedAnalysis._Cast_SteadyStateSynchronousResponseAtASpeedAnalysis",
            parent: "SteadyStateSynchronousResponseAtASpeedAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "SteadyStateSynchronousResponseAtASpeedAnalysis._Cast_SteadyStateSynchronousResponseAtASpeedAnalysis",
        ):
            return self._parent._cast(_2620.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "SteadyStateSynchronousResponseAtASpeedAnalysis._Cast_SteadyStateSynchronousResponseAtASpeedAnalysis",
        ):
            from mastapy import _7552

            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def steady_state_synchronous_response_at_a_speed_analysis(
            self: "SteadyStateSynchronousResponseAtASpeedAnalysis._Cast_SteadyStateSynchronousResponseAtASpeedAnalysis",
        ) -> "SteadyStateSynchronousResponseAtASpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SteadyStateSynchronousResponseAtASpeedAnalysis._Cast_SteadyStateSynchronousResponseAtASpeedAnalysis",
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
        instance_to_wrap: "SteadyStateSynchronousResponseAtASpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "SteadyStateSynchronousResponseAtASpeedAnalysis._Cast_SteadyStateSynchronousResponseAtASpeedAnalysis":
        return self._Cast_SteadyStateSynchronousResponseAtASpeedAnalysis(self)

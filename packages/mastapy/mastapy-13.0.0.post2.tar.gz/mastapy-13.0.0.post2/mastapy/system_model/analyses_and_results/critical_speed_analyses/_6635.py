"""RingPinsToDiscConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6610
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "RingPinsToDiscConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.static_loads import _6944


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionCriticalSpeedAnalysis")


class RingPinsToDiscConnectionCriticalSpeedAnalysis(
    _6610.InterMountableComponentConnectionCriticalSpeedAnalysis
):
    """RingPinsToDiscConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis"
    )

    class _Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis:
        """Special nested class for casting RingPinsToDiscConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
            parent: "RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6610.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_critical_speed_analysis(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
        ) -> "RingPinsToDiscConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis",
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
        instance_to_wrap: "RingPinsToDiscConnectionCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6944.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionCriticalSpeedAnalysis._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis":
        return self._Cast_RingPinsToDiscConnectionCriticalSpeedAnalysis(self)

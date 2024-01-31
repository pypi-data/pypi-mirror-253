"""CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2335


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis"
)


class CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis(
    _6566.CoaxialConnectionCriticalSpeedAnalysis
):
    """CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6566.CoaxialConnectionCriticalSpeedAnalysis)

        @property
        def shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6642,
            )

            return self._parent._cast(
                _6642.ShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6545,
            )

            return self._parent._cast(
                _6545.AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2335.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis(
            self
        )

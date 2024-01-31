"""ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6678,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6643


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
)


class ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis(
    _6678.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6678.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(
                _6699.CoaxialConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6719,
            )

            return self._parent._cast(
                _6719.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6758,
            )

            return self._parent._cast(
                _6758.PlanetaryConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6643.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6643.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ShaftToMountableComponentConnectionCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis":
        return (
            self._Cast_ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis(
                self
            )
        )

"""CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6699,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6590


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis"
)


class CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis(
    _6699.CoaxialConnectionCompoundCriticalSpeedAnalysis
):
    """CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6699.CoaxialConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(
                _6772.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6678,
            )

            return self._parent._cast(
                _6678.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6590.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6590.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis(
            self
        )

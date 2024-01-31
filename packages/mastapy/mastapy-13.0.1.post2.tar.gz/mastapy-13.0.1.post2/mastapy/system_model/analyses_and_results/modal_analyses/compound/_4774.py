"""CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4731
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
        "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2338
    from mastapy.system_model.analyses_and_results.modal_analyses import _4619


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis"
)


class CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis(
    _4731.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
):
    """CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
            parent: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
        ):
            return self._parent._cast(
                _4731.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
        ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2338.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2338.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4619.CycloidalDiscPlanetaryBearingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscPlanetaryBearingConnectionModalAnalysis]

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
    ) -> "List[_4619.CycloidalDiscPlanetaryBearingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscPlanetaryBearingConnectionModalAnalysis]

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis(
            self
        )

"""CycloidalDiscCentralBearingConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4617


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundModalAnalysis"
)


class CycloidalDiscCentralBearingConnectionCompoundModalAnalysis(
    _4752.CoaxialConnectionCompoundModalAnalysis
):
    """CycloidalDiscCentralBearingConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
        ):
            return self._parent._cast(_4752.CoaxialConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(
                _4825.ShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4731,
            )

            return self._parent._cast(
                _4731.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4617.CycloidalDiscCentralBearingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscCentralBearingConnectionModalAnalysis]

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
    ) -> "List[_4617.CycloidalDiscCentralBearingConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CycloidalDiscCentralBearingConnectionModalAnalysis]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysis(
            self
        )

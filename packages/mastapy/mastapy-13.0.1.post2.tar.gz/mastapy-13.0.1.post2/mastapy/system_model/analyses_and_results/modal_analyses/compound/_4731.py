"""AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4575


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"
)


class AbstractShaftToMountableComponentConnectionCompoundModalAnalysis(
    _4763.ConnectionCompoundModalAnalysis
):
    """AbstractShaftToMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            return self._parent._cast(_4763.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.CoaxialConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(
                _4772.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(
                _4774.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
            )

        @property
        def planetary_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(
                _4825.ShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4575.AbstractShaftToMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftToMountableComponentConnectionModalAnalysis]

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
    ) -> "List[_4575.AbstractShaftToMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AbstractShaftToMountableComponentConnectionModalAnalysis]

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
    ) -> "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis":
        return (
            self._Cast_AbstractShaftToMountableComponentConnectionCompoundModalAnalysis(
                self
            )
        )

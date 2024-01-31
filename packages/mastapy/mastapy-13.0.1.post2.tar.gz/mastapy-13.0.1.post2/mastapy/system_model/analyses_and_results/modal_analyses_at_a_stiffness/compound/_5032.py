"""CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5012,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4901,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
)


class CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness(
    _5012.CoaxialConnectionCompoundModalAnalysisAtAStiffness
):
    """CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
            parent: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5012.CoaxialConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4991,
            )

            return self._parent._cast(
                _4991.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(_5023.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4901.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4901.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CycloidalDiscCentralBearingConnectionModalAnalysisAtAStiffness]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness(
            self
        )

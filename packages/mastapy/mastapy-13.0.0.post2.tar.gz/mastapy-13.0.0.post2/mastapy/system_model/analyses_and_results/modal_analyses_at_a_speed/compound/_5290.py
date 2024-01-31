"""CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5270,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5160,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed"
)


class CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed(
    _5270.CoaxialConnectionCompoundModalAnalysisAtASpeed
):
    """CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
            parent: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5270.CoaxialConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5343,
            )

            return self._parent._cast(
                _5343.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(_5281.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5160.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5160.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed(
            self
        )

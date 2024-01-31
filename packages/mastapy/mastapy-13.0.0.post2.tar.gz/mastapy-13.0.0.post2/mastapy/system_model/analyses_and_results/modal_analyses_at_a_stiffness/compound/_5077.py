"""RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5052,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2341
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4948,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness"
)


class RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness(
    _5052.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
):
    """RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
            parent: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5052.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(_5022.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_stiffness(
            self: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2341.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4948.RingPinsToDiscConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.RingPinsToDiscConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4948.RingPinsToDiscConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.RingPinsToDiscConnectionModalAnalysisAtAStiffness]

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
    ) -> "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness(
            self
        )

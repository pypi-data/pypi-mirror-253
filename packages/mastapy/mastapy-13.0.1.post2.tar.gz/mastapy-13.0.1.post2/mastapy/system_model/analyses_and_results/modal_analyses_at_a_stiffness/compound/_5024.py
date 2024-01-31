"""ConnectorCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5065,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ConnectorCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4893,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConnectorCompoundModalAnalysisAtAStiffness")


class ConnectorCompoundModalAnalysisAtAStiffness(
    _5065.MountableComponentCompoundModalAnalysisAtAStiffness
):
    """ConnectorCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_ConnectorCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ConnectorCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
            parent: "ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5065.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(_4996.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(
                _5084.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
        ) -> "ConnectorCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConnectorCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4893.ConnectorModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConnectorModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4893.ConnectorModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConnectorModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundModalAnalysisAtAStiffness._Cast_ConnectorCompoundModalAnalysisAtAStiffness":
        return self._Cast_ConnectorCompoundModalAnalysisAtAStiffness(self)

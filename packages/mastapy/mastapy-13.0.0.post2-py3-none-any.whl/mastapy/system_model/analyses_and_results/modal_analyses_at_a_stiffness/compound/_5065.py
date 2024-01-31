"""OilSealCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5023,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "OilSealCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4936,
    )


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="OilSealCompoundModalAnalysisAtAStiffness")


class OilSealCompoundModalAnalysisAtAStiffness(
    _5023.ConnectorCompoundModalAnalysisAtAStiffness
):
    """OilSealCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OilSealCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_OilSealCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting OilSealCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
            parent: "OilSealCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_5023.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(_5012.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
        ) -> "OilSealCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "OilSealCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4936.OilSealModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.OilSealModalAnalysisAtAStiffness]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4936.OilSealModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.OilSealModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "OilSealCompoundModalAnalysisAtAStiffness._Cast_OilSealCompoundModalAnalysisAtAStiffness":
        return self._Cast_OilSealCompoundModalAnalysisAtAStiffness(self)

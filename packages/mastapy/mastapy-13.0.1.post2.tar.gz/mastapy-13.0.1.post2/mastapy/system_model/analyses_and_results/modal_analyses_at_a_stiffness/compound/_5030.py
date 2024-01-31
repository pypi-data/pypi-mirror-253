"""CVTPulleyCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5076,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "CVTPulleyCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4899,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTPulleyCompoundModalAnalysisAtAStiffness")


class CVTPulleyCompoundModalAnalysisAtAStiffness(
    _5076.PulleyCompoundModalAnalysisAtAStiffness
):
    """CVTPulleyCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTPulleyCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_CVTPulleyCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting CVTPulleyCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
            parent: "CVTPulleyCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_5076.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(
                _5027.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(
                _5065.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
        ) -> "CVTPulleyCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4899.CVTPulleyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CVTPulleyModalAnalysisAtAStiffness]

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
    ) -> "List[_4899.CVTPulleyModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.CVTPulleyModalAnalysisAtAStiffness]

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
    ) -> "CVTPulleyCompoundModalAnalysisAtAStiffness._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness":
        return self._Cast_CVTPulleyCompoundModalAnalysisAtAStiffness(self)

"""ClutchCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5025,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ClutchCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4880,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ClutchCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ClutchCompoundModalAnalysisAtAStiffness")


class ClutchCompoundModalAnalysisAtAStiffness(
    _5025.CouplingCompoundModalAnalysisAtAStiffness
):
    """ClutchCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ClutchCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_ClutchCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ClutchCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
            parent: "ClutchCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_5025.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4988,
            )

            return self._parent._cast(
                _4988.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
        ) -> "ClutchCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ClutchCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2578.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2578.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4880.ClutchModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ClutchModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4880.ClutchModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ClutchModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchCompoundModalAnalysisAtAStiffness._Cast_ClutchCompoundModalAnalysisAtAStiffness":
        return self._Cast_ClutchCompoundModalAnalysisAtAStiffness(self)

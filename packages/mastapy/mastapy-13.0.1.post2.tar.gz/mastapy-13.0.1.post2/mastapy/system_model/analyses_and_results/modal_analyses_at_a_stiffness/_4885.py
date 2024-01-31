"""ConceptCouplingModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4896,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConceptCouplingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.static_loads import _6841


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ConceptCouplingModalAnalysisAtAStiffness")


class ConceptCouplingModalAnalysisAtAStiffness(_4896.CouplingModalAnalysisAtAStiffness):
    """ConceptCouplingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingModalAnalysisAtAStiffness"
    )

    class _Cast_ConceptCouplingModalAnalysisAtAStiffness:
        """Special nested class for casting ConceptCouplingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
            parent: "ConceptCouplingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4896.CouplingModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(
                _4957.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(_4857.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
        ) -> "ConceptCouplingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ConceptCouplingModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2581.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6841.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingModalAnalysisAtAStiffness._Cast_ConceptCouplingModalAnalysisAtAStiffness":
        return self._Cast_ConceptCouplingModalAnalysisAtAStiffness(self)

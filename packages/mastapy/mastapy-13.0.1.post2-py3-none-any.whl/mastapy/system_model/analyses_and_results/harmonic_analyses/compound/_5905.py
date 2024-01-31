"""ConceptCouplingCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5916
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConceptCouplingCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2581
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5708


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundHarmonicAnalysis")


class ConceptCouplingCompoundHarmonicAnalysis(_5916.CouplingCompoundHarmonicAnalysis):
    """ConceptCouplingCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingCompoundHarmonicAnalysis"
    )

    class _Cast_ConceptCouplingCompoundHarmonicAnalysis:
        """Special nested class for casting ConceptCouplingCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
            parent: "ConceptCouplingCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_harmonic_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5916.CouplingCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5879,
            )

            return self._parent._cast(_5879.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
        ) -> "ConceptCouplingCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2581.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5708.ConceptCouplingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHarmonicAnalysis]

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
    ) -> "List[_5708.ConceptCouplingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHarmonicAnalysis]

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
    ) -> "ConceptCouplingCompoundHarmonicAnalysis._Cast_ConceptCouplingCompoundHarmonicAnalysis":
        return self._Cast_ConceptCouplingCompoundHarmonicAnalysis(self)

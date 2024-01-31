"""FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6236,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6064,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation"
)


class FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
    _6236.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
):
    """FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6236.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6138,
            )

            return self._parent._cast(
                _6138.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2454.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

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
    ) -> "List[_6064.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6064.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )

"""AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5913
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5685


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundHarmonicAnalysis")


class AGMAGleasonConicalGearSetCompoundHarmonicAnalysis(
    _5913.ConicalGearSetCompoundHarmonicAnalysis
):
    """AGMAGleasonConicalGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5913.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5879,
            )

            return self._parent._cast(_5879.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5892,
            )

            return self._parent._cast(
                _5892.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5897,
            )

            return self._parent._cast(_5897.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5943,
            )

            return self._parent._cast(_5943.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(_5980.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(
                _5986.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(
                _5989.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6007,
            )

            return self._parent._cast(_6007.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5685.AGMAGleasonConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearSetHarmonicAnalysis]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5685.AGMAGleasonConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearSetHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis(self)

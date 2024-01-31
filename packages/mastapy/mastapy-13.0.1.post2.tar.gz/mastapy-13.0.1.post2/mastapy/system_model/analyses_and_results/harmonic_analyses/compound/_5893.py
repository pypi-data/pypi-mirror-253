"""BevelDifferentialPlanetGearCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5890
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5693


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundHarmonicAnalysis")


class BevelDifferentialPlanetGearCompoundHarmonicAnalysis(
    _5890.BevelDifferentialGearCompoundHarmonicAnalysis
):
    """BevelDifferentialPlanetGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
            parent: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(
                _5890.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(_5895.BevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5883,
            )

            return self._parent._cast(
                _5883.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
        ) -> "BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5693.BevelDifferentialPlanetGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialPlanetGearHarmonicAnalysis]

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
    ) -> "List[_5693.BevelDifferentialPlanetGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialPlanetGearHarmonicAnalysis]

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
    ) -> "BevelDifferentialPlanetGearCompoundHarmonicAnalysis._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCompoundHarmonicAnalysis(self)

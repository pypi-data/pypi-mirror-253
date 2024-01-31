"""AGMAGleasonConicalGearCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5683


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundHarmonicAnalysis")


class AGMAGleasonConicalGearCompoundHarmonicAnalysis(
    _5911.ConicalGearCompoundHarmonicAnalysis
):
    """AGMAGleasonConicalGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
            parent: "AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5911.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5890,
            )

            return self._parent._cast(
                _5890.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5893,
            )

            return self._parent._cast(
                _5893.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(
                _5894.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(_5895.BevelGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(_5941.HypoidGearCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5978,
            )

            return self._parent._cast(_5978.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(
                _5984.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(_5987.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(
                _5990.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(
                _5991.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6005,
            )

            return self._parent._cast(_6005.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
        ) -> "AGMAGleasonConicalGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5683.AGMAGleasonConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearHarmonicAnalysis]

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
    ) -> "List[_5683.AGMAGleasonConicalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearHarmonicAnalysis]

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
    ) -> "AGMAGleasonConicalGearCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis":
        return self._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysis(self)

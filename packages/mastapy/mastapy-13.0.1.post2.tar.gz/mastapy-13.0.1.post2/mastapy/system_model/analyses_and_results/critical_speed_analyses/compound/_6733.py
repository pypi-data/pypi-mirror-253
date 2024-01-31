"""GearCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6752,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "GearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6604


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearCompoundCriticalSpeedAnalysis")


class GearCompoundCriticalSpeedAnalysis(
    _6752.MountableComponentCompoundCriticalSpeedAnalysis
):
    """GearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundCriticalSpeedAnalysis")

    class _Cast_GearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
            parent: "GearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6752.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(_6700.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6679,
            )

            return self._parent._cast(
                _6679.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6686,
            )

            return self._parent._cast(
                _6686.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(
                _6689.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(
                _6690.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6691,
            )

            return self._parent._cast(_6691.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6704,
            )

            return self._parent._cast(_6704.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(_6707.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(
                _6722.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6725,
            )

            return self._parent._cast(
                _6725.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(_6737.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(
                _6741.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(
                _6744.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6747,
            )

            return self._parent._cast(
                _6747.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6774,
            )

            return self._parent._cast(
                _6774.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6783,
            )

            return self._parent._cast(
                _6783.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(_6798.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6801,
            )

            return self._parent._cast(_6801.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "GearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "GearCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6604.GearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearCriticalSpeedAnalysis]

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
    ) -> "List[_6604.GearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearCriticalSpeedAnalysis]

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
    ) -> "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis":
        return self._Cast_GearCompoundCriticalSpeedAnalysis(self)

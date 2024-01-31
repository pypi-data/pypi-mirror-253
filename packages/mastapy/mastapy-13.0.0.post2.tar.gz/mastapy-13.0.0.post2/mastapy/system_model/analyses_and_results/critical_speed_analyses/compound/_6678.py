"""AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6706,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6546


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis")


class AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis(
    _6706.ConicalGearCompoundCriticalSpeedAnalysis
):
    """AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
            parent: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6706.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(_6732.GearCompoundCriticalSpeedAnalysis)

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(_6699.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6685,
            )

            return self._parent._cast(
                _6685.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6688,
            )

            return self._parent._cast(
                _6688.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(
                _6689.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(_6690.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(
                _6779.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(
                _6785.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(_6800.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
        ) -> "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6546.AGMAGleasonConicalGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearCriticalSpeedAnalysis]

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
    ) -> "List[_6546.AGMAGleasonConicalGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearCriticalSpeedAnalysis]

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
    ) -> "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
        return self._Cast_AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis(self)

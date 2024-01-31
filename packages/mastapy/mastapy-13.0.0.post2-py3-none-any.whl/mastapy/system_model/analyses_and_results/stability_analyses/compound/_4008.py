"""StraightBevelPlanetGearCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "StraightBevelPlanetGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3879


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundStabilityAnalysis")


class StraightBevelPlanetGearCompoundStabilityAnalysis(
    _4002.StraightBevelDiffGearCompoundStabilityAnalysis
):
    """StraightBevelPlanetGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundStabilityAnalysis"
    )

    class _Cast_StraightBevelPlanetGearCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelPlanetGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
            parent: "StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            return self._parent._cast(
                _4002.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3913,
            )

            return self._parent._cast(_3913.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3901,
            )

            return self._parent._cast(
                _3901.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(_3922.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
        ) -> "StraightBevelPlanetGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3879.StraightBevelPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelPlanetGearStabilityAnalysis]

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
    ) -> "List[_3879.StraightBevelPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelPlanetGearStabilityAnalysis]

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
    ) -> "StraightBevelPlanetGearCompoundStabilityAnalysis._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis":
        return self._Cast_StraightBevelPlanetGearCompoundStabilityAnalysis(self)

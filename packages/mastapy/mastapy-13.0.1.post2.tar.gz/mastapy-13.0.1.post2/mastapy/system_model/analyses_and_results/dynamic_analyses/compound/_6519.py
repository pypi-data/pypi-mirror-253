"""StraightBevelPlanetGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "StraightBevelPlanetGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundDynamicAnalysis")


class StraightBevelPlanetGearCompoundDynamicAnalysis(
    _6513.StraightBevelDiffGearCompoundDynamicAnalysis
):
    """StraightBevelPlanetGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundDynamicAnalysis"
    )

    class _Cast_StraightBevelPlanetGearCompoundDynamicAnalysis:
        """Special nested class for casting StraightBevelPlanetGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
            parent: "StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            return self._parent._cast(
                _6513.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(_6424.BevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(
                _6412.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
        ) -> "StraightBevelPlanetGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6390.StraightBevelPlanetGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelPlanetGearDynamicAnalysis]

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
    ) -> "List[_6390.StraightBevelPlanetGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelPlanetGearDynamicAnalysis]

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
    ) -> "StraightBevelPlanetGearCompoundDynamicAnalysis._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis":
        return self._Cast_StraightBevelPlanetGearCompoundDynamicAnalysis(self)

"""AGMAGleasonConicalGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6440
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundDynamicAnalysis")


class AGMAGleasonConicalGearCompoundDynamicAnalysis(
    _6440.ConicalGearCompoundDynamicAnalysis
):
    """AGMAGleasonConicalGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
            parent: "AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6440.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6419,
            )

            return self._parent._cast(
                _6419.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6422,
            )

            return self._parent._cast(
                _6422.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(
                _6423.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(_6424.BevelGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(_6470.HypoidGearCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(_6507.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(
                _6513.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6516,
            )

            return self._parent._cast(_6516.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6519,
            )

            return self._parent._cast(
                _6519.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6534,
            )

            return self._parent._cast(_6534.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
        ) -> "AGMAGleasonConicalGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6281.AGMAGleasonConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearDynamicAnalysis]

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
    ) -> "List[_6281.AGMAGleasonConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearDynamicAnalysis]

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
    ) -> "AGMAGleasonConicalGearCompoundDynamicAnalysis._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis":
        return self._Cast_AGMAGleasonConicalGearCompoundDynamicAnalysis(self)

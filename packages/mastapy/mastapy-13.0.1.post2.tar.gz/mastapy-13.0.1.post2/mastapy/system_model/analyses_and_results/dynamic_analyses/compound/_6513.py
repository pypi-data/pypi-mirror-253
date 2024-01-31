"""StraightBevelDiffGearCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6424
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "StraightBevelDiffGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundDynamicAnalysis")


class StraightBevelDiffGearCompoundDynamicAnalysis(
    _6424.BevelGearCompoundDynamicAnalysis
):
    """StraightBevelDiffGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearCompoundDynamicAnalysis"
    )

    class _Cast_StraightBevelDiffGearCompoundDynamicAnalysis:
        """Special nested class for casting StraightBevelDiffGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
            parent: "StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6424.BevelGearCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(
                _6412.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConicalGearCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6519,
            )

            return self._parent._cast(
                _6519.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
        ) -> "StraightBevelDiffGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6384.StraightBevelDiffGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearDynamicAnalysis]

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
    ) -> "List[_6384.StraightBevelDiffGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearDynamicAnalysis]

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
    ) -> "StraightBevelDiffGearCompoundDynamicAnalysis._Cast_StraightBevelDiffGearCompoundDynamicAnalysis":
        return self._Cast_StraightBevelDiffGearCompoundDynamicAnalysis(self)

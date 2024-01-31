"""BevelGearCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6547
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearCriticalSpeedAnalysis")


class BevelGearCriticalSpeedAnalysis(_6547.AGMAGleasonConicalGearCriticalSpeedAnalysis):
    """BevelGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearCriticalSpeedAnalysis")

    class _Cast_BevelGearCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
            parent: "BevelGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6547.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(_6554.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(
                _6557.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6558,
            )

            return self._parent._cast(
                _6558.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(_6645.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(
                _6657.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6672,
            )

            return self._parent._cast(_6672.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "BevelGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2519.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis":
        return self._Cast_BevelGearCriticalSpeedAnalysis(self)

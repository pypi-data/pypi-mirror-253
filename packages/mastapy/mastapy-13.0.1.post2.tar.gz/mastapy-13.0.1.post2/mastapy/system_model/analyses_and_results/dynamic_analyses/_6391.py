"""StraightBevelSunGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "StraightBevelSunGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearDynamicAnalysis")


class StraightBevelSunGearDynamicAnalysis(_6384.StraightBevelDiffGearDynamicAnalysis):
    """StraightBevelSunGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGearDynamicAnalysis")

    class _Cast_StraightBevelSunGearDynamicAnalysis:
        """Special nested class for casting StraightBevelSunGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
            parent: "StraightBevelSunGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            return self._parent._cast(_6384.StraightBevelDiffGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281

            return self._parent._cast(_6281.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
        ) -> "StraightBevelSunGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

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
    ) -> (
        "StraightBevelSunGearDynamicAnalysis._Cast_StraightBevelSunGearDynamicAnalysis"
    ):
        return self._Cast_StraightBevelSunGearDynamicAnalysis(self)

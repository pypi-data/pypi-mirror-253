"""AGMAGleasonConicalGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AGMAGleasonConicalGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearDynamicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearDynamicAnalysis")


class AGMAGleasonConicalGearDynamicAnalysis(_6309.ConicalGearDynamicAnalysis):
    """AGMAGleasonConicalGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearDynamicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearDynamicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
            parent: "AGMAGleasonConicalGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            return self._parent._cast(_6309.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BevelGearDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(_6341.HypoidGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.SpiralBevelGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.StraightBevelSunGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.ZerolBevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
        ) -> "AGMAGleasonConicalGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2513.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearDynamicAnalysis._Cast_AGMAGleasonConicalGearDynamicAnalysis":
        return self._Cast_AGMAGleasonConicalGearDynamicAnalysis(self)

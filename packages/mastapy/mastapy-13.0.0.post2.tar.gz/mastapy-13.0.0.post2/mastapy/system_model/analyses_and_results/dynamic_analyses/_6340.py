"""HypoidGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "HypoidGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.static_loads import _6905


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearDynamicAnalysis",)


Self = TypeVar("Self", bound="HypoidGearDynamicAnalysis")


class HypoidGearDynamicAnalysis(_6280.AGMAGleasonConicalGearDynamicAnalysis):
    """HypoidGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearDynamicAnalysis")

    class _Cast_HypoidGearDynamicAnalysis:
        """Special nested class for casting HypoidGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
            parent: "HypoidGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            return self._parent._cast(_6280.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis",
        ) -> "HypoidGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6905.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearDynamicAnalysis._Cast_HypoidGearDynamicAnalysis":
        return self._Cast_HypoidGearDynamicAnalysis(self)

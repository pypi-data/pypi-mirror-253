"""BevelGearPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4037
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "BevelGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearPowerFlow",)


Self = TypeVar("Self", bound="BevelGearPowerFlow")


class BevelGearPowerFlow(_4037.AGMAGleasonConicalGearPowerFlow):
    """BevelGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearPowerFlow")

    class _Cast_BevelGearPowerFlow:
        """Special nested class for casting BevelGearPowerFlow to subclasses."""

        def __init__(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
            parent: "BevelGearPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            return self._parent._cast(_4037.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConicalGearPowerFlow)

        @property
        def gear_power_flow(self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.MountableComponentPowerFlow)

        @property
        def component_power_flow(self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelDifferentialSunGearPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.StraightBevelSunGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.ZerolBevelGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "BevelGearPowerFlow":
            return self._parent

        def __getattr__(self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearPowerFlow.TYPE"):
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
    def cast_to(self: Self) -> "BevelGearPowerFlow._Cast_BevelGearPowerFlow":
        return self._Cast_BevelGearPowerFlow(self)

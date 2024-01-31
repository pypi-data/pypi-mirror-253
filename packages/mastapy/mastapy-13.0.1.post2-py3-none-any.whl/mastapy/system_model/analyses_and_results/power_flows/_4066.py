"""ConicalGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4095
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConicalGearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearSetPowerFlow")


class ConicalGearSetPowerFlow(_4095.GearSetPowerFlow):
    """ConicalGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetPowerFlow")

    class _Cast_ConicalGearSetPowerFlow:
        """Special nested class for casting ConicalGearSetPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
            parent: "ConicalGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            return self._parent._cast(_4095.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4038

            return self._parent._cast(_4038.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BevelGearSetPowerFlow)

        @property
        def hypoid_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(
                _4103.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(
                _4106.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(
                _4109.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.SpiralBevelGearSetPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.StraightBevelGearSetPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.ZerolBevelGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow",
        ) -> "ConicalGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2524.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearSetPowerFlow._Cast_ConicalGearSetPowerFlow":
        return self._Cast_ConicalGearSetPowerFlow(self)

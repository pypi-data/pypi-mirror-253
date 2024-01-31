"""PlanetaryGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4082
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "PlanetaryGearSetPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetPowerFlow",)


Self = TypeVar("Self", bound="PlanetaryGearSetPowerFlow")


class PlanetaryGearSetPowerFlow(_4082.CylindricalGearSetPowerFlow):
    """PlanetaryGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetPowerFlow")

    class _Cast_PlanetaryGearSetPowerFlow:
        """Special nested class for casting PlanetaryGearSetPowerFlow to subclasses."""

        def __init__(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
            parent: "PlanetaryGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            return self._parent._cast(_4082.CylindricalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_power_flow(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow",
        ) -> "PlanetaryGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetPowerFlow._Cast_PlanetaryGearSetPowerFlow":
        return self._Cast_PlanetaryGearSetPowerFlow(self)

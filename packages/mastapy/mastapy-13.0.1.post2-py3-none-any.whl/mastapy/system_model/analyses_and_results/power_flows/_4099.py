"""HypoidGearSetPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4038
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "HypoidGearSetPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2535
    from mastapy.system_model.analyses_and_results.static_loads import _6908
    from mastapy.gears.rating.hypoid import _440
    from mastapy.system_model.analyses_and_results.power_flows import _4098, _4097


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetPowerFlow",)


Self = TypeVar("Self", bound="HypoidGearSetPowerFlow")


class HypoidGearSetPowerFlow(_4038.AGMAGleasonConicalGearSetPowerFlow):
    """HypoidGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetPowerFlow")

    class _Cast_HypoidGearSetPowerFlow:
        """Special nested class for casting HypoidGearSetPowerFlow to subclasses."""

        def __init__(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
            parent: "HypoidGearSetPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            return self._parent._cast(_4038.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.ConicalGearSetPowerFlow)

        @property
        def gear_set_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.GearSetPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_power_flow(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow",
        ) -> "HypoidGearSetPowerFlow":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2535.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6908.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_440.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_440.HypoidGearSetRating":
        """mastapy.gears.rating.hypoid.HypoidGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_power_flow(self: Self) -> "List[_4098.HypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_power_flow(self: Self) -> "List[_4098.HypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_power_flow(self: Self) -> "List[_4097.HypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_power_flow(self: Self) -> "List[_4097.HypoidGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.HypoidGearMeshPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HypoidGearSetPowerFlow._Cast_HypoidGearSetPowerFlow":
        return self._Cast_HypoidGearSetPowerFlow(self)

"""RollingRingAssemblyPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4134
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "RollingRingAssemblyPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6945


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyPowerFlow",)


Self = TypeVar("Self", bound="RollingRingAssemblyPowerFlow")


class RollingRingAssemblyPowerFlow(_4134.SpecialisedAssemblyPowerFlow):
    """RollingRingAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssemblyPowerFlow")

    class _Cast_RollingRingAssemblyPowerFlow:
        """Special nested class for casting RollingRingAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
            parent: "RollingRingAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
        ):
            return self._parent._cast(_4134.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_power_flow(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
        ) -> "RollingRingAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingAssemblyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2597.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6945.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingAssemblyPowerFlow._Cast_RollingRingAssemblyPowerFlow":
        return self._Cast_RollingRingAssemblyPowerFlow(self)

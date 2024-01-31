"""PowerLoadPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4159
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PowerLoadPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6939


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadPowerFlow",)


Self = TypeVar("Self", bound="PowerLoadPowerFlow")


class PowerLoadPowerFlow(_4159.VirtualComponentPowerFlow):
    """PowerLoadPowerFlow

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadPowerFlow")

    class _Cast_PowerLoadPowerFlow:
        """Special nested class for casting PowerLoadPowerFlow to subclasses."""

        def __init__(
            self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow",
            parent: "PowerLoadPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_power_flow(
            self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow",
        ):
            return self._parent._cast(_4159.VirtualComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def component_power_flow(self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def power_load_power_flow(
            self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow",
        ) -> "PowerLoadPowerFlow":
            return self._parent

        def __getattr__(self: "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PowerLoadPowerFlow._Cast_PowerLoadPowerFlow":
        return self._Cast_PowerLoadPowerFlow(self)

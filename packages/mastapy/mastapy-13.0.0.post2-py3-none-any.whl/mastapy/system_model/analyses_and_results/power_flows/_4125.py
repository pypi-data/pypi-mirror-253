"""RingPinsPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4111
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "RingPinsPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2570
    from mastapy.system_model.analyses_and_results.static_loads import _6943


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsPowerFlow",)


Self = TypeVar("Self", bound="RingPinsPowerFlow")


class RingPinsPowerFlow(_4111.MountableComponentPowerFlow):
    """RingPinsPowerFlow

    This is a mastapy class.
    """

    TYPE = _RING_PINS_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsPowerFlow")

    class _Cast_RingPinsPowerFlow:
        """Special nested class for casting RingPinsPowerFlow to subclasses."""

        def __init__(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
            parent: "RingPinsPowerFlow",
        ):
            self._parent = parent

        @property
        def mountable_component_power_flow(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ):
            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def component_power_flow(self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def ring_pins_power_flow(
            self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow",
        ) -> "RingPinsPowerFlow":
            return self._parent

        def __getattr__(self: "RingPinsPowerFlow._Cast_RingPinsPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2570.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6943.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RingPinsPowerFlow._Cast_RingPinsPowerFlow":
        return self._Cast_RingPinsPowerFlow(self)

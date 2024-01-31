"""ShaftPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ShaftPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2482
    from mastapy.system_model.analyses_and_results.static_loads import _6950


__docformat__ = "restructuredtext en"
__all__ = ("ShaftPowerFlow",)


Self = TypeVar("Self", bound="ShaftPowerFlow")


class ShaftPowerFlow(_4034.AbstractShaftPowerFlow):
    """ShaftPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftPowerFlow")

    class _Cast_ShaftPowerFlow:
        """Special nested class for casting ShaftPowerFlow to subclasses."""

        def __init__(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow", parent: "ShaftPowerFlow"
        ):
            self._parent = parent

        @property
        def abstract_shaft_power_flow(self: "ShaftPowerFlow._Cast_ShaftPowerFlow"):
            return self._parent._cast(_4034.AbstractShaftPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4033

            return self._parent._cast(_4033.AbstractShaftOrHousingPowerFlow)

        @property
        def component_power_flow(self: "ShaftPowerFlow._Cast_ShaftPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(self: "ShaftPowerFlow._Cast_ShaftPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(self: "ShaftPowerFlow._Cast_ShaftPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "ShaftPowerFlow._Cast_ShaftPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "ShaftPowerFlow._Cast_ShaftPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ShaftPowerFlow._Cast_ShaftPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_power_flow(
            self: "ShaftPowerFlow._Cast_ShaftPowerFlow",
        ) -> "ShaftPowerFlow":
            return self._parent

        def __getattr__(self: "ShaftPowerFlow._Cast_ShaftPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pin_tangential_oscillation_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinTangentialOscillationFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2482.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6950.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ShaftPowerFlow._Cast_ShaftPowerFlow":
        return self._Cast_ShaftPowerFlow(self)

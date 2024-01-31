"""TorqueConverterPumpPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4070
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "TorqueConverterPumpPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6974


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterPumpPowerFlow")


class TorqueConverterPumpPowerFlow(_4070.CouplingHalfPowerFlow):
    """TorqueConverterPumpPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPumpPowerFlow")

    class _Cast_TorqueConverterPumpPowerFlow:
        """Special nested class for casting TorqueConverterPumpPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
            parent: "TorqueConverterPumpPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ):
            return self._parent._cast(_4070.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_pump_power_flow(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
        ) -> "TorqueConverterPumpPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterPumpPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6974.TorqueConverterPumpLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase

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
    ) -> "TorqueConverterPumpPowerFlow._Cast_TorqueConverterPumpPowerFlow":
        return self._Cast_TorqueConverterPumpPowerFlow(self)

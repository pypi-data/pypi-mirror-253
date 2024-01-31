"""MeasurementComponentPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4159
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "MeasurementComponentPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.static_loads import _6922


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentPowerFlow",)


Self = TypeVar("Self", bound="MeasurementComponentPowerFlow")


class MeasurementComponentPowerFlow(_4159.VirtualComponentPowerFlow):
    """MeasurementComponentPowerFlow

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeasurementComponentPowerFlow")

    class _Cast_MeasurementComponentPowerFlow:
        """Special nested class for casting MeasurementComponentPowerFlow to subclasses."""

        def __init__(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
            parent: "MeasurementComponentPowerFlow",
        ):
            self._parent = parent

        @property
        def virtual_component_power_flow(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ):
            return self._parent._cast(_4159.VirtualComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def measurement_component_power_flow(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
        ) -> "MeasurementComponentPowerFlow":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeasurementComponentPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2463.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6922.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

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
    ) -> "MeasurementComponentPowerFlow._Cast_MeasurementComponentPowerFlow":
        return self._Cast_MeasurementComponentPowerFlow(self)

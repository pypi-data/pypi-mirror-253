"""ShaftHubConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4068
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "ShaftHubConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.detailed_rigid_connectors.rating import _1435
    from mastapy.system_model.analyses_and_results.static_loads import _6949


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionPowerFlow",)


Self = TypeVar("Self", bound="ShaftHubConnectionPowerFlow")


class ShaftHubConnectionPowerFlow(_4068.ConnectorPowerFlow):
    """ShaftHubConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnectionPowerFlow")

    class _Cast_ShaftHubConnectionPowerFlow:
        """Special nested class for casting ShaftHubConnectionPowerFlow to subclasses."""

        def __init__(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
            parent: "ShaftHubConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def connector_power_flow(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ):
            return self._parent._cast(_4068.ConnectorPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_power_flow(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
        ) -> "ShaftHubConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftHubConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_1435.ShaftHubConnectionRating":
        """mastapy.detailed_rigid_connectors.rating.ShaftHubConnectionRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6949.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

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
    ) -> "ShaftHubConnectionPowerFlow._Cast_ShaftHubConnectionPowerFlow":
        return self._Cast_ShaftHubConnectionPowerFlow(self)

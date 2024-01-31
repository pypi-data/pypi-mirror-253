"""PlanetaryConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4133
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "PlanetaryConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6932


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionPowerFlow",)


Self = TypeVar("Self", bound="PlanetaryConnectionPowerFlow")


class PlanetaryConnectionPowerFlow(_4133.ShaftToMountableComponentConnectionPowerFlow):
    """PlanetaryConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionPowerFlow")

    class _Cast_PlanetaryConnectionPowerFlow:
        """Special nested class for casting PlanetaryConnectionPowerFlow to subclasses."""

        def __init__(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
            parent: "PlanetaryConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_power_flow(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
        ):
            return self._parent._cast(
                _4133.ShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def abstract_shaft_to_mountable_component_connection_power_flow(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4035

            return self._parent._cast(
                _4035.AbstractShaftToMountableComponentConnectionPowerFlow
            )

        @property
        def connection_power_flow(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_connection_power_flow(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
        ) -> "PlanetaryConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetaryConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6932.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryConnectionPowerFlow._Cast_PlanetaryConnectionPowerFlow":
        return self._Cast_PlanetaryConnectionPowerFlow(self)

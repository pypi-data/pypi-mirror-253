"""TorqueConverterConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4069
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "TorqueConverterConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2352
    from mastapy.system_model.analyses_and_results.static_loads import _6972


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterConnectionPowerFlow")


class TorqueConverterConnectionPowerFlow(_4069.CouplingConnectionPowerFlow):
    """TorqueConverterConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterConnectionPowerFlow")

    class _Cast_TorqueConverterConnectionPowerFlow:
        """Special nested class for casting TorqueConverterConnectionPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
            parent: "TorqueConverterConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_power_flow(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ):
            return self._parent._cast(_4069.CouplingConnectionPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_connection_power_flow(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
        ) -> "TorqueConverterConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "TorqueConverterConnectionPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2352.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6972.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

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
    ) -> "TorqueConverterConnectionPowerFlow._Cast_TorqueConverterConnectionPowerFlow":
        return self._Cast_TorqueConverterConnectionPowerFlow(self)

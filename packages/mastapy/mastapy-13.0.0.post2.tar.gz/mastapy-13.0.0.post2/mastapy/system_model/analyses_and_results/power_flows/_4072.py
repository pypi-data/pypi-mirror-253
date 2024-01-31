"""CVTBeltConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4041
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CVTBeltConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2273


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionPowerFlow",)


Self = TypeVar("Self", bound="CVTBeltConnectionPowerFlow")


class CVTBeltConnectionPowerFlow(_4041.BeltConnectionPowerFlow):
    """CVTBeltConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionPowerFlow")

    class _Cast_CVTBeltConnectionPowerFlow:
        """Special nested class for casting CVTBeltConnectionPowerFlow to subclasses."""

        def __init__(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
            parent: "CVTBeltConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def belt_connection_power_flow(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ):
            return self._parent._cast(_4041.BeltConnectionPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_power_flow(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
        ) -> "CVTBeltConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTBeltConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2273.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionPowerFlow._Cast_CVTBeltConnectionPowerFlow":
        return self._Cast_CVTBeltConnectionPowerFlow(self)

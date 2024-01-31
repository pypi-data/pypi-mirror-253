"""CouplingConnectionPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4099
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CouplingConnectionPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionPowerFlow",)


Self = TypeVar("Self", bound="CouplingConnectionPowerFlow")


class CouplingConnectionPowerFlow(_4099.InterMountableComponentConnectionPowerFlow):
    """CouplingConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionPowerFlow")

    class _Cast_CouplingConnectionPowerFlow:
        """Special nested class for casting CouplingConnectionPowerFlow to subclasses."""

        def __init__(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
            parent: "CouplingConnectionPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            return self._parent._cast(_4099.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4053

            return self._parent._cast(_4053.ClutchConnectionPowerFlow)

        @property
        def concept_coupling_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4058

            return self._parent._cast(_4058.ConceptCouplingConnectionPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartToPartShearCouplingConnectionPowerFlow)

        @property
        def spring_damper_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.SpringDamperConnectionPowerFlow)

        @property
        def torque_converter_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4154

            return self._parent._cast(_4154.TorqueConverterConnectionPowerFlow)

        @property
        def coupling_connection_power_flow(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
        ) -> "CouplingConnectionPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingConnectionPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2346.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

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
    ) -> "CouplingConnectionPowerFlow._Cast_CouplingConnectionPowerFlow":
        return self._Cast_CouplingConnectionPowerFlow(self)

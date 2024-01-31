"""AbstractShaftToMountableComponentConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4201
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4035


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundPowerFlow",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionCompoundPowerFlow"
)


class AbstractShaftToMountableComponentConnectionCompoundPowerFlow(
    _4201.ConnectionCompoundPowerFlow
):
    """AbstractShaftToMountableComponentConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
            parent: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def connection_compound_power_flow(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            return self._parent._cast(_4201.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_power_flow(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.CoaxialConnectionCompoundPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(
                _4210.CycloidalDiscCentralBearingConnectionCompoundPowerFlow
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_power_flow(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(
                _4212.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
            )

        @property
        def planetary_connection_compound_power_flow(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(_4249.PlanetaryConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(
                _4263.ShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
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
        self: Self,
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4035.AbstractShaftToMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftToMountableComponentConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4035.AbstractShaftToMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftToMountableComponentConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow(
            self
        )

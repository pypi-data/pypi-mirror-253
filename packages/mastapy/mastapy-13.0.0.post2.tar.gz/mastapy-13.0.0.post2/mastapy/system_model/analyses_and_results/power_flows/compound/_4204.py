"""CouplingConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4231
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CouplingConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4069


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundPowerFlow")


class CouplingConnectionCompoundPowerFlow(
    _4231.InterMountableComponentConnectionCompoundPowerFlow
):
    """CouplingConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionCompoundPowerFlow")

    class _Cast_CouplingConnectionCompoundPowerFlow:
        """Special nested class for casting CouplingConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
            parent: "CouplingConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            return self._parent._cast(
                _4231.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.ClutchConnectionCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(
                _4247.PartToPartShearCouplingConnectionCompoundPowerFlow
            )

        @property
        def spring_damper_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.SpringDamperConnectionCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
        ) -> "CouplingConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "CouplingConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4069.CouplingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow]

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
    ) -> "List[_4069.CouplingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow]

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
    ) -> (
        "CouplingConnectionCompoundPowerFlow._Cast_CouplingConnectionCompoundPowerFlow"
    ):
        return self._Cast_CouplingConnectionCompoundPowerFlow(self)

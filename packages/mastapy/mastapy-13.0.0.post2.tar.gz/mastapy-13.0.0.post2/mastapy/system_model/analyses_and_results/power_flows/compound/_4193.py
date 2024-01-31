"""ConceptCouplingConnectionCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4204
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConceptCouplingConnectionCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2344
    from mastapy.system_model.analyses_and_results.power_flows import _4058


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionCompoundPowerFlow")


class ConceptCouplingConnectionCompoundPowerFlow(
    _4204.CouplingConnectionCompoundPowerFlow
):
    """ConceptCouplingConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionCompoundPowerFlow"
    )

    class _Cast_ConceptCouplingConnectionCompoundPowerFlow:
        """Special nested class for casting ConceptCouplingConnectionCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow",
            parent: "ConceptCouplingConnectionCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_power_flow(
            self: "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow",
        ):
            return self._parent._cast(_4204.CouplingConnectionCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(
                _4231.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def connection_compound_power_flow(
            self: "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConnectionCompoundPowerFlow)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_power_flow(
            self: "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow",
        ) -> "ConceptCouplingConnectionCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "ConceptCouplingConnectionCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2344.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2344.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4058.ConceptCouplingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingConnectionPowerFlow]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4058.ConceptCouplingConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingConnectionPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionCompoundPowerFlow._Cast_ConceptCouplingConnectionCompoundPowerFlow":
        return self._Cast_ConceptCouplingConnectionCompoundPowerFlow(self)

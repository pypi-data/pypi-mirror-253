"""ConceptCouplingHalfCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConceptCouplingHalfCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2582
    from mastapy.system_model.analyses_and_results.power_flows import _4059


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConceptCouplingHalfCompoundPowerFlow")


class ConceptCouplingHalfCompoundPowerFlow(_4205.CouplingHalfCompoundPowerFlow):
    """ConceptCouplingHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingHalfCompoundPowerFlow")

    class _Cast_ConceptCouplingHalfCompoundPowerFlow:
        """Special nested class for casting ConceptCouplingHalfCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
            parent: "ConceptCouplingHalfCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
        ):
            return self._parent._cast(_4205.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
        ) -> "ConceptCouplingHalfCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "ConceptCouplingHalfCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2582.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4059.ConceptCouplingHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingHalfPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4059.ConceptCouplingHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConceptCouplingHalfPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingHalfCompoundPowerFlow._Cast_ConceptCouplingHalfCompoundPowerFlow":
        return self._Cast_ConceptCouplingHalfCompoundPowerFlow(self)

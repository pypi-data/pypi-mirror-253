"""SpringDamperHalfCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4206
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpringDamperHalfCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2601
    from mastapy.system_model.analyses_and_results.power_flows import _4140


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpringDamperHalfCompoundPowerFlow")


class SpringDamperHalfCompoundPowerFlow(_4206.CouplingHalfCompoundPowerFlow):
    """SpringDamperHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperHalfCompoundPowerFlow")

    class _Cast_SpringDamperHalfCompoundPowerFlow:
        """Special nested class for casting SpringDamperHalfCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
            parent: "SpringDamperHalfCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
        ):
            return self._parent._cast(_4206.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_half_compound_power_flow(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
        ) -> "SpringDamperHalfCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SpringDamperHalfCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2601.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

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
    ) -> "List[_4140.SpringDamperHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpringDamperHalfPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4140.SpringDamperHalfPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpringDamperHalfPowerFlow]

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
    ) -> "SpringDamperHalfCompoundPowerFlow._Cast_SpringDamperHalfCompoundPowerFlow":
        return self._Cast_SpringDamperHalfCompoundPowerFlow(self)

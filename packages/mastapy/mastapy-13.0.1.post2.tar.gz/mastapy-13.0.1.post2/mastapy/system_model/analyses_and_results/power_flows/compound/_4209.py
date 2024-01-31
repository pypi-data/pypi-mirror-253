"""CVTPulleyCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4255
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CVTPulleyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4074


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundPowerFlow",)


Self = TypeVar("Self", bound="CVTPulleyCompoundPowerFlow")


class CVTPulleyCompoundPowerFlow(_4255.PulleyCompoundPowerFlow):
    """CVTPulleyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCompoundPowerFlow")

    class _Cast_CVTPulleyCompoundPowerFlow:
        """Special nested class for casting CVTPulleyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
            parent: "CVTPulleyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def pulley_compound_power_flow(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
        ):
            return self._parent._cast(_4255.PulleyCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_power_flow(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
        ) -> "CVTPulleyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4074.CVTPulleyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CVTPulleyPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4074.CVTPulleyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CVTPulleyPowerFlow]

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
    ) -> "CVTPulleyCompoundPowerFlow._Cast_CVTPulleyCompoundPowerFlow":
        return self._Cast_CVTPulleyCompoundPowerFlow(self)

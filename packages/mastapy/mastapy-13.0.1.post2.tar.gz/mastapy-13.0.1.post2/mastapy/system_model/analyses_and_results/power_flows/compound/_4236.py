"""KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4233
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.power_flows import _4105


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow")


class KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow(
    _4233.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
):
    """KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            return self._parent._cast(
                _4233.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def conical_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

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
    ) -> "List[_4105.KlingelnbergCycloPalloidHypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearPowerFlow]

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
    ) -> "List[_4105.KlingelnbergCycloPalloidHypoidGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidHypoidGearPowerFlow]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow(self)

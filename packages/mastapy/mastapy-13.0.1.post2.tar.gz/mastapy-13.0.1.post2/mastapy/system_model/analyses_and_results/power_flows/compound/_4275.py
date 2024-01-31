"""StraightBevelGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4183
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "StraightBevelGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.power_flows import _4146


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelGearCompoundPowerFlow")


class StraightBevelGearCompoundPowerFlow(_4183.BevelGearCompoundPowerFlow):
    """StraightBevelGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearCompoundPowerFlow")

    class _Cast_StraightBevelGearCompoundPowerFlow:
        """Special nested class for casting StraightBevelGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
            parent: "StraightBevelGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_power_flow(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            return self._parent._cast(_4183.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4171,
            )

            return self._parent._cast(_4171.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
        ) -> "StraightBevelGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

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
    ) -> "List[_4146.StraightBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearPowerFlow]

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
    ) -> "List[_4146.StraightBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelGearPowerFlow]

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
    ) -> "StraightBevelGearCompoundPowerFlow._Cast_StraightBevelGearCompoundPowerFlow":
        return self._Cast_StraightBevelGearCompoundPowerFlow(self)

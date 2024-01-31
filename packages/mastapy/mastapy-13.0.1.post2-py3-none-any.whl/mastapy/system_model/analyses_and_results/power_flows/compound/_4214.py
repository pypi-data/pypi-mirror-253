"""CylindricalGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4225
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "CylindricalGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.gears.rating.cylindrical import _455
    from mastapy.system_model.analyses_and_results.power_flows import _4081


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="CylindricalGearCompoundPowerFlow")


class CylindricalGearCompoundPowerFlow(_4225.GearCompoundPowerFlow):
    """CylindricalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearCompoundPowerFlow")

    class _Cast_CylindricalGearCompoundPowerFlow:
        """Special nested class for casting CylindricalGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
            parent: "CylindricalGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_compound_power_flow(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
        ):
            return self._parent._cast(_4225.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
        ) -> "CylindricalGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_duty_cycle_rating(self: Self) -> "_455.CylindricalGearDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_duty_cycle_rating(
        self: Self,
    ) -> "_455.CylindricalGearDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4081.CylindricalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalGearPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4081.CylindricalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.CylindricalGearPowerFlow]

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
    ) -> "CylindricalGearCompoundPowerFlow._Cast_CylindricalGearCompoundPowerFlow":
        return self._Cast_CylindricalGearCompoundPowerFlow(self)

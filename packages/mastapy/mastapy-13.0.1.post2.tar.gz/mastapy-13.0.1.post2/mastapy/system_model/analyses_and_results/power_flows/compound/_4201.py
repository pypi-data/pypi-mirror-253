"""ConicalGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ConicalGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.conical import _541
    from mastapy.system_model.analyses_and_results.power_flows import _4066


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundPowerFlow")


class ConicalGearSetCompoundPowerFlow(_4227.GearSetCompoundPowerFlow):
    """ConicalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetCompoundPowerFlow")

    class _Cast_ConicalGearSetCompoundPowerFlow:
        """Special nested class for casting ConicalGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
            parent: "ConicalGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4227.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4167,
            )

            return self._parent._cast(_4167.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.BevelGearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(
                _4238.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(
                _4241.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.StraightBevelGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
        ) -> "ConicalGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_rating(self: Self) -> "_541.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_set_duty_cycle_rating(
        self: Self,
    ) -> "_541.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4066.ConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4066.ConicalGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ConicalGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetCompoundPowerFlow._Cast_ConicalGearSetCompoundPowerFlow":
        return self._Cast_ConicalGearSetCompoundPowerFlow(self)

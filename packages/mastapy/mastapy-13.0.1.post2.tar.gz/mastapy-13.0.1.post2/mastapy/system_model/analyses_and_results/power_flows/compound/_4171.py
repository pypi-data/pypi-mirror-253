"""AGMAGleasonConicalGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4199
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AGMAGleasonConicalGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4037


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundPowerFlow")


class AGMAGleasonConicalGearCompoundPowerFlow(_4199.ConicalGearCompoundPowerFlow):
    """AGMAGleasonConicalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundPowerFlow"
    )

    class _Cast_AGMAGleasonConicalGearCompoundPowerFlow:
        """Special nested class for casting AGMAGleasonConicalGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
            parent: "AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            return self._parent._cast(_4199.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4178,
            )

            return self._parent._cast(_4178.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(
                _4181.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4183,
            )

            return self._parent._cast(_4183.BevelGearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(_4229.HypoidGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.SpiralBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(_4272.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.StraightBevelSunGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4293,
            )

            return self._parent._cast(_4293.ZerolBevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
        ) -> "AGMAGleasonConicalGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4037.AGMAGleasonConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4037.AGMAGleasonConicalGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundPowerFlow._Cast_AGMAGleasonConicalGearCompoundPowerFlow":
        return self._Cast_AGMAGleasonConicalGearCompoundPowerFlow(self)

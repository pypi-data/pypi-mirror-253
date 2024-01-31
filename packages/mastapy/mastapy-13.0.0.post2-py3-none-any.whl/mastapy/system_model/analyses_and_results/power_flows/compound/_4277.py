"""StraightBevelPlanetGearCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4271
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "StraightBevelPlanetGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4147


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearCompoundPowerFlow")


class StraightBevelPlanetGearCompoundPowerFlow(
    _4271.StraightBevelDiffGearCompoundPowerFlow
):
    """StraightBevelPlanetGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearCompoundPowerFlow"
    )

    class _Cast_StraightBevelPlanetGearCompoundPowerFlow:
        """Special nested class for casting StraightBevelPlanetGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
            parent: "StraightBevelPlanetGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            return self._parent._cast(_4271.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4170,
            )

            return self._parent._cast(_4170.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
        ) -> "StraightBevelPlanetGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4147.StraightBevelPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelPlanetGearPowerFlow]

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
    ) -> "List[_4147.StraightBevelPlanetGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelPlanetGearPowerFlow]

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
    ) -> "StraightBevelPlanetGearCompoundPowerFlow._Cast_StraightBevelPlanetGearCompoundPowerFlow":
        return self._Cast_StraightBevelPlanetGearCompoundPowerFlow(self)

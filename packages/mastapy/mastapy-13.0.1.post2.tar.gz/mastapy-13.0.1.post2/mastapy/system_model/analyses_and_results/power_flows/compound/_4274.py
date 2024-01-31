"""StraightBevelDiffGearSetCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4185
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "StraightBevelDiffGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.power_flows import _4144
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4272,
        _4273,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCompoundPowerFlow")


class StraightBevelDiffGearSetCompoundPowerFlow(_4185.BevelGearSetCompoundPowerFlow):
    """StraightBevelDiffGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetCompoundPowerFlow"
    )

    class _Cast_StraightBevelDiffGearSetCompoundPowerFlow:
        """Special nested class for casting StraightBevelDiffGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
            parent: "StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_power_flow(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            return self._parent._cast(_4185.BevelGearSetCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConicalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4167,
            )

            return self._parent._cast(_4167.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
        ) -> "StraightBevelDiffGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2546.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4144.StraightBevelDiffGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearSetPowerFlow]

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
    def straight_bevel_diff_gears_compound_power_flow(
        self: Self,
    ) -> "List[_4272.StraightBevelDiffGearCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelDiffGearCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_power_flow(
        self: Self,
    ) -> "List[_4273.StraightBevelDiffGearMeshCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelDiffGearMeshCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4144.StraightBevelDiffGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearSetPowerFlow]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetCompoundPowerFlow._Cast_StraightBevelDiffGearSetCompoundPowerFlow":
        return self._Cast_StraightBevelDiffGearSetCompoundPowerFlow(self)

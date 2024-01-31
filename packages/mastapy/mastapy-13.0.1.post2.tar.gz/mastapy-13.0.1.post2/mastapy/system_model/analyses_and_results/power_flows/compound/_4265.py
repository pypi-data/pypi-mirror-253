"""SpecialisedAssemblyCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4167
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpecialisedAssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4135


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundPowerFlow")


class SpecialisedAssemblyCompoundPowerFlow(_4167.AbstractAssemblyCompoundPowerFlow):
    """SpecialisedAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundPowerFlow")

    class _Cast_SpecialisedAssemblyCompoundPowerFlow:
        """Special nested class for casting SpecialisedAssemblyCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
            parent: "SpecialisedAssemblyCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            return self._parent._cast(_4167.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.BevelGearSetCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4187,
            )

            return self._parent._cast(_4187.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.ClutchCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConicalGearSetCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.CouplingCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.CVTCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.CylindricalGearSetCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.FaceGearSetCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.GearSetCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.HypoidGearSetCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(
                _4238.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(
                _4241.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.PlanetaryGearSetCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(_4258.RollingRingAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.SpringDamperCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.StraightBevelGearSetCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.SynchroniserCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.TorqueConverterCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
        ) -> "SpecialisedAssemblyCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4135.SpecialisedAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow]

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
    ) -> "List[_4135.SpecialisedAssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpecialisedAssemblyPowerFlow]

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
    ) -> "SpecialisedAssemblyCompoundPowerFlow._Cast_SpecialisedAssemblyCompoundPowerFlow":
        return self._Cast_SpecialisedAssemblyCompoundPowerFlow(self)

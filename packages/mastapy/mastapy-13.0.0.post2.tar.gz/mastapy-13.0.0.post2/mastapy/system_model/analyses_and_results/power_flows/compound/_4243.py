"""MountableComponentCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4191
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "MountableComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4111


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="MountableComponentCompoundPowerFlow")


class MountableComponentCompoundPowerFlow(_4191.ComponentCompoundPowerFlow):
    """MountableComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentCompoundPowerFlow")

    class _Cast_MountableComponentCompoundPowerFlow:
        """Special nested class for casting MountableComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
            parent: "MountableComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            return self._parent._cast(_4191.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4170,
            )

            return self._parent._cast(_4170.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4174,
            )

            return self._parent._cast(_4174.BearingCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(
                _4180.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(_4181.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.BevelGearCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConicalGearCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.ConnectorCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.CVTPulleyCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(_4213.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.FaceGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.GearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(
                _4238.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(_4241.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.MeasurementComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(
                _4248.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planet_carrier_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(_4253.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(_4258.RollingRingCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.ShaftHubConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpiralBevelGearCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.ZerolBevelGearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "MountableComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4111.MountableComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow]

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
    ) -> "List[_4111.MountableComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow]

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
    ) -> (
        "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow"
    ):
        return self._Cast_MountableComponentCompoundPowerFlow(self)

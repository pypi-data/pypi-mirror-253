"""MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7166,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7089,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7145,
            )

            return self._parent._cast(
                _7145.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.BearingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7152,
            )

            return self._parent._cast(
                _7152.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7155,
            )

            return self._parent._cast(
                _7155.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7156,
            )

            return self._parent._cast(
                _7156.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7157,
            )

            return self._parent._cast(
                _7157.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7164,
            )

            return self._parent._cast(
                _7164.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7169,
            )

            return self._parent._cast(
                _7169.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7170,
            )

            return self._parent._cast(
                _7170.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7173,
            )

            return self._parent._cast(
                _7173.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7177,
            )

            return self._parent._cast(
                _7177.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7183,
            )

            return self._parent._cast(
                _7183.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7188,
            )

            return self._parent._cast(
                _7188.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7191,
            )

            return self._parent._cast(
                _7191.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7194,
            )

            return self._parent._cast(
                _7194.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7199,
            )

            return self._parent._cast(
                _7199.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7203,
            )

            return self._parent._cast(
                _7203.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7207,
            )

            return self._parent._cast(
                _7207.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7210,
            )

            return self._parent._cast(
                _7210.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7213,
            )

            return self._parent._cast(
                _7213.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7216,
            )

            return self._parent._cast(
                _7216.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7223,
            )

            return self._parent._cast(
                _7223.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7226,
            )

            return self._parent._cast(
                _7226.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7230,
            )

            return self._parent._cast(
                _7230.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7233,
            )

            return self._parent._cast(
                _7233.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7237,
            )

            return self._parent._cast(
                _7237.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7240,
            )

            return self._parent._cast(
                _7240.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7245,
            )

            return self._parent._cast(
                _7245.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7246,
            )

            return self._parent._cast(
                _7246.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7249,
            )

            return self._parent._cast(
                _7249.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7252,
            )

            return self._parent._cast(
                _7252.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7253,
            )

            return self._parent._cast(
                _7253.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7255,
            )

            return self._parent._cast(
                _7255.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7256,
            )

            return self._parent._cast(
                _7256.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7260,
            )

            return self._parent._cast(
                _7260.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7261,
            )

            return self._parent._cast(
                _7261.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7263,
            )

            return self._parent._cast(
                _7263.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7264,
            )

            return self._parent._cast(
                _7264.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7267,
            )

            return self._parent._cast(
                _7267.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.MountableComponentAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.MountableComponentAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )

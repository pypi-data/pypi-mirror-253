"""PartAnalysisCase"""
from __future__ import annotations

from typing import TypeVar

from PIL.Image import Image

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results import _2657
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartAnalysisCase"
)


__docformat__ = "restructuredtext en"
__all__ = ("PartAnalysisCase",)


Self = TypeVar("Self", bound="PartAnalysisCase")


class PartAnalysisCase(_2657.PartAnalysis):
    """PartAnalysisCase

    This is a mastapy class.
    """

    TYPE = _PART_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartAnalysisCase")

    class _Cast_PartAnalysisCase:
        """Special nested class for casting PartAnalysisCase to subclasses."""

        def __init__(
            self: "PartAnalysisCase._Cast_PartAnalysisCase", parent: "PartAnalysisCase"
        ):
            self._parent = parent

        @property
        def part_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(_2685.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2686,
            )

            return self._parent._cast(_2686.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2690,
            )

            return self._parent._cast(_2690.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2691,
            )

            return self._parent._cast(_2691.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2692,
            )

            return self._parent._cast(_2692.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2698,
            )

            return self._parent._cast(_2698.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2703,
            )

            return self._parent._cast(_2703.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(
                _2744.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(_2746.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(
                _2747.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2751,
            )

            return self._parent._cast(_2751.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.GearSetSystemDeflection)

        @property
        def gear_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2776,
            )

            return self._parent._cast(
                _2776.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.OilSealSystemDeflection)

        @property
        def part_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(_2794.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2800,
            )

            return self._parent._cast(_2800.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2983,
            )

            return self._parent._cast(
                _2983.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2984,
            )

            return self._parent._cast(
                _2984.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(_2985.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2988,
            )

            return self._parent._cast(
                _2988.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2989,
            )

            return self._parent._cast(
                _2989.AGMAGleasonConicalGearSteadyStateSynchronousResponse
            )

        @property
        def assembly_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2990,
            )

            return self._parent._cast(_2990.AssemblySteadyStateSynchronousResponse)

        @property
        def bearing_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2991,
            )

            return self._parent._cast(_2991.BearingSteadyStateSynchronousResponse)

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2993,
            )

            return self._parent._cast(_2993.BeltDriveSteadyStateSynchronousResponse)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2995,
            )

            return self._parent._cast(
                _2995.BevelDifferentialGearSetSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2996,
            )

            return self._parent._cast(
                _2996.BevelDifferentialGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2997,
            )

            return self._parent._cast(
                _2997.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2998,
            )

            return self._parent._cast(
                _2998.BevelDifferentialSunGearSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3000,
            )

            return self._parent._cast(_3000.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def bevel_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3001,
            )

            return self._parent._cast(_3001.BevelGearSteadyStateSynchronousResponse)

        @property
        def bolted_joint_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3002,
            )

            return self._parent._cast(_3002.BoltedJointSteadyStateSynchronousResponse)

        @property
        def bolt_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3003,
            )

            return self._parent._cast(_3003.BoltSteadyStateSynchronousResponse)

        @property
        def clutch_half_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3005,
            )

            return self._parent._cast(_3005.ClutchHalfSteadyStateSynchronousResponse)

        @property
        def clutch_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(_3006.ClutchSteadyStateSynchronousResponse)

        @property
        def component_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3008,
            )

            return self._parent._cast(_3008.ComponentSteadyStateSynchronousResponse)

        @property
        def concept_coupling_half_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(
                _3010.ConceptCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(
                _3011.ConceptCouplingSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3013,
            )

            return self._parent._cast(
                _3013.ConceptGearSetSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3014,
            )

            return self._parent._cast(_3014.ConceptGearSteadyStateSynchronousResponse)

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3016,
            )

            return self._parent._cast(
                _3016.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3017,
            )

            return self._parent._cast(_3017.ConicalGearSteadyStateSynchronousResponse)

        @property
        def connector_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(_3019.ConnectorSteadyStateSynchronousResponse)

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3021,
            )

            return self._parent._cast(_3021.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def coupling_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3022,
            )

            return self._parent._cast(_3022.CouplingSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3024,
            )

            return self._parent._cast(_3024.CVTPulleySteadyStateSynchronousResponse)

        @property
        def cvt_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(_3025.CVTSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3026,
            )

            return self._parent._cast(
                _3026.CycloidalAssemblySteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3029,
            )

            return self._parent._cast(_3029.CycloidalDiscSteadyStateSynchronousResponse)

        @property
        def cylindrical_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3031,
            )

            return self._parent._cast(
                _3031.CylindricalGearSetSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3032,
            )

            return self._parent._cast(
                _3032.CylindricalGearSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3033,
            )

            return self._parent._cast(
                _3033.CylindricalPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def datum_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3034,
            )

            return self._parent._cast(_3034.DatumSteadyStateSynchronousResponse)

        @property
        def external_cad_model_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3036,
            )

            return self._parent._cast(
                _3036.ExternalCADModelSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3038,
            )

            return self._parent._cast(_3038.FaceGearSetSteadyStateSynchronousResponse)

        @property
        def face_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(_3039.FaceGearSteadyStateSynchronousResponse)

        @property
        def fe_part_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3040,
            )

            return self._parent._cast(_3040.FEPartSteadyStateSynchronousResponse)

        @property
        def flexible_pin_assembly_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3041,
            )

            return self._parent._cast(
                _3041.FlexiblePinAssemblySteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3043,
            )

            return self._parent._cast(_3043.GearSetSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(_3044.GearSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.GuideDxfModelSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3047,
            )

            return self._parent._cast(_3047.HypoidGearSetSteadyStateSynchronousResponse)

        @property
        def hypoid_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3048,
            )

            return self._parent._cast(_3048.HypoidGearSteadyStateSynchronousResponse)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(
                _3051.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3052,
            )

            return self._parent._cast(
                _3052.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3054,
            )

            return self._parent._cast(
                _3054.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3055,
            )

            return self._parent._cast(
                _3055.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3057,
            )

            return self._parent._cast(
                _3057.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3058,
            )

            return self._parent._cast(
                _3058.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3059,
            )

            return self._parent._cast(_3059.MassDiscSteadyStateSynchronousResponse)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3060,
            )

            return self._parent._cast(
                _3060.MeasurementComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3061,
            )

            return self._parent._cast(
                _3061.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3062,
            )

            return self._parent._cast(_3062.OilSealSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(_3063.PartSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(
                _3065.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(
                _3066.PartToPartShearCouplingSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3068,
            )

            return self._parent._cast(
                _3068.PlanetaryGearSetSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3069,
            )

            return self._parent._cast(_3069.PlanetCarrierSteadyStateSynchronousResponse)

        @property
        def point_load_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3070,
            )

            return self._parent._cast(_3070.PointLoadSteadyStateSynchronousResponse)

        @property
        def power_load_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3071,
            )

            return self._parent._cast(_3071.PowerLoadSteadyStateSynchronousResponse)

        @property
        def pulley_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3072,
            )

            return self._parent._cast(_3072.PulleySteadyStateSynchronousResponse)

        @property
        def ring_pins_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3073,
            )

            return self._parent._cast(_3073.RingPinsSteadyStateSynchronousResponse)

        @property
        def rolling_ring_assembly_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3075,
            )

            return self._parent._cast(
                _3075.RollingRingAssemblySteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3077,
            )

            return self._parent._cast(_3077.RollingRingSteadyStateSynchronousResponse)

        @property
        def root_assembly_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3078,
            )

            return self._parent._cast(_3078.RootAssemblySteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3079,
            )

            return self._parent._cast(
                _3079.ShaftHubConnectionSteadyStateSynchronousResponse
            )

        @property
        def shaft_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3080,
            )

            return self._parent._cast(_3080.ShaftSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3082,
            )

            return self._parent._cast(
                _3082.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.SpiralBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3085,
            )

            return self._parent._cast(
                _3085.SpiralBevelGearSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3087,
            )

            return self._parent._cast(
                _3087.SpringDamperHalfSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3088,
            )

            return self._parent._cast(_3088.SpringDamperSteadyStateSynchronousResponse)

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3093,
            )

            return self._parent._cast(
                _3093.StraightBevelDiffGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3094,
            )

            return self._parent._cast(
                _3094.StraightBevelDiffGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3096,
            )

            return self._parent._cast(
                _3096.StraightBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3097,
            )

            return self._parent._cast(
                _3097.StraightBevelGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3098,
            )

            return self._parent._cast(
                _3098.StraightBevelPlanetGearSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3099,
            )

            return self._parent._cast(
                _3099.StraightBevelSunGearSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3100,
            )

            return self._parent._cast(
                _3100.SynchroniserHalfSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3101,
            )

            return self._parent._cast(
                _3101.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3102,
            )

            return self._parent._cast(
                _3102.SynchroniserSleeveSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3103,
            )

            return self._parent._cast(_3103.SynchroniserSteadyStateSynchronousResponse)

        @property
        def torque_converter_pump_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.TorqueConverterPumpSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3106,
            )

            return self._parent._cast(
                _3106.TorqueConverterSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3107,
            )

            return self._parent._cast(
                _3107.TorqueConverterTurbineSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3108,
            )

            return self._parent._cast(
                _3108.UnbalancedMassSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3109,
            )

            return self._parent._cast(
                _3109.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3111,
            )

            return self._parent._cast(_3111.WormGearSetSteadyStateSynchronousResponse)

        @property
        def worm_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3112,
            )

            return self._parent._cast(_3112.WormGearSteadyStateSynchronousResponse)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3114,
            )

            return self._parent._cast(
                _3114.ZerolBevelGearSetSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3115,
            )

            return self._parent._cast(
                _3115.ZerolBevelGearSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3245,
            )

            return self._parent._cast(
                _3245.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3246,
            )

            return self._parent._cast(
                _3246.AbstractShaftOrHousingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3247,
            )

            return self._parent._cast(
                _3247.AbstractShaftSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3250,
            )

            return self._parent._cast(
                _3250.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3251,
            )

            return self._parent._cast(
                _3251.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3252,
            )

            return self._parent._cast(
                _3252.AssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3253,
            )

            return self._parent._cast(
                _3253.BearingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3255,
            )

            return self._parent._cast(
                _3255.BeltDriveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3257,
            )

            return self._parent._cast(
                _3257.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3258,
            )

            return self._parent._cast(
                _3258.BevelDifferentialGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3259,
            )

            return self._parent._cast(
                _3259.BevelDifferentialPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3260,
            )

            return self._parent._cast(
                _3260.BevelDifferentialSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3262,
            )

            return self._parent._cast(
                _3262.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3263,
            )

            return self._parent._cast(
                _3263.BevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3264,
            )

            return self._parent._cast(
                _3264.BoltedJointSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3265,
            )

            return self._parent._cast(_3265.BoltSteadyStateSynchronousResponseOnAShaft)

        @property
        def clutch_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3267,
            )

            return self._parent._cast(
                _3267.ClutchHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.ClutchSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3270,
            )

            return self._parent._cast(
                _3270.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.ConceptCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3275,
            )

            return self._parent._cast(
                _3275.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3276,
            )

            return self._parent._cast(
                _3276.ConceptGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3278,
            )

            return self._parent._cast(
                _3278.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3279,
            )

            return self._parent._cast(
                _3279.ConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3281,
            )

            return self._parent._cast(
                _3281.ConnectorSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3283,
            )

            return self._parent._cast(
                _3283.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3284,
            )

            return self._parent._cast(
                _3284.CouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3286,
            )

            return self._parent._cast(
                _3286.CVTPulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3287,
            )

            return self._parent._cast(_3287.CVTSteadyStateSynchronousResponseOnAShaft)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3288,
            )

            return self._parent._cast(
                _3288.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3291,
            )

            return self._parent._cast(
                _3291.CycloidalDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3293,
            )

            return self._parent._cast(
                _3293.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3294,
            )

            return self._parent._cast(
                _3294.CylindricalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3295,
            )

            return self._parent._cast(
                _3295.CylindricalPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3296,
            )

            return self._parent._cast(_3296.DatumSteadyStateSynchronousResponseOnAShaft)

        @property
        def external_cad_model_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3297,
            )

            return self._parent._cast(
                _3297.ExternalCADModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3299,
            )

            return self._parent._cast(
                _3299.FaceGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3300,
            )

            return self._parent._cast(
                _3300.FaceGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.FEPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3302,
            )

            return self._parent._cast(
                _3302.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3304,
            )

            return self._parent._cast(
                _3304.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(_3305.GearSteadyStateSynchronousResponseOnAShaft)

        @property
        def guide_dxf_model_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3306,
            )

            return self._parent._cast(
                _3306.GuideDxfModelSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3308,
            )

            return self._parent._cast(
                _3308.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.HypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3313,
            )

            return self._parent._cast(
                _3313.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3315,
            )

            return self._parent._cast(
                _3315.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3316,
            )

            return self._parent._cast(
                _3316.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3318,
            )

            return self._parent._cast(
                _3318.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3319,
            )

            return self._parent._cast(
                _3319.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3320,
            )

            return self._parent._cast(
                _3320.MassDiscSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3321,
            )

            return self._parent._cast(
                _3321.MeasurementComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3322,
            )

            return self._parent._cast(
                _3322.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3323,
            )

            return self._parent._cast(
                _3323.OilSealSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(_3324.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(
                _3326.PartToPartShearCouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3329,
            )

            return self._parent._cast(
                _3329.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3330,
            )

            return self._parent._cast(
                _3330.PlanetCarrierSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3331,
            )

            return self._parent._cast(
                _3331.PointLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3332,
            )

            return self._parent._cast(
                _3332.PowerLoadSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3333,
            )

            return self._parent._cast(
                _3333.PulleySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3334,
            )

            return self._parent._cast(
                _3334.RingPinsSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3336,
            )

            return self._parent._cast(
                _3336.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3338,
            )

            return self._parent._cast(
                _3338.RollingRingSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3339,
            )

            return self._parent._cast(
                _3339.RootAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3340,
            )

            return self._parent._cast(
                _3340.ShaftHubConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3341,
            )

            return self._parent._cast(_3341.ShaftSteadyStateSynchronousResponseOnAShaft)

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3343,
            )

            return self._parent._cast(
                _3343.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.SpiralBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3348,
            )

            return self._parent._cast(
                _3348.SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3349,
            )

            return self._parent._cast(
                _3349.SpringDamperSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3352,
            )

            return self._parent._cast(
                _3352.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.StraightBevelDiffGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3355,
            )

            return self._parent._cast(
                _3355.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3356,
            )

            return self._parent._cast(
                _3356.StraightBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3357,
            )

            return self._parent._cast(
                _3357.StraightBevelPlanetGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3358,
            )

            return self._parent._cast(
                _3358.StraightBevelSunGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3359,
            )

            return self._parent._cast(
                _3359.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3360,
            )

            return self._parent._cast(
                _3360.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3361,
            )

            return self._parent._cast(
                _3361.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3362,
            )

            return self._parent._cast(
                _3362.SynchroniserSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3364,
            )

            return self._parent._cast(
                _3364.TorqueConverterPumpSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3365,
            )

            return self._parent._cast(
                _3365.TorqueConverterSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.TorqueConverterTurbineSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3367,
            )

            return self._parent._cast(
                _3367.UnbalancedMassSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3368,
            )

            return self._parent._cast(
                _3368.VirtualComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3370,
            )

            return self._parent._cast(
                _3370.WormGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3371,
            )

            return self._parent._cast(
                _3371.WormGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3373,
            )

            return self._parent._cast(
                _3373.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_on_a_shaft(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3374,
            )

            return self._parent._cast(
                _3374.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3504,
            )

            return self._parent._cast(
                _3504.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3505,
            )

            return self._parent._cast(
                _3505.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3506,
            )

            return self._parent._cast(
                _3506.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3509,
            )

            return self._parent._cast(
                _3509.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3510,
            )

            return self._parent._cast(
                _3510.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3511,
            )

            return self._parent._cast(
                _3511.AssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3512,
            )

            return self._parent._cast(
                _3512.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3514,
            )

            return self._parent._cast(
                _3514.BeltDriveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3516,
            )

            return self._parent._cast(
                _3516.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3517,
            )

            return self._parent._cast(
                _3517.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3518,
            )

            return self._parent._cast(
                _3518.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3519,
            )

            return self._parent._cast(
                _3519.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3521,
            )

            return self._parent._cast(
                _3521.BevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3522,
            )

            return self._parent._cast(
                _3522.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3523,
            )

            return self._parent._cast(
                _3523.BoltedJointSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3524,
            )

            return self._parent._cast(_3524.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3526,
            )

            return self._parent._cast(
                _3526.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3527,
            )

            return self._parent._cast(
                _3527.ClutchSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3532,
            )

            return self._parent._cast(
                _3532.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3534,
            )

            return self._parent._cast(
                _3534.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3537,
            )

            return self._parent._cast(
                _3537.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3543,
            )

            return self._parent._cast(
                _3543.CouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3545,
            )

            return self._parent._cast(
                _3545.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3546,
            )

            return self._parent._cast(_3546.CVTSteadyStateSynchronousResponseAtASpeed)

        @property
        def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(
                _3547.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3550,
            )

            return self._parent._cast(
                _3550.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3552,
            )

            return self._parent._cast(
                _3552.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3553,
            )

            return self._parent._cast(
                _3553.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3554,
            )

            return self._parent._cast(
                _3554.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3555,
            )

            return self._parent._cast(_3555.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3556,
            )

            return self._parent._cast(
                _3556.ExternalCADModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3558,
            )

            return self._parent._cast(
                _3558.FaceGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3559,
            )

            return self._parent._cast(
                _3559.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3560,
            )

            return self._parent._cast(
                _3560.FEPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3563,
            )

            return self._parent._cast(
                _3563.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(_3564.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.GuideDxfModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3567,
            )

            return self._parent._cast(
                _3567.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3572,
            )

            return self._parent._cast(
                _3572.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3574,
            )

            return self._parent._cast(
                _3574.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3575,
            )

            return self._parent._cast(
                _3575.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(
                _3578.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3580,
            )

            return self._parent._cast(
                _3580.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3581,
            )

            return self._parent._cast(
                _3581.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(_3583.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3586,
            )

            return self._parent._cast(
                _3586.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3589,
            )

            return self._parent._cast(
                _3589.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3590,
            )

            return self._parent._cast(
                _3590.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(
                _3591.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3592,
            )

            return self._parent._cast(
                _3592.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3593,
            )

            return self._parent._cast(
                _3593.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3595,
            )

            return self._parent._cast(
                _3595.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3597,
            )

            return self._parent._cast(
                _3597.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3598,
            )

            return self._parent._cast(
                _3598.RootAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3599,
            )

            return self._parent._cast(
                _3599.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3600,
            )

            return self._parent._cast(_3600.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3605,
            )

            return self._parent._cast(
                _3605.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3607,
            )

            return self._parent._cast(
                _3607.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.SpringDamperSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3611,
            )

            return self._parent._cast(
                _3611.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3617,
            )

            return self._parent._cast(
                _3617.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3618,
            )

            return self._parent._cast(
                _3618.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3619,
            )

            return self._parent._cast(
                _3619.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3621,
            )

            return self._parent._cast(
                _3621.SynchroniserSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(
                _3623.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3624,
            )

            return self._parent._cast(
                _3624.TorqueConverterSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3625,
            )

            return self._parent._cast(
                _3625.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3626,
            )

            return self._parent._cast(
                _3626.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3627,
            )

            return self._parent._cast(
                _3627.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3629,
            )

            return self._parent._cast(
                _3629.WormGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(
                _3630.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3632,
            )

            return self._parent._cast(
                _3632.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3633,
            )

            return self._parent._cast(
                _3633.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3763,
            )

            return self._parent._cast(_3763.AbstractAssemblyStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3764,
            )

            return self._parent._cast(_3764.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AbstractShaftStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3768,
            )

            return self._parent._cast(_3768.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3769,
            )

            return self._parent._cast(_3769.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def assembly_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3770,
            )

            return self._parent._cast(_3770.AssemblyStabilityAnalysis)

        @property
        def bearing_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.BearingStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BeltDriveStabilityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3775,
            )

            return self._parent._cast(_3775.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3777,
            )

            return self._parent._cast(
                _3777.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3780,
            )

            return self._parent._cast(_3780.BevelGearSetStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3781,
            )

            return self._parent._cast(_3781.BevelGearStabilityAnalysis)

        @property
        def bolted_joint_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3782,
            )

            return self._parent._cast(_3782.BoltedJointStabilityAnalysis)

        @property
        def bolt_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.BoltStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.ClutchHalfStabilityAnalysis)

        @property
        def clutch_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.ClutchStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_coupling_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.ConceptCouplingStabilityAnalysis)

        @property
        def concept_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3793,
            )

            return self._parent._cast(_3793.ConceptGearSetStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3801,
            )

            return self._parent._cast(_3801.CouplingHalfStabilityAnalysis)

        @property
        def coupling_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.CouplingStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3805,
            )

            return self._parent._cast(_3805.CVTPulleyStabilityAnalysis)

        @property
        def cvt_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3806,
            )

            return self._parent._cast(_3806.CVTStabilityAnalysis)

        @property
        def cycloidal_assembly_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(_3807.CycloidalAssemblyStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.CycloidalDiscStabilityAnalysis)

        @property
        def cylindrical_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.CylindricalGearSetStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3814,
            )

            return self._parent._cast(_3814.CylindricalPlanetGearStabilityAnalysis)

        @property
        def datum_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3815,
            )

            return self._parent._cast(_3815.DatumStabilityAnalysis)

        @property
        def external_cad_model_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.ExternalCADModelStabilityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.FaceGearSetStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.FaceGearStabilityAnalysis)

        @property
        def fe_part_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3821,
            )

            return self._parent._cast(_3821.FEPartStabilityAnalysis)

        @property
        def flexible_pin_assembly_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.FlexiblePinAssemblyStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3824,
            )

            return self._parent._cast(_3824.GearSetStabilityAnalysis)

        @property
        def gear_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.GearStabilityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3826,
            )

            return self._parent._cast(_3826.GuideDxfModelStabilityAnalysis)

        @property
        def hypoid_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(_3828.HypoidGearSetStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3829,
            )

            return self._parent._cast(_3829.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3833,
            )

            return self._parent._cast(
                _3833.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(
                _3835.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(
                _3836.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(
                _3838.KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3839,
            )

            return self._parent._cast(
                _3839.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3840,
            )

            return self._parent._cast(_3840.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.MeasurementComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(_3843.OilSealStabilityAnalysis)

        @property
        def part_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(
                _3846.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.PartToPartShearCouplingStabilityAnalysis)

        @property
        def planetary_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3849,
            )

            return self._parent._cast(_3849.PlanetaryGearSetStabilityAnalysis)

        @property
        def planet_carrier_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3851,
            )

            return self._parent._cast(_3851.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(_3853.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3854,
            )

            return self._parent._cast(_3854.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(_3856.RollingRingAssemblyStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3858,
            )

            return self._parent._cast(_3858.RollingRingStabilityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(_3859.RootAssemblyStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.ShaftHubConnectionStabilityAnalysis)

        @property
        def shaft_stability_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3861,
            )

            return self._parent._cast(_3861.ShaftStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpecialisedAssemblyStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpiralBevelGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(_3868.SpringDamperHalfStabilityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3869,
            )

            return self._parent._cast(_3869.SpringDamperStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3879,
            )

            return self._parent._cast(_3879.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.SynchroniserSleeveStabilityAnalysis)

        @property
        def synchroniser_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.SynchroniserStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.TorqueConverterStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.WormGearSetStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3893,
            )

            return self._parent._cast(_3893.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3895,
            )

            return self._parent._cast(_3895.ZerolBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3896,
            )

            return self._parent._cast(_3896.ZerolBevelGearStabilityAnalysis)

        @property
        def abstract_assembly_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4033

            return self._parent._cast(_4033.AbstractShaftOrHousingPowerFlow)

        @property
        def abstract_shaft_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AbstractShaftPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4037

            return self._parent._cast(_4037.AGMAGleasonConicalGearPowerFlow)

        @property
        def agma_gleason_conical_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4038

            return self._parent._cast(_4038.AGMAGleasonConicalGearSetPowerFlow)

        @property
        def assembly_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4039

            return self._parent._cast(_4039.AssemblyPowerFlow)

        @property
        def bearing_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4040

            return self._parent._cast(_4040.BearingPowerFlow)

        @property
        def belt_drive_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4042

            return self._parent._cast(_4042.BeltDrivePowerFlow)

        @property
        def bevel_differential_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4044

            return self._parent._cast(_4044.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4045

            return self._parent._cast(_4045.BevelDifferentialGearSetPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4047

            return self._parent._cast(_4047.BevelDifferentialSunGearPowerFlow)

        @property
        def bevel_gear_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BevelGearPowerFlow)

        @property
        def bevel_gear_set_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4050

            return self._parent._cast(_4050.BevelGearSetPowerFlow)

        @property
        def bolted_joint_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4051

            return self._parent._cast(_4051.BoltedJointPowerFlow)

        @property
        def bolt_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4052

            return self._parent._cast(_4052.BoltPowerFlow)

        @property
        def clutch_half_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4054

            return self._parent._cast(_4054.ClutchHalfPowerFlow)

        @property
        def clutch_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4055

            return self._parent._cast(_4055.ClutchPowerFlow)

        @property
        def component_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def concept_coupling_half_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ConceptCouplingHalfPowerFlow)

        @property
        def concept_coupling_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4060

            return self._parent._cast(_4060.ConceptCouplingPowerFlow)

        @property
        def concept_gear_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4062

            return self._parent._cast(_4062.ConceptGearPowerFlow)

        @property
        def concept_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4063

            return self._parent._cast(_4063.ConceptGearSetPowerFlow)

        @property
        def conical_gear_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4065

            return self._parent._cast(_4065.ConicalGearPowerFlow)

        @property
        def conical_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4066

            return self._parent._cast(_4066.ConicalGearSetPowerFlow)

        @property
        def connector_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4068

            return self._parent._cast(_4068.ConnectorPowerFlow)

        @property
        def coupling_half_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4070

            return self._parent._cast(_4070.CouplingHalfPowerFlow)

        @property
        def coupling_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4071

            return self._parent._cast(_4071.CouplingPowerFlow)

        @property
        def cvt_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.CVTPowerFlow)

        @property
        def cvt_pulley_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.CVTPulleyPowerFlow)

        @property
        def cycloidal_assembly_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4075

            return self._parent._cast(_4075.CycloidalAssemblyPowerFlow)

        @property
        def cycloidal_disc_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4078

            return self._parent._cast(_4078.CycloidalDiscPowerFlow)

        @property
        def cylindrical_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4081

            return self._parent._cast(_4081.CylindricalGearPowerFlow)

        @property
        def cylindrical_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4082

            return self._parent._cast(_4082.CylindricalGearSetPowerFlow)

        @property
        def cylindrical_planet_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4083

            return self._parent._cast(_4083.CylindricalPlanetGearPowerFlow)

        @property
        def datum_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4084

            return self._parent._cast(_4084.DatumPowerFlow)

        @property
        def external_cad_model_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4085

            return self._parent._cast(_4085.ExternalCADModelPowerFlow)

        @property
        def face_gear_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4087

            return self._parent._cast(_4087.FaceGearPowerFlow)

        @property
        def face_gear_set_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4088

            return self._parent._cast(_4088.FaceGearSetPowerFlow)

        @property
        def fe_part_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4091

            return self._parent._cast(_4091.FEPartPowerFlow)

        @property
        def flexible_pin_assembly_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4092

            return self._parent._cast(_4092.FlexiblePinAssemblyPowerFlow)

        @property
        def gear_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4094

            return self._parent._cast(_4094.GearPowerFlow)

        @property
        def gear_set_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4095

            return self._parent._cast(_4095.GearSetPowerFlow)

        @property
        def guide_dxf_model_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.GuideDxfModelPowerFlow)

        @property
        def hypoid_gear_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4098

            return self._parent._cast(_4098.HypoidGearPowerFlow)

        @property
        def hypoid_gear_set_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4099

            return self._parent._cast(_4099.HypoidGearSetPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(
                _4102.KlingelnbergCycloPalloidConicalGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4103

            return self._parent._cast(
                _4103.KlingelnbergCycloPalloidConicalGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4105

            return self._parent._cast(_4105.KlingelnbergCycloPalloidHypoidGearPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4106

            return self._parent._cast(
                _4106.KlingelnbergCycloPalloidHypoidGearSetPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4108

            return self._parent._cast(
                _4108.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4109

            return self._parent._cast(
                _4109.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
            )

        @property
        def mass_disc_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4110

            return self._parent._cast(_4110.MassDiscPowerFlow)

        @property
        def measurement_component_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MeasurementComponentPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4112

            return self._parent._cast(_4112.MountableComponentPowerFlow)

        @property
        def oil_seal_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.OilSealPowerFlow)

        @property
        def part_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.PartPowerFlow)

        @property
        def part_to_part_shear_coupling_half_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartToPartShearCouplingHalfPowerFlow)

        @property
        def part_to_part_shear_coupling_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4117

            return self._parent._cast(_4117.PartToPartShearCouplingPowerFlow)

        @property
        def planetary_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4119

            return self._parent._cast(_4119.PlanetaryGearSetPowerFlow)

        @property
        def planet_carrier_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4120

            return self._parent._cast(_4120.PlanetCarrierPowerFlow)

        @property
        def point_load_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4121

            return self._parent._cast(_4121.PointLoadPowerFlow)

        @property
        def power_load_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4124

            return self._parent._cast(_4124.PowerLoadPowerFlow)

        @property
        def pulley_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4125

            return self._parent._cast(_4125.PulleyPowerFlow)

        @property
        def ring_pins_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4126

            return self._parent._cast(_4126.RingPinsPowerFlow)

        @property
        def rolling_ring_assembly_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4128

            return self._parent._cast(_4128.RollingRingAssemblyPowerFlow)

        @property
        def rolling_ring_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4130

            return self._parent._cast(_4130.RollingRingPowerFlow)

        @property
        def root_assembly_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4131

            return self._parent._cast(_4131.RootAssemblyPowerFlow)

        @property
        def shaft_hub_connection_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4132

            return self._parent._cast(_4132.ShaftHubConnectionPowerFlow)

        @property
        def shaft_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4133

            return self._parent._cast(_4133.ShaftPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4135

            return self._parent._cast(_4135.SpecialisedAssemblyPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpiralBevelGearPowerFlow)

        @property
        def spiral_bevel_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4138

            return self._parent._cast(_4138.SpiralBevelGearSetPowerFlow)

        @property
        def spring_damper_half_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4140

            return self._parent._cast(_4140.SpringDamperHalfPowerFlow)

        @property
        def spring_damper_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4141

            return self._parent._cast(_4141.SpringDamperPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4143

            return self._parent._cast(_4143.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_diff_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4144

            return self._parent._cast(_4144.StraightBevelDiffGearSetPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4146

            return self._parent._cast(_4146.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4147

            return self._parent._cast(_4147.StraightBevelGearSetPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.StraightBevelSunGearPowerFlow)

        @property
        def synchroniser_half_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.SynchroniserPartPowerFlow)

        @property
        def synchroniser_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.SynchroniserPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4153

            return self._parent._cast(_4153.SynchroniserSleevePowerFlow)

        @property
        def torque_converter_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4156

            return self._parent._cast(_4156.TorqueConverterPowerFlow)

        @property
        def torque_converter_pump_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4157

            return self._parent._cast(_4157.TorqueConverterPumpPowerFlow)

        @property
        def torque_converter_turbine_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4158

            return self._parent._cast(_4158.TorqueConverterTurbinePowerFlow)

        @property
        def unbalanced_mass_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4159

            return self._parent._cast(_4159.UnbalancedMassPowerFlow)

        @property
        def virtual_component_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4160

            return self._parent._cast(_4160.VirtualComponentPowerFlow)

        @property
        def worm_gear_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4162

            return self._parent._cast(_4162.WormGearPowerFlow)

        @property
        def worm_gear_set_power_flow(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.power_flows import _4163

            return self._parent._cast(_4163.WormGearSetPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4165

            return self._parent._cast(_4165.ZerolBevelGearPowerFlow)

        @property
        def zerol_bevel_gear_set_power_flow(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4166

            return self._parent._cast(_4166.ZerolBevelGearSetPowerFlow)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4296,
            )

            return self._parent._cast(_4296.AbstractAssemblyParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4297,
            )

            return self._parent._cast(_4297.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(_4298.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(_4301.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4302,
            )

            return self._parent._cast(
                _4302.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def assembly_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4303,
            )

            return self._parent._cast(_4303.AssemblyParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.BearingParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(_4306.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4308,
            )

            return self._parent._cast(_4308.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4309,
            )

            return self._parent._cast(_4309.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(
                _4310.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4311,
            )

            return self._parent._cast(_4311.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4313,
            )

            return self._parent._cast(_4313.BevelGearParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4314,
            )

            return self._parent._cast(_4314.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.BoltedJointParametricStudyTool)

        @property
        def bolt_parametric_study_tool(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4316,
            )

            return self._parent._cast(_4316.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ClutchHalfParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4319,
            )

            return self._parent._cast(_4319.ClutchParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ComponentParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4324,
            )

            return self._parent._cast(_4324.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ConceptGearParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4327,
            )

            return self._parent._cast(_4327.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConicalGearParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4330,
            )

            return self._parent._cast(_4330.ConicalGearSetParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.CouplingHalfParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4335,
            )

            return self._parent._cast(_4335.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.CVTParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(_4339.CycloidalAssemblyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4345,
            )

            return self._parent._cast(_4345.CylindricalGearSetParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4346,
            )

            return self._parent._cast(_4346.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4347,
            )

            return self._parent._cast(_4347.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4355,
            )

            return self._parent._cast(_4355.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4357,
            )

            return self._parent._cast(_4357.FaceGearParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4358,
            )

            return self._parent._cast(_4358.FaceGearSetParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.FEPartParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_parametric_study_tool(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.GearParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4363,
            )

            return self._parent._cast(_4363.GearSetParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(_4366.HypoidGearParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4367,
            )

            return self._parent._cast(_4367.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4371,
            )

            return self._parent._cast(
                _4371.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4374,
            )

            return self._parent._cast(
                _4374.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(
                _4376.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4377,
            )

            return self._parent._cast(
                _4377.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(_4379.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4382,
            )

            return self._parent._cast(_4382.OilSealParametricStudyTool)

        @property
        def part_parametric_study_tool(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4393,
            )

            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(
                _4395.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4396,
            )

            return self._parent._cast(_4396.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PlanetaryGearSetParametricStudyTool)

        @property
        def planet_carrier_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4403,
            )

            return self._parent._cast(_4403.RingPinsParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4405,
            )

            return self._parent._cast(_4405.RollingRingAssemblyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.RollingRingParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4408,
            )

            return self._parent._cast(_4408.RootAssemblyParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.ShaftParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4412,
            )

            return self._parent._cast(_4412.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpiralBevelGearParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4415,
            )

            return self._parent._cast(_4415.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.SpringDamperHalfParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(_4418.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4421,
            )

            return self._parent._cast(_4421.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4424,
            )

            return self._parent._cast(_4424.StraightBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4427,
            )

            return self._parent._cast(_4427.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.SynchroniserParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.TorqueConverterParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.WormGearParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4439,
            )

            return self._parent._cast(_4439.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.ZerolBevelGearParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4442,
            )

            return self._parent._cast(_4442.ZerolBevelGearSetParametricStudyTool)

        @property
        def abstract_assembly_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(_4572.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573

            return self._parent._cast(_4573.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577

            return self._parent._cast(_4577.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4578

            return self._parent._cast(_4578.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579

            return self._parent._cast(_4579.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.BearingModalAnalysis)

        @property
        def belt_drive_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589

            return self._parent._cast(_4589.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4590

            return self._parent._cast(_4590.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4591

            return self._parent._cast(_4591.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592

            return self._parent._cast(_4592.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.ClutchModalAnalysis)

        @property
        def component_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.ConicalGearSetModalAnalysis)

        @property
        def connector_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4612

            return self._parent._cast(_4612.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621

            return self._parent._cast(_4621.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4622

            return self._parent._cast(_4622.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4628

            return self._parent._cast(_4628.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4637

            return self._parent._cast(_4637.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(_4640.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4644

            return self._parent._cast(
                _4644.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(
                _4648.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(
                _4650.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4651

            return self._parent._cast(
                _4651.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652

            return self._parent._cast(_4652.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(_4653.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.OilSealModalAnalysis)

        @property
        def part_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(_4665.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(_4669.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(_4671.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.RingPinsModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4677

            return self._parent._cast(_4677.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.ShaftModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4694

            return self._parent._cast(_4694.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4703

            return self._parent._cast(_4703.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4704

            return self._parent._cast(_4704.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4715

            return self._parent._cast(_4715.ZerolBevelGearSetModalAnalysis)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(_4857.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4858,
            )

            return self._parent._cast(_4858.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(
                _4859.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4862,
            )

            return self._parent._cast(
                _4862.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4863,
            )

            return self._parent._cast(
                _4863.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def assembly_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4864,
            )

            return self._parent._cast(_4864.AssemblyModalAnalysisAtAStiffness)

        @property
        def bearing_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4865,
            )

            return self._parent._cast(_4865.BearingModalAnalysisAtAStiffness)

        @property
        def belt_drive_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4867,
            )

            return self._parent._cast(_4867.BeltDriveModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4869,
            )

            return self._parent._cast(
                _4869.BevelDifferentialGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4870,
            )

            return self._parent._cast(
                _4870.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4871,
            )

            return self._parent._cast(
                _4871.BevelDifferentialPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4872,
            )

            return self._parent._cast(
                _4872.BevelDifferentialSunGearModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4874,
            )

            return self._parent._cast(_4874.BevelGearModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4875,
            )

            return self._parent._cast(_4875.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def bolted_joint_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4876,
            )

            return self._parent._cast(_4876.BoltedJointModalAnalysisAtAStiffness)

        @property
        def bolt_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4877,
            )

            return self._parent._cast(_4877.BoltModalAnalysisAtAStiffness)

        @property
        def clutch_half_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4879,
            )

            return self._parent._cast(_4879.ClutchHalfModalAnalysisAtAStiffness)

        @property
        def clutch_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(_4880.ClutchModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(_4882.ComponentModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4884,
            )

            return self._parent._cast(
                _4884.ConceptCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4885,
            )

            return self._parent._cast(_4885.ConceptCouplingModalAnalysisAtAStiffness)

        @property
        def concept_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4887,
            )

            return self._parent._cast(_4887.ConceptGearModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ConceptGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.ConicalGearModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def connector_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4893,
            )

            return self._parent._cast(_4893.ConnectorModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4895,
            )

            return self._parent._cast(_4895.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4896,
            )

            return self._parent._cast(_4896.CouplingModalAnalysisAtAStiffness)

        @property
        def cvt_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4898,
            )

            return self._parent._cast(_4898.CVTModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4899,
            )

            return self._parent._cast(_4899.CVTPulleyModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4900,
            )

            return self._parent._cast(_4900.CycloidalAssemblyModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4902,
            )

            return self._parent._cast(_4902.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.CylindricalGearModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(_4906.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4907,
            )

            return self._parent._cast(
                _4907.CylindricalPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def datum_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4908,
            )

            return self._parent._cast(_4908.DatumModalAnalysisAtAStiffness)

        @property
        def external_cad_model_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4910,
            )

            return self._parent._cast(_4910.ExternalCADModelModalAnalysisAtAStiffness)

        @property
        def face_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4912,
            )

            return self._parent._cast(_4912.FaceGearModalAnalysisAtAStiffness)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.FaceGearSetModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4914,
            )

            return self._parent._cast(_4914.FEPartModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4915,
            )

            return self._parent._cast(
                _4915.FlexiblePinAssemblyModalAnalysisAtAStiffness
            )

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.GearModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.GearSetModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4919,
            )

            return self._parent._cast(_4919.GuideDxfModelModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4921,
            )

            return self._parent._cast(_4921.HypoidGearModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(_4922.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(
                _4925.KlingelnbergCycloPalloidConicalGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4926,
            )

            return self._parent._cast(
                _4926.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4928,
            )

            return self._parent._cast(
                _4928.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4929,
            )

            return self._parent._cast(
                _4929.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4931,
            )

            return self._parent._cast(
                _4931.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(
                _4932.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4933,
            )

            return self._parent._cast(_4933.MassDiscModalAnalysisAtAStiffness)

        @property
        def measurement_component_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4934,
            )

            return self._parent._cast(
                _4934.MeasurementComponentModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(_4936.MountableComponentModalAnalysisAtAStiffness)

        @property
        def oil_seal_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.OilSealModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(
                _4940.PartToPartShearCouplingHalfModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4941,
            )

            return self._parent._cast(
                _4941.PartToPartShearCouplingModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4943,
            )

            return self._parent._cast(_4943.PlanetaryGearSetModalAnalysisAtAStiffness)

        @property
        def planet_carrier_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4944,
            )

            return self._parent._cast(_4944.PlanetCarrierModalAnalysisAtAStiffness)

        @property
        def point_load_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4945,
            )

            return self._parent._cast(_4945.PointLoadModalAnalysisAtAStiffness)

        @property
        def power_load_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4946,
            )

            return self._parent._cast(_4946.PowerLoadModalAnalysisAtAStiffness)

        @property
        def pulley_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4947,
            )

            return self._parent._cast(_4947.PulleyModalAnalysisAtAStiffness)

        @property
        def ring_pins_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4948,
            )

            return self._parent._cast(_4948.RingPinsModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4950,
            )

            return self._parent._cast(
                _4950.RollingRingAssemblyModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4952,
            )

            return self._parent._cast(_4952.RollingRingModalAnalysisAtAStiffness)

        @property
        def root_assembly_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4953,
            )

            return self._parent._cast(_4953.RootAssemblyModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4954,
            )

            return self._parent._cast(_4954.ShaftHubConnectionModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4955,
            )

            return self._parent._cast(_4955.ShaftModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(
                _4957.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.SpiralBevelGearModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4960,
            )

            return self._parent._cast(_4960.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def spring_damper_half_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4962,
            )

            return self._parent._cast(_4962.SpringDamperHalfModalAnalysisAtAStiffness)

        @property
        def spring_damper_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4963,
            )

            return self._parent._cast(_4963.SpringDamperModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4965,
            )

            return self._parent._cast(
                _4965.StraightBevelDiffGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(
                _4966.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4968,
            )

            return self._parent._cast(_4968.StraightBevelGearModalAnalysisAtAStiffness)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4969,
            )

            return self._parent._cast(
                _4969.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4970,
            )

            return self._parent._cast(
                _4970.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4971,
            )

            return self._parent._cast(
                _4971.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4972,
            )

            return self._parent._cast(_4972.SynchroniserHalfModalAnalysisAtAStiffness)

        @property
        def synchroniser_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4973,
            )

            return self._parent._cast(_4973.SynchroniserModalAnalysisAtAStiffness)

        @property
        def synchroniser_part_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4974,
            )

            return self._parent._cast(_4974.SynchroniserPartModalAnalysisAtAStiffness)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4975,
            )

            return self._parent._cast(_4975.SynchroniserSleeveModalAnalysisAtAStiffness)

        @property
        def torque_converter_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4977,
            )

            return self._parent._cast(_4977.TorqueConverterModalAnalysisAtAStiffness)

        @property
        def torque_converter_pump_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(
                _4978.TorqueConverterPumpModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4979,
            )

            return self._parent._cast(
                _4979.TorqueConverterTurbineModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4980,
            )

            return self._parent._cast(_4980.UnbalancedMassModalAnalysisAtAStiffness)

        @property
        def virtual_component_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4981,
            )

            return self._parent._cast(_4981.VirtualComponentModalAnalysisAtAStiffness)

        @property
        def worm_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4983,
            )

            return self._parent._cast(_4983.WormGearModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4984,
            )

            return self._parent._cast(_4984.WormGearSetModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4986,
            )

            return self._parent._cast(_4986.ZerolBevelGearModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4987,
            )

            return self._parent._cast(_4987.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(_5117.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_shaft_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5118,
            )

            return self._parent._cast(_5118.AbstractShaftModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(_5119.AbstractShaftOrHousingModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5122,
            )

            return self._parent._cast(_5122.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5123,
            )

            return self._parent._cast(
                _5123.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def assembly_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5124,
            )

            return self._parent._cast(_5124.AssemblyModalAnalysisAtASpeed)

        @property
        def bearing_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5125,
            )

            return self._parent._cast(_5125.BearingModalAnalysisAtASpeed)

        @property
        def belt_drive_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5127,
            )

            return self._parent._cast(_5127.BeltDriveModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5129,
            )

            return self._parent._cast(_5129.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5130,
            )

            return self._parent._cast(
                _5130.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5131,
            )

            return self._parent._cast(
                _5131.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5132,
            )

            return self._parent._cast(
                _5132.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5134,
            )

            return self._parent._cast(_5134.BevelGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5135,
            )

            return self._parent._cast(_5135.BevelGearSetModalAnalysisAtASpeed)

        @property
        def bolted_joint_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5136,
            )

            return self._parent._cast(_5136.BoltedJointModalAnalysisAtASpeed)

        @property
        def bolt_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5137,
            )

            return self._parent._cast(_5137.BoltModalAnalysisAtASpeed)

        @property
        def clutch_half_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5139,
            )

            return self._parent._cast(_5139.ClutchHalfModalAnalysisAtASpeed)

        @property
        def clutch_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(_5140.ClutchModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.ComponentModalAnalysisAtASpeed)

        @property
        def concept_coupling_half_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ConceptCouplingHalfModalAnalysisAtASpeed)

        @property
        def concept_coupling_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5145,
            )

            return self._parent._cast(_5145.ConceptCouplingModalAnalysisAtASpeed)

        @property
        def concept_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5147,
            )

            return self._parent._cast(_5147.ConceptGearModalAnalysisAtASpeed)

        @property
        def concept_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5148,
            )

            return self._parent._cast(_5148.ConceptGearSetModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def connector_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5153,
            )

            return self._parent._cast(_5153.ConnectorModalAnalysisAtASpeed)

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5155,
            )

            return self._parent._cast(_5155.CouplingHalfModalAnalysisAtASpeed)

        @property
        def coupling_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5156,
            )

            return self._parent._cast(_5156.CouplingModalAnalysisAtASpeed)

        @property
        def cvt_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5158,
            )

            return self._parent._cast(_5158.CVTModalAnalysisAtASpeed)

        @property
        def cvt_pulley_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5159,
            )

            return self._parent._cast(_5159.CVTPulleyModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5160,
            )

            return self._parent._cast(_5160.CycloidalAssemblyModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5162,
            )

            return self._parent._cast(_5162.CycloidalDiscModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5165,
            )

            return self._parent._cast(_5165.CylindricalGearModalAnalysisAtASpeed)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5166,
            )

            return self._parent._cast(_5166.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5167,
            )

            return self._parent._cast(_5167.CylindricalPlanetGearModalAnalysisAtASpeed)

        @property
        def datum_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5168,
            )

            return self._parent._cast(_5168.DatumModalAnalysisAtASpeed)

        @property
        def external_cad_model_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5169,
            )

            return self._parent._cast(_5169.ExternalCADModelModalAnalysisAtASpeed)

        @property
        def face_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5171,
            )

            return self._parent._cast(_5171.FaceGearModalAnalysisAtASpeed)

        @property
        def face_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5172,
            )

            return self._parent._cast(_5172.FaceGearSetModalAnalysisAtASpeed)

        @property
        def fe_part_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5173,
            )

            return self._parent._cast(_5173.FEPartModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5174,
            )

            return self._parent._cast(_5174.FlexiblePinAssemblyModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5176,
            )

            return self._parent._cast(_5176.GearModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.GearSetModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5178,
            )

            return self._parent._cast(_5178.GuideDxfModelModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5180,
            )

            return self._parent._cast(_5180.HypoidGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(_5181.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(
                _5184.KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5185,
            )

            return self._parent._cast(
                _5185.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5187,
            )

            return self._parent._cast(
                _5187.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(
                _5188.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5190,
            )

            return self._parent._cast(
                _5190.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5191,
            )

            return self._parent._cast(
                _5191.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
            )

        @property
        def mass_disc_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5192,
            )

            return self._parent._cast(_5192.MassDiscModalAnalysisAtASpeed)

        @property
        def measurement_component_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5193,
            )

            return self._parent._cast(_5193.MeasurementComponentModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(_5195.MountableComponentModalAnalysisAtASpeed)

        @property
        def oil_seal_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.OilSealModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(
                _5199.PartToPartShearCouplingHalfModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5200,
            )

            return self._parent._cast(
                _5200.PartToPartShearCouplingModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5202,
            )

            return self._parent._cast(_5202.PlanetaryGearSetModalAnalysisAtASpeed)

        @property
        def planet_carrier_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.PlanetCarrierModalAnalysisAtASpeed)

        @property
        def point_load_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5204,
            )

            return self._parent._cast(_5204.PointLoadModalAnalysisAtASpeed)

        @property
        def power_load_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PowerLoadModalAnalysisAtASpeed)

        @property
        def pulley_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5206,
            )

            return self._parent._cast(_5206.PulleyModalAnalysisAtASpeed)

        @property
        def ring_pins_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5207,
            )

            return self._parent._cast(_5207.RingPinsModalAnalysisAtASpeed)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5209,
            )

            return self._parent._cast(_5209.RollingRingAssemblyModalAnalysisAtASpeed)

        @property
        def rolling_ring_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5211,
            )

            return self._parent._cast(_5211.RollingRingModalAnalysisAtASpeed)

        @property
        def root_assembly_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5212,
            )

            return self._parent._cast(_5212.RootAssemblyModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5213,
            )

            return self._parent._cast(_5213.ShaftHubConnectionModalAnalysisAtASpeed)

        @property
        def shaft_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5214,
            )

            return self._parent._cast(_5214.ShaftModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5218,
            )

            return self._parent._cast(_5218.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(_5219.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def spring_damper_half_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5221,
            )

            return self._parent._cast(_5221.SpringDamperHalfModalAnalysisAtASpeed)

        @property
        def spring_damper_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5222,
            )

            return self._parent._cast(_5222.SpringDamperModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5224,
            )

            return self._parent._cast(_5224.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(
                _5225.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5227,
            )

            return self._parent._cast(_5227.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5229,
            )

            return self._parent._cast(
                _5229.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5230,
            )

            return self._parent._cast(_5230.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def synchroniser_half_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5231,
            )

            return self._parent._cast(_5231.SynchroniserHalfModalAnalysisAtASpeed)

        @property
        def synchroniser_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5232,
            )

            return self._parent._cast(_5232.SynchroniserModalAnalysisAtASpeed)

        @property
        def synchroniser_part_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5233,
            )

            return self._parent._cast(_5233.SynchroniserPartModalAnalysisAtASpeed)

        @property
        def synchroniser_sleeve_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5234,
            )

            return self._parent._cast(_5234.SynchroniserSleeveModalAnalysisAtASpeed)

        @property
        def torque_converter_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5236,
            )

            return self._parent._cast(_5236.TorqueConverterModalAnalysisAtASpeed)

        @property
        def torque_converter_pump_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(_5237.TorqueConverterPumpModalAnalysisAtASpeed)

        @property
        def torque_converter_turbine_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5238,
            )

            return self._parent._cast(_5238.TorqueConverterTurbineModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5239,
            )

            return self._parent._cast(_5239.UnbalancedMassModalAnalysisAtASpeed)

        @property
        def virtual_component_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5240,
            )

            return self._parent._cast(_5240.VirtualComponentModalAnalysisAtASpeed)

        @property
        def worm_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5242,
            )

            return self._parent._cast(_5242.WormGearModalAnalysisAtASpeed)

        @property
        def worm_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5243,
            )

            return self._parent._cast(_5243.WormGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5245,
            )

            return self._parent._cast(_5245.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5246,
            )

            return self._parent._cast(_5246.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5376

            return self._parent._cast(_5376.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5377

            return self._parent._cast(_5377.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(
                _5378.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381

            return self._parent._cast(
                _5381.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382

            return self._parent._cast(
                _5382.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def assembly_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.AssemblyMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5385

            return self._parent._cast(_5385.BearingMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5388

            return self._parent._cast(_5388.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(
                _5390.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(
                _5391.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(
                _5392.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(
                _5393.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395

            return self._parent._cast(_5395.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(_5398.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ClutchMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(_5404.ComponentMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(
                _5406.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(_5407.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(_5417.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.CVTMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427

            return self._parent._cast(_5427.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(
                _5429.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def datum_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(_5430.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(_5431.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.FaceGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434

            return self._parent._cast(_5434.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.FEPartMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(
                _5436.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5440

            return self._parent._cast(_5440.GearSetMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5443

            return self._parent._cast(_5443.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(_5444.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(
                _5454.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(
                _5455.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(
                _5457.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5458

            return self._parent._cast(
                _5458.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(_5459.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(
                _5463.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(_5467.PartMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(
                _5469.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(_5472.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(_5473.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474

            return self._parent._cast(_5474.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(_5476.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(_5477.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(
                _5479.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(_5481.RollingRingMultibodyDynamicsAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(_5482.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5485

            return self._parent._cast(_5485.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(_5486.ShaftMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(
                _5489.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(_5492.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(_5494.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(_5495.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(
                _5497.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(_5500.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(
                _5501.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5502

            return self._parent._cast(
                _5502.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(
                _5503.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(_5504.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(_5505.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(_5506.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(_5507.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(_5510.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(
                _5511.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5514

            return self._parent._cast(_5514.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(_5515.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5518

            return self._parent._cast(_5518.WormGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5521

            return self._parent._cast(_5521.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(_5522.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5678,
            )

            return self._parent._cast(_5678.AbstractAssemblyHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5680,
            )

            return self._parent._cast(_5680.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5681,
            )

            return self._parent._cast(_5681.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5683,
            )

            return self._parent._cast(_5683.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5685,
            )

            return self._parent._cast(_5685.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def assembly_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AssemblyHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.BearingHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(_5690.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5692,
            )

            return self._parent._cast(_5692.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5694,
            )

            return self._parent._cast(_5694.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BevelGearHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5698,
            )

            return self._parent._cast(_5698.BoltedJointHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5699,
            )

            return self._parent._cast(_5699.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.ClutchHalfHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5702,
            )

            return self._parent._cast(_5702.ClutchHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5705,
            )

            return self._parent._cast(_5705.ComponentHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5708,
            )

            return self._parent._cast(_5708.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ConceptGearHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConicalGearHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.ConicalGearSetHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.CouplingHalfHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5719,
            )

            return self._parent._cast(_5719.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.CVTHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5725,
            )

            return self._parent._cast(_5725.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.CylindricalGearSetHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5730,
            )

            return self._parent._cast(_5730.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(_5746.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5747,
            )

            return self._parent._cast(_5747.FaceGearHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.FaceGearSetHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5750,
            )

            return self._parent._cast(_5750.FEPartHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.GearHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5758,
            )

            return self._parent._cast(_5758.GearSetHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5760,
            )

            return self._parent._cast(_5760.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(_5771.HypoidGearHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(_5773.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5775,
            )

            return self._parent._cast(
                _5775.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(
                _5777.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5778,
            )

            return self._parent._cast(
                _5778.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(
                _5780.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(
                _5781.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(
                _5783.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.OilSealHarmonicAnalysis)

        @property
        def part_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.PartHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5791,
            )

            return self._parent._cast(_5791.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.PlanetaryGearSetHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(_5795.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5797,
            )

            return self._parent._cast(_5797.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(_5802.RollingRingAssemblyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(_5804.RollingRingHarmonicAnalysis)

        @property
        def root_assembly_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5805,
            )

            return self._parent._cast(_5805.RootAssemblyHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(_5807.ShaftHubConnectionHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5810,
            )

            return self._parent._cast(_5810.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.SpiralBevelGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.SpringDamperHalfHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.StraightBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5827,
            )

            return self._parent._cast(_5827.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.SynchroniserHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.TorqueConverterHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.WormGearHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5841,
            )

            return self._parent._cast(_5841.ZerolBevelGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6008,
            )

            return self._parent._cast(
                _6008.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6009,
            )

            return self._parent._cast(
                _6009.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6010,
            )

            return self._parent._cast(
                _6010.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(
                _6012.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(
                _6014.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6015,
            )

            return self._parent._cast(_6015.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6016,
            )

            return self._parent._cast(_6016.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(_6018.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6019,
            )

            return self._parent._cast(
                _6019.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(
                _6021.BevelDifferentialGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6022,
            )

            return self._parent._cast(
                _6022.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6023,
            )

            return self._parent._cast(
                _6023.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6024,
            )

            return self._parent._cast(_6024.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(
                _6026.BevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6027,
            )

            return self._parent._cast(
                _6027.BoltedJointHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6028,
            )

            return self._parent._cast(_6028.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(
                _6030.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6031,
            )

            return self._parent._cast(_6031.ClutchHarmonicAnalysisOfSingleExcitation)

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6033,
            )

            return self._parent._cast(_6033.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(
                _6035.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6036,
            )

            return self._parent._cast(
                _6036.ConceptCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(
                _6037.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConceptGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6040,
            )

            return self._parent._cast(
                _6040.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.ConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6044,
            )

            return self._parent._cast(_6044.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(
                _6046.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6047,
            )

            return self._parent._cast(_6047.CouplingHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6049,
            )

            return self._parent._cast(_6049.CVTHarmonicAnalysisOfSingleExcitation)

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6050,
            )

            return self._parent._cast(_6050.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_assembly_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6051,
            )

            return self._parent._cast(
                _6051.CycloidalAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6053,
            )

            return self._parent._cast(
                _6053.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(
                _6055.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(
                _6057.CylindricalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6058,
            )

            return self._parent._cast(
                _6058.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6059,
            )

            return self._parent._cast(_6059.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(
                _6060.ExternalCADModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(_6061.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def face_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(
                _6063.FaceGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6064,
            )

            return self._parent._cast(_6064.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def flexible_pin_assembly_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6065,
            )

            return self._parent._cast(
                _6065.FlexiblePinAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(_6066.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(_6068.GearSetHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(
                _6069.GuideDxfModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.HypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6075,
            )

            return self._parent._cast(
                _6075.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6078,
            )

            return self._parent._cast(
                _6078.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6081,
            )

            return self._parent._cast(
                _6081.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6084,
            )

            return self._parent._cast(_6084.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6085,
            )

            return self._parent._cast(
                _6085.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6088,
            )

            return self._parent._cast(_6088.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(_6089.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(
                _6091.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6092,
            )

            return self._parent._cast(
                _6092.PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6094,
            )

            return self._parent._cast(
                _6094.PlanetaryGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6095,
            )

            return self._parent._cast(
                _6095.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6096,
            )

            return self._parent._cast(_6096.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(_6097.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(_6098.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(_6099.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_assembly_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(
                _6101.RollingRingAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6103,
            )

            return self._parent._cast(
                _6103.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6104,
            )

            return self._parent._cast(
                _6104.RootAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(_6105.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6106,
            )

            return self._parent._cast(
                _6106.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6109,
            )

            return self._parent._cast(
                _6109.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.SpiralBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6113,
            )

            return self._parent._cast(
                _6113.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6114,
            )

            return self._parent._cast(
                _6114.SpringDamperHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(
                _6115.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelDiffGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6118,
            )

            return self._parent._cast(
                _6118.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6121,
            )

            return self._parent._cast(
                _6121.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6122,
            )

            return self._parent._cast(
                _6122.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(
                _6123.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.SynchroniserHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6126,
            )

            return self._parent._cast(
                _6126.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.TorqueConverterHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6129,
            )

            return self._parent._cast(
                _6129.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6130,
            )

            return self._parent._cast(
                _6130.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(_6133.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def worm_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(
                _6135.WormGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6136,
            )

            return self._parent._cast(
                _6136.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_harmonic_analysis_of_single_excitation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6138,
            )

            return self._parent._cast(
                _6138.ZerolBevelGearSetHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(_6277.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278

            return self._parent._cast(_6278.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281

            return self._parent._cast(_6281.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300

            return self._parent._cast(_6300.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327

            return self._parent._cast(_6327.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(_6341.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(_6343.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(
                _6345.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(
                _6348.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(
                _6350.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(
                _6351.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(
                _6353.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(_6372.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6407

            return self._parent._cast(_6407.ZerolBevelGearSetDynamicAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6543,
            )

            return self._parent._cast(_6543.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_shaft_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6544,
            )

            return self._parent._cast(_6544.AbstractShaftCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6545,
            )

            return self._parent._cast(_6545.AbstractShaftOrHousingCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6547,
            )

            return self._parent._cast(_6547.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6549,
            )

            return self._parent._cast(
                _6549.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def assembly_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6550,
            )

            return self._parent._cast(_6550.AssemblyCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6551,
            )

            return self._parent._cast(_6551.BearingCriticalSpeedAnalysis)

        @property
        def belt_drive_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6553,
            )

            return self._parent._cast(_6553.BeltDriveCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6554,
            )

            return self._parent._cast(_6554.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(
                _6556.BevelDifferentialGearSetCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(
                _6557.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6558,
            )

            return self._parent._cast(
                _6558.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6559,
            )

            return self._parent._cast(_6559.BevelGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6561,
            )

            return self._parent._cast(_6561.BevelGearSetCriticalSpeedAnalysis)

        @property
        def bolt_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6562,
            )

            return self._parent._cast(_6562.BoltCriticalSpeedAnalysis)

        @property
        def bolted_joint_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6563,
            )

            return self._parent._cast(_6563.BoltedJointCriticalSpeedAnalysis)

        @property
        def clutch_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(_6565.ClutchCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6566,
            )

            return self._parent._cast(_6566.ClutchHalfCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ComponentCriticalSpeedAnalysis)

        @property
        def concept_coupling_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ConceptCouplingCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6571,
            )

            return self._parent._cast(_6571.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6572,
            )

            return self._parent._cast(_6572.ConceptGearCriticalSpeedAnalysis)

        @property
        def concept_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConceptGearSetCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6575,
            )

            return self._parent._cast(_6575.ConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6579,
            )

            return self._parent._cast(_6579.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6581,
            )

            return self._parent._cast(_6581.CouplingCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6582,
            )

            return self._parent._cast(_6582.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6587,
            )

            return self._parent._cast(_6587.CVTCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6588,
            )

            return self._parent._cast(_6588.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6589,
            )

            return self._parent._cast(_6589.CycloidalAssemblyCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6591,
            )

            return self._parent._cast(_6591.CycloidalDiscCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6593,
            )

            return self._parent._cast(_6593.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6596,
            )

            return self._parent._cast(_6596.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def datum_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6597,
            )

            return self._parent._cast(_6597.DatumCriticalSpeedAnalysis)

        @property
        def external_cad_model_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.ExternalCADModelCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6599,
            )

            return self._parent._cast(_6599.FaceGearCriticalSpeedAnalysis)

        @property
        def face_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.FaceGearSetCriticalSpeedAnalysis)

        @property
        def fe_part_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.FEPartCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6603,
            )

            return self._parent._cast(_6603.FlexiblePinAssemblyCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.GearCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.GearSetCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(_6607.GuideDxfModelCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(_6608.HypoidGearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(_6610.HypoidGearSetCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6612,
            )

            return self._parent._cast(
                _6612.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6615,
            )

            return self._parent._cast(
                _6615.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(
                _6617.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6618,
            )

            return self._parent._cast(
                _6618.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(
                _6620.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
            )

        @property
        def mass_disc_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.MountableComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.OilSealCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(
                _6627.PartToPartShearCouplingCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6628,
            )

            return self._parent._cast(
                _6628.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(_6630.PlanetaryGearSetCriticalSpeedAnalysis)

        @property
        def planet_carrier_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6631,
            )

            return self._parent._cast(_6631.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6632,
            )

            return self._parent._cast(_6632.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(_6634.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(_6635.RingPinsCriticalSpeedAnalysis)

        @property
        def rolling_ring_assembly_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(_6637.RollingRingAssemblyCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6639,
            )

            return self._parent._cast(_6639.RollingRingCriticalSpeedAnalysis)

        @property
        def root_assembly_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(_6640.RootAssemblyCriticalSpeedAnalysis)

        @property
        def shaft_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(_6641.ShaftCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6642,
            )

            return self._parent._cast(_6642.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6645,
            )

            return self._parent._cast(_6645.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.SpiralBevelGearSetCriticalSpeedAnalysis)

        @property
        def spring_damper_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.SpringDamperCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6650,
            )

            return self._parent._cast(_6650.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(
                _6653.StraightBevelDiffGearSetCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(_6654.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.StraightBevelGearSetCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(
                _6657.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6658,
            )

            return self._parent._cast(_6658.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(_6659.SynchroniserCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(_6660.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6661,
            )

            return self._parent._cast(_6661.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.TorqueConverterCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6665,
            )

            return self._parent._cast(_6665.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6666,
            )

            return self._parent._cast(_6666.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6667,
            )

            return self._parent._cast(_6667.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6669,
            )

            return self._parent._cast(_6669.WormGearCriticalSpeedAnalysis)

        @property
        def worm_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6671,
            )

            return self._parent._cast(_6671.WormGearSetCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6672,
            )

            return self._parent._cast(_6672.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_set_critical_speed_analysis(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6674,
            )

            return self._parent._cast(_6674.ZerolBevelGearSetCriticalSpeedAnalysis)

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7007,
            )

            return self._parent._cast(
                _7007.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7008,
            )

            return self._parent._cast(
                _7008.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7014,
            )

            return self._parent._cast(
                _7014.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7016,
            )

            return self._parent._cast(
                _7016.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7017,
            )

            return self._parent._cast(
                _7017.AssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7019,
            )

            return self._parent._cast(
                _7019.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7021,
            )

            return self._parent._cast(
                _7021.BeltDriveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7022,
            )

            return self._parent._cast(
                _7022.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7024,
            )

            return self._parent._cast(
                _7024.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7025,
            )

            return self._parent._cast(
                _7025.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7026,
            )

            return self._parent._cast(
                _7026.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7029,
            )

            return self._parent._cast(
                _7029.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7030,
            )

            return self._parent._cast(
                _7030.BoltAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7031,
            )

            return self._parent._cast(
                _7031.BoltedJointAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7032,
            )

            return self._parent._cast(
                _7032.ClutchAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7034,
            )

            return self._parent._cast(
                _7034.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7037,
            )

            return self._parent._cast(
                _7037.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7039,
            )

            return self._parent._cast(
                _7039.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.ConceptGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7047,
            )

            return self._parent._cast(
                _7047.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.CouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7050,
            )

            return self._parent._cast(
                _7050.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7051,
            )

            return self._parent._cast(
                _7051.CVTAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7053,
            )

            return self._parent._cast(
                _7053.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7055,
            )

            return self._parent._cast(
                _7055.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7060,
            )

            return self._parent._cast(
                _7060.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7061,
            )

            return self._parent._cast(
                _7061.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7062,
            )

            return self._parent._cast(
                _7062.DatumAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7063,
            )

            return self._parent._cast(
                _7063.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7064,
            )

            return self._parent._cast(
                _7064.FaceGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7066,
            )

            return self._parent._cast(
                _7066.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7067,
            )

            return self._parent._cast(
                _7067.FEPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7068,
            )

            return self._parent._cast(
                _7068.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7071,
            )

            return self._parent._cast(
                _7071.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7074,
            )

            return self._parent._cast(
                _7074.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7078,
            )

            return self._parent._cast(
                _7078.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7080,
            )

            return self._parent._cast(
                _7080.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7081,
            )

            return self._parent._cast(
                _7081.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7083,
            )

            return self._parent._cast(
                _7083.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7084,
            )

            return self._parent._cast(
                _7084.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7094,
            )

            return self._parent._cast(
                _7094.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7096,
            )

            return self._parent._cast(
                _7096.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7098,
            )

            return self._parent._cast(
                _7098.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7101,
            )

            return self._parent._cast(
                _7101.RingPinsAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7104,
            )

            return self._parent._cast(
                _7104.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7106,
            )

            return self._parent._cast(
                _7106.RootAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7107,
            )

            return self._parent._cast(
                _7107.ShaftAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7108,
            )

            return self._parent._cast(
                _7108.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7111,
            )

            return self._parent._cast(
                _7111.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7114,
            )

            return self._parent._cast(
                _7114.SpringDamperAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7116,
            )

            return self._parent._cast(
                _7116.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7117,
            )

            return self._parent._cast(
                _7117.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7123,
            )

            return self._parent._cast(
                _7123.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7124,
            )

            return self._parent._cast(
                _7124.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.SynchroniserAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7126,
            )

            return self._parent._cast(
                _7126.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7127,
            )

            return self._parent._cast(
                _7127.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7128,
            )

            return self._parent._cast(
                _7128.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7131,
            )

            return self._parent._cast(
                _7131.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7135,
            )

            return self._parent._cast(
                _7135.WormGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7137,
            )

            return self._parent._cast(
                _7137.WormGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7138,
            )

            return self._parent._cast(
                _7138.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7140,
            )

            return self._parent._cast(
                _7140.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7270,
            )

            return self._parent._cast(_7270.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7271,
            )

            return self._parent._cast(_7271.AbstractShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7272,
            )

            return self._parent._cast(
                _7272.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7277,
            )

            return self._parent._cast(
                _7277.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7279,
            )

            return self._parent._cast(
                _7279.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def assembly_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7280,
            )

            return self._parent._cast(_7280.AssemblyAdvancedSystemDeflection)

        @property
        def bearing_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7281,
            )

            return self._parent._cast(_7281.BearingAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7283,
            )

            return self._parent._cast(_7283.BeltDriveAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(
                _7284.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7286,
            )

            return self._parent._cast(
                _7286.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(
                _7287.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7288,
            )

            return self._parent._cast(
                _7288.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7289,
            )

            return self._parent._cast(_7289.BevelGearAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7291,
            )

            return self._parent._cast(_7291.BevelGearSetAdvancedSystemDeflection)

        @property
        def bolt_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7292,
            )

            return self._parent._cast(_7292.BoltAdvancedSystemDeflection)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7293,
            )

            return self._parent._cast(_7293.BoltedJointAdvancedSystemDeflection)

        @property
        def clutch_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7294,
            )

            return self._parent._cast(_7294.ClutchAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.ClutchHalfAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def concept_coupling_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7299,
            )

            return self._parent._cast(_7299.ConceptCouplingAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7301,
            )

            return self._parent._cast(_7301.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.ConceptGearAdvancedSystemDeflection)

        @property
        def concept_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ConceptGearSetAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConicalGearAdvancedSystemDeflection)

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.ConicalGearSetAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7311,
            )

            return self._parent._cast(_7311.CouplingAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(_7314.CVTAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.CVTPulleyAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7317,
            )

            return self._parent._cast(_7317.CycloidalAssemblyAdvancedSystemDeflection)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7318,
            )

            return self._parent._cast(_7318.CycloidalDiscAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7321,
            )

            return self._parent._cast(_7321.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7323,
            )

            return self._parent._cast(_7323.CylindricalGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(
                _7325.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def datum_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(_7326.DatumAdvancedSystemDeflection)

        @property
        def external_cad_model_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(_7327.ExternalCADModelAdvancedSystemDeflection)

        @property
        def face_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.FaceGearAdvancedSystemDeflection)

        @property
        def face_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.FaceGearSetAdvancedSystemDeflection)

        @property
        def fe_part_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.FEPartAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.FlexiblePinAssemblyAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.GearAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7335,
            )

            return self._parent._cast(_7335.GearSetAdvancedSystemDeflection)

        @property
        def guide_dxf_model_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(_7336.GuideDxfModelAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(_7337.HypoidGearAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.HypoidGearSetAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7341,
            )

            return self._parent._cast(
                _7341.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7343,
            )

            return self._parent._cast(
                _7343.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(
                _7344.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7346,
            )

            return self._parent._cast(
                _7346.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(
                _7347.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7349,
            )

            return self._parent._cast(
                _7349.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(
                _7352.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def mountable_component_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.OilSealAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7356,
            )

            return self._parent._cast(
                _7356.PartToPartShearCouplingAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7358,
            )

            return self._parent._cast(
                _7358.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(_7360.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def planet_carrier_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(_7364.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7365,
            )

            return self._parent._cast(_7365.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7367,
            )

            return self._parent._cast(_7367.RollingRingAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(_7368.RollingRingAssemblyAdvancedSystemDeflection)

        @property
        def root_assembly_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(_7370.RootAssemblyAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(_7371.ShaftAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(_7374.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(_7375.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7377,
            )

            return self._parent._cast(_7377.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def spring_damper_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(_7378.SpringDamperAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(_7380.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(
                _7381.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(
                _7383.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(_7384.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7386,
            )

            return self._parent._cast(
                _7386.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(
                _7387.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(
                _7388.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7389,
            )

            return self._parent._cast(_7389.SynchroniserAdvancedSystemDeflection)

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(_7390.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(_7391.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7393,
            )

            return self._parent._cast(_7393.TorqueConverterAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(_7395.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(
                _7396.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(_7399.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.WormGearAdvancedSystemDeflection)

        @property
        def worm_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7402,
            )

            return self._parent._cast(_7402.WormGearSetAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(_7403.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7405,
            )

            return self._parent._cast(_7405.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def part_fe_analysis(self: "PartAnalysisCase._Cast_PartAnalysisCase"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_time_series_load_analysis_case(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartAnalysisCase._Cast_PartAnalysisCase",
        ) -> "PartAnalysisCase":
            return self._parent

        def __getattr__(self: "PartAnalysisCase._Cast_PartAnalysisCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartAnalysisCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def three_d_isometric_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDIsometricView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDView

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXyPlaneWithZAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInXzPlaneWithYAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_into_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingIntoTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_out_of_the_screen(
        self: Self,
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThreeDViewOrientatedInYzPlaneWithXAxisPointingOutOfTheScreen

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PartAnalysisCase._Cast_PartAnalysisCase":
        return self._Cast_PartAnalysisCase(self)

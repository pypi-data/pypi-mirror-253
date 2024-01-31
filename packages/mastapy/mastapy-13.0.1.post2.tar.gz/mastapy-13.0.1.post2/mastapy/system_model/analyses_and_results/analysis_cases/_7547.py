"""PartFEAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7548
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_FE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartFEAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("PartFEAnalysis",)


Self = TypeVar("Self", bound="PartFEAnalysis")


class PartFEAnalysis(_7548.PartStaticLoadAnalysisCase):
    """PartFEAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_FE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartFEAnalysis")

    class _Cast_PartFEAnalysis:
        """Special nested class for casting PartFEAnalysis to subclasses."""

        def __init__(
            self: "PartFEAnalysis._Cast_PartFEAnalysis", parent: "PartFEAnalysis"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(_2685.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2686,
            )

            return self._parent._cast(_2686.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2690,
            )

            return self._parent._cast(_2690.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2691,
            )

            return self._parent._cast(_2691.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2692,
            )

            return self._parent._cast(_2692.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2698,
            )

            return self._parent._cast(_2698.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2703,
            )

            return self._parent._cast(_2703.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.ClutchSystemDeflection)

        @property
        def component_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2718,
            )

            return self._parent._cast(_2718.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(
                _2744.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(_2746.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(
                _2747.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2751,
            )

            return self._parent._cast(_2751.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.GearSetSystemDeflection)

        @property
        def gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2769,
            )

            return self._parent._cast(
                _2769.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2776,
            )

            return self._parent._cast(
                _2776.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.OilSealSystemDeflection)

        @property
        def part_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(_2794.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(_2797.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2800,
            )

            return self._parent._cast(_2800.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6277

            return self._parent._cast(_6277.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278

            return self._parent._cast(_6278.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281

            return self._parent._cast(_6281.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6288

            return self._parent._cast(_6288.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6300

            return self._parent._cast(_6300.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6305

            return self._parent._cast(_6305.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(_6319.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327

            return self._parent._cast(_6327.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6331

            return self._parent._cast(_6331.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6332

            return self._parent._cast(_6332.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(_6340.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(_6341.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(_6343.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(
                _6345.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(
                _6348.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(
                _6350.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(
                _6351.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(
                _6353.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(_6355.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6361

            return self._parent._cast(_6361.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364

            return self._parent._cast(_6364.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(_6372.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6378

            return self._parent._cast(_6378.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6383

            return self._parent._cast(_6383.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6398

            return self._parent._cast(_6398.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(self: "PartFEAnalysis._Cast_PartFEAnalysis"):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6407

            return self._parent._cast(_6407.ZerolBevelGearSetDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "PartFEAnalysis":
            return self._parent

        def __getattr__(self: "PartFEAnalysis._Cast_PartFEAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartFEAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PartFEAnalysis._Cast_PartFEAnalysis":
        return self._Cast_PartFEAnalysis(self)

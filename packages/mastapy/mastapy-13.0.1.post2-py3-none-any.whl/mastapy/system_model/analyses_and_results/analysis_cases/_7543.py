"""DesignEntityCompoundAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.analyses_and_results import _2651
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY_COMPOUND_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "DesignEntityCompoundAnalysis",
)


__docformat__ = "restructuredtext en"
__all__ = ("DesignEntityCompoundAnalysis",)


Self = TypeVar("Self", bound="DesignEntityCompoundAnalysis")


class DesignEntityCompoundAnalysis(_2651.DesignEntityAnalysis):
    """DesignEntityCompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY_COMPOUND_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignEntityCompoundAnalysis")

    class _Cast_DesignEntityCompoundAnalysis:
        """Special nested class for casting DesignEntityCompoundAnalysis to subclasses."""

        def __init__(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
            parent: "DesignEntityCompoundAnalysis",
        ):
            self._parent = parent

        @property
        def design_entity_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2851,
            )

            return self._parent._cast(_2851.AbstractAssemblyCompoundSystemDeflection)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2852,
            )

            return self._parent._cast(_2852.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2853,
            )

            return self._parent._cast(
                _2853.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2854,
            )

            return self._parent._cast(
                _2854.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(
                _2855.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2856,
            )

            return self._parent._cast(
                _2856.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2857,
            )

            return self._parent._cast(
                _2857.AGMAGleasonConicalGearSetCompoundSystemDeflection
            )

        @property
        def assembly_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2858,
            )

            return self._parent._cast(_2858.AssemblyCompoundSystemDeflection)

        @property
        def bearing_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2859,
            )

            return self._parent._cast(_2859.BearingCompoundSystemDeflection)

        @property
        def belt_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2860,
            )

            return self._parent._cast(_2860.BeltConnectionCompoundSystemDeflection)

        @property
        def belt_drive_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(_2861.BeltDriveCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2862,
            )

            return self._parent._cast(
                _2862.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2863,
            )

            return self._parent._cast(
                _2863.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(
                _2864.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2865,
            )

            return self._parent._cast(
                _2865.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2866,
            )

            return self._parent._cast(
                _2866.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(_2867.BevelGearCompoundSystemDeflection)

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2868,
            )

            return self._parent._cast(_2868.BevelGearMeshCompoundSystemDeflection)

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.BevelGearSetCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2870,
            )

            return self._parent._cast(_2870.BoltCompoundSystemDeflection)

        @property
        def bolted_joint_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2871,
            )

            return self._parent._cast(_2871.BoltedJointCompoundSystemDeflection)

        @property
        def clutch_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(_2872.ClutchCompoundSystemDeflection)

        @property
        def clutch_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ClutchConnectionCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.ClutchHalfCompoundSystemDeflection)

        @property
        def coaxial_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(_2875.CoaxialConnectionCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.ComponentCompoundSystemDeflection)

        @property
        def concept_coupling_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(_2877.ConceptCouplingCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(
                _2878.ConceptCouplingConnectionCompoundSystemDeflection
            )

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(_2879.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2880,
            )

            return self._parent._cast(_2880.ConceptGearCompoundSystemDeflection)

        @property
        def concept_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.ConceptGearMeshCompoundSystemDeflection)

        @property
        def concept_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ConceptGearSetCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(_2883.ConicalGearCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ConicalGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(_2885.ConicalGearSetCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(_2886.ConnectionCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.ConnectorCompoundSystemDeflection)

        @property
        def coupling_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.CouplingCompoundSystemDeflection)

        @property
        def coupling_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.CouplingConnectionCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_belt_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.CVTBeltConnectionCompoundSystemDeflection)

        @property
        def cvt_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.CVTCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_assembly_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.CycloidalAssemblyCompoundSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(
                _2895.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
            )

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2896,
            )

            return self._parent._cast(_2896.CycloidalDiscCompoundSystemDeflection)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(
                _2897.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
            )

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(_2898.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(_2899.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def cylindrical_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.CylindricalGearSetCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2901,
            )

            return self._parent._cast(
                _2901.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def datum_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2902,
            )

            return self._parent._cast(_2902.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2905,
            )

            return self._parent._cast(_2905.FaceGearCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.FaceGearMeshCompoundSystemDeflection)

        @property
        def face_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.FaceGearSetCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.FEPartCompoundSystemDeflection)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.FlexiblePinAssemblyCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.GearCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2911,
            )

            return self._parent._cast(_2911.GearMeshCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2912,
            )

            return self._parent._cast(_2912.GearSetCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2914,
            )

            return self._parent._cast(_2914.HypoidGearCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(_2915.HypoidGearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(_2916.HypoidGearSetCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2917,
            )

            return self._parent._cast(
                _2917.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(
                _2918.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(
                _2919.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(
                _2920.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2921,
            )

            return self._parent._cast(
                _2921.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(
                _2922.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(
                _2923.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2924,
            )

            return self._parent._cast(
                _2924.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(
                _2925.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(
                _2926.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2927,
            )

            return self._parent._cast(_2927.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(
                _2928.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def mountable_component_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(_2930.OilSealCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.PartCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(
                _2932.PartToPartShearCouplingCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(
                _2933.PartToPartShearCouplingConnectionCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(
                _2934.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planetary_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.PlanetaryConnectionCompoundSystemDeflection)

        @property
        def planetary_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(_2936.PlanetaryGearSetCompoundSystemDeflection)

        @property
        def planet_carrier_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2937,
            )

            return self._parent._cast(_2937.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(_2938.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(_2940.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(_2941.RingPinsCompoundSystemDeflection)

        @property
        def ring_pins_to_disc_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(
                _2942.RingPinsToDiscConnectionCompoundSystemDeflection
            )

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(_2943.RollingRingAssemblyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2944,
            )

            return self._parent._cast(_2944.RollingRingCompoundSystemDeflection)

        @property
        def rolling_ring_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2945,
            )

            return self._parent._cast(
                _2945.RollingRingConnectionCompoundSystemDeflection
            )

        @property
        def root_assembly_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(_2946.RootAssemblyCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2947,
            )

            return self._parent._cast(_2947.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(
                _2950.ShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def specialised_assembly_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2953,
            )

            return self._parent._cast(_2953.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def spring_damper_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(_2955.SpringDamperCompoundSystemDeflection)

        @property
        def spring_damper_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2956,
            )

            return self._parent._cast(
                _2956.SpringDamperConnectionCompoundSystemDeflection
            )

        @property
        def spring_damper_half_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2957,
            )

            return self._parent._cast(_2957.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2958,
            )

            return self._parent._cast(
                _2958.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(
                _2959.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(
                _2960.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(_2961.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(
                _2962.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(
                _2963.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2964,
            )

            return self._parent._cast(
                _2964.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(
                _2965.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(_2966.SynchroniserCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(_2967.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(_2968.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(_2970.TorqueConverterCompoundSystemDeflection)

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(
                _2971.TorqueConverterConnectionCompoundSystemDeflection
            )

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2972,
            )

            return self._parent._cast(_2972.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2973,
            )

            return self._parent._cast(
                _2973.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.WormGearCompoundSystemDeflection)

        @property
        def worm_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.WormGearMeshCompoundSystemDeflection)

        @property
        def worm_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.WormGearSetCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2979,
            )

            return self._parent._cast(_2979.ZerolBevelGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(_2980.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2981,
            )

            return self._parent._cast(_2981.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3116,
            )

            return self._parent._cast(
                _3116.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3117,
            )

            return self._parent._cast(
                _3117.AbstractShaftCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3118,
            )

            return self._parent._cast(
                _3118.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3119,
            )

            return self._parent._cast(
                _3119.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3120,
            )

            return self._parent._cast(
                _3120.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3121,
            )

            return self._parent._cast(
                _3121.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3122,
            )

            return self._parent._cast(
                _3122.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def assembly_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3123,
            )

            return self._parent._cast(
                _3123.AssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def bearing_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.BearingCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3125,
            )

            return self._parent._cast(
                _3125.BeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3126,
            )

            return self._parent._cast(
                _3126.BeltDriveCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3127,
            )

            return self._parent._cast(
                _3127.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3128,
            )

            return self._parent._cast(
                _3128.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3129,
            )

            return self._parent._cast(
                _3129.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3130,
            )

            return self._parent._cast(
                _3130.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3131,
            )

            return self._parent._cast(
                _3131.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3132,
            )

            return self._parent._cast(
                _3132.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3133,
            )

            return self._parent._cast(
                _3133.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3134,
            )

            return self._parent._cast(
                _3134.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolt_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3135,
            )

            return self._parent._cast(_3135.BoltCompoundSteadyStateSynchronousResponse)

        @property
        def bolted_joint_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3136,
            )

            return self._parent._cast(
                _3136.BoltedJointCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3137,
            )

            return self._parent._cast(
                _3137.ClutchCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3138,
            )

            return self._parent._cast(
                _3138.ClutchConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.ClutchHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3140,
            )

            return self._parent._cast(
                _3140.CoaxialConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3142,
            )

            return self._parent._cast(
                _3142.ConceptCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(
                _3143.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3145,
            )

            return self._parent._cast(
                _3145.ConceptGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3146,
            )

            return self._parent._cast(
                _3146.ConceptGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.ConceptGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3150,
            )

            return self._parent._cast(
                _3150.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connector_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.ConnectorCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(
                _3154.CouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3155,
            )

            return self._parent._cast(
                _3155.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3156,
            )

            return self._parent._cast(
                _3156.CVTBeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3157,
            )

            return self._parent._cast(_3157.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(
                _3158.CVTPulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(
                _3159.CycloidalAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3160,
            )

            return self._parent._cast(
                _3160.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3161,
            )

            return self._parent._cast(
                _3161.CycloidalDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3163,
            )

            return self._parent._cast(
                _3163.CylindricalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3164,
            )

            return self._parent._cast(
                _3164.CylindricalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3165,
            )

            return self._parent._cast(
                _3165.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3166,
            )

            return self._parent._cast(
                _3166.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def datum_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3167,
            )

            return self._parent._cast(_3167.DatumCompoundSteadyStateSynchronousResponse)

        @property
        def external_cad_model_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.ExternalCADModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3169,
            )

            return self._parent._cast(
                _3169.FaceGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3170,
            )

            return self._parent._cast(
                _3170.FaceGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(
                _3171.FaceGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def fe_part_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.FEPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3174,
            )

            return self._parent._cast(_3174.GearCompoundSteadyStateSynchronousResponse)

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3175,
            )

            return self._parent._cast(
                _3175.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3176,
            )

            return self._parent._cast(
                _3176.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.GuideDxfModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3178,
            )

            return self._parent._cast(
                _3178.HypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3179,
            )

            return self._parent._cast(
                _3179.HypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3180,
            )

            return self._parent._cast(
                _3180.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3182,
            )

            return self._parent._cast(
                _3182.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3185,
            )

            return self._parent._cast(
                _3185.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3186,
            )

            return self._parent._cast(
                _3186.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3187,
            )

            return self._parent._cast(
                _3187.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3188,
            )

            return self._parent._cast(
                _3188.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3189,
            )

            return self._parent._cast(
                _3189.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(
                _3190.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.MassDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(
                _3192.MeasurementComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3194,
            )

            return self._parent._cast(
                _3194.OilSealCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(_3195.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3196,
            )

            return self._parent._cast(
                _3196.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(
                _3197.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3199,
            )

            return self._parent._cast(
                _3199.PlanetaryConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3200,
            )

            return self._parent._cast(
                _3200.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3201,
            )

            return self._parent._cast(
                _3201.PlanetCarrierCompoundSteadyStateSynchronousResponse
            )

        @property
        def point_load_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.PointLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def power_load_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(
                _3203.PowerLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def pulley_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3204,
            )

            return self._parent._cast(
                _3204.PulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3205,
            )

            return self._parent._cast(
                _3205.RingPinsCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3206,
            )

            return self._parent._cast(
                _3206.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3207,
            )

            return self._parent._cast(
                _3207.RollingRingAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3208,
            )

            return self._parent._cast(
                _3208.RollingRingCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3209,
            )

            return self._parent._cast(
                _3209.RollingRingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3210,
            )

            return self._parent._cast(
                _3210.RootAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(_3211.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.ShaftHubConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3213,
            )

            return self._parent._cast(
                _3213.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3215,
            )

            return self._parent._cast(
                _3215.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3217,
            )

            return self._parent._cast(
                _3217.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(
                _3218.SpringDamperCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3219,
            )

            return self._parent._cast(
                _3219.SpringDamperConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.SpringDamperHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3221,
            )

            return self._parent._cast(
                _3221.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3222,
            )

            return self._parent._cast(
                _3222.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3224,
            )

            return self._parent._cast(
                _3224.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3227,
            )

            return self._parent._cast(
                _3227.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3228,
            )

            return self._parent._cast(
                _3228.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3229,
            )

            return self._parent._cast(
                _3229.SynchroniserCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3230,
            )

            return self._parent._cast(
                _3230.SynchroniserHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3231,
            )

            return self._parent._cast(
                _3231.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3232,
            )

            return self._parent._cast(
                _3232.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3233,
            )

            return self._parent._cast(
                _3233.TorqueConverterCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(
                _3234.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3235,
            )

            return self._parent._cast(
                _3235.TorqueConverterPumpCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3236,
            )

            return self._parent._cast(
                _3236.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3237,
            )

            return self._parent._cast(
                _3237.UnbalancedMassCompoundSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.WormGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3240,
            )

            return self._parent._cast(
                _3240.WormGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.WormGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3242,
            )

            return self._parent._cast(
                _3242.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3243,
            )

            return self._parent._cast(
                _3243.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3244,
            )

            return self._parent._cast(
                _3244.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3375,
            )

            return self._parent._cast(
                _3375.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3376,
            )

            return self._parent._cast(
                _3376.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3377,
            )

            return self._parent._cast(
                _3377.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3378,
            )

            return self._parent._cast(
                _3378.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3379,
            )

            return self._parent._cast(
                _3379.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3380,
            )

            return self._parent._cast(
                _3380.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3381,
            )

            return self._parent._cast(
                _3381.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3382,
            )

            return self._parent._cast(
                _3382.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3383,
            )

            return self._parent._cast(
                _3383.BearingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3384,
            )

            return self._parent._cast(
                _3384.BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3385,
            )

            return self._parent._cast(
                _3385.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3386,
            )

            return self._parent._cast(
                _3386.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3387,
            )

            return self._parent._cast(
                _3387.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3388,
            )

            return self._parent._cast(
                _3388.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3389,
            )

            return self._parent._cast(
                _3389.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3390,
            )

            return self._parent._cast(
                _3390.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3391,
            )

            return self._parent._cast(
                _3391.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3392,
            )

            return self._parent._cast(
                _3392.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3393,
            )

            return self._parent._cast(
                _3393.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3394,
            )

            return self._parent._cast(
                _3394.BoltCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3395,
            )

            return self._parent._cast(
                _3395.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3396,
            )

            return self._parent._cast(
                _3396.ClutchCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3397,
            )

            return self._parent._cast(
                _3397.ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3399,
            )

            return self._parent._cast(
                _3399.CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3400,
            )

            return self._parent._cast(
                _3400.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3401,
            )

            return self._parent._cast(
                _3401.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3402,
            )

            return self._parent._cast(
                _3402.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3403,
            )

            return self._parent._cast(
                _3403.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3404,
            )

            return self._parent._cast(
                _3404.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3405,
            )

            return self._parent._cast(
                _3405.ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3407,
            )

            return self._parent._cast(
                _3407.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3409,
            )

            return self._parent._cast(
                _3409.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3410,
            )

            return self._parent._cast(
                _3410.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3412,
            )

            return self._parent._cast(
                _3412.CouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3414,
            )

            return self._parent._cast(
                _3414.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3415,
            )

            return self._parent._cast(
                _3415.CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3416,
            )

            return self._parent._cast(
                _3416.CVTCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3417,
            )

            return self._parent._cast(
                _3417.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3418,
            )

            return self._parent._cast(
                _3418.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3420,
            )

            return self._parent._cast(
                _3420.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3421,
            )

            return self._parent._cast(
                _3421.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3422,
            )

            return self._parent._cast(
                _3422.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3424,
            )

            return self._parent._cast(
                _3424.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3425,
            )

            return self._parent._cast(
                _3425.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def datum_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3426,
            )

            return self._parent._cast(
                _3426.DatumCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3427,
            )

            return self._parent._cast(
                _3427.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3428,
            )

            return self._parent._cast(
                _3428.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3429,
            )

            return self._parent._cast(
                _3429.FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3430,
            )

            return self._parent._cast(
                _3430.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3431,
            )

            return self._parent._cast(
                _3431.FEPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3435,
            )

            return self._parent._cast(
                _3435.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3436,
            )

            return self._parent._cast(
                _3436.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3437,
            )

            return self._parent._cast(
                _3437.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3438,
            )

            return self._parent._cast(
                _3438.HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3439,
            )

            return self._parent._cast(
                _3439.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3442,
            )

            return self._parent._cast(
                _3442.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3443,
            )

            return self._parent._cast(
                _3443.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3444,
            )

            return self._parent._cast(
                _3444.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3445,
            )

            return self._parent._cast(
                _3445.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3446,
            )

            return self._parent._cast(
                _3446.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3447,
            )

            return self._parent._cast(
                _3447.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3448,
            )

            return self._parent._cast(
                _3448.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3449,
            )

            return self._parent._cast(
                _3449.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3450,
            )

            return self._parent._cast(
                _3450.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3451,
            )

            return self._parent._cast(
                _3451.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3452,
            )

            return self._parent._cast(
                _3452.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3453,
            )

            return self._parent._cast(
                _3453.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3457,
            )

            return self._parent._cast(
                _3457.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3458,
            )

            return self._parent._cast(
                _3458.PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3461,
            )

            return self._parent._cast(
                _3461.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3464,
            )

            return self._parent._cast(
                _3464.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3465,
            )

            return self._parent._cast(
                _3465.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3467,
            )

            return self._parent._cast(
                _3467.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3468,
            )

            return self._parent._cast(
                _3468.RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3470,
            )

            return self._parent._cast(
                _3470.ShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3471,
            )

            return self._parent._cast(
                _3471.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3472,
            )

            return self._parent._cast(
                _3472.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3474,
            )

            return self._parent._cast(
                _3474.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3476,
            )

            return self._parent._cast(
                _3476.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3478,
            )

            return self._parent._cast(
                _3478.SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3479,
            )

            return self._parent._cast(
                _3479.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3480,
            )

            return self._parent._cast(
                _3480.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3481,
            )

            return self._parent._cast(
                _3481.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3483,
            )

            return self._parent._cast(
                _3483.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3484,
            )

            return self._parent._cast(
                _3484.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3485,
            )

            return self._parent._cast(
                _3485.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3486,
            )

            return self._parent._cast(
                _3486.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3487,
            )

            return self._parent._cast(
                _3487.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3488,
            )

            return self._parent._cast(
                _3488.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3489,
            )

            return self._parent._cast(
                _3489.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3490,
            )

            return self._parent._cast(
                _3490.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3491,
            )

            return self._parent._cast(
                _3491.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3492,
            )

            return self._parent._cast(
                _3492.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3493,
            )

            return self._parent._cast(
                _3493.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3495,
            )

            return self._parent._cast(
                _3495.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3498,
            )

            return self._parent._cast(
                _3498.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3499,
            )

            return self._parent._cast(
                _3499.WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3500,
            )

            return self._parent._cast(
                _3500.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3501,
            )

            return self._parent._cast(
                _3501.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3503,
            )

            return self._parent._cast(
                _3503.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3634,
            )

            return self._parent._cast(
                _3634.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3635,
            )

            return self._parent._cast(
                _3635.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3636,
            )

            return self._parent._cast(
                _3636.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3637,
            )

            return self._parent._cast(
                _3637.AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3638,
            )

            return self._parent._cast(
                _3638.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3639,
            )

            return self._parent._cast(
                _3639.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3640,
            )

            return self._parent._cast(
                _3640.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3641,
            )

            return self._parent._cast(
                _3641.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3642,
            )

            return self._parent._cast(
                _3642.BearingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3643,
            )

            return self._parent._cast(
                _3643.BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3644,
            )

            return self._parent._cast(
                _3644.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3645,
            )

            return self._parent._cast(
                _3645.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3646,
            )

            return self._parent._cast(
                _3646.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3647,
            )

            return self._parent._cast(
                _3647.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3648,
            )

            return self._parent._cast(
                _3648.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3649,
            )

            return self._parent._cast(
                _3649.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3650,
            )

            return self._parent._cast(
                _3650.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3651,
            )

            return self._parent._cast(
                _3651.BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3652,
            )

            return self._parent._cast(
                _3652.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3653,
            )

            return self._parent._cast(
                _3653.BoltCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3654,
            )

            return self._parent._cast(
                _3654.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3655,
            )

            return self._parent._cast(
                _3655.ClutchCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3656,
            )

            return self._parent._cast(
                _3656.ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coaxial_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3658,
            )

            return self._parent._cast(
                _3658.CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3659,
            )

            return self._parent._cast(
                _3659.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3660,
            )

            return self._parent._cast(
                _3660.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3661,
            )

            return self._parent._cast(
                _3661.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3662,
            )

            return self._parent._cast(
                _3662.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3663,
            )

            return self._parent._cast(
                _3663.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3664,
            )

            return self._parent._cast(
                _3664.ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3665,
            )

            return self._parent._cast(
                _3665.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3666,
            )

            return self._parent._cast(
                _3666.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3668,
            )

            return self._parent._cast(
                _3668.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3669,
            )

            return self._parent._cast(
                _3669.ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3670,
            )

            return self._parent._cast(
                _3670.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3671,
            )

            return self._parent._cast(
                _3671.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3672,
            )

            return self._parent._cast(
                _3672.CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3673,
            )

            return self._parent._cast(
                _3673.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3674,
            )

            return self._parent._cast(
                _3674.CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3675,
            )

            return self._parent._cast(
                _3675.CVTCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3676,
            )

            return self._parent._cast(
                _3676.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3678,
            )

            return self._parent._cast(
                _3678.CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3679,
            )

            return self._parent._cast(
                _3679.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3680,
            )

            return self._parent._cast(
                _3680.CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3681,
            )

            return self._parent._cast(
                _3681.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3682,
            )

            return self._parent._cast(
                _3682.CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3683,
            )

            return self._parent._cast(
                _3683.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3684,
            )

            return self._parent._cast(
                _3684.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3685,
            )

            return self._parent._cast(
                _3685.DatumCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3686,
            )

            return self._parent._cast(
                _3686.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3687,
            )

            return self._parent._cast(
                _3687.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3688,
            )

            return self._parent._cast(
                _3688.FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3689,
            )

            return self._parent._cast(
                _3689.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3690,
            )

            return self._parent._cast(
                _3690.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3692,
            )

            return self._parent._cast(
                _3692.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3693,
            )

            return self._parent._cast(
                _3693.GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3694,
            )

            return self._parent._cast(
                _3694.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3695,
            )

            return self._parent._cast(
                _3695.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3696,
            )

            return self._parent._cast(
                _3696.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3697,
            )

            return self._parent._cast(
                _3697.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3698,
            )

            return self._parent._cast(
                _3698.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3699,
            )

            return self._parent._cast(
                _3699.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3700,
            )

            return self._parent._cast(
                _3700.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3701,
            )

            return self._parent._cast(
                _3701.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3702,
            )

            return self._parent._cast(
                _3702.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3703,
            )

            return self._parent._cast(
                _3703.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3704,
            )

            return self._parent._cast(
                _3704.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3705,
            )

            return self._parent._cast(
                _3705.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3706,
            )

            return self._parent._cast(
                _3706.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3707,
            )

            return self._parent._cast(
                _3707.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3708,
            )

            return self._parent._cast(
                _3708.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3709,
            )

            return self._parent._cast(
                _3709.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3710,
            )

            return self._parent._cast(
                _3710.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3711,
            )

            return self._parent._cast(
                _3711.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3712,
            )

            return self._parent._cast(
                _3712.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3716,
            )

            return self._parent._cast(
                _3716.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3717,
            )

            return self._parent._cast(
                _3717.PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3718,
            )

            return self._parent._cast(
                _3718.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3719,
            )

            return self._parent._cast(
                _3719.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3720,
            )

            return self._parent._cast(
                _3720.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3722,
            )

            return self._parent._cast(
                _3722.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3723,
            )

            return self._parent._cast(
                _3723.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3724,
            )

            return self._parent._cast(
                _3724.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3725,
            )

            return self._parent._cast(
                _3725.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3726,
            )

            return self._parent._cast(
                _3726.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3727,
            )

            return self._parent._cast(
                _3727.RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3728,
            )

            return self._parent._cast(
                _3728.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3729,
            )

            return self._parent._cast(
                _3729.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3730,
            )

            return self._parent._cast(
                _3730.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3731,
            )

            return self._parent._cast(
                _3731.ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3732,
            )

            return self._parent._cast(
                _3732.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3733,
            )

            return self._parent._cast(
                _3733.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3734,
            )

            return self._parent._cast(
                _3734.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3735,
            )

            return self._parent._cast(
                _3735.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3737,
            )

            return self._parent._cast(
                _3737.SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3738,
            )

            return self._parent._cast(
                _3738.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3739,
            )

            return self._parent._cast(
                _3739.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3740,
            )

            return self._parent._cast(
                _3740.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3741,
            )

            return self._parent._cast(
                _3741.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3742,
            )

            return self._parent._cast(
                _3742.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3743,
            )

            return self._parent._cast(
                _3743.StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3744,
            )

            return self._parent._cast(
                _3744.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3745,
            )

            return self._parent._cast(
                _3745.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3746,
            )

            return self._parent._cast(
                _3746.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3747,
            )

            return self._parent._cast(
                _3747.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3748,
            )

            return self._parent._cast(
                _3748.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3749,
            )

            return self._parent._cast(
                _3749.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3750,
            )

            return self._parent._cast(
                _3750.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3751,
            )

            return self._parent._cast(
                _3751.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3752,
            )

            return self._parent._cast(
                _3752.TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3753,
            )

            return self._parent._cast(
                _3753.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3754,
            )

            return self._parent._cast(
                _3754.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3756,
            )

            return self._parent._cast(
                _3756.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3757,
            )

            return self._parent._cast(
                _3757.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3758,
            )

            return self._parent._cast(
                _3758.WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3759,
            )

            return self._parent._cast(
                _3759.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3760,
            )

            return self._parent._cast(
                _3760.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3761,
            )

            return self._parent._cast(
                _3761.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3762,
            )

            return self._parent._cast(
                _3762.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3897,
            )

            return self._parent._cast(_3897.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def abstract_shaft_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3898,
            )

            return self._parent._cast(_3898.AbstractShaftCompoundStabilityAnalysis)

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3899,
            )

            return self._parent._cast(
                _3899.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3900,
            )

            return self._parent._cast(
                _3900.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3901,
            )

            return self._parent._cast(
                _3901.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3902,
            )

            return self._parent._cast(
                _3902.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3903,
            )

            return self._parent._cast(
                _3903.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def assembly_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3904,
            )

            return self._parent._cast(_3904.AssemblyCompoundStabilityAnalysis)

        @property
        def bearing_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3905,
            )

            return self._parent._cast(_3905.BearingCompoundStabilityAnalysis)

        @property
        def belt_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(_3906.BeltConnectionCompoundStabilityAnalysis)

        @property
        def belt_drive_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3907,
            )

            return self._parent._cast(_3907.BeltDriveCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3908,
            )

            return self._parent._cast(
                _3908.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3909,
            )

            return self._parent._cast(
                _3909.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(
                _3910.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(
                _3911.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3912,
            )

            return self._parent._cast(
                _3912.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3913,
            )

            return self._parent._cast(_3913.BevelGearCompoundStabilityAnalysis)

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3914,
            )

            return self._parent._cast(_3914.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.BevelGearSetCompoundStabilityAnalysis)

        @property
        def bolt_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3916,
            )

            return self._parent._cast(_3916.BoltCompoundStabilityAnalysis)

        @property
        def bolted_joint_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3917,
            )

            return self._parent._cast(_3917.BoltedJointCompoundStabilityAnalysis)

        @property
        def clutch_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3918,
            )

            return self._parent._cast(_3918.ClutchCompoundStabilityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3919,
            )

            return self._parent._cast(_3919.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.ClutchHalfCompoundStabilityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3921,
            )

            return self._parent._cast(_3921.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(_3922.ComponentCompoundStabilityAnalysis)

        @property
        def concept_coupling_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(_3923.ConceptCouplingCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(
                _3924.ConceptCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(
                _3925.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(_3926.ConceptGearCompoundStabilityAnalysis)

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def concept_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.ConceptGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.ConicalGearCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3930,
            )

            return self._parent._cast(_3930.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(_3932.ConnectionCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(_3933.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(_3934.CouplingCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(_3935.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def cvt_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(_3938.CVTCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3939,
            )

            return self._parent._cast(_3939.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cycloidal_assembly_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.CycloidalAssemblyCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3941,
            )

            return self._parent._cast(
                _3941.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cycloidal_disc_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.CycloidalDiscCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(
                _3943.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(_3944.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(
                _3945.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3946,
            )

            return self._parent._cast(_3946.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3947,
            )

            return self._parent._cast(
                _3947.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def datum_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.DatumCompoundStabilityAnalysis)

        @property
        def external_cad_model_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(_3949.ExternalCADModelCompoundStabilityAnalysis)

        @property
        def face_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.FaceGearCompoundStabilityAnalysis)

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3951,
            )

            return self._parent._cast(_3951.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def face_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.FaceGearSetCompoundStabilityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.FEPartCompoundStabilityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(
                _3954.FlexiblePinAssemblyCompoundStabilityAnalysis
            )

        @property
        def gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3955,
            )

            return self._parent._cast(_3955.GearCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.GearMeshCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.GearSetCompoundStabilityAnalysis)

        @property
        def guide_dxf_model_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.GuideDxfModelCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(_3959.HypoidGearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(_3960.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3961,
            )

            return self._parent._cast(_3961.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(
                _3962.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3963,
            )

            return self._parent._cast(
                _3963.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3965,
            )

            return self._parent._cast(
                _3965.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3969,
            )

            return self._parent._cast(
                _3969.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3971,
            )

            return self._parent._cast(
                _3971.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3972,
            )

            return self._parent._cast(_3972.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(
                _3973.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def mountable_component_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.MountableComponentCompoundStabilityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3975,
            )

            return self._parent._cast(_3975.OilSealCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3977,
            )

            return self._parent._cast(
                _3977.PartToPartShearCouplingCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(
                _3978.PartToPartShearCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(
                _3979.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planetary_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(
                _3980.PlanetaryConnectionCompoundStabilityAnalysis
            )

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3981,
            )

            return self._parent._cast(_3981.PlanetaryGearSetCompoundStabilityAnalysis)

        @property
        def planet_carrier_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(_3983.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(_3985.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(_3986.RingPinsCompoundStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3987,
            )

            return self._parent._cast(
                _3987.RingPinsToDiscConnectionCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_assembly_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(
                _3988.RollingRingAssemblyCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(_3989.RollingRingCompoundStabilityAnalysis)

        @property
        def rolling_ring_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(
                _3990.RollingRingConnectionCompoundStabilityAnalysis
            )

        @property
        def root_assembly_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(_3991.RootAssemblyCompoundStabilityAnalysis)

        @property
        def shaft_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(_3992.ShaftCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(_3993.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(
                _3994.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(
                _3995.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(_3996.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(
                _3997.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(_3998.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def spring_damper_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.SpringDamperCompoundStabilityAnalysis)

        @property
        def spring_damper_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.SpringDamperConnectionCompoundStabilityAnalysis
            )

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(_4001.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(
                _4002.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4004,
            )

            return self._parent._cast(
                _4004.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(_4005.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(
                _4006.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(
                _4007.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(
                _4008.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(
                _4009.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(_4010.SynchroniserCompoundStabilityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4011,
            )

            return self._parent._cast(_4011.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(_4012.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(_4013.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4014,
            )

            return self._parent._cast(_4014.TorqueConverterCompoundStabilityAnalysis)

        @property
        def torque_converter_connection_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(
                _4015.TorqueConverterConnectionCompoundStabilityAnalysis
            )

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(
                _4016.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(
                _4017.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(_4018.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(_4020.WormGearCompoundStabilityAnalysis)

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.WormGearMeshCompoundStabilityAnalysis)

        @property
        def worm_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4022,
            )

            return self._parent._cast(_4022.WormGearSetCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4023,
            )

            return self._parent._cast(_4023.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(_4024.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4025,
            )

            return self._parent._cast(_4025.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def abstract_assembly_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4167,
            )

            return self._parent._cast(_4167.AbstractAssemblyCompoundPowerFlow)

        @property
        def abstract_shaft_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4168,
            )

            return self._parent._cast(_4168.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4169,
            )

            return self._parent._cast(_4169.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4170,
            )

            return self._parent._cast(
                _4170.AbstractShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4171,
            )

            return self._parent._cast(_4171.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4172,
            )

            return self._parent._cast(_4172.AGMAGleasonConicalGearMeshCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearSetCompoundPowerFlow)

        @property
        def assembly_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4174,
            )

            return self._parent._cast(_4174.AssemblyCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4175,
            )

            return self._parent._cast(_4175.BearingCompoundPowerFlow)

        @property
        def belt_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4176,
            )

            return self._parent._cast(_4176.BeltConnectionCompoundPowerFlow)

        @property
        def belt_drive_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.BeltDriveCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4178,
            )

            return self._parent._cast(_4178.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4179,
            )

            return self._parent._cast(_4179.BevelDifferentialGearMeshCompoundPowerFlow)

        @property
        def bevel_differential_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelDifferentialGearSetCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4181,
            )

            return self._parent._cast(
                _4181.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4182,
            )

            return self._parent._cast(_4182.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4183,
            )

            return self._parent._cast(_4183.BevelGearCompoundPowerFlow)

        @property
        def bevel_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4184,
            )

            return self._parent._cast(_4184.BevelGearMeshCompoundPowerFlow)

        @property
        def bevel_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.BevelGearSetCompoundPowerFlow)

        @property
        def bolt_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4186,
            )

            return self._parent._cast(_4186.BoltCompoundPowerFlow)

        @property
        def bolted_joint_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4187,
            )

            return self._parent._cast(_4187.BoltedJointCompoundPowerFlow)

        @property
        def clutch_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4188,
            )

            return self._parent._cast(_4188.ClutchCompoundPowerFlow)

        @property
        def clutch_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4189,
            )

            return self._parent._cast(_4189.ClutchConnectionCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.ClutchHalfCompoundPowerFlow)

        @property
        def coaxial_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.CoaxialConnectionCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def concept_coupling_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4193,
            )

            return self._parent._cast(_4193.ConceptCouplingCompoundPowerFlow)

        @property
        def concept_coupling_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ConceptCouplingConnectionCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4195,
            )

            return self._parent._cast(_4195.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4196,
            )

            return self._parent._cast(_4196.ConceptGearCompoundPowerFlow)

        @property
        def concept_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConceptGearMeshCompoundPowerFlow)

        @property
        def concept_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConceptGearSetCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4199,
            )

            return self._parent._cast(_4199.ConicalGearCompoundPowerFlow)

        @property
        def conical_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4200,
            )

            return self._parent._cast(_4200.ConicalGearMeshCompoundPowerFlow)

        @property
        def conical_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConicalGearSetCompoundPowerFlow)

        @property
        def connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4202,
            )

            return self._parent._cast(_4202.ConnectionCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4203,
            )

            return self._parent._cast(_4203.ConnectorCompoundPowerFlow)

        @property
        def coupling_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4204,
            )

            return self._parent._cast(_4204.CouplingCompoundPowerFlow)

        @property
        def coupling_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.CouplingConnectionCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4206,
            )

            return self._parent._cast(_4206.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_belt_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4207,
            )

            return self._parent._cast(_4207.CVTBeltConnectionCompoundPowerFlow)

        @property
        def cvt_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.CVTCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4209,
            )

            return self._parent._cast(_4209.CVTPulleyCompoundPowerFlow)

        @property
        def cycloidal_assembly_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4210,
            )

            return self._parent._cast(_4210.CycloidalAssemblyCompoundPowerFlow)

        @property
        def cycloidal_disc_central_bearing_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(
                _4211.CycloidalDiscCentralBearingConnectionCompoundPowerFlow
            )

        @property
        def cycloidal_disc_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4212,
            )

            return self._parent._cast(_4212.CycloidalDiscCompoundPowerFlow)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4213,
            )

            return self._parent._cast(
                _4213.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
            )

        @property
        def cylindrical_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4214,
            )

            return self._parent._cast(_4214.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4215,
            )

            return self._parent._cast(_4215.CylindricalGearMeshCompoundPowerFlow)

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.CylindricalGearSetCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4217,
            )

            return self._parent._cast(_4217.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def datum_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4218,
            )

            return self._parent._cast(_4218.DatumCompoundPowerFlow)

        @property
        def external_cad_model_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.ExternalCADModelCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4220,
            )

            return self._parent._cast(_4220.FaceGearCompoundPowerFlow)

        @property
        def face_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4221,
            )

            return self._parent._cast(_4221.FaceGearMeshCompoundPowerFlow)

        @property
        def face_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.FaceGearSetCompoundPowerFlow)

        @property
        def fe_part_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4223,
            )

            return self._parent._cast(_4223.FEPartCompoundPowerFlow)

        @property
        def flexible_pin_assembly_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4224,
            )

            return self._parent._cast(_4224.FlexiblePinAssemblyCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4225,
            )

            return self._parent._cast(_4225.GearCompoundPowerFlow)

        @property
        def gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4226,
            )

            return self._parent._cast(_4226.GearMeshCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.GearSetCompoundPowerFlow)

        @property
        def guide_dxf_model_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4228,
            )

            return self._parent._cast(_4228.GuideDxfModelCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4229,
            )

            return self._parent._cast(_4229.HypoidGearCompoundPowerFlow)

        @property
        def hypoid_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4230,
            )

            return self._parent._cast(_4230.HypoidGearMeshCompoundPowerFlow)

        @property
        def hypoid_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.HypoidGearSetCompoundPowerFlow)

        @property
        def inter_mountable_component_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4232,
            )

            return self._parent._cast(
                _4232.InterMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4233,
            )

            return self._parent._cast(
                _4233.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4234,
            )

            return self._parent._cast(
                _4234.KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4236,
            )

            return self._parent._cast(
                _4236.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4237,
            )

            return self._parent._cast(
                _4237.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(
                _4238.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4239,
            )

            return self._parent._cast(
                _4239.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4240,
            )

            return self._parent._cast(
                _4240.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(
                _4241.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4242,
            )

            return self._parent._cast(_4242.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.MeasurementComponentCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.OilSealCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.PartToPartShearCouplingCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(
                _4248.PartToPartShearCouplingConnectionCompoundPowerFlow
            )

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4249,
            )

            return self._parent._cast(
                _4249.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planetary_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.PlanetaryConnectionCompoundPowerFlow)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(_4251.PlanetaryGearSetCompoundPowerFlow)

        @property
        def planet_carrier_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4252,
            )

            return self._parent._cast(_4252.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4253,
            )

            return self._parent._cast(_4253.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(_4256.RingPinsCompoundPowerFlow)

        @property
        def ring_pins_to_disc_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(_4257.RingPinsToDiscConnectionCompoundPowerFlow)

        @property
        def rolling_ring_assembly_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(_4258.RollingRingAssemblyCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4259,
            )

            return self._parent._cast(_4259.RollingRingCompoundPowerFlow)

        @property
        def rolling_ring_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4260,
            )

            return self._parent._cast(_4260.RollingRingConnectionCompoundPowerFlow)

        @property
        def root_assembly_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.RootAssemblyCompoundPowerFlow)

        @property
        def shaft_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4262,
            )

            return self._parent._cast(_4262.ShaftCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4263,
            )

            return self._parent._cast(_4263.ShaftHubConnectionCompoundPowerFlow)

        @property
        def shaft_to_mountable_component_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(
                _4264.ShaftToMountableComponentConnectionCompoundPowerFlow
            )

        @property
        def specialised_assembly_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4266,
            )

            return self._parent._cast(_4266.SpiralBevelGearCompoundPowerFlow)

        @property
        def spiral_bevel_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4267,
            )

            return self._parent._cast(_4267.SpiralBevelGearMeshCompoundPowerFlow)

        @property
        def spiral_bevel_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.SpiralBevelGearSetCompoundPowerFlow)

        @property
        def spring_damper_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.SpringDamperCompoundPowerFlow)

        @property
        def spring_damper_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4270,
            )

            return self._parent._cast(_4270.SpringDamperConnectionCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4271,
            )

            return self._parent._cast(_4271.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4272,
            )

            return self._parent._cast(_4272.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.StraightBevelDiffGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelDiffGearSetCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4275,
            )

            return self._parent._cast(_4275.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4276,
            )

            return self._parent._cast(_4276.StraightBevelGearMeshCompoundPowerFlow)

        @property
        def straight_bevel_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.StraightBevelGearSetCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4278,
            )

            return self._parent._cast(_4278.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4279,
            )

            return self._parent._cast(_4279.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.SynchroniserCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4282,
            )

            return self._parent._cast(_4282.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.TorqueConverterCompoundPowerFlow)

        @property
        def torque_converter_connection_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.TorqueConverterConnectionCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4286,
            )

            return self._parent._cast(_4286.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4287,
            )

            return self._parent._cast(_4287.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.WormGearCompoundPowerFlow)

        @property
        def worm_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.WormGearMeshCompoundPowerFlow)

        @property
        def worm_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.WormGearSetCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4293,
            )

            return self._parent._cast(_4293.ZerolBevelGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_mesh_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4294,
            )

            return self._parent._cast(_4294.ZerolBevelGearMeshCompoundPowerFlow)

        @property
        def zerol_bevel_gear_set_compound_power_flow(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.ZerolBevelGearSetCompoundPowerFlow)

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4443,
            )

            return self._parent._cast(_4443.AbstractAssemblyCompoundParametricStudyTool)

        @property
        def abstract_shaft_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4444,
            )

            return self._parent._cast(_4444.AbstractShaftCompoundParametricStudyTool)

        @property
        def abstract_shaft_or_housing_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4445,
            )

            return self._parent._cast(
                _4445.AbstractShaftOrHousingCompoundParametricStudyTool
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4446,
            )

            return self._parent._cast(
                _4446.AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4447,
            )

            return self._parent._cast(
                _4447.AGMAGleasonConicalGearCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4448,
            )

            return self._parent._cast(
                _4448.AGMAGleasonConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4449,
            )

            return self._parent._cast(
                _4449.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def assembly_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4450,
            )

            return self._parent._cast(_4450.AssemblyCompoundParametricStudyTool)

        @property
        def bearing_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(_4451.BearingCompoundParametricStudyTool)

        @property
        def belt_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(_4452.BeltConnectionCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4453,
            )

            return self._parent._cast(_4453.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4454,
            )

            return self._parent._cast(
                _4454.BevelDifferentialGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(
                _4455.BevelDifferentialGearMeshCompoundParametricStudyTool
            )

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4456,
            )

            return self._parent._cast(
                _4456.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_differential_planet_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4457,
            )

            return self._parent._cast(
                _4457.BevelDifferentialPlanetGearCompoundParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(
                _4458.BevelDifferentialSunGearCompoundParametricStudyTool
            )

        @property
        def bevel_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4459,
            )

            return self._parent._cast(_4459.BevelGearCompoundParametricStudyTool)

        @property
        def bevel_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4460,
            )

            return self._parent._cast(_4460.BevelGearMeshCompoundParametricStudyTool)

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4461,
            )

            return self._parent._cast(_4461.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolt_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4462,
            )

            return self._parent._cast(_4462.BoltCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4463,
            )

            return self._parent._cast(_4463.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4464,
            )

            return self._parent._cast(_4464.ClutchCompoundParametricStudyTool)

        @property
        def clutch_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.ClutchConnectionCompoundParametricStudyTool)

        @property
        def clutch_half_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4466,
            )

            return self._parent._cast(_4466.ClutchHalfCompoundParametricStudyTool)

        @property
        def coaxial_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4467,
            )

            return self._parent._cast(
                _4467.CoaxialConnectionCompoundParametricStudyTool
            )

        @property
        def component_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4468,
            )

            return self._parent._cast(_4468.ComponentCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4469,
            )

            return self._parent._cast(_4469.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_coupling_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4470,
            )

            return self._parent._cast(
                _4470.ConceptCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def concept_coupling_half_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4471,
            )

            return self._parent._cast(
                _4471.ConceptCouplingHalfCompoundParametricStudyTool
            )

        @property
        def concept_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4472,
            )

            return self._parent._cast(_4472.ConceptGearCompoundParametricStudyTool)

        @property
        def concept_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4473,
            )

            return self._parent._cast(_4473.ConceptGearMeshCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4474,
            )

            return self._parent._cast(_4474.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4475,
            )

            return self._parent._cast(_4475.ConicalGearCompoundParametricStudyTool)

        @property
        def conical_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ConicalGearMeshCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4477,
            )

            return self._parent._cast(_4477.ConicalGearSetCompoundParametricStudyTool)

        @property
        def connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4478,
            )

            return self._parent._cast(_4478.ConnectionCompoundParametricStudyTool)

        @property
        def connector_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4479,
            )

            return self._parent._cast(_4479.ConnectorCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4480,
            )

            return self._parent._cast(_4480.CouplingCompoundParametricStudyTool)

        @property
        def coupling_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4481,
            )

            return self._parent._cast(
                _4481.CouplingConnectionCompoundParametricStudyTool
            )

        @property
        def coupling_half_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.CouplingHalfCompoundParametricStudyTool)

        @property
        def cvt_belt_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4483,
            )

            return self._parent._cast(
                _4483.CVTBeltConnectionCompoundParametricStudyTool
            )

        @property
        def cvt_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4484,
            )

            return self._parent._cast(_4484.CVTCompoundParametricStudyTool)

        @property
        def cvt_pulley_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4485,
            )

            return self._parent._cast(_4485.CVTPulleyCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(
                _4486.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4487,
            )

            return self._parent._cast(
                _4487.CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
            )

        @property
        def cycloidal_disc_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(_4488.CycloidalDiscCompoundParametricStudyTool)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4489,
            )

            return self._parent._cast(
                _4489.CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4490,
            )

            return self._parent._cast(_4490.CylindricalGearCompoundParametricStudyTool)

        @property
        def cylindrical_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4491,
            )

            return self._parent._cast(
                _4491.CylindricalGearMeshCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4492,
            )

            return self._parent._cast(
                _4492.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def cylindrical_planet_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4493,
            )

            return self._parent._cast(
                _4493.CylindricalPlanetGearCompoundParametricStudyTool
            )

        @property
        def datum_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(_4494.DatumCompoundParametricStudyTool)

        @property
        def external_cad_model_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4495,
            )

            return self._parent._cast(_4495.ExternalCADModelCompoundParametricStudyTool)

        @property
        def face_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4496,
            )

            return self._parent._cast(_4496.FaceGearCompoundParametricStudyTool)

        @property
        def face_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4497,
            )

            return self._parent._cast(_4497.FaceGearMeshCompoundParametricStudyTool)

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4498,
            )

            return self._parent._cast(_4498.FaceGearSetCompoundParametricStudyTool)

        @property
        def fe_part_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4499,
            )

            return self._parent._cast(_4499.FEPartCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(
                _4500.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.GearCompoundParametricStudyTool)

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(_4502.GearMeshCompoundParametricStudyTool)

        @property
        def gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4503,
            )

            return self._parent._cast(_4503.GearSetCompoundParametricStudyTool)

        @property
        def guide_dxf_model_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4504,
            )

            return self._parent._cast(_4504.GuideDxfModelCompoundParametricStudyTool)

        @property
        def hypoid_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(_4505.HypoidGearCompoundParametricStudyTool)

        @property
        def hypoid_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4506,
            )

            return self._parent._cast(_4506.HypoidGearMeshCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4507,
            )

            return self._parent._cast(_4507.HypoidGearSetCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4508,
            )

            return self._parent._cast(
                _4508.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(
                _4509.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4510,
            )

            return self._parent._cast(
                _4510.KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4511,
            )

            return self._parent._cast(
                _4511.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4512,
            )

            return self._parent._cast(
                _4512.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4514,
            )

            return self._parent._cast(
                _4514.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4515,
            )

            return self._parent._cast(
                _4515.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4517,
            )

            return self._parent._cast(
                _4517.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def mass_disc_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4518,
            )

            return self._parent._cast(_4518.MassDiscCompoundParametricStudyTool)

        @property
        def measurement_component_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.MeasurementComponentCompoundParametricStudyTool
            )

        @property
        def mountable_component_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4520,
            )

            return self._parent._cast(
                _4520.MountableComponentCompoundParametricStudyTool
            )

        @property
        def oil_seal_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4521,
            )

            return self._parent._cast(_4521.OilSealCompoundParametricStudyTool)

        @property
        def part_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4522,
            )

            return self._parent._cast(_4522.PartCompoundParametricStudyTool)

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4523,
            )

            return self._parent._cast(
                _4523.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4524,
            )

            return self._parent._cast(
                _4524.PartToPartShearCouplingConnectionCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_half_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(
                _4525.PartToPartShearCouplingHalfCompoundParametricStudyTool
            )

        @property
        def planetary_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4526,
            )

            return self._parent._cast(
                _4526.PlanetaryConnectionCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4527,
            )

            return self._parent._cast(_4527.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def planet_carrier_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4528,
            )

            return self._parent._cast(_4528.PlanetCarrierCompoundParametricStudyTool)

        @property
        def point_load_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(_4529.PointLoadCompoundParametricStudyTool)

        @property
        def power_load_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4530,
            )

            return self._parent._cast(_4530.PowerLoadCompoundParametricStudyTool)

        @property
        def pulley_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(_4531.PulleyCompoundParametricStudyTool)

        @property
        def ring_pins_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4532,
            )

            return self._parent._cast(_4532.RingPinsCompoundParametricStudyTool)

        @property
        def ring_pins_to_disc_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4533,
            )

            return self._parent._cast(
                _4533.RingPinsToDiscConnectionCompoundParametricStudyTool
            )

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4534,
            )

            return self._parent._cast(
                _4534.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def rolling_ring_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4535,
            )

            return self._parent._cast(_4535.RollingRingCompoundParametricStudyTool)

        @property
        def rolling_ring_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4536,
            )

            return self._parent._cast(
                _4536.RollingRingConnectionCompoundParametricStudyTool
            )

        @property
        def root_assembly_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4537,
            )

            return self._parent._cast(_4537.RootAssemblyCompoundParametricStudyTool)

        @property
        def shaft_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4538,
            )

            return self._parent._cast(_4538.ShaftCompoundParametricStudyTool)

        @property
        def shaft_hub_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(
                _4539.ShaftHubConnectionCompoundParametricStudyTool
            )

        @property
        def shaft_to_mountable_component_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4540,
            )

            return self._parent._cast(
                _4540.ShaftToMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4541,
            )

            return self._parent._cast(
                _4541.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4542,
            )

            return self._parent._cast(_4542.SpiralBevelGearCompoundParametricStudyTool)

        @property
        def spiral_bevel_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.SpiralBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4544,
            )

            return self._parent._cast(
                _4544.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4545,
            )

            return self._parent._cast(_4545.SpringDamperCompoundParametricStudyTool)

        @property
        def spring_damper_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.SpringDamperConnectionCompoundParametricStudyTool
            )

        @property
        def spring_damper_half_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(_4547.SpringDamperHalfCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4548,
            )

            return self._parent._cast(
                _4548.StraightBevelDiffGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4549,
            )

            return self._parent._cast(
                _4549.StraightBevelDiffGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4550,
            )

            return self._parent._cast(
                _4550.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4551,
            )

            return self._parent._cast(
                _4551.StraightBevelGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(
                _4552.StraightBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4553,
            )

            return self._parent._cast(
                _4553.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_planet_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4554,
            )

            return self._parent._cast(
                _4554.StraightBevelPlanetGearCompoundParametricStudyTool
            )

        @property
        def straight_bevel_sun_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(
                _4555.StraightBevelSunGearCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4556,
            )

            return self._parent._cast(_4556.SynchroniserCompoundParametricStudyTool)

        @property
        def synchroniser_half_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4557,
            )

            return self._parent._cast(_4557.SynchroniserHalfCompoundParametricStudyTool)

        @property
        def synchroniser_part_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(_4558.SynchroniserPartCompoundParametricStudyTool)

        @property
        def synchroniser_sleeve_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4559,
            )

            return self._parent._cast(
                _4559.SynchroniserSleeveCompoundParametricStudyTool
            )

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4560,
            )

            return self._parent._cast(_4560.TorqueConverterCompoundParametricStudyTool)

        @property
        def torque_converter_connection_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4561,
            )

            return self._parent._cast(
                _4561.TorqueConverterConnectionCompoundParametricStudyTool
            )

        @property
        def torque_converter_pump_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(
                _4562.TorqueConverterPumpCompoundParametricStudyTool
            )

        @property
        def torque_converter_turbine_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4563,
            )

            return self._parent._cast(
                _4563.TorqueConverterTurbineCompoundParametricStudyTool
            )

        @property
        def unbalanced_mass_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4564,
            )

            return self._parent._cast(_4564.UnbalancedMassCompoundParametricStudyTool)

        @property
        def virtual_component_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4565,
            )

            return self._parent._cast(_4565.VirtualComponentCompoundParametricStudyTool)

        @property
        def worm_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4566,
            )

            return self._parent._cast(_4566.WormGearCompoundParametricStudyTool)

        @property
        def worm_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4567,
            )

            return self._parent._cast(_4567.WormGearMeshCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4568,
            )

            return self._parent._cast(_4568.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4569,
            )

            return self._parent._cast(_4569.ZerolBevelGearCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_mesh_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(
                _4570.ZerolBevelGearMeshCompoundParametricStudyTool
            )

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4571,
            )

            return self._parent._cast(
                _4571.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AbstractAssemblyCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4729,
            )

            return self._parent._cast(_4729.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4730,
            )

            return self._parent._cast(_4730.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4731,
            )

            return self._parent._cast(
                _4731.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4732,
            )

            return self._parent._cast(_4732.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4733,
            )

            return self._parent._cast(
                _4733.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(
                _4734.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def assembly_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4735,
            )

            return self._parent._cast(_4735.AssemblyCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.BearingCompoundModalAnalysis)

        @property
        def belt_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4737,
            )

            return self._parent._cast(_4737.BeltConnectionCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(_4738.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4739,
            )

            return self._parent._cast(_4739.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(
                _4740.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(
                _4741.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(
                _4742.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(
                _4743.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4744,
            )

            return self._parent._cast(_4744.BevelGearCompoundModalAnalysis)

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4745,
            )

            return self._parent._cast(_4745.BevelGearMeshCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BevelGearSetCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4747,
            )

            return self._parent._cast(_4747.BoltCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4748,
            )

            return self._parent._cast(_4748.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.ClutchCompoundModalAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(_4750.ClutchConnectionCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.ClutchHalfCompoundModalAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.CoaxialConnectionCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(_4754.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4755,
            )

            return self._parent._cast(
                _4755.ConceptCouplingConnectionCompoundModalAnalysis
            )

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(_4757.ConceptGearCompoundModalAnalysis)

        @property
        def concept_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.ConceptGearMeshCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.ConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ConicalGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConicalGearSetCompoundModalAnalysis)

        @property
        def connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.ConnectionCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(_4764.ConnectorCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.CouplingCompoundModalAnalysis)

        @property
        def coupling_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.CouplingConnectionCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4768,
            )

            return self._parent._cast(_4768.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.CVTCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4770,
            )

            return self._parent._cast(_4770.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(
                _4772.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
            )

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CycloidalDiscCompoundModalAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4774,
            )

            return self._parent._cast(
                _4774.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
            )

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.CylindricalGearSetCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4778,
            )

            return self._parent._cast(_4778.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4781,
            )

            return self._parent._cast(_4781.FaceGearCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.FaceGearMeshCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.FaceGearSetCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.FEPartCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.GearCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4787,
            )

            return self._parent._cast(_4787.GearMeshCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.GearSetCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4789,
            )

            return self._parent._cast(_4789.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4790,
            )

            return self._parent._cast(_4790.HypoidGearCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4791,
            )

            return self._parent._cast(_4791.HypoidGearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.HypoidGearSetCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(
                _4793.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(
                _4794.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(
                _4795.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4797,
            )

            return self._parent._cast(
                _4797.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(
                _4798.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4800,
            )

            return self._parent._cast(
                _4800.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(
                _4801.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.OilSealCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(
                _4808.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(
                _4809.PartToPartShearCouplingConnectionCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(
                _4810.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planetary_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def planet_carrier_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(_4814.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(_4816.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(_4817.RingPinsCompoundModalAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(
                _4818.RingPinsToDiscConnectionCompoundModalAnalysis
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(_4820.RollingRingCompoundModalAnalysis)

        @property
        def rolling_ring_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4821,
            )

            return self._parent._cast(_4821.RollingRingConnectionCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.RootAssemblyCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(_4824.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4825,
            )

            return self._parent._cast(
                _4825.ShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4827,
            )

            return self._parent._cast(_4827.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.SpringDamperCompoundModalAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4831,
            )

            return self._parent._cast(_4831.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4833,
            )

            return self._parent._cast(_4833.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(
                _4834.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(
                _4835.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4836,
            )

            return self._parent._cast(_4836.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(_4837.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(
                _4839.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.SynchroniserCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.TorqueConverterCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(
                _4846.TorqueConverterConnectionCompoundModalAnalysis
            )

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.WormGearCompoundModalAnalysis)

        @property
        def worm_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.WormGearMeshCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4854,
            )

            return self._parent._cast(_4854.ZerolBevelGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(_4855.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4988,
            )

            return self._parent._cast(
                _4988.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4989,
            )

            return self._parent._cast(
                _4989.AbstractShaftCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4990,
            )

            return self._parent._cast(
                _4990.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4991,
            )

            return self._parent._cast(
                _4991.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4992,
            )

            return self._parent._cast(
                _4992.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4993,
            )

            return self._parent._cast(
                _4993.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4994,
            )

            return self._parent._cast(
                _4994.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4995,
            )

            return self._parent._cast(_4995.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(_4996.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(
                _4997.BeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4998,
            )

            return self._parent._cast(_4998.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4999,
            )

            return self._parent._cast(
                _4999.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(
                _5000.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5001,
            )

            return self._parent._cast(
                _5001.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5003,
            )

            return self._parent._cast(
                _5003.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5004,
            )

            return self._parent._cast(_5004.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(
                _5005.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5006,
            )

            return self._parent._cast(
                _5006.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bolt_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5007,
            )

            return self._parent._cast(_5007.BoltCompoundModalAnalysisAtAStiffness)

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5008,
            )

            return self._parent._cast(
                _5008.BoltedJointCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(_5009.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(
                _5010.ClutchConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(_5011.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(
                _5012.CoaxialConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5014,
            )

            return self._parent._cast(
                _5014.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(
                _5015.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5016,
            )

            return self._parent._cast(
                _5016.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5017,
            )

            return self._parent._cast(
                _5017.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ConceptGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5019,
            )

            return self._parent._cast(
                _5019.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5020,
            )

            return self._parent._cast(
                _5020.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(
                _5021.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(_5023.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(_5024.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5025,
            )

            return self._parent._cast(_5025.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5026,
            )

            return self._parent._cast(
                _5026.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(
                _5027.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5028,
            )

            return self._parent._cast(
                _5028.CVTBeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5029,
            )

            return self._parent._cast(_5029.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5030,
            )

            return self._parent._cast(_5030.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(
                _5031.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(
                _5032.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(
                _5033.CycloidalDiscCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5034,
            )

            return self._parent._cast(
                _5034.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(
                _5035.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5036,
            )

            return self._parent._cast(
                _5036.CylindricalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(
                _5037.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5038,
            )

            return self._parent._cast(
                _5038.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def datum_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(_5039.DatumCompoundModalAnalysisAtAStiffness)

        @property
        def external_cad_model_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5040,
            )

            return self._parent._cast(
                _5040.ExternalCADModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(_5041.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5042,
            )

            return self._parent._cast(
                _5042.FaceGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(
                _5043.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def fe_part_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5044,
            )

            return self._parent._cast(_5044.FEPartCompoundModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(
                _5045.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(_5046.GearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(_5047.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(_5048.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5049,
            )

            return self._parent._cast(
                _5049.GuideDxfModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(_5050.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.HypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(
                _5052.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5054,
            )

            return self._parent._cast(
                _5054.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(
                _5055.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(
                _5056.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5057,
            )

            return self._parent._cast(
                _5057.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5059,
            )

            return self._parent._cast(
                _5059.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5060,
            )

            return self._parent._cast(
                _5060.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(
                _5062.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5063,
            )

            return self._parent._cast(_5063.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(
                _5065.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(
                _5068.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(
                _5069.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5070,
            )

            return self._parent._cast(
                _5070.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(
                _5071.PlanetaryConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5072,
            )

            return self._parent._cast(
                _5072.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(
                _5073.PlanetCarrierCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(_5074.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(_5076.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5077,
            )

            return self._parent._cast(_5077.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(
                _5078.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5079,
            )

            return self._parent._cast(
                _5079.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5080,
            )

            return self._parent._cast(
                _5080.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5081,
            )

            return self._parent._cast(
                _5081.RollingRingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5082,
            )

            return self._parent._cast(
                _5082.RootAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5083,
            )

            return self._parent._cast(_5083.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(
                _5084.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(
                _5085.ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5087,
            )

            return self._parent._cast(
                _5087.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(
                _5090.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(
                _5091.SpringDamperConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5092,
            )

            return self._parent._cast(
                _5092.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5093,
            )

            return self._parent._cast(
                _5093.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5095,
            )

            return self._parent._cast(
                _5095.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5096,
            )

            return self._parent._cast(
                _5096.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(
                _5098.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5099,
            )

            return self._parent._cast(
                _5099.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5100,
            )

            return self._parent._cast(
                _5100.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.SynchroniserCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5102,
            )

            return self._parent._cast(
                _5102.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5103,
            )

            return self._parent._cast(
                _5103.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5105,
            )

            return self._parent._cast(
                _5105.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5107,
            )

            return self._parent._cast(
                _5107.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5108,
            )

            return self._parent._cast(
                _5108.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(_5111.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.WormGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(
                _5113.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5114,
            )

            return self._parent._cast(
                _5114.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5116,
            )

            return self._parent._cast(
                _5116.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5248,
            )

            return self._parent._cast(_5248.AbstractShaftCompoundModalAnalysisAtASpeed)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5249,
            )

            return self._parent._cast(
                _5249.AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5250,
            )

            return self._parent._cast(
                _5250.AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5251,
            )

            return self._parent._cast(
                _5251.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5252,
            )

            return self._parent._cast(
                _5252.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5253,
            )

            return self._parent._cast(
                _5253.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5254,
            )

            return self._parent._cast(_5254.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def bearing_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5255,
            )

            return self._parent._cast(_5255.BearingCompoundModalAnalysisAtASpeed)

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(_5256.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5257,
            )

            return self._parent._cast(_5257.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5258,
            )

            return self._parent._cast(
                _5258.BevelDifferentialGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(
                _5259.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5260,
            )

            return self._parent._cast(
                _5260.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5261,
            )

            return self._parent._cast(
                _5261.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5262,
            )

            return self._parent._cast(
                _5262.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5263,
            )

            return self._parent._cast(_5263.BevelGearCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5264,
            )

            return self._parent._cast(_5264.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5265,
            )

            return self._parent._cast(_5265.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolt_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5266,
            )

            return self._parent._cast(_5266.BoltCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5267,
            )

            return self._parent._cast(_5267.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(_5268.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(
                _5269.ClutchConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def clutch_half_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(_5270.ClutchHalfCompoundModalAnalysisAtASpeed)

        @property
        def coaxial_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5271,
            )

            return self._parent._cast(
                _5271.CoaxialConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(_5272.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5273,
            )

            return self._parent._cast(
                _5273.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(
                _5274.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5275,
            )

            return self._parent._cast(
                _5275.ConceptCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5276,
            )

            return self._parent._cast(_5276.ConceptGearCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(
                _5277.ConceptGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5279,
            )

            return self._parent._cast(_5279.ConicalGearCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(
                _5280.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(_5281.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(_5282.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connector_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5283,
            )

            return self._parent._cast(_5283.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(
                _5285.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(
                _5287.CVTBeltConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(_5288.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5289,
            )

            return self._parent._cast(_5289.CVTPulleyCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(
                _5290.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5291,
            )

            return self._parent._cast(
                _5291.CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5292,
            )

            return self._parent._cast(_5292.CycloidalDiscCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5293,
            )

            return self._parent._cast(
                _5293.CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5294,
            )

            return self._parent._cast(
                _5294.CylindricalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(
                _5295.CylindricalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(
                _5296.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5297,
            )

            return self._parent._cast(
                _5297.CylindricalPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def datum_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5298,
            )

            return self._parent._cast(_5298.DatumCompoundModalAnalysisAtASpeed)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5299,
            )

            return self._parent._cast(
                _5299.ExternalCADModelCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5300,
            )

            return self._parent._cast(_5300.FaceGearCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(_5301.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(_5302.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def fe_part_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5303,
            )

            return self._parent._cast(_5303.FEPartCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(
                _5304.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5305,
            )

            return self._parent._cast(_5305.GearCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(_5306.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5308,
            )

            return self._parent._cast(_5308.GuideDxfModelCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5309,
            )

            return self._parent._cast(_5309.HypoidGearCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5310,
            )

            return self._parent._cast(_5310.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(_5311.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5312,
            )

            return self._parent._cast(
                _5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5313,
            )

            return self._parent._cast(
                _5313.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(
                _5315.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5316,
            )

            return self._parent._cast(
                _5316.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5318,
            )

            return self._parent._cast(
                _5318.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5319,
            )

            return self._parent._cast(
                _5319.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(
                _5321.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5322,
            )

            return self._parent._cast(_5322.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5323,
            )

            return self._parent._cast(
                _5323.MeasurementComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(
                _5324.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(_5325.OilSealCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(
                _5328.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5329,
            )

            return self._parent._cast(
                _5329.PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(
                _5330.PlanetaryConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(
                _5331.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(_5332.PlanetCarrierCompoundModalAnalysisAtASpeed)

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5333,
            )

            return self._parent._cast(_5333.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def pulley_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5335,
            )

            return self._parent._cast(_5335.PulleyCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5336,
            )

            return self._parent._cast(_5336.RingPinsCompoundModalAnalysisAtASpeed)

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(
                _5337.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5338,
            )

            return self._parent._cast(
                _5338.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5339,
            )

            return self._parent._cast(_5339.RollingRingCompoundModalAnalysisAtASpeed)

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5340,
            )

            return self._parent._cast(
                _5340.RollingRingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(_5341.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def shaft_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(_5342.ShaftCompoundModalAnalysisAtASpeed)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5343,
            )

            return self._parent._cast(
                _5343.ShaftHubConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5344,
            )

            return self._parent._cast(
                _5344.ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5346,
            )

            return self._parent._cast(
                _5346.SpiralBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5348,
            )

            return self._parent._cast(
                _5348.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.SpringDamperConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5351,
            )

            return self._parent._cast(
                _5351.SpringDamperHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5352,
            )

            return self._parent._cast(
                _5352.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5355,
            )

            return self._parent._cast(
                _5355.StraightBevelGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(
                _5356.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(
                _5357.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(
                _5358.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5359,
            )

            return self._parent._cast(
                _5359.StraightBevelSunGearCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(_5360.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5361,
            )

            return self._parent._cast(
                _5361.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5362,
            )

            return self._parent._cast(
                _5362.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5363,
            )

            return self._parent._cast(
                _5363.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(
                _5364.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(
                _5365.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5366,
            )

            return self._parent._cast(
                _5366.TorqueConverterPumpCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5367,
            )

            return self._parent._cast(
                _5367.TorqueConverterTurbineCompoundModalAnalysisAtASpeed
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(_5368.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(
                _5369.VirtualComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5370,
            )

            return self._parent._cast(_5370.WormGearCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(_5371.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5372,
            )

            return self._parent._cast(_5372.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5373,
            )

            return self._parent._cast(_5373.ZerolBevelGearCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(
                _5375.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5530,
            )

            return self._parent._cast(
                _5530.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5531,
            )

            return self._parent._cast(
                _5531.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5532,
            )

            return self._parent._cast(
                _5532.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5533,
            )

            return self._parent._cast(
                _5533.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5534,
            )

            return self._parent._cast(
                _5534.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5535,
            )

            return self._parent._cast(
                _5535.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5536,
            )

            return self._parent._cast(_5536.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5537,
            )

            return self._parent._cast(_5537.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(
                _5538.BeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(_5539.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5540,
            )

            return self._parent._cast(
                _5540.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(
                _5541.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(
                _5544.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(_5545.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(
                _5546.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(
                _5547.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5548,
            )

            return self._parent._cast(_5548.BoltCompoundMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5549,
            )

            return self._parent._cast(
                _5549.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(
                _5551.ClutchConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5552,
            )

            return self._parent._cast(_5552.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(
                _5553.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(
                _5556.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5558,
            )

            return self._parent._cast(
                _5558.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ConceptGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(
                _5561.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5564,
            )

            return self._parent._cast(_5564.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(_5565.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(_5566.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(
                _5569.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(_5570.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5571,
            )

            return self._parent._cast(_5571.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(
                _5572.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5573,
            )

            return self._parent._cast(
                _5573.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(
                _5575.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5576,
            )

            return self._parent._cast(
                _5576.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(
                _5578.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5579,
            )

            return self._parent._cast(
                _5579.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def datum_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(_5580.DatumCompoundMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.ExternalCADModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5582,
            )

            return self._parent._cast(_5582.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.FaceGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(
                _5584.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(
                _5586.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(_5588.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(_5589.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(
                _5590.GuideDxfModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5592,
            )

            return self._parent._cast(
                _5592.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5595,
            )

            return self._parent._cast(
                _5595.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(
                _5597.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5598,
            )

            return self._parent._cast(
                _5598.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5601,
            )

            return self._parent._cast(
                _5601.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(_5607.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(
                _5609.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(
                _5610.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5611,
            )

            return self._parent._cast(
                _5611.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5612,
            )

            return self._parent._cast(
                _5612.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(
                _5614.PlanetCarrierCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(_5615.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(_5617.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5618,
            )

            return self._parent._cast(_5618.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(
                _5619.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(
                _5620.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5622,
            )

            return self._parent._cast(
                _5622.RollingRingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.RootAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(_5624.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5625,
            )

            return self._parent._cast(
                _5625.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(
                _5626.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5628,
            )

            return self._parent._cast(
                _5628.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5631,
            )

            return self._parent._cast(
                _5631.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(
                _5634.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5637,
            )

            return self._parent._cast(
                _5637.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5649,
            )

            return self._parent._cast(
                _5649.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5652,
            )

            return self._parent._cast(_5652.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.WormGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(
                _5654.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5655,
            )

            return self._parent._cast(
                _5655.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5879,
            )

            return self._parent._cast(_5879.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5880,
            )

            return self._parent._cast(_5880.AbstractShaftCompoundHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5881,
            )

            return self._parent._cast(
                _5881.AbstractShaftOrHousingCompoundHarmonicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5882,
            )

            return self._parent._cast(
                _5882.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5883,
            )

            return self._parent._cast(
                _5883.AGMAGleasonConicalGearCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5884,
            )

            return self._parent._cast(
                _5884.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5885,
            )

            return self._parent._cast(
                _5885.AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def assembly_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5886,
            )

            return self._parent._cast(_5886.AssemblyCompoundHarmonicAnalysis)

        @property
        def bearing_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(_5887.BearingCompoundHarmonicAnalysis)

        @property
        def belt_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5888,
            )

            return self._parent._cast(_5888.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def belt_drive_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5889,
            )

            return self._parent._cast(_5889.BeltDriveCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5890,
            )

            return self._parent._cast(
                _5890.BevelDifferentialGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5891,
            )

            return self._parent._cast(
                _5891.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5892,
            )

            return self._parent._cast(
                _5892.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5893,
            )

            return self._parent._cast(
                _5893.BevelDifferentialPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(
                _5894.BevelDifferentialSunGearCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(_5895.BevelGearCompoundHarmonicAnalysis)

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5896,
            )

            return self._parent._cast(_5896.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5897,
            )

            return self._parent._cast(_5897.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def bolt_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5898,
            )

            return self._parent._cast(_5898.BoltCompoundHarmonicAnalysis)

        @property
        def bolted_joint_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5899,
            )

            return self._parent._cast(_5899.BoltedJointCompoundHarmonicAnalysis)

        @property
        def clutch_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5900,
            )

            return self._parent._cast(_5900.ClutchCompoundHarmonicAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5901,
            )

            return self._parent._cast(_5901.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5902,
            )

            return self._parent._cast(_5902.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5903,
            )

            return self._parent._cast(_5903.CoaxialConnectionCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def concept_coupling_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(_5905.ConceptCouplingCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(
                _5906.ConceptCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5907,
            )

            return self._parent._cast(_5907.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def concept_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(_5908.ConceptGearCompoundHarmonicAnalysis)

        @property
        def concept_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5909,
            )

            return self._parent._cast(_5909.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def concept_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5910,
            )

            return self._parent._cast(_5910.ConceptGearSetCompoundHarmonicAnalysis)

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5911,
            )

            return self._parent._cast(_5911.ConicalGearCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(_5914.ConnectionCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5915,
            )

            return self._parent._cast(_5915.ConnectorCompoundHarmonicAnalysis)

        @property
        def coupling_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(_5916.CouplingCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5917,
            )

            return self._parent._cast(_5917.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5919,
            )

            return self._parent._cast(_5919.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def cvt_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5920,
            )

            return self._parent._cast(_5920.CVTCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5921,
            )

            return self._parent._cast(_5921.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def cycloidal_assembly_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.CycloidalAssemblyCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(
                _5923.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cycloidal_disc_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5924,
            )

            return self._parent._cast(_5924.CycloidalDiscCompoundHarmonicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5925,
            )

            return self._parent._cast(
                _5925.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5926,
            )

            return self._parent._cast(_5926.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5927,
            )

            return self._parent._cast(_5927.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.CylindricalGearSetCompoundHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5929,
            )

            return self._parent._cast(
                _5929.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def datum_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.DatumCompoundHarmonicAnalysis)

        @property
        def external_cad_model_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5931,
            )

            return self._parent._cast(_5931.ExternalCADModelCompoundHarmonicAnalysis)

        @property
        def face_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5932,
            )

            return self._parent._cast(_5932.FaceGearCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5934,
            )

            return self._parent._cast(_5934.FaceGearSetCompoundHarmonicAnalysis)

        @property
        def fe_part_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5935,
            )

            return self._parent._cast(_5935.FEPartCompoundHarmonicAnalysis)

        @property
        def flexible_pin_assembly_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5936,
            )

            return self._parent._cast(_5936.FlexiblePinAssemblyCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5937,
            )

            return self._parent._cast(_5937.GearCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.GearMeshCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.GearSetCompoundHarmonicAnalysis)

        @property
        def guide_dxf_model_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.GuideDxfModelCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(_5941.HypoidGearCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(_5942.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5943,
            )

            return self._parent._cast(_5943.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5944,
            )

            return self._parent._cast(
                _5944.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(
                _5945.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(
                _5947.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5948,
            )

            return self._parent._cast(
                _5948.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5949,
            )

            return self._parent._cast(
                _5949.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(
                _5950.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5951,
            )

            return self._parent._cast(
                _5951.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(
                _5952.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5953,
            )

            return self._parent._cast(
                _5953.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def mass_disc_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5954,
            )

            return self._parent._cast(_5954.MassDiscCompoundHarmonicAnalysis)

        @property
        def measurement_component_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(
                _5955.MeasurementComponentCompoundHarmonicAnalysis
            )

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.MountableComponentCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5957,
            )

            return self._parent._cast(_5957.OilSealCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5959,
            )

            return self._parent._cast(
                _5959.PartToPartShearCouplingCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(
                _5960.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5961,
            )

            return self._parent._cast(
                _5961.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def planetary_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5962,
            )

            return self._parent._cast(_5962.PlanetaryConnectionCompoundHarmonicAnalysis)

        @property
        def planetary_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5963,
            )

            return self._parent._cast(_5963.PlanetaryGearSetCompoundHarmonicAnalysis)

        @property
        def planet_carrier_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.PlanetCarrierCompoundHarmonicAnalysis)

        @property
        def point_load_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.PointLoadCompoundHarmonicAnalysis)

        @property
        def power_load_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PowerLoadCompoundHarmonicAnalysis)

        @property
        def pulley_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5967,
            )

            return self._parent._cast(_5967.PulleyCompoundHarmonicAnalysis)

        @property
        def ring_pins_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(_5968.RingPinsCompoundHarmonicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5969,
            )

            return self._parent._cast(
                _5969.RingPinsToDiscConnectionCompoundHarmonicAnalysis
            )

        @property
        def rolling_ring_assembly_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5970,
            )

            return self._parent._cast(_5970.RollingRingAssemblyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5971,
            )

            return self._parent._cast(_5971.RollingRingCompoundHarmonicAnalysis)

        @property
        def rolling_ring_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5972,
            )

            return self._parent._cast(
                _5972.RollingRingConnectionCompoundHarmonicAnalysis
            )

        @property
        def root_assembly_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5973,
            )

            return self._parent._cast(_5973.RootAssemblyCompoundHarmonicAnalysis)

        @property
        def shaft_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5974,
            )

            return self._parent._cast(_5974.ShaftCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5975,
            )

            return self._parent._cast(_5975.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5976,
            )

            return self._parent._cast(
                _5976.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5977,
            )

            return self._parent._cast(_5977.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5978,
            )

            return self._parent._cast(_5978.SpiralBevelGearCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5980,
            )

            return self._parent._cast(_5980.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def spring_damper_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5981,
            )

            return self._parent._cast(_5981.SpringDamperCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(
                _5982.SpringDamperConnectionCompoundHarmonicAnalysis
            )

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(_5983.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(
                _5984.StraightBevelDiffGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5985,
            )

            return self._parent._cast(
                _5985.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5986,
            )

            return self._parent._cast(
                _5986.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(_5987.StraightBevelGearCompoundHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(
                _5988.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5989,
            )

            return self._parent._cast(
                _5989.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5990,
            )

            return self._parent._cast(
                _5990.StraightBevelPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(
                _5991.StraightBevelSunGearCompoundHarmonicAnalysis
            )

        @property
        def synchroniser_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5992,
            )

            return self._parent._cast(_5992.SynchroniserCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(_5993.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5994,
            )

            return self._parent._cast(_5994.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5995,
            )

            return self._parent._cast(_5995.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(_5996.TorqueConverterCompoundHarmonicAnalysis)

        @property
        def torque_converter_connection_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(
                _5997.TorqueConverterConnectionCompoundHarmonicAnalysis
            )

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5998,
            )

            return self._parent._cast(_5998.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5999,
            )

            return self._parent._cast(
                _5999.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6000,
            )

            return self._parent._cast(_6000.UnbalancedMassCompoundHarmonicAnalysis)

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6001,
            )

            return self._parent._cast(_6001.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def worm_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.WormGearCompoundHarmonicAnalysis)

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6003,
            )

            return self._parent._cast(_6003.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def worm_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6004,
            )

            return self._parent._cast(_6004.WormGearSetCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6005,
            )

            return self._parent._cast(_6005.ZerolBevelGearCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6006,
            )

            return self._parent._cast(_6006.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6007,
            )

            return self._parent._cast(_6007.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6139,
            )

            return self._parent._cast(
                _6139.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6140,
            )

            return self._parent._cast(
                _6140.AbstractShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6141,
            )

            return self._parent._cast(
                _6141.AbstractShaftOrHousingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6142,
            )

            return self._parent._cast(
                _6142.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6143,
            )

            return self._parent._cast(
                _6143.AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6144,
            )

            return self._parent._cast(
                _6144.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6145,
            )

            return self._parent._cast(
                _6145.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def assembly_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6146,
            )

            return self._parent._cast(
                _6146.AssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6147,
            )

            return self._parent._cast(
                _6147.BearingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6148,
            )

            return self._parent._cast(
                _6148.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6149,
            )

            return self._parent._cast(
                _6149.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6150,
            )

            return self._parent._cast(
                _6150.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6151,
            )

            return self._parent._cast(
                _6151.BevelDifferentialGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6152,
            )

            return self._parent._cast(
                _6152.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6153,
            )

            return self._parent._cast(
                _6153.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6154,
            )

            return self._parent._cast(
                _6154.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6155,
            )

            return self._parent._cast(
                _6155.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6156,
            )

            return self._parent._cast(
                _6156.BevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6157,
            )

            return self._parent._cast(
                _6157.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolt_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6158,
            )

            return self._parent._cast(
                _6158.BoltCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bolted_joint_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6159,
            )

            return self._parent._cast(
                _6159.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6160,
            )

            return self._parent._cast(
                _6160.ClutchCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6161,
            )

            return self._parent._cast(
                _6161.ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def clutch_half_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6162,
            )

            return self._parent._cast(
                _6162.ClutchHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6164,
            )

            return self._parent._cast(
                _6164.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6165,
            )

            return self._parent._cast(
                _6165.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6167,
            )

            return self._parent._cast(
                _6167.ConceptCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6168,
            )

            return self._parent._cast(
                _6168.ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6169,
            )

            return self._parent._cast(
                _6169.ConceptGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6170,
            )

            return self._parent._cast(
                _6170.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6171,
            )

            return self._parent._cast(
                _6171.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6172,
            )

            return self._parent._cast(
                _6172.ConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6173,
            )

            return self._parent._cast(
                _6173.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6174,
            )

            return self._parent._cast(
                _6174.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6175,
            )

            return self._parent._cast(
                _6175.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.CouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6177,
            )

            return self._parent._cast(
                _6177.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6178,
            )

            return self._parent._cast(
                _6178.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6179,
            )

            return self._parent._cast(
                _6179.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6180,
            )

            return self._parent._cast(
                _6180.CVTCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6181,
            )

            return self._parent._cast(
                _6181.CVTPulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6182,
            )

            return self._parent._cast(
                _6182.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6183,
            )

            return self._parent._cast(
                _6183.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6184,
            )

            return self._parent._cast(
                _6184.CycloidalDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6186,
            )

            return self._parent._cast(
                _6186.CylindricalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6187,
            )

            return self._parent._cast(
                _6187.CylindricalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6188,
            )

            return self._parent._cast(
                _6188.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6189,
            )

            return self._parent._cast(
                _6189.CylindricalPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6190,
            )

            return self._parent._cast(
                _6190.DatumCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def external_cad_model_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6191,
            )

            return self._parent._cast(
                _6191.ExternalCADModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6192,
            )

            return self._parent._cast(
                _6192.FaceGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6193,
            )

            return self._parent._cast(
                _6193.FaceGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6194,
            )

            return self._parent._cast(
                _6194.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def fe_part_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6195,
            )

            return self._parent._cast(
                _6195.FEPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6196,
            )

            return self._parent._cast(
                _6196.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6197,
            )

            return self._parent._cast(
                _6197.GearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6198,
            )

            return self._parent._cast(
                _6198.GearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6199,
            )

            return self._parent._cast(
                _6199.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def guide_dxf_model_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6200,
            )

            return self._parent._cast(
                _6200.GuideDxfModelCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6201,
            )

            return self._parent._cast(
                _6201.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6202,
            )

            return self._parent._cast(
                _6202.HypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6203,
            )

            return self._parent._cast(
                _6203.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6204,
            )

            return self._parent._cast(
                _6204.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6205,
            )

            return self._parent._cast(
                _6205.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6206,
            )

            return self._parent._cast(
                _6206.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6207,
            )

            return self._parent._cast(
                _6207.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6208,
            )

            return self._parent._cast(
                _6208.KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6209,
            )

            return self._parent._cast(
                _6209.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6210,
            )

            return self._parent._cast(
                _6210.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6211,
            )

            return self._parent._cast(
                _6211.KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6212,
            )

            return self._parent._cast(
                _6212.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6213,
            )

            return self._parent._cast(
                _6213.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6214,
            )

            return self._parent._cast(
                _6214.MassDiscCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def measurement_component_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.MeasurementComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6216,
            )

            return self._parent._cast(
                _6216.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.OilSealCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6219,
            )

            return self._parent._cast(
                _6219.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.PartToPartShearCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6221,
            )

            return self._parent._cast(
                _6221.PartToPartShearCouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6223,
            )

            return self._parent._cast(
                _6223.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.PlanetCarrierCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6225,
            )

            return self._parent._cast(
                _6225.PointLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def power_load_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6226,
            )

            return self._parent._cast(
                _6226.PowerLoadCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def pulley_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6227,
            )

            return self._parent._cast(
                _6227.PulleyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6228,
            )

            return self._parent._cast(
                _6228.RingPinsCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6229,
            )

            return self._parent._cast(
                _6229.RingPinsToDiscConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6230,
            )

            return self._parent._cast(
                _6230.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6231,
            )

            return self._parent._cast(
                _6231.RollingRingCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6232,
            )

            return self._parent._cast(
                _6232.RollingRingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def root_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6233,
            )

            return self._parent._cast(
                _6233.RootAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6234,
            )

            return self._parent._cast(
                _6234.ShaftCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_hub_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6235,
            )

            return self._parent._cast(
                _6235.ShaftHubConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6237,
            )

            return self._parent._cast(
                _6237.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6238,
            )

            return self._parent._cast(
                _6238.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.SpiralBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6240,
            )

            return self._parent._cast(
                _6240.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6241,
            )

            return self._parent._cast(
                _6241.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.SpringDamperConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6243,
            )

            return self._parent._cast(
                _6243.SpringDamperHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6244,
            )

            return self._parent._cast(
                _6244.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6245,
            )

            return self._parent._cast(
                _6245.StraightBevelDiffGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6246,
            )

            return self._parent._cast(
                _6246.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6247,
            )

            return self._parent._cast(
                _6247.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6248,
            )

            return self._parent._cast(
                _6248.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6249,
            )

            return self._parent._cast(
                _6249.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6250,
            )

            return self._parent._cast(
                _6250.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6252,
            )

            return self._parent._cast(
                _6252.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6253,
            )

            return self._parent._cast(
                _6253.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6254,
            )

            return self._parent._cast(
                _6254.SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6256,
            )

            return self._parent._cast(
                _6256.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6257,
            )

            return self._parent._cast(
                _6257.TorqueConverterConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6258,
            )

            return self._parent._cast(
                _6258.TorqueConverterPumpCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6259,
            )

            return self._parent._cast(
                _6259.TorqueConverterTurbineCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6260,
            )

            return self._parent._cast(
                _6260.UnbalancedMassCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6261,
            )

            return self._parent._cast(
                _6261.VirtualComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6262,
            )

            return self._parent._cast(
                _6262.WormGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6263,
            )

            return self._parent._cast(
                _6263.WormGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6264,
            )

            return self._parent._cast(
                _6264.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6265,
            )

            return self._parent._cast(
                _6265.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6266,
            )

            return self._parent._cast(
                _6266.ZerolBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6267,
            )

            return self._parent._cast(
                _6267.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6408,
            )

            return self._parent._cast(_6408.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6409,
            )

            return self._parent._cast(_6409.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6410,
            )

            return self._parent._cast(
                _6410.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6411,
            )

            return self._parent._cast(
                _6411.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6412,
            )

            return self._parent._cast(
                _6412.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6413,
            )

            return self._parent._cast(
                _6413.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(
                _6414.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def assembly_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6415,
            )

            return self._parent._cast(_6415.AssemblyCompoundDynamicAnalysis)

        @property
        def bearing_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(_6416.BearingCompoundDynamicAnalysis)

        @property
        def belt_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6417,
            )

            return self._parent._cast(_6417.BeltConnectionCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(_6418.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6419,
            )

            return self._parent._cast(
                _6419.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6420,
            )

            return self._parent._cast(
                _6420.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(
                _6421.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6422,
            )

            return self._parent._cast(
                _6422.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6423,
            )

            return self._parent._cast(
                _6423.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(_6424.BevelGearCompoundDynamicAnalysis)

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6425,
            )

            return self._parent._cast(_6425.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolt_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6427,
            )

            return self._parent._cast(_6427.BoltCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6429,
            )

            return self._parent._cast(_6429.ClutchCompoundDynamicAnalysis)

        @property
        def clutch_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def clutch_half_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(_6431.ClutchHalfCompoundDynamicAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(_6432.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6433,
            )

            return self._parent._cast(_6433.ComponentCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(
                _6435.ConceptCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6436,
            )

            return self._parent._cast(_6436.ConceptCouplingHalfCompoundDynamicAnalysis)

        @property
        def concept_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6437,
            )

            return self._parent._cast(_6437.ConceptGearCompoundDynamicAnalysis)

        @property
        def concept_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(_6438.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(_6439.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6440,
            )

            return self._parent._cast(_6440.ConicalGearCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.ConnectionCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(_6444.ConnectorCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.CouplingCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(_6446.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CouplingHalfCompoundDynamicAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6448,
            )

            return self._parent._cast(_6448.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6449,
            )

            return self._parent._cast(_6449.CVTCompoundDynamicAnalysis)

        @property
        def cvt_pulley_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6450,
            )

            return self._parent._cast(_6450.CVTPulleyCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6452,
            )

            return self._parent._cast(
                _6452.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cycloidal_disc_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CycloidalDiscCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6454,
            )

            return self._parent._cast(
                _6454.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cylindrical_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(_6455.CylindricalGearCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6456,
            )

            return self._parent._cast(_6456.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6457,
            )

            return self._parent._cast(_6457.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def cylindrical_planet_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6458,
            )

            return self._parent._cast(
                _6458.CylindricalPlanetGearCompoundDynamicAnalysis
            )

        @property
        def datum_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.DatumCompoundDynamicAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6460,
            )

            return self._parent._cast(_6460.ExternalCADModelCompoundDynamicAnalysis)

        @property
        def face_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.FaceGearCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6462,
            )

            return self._parent._cast(_6462.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.FaceGearSetCompoundDynamicAnalysis)

        @property
        def fe_part_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.FEPartCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6465,
            )

            return self._parent._cast(_6465.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6466,
            )

            return self._parent._cast(_6466.GearCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.GearMeshCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.GearSetCompoundDynamicAnalysis)

        @property
        def guide_dxf_model_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.GuideDxfModelCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6470,
            )

            return self._parent._cast(_6470.HypoidGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6471,
            )

            return self._parent._cast(_6471.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(
                _6474.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6475,
            )

            return self._parent._cast(
                _6475.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6477,
            )

            return self._parent._cast(
                _6477.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6480,
            )

            return self._parent._cast(
                _6480.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6481,
            )

            return self._parent._cast(
                _6481.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(
                _6482.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def mass_disc_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6483,
            )

            return self._parent._cast(_6483.MassDiscCompoundDynamicAnalysis)

        @property
        def measurement_component_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.MeasurementComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(_6485.MountableComponentCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.OilSealCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PartCompoundDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(
                _6488.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(
                _6489.PartToPartShearCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6490,
            )

            return self._parent._cast(
                _6490.PartToPartShearCouplingHalfCompoundDynamicAnalysis
            )

        @property
        def planetary_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6491,
            )

            return self._parent._cast(_6491.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6492,
            )

            return self._parent._cast(_6492.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def planet_carrier_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.PlanetCarrierCompoundDynamicAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.PointLoadCompoundDynamicAnalysis)

        @property
        def power_load_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PowerLoadCompoundDynamicAnalysis)

        @property
        def pulley_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6496,
            )

            return self._parent._cast(_6496.PulleyCompoundDynamicAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(_6497.RingPinsCompoundDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(
                _6498.RingPinsToDiscConnectionCompoundDynamicAnalysis
            )

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(_6499.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def rolling_ring_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6500,
            )

            return self._parent._cast(_6500.RollingRingCompoundDynamicAnalysis)

        @property
        def rolling_ring_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(
                _6501.RollingRingConnectionCompoundDynamicAnalysis
            )

        @property
        def root_assembly_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(_6502.RootAssemblyCompoundDynamicAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6503,
            )

            return self._parent._cast(_6503.ShaftCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(_6504.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6505,
            )

            return self._parent._cast(
                _6505.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(_6507.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6508,
            )

            return self._parent._cast(_6508.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6510,
            )

            return self._parent._cast(_6510.SpringDamperCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(
                _6511.SpringDamperConnectionCompoundDynamicAnalysis
            )

        @property
        def spring_damper_half_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.SpringDamperHalfCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(
                _6513.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(
                _6514.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6516,
            )

            return self._parent._cast(_6516.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(
                _6517.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6519,
            )

            return self._parent._cast(
                _6519.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6520,
            )

            return self._parent._cast(_6520.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(_6521.SynchroniserCompoundDynamicAnalysis)

        @property
        def synchroniser_half_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6522,
            )

            return self._parent._cast(_6522.SynchroniserHalfCompoundDynamicAnalysis)

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6523,
            )

            return self._parent._cast(_6523.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(_6524.SynchroniserSleeveCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6525,
            )

            return self._parent._cast(_6525.TorqueConverterCompoundDynamicAnalysis)

        @property
        def torque_converter_connection_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6526,
            )

            return self._parent._cast(
                _6526.TorqueConverterConnectionCompoundDynamicAnalysis
            )

        @property
        def torque_converter_pump_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(_6527.TorqueConverterPumpCompoundDynamicAnalysis)

        @property
        def torque_converter_turbine_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6528,
            )

            return self._parent._cast(
                _6528.TorqueConverterTurbineCompoundDynamicAnalysis
            )

        @property
        def unbalanced_mass_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.UnbalancedMassCompoundDynamicAnalysis)

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6530,
            )

            return self._parent._cast(_6530.VirtualComponentCompoundDynamicAnalysis)

        @property
        def worm_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6531,
            )

            return self._parent._cast(_6531.WormGearCompoundDynamicAnalysis)

        @property
        def worm_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.WormGearMeshCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6533,
            )

            return self._parent._cast(_6533.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6534,
            )

            return self._parent._cast(_6534.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(_6535.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(_6536.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6675,
            )

            return self._parent._cast(
                _6675.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6676,
            )

            return self._parent._cast(_6676.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6677,
            )

            return self._parent._cast(
                _6677.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6678,
            )

            return self._parent._cast(
                _6678.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6679,
            )

            return self._parent._cast(
                _6679.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6680,
            )

            return self._parent._cast(
                _6680.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6681,
            )

            return self._parent._cast(
                _6681.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def assembly_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6682,
            )

            return self._parent._cast(_6682.AssemblyCompoundCriticalSpeedAnalysis)

        @property
        def bearing_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6683,
            )

            return self._parent._cast(_6683.BearingCompoundCriticalSpeedAnalysis)

        @property
        def belt_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6684,
            )

            return self._parent._cast(_6684.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6685,
            )

            return self._parent._cast(_6685.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6686,
            )

            return self._parent._cast(
                _6686.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(
                _6687.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6688,
            )

            return self._parent._cast(
                _6688.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(
                _6689.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(
                _6690.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6691,
            )

            return self._parent._cast(_6691.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6692,
            )

            return self._parent._cast(_6692.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6693,
            )

            return self._parent._cast(_6693.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def bolt_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(_6694.BoltCompoundCriticalSpeedAnalysis)

        @property
        def bolted_joint_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6695,
            )

            return self._parent._cast(_6695.BoltedJointCompoundCriticalSpeedAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6696,
            )

            return self._parent._cast(_6696.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6697,
            )

            return self._parent._cast(
                _6697.ClutchConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def clutch_half_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6698,
            )

            return self._parent._cast(_6698.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def coaxial_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6699,
            )

            return self._parent._cast(
                _6699.CoaxialConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6700,
            )

            return self._parent._cast(_6700.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.ConceptCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(
                _6702.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(
                _6703.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6704,
            )

            return self._parent._cast(_6704.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(
                _6705.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ConceptGearSetCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(_6707.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(
                _6708.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6711,
            )

            return self._parent._cast(_6711.ConnectorCompoundCriticalSpeedAnalysis)

        @property
        def coupling_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6712,
            )

            return self._parent._cast(_6712.CouplingCompoundCriticalSpeedAnalysis)

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6713,
            )

            return self._parent._cast(
                _6713.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(_6714.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6715,
            )

            return self._parent._cast(
                _6715.CVTBeltConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cvt_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6716,
            )

            return self._parent._cast(_6716.CVTCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6717,
            )

            return self._parent._cast(_6717.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_assembly_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6718,
            )

            return self._parent._cast(
                _6718.CycloidalAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6719,
            )

            return self._parent._cast(
                _6719.CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6720,
            )

            return self._parent._cast(_6720.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6721,
            )

            return self._parent._cast(
                _6721.CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(
                _6722.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6723,
            )

            return self._parent._cast(
                _6723.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6724,
            )

            return self._parent._cast(
                _6724.CylindricalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6725,
            )

            return self._parent._cast(
                _6725.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def datum_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.DatumCompoundCriticalSpeedAnalysis)

        @property
        def external_cad_model_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(
                _6727.ExternalCADModelCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(_6729.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def face_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.FaceGearSetCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def flexible_pin_assembly_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6732,
            )

            return self._parent._cast(
                _6732.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(_6733.GearCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(_6734.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.GuideDxfModelCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(_6737.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6738,
            )

            return self._parent._cast(_6738.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(_6739.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(
                _6741.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6742,
            )

            return self._parent._cast(
                _6742.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6743,
            )

            return self._parent._cast(
                _6743.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(
                _6744.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(
                _6745.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(
                _6746.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6747,
            )

            return self._parent._cast(
                _6747.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(
                _6749.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def mass_disc_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.MeasurementComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def oil_seal_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6755,
            )

            return self._parent._cast(
                _6755.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(
                _6756.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6757,
            )

            return self._parent._cast(
                _6757.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6758,
            )

            return self._parent._cast(
                _6758.PlanetaryConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def planetary_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6759,
            )

            return self._parent._cast(
                _6759.PlanetaryGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(_6760.PlanetCarrierCompoundCriticalSpeedAnalysis)

        @property
        def point_load_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(_6761.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(_6763.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6764,
            )

            return self._parent._cast(_6764.RingPinsCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6765,
            )

            return self._parent._cast(
                _6765.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_assembly_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6766,
            )

            return self._parent._cast(
                _6766.RollingRingAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(_6767.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6768,
            )

            return self._parent._cast(
                _6768.RollingRingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def root_assembly_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6769,
            )

            return self._parent._cast(_6769.RootAssemblyCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(_6770.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6771,
            )

            return self._parent._cast(
                _6771.ShaftHubConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(
                _6772.ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6773,
            )

            return self._parent._cast(
                _6773.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6774,
            )

            return self._parent._cast(
                _6774.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(
                _6775.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6776,
            )

            return self._parent._cast(
                _6776.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(_6777.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6778,
            )

            return self._parent._cast(
                _6778.SpringDamperConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(
                _6779.SpringDamperHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6783,
            )

            return self._parent._cast(
                _6783.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6784,
            )

            return self._parent._cast(
                _6784.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(
                _6785.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(_6788.SynchroniserCompoundCriticalSpeedAnalysis)

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(
                _6790.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(
                _6791.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6792,
            )

            return self._parent._cast(
                _6792.TorqueConverterCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_connection_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6793,
            )

            return self._parent._cast(
                _6793.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_pump_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.TorqueConverterPumpCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6795,
            )

            return self._parent._cast(
                _6795.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
            )

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(_6796.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(
                _6797.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(_6798.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(_6799.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def worm_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(_6800.WormGearSetCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6801,
            )

            return self._parent._cast(_6801.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(
                _6802.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(
                _6803.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7141,
            )

            return self._parent._cast(
                _7141.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7142,
            )

            return self._parent._cast(
                _7142.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7143,
            )

            return self._parent._cast(
                _7143.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7144,
            )

            return self._parent._cast(
                _7144.AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7145,
            )

            return self._parent._cast(
                _7145.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7146,
            )

            return self._parent._cast(
                _7146.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7147,
            )

            return self._parent._cast(
                _7147.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7148,
            )

            return self._parent._cast(
                _7148.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7149,
            )

            return self._parent._cast(
                _7149.BearingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7150,
            )

            return self._parent._cast(
                _7150.BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_drive_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7151,
            )

            return self._parent._cast(
                _7151.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7152,
            )

            return self._parent._cast(
                _7152.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7153,
            )

            return self._parent._cast(
                _7153.BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7154,
            )

            return self._parent._cast(
                _7154.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7155,
            )

            return self._parent._cast(
                _7155.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7156,
            )

            return self._parent._cast(
                _7156.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7157,
            )

            return self._parent._cast(
                _7157.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7158,
            )

            return self._parent._cast(
                _7158.BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7159,
            )

            return self._parent._cast(
                _7159.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7160,
            )

            return self._parent._cast(
                _7160.BoltCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bolted_joint_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7161,
            )

            return self._parent._cast(
                _7161.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7162,
            )

            return self._parent._cast(
                _7162.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7163,
            )

            return self._parent._cast(
                _7163.ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7164,
            )

            return self._parent._cast(
                _7164.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7165,
            )

            return self._parent._cast(
                _7165.CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7167,
            )

            return self._parent._cast(
                _7167.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7168,
            )

            return self._parent._cast(
                _7168.ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7169,
            )

            return self._parent._cast(
                _7169.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7170,
            )

            return self._parent._cast(
                _7170.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7172,
            )

            return self._parent._cast(
                _7172.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7173,
            )

            return self._parent._cast(
                _7173.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7174,
            )

            return self._parent._cast(
                _7174.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7175,
            )

            return self._parent._cast(
                _7175.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7176,
            )

            return self._parent._cast(
                _7176.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7177,
            )

            return self._parent._cast(
                _7177.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7178,
            )

            return self._parent._cast(
                _7178.CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7179,
            )

            return self._parent._cast(
                _7179.CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7181,
            )

            return self._parent._cast(
                _7181.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7182,
            )

            return self._parent._cast(
                _7182.CVTCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7183,
            )

            return self._parent._cast(
                _7183.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7185,
            )

            return self._parent._cast(
                _7185.CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7186,
            )

            return self._parent._cast(
                _7186.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7187,
            )

            return self._parent._cast(
                _7187.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7188,
            )

            return self._parent._cast(
                _7188.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7189,
            )

            return self._parent._cast(
                _7189.CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7190,
            )

            return self._parent._cast(
                _7190.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7191,
            )

            return self._parent._cast(
                _7191.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def datum_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.DatumCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def external_cad_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7193,
            )

            return self._parent._cast(
                _7193.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7194,
            )

            return self._parent._cast(
                _7194.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7195,
            )

            return self._parent._cast(
                _7195.FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7196,
            )

            return self._parent._cast(
                _7196.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def fe_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7197,
            )

            return self._parent._cast(
                _7197.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def flexible_pin_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7198,
            )

            return self._parent._cast(
                _7198.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7199,
            )

            return self._parent._cast(
                _7199.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7200,
            )

            return self._parent._cast(
                _7200.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def guide_dxf_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7202,
            )

            return self._parent._cast(
                _7202.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7203,
            )

            return self._parent._cast(
                _7203.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7204,
            )

            return self._parent._cast(
                _7204.HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7205,
            )

            return self._parent._cast(
                _7205.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7206,
            )

            return self._parent._cast(
                _7206.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7207,
            )

            return self._parent._cast(
                _7207.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7209,
            )

            return self._parent._cast(
                _7209.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7210,
            )

            return self._parent._cast(
                _7210.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7211,
            )

            return self._parent._cast(
                _7211.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7212,
            )

            return self._parent._cast(
                _7212.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7213,
            )

            return self._parent._cast(
                _7213.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7214,
            )

            return self._parent._cast(
                _7214.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7215,
            )

            return self._parent._cast(
                _7215.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7216,
            )

            return self._parent._cast(
                _7216.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7217,
            )

            return self._parent._cast(
                _7217.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7218,
            )

            return self._parent._cast(
                _7218.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7223,
            )

            return self._parent._cast(
                _7223.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7224,
            )

            return self._parent._cast(
                _7224.PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7225,
            )

            return self._parent._cast(
                _7225.PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7226,
            )

            return self._parent._cast(
                _7226.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7230,
            )

            return self._parent._cast(
                _7230.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7231,
            )

            return self._parent._cast(
                _7231.RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7232,
            )

            return self._parent._cast(
                _7232.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7233,
            )

            return self._parent._cast(
                _7233.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7234,
            )

            return self._parent._cast(
                _7234.RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7235,
            )

            return self._parent._cast(
                _7235.RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7236,
            )

            return self._parent._cast(
                _7236.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7237,
            )

            return self._parent._cast(
                _7237.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7238,
            )

            return self._parent._cast(
                _7238.ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7239,
            )

            return self._parent._cast(
                _7239.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7240,
            )

            return self._parent._cast(
                _7240.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7241,
            )

            return self._parent._cast(
                _7241.SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7242,
            )

            return self._parent._cast(
                _7242.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7243,
            )

            return self._parent._cast(
                _7243.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7245,
            )

            return self._parent._cast(
                _7245.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7246,
            )

            return self._parent._cast(
                _7246.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7248,
            )

            return self._parent._cast(
                _7248.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7249,
            )

            return self._parent._cast(
                _7249.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7250,
            )

            return self._parent._cast(
                _7250.StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7251,
            )

            return self._parent._cast(
                _7251.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7252,
            )

            return self._parent._cast(
                _7252.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7253,
            )

            return self._parent._cast(
                _7253.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7255,
            )

            return self._parent._cast(
                _7255.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7256,
            )

            return self._parent._cast(
                _7256.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7258,
            )

            return self._parent._cast(
                _7258.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7260,
            )

            return self._parent._cast(
                _7260.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7261,
            )

            return self._parent._cast(
                _7261.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7263,
            )

            return self._parent._cast(
                _7263.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7264,
            )

            return self._parent._cast(
                _7264.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7266,
            )

            return self._parent._cast(
                _7266.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7267,
            )

            return self._parent._cast(
                _7267.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7268,
            )

            return self._parent._cast(
                _7268.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7269,
            )

            return self._parent._cast(
                _7269.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7406,
            )

            return self._parent._cast(
                _7406.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7407,
            )

            return self._parent._cast(
                _7407.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7409,
            )

            return self._parent._cast(
                _7409.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7410,
            )

            return self._parent._cast(
                _7410.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7411,
            )

            return self._parent._cast(
                _7411.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7412,
            )

            return self._parent._cast(
                _7412.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def assembly_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7413,
            )

            return self._parent._cast(_7413.AssemblyCompoundAdvancedSystemDeflection)

        @property
        def bearing_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(_7414.BearingCompoundAdvancedSystemDeflection)

        @property
        def belt_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(
                _7415.BeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7416,
            )

            return self._parent._cast(_7416.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7417,
            )

            return self._parent._cast(
                _7417.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(
                _7418.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7419,
            )

            return self._parent._cast(
                _7419.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(
                _7421.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(_7422.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7423,
            )

            return self._parent._cast(
                _7423.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7424,
            )

            return self._parent._cast(
                _7424.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bolt_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7425,
            )

            return self._parent._cast(_7425.BoltCompoundAdvancedSystemDeflection)

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(_7426.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(_7427.ClutchCompoundAdvancedSystemDeflection)

        @property
        def clutch_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(
                _7428.ClutchConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(_7429.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def coaxial_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(
                _7430.CoaxialConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ComponentCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(
                _7433.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(
                _7434.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7435,
            )

            return self._parent._cast(_7435.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConceptGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7437,
            )

            return self._parent._cast(
                _7437.ConceptGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(_7438.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(
                _7440.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(_7441.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connector_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(_7442.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(_7443.CouplingCompoundAdvancedSystemDeflection)

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7444,
            )

            return self._parent._cast(
                _7444.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(
                _7445.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7446,
            )

            return self._parent._cast(
                _7446.CVTBeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7447,
            )

            return self._parent._cast(_7447.CVTCompoundAdvancedSystemDeflection)

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7448,
            )

            return self._parent._cast(_7448.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(
                _7449.CycloidalAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7450,
            )

            return self._parent._cast(
                _7450.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7452,
            )

            return self._parent._cast(
                _7452.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7453,
            )

            return self._parent._cast(
                _7453.CylindricalGearCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7454,
            )

            return self._parent._cast(
                _7454.CylindricalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7455,
            )

            return self._parent._cast(
                _7455.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7456,
            )

            return self._parent._cast(
                _7456.CylindricalPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def datum_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7458,
            )

            return self._parent._cast(
                _7458.ExternalCADModelCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(_7459.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def face_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(
                _7460.FaceGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(_7461.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.FEPartCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(
                _7463.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.GearCompoundAdvancedSystemDeflection)

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(_7465.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(_7466.GearSetCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(
                _7467.GuideDxfModelCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(_7468.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(
                _7469.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(
                _7470.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(
                _7472.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(
                _7473.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7474,
            )

            return self._parent._cast(
                _7474.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7475,
            )

            return self._parent._cast(
                _7475.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7477,
            )

            return self._parent._cast(
                _7477.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7478,
            )

            return self._parent._cast(
                _7478.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(
                _7480.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(_7481.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(_7484.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(
                _7486.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(
                _7487.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7489,
            )

            return self._parent._cast(
                _7489.PlanetaryConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(
                _7490.PlanetaryGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def planet_carrier_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(
                _7491.PlanetCarrierCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(_7492.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(_7494.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7495,
            )

            return self._parent._cast(_7495.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_to_disc_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7497,
            )

            return self._parent._cast(
                _7497.RollingRingAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7498,
            )

            return self._parent._cast(_7498.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.RollingRingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def root_assembly_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7500,
            )

            return self._parent._cast(
                _7500.RootAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7501,
            )

            return self._parent._cast(_7501.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(
                _7502.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(
                _7505.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7507,
            )

            return self._parent._cast(
                _7507.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7508,
            )

            return self._parent._cast(
                _7508.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.SpringDamperConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(
                _7511.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(
                _7513.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(
                _7514.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7517,
            )

            return self._parent._cast(
                _7517.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(
                _7519.SynchroniserCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(
                _7522.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.TorqueConverterConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7526,
            )

            return self._parent._cast(
                _7526.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7529,
            )

            return self._parent._cast(_7529.WormGearCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.WormGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7531,
            )

            return self._parent._cast(_7531.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7532,
            )

            return self._parent._cast(
                _7532.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(
                _7533.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def part_compound_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
        ) -> "DesignEntityCompoundAnalysis":
            return self._parent

        def __getattr__(
            self: "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignEntityCompoundAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AnalysisTime

        if temp is None:
            return 0.0

        return temp

    @analysis_time.setter
    @enforce_parameter_types
    def analysis_time(self: Self, value: "float"):
        self.wrapped.AnalysisTime = float(value) if value is not None else 0.0

    @property
    def real_name_in_context_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RealNameInContextName

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "DesignEntityCompoundAnalysis._Cast_DesignEntityCompoundAnalysis":
        return self._Cast_DesignEntityCompoundAnalysis(self)

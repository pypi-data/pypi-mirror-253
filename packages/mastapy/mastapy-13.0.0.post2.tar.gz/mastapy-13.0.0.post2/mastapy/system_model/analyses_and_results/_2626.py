"""DynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2620
from mastapy._internal.cast_exception import CastException

_SPRING_DAMPER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperConnectionLoadCase",
)
_TORQUE_CONVERTER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterConnectionLoadCase",
)
_WORM_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearLoadCase"
)
_WORM_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearSetLoadCase"
)
_ZEROL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ZerolBevelGearLoadCase"
)
_ZEROL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ZerolBevelGearSetLoadCase",
)
_CYCLOIDAL_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalAssemblyLoadCase",
)
_CYCLOIDAL_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CycloidalDiscLoadCase"
)
_RING_PINS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RingPinsLoadCase"
)
_PART_TO_PART_SHEAR_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingLoadCase",
)
_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingHalfLoadCase",
)
_BELT_DRIVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BeltDriveLoadCase"
)
_CLUTCH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchLoadCase"
)
_CLUTCH_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchHalfLoadCase"
)
_CONCEPT_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptCouplingLoadCase"
)
_CONCEPT_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingHalfLoadCase",
)
_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingLoadCase"
)
_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingHalfLoadCase"
)
_CVT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTLoadCase"
)
_CVT_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTPulleyLoadCase"
)
_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PulleyLoadCase"
)
_SHAFT_HUB_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftHubConnectionLoadCase",
)
_ROLLING_RING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RollingRingLoadCase"
)
_ROLLING_RING_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingAssemblyLoadCase",
)
_SPRING_DAMPER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpringDamperLoadCase"
)
_SPRING_DAMPER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperHalfLoadCase",
)
_SYNCHRONISER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SynchroniserLoadCase"
)
_SYNCHRONISER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserHalfLoadCase",
)
_SYNCHRONISER_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserPartLoadCase",
)
_SYNCHRONISER_SLEEVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserSleeveLoadCase",
)
_TORQUE_CONVERTER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "TorqueConverterLoadCase"
)
_TORQUE_CONVERTER_PUMP_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterPumpLoadCase",
)
_TORQUE_CONVERTER_TURBINE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterTurbineLoadCase",
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftToMountableComponentConnectionLoadCase",
)
_CVT_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CVTBeltConnectionLoadCase",
)
_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BeltConnectionLoadCase"
)
_COAXIAL_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CoaxialConnectionLoadCase",
)
_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectionLoadCase"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "InterMountableComponentConnectionLoadCase",
)
_PLANETARY_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryConnectionLoadCase",
)
_ROLLING_RING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingConnectionLoadCase",
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftToMountableComponentConnectionLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearMeshLoadCase",
)
_CONCEPT_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearMeshLoadCase"
)
_FACE_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearMeshLoadCase"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearMeshLoadCase",
)
_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearMeshLoadCase"
)
_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearMeshLoadCase"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearMeshLoadCase",
)
_CYLINDRICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearMeshLoadCase",
)
_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearMeshLoadCase"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
)
_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearMeshLoadCase",
)
_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearMeshLoadCase",
)
_WORM_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearMeshLoadCase"
)
_ZEROL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ZerolBevelGearMeshLoadCase",
)
_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearMeshLoadCase"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscCentralBearingConnectionLoadCase",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
)
_RING_PINS_TO_DISC_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RingPinsToDiscConnectionLoadCase",
)
_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingConnectionLoadCase",
)
_CLUTCH_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ClutchConnectionLoadCase",
)
_CONCEPT_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingConnectionLoadCase",
)
_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CouplingConnectionLoadCase",
)
_ABSTRACT_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "AbstractShaftLoadCase"
)
_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractAssemblyLoadCase",
)
_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftOrHousingLoadCase",
)
_BEARING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BearingLoadCase"
)
_BOLT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltLoadCase"
)
_BOLTED_JOINT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltedJointLoadCase"
)
_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ComponentLoadCase"
)
_CONNECTOR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectorLoadCase"
)
_DATUM_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "DatumLoadCase"
)
_EXTERNAL_CAD_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ExternalCADModelLoadCase",
)
_FE_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FEPartLoadCase"
)
_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "FlexiblePinAssemblyLoadCase",
)
_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "AssemblyLoadCase"
)
_GUIDE_DXF_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GuideDxfModelLoadCase"
)
_MASS_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "MassDiscLoadCase"
)
_MEASUREMENT_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MeasurementComponentLoadCase",
)
_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MountableComponentLoadCase",
)
_OIL_SEAL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "OilSealLoadCase"
)
_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)
_PLANET_CARRIER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PlanetCarrierLoadCase"
)
_POINT_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PointLoadLoadCase"
)
_POWER_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PowerLoadLoadCase"
)
_ROOT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RootAssemblyLoadCase"
)
_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpecialisedAssemblyLoadCase",
)
_UNBALANCED_MASS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "UnbalancedMassLoadCase"
)
_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "VirtualComponentLoadCase",
)
_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ShaftLoadCase"
)
_CONCEPT_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearLoadCase"
)
_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearSetLoadCase"
)
_FACE_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearLoadCase"
)
_FACE_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearSetLoadCase"
)
_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearLoadCase",
)
_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearSetLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearSetLoadCase",
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialPlanetGearLoadCase",
)
_BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialSunGearLoadCase",
)
_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearLoadCase"
)
_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearSetLoadCase"
)
_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearLoadCase"
)
_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearSetLoadCase"
)
_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CylindricalGearLoadCase"
)
_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearSetLoadCase",
)
_CYLINDRICAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalPlanetGearLoadCase",
)
_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearLoadCase"
)
_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearSetLoadCase"
)
_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearLoadCase"
)
_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearSetLoadCase"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
)
_PLANETARY_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryGearSetLoadCase",
)
_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpiralBevelGearLoadCase"
)
_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearSetLoadCase",
)
_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearLoadCase",
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearSetLoadCase",
)
_STRAIGHT_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearLoadCase",
)
_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearSetLoadCase",
)
_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelPlanetGearLoadCase",
)
_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelSunGearLoadCase",
)
_TORQUE_CONVERTER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "TorqueConverterConnection",
)
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "PartToPartShearCouplingConnection",
)
_CLUTCH_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "ClutchConnection"
)
_CONCEPT_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "ConceptCouplingConnection",
)
_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingConnection"
)
_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
)
_WORM_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
)
_ZEROL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGear"
)
_ZEROL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGearSet"
)
_CONCEPT_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGear"
)
_CONCEPT_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGearSet"
)
_FACE_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGear")
_FACE_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGearSet"
)
_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)
_BEVEL_DIFFERENTIAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGear"
)
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGearSet"
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialPlanetGear"
)
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
)
_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")
_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
)
_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)
_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)
_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGear"
)
_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGearSet"
)
_CYLINDRICAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalPlanetGear"
)
_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "Gear")
_GEAR_SET = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSet")
_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
)
_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGear"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGear"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGear",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
)
_PLANETARY_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "PlanetaryGearSet"
)
_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGear"
)
_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGearSet"
)
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGear"
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)
_STRAIGHT_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGear"
)
_STRAIGHT_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGearSet"
)
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
)
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelSunGear"
)
_WORM_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGear")
_CYCLOIDAL_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalAssembly"
)
_CYCLOIDAL_DISC = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalDisc"
)
_RING_PINS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "RingPins"
)
_PART_TO_PART_SHEAR_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCoupling"
)
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCouplingHalf"
)
_BELT_DRIVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "BeltDrive"
)
_CLUTCH = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Clutch")
_CLUTCH_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchHalf"
)
_CONCEPT_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCoupling"
)
_CONCEPT_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCouplingHalf"
)
_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Coupling"
)
_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)
_CVT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVT")
_CVT_PULLEY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVTPulley"
)
_PULLEY = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Pulley")
_SHAFT_HUB_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ShaftHubConnection"
)
_ROLLING_RING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRing"
)
_ROLLING_RING_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRingAssembly"
)
_SPRING_DAMPER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamper"
)
_SPRING_DAMPER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamperHalf"
)
_SYNCHRONISER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Synchroniser"
)
_SYNCHRONISER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserHalf"
)
_SYNCHRONISER_PART = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
)
_SYNCHRONISER_SLEEVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserSleeve"
)
_TORQUE_CONVERTER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverter"
)
_TORQUE_CONVERTER_PUMP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterPump"
)
_TORQUE_CONVERTER_TURBINE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterTurbine"
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "ShaftToMountableComponentConnection",
)
_CVT_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTBeltConnection"
)
_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BeltConnection"
)
_COAXIAL_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CoaxialConnection"
)
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)
_PLANETARY_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PlanetaryConnection"
)
_ROLLING_RING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "RollingRingConnection"
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "AbstractShaftToMountableComponentConnection",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelDifferentialGearMesh"
)
_CONCEPT_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConceptGearMesh"
)
_FACE_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "FaceGearMesh"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelDiffGearMesh"
)
_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearMesh"
)
_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)
_CYLINDRICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "CylindricalGearMesh"
)
_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearMesh"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidConicalGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidHypoidGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
)
_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "SpiralBevelGearMesh"
)
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelGearMesh"
)
_WORM_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "WormGearMesh"
)
_ZEROL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearMesh"
)
_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearMesh"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscCentralBearingConnection",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscPlanetaryBearingConnection",
)
_RING_PINS_TO_DISC_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "RingPinsToDiscConnection",
)
_ABSTRACT_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaft"
)
_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaftOrHousing"
)
_BEARING = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bearing")
_BOLT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bolt")
_BOLTED_JOINT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "BoltedJoint")
_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_CONNECTOR = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Connector")
_DATUM = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Datum")
_EXTERNAL_CAD_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "ExternalCADModel"
)
_FE_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "FEPart")
_FLEXIBLE_PIN_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "FlexiblePinAssembly"
)
_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Assembly")
_GUIDE_DXF_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "GuideDxfModel"
)
_MASS_DISC = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "MassDisc")
_MEASUREMENT_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MeasurementComponent"
)
_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)
_OIL_SEAL = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "OilSeal")
_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")
_PLANET_CARRIER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "PlanetCarrier"
)
_POINT_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PointLoad")
_POWER_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PowerLoad")
_ROOT_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "RootAssembly")
_SPECIALISED_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
)
_UNBALANCED_MASS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMass"
)
_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)
_SHAFT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.ShaftModel", "Shaft")
_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "DynamicAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6956,
        _6972,
        _6982,
        _6984,
        _6985,
        _6987,
        _6857,
        _6859,
        _6943,
        _6931,
        _6930,
        _6821,
        _6834,
        _6833,
        _6840,
        _6839,
        _6853,
        _6852,
        _6855,
        _6856,
        _6940,
        _6949,
        _6947,
        _6945,
        _6958,
        _6957,
        _6968,
        _6967,
        _6969,
        _6970,
        _6973,
        _6974,
        _6975,
        _6951,
        _6854,
        _6820,
        _6836,
        _6849,
        _6911,
        _6932,
        _6946,
        _6809,
        _6823,
        _6842,
        _6885,
        _6960,
        _6828,
        _6846,
        _6814,
        _6863,
        _6906,
        _6913,
        _6916,
        _6919,
        _6954,
        _6963,
        _6983,
        _6986,
        _6892,
        _6858,
        _6860,
        _6944,
        _6929,
        _6832,
        _6838,
        _6851,
        _6807,
        _6806,
        _6808,
        _6819,
        _6831,
        _6830,
        _6837,
        _6850,
        _6869,
        _6883,
        _6887,
        _6888,
        _6818,
        _6896,
        _6921,
        _6922,
        _6924,
        _6926,
        _6928,
        _6935,
        _6938,
        _6939,
        _6948,
        _6952,
        _6980,
        _6981,
        _6950,
        _6841,
        _6843,
        _6884,
        _6886,
        _6813,
        _6815,
        _6822,
        _6824,
        _6825,
        _6826,
        _6827,
        _6829,
        _6844,
        _6848,
        _6861,
        _6865,
        _6866,
        _6890,
        _6895,
        _6905,
        _6907,
        _6912,
        _6914,
        _6915,
        _6917,
        _6918,
        _6920,
        _6933,
        _6953,
        _6955,
        _6959,
        _6961,
        _6962,
        _6964,
        _6965,
        _6966,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6380,
        _6395,
        _6401,
        _6403,
        _6404,
        _6406,
        _6319,
        _6321,
        _6367,
        _6359,
        _6360,
        _6286,
        _6298,
        _6299,
        _6303,
        _6304,
        _6314,
        _6315,
        _6317,
        _6318,
        _6366,
        _6374,
        _6371,
        _6369,
        _6381,
        _6382,
        _6391,
        _6392,
        _6393,
        _6394,
        _6396,
        _6397,
        _6398,
        _6375,
        _6316,
        _6285,
        _6300,
        _6311,
        _6343,
        _6361,
        _6370,
        _6279,
        _6288,
        _6306,
        _6332,
        _6384,
        _6293,
        _6309,
        _6281,
        _6324,
        _6341,
        _6345,
        _6348,
        _6351,
        _6378,
        _6387,
        _6402,
        _6405,
        _6337,
        _6320,
        _6322,
        _6368,
        _6358,
        _6297,
        _6302,
        _6313,
        _6277,
        _6276,
        _6278,
        _6284,
        _6295,
        _6296,
        _6301,
        _6312,
        _6327,
        _6330,
        _6334,
        _6335,
        _6283,
        _6339,
        _6353,
        _6354,
        _6355,
        _6356,
        _6357,
        _6363,
        _6364,
        _6365,
        _6372,
        _6376,
        _6399,
        _6400,
        _6373,
        _6305,
        _6307,
        _6331,
        _6333,
        _6280,
        _6282,
        _6287,
        _6289,
        _6290,
        _6291,
        _6292,
        _6294,
        _6308,
        _6310,
        _6323,
        _6325,
        _6326,
        _6336,
        _6338,
        _6340,
        _6342,
        _6344,
        _6346,
        _6347,
        _6349,
        _6350,
        _6352,
        _6362,
        _6377,
        _6379,
        _6383,
        _6385,
        _6386,
        _6388,
        _6389,
        _6390,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2352,
        _2348,
        _2342,
        _2344,
        _2346,
        _2350,
    )
    from mastapy.system_model.part_model.gears import (
        _2552,
        _2553,
        _2554,
        _2521,
        _2522,
        _2528,
        _2529,
        _2513,
        _2514,
        _2515,
        _2516,
        _2517,
        _2518,
        _2519,
        _2520,
        _2523,
        _2524,
        _2525,
        _2526,
        _2527,
        _2530,
        _2532,
        _2534,
        _2535,
        _2536,
        _2537,
        _2538,
        _2539,
        _2540,
        _2541,
        _2542,
        _2543,
        _2544,
        _2545,
        _2546,
        _2547,
        _2548,
        _2549,
        _2550,
        _2551,
    )
    from mastapy.system_model.part_model.cycloidal import _2568, _2569, _2570
    from mastapy.system_model.part_model.couplings import (
        _2588,
        _2589,
        _2576,
        _2578,
        _2579,
        _2581,
        _2582,
        _2583,
        _2584,
        _2586,
        _2587,
        _2590,
        _2598,
        _2596,
        _2597,
        _2600,
        _2601,
        _2602,
        _2604,
        _2605,
        _2606,
        _2607,
        _2608,
        _2610,
    )
    from mastapy.system_model.connections_and_sockets import (
        _2295,
        _2273,
        _2268,
        _2269,
        _2272,
        _2281,
        _2287,
        _2292,
        _2265,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2301,
        _2305,
        _2311,
        _2325,
        _2303,
        _2307,
        _2299,
        _2309,
        _2315,
        _2318,
        _2319,
        _2320,
        _2323,
        _2327,
        _2329,
        _2331,
        _2313,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2335,
        _2338,
        _2341,
    )
    from mastapy.system_model.part_model import (
        _2435,
        _2434,
        _2436,
        _2439,
        _2442,
        _2443,
        _2444,
        _2447,
        _2448,
        _2452,
        _2453,
        _2454,
        _2433,
        _2455,
        _2462,
        _2463,
        _2464,
        _2466,
        _2468,
        _2469,
        _2471,
        _2472,
        _2474,
        _2476,
        _2477,
        _2479,
    )
    from mastapy.system_model.part_model.shaft_model import _2482


__docformat__ = "restructuredtext en"
__all__ = ("DynamicAnalysis",)


Self = TypeVar("Self", bound="DynamicAnalysis")


class DynamicAnalysis(_2620.SingleAnalysis):
    """DynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicAnalysis")

    class _Cast_DynamicAnalysis:
        """Special nested class for casting DynamicAnalysis to subclasses."""

        def __init__(
            self: "DynamicAnalysis._Cast_DynamicAnalysis", parent: "DynamicAnalysis"
        ):
            self._parent = parent

        @property
        def single_analysis(self: "DynamicAnalysis._Cast_DynamicAnalysis"):
            return self._parent._cast(_2620.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ):
            from mastapy import _7552

            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def dynamic_analysis(
            self: "DynamicAnalysis._Cast_DynamicAnalysis",
        ) -> "DynamicAnalysis":
            return self._parent

        def __getattr__(self: "DynamicAnalysis._Cast_DynamicAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def results_for_spring_damper_connection_load_case(
        self: Self, design_entity_analysis: "_6956.SpringDamperConnectionLoadCase"
    ) -> "_6380.SpringDamperConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPRING_DAMPER_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection(
        self: Self, design_entity: "_2352.TorqueConverterConnection"
    ) -> "_6395.TorqueConverterConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection_load_case(
        self: Self, design_entity_analysis: "_6972.TorqueConverterConnectionLoadCase"
    ) -> "_6395.TorqueConverterConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _TORQUE_CONVERTER_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_load_case(
        self: Self, design_entity_analysis: "_6982.WormGearLoadCase"
    ) -> "_6401.WormGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_set(
        self: Self, design_entity: "_2552.WormGearSet"
    ) -> "_6403.WormGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_set_load_case(
        self: Self, design_entity_analysis: "_6984.WormGearSetLoadCase"
    ) -> "_6403.WormGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear(
        self: Self, design_entity: "_2553.ZerolBevelGear"
    ) -> "_6404.ZerolBevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_load_case(
        self: Self, design_entity_analysis: "_6985.ZerolBevelGearLoadCase"
    ) -> "_6404.ZerolBevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set(
        self: Self, design_entity: "_2554.ZerolBevelGearSet"
    ) -> "_6406.ZerolBevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set_load_case(
        self: Self, design_entity_analysis: "_6987.ZerolBevelGearSetLoadCase"
    ) -> "_6406.ZerolBevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ZEROL_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly(
        self: Self, design_entity: "_2568.CycloidalAssembly"
    ) -> "_6319.CycloidalAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalAssemblyDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly_load_case(
        self: Self, design_entity_analysis: "_6857.CycloidalAssemblyLoadCase"
    ) -> "_6319.CycloidalAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalAssemblyDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc(
        self: Self, design_entity: "_2569.CycloidalDisc"
    ) -> "_6321.CycloidalDiscDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_load_case(
        self: Self, design_entity_analysis: "_6859.CycloidalDiscLoadCase"
    ) -> "_6321.CycloidalDiscDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYCLOIDAL_DISC_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins(
        self: Self, design_entity: "_2570.RingPins"
    ) -> "_6367.RingPinsDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RingPinsDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_load_case(
        self: Self, design_entity_analysis: "_6943.RingPinsLoadCase"
    ) -> "_6367.RingPinsDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RingPinsDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_RING_PINS_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling(
        self: Self, design_entity: "_2588.PartToPartShearCoupling"
    ) -> "_6359.PartToPartShearCouplingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_load_case(
        self: Self, design_entity_analysis: "_6931.PartToPartShearCouplingLoadCase"
    ) -> "_6359.PartToPartShearCouplingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half(
        self: Self, design_entity: "_2589.PartToPartShearCouplingHalf"
    ) -> "_6360.PartToPartShearCouplingHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingHalfDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_HALF
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half_load_case(
        self: Self, design_entity_analysis: "_6930.PartToPartShearCouplingHalfLoadCase"
    ) -> "_6360.PartToPartShearCouplingHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingHalfDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_drive(
        self: Self, design_entity: "_2576.BeltDrive"
    ) -> "_6286.BeltDriveDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BeltDriveDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_drive_load_case(
        self: Self, design_entity_analysis: "_6821.BeltDriveLoadCase"
    ) -> "_6286.BeltDriveDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BeltDriveDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch(
        self: Self, design_entity: "_2578.Clutch"
    ) -> "_6298.ClutchDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_load_case(
        self: Self, design_entity_analysis: "_6834.ClutchLoadCase"
    ) -> "_6298.ClutchDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_half(
        self: Self, design_entity: "_2579.ClutchHalf"
    ) -> "_6299.ClutchHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchHalfDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_half_load_case(
        self: Self, design_entity_analysis: "_6833.ClutchHalfLoadCase"
    ) -> "_6299.ClutchHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchHalfDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling(
        self: Self, design_entity: "_2581.ConceptCoupling"
    ) -> "_6303.ConceptCouplingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_load_case(
        self: Self, design_entity_analysis: "_6840.ConceptCouplingLoadCase"
    ) -> "_6303.ConceptCouplingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half(
        self: Self, design_entity: "_2582.ConceptCouplingHalf"
    ) -> "_6304.ConceptCouplingHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingHalfDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half_load_case(
        self: Self, design_entity_analysis: "_6839.ConceptCouplingHalfLoadCase"
    ) -> "_6304.ConceptCouplingHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingHalfDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CONCEPT_COUPLING_HALF_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling(
        self: Self, design_entity: "_2583.Coupling"
    ) -> "_6314.CouplingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_load_case(
        self: Self, design_entity_analysis: "_6853.CouplingLoadCase"
    ) -> "_6314.CouplingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_half(
        self: Self, design_entity: "_2584.CouplingHalf"
    ) -> "_6315.CouplingHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_half_load_case(
        self: Self, design_entity_analysis: "_6852.CouplingHalfLoadCase"
    ) -> "_6315.CouplingHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt(
        self: Self, design_entity: "_2586.CVT"
    ) -> "_6317.CVTDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CVTDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_load_case(
        self: Self, design_entity_analysis: "_6855.CVTLoadCase"
    ) -> "_6317.CVTDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CVTDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_pulley(
        self: Self, design_entity: "_2587.CVTPulley"
    ) -> "_6318.CVTPulleyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CVTPulleyDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_pulley_load_case(
        self: Self, design_entity_analysis: "_6856.CVTPulleyLoadCase"
    ) -> "_6318.CVTPulleyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CVTPulleyDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_pulley(
        self: Self, design_entity: "_2590.Pulley"
    ) -> "_6366.PulleyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PulleyDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_pulley_load_case(
        self: Self, design_entity_analysis: "_6940.PulleyLoadCase"
    ) -> "_6366.PulleyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PulleyDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection(
        self: Self, design_entity: "_2598.ShaftHubConnection"
    ) -> "_6374.ShaftHubConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftHubConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection_load_case(
        self: Self, design_entity_analysis: "_6949.ShaftHubConnectionLoadCase"
    ) -> "_6374.ShaftHubConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftHubConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SHAFT_HUB_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring(
        self: Self, design_entity: "_2596.RollingRing"
    ) -> "_6371.RollingRingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_load_case(
        self: Self, design_entity_analysis: "_6947.RollingRingLoadCase"
    ) -> "_6371.RollingRingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly(
        self: Self, design_entity: "_2597.RollingRingAssembly"
    ) -> "_6369.RollingRingAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingAssemblyDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly_load_case(
        self: Self, design_entity_analysis: "_6945.RollingRingAssemblyLoadCase"
    ) -> "_6369.RollingRingAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingAssemblyDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ROLLING_RING_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper(
        self: Self, design_entity: "_2600.SpringDamper"
    ) -> "_6381.SpringDamperDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_load_case(
        self: Self, design_entity_analysis: "_6958.SpringDamperLoadCase"
    ) -> "_6381.SpringDamperDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_half(
        self: Self, design_entity: "_2601.SpringDamperHalf"
    ) -> "_6382.SpringDamperHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperHalfDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_half_load_case(
        self: Self, design_entity_analysis: "_6957.SpringDamperHalfLoadCase"
    ) -> "_6382.SpringDamperHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperHalfDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPRING_DAMPER_HALF_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser(
        self: Self, design_entity: "_2602.Synchroniser"
    ) -> "_6391.SynchroniserDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_load_case(
        self: Self, design_entity_analysis: "_6968.SynchroniserLoadCase"
    ) -> "_6391.SynchroniserDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_half(
        self: Self, design_entity: "_2604.SynchroniserHalf"
    ) -> "_6392.SynchroniserHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserHalfDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_half_load_case(
        self: Self, design_entity_analysis: "_6967.SynchroniserHalfLoadCase"
    ) -> "_6392.SynchroniserHalfDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserHalfDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_part(
        self: Self, design_entity: "_2605.SynchroniserPart"
    ) -> "_6393.SynchroniserPartDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserPartDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_part_load_case(
        self: Self, design_entity_analysis: "_6969.SynchroniserPartLoadCase"
    ) -> "_6393.SynchroniserPartDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserPartDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve(
        self: Self, design_entity: "_2606.SynchroniserSleeve"
    ) -> "_6394.SynchroniserSleeveDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserSleeveDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve_load_case(
        self: Self, design_entity_analysis: "_6970.SynchroniserSleeveLoadCase"
    ) -> "_6394.SynchroniserSleeveDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserSleeveDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SYNCHRONISER_SLEEVE_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter(
        self: Self, design_entity: "_2607.TorqueConverter"
    ) -> "_6396.TorqueConverterDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_load_case(
        self: Self, design_entity_analysis: "_6973.TorqueConverterLoadCase"
    ) -> "_6396.TorqueConverterDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump(
        self: Self, design_entity: "_2608.TorqueConverterPump"
    ) -> "_6397.TorqueConverterPumpDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterPumpDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump_load_case(
        self: Self, design_entity_analysis: "_6974.TorqueConverterPumpLoadCase"
    ) -> "_6397.TorqueConverterPumpDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterPumpDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _TORQUE_CONVERTER_PUMP_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine(
        self: Self, design_entity: "_2610.TorqueConverterTurbine"
    ) -> "_6398.TorqueConverterTurbineDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterTurbineDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine_load_case(
        self: Self, design_entity_analysis: "_6975.TorqueConverterTurbineLoadCase"
    ) -> "_6398.TorqueConverterTurbineDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.TorqueConverterTurbineDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _TORQUE_CONVERTER_TURBINE_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2295.ShaftToMountableComponentConnection"
    ) -> "_6375.ShaftToMountableComponentConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftToMountableComponentConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection_load_case(
        self: Self,
        design_entity_analysis: "_6951.ShaftToMountableComponentConnectionLoadCase",
    ) -> "_6375.ShaftToMountableComponentConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftToMountableComponentConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection(
        self: Self, design_entity: "_2273.CVTBeltConnection"
    ) -> "_6316.CVTBeltConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CVTBeltConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection_load_case(
        self: Self, design_entity_analysis: "_6854.CVTBeltConnectionLoadCase"
    ) -> "_6316.CVTBeltConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CVTBeltConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CVT_BELT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_connection(
        self: Self, design_entity: "_2268.BeltConnection"
    ) -> "_6285.BeltConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BeltConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_connection_load_case(
        self: Self, design_entity_analysis: "_6820.BeltConnectionLoadCase"
    ) -> "_6285.BeltConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BeltConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coaxial_connection(
        self: Self, design_entity: "_2269.CoaxialConnection"
    ) -> "_6300.CoaxialConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CoaxialConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coaxial_connection_load_case(
        self: Self, design_entity_analysis: "_6836.CoaxialConnectionLoadCase"
    ) -> "_6300.CoaxialConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CoaxialConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _COAXIAL_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connection(
        self: Self, design_entity: "_2272.Connection"
    ) -> "_6311.ConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connection_load_case(
        self: Self, design_entity_analysis: "_6849.ConnectionLoadCase"
    ) -> "_6311.ConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection(
        self: Self, design_entity: "_2281.InterMountableComponentConnection"
    ) -> "_6343.InterMountableComponentConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.InterMountableComponentConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _INTER_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection_load_case(
        self: Self,
        design_entity_analysis: "_6911.InterMountableComponentConnectionLoadCase",
    ) -> "_6343.InterMountableComponentConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.InterMountableComponentConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_connection(
        self: Self, design_entity: "_2287.PlanetaryConnection"
    ) -> "_6361.PlanetaryConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_connection_load_case(
        self: Self, design_entity_analysis: "_6932.PlanetaryConnectionLoadCase"
    ) -> "_6361.PlanetaryConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PLANETARY_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection(
        self: Self, design_entity: "_2292.RollingRingConnection"
    ) -> "_6370.RollingRingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection_load_case(
        self: Self, design_entity_analysis: "_6946.RollingRingConnectionLoadCase"
    ) -> "_6370.RollingRingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RollingRingConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ROLLING_RING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection(
        self: Self, design_entity: "_2265.AbstractShaftToMountableComponentConnection"
    ) -> "_6279.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftToMountableComponentConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection_load_case(
        self: Self,
        design_entity_analysis: "_6809.AbstractShaftToMountableComponentConnectionLoadCase",
    ) -> "_6279.AbstractShaftToMountableComponentConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftToMountableComponentConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftToMountableComponentConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh(
        self: Self, design_entity: "_2301.BevelDifferentialGearMesh"
    ) -> "_6288.BevelDifferentialGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6823.BevelDifferentialGearMeshLoadCase"
    ) -> "_6288.BevelDifferentialGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh(
        self: Self, design_entity: "_2305.ConceptGearMesh"
    ) -> "_6306.ConceptGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6842.ConceptGearMeshLoadCase"
    ) -> "_6306.ConceptGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh(
        self: Self, design_entity: "_2311.FaceGearMesh"
    ) -> "_6332.FaceGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6885.FaceGearMeshLoadCase"
    ) -> "_6332.FaceGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh(
        self: Self, design_entity: "_2325.StraightBevelDiffGearMesh"
    ) -> "_6384.StraightBevelDiffGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6960.StraightBevelDiffGearMeshLoadCase"
    ) -> "_6384.StraightBevelDiffGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh(
        self: Self, design_entity: "_2303.BevelGearMesh"
    ) -> "_6293.BevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6828.BevelGearMeshLoadCase"
    ) -> "_6293.BevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh(
        self: Self, design_entity: "_2307.ConicalGearMesh"
    ) -> "_6309.ConicalGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6846.ConicalGearMeshLoadCase"
    ) -> "_6309.ConicalGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh(
        self: Self, design_entity: "_2299.AGMAGleasonConicalGearMesh"
    ) -> "_6281.AGMAGleasonConicalGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6814.AGMAGleasonConicalGearMeshLoadCase"
    ) -> "_6281.AGMAGleasonConicalGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh(
        self: Self, design_entity: "_2309.CylindricalGearMesh"
    ) -> "_6324.CylindricalGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6863.CylindricalGearMeshLoadCase"
    ) -> "_6324.CylindricalGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYLINDRICAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh(
        self: Self, design_entity: "_2315.HypoidGearMesh"
    ) -> "_6341.HypoidGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6906.HypoidGearMeshLoadCase"
    ) -> "_6341.HypoidGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: Self, design_entity: "_2318.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "_6345.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
        self: Self,
        design_entity_analysis: "_6913.KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    ) -> "_6345.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: Self, design_entity: "_2319.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> "_6348.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
        self: Self,
        design_entity_analysis: "_6916.KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    ) -> "_6348.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2320.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "_6351.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
        self: Self,
        design_entity_analysis: "_6919.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    ) -> "_6351.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh(
        self: Self, design_entity: "_2323.SpiralBevelGearMesh"
    ) -> "_6378.SpiralBevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6954.SpiralBevelGearMeshLoadCase"
    ) -> "_6378.SpiralBevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh(
        self: Self, design_entity: "_2327.StraightBevelGearMesh"
    ) -> "_6387.StraightBevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6963.StraightBevelGearMeshLoadCase"
    ) -> "_6387.StraightBevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh(
        self: Self, design_entity: "_2329.WormGearMesh"
    ) -> "_6402.WormGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6983.WormGearMeshLoadCase"
    ) -> "_6402.WormGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh(
        self: Self, design_entity: "_2331.ZerolBevelGearMesh"
    ) -> "_6405.ZerolBevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6986.ZerolBevelGearMeshLoadCase"
    ) -> "_6405.ZerolBevelGearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ZerolBevelGearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ZEROL_BEVEL_GEAR_MESH_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_mesh(
        self: Self, design_entity: "_2313.GearMesh"
    ) -> "_6337.GearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.GearMeshDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_mesh_load_case(
        self: Self, design_entity_analysis: "_6892.GearMeshLoadCase"
    ) -> "_6337.GearMeshDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.GearMeshDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection(
        self: Self, design_entity: "_2335.CycloidalDiscCentralBearingConnection"
    ) -> "_6320.CycloidalDiscCentralBearingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscCentralBearingConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection_load_case(
        self: Self,
        design_entity_analysis: "_6858.CycloidalDiscCentralBearingConnectionLoadCase",
    ) -> "_6320.CycloidalDiscCentralBearingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscCentralBearingConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscCentralBearingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection(
        self: Self, design_entity: "_2338.CycloidalDiscPlanetaryBearingConnection"
    ) -> "_6322.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection_load_case(
        self: Self,
        design_entity_analysis: "_6860.CycloidalDiscPlanetaryBearingConnectionLoadCase",
    ) -> "_6322.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection(
        self: Self, design_entity: "_2341.RingPinsToDiscConnection"
    ) -> "_6368.RingPinsToDiscConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RingPinsToDiscConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _RING_PINS_TO_DISC_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection_load_case(
        self: Self, design_entity_analysis: "_6944.RingPinsToDiscConnectionLoadCase"
    ) -> "_6368.RingPinsToDiscConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RingPinsToDiscConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _RING_PINS_TO_DISC_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection(
        self: Self, design_entity: "_2348.PartToPartShearCouplingConnection"
    ) -> "_6358.PartToPartShearCouplingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_CONNECTION
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection_load_case(
        self: Self,
        design_entity_analysis: "_6929.PartToPartShearCouplingConnectionLoadCase",
    ) -> "_6358.PartToPartShearCouplingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PartToPartShearCouplingConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_connection(
        self: Self, design_entity: "_2342.ClutchConnection"
    ) -> "_6297.ClutchConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_connection_load_case(
        self: Self, design_entity_analysis: "_6832.ClutchConnectionLoadCase"
    ) -> "_6297.ClutchConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ClutchConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection(
        self: Self, design_entity: "_2344.ConceptCouplingConnection"
    ) -> "_6302.ConceptCouplingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection_load_case(
        self: Self, design_entity_analysis: "_6838.ConceptCouplingConnectionLoadCase"
    ) -> "_6302.ConceptCouplingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CONCEPT_COUPLING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_connection(
        self: Self, design_entity: "_2346.CouplingConnection"
    ) -> "_6313.CouplingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_connection_load_case(
        self: Self, design_entity_analysis: "_6851.CouplingConnectionLoadCase"
    ) -> "_6313.CouplingConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingConnectionDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _COUPLING_CONNECTION_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: Self, design_entity: "_2350.SpringDamperConnection"
    ) -> "_6380.SpringDamperConnectionDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpringDamperConnectionDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft(
        self: Self, design_entity: "_2435.AbstractShaft"
    ) -> "_6277.AbstractShaftDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_load_case(
        self: Self, design_entity_analysis: "_6807.AbstractShaftLoadCase"
    ) -> "_6277.AbstractShaftDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_assembly(
        self: Self, design_entity: "_2434.AbstractAssembly"
    ) -> "_6276.AbstractAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractAssemblyDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_assembly_load_case(
        self: Self, design_entity_analysis: "_6806.AbstractAssemblyLoadCase"
    ) -> "_6276.AbstractAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractAssemblyDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing(
        self: Self, design_entity: "_2436.AbstractShaftOrHousing"
    ) -> "_6278.AbstractShaftOrHousingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftOrHousingDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing_load_case(
        self: Self, design_entity_analysis: "_6808.AbstractShaftOrHousingLoadCase"
    ) -> "_6278.AbstractShaftOrHousingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractShaftOrHousingDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bearing(
        self: Self, design_entity: "_2439.Bearing"
    ) -> "_6284.BearingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BearingDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEARING](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bearing_load_case(
        self: Self, design_entity_analysis: "_6819.BearingLoadCase"
    ) -> "_6284.BearingDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BearingDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEARING_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolt(
        self: Self, design_entity: "_2442.Bolt"
    ) -> "_6295.BoltDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BoltDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolt_load_case(
        self: Self, design_entity_analysis: "_6831.BoltLoadCase"
    ) -> "_6295.BoltDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BoltDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolted_joint(
        self: Self, design_entity: "_2443.BoltedJoint"
    ) -> "_6296.BoltedJointDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BoltedJointDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolted_joint_load_case(
        self: Self, design_entity_analysis: "_6830.BoltedJointLoadCase"
    ) -> "_6296.BoltedJointDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BoltedJointDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_component(
        self: Self, design_entity: "_2444.Component"
    ) -> "_6301.ComponentDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ComponentDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_component_load_case(
        self: Self, design_entity_analysis: "_6837.ComponentLoadCase"
    ) -> "_6301.ComponentDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ComponentDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connector(
        self: Self, design_entity: "_2447.Connector"
    ) -> "_6312.ConnectorDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectorDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Connector)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connector_load_case(
        self: Self, design_entity_analysis: "_6850.ConnectorLoadCase"
    ) -> "_6312.ConnectorDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectorDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_datum(
        self: Self, design_entity: "_2448.Datum"
    ) -> "_6327.DatumDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.DatumDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Datum)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_DATUM](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_datum_load_case(
        self: Self, design_entity_analysis: "_6869.DatumLoadCase"
    ) -> "_6327.DatumDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.DatumDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_DATUM_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_external_cad_model(
        self: Self, design_entity: "_2452.ExternalCADModel"
    ) -> "_6330.ExternalCADModelDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ExternalCADModelDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_external_cad_model_load_case(
        self: Self, design_entity_analysis: "_6883.ExternalCADModelLoadCase"
    ) -> "_6330.ExternalCADModelDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ExternalCADModelDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _EXTERNAL_CAD_MODEL_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_fe_part(
        self: Self, design_entity: "_2453.FEPart"
    ) -> "_6334.FEPartDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FEPartDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FE_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_fe_part_load_case(
        self: Self, design_entity_analysis: "_6887.FEPartLoadCase"
    ) -> "_6334.FEPartDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FEPartDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FE_PART_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly(
        self: Self, design_entity: "_2454.FlexiblePinAssembly"
    ) -> "_6335.FlexiblePinAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FlexiblePinAssemblyDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly_load_case(
        self: Self, design_entity_analysis: "_6888.FlexiblePinAssemblyLoadCase"
    ) -> "_6335.FlexiblePinAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FlexiblePinAssemblyDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_assembly(
        self: Self, design_entity: "_2433.Assembly"
    ) -> "_6283.AssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AssemblyDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_assembly_load_case(
        self: Self, design_entity_analysis: "_6818.AssemblyLoadCase"
    ) -> "_6283.AssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AssemblyDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model(
        self: Self, design_entity: "_2455.GuideDxfModel"
    ) -> "_6339.GuideDxfModelDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.GuideDxfModelDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model_load_case(
        self: Self, design_entity_analysis: "_6896.GuideDxfModelLoadCase"
    ) -> "_6339.GuideDxfModelDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.GuideDxfModelDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mass_disc(
        self: Self, design_entity: "_2462.MassDisc"
    ) -> "_6353.MassDiscDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.MassDiscDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mass_disc_load_case(
        self: Self, design_entity_analysis: "_6921.MassDiscLoadCase"
    ) -> "_6353.MassDiscDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.MassDiscDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_measurement_component(
        self: Self, design_entity: "_2463.MeasurementComponent"
    ) -> "_6354.MeasurementComponentDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.MeasurementComponentDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_measurement_component_load_case(
        self: Self, design_entity_analysis: "_6922.MeasurementComponentLoadCase"
    ) -> "_6354.MeasurementComponentDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.MeasurementComponentDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _MEASUREMENT_COMPONENT_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mountable_component(
        self: Self, design_entity: "_2464.MountableComponent"
    ) -> "_6355.MountableComponentDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.MountableComponentDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mountable_component_load_case(
        self: Self, design_entity_analysis: "_6924.MountableComponentLoadCase"
    ) -> "_6355.MountableComponentDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.MountableComponentDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _MOUNTABLE_COMPONENT_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_oil_seal(
        self: Self, design_entity: "_2466.OilSeal"
    ) -> "_6356.OilSealDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.OilSealDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_oil_seal_load_case(
        self: Self, design_entity_analysis: "_6926.OilSealLoadCase"
    ) -> "_6356.OilSealDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.OilSealDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part(
        self: Self, design_entity: "_2468.Part"
    ) -> "_6357.PartDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PartDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Part)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PART](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_load_case(
        self: Self, design_entity_analysis: "_6928.PartLoadCase"
    ) -> "_6357.PartDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PartDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PART_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planet_carrier(
        self: Self, design_entity: "_2469.PlanetCarrier"
    ) -> "_6363.PlanetCarrierDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetCarrierDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planet_carrier_load_case(
        self: Self, design_entity_analysis: "_6935.PlanetCarrierLoadCase"
    ) -> "_6363.PlanetCarrierDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetCarrierDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_point_load(
        self: Self, design_entity: "_2471.PointLoad"
    ) -> "_6364.PointLoadDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PointLoadDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_point_load_load_case(
        self: Self, design_entity_analysis: "_6938.PointLoadLoadCase"
    ) -> "_6364.PointLoadDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PointLoadDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_power_load(
        self: Self, design_entity: "_2472.PowerLoad"
    ) -> "_6365.PowerLoadDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PowerLoadDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_power_load_load_case(
        self: Self, design_entity_analysis: "_6939.PowerLoadLoadCase"
    ) -> "_6365.PowerLoadDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PowerLoadDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_root_assembly(
        self: Self, design_entity: "_2474.RootAssembly"
    ) -> "_6372.RootAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RootAssemblyDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_root_assembly_load_case(
        self: Self, design_entity_analysis: "_6948.RootAssemblyLoadCase"
    ) -> "_6372.RootAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.RootAssemblyDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_specialised_assembly(
        self: Self, design_entity: "_2476.SpecialisedAssembly"
    ) -> "_6376.SpecialisedAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_specialised_assembly_load_case(
        self: Self, design_entity_analysis: "_6952.SpecialisedAssemblyLoadCase"
    ) -> "_6376.SpecialisedAssemblyDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpecialisedAssemblyDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPECIALISED_ASSEMBLY_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass(
        self: Self, design_entity: "_2477.UnbalancedMass"
    ) -> "_6399.UnbalancedMassDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.UnbalancedMassDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass_load_case(
        self: Self, design_entity_analysis: "_6980.UnbalancedMassLoadCase"
    ) -> "_6399.UnbalancedMassDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.UnbalancedMassDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_virtual_component(
        self: Self, design_entity: "_2479.VirtualComponent"
    ) -> "_6400.VirtualComponentDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.VirtualComponentDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_virtual_component_load_case(
        self: Self, design_entity_analysis: "_6981.VirtualComponentLoadCase"
    ) -> "_6400.VirtualComponentDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.VirtualComponentDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft(
        self: Self, design_entity: "_2482.Shaft"
    ) -> "_6373.ShaftDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_load_case(
        self: Self, design_entity_analysis: "_6950.ShaftLoadCase"
    ) -> "_6373.ShaftDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear(
        self: Self, design_entity: "_2521.ConceptGear"
    ) -> "_6305.ConceptGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_load_case(
        self: Self, design_entity_analysis: "_6841.ConceptGearLoadCase"
    ) -> "_6305.ConceptGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_set(
        self: Self, design_entity: "_2522.ConceptGearSet"
    ) -> "_6307.ConceptGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_set_load_case(
        self: Self, design_entity_analysis: "_6843.ConceptGearSetLoadCase"
    ) -> "_6307.ConceptGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear(
        self: Self, design_entity: "_2528.FaceGear"
    ) -> "_6331.FaceGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_load_case(
        self: Self, design_entity_analysis: "_6884.FaceGearLoadCase"
    ) -> "_6331.FaceGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_set(
        self: Self, design_entity: "_2529.FaceGearSet"
    ) -> "_6333.FaceGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_set_load_case(
        self: Self, design_entity_analysis: "_6886.FaceGearSetLoadCase"
    ) -> "_6333.FaceGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.FaceGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear(
        self: Self, design_entity: "_2513.AGMAGleasonConicalGear"
    ) -> "_6280.AGMAGleasonConicalGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_load_case(
        self: Self, design_entity_analysis: "_6813.AGMAGleasonConicalGearLoadCase"
    ) -> "_6280.AGMAGleasonConicalGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set(
        self: Self, design_entity: "_2514.AGMAGleasonConicalGearSet"
    ) -> "_6282.AGMAGleasonConicalGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set_load_case(
        self: Self, design_entity_analysis: "_6815.AGMAGleasonConicalGearSetLoadCase"
    ) -> "_6282.AGMAGleasonConicalGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear(
        self: Self, design_entity: "_2515.BevelDifferentialGear"
    ) -> "_6287.BevelDifferentialGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_load_case(
        self: Self, design_entity_analysis: "_6822.BevelDifferentialGearLoadCase"
    ) -> "_6287.BevelDifferentialGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set(
        self: Self, design_entity: "_2516.BevelDifferentialGearSet"
    ) -> "_6289.BevelDifferentialGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set_load_case(
        self: Self, design_entity_analysis: "_6824.BevelDifferentialGearSetLoadCase"
    ) -> "_6289.BevelDifferentialGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear(
        self: Self, design_entity: "_2517.BevelDifferentialPlanetGear"
    ) -> "_6290.BevelDifferentialPlanetGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialPlanetGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_PLANET_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear_load_case(
        self: Self, design_entity_analysis: "_6825.BevelDifferentialPlanetGearLoadCase"
    ) -> "_6290.BevelDifferentialPlanetGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialPlanetGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear(
        self: Self, design_entity: "_2518.BevelDifferentialSunGear"
    ) -> "_6291.BevelDifferentialSunGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialSunGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear_load_case(
        self: Self, design_entity_analysis: "_6826.BevelDifferentialSunGearLoadCase"
    ) -> "_6291.BevelDifferentialSunGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelDifferentialSunGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear(
        self: Self, design_entity: "_2519.BevelGear"
    ) -> "_6292.BevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_load_case(
        self: Self, design_entity_analysis: "_6827.BevelGearLoadCase"
    ) -> "_6292.BevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set(
        self: Self, design_entity: "_2520.BevelGearSet"
    ) -> "_6294.BevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set_load_case(
        self: Self, design_entity_analysis: "_6829.BevelGearSetLoadCase"
    ) -> "_6294.BevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear(
        self: Self, design_entity: "_2523.ConicalGear"
    ) -> "_6308.ConicalGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_load_case(
        self: Self, design_entity_analysis: "_6844.ConicalGearLoadCase"
    ) -> "_6308.ConicalGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_set(
        self: Self, design_entity: "_2524.ConicalGearSet"
    ) -> "_6310.ConicalGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_set_load_case(
        self: Self, design_entity_analysis: "_6848.ConicalGearSetLoadCase"
    ) -> "_6310.ConicalGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear(
        self: Self, design_entity: "_2525.CylindricalGear"
    ) -> "_6323.CylindricalGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_load_case(
        self: Self, design_entity_analysis: "_6861.CylindricalGearLoadCase"
    ) -> "_6323.CylindricalGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set(
        self: Self, design_entity: "_2526.CylindricalGearSet"
    ) -> "_6325.CylindricalGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set_load_case(
        self: Self, design_entity_analysis: "_6865.CylindricalGearSetLoadCase"
    ) -> "_6325.CylindricalGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYLINDRICAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear(
        self: Self, design_entity: "_2527.CylindricalPlanetGear"
    ) -> "_6326.CylindricalPlanetGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalPlanetGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear_load_case(
        self: Self, design_entity_analysis: "_6866.CylindricalPlanetGearLoadCase"
    ) -> "_6326.CylindricalPlanetGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalPlanetGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _CYLINDRICAL_PLANET_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear(
        self: Self, design_entity: "_2530.Gear"
    ) -> "_6336.GearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.GearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_load_case(
        self: Self, design_entity_analysis: "_6890.GearLoadCase"
    ) -> "_6336.GearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.GearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_set(
        self: Self, design_entity: "_2532.GearSet"
    ) -> "_6338.GearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.GearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_set_load_case(
        self: Self, design_entity_analysis: "_6895.GearSetLoadCase"
    ) -> "_6338.GearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.GearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear(
        self: Self, design_entity: "_2534.HypoidGear"
    ) -> "_6340.HypoidGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_load_case(
        self: Self, design_entity_analysis: "_6905.HypoidGearLoadCase"
    ) -> "_6340.HypoidGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set(
        self: Self, design_entity: "_2535.HypoidGearSet"
    ) -> "_6342.HypoidGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set_load_case(
        self: Self, design_entity_analysis: "_6907.HypoidGearSetLoadCase"
    ) -> "_6342.HypoidGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.HypoidGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear(
        self: Self, design_entity: "_2536.KlingelnbergCycloPalloidConicalGear"
    ) -> "_6344.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(
        self: Self,
        design_entity_analysis: "_6912.KlingelnbergCycloPalloidConicalGearLoadCase",
    ) -> "_6344.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: Self, design_entity: "_2537.KlingelnbergCycloPalloidConicalGearSet"
    ) -> "_6346.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(
        self: Self,
        design_entity_analysis: "_6914.KlingelnbergCycloPalloidConicalGearSetLoadCase",
    ) -> "_6346.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: Self, design_entity: "_2538.KlingelnbergCycloPalloidHypoidGear"
    ) -> "_6347.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(
        self: Self,
        design_entity_analysis: "_6915.KlingelnbergCycloPalloidHypoidGearLoadCase",
    ) -> "_6347.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self, design_entity: "_2539.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> "_6349.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
        self: Self,
        design_entity_analysis: "_6917.KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    ) -> "_6349.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: Self, design_entity: "_2540.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "_6350.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
        self: Self,
        design_entity_analysis: "_6918.KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    ) -> "_6350.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: Self, design_entity: "_2541.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "_6352.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
        self: Self,
        design_entity_analysis: "_6920.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    ) -> "_6352.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set(
        self: Self, design_entity: "_2542.PlanetaryGearSet"
    ) -> "_6362.PlanetaryGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set_load_case(
        self: Self, design_entity_analysis: "_6933.PlanetaryGearSetLoadCase"
    ) -> "_6362.PlanetaryGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _PLANETARY_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear(
        self: Self, design_entity: "_2543.SpiralBevelGear"
    ) -> "_6377.SpiralBevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_load_case(
        self: Self, design_entity_analysis: "_6953.SpiralBevelGearLoadCase"
    ) -> "_6377.SpiralBevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_LOAD_CASE](
            design_entity_analysis.wrapped if design_entity_analysis else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set(
        self: Self, design_entity: "_2544.SpiralBevelGearSet"
    ) -> "_6379.SpiralBevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set_load_case(
        self: Self, design_entity_analysis: "_6955.SpiralBevelGearSetLoadCase"
    ) -> "_6379.SpiralBevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear(
        self: Self, design_entity: "_2545.StraightBevelDiffGear"
    ) -> "_6383.StraightBevelDiffGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_load_case(
        self: Self, design_entity_analysis: "_6959.StraightBevelDiffGearLoadCase"
    ) -> "_6383.StraightBevelDiffGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set(
        self: Self, design_entity: "_2546.StraightBevelDiffGearSet"
    ) -> "_6385.StraightBevelDiffGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_SET
        ](design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set_load_case(
        self: Self, design_entity_analysis: "_6961.StraightBevelDiffGearSetLoadCase"
    ) -> "_6385.StraightBevelDiffGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelDiffGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear(
        self: Self, design_entity: "_2547.StraightBevelGear"
    ) -> "_6386.StraightBevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_load_case(
        self: Self, design_entity_analysis: "_6962.StraightBevelGearLoadCase"
    ) -> "_6386.StraightBevelGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set(
        self: Self, design_entity: "_2548.StraightBevelGearSet"
    ) -> "_6388.StraightBevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearSetDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set_load_case(
        self: Self, design_entity_analysis: "_6964.StraightBevelGearSetLoadCase"
    ) -> "_6388.StraightBevelGearSetDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearSetDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear(
        self: Self, design_entity: "_2549.StraightBevelPlanetGear"
    ) -> "_6389.StraightBevelPlanetGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelPlanetGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear_load_case(
        self: Self, design_entity_analysis: "_6965.StraightBevelPlanetGearLoadCase"
    ) -> "_6389.StraightBevelPlanetGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelPlanetGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear(
        self: Self, design_entity: "_2550.StraightBevelSunGear"
    ) -> "_6390.StraightBevelSunGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelSunGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear_load_case(
        self: Self, design_entity_analysis: "_6966.StraightBevelSunGearLoadCase"
    ) -> "_6390.StraightBevelSunGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelSunGearDynamicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)
        """
        method_result = self.wrapped.ResultsFor.Overloads[
            _STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE
        ](design_entity_analysis.wrapped if design_entity_analysis else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear(
        self: Self, design_entity: "_2551.WormGear"
    ) -> "_6401.WormGearDynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.WormGearDynamicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)
        """
        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR](
            design_entity.wrapped if design_entity else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "DynamicAnalysis._Cast_DynamicAnalysis":
        return self._Cast_DynamicAnalysis(self)

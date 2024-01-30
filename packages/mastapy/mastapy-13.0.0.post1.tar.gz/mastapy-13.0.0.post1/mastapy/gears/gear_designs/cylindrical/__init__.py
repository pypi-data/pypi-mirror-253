"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._998 import AddendumModificationDistributionRule
    from ._999 import BacklashSpecification
    from ._1000 import BasicRackProfiles
    from ._1001 import CaseHardeningProperties
    from ._1002 import CreateNewSuitableCutterOption
    from ._1003 import CrossedAxisCylindricalGearPair
    from ._1004 import CrossedAxisCylindricalGearPairLineContact
    from ._1005 import CrossedAxisCylindricalGearPairPointContact
    from ._1006 import CylindricalGearAbstractRack
    from ._1007 import CylindricalGearAbstractRackFlank
    from ._1008 import CylindricalGearBasicRack
    from ._1009 import CylindricalGearBasicRackFlank
    from ._1010 import CylindricalGearCuttingOptions
    from ._1011 import CylindricalGearDefaults
    from ._1012 import CylindricalGearDesign
    from ._1013 import CylindricalGearDesignConstraint
    from ._1014 import CylindricalGearDesignConstraints
    from ._1015 import CylindricalGearDesignConstraintsDatabase
    from ._1016 import CylindricalGearDesignConstraintSettings
    from ._1017 import CylindricalGearFlankDesign
    from ._1018 import CylindricalGearMeshDesign
    from ._1019 import CylindricalGearMeshFlankDesign
    from ._1020 import CylindricalGearMicroGeometrySettings
    from ._1021 import CylindricalGearMicroGeometrySettingsDatabase
    from ._1022 import CylindricalGearMicroGeometrySettingsItem
    from ._1023 import CylindricalGearPinionTypeCutter
    from ._1024 import CylindricalGearPinionTypeCutterFlank
    from ._1025 import CylindricalGearProfileMeasurement
    from ._1026 import CylindricalGearProfileMeasurementType
    from ._1027 import CylindricalGearProfileModifications
    from ._1028 import CylindricalGearSetDesign
    from ._1029 import CylindricalGearSetFlankDesign
    from ._1030 import CylindricalGearSetMacroGeometryOptimiser
    from ._1031 import CylindricalGearSetManufacturingConfigurationSelection
    from ._1032 import CylindricalGearSetMicroGeometrySettings
    from ._1033 import CylindricalGearSetOptimisationWrapper
    from ._1034 import CylindricalGearTableMGItemDetail
    from ._1035 import CylindricalGearTableWithMGCharts
    from ._1036 import CylindricalGearToothThicknessSpecification
    from ._1037 import CylindricalMeshAngularBacklash
    from ._1038 import CylindricalMeshedGear
    from ._1039 import CylindricalMeshedGearFlank
    from ._1040 import CylindricalMeshLinearBacklashSpecification
    from ._1041 import CylindricalPlanetaryGearSetDesign
    from ._1042 import CylindricalPlanetGearDesign
    from ._1043 import DIN3967AllowanceSeries
    from ._1044 import DIN3967ToleranceSeries
    from ._1045 import DoubleAxisScaleAndRange
    from ._1046 import FinishToothThicknessDesignSpecification
    from ._1047 import GearFitSystems
    from ._1048 import GearManufacturingConfigSetupViewModel
    from ._1049 import GearSetManufacturingConfigurationSetup
    from ._1050 import GeometrySpecificationType
    from ._1051 import HardenedMaterialProperties
    from ._1052 import HardnessProfileCalculationMethod
    from ._1053 import HeatTreatmentType
    from ._1054 import ISO6336Geometry
    from ._1055 import ISO6336GeometryBase
    from ._1056 import ISO6336GeometryForShapedGears
    from ._1057 import ISO6336GeometryManufactured
    from ._1058 import LinearBacklashSpecification
    from ._1059 import LTCALoadCaseModifiableSettings
    from ._1060 import LTCASettings
    from ._1061 import MicroGeometryConvention
    from ._1062 import MicroGeometryProfileConvention
    from ._1063 import Micropitting
    from ._1064 import NamedPlanetAssemblyIndex
    from ._1065 import NamedPlanetSideBandAmplitudeFactor
    from ._1066 import ReadonlyToothThicknessSpecification
    from ._1067 import RelativeMeasurementViewModel
    from ._1068 import RelativeValuesSpecification
    from ._1069 import RootStressSurfaceChartOption
    from ._1070 import Scuffing
    from ._1071 import ScuffingCoefficientOfFrictionMethods
    from ._1072 import ScuffingTemperatureMethodsAGMA
    from ._1073 import ScuffingTemperatureMethodsISO
    from ._1074 import ShaperEdgeTypes
    from ._1075 import SpurGearLoadSharingCodes
    from ._1076 import StandardRack
    from ._1077 import StandardRackFlank
    from ._1078 import SurfaceRoughness
    from ._1079 import ThicknessType
    from ._1080 import TiffAnalysisSettings
    from ._1081 import TipAlterationCoefficientMethod
    from ._1082 import TolerancedMetalMeasurements
    from ._1083 import TolerancedValueSpecification
    from ._1084 import ToothFlankFractureAnalysisSettings
    from ._1085 import ToothThicknessSpecification
    from ._1086 import ToothThicknessSpecificationBase
    from ._1087 import TypeOfMechanismHousing
    from ._1088 import Usage
else:
    import_structure = {
        "_998": ["AddendumModificationDistributionRule"],
        "_999": ["BacklashSpecification"],
        "_1000": ["BasicRackProfiles"],
        "_1001": ["CaseHardeningProperties"],
        "_1002": ["CreateNewSuitableCutterOption"],
        "_1003": ["CrossedAxisCylindricalGearPair"],
        "_1004": ["CrossedAxisCylindricalGearPairLineContact"],
        "_1005": ["CrossedAxisCylindricalGearPairPointContact"],
        "_1006": ["CylindricalGearAbstractRack"],
        "_1007": ["CylindricalGearAbstractRackFlank"],
        "_1008": ["CylindricalGearBasicRack"],
        "_1009": ["CylindricalGearBasicRackFlank"],
        "_1010": ["CylindricalGearCuttingOptions"],
        "_1011": ["CylindricalGearDefaults"],
        "_1012": ["CylindricalGearDesign"],
        "_1013": ["CylindricalGearDesignConstraint"],
        "_1014": ["CylindricalGearDesignConstraints"],
        "_1015": ["CylindricalGearDesignConstraintsDatabase"],
        "_1016": ["CylindricalGearDesignConstraintSettings"],
        "_1017": ["CylindricalGearFlankDesign"],
        "_1018": ["CylindricalGearMeshDesign"],
        "_1019": ["CylindricalGearMeshFlankDesign"],
        "_1020": ["CylindricalGearMicroGeometrySettings"],
        "_1021": ["CylindricalGearMicroGeometrySettingsDatabase"],
        "_1022": ["CylindricalGearMicroGeometrySettingsItem"],
        "_1023": ["CylindricalGearPinionTypeCutter"],
        "_1024": ["CylindricalGearPinionTypeCutterFlank"],
        "_1025": ["CylindricalGearProfileMeasurement"],
        "_1026": ["CylindricalGearProfileMeasurementType"],
        "_1027": ["CylindricalGearProfileModifications"],
        "_1028": ["CylindricalGearSetDesign"],
        "_1029": ["CylindricalGearSetFlankDesign"],
        "_1030": ["CylindricalGearSetMacroGeometryOptimiser"],
        "_1031": ["CylindricalGearSetManufacturingConfigurationSelection"],
        "_1032": ["CylindricalGearSetMicroGeometrySettings"],
        "_1033": ["CylindricalGearSetOptimisationWrapper"],
        "_1034": ["CylindricalGearTableMGItemDetail"],
        "_1035": ["CylindricalGearTableWithMGCharts"],
        "_1036": ["CylindricalGearToothThicknessSpecification"],
        "_1037": ["CylindricalMeshAngularBacklash"],
        "_1038": ["CylindricalMeshedGear"],
        "_1039": ["CylindricalMeshedGearFlank"],
        "_1040": ["CylindricalMeshLinearBacklashSpecification"],
        "_1041": ["CylindricalPlanetaryGearSetDesign"],
        "_1042": ["CylindricalPlanetGearDesign"],
        "_1043": ["DIN3967AllowanceSeries"],
        "_1044": ["DIN3967ToleranceSeries"],
        "_1045": ["DoubleAxisScaleAndRange"],
        "_1046": ["FinishToothThicknessDesignSpecification"],
        "_1047": ["GearFitSystems"],
        "_1048": ["GearManufacturingConfigSetupViewModel"],
        "_1049": ["GearSetManufacturingConfigurationSetup"],
        "_1050": ["GeometrySpecificationType"],
        "_1051": ["HardenedMaterialProperties"],
        "_1052": ["HardnessProfileCalculationMethod"],
        "_1053": ["HeatTreatmentType"],
        "_1054": ["ISO6336Geometry"],
        "_1055": ["ISO6336GeometryBase"],
        "_1056": ["ISO6336GeometryForShapedGears"],
        "_1057": ["ISO6336GeometryManufactured"],
        "_1058": ["LinearBacklashSpecification"],
        "_1059": ["LTCALoadCaseModifiableSettings"],
        "_1060": ["LTCASettings"],
        "_1061": ["MicroGeometryConvention"],
        "_1062": ["MicroGeometryProfileConvention"],
        "_1063": ["Micropitting"],
        "_1064": ["NamedPlanetAssemblyIndex"],
        "_1065": ["NamedPlanetSideBandAmplitudeFactor"],
        "_1066": ["ReadonlyToothThicknessSpecification"],
        "_1067": ["RelativeMeasurementViewModel"],
        "_1068": ["RelativeValuesSpecification"],
        "_1069": ["RootStressSurfaceChartOption"],
        "_1070": ["Scuffing"],
        "_1071": ["ScuffingCoefficientOfFrictionMethods"],
        "_1072": ["ScuffingTemperatureMethodsAGMA"],
        "_1073": ["ScuffingTemperatureMethodsISO"],
        "_1074": ["ShaperEdgeTypes"],
        "_1075": ["SpurGearLoadSharingCodes"],
        "_1076": ["StandardRack"],
        "_1077": ["StandardRackFlank"],
        "_1078": ["SurfaceRoughness"],
        "_1079": ["ThicknessType"],
        "_1080": ["TiffAnalysisSettings"],
        "_1081": ["TipAlterationCoefficientMethod"],
        "_1082": ["TolerancedMetalMeasurements"],
        "_1083": ["TolerancedValueSpecification"],
        "_1084": ["ToothFlankFractureAnalysisSettings"],
        "_1085": ["ToothThicknessSpecification"],
        "_1086": ["ToothThicknessSpecificationBase"],
        "_1087": ["TypeOfMechanismHousing"],
        "_1088": ["Usage"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AddendumModificationDistributionRule",
    "BacklashSpecification",
    "BasicRackProfiles",
    "CaseHardeningProperties",
    "CreateNewSuitableCutterOption",
    "CrossedAxisCylindricalGearPair",
    "CrossedAxisCylindricalGearPairLineContact",
    "CrossedAxisCylindricalGearPairPointContact",
    "CylindricalGearAbstractRack",
    "CylindricalGearAbstractRackFlank",
    "CylindricalGearBasicRack",
    "CylindricalGearBasicRackFlank",
    "CylindricalGearCuttingOptions",
    "CylindricalGearDefaults",
    "CylindricalGearDesign",
    "CylindricalGearDesignConstraint",
    "CylindricalGearDesignConstraints",
    "CylindricalGearDesignConstraintsDatabase",
    "CylindricalGearDesignConstraintSettings",
    "CylindricalGearFlankDesign",
    "CylindricalGearMeshDesign",
    "CylindricalGearMeshFlankDesign",
    "CylindricalGearMicroGeometrySettings",
    "CylindricalGearMicroGeometrySettingsDatabase",
    "CylindricalGearMicroGeometrySettingsItem",
    "CylindricalGearPinionTypeCutter",
    "CylindricalGearPinionTypeCutterFlank",
    "CylindricalGearProfileMeasurement",
    "CylindricalGearProfileMeasurementType",
    "CylindricalGearProfileModifications",
    "CylindricalGearSetDesign",
    "CylindricalGearSetFlankDesign",
    "CylindricalGearSetMacroGeometryOptimiser",
    "CylindricalGearSetManufacturingConfigurationSelection",
    "CylindricalGearSetMicroGeometrySettings",
    "CylindricalGearSetOptimisationWrapper",
    "CylindricalGearTableMGItemDetail",
    "CylindricalGearTableWithMGCharts",
    "CylindricalGearToothThicknessSpecification",
    "CylindricalMeshAngularBacklash",
    "CylindricalMeshedGear",
    "CylindricalMeshedGearFlank",
    "CylindricalMeshLinearBacklashSpecification",
    "CylindricalPlanetaryGearSetDesign",
    "CylindricalPlanetGearDesign",
    "DIN3967AllowanceSeries",
    "DIN3967ToleranceSeries",
    "DoubleAxisScaleAndRange",
    "FinishToothThicknessDesignSpecification",
    "GearFitSystems",
    "GearManufacturingConfigSetupViewModel",
    "GearSetManufacturingConfigurationSetup",
    "GeometrySpecificationType",
    "HardenedMaterialProperties",
    "HardnessProfileCalculationMethod",
    "HeatTreatmentType",
    "ISO6336Geometry",
    "ISO6336GeometryBase",
    "ISO6336GeometryForShapedGears",
    "ISO6336GeometryManufactured",
    "LinearBacklashSpecification",
    "LTCALoadCaseModifiableSettings",
    "LTCASettings",
    "MicroGeometryConvention",
    "MicroGeometryProfileConvention",
    "Micropitting",
    "NamedPlanetAssemblyIndex",
    "NamedPlanetSideBandAmplitudeFactor",
    "ReadonlyToothThicknessSpecification",
    "RelativeMeasurementViewModel",
    "RelativeValuesSpecification",
    "RootStressSurfaceChartOption",
    "Scuffing",
    "ScuffingCoefficientOfFrictionMethods",
    "ScuffingTemperatureMethodsAGMA",
    "ScuffingTemperatureMethodsISO",
    "ShaperEdgeTypes",
    "SpurGearLoadSharingCodes",
    "StandardRack",
    "StandardRackFlank",
    "SurfaceRoughness",
    "ThicknessType",
    "TiffAnalysisSettings",
    "TipAlterationCoefficientMethod",
    "TolerancedMetalMeasurements",
    "TolerancedValueSpecification",
    "ToothFlankFractureAnalysisSettings",
    "ToothThicknessSpecification",
    "ToothThicknessSpecificationBase",
    "TypeOfMechanismHousing",
    "Usage",
)

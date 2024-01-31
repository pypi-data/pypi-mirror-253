"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._236 import AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial
    from ._237 import AcousticRadiationEfficiency
    from ._238 import AcousticRadiationEfficiencyInputType
    from ._239 import AGMALubricantType
    from ._240 import AGMAMaterialApplications
    from ._241 import AGMAMaterialClasses
    from ._242 import AGMAMaterialGrade
    from ._243 import AirProperties
    from ._244 import BearingLubricationCondition
    from ._245 import BearingMaterial
    from ._246 import BearingMaterialDatabase
    from ._247 import BHCurveExtrapolationMethod
    from ._248 import BHCurveSpecification
    from ._249 import ComponentMaterialDatabase
    from ._250 import CompositeFatigueSafetyFactorItem
    from ._251 import CylindricalGearRatingMethods
    from ._252 import DensitySpecificationMethod
    from ._253 import FatigueSafetyFactorItem
    from ._254 import FatigueSafetyFactorItemBase
    from ._255 import GearingTypes
    from ._256 import GeneralTransmissionProperties
    from ._257 import GreaseContaminationOptions
    from ._258 import HardnessType
    from ._259 import ISO76StaticSafetyFactorLimits
    from ._260 import ISOLubricantType
    from ._261 import LubricantDefinition
    from ._262 import LubricantDelivery
    from ._263 import LubricantViscosityClassAGMA
    from ._264 import LubricantViscosityClassification
    from ._265 import LubricantViscosityClassISO
    from ._266 import LubricantViscosityClassSAE
    from ._267 import LubricationDetail
    from ._268 import LubricationDetailDatabase
    from ._269 import Material
    from ._270 import MaterialDatabase
    from ._271 import MaterialsSettings
    from ._272 import MaterialsSettingsDatabase
    from ._273 import MaterialsSettingsItem
    from ._274 import MaterialStandards
    from ._275 import MetalPlasticType
    from ._276 import OilFiltrationOptions
    from ._277 import PressureViscosityCoefficientMethod
    from ._278 import QualityGrade
    from ._279 import SafetyFactorGroup
    from ._280 import SafetyFactorItem
    from ._281 import SNCurve
    from ._282 import SNCurvePoint
    from ._283 import SoundPressureEnclosure
    from ._284 import SoundPressureEnclosureType
    from ._285 import StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial
    from ._286 import StressCyclesDataForTheContactSNCurveOfAPlasticMaterial
    from ._287 import TransmissionApplications
    from ._288 import VDI2736LubricantType
    from ._289 import VehicleDynamicsProperties
    from ._290 import WindTurbineStandards
    from ._291 import WorkingCharacteristics
else:
    import_structure = {
        "_236": ["AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial"],
        "_237": ["AcousticRadiationEfficiency"],
        "_238": ["AcousticRadiationEfficiencyInputType"],
        "_239": ["AGMALubricantType"],
        "_240": ["AGMAMaterialApplications"],
        "_241": ["AGMAMaterialClasses"],
        "_242": ["AGMAMaterialGrade"],
        "_243": ["AirProperties"],
        "_244": ["BearingLubricationCondition"],
        "_245": ["BearingMaterial"],
        "_246": ["BearingMaterialDatabase"],
        "_247": ["BHCurveExtrapolationMethod"],
        "_248": ["BHCurveSpecification"],
        "_249": ["ComponentMaterialDatabase"],
        "_250": ["CompositeFatigueSafetyFactorItem"],
        "_251": ["CylindricalGearRatingMethods"],
        "_252": ["DensitySpecificationMethod"],
        "_253": ["FatigueSafetyFactorItem"],
        "_254": ["FatigueSafetyFactorItemBase"],
        "_255": ["GearingTypes"],
        "_256": ["GeneralTransmissionProperties"],
        "_257": ["GreaseContaminationOptions"],
        "_258": ["HardnessType"],
        "_259": ["ISO76StaticSafetyFactorLimits"],
        "_260": ["ISOLubricantType"],
        "_261": ["LubricantDefinition"],
        "_262": ["LubricantDelivery"],
        "_263": ["LubricantViscosityClassAGMA"],
        "_264": ["LubricantViscosityClassification"],
        "_265": ["LubricantViscosityClassISO"],
        "_266": ["LubricantViscosityClassSAE"],
        "_267": ["LubricationDetail"],
        "_268": ["LubricationDetailDatabase"],
        "_269": ["Material"],
        "_270": ["MaterialDatabase"],
        "_271": ["MaterialsSettings"],
        "_272": ["MaterialsSettingsDatabase"],
        "_273": ["MaterialsSettingsItem"],
        "_274": ["MaterialStandards"],
        "_275": ["MetalPlasticType"],
        "_276": ["OilFiltrationOptions"],
        "_277": ["PressureViscosityCoefficientMethod"],
        "_278": ["QualityGrade"],
        "_279": ["SafetyFactorGroup"],
        "_280": ["SafetyFactorItem"],
        "_281": ["SNCurve"],
        "_282": ["SNCurvePoint"],
        "_283": ["SoundPressureEnclosure"],
        "_284": ["SoundPressureEnclosureType"],
        "_285": ["StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial"],
        "_286": ["StressCyclesDataForTheContactSNCurveOfAPlasticMaterial"],
        "_287": ["TransmissionApplications"],
        "_288": ["VDI2736LubricantType"],
        "_289": ["VehicleDynamicsProperties"],
        "_290": ["WindTurbineStandards"],
        "_291": ["WorkingCharacteristics"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStressCyclesDataForAnSNCurveOfAPlasticMaterial",
    "AcousticRadiationEfficiency",
    "AcousticRadiationEfficiencyInputType",
    "AGMALubricantType",
    "AGMAMaterialApplications",
    "AGMAMaterialClasses",
    "AGMAMaterialGrade",
    "AirProperties",
    "BearingLubricationCondition",
    "BearingMaterial",
    "BearingMaterialDatabase",
    "BHCurveExtrapolationMethod",
    "BHCurveSpecification",
    "ComponentMaterialDatabase",
    "CompositeFatigueSafetyFactorItem",
    "CylindricalGearRatingMethods",
    "DensitySpecificationMethod",
    "FatigueSafetyFactorItem",
    "FatigueSafetyFactorItemBase",
    "GearingTypes",
    "GeneralTransmissionProperties",
    "GreaseContaminationOptions",
    "HardnessType",
    "ISO76StaticSafetyFactorLimits",
    "ISOLubricantType",
    "LubricantDefinition",
    "LubricantDelivery",
    "LubricantViscosityClassAGMA",
    "LubricantViscosityClassification",
    "LubricantViscosityClassISO",
    "LubricantViscosityClassSAE",
    "LubricationDetail",
    "LubricationDetailDatabase",
    "Material",
    "MaterialDatabase",
    "MaterialsSettings",
    "MaterialsSettingsDatabase",
    "MaterialsSettingsItem",
    "MaterialStandards",
    "MetalPlasticType",
    "OilFiltrationOptions",
    "PressureViscosityCoefficientMethod",
    "QualityGrade",
    "SafetyFactorGroup",
    "SafetyFactorItem",
    "SNCurve",
    "SNCurvePoint",
    "SoundPressureEnclosure",
    "SoundPressureEnclosureType",
    "StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial",
    "StressCyclesDataForTheContactSNCurveOfAPlasticMaterial",
    "TransmissionApplications",
    "VDI2736LubricantType",
    "VehicleDynamicsProperties",
    "WindTurbineStandards",
    "WorkingCharacteristics",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._314 import AccuracyGrades
    from ._315 import AGMAToleranceStandard
    from ._316 import BevelHypoidGearDesignSettings
    from ._317 import BevelHypoidGearRatingSettings
    from ._318 import CentreDistanceChangeMethod
    from ._319 import CoefficientOfFrictionCalculationMethod
    from ._320 import ConicalGearToothSurface
    from ._321 import ContactRatioDataSource
    from ._322 import ContactRatioRequirements
    from ._323 import CylindricalFlanks
    from ._324 import CylindricalMisalignmentDataSource
    from ._325 import DeflectionFromBendingOption
    from ._326 import GearFlanks
    from ._327 import GearNURBSSurface
    from ._328 import GearSetDesignGroup
    from ._329 import GearSetModes
    from ._330 import GearSetOptimisationResult
    from ._331 import GearSetOptimisationResults
    from ._332 import GearSetOptimiser
    from ._333 import Hand
    from ._334 import ISOToleranceStandard
    from ._335 import LubricationMethods
    from ._336 import MicroGeometryInputTypes
    from ._337 import MicroGeometryModel
    from ._338 import MicropittingCoefficientOfFrictionCalculationMethod
    from ._339 import NamedPlanetAngle
    from ._340 import PlanetaryDetail
    from ._341 import PlanetaryRatingLoadSharingOption
    from ._342 import PocketingPowerLossCoefficients
    from ._343 import PocketingPowerLossCoefficientsDatabase
    from ._344 import QualityGradeTypes
    from ._345 import SafetyRequirementsAGMA
    from ._346 import SpecificationForTheEffectOfOilKinematicViscosity
    from ._347 import SpiralBevelRootLineTilt
    from ._348 import SpiralBevelToothTaper
    from ._349 import TESpecificationType
    from ._350 import WormAddendumFactor
    from ._351 import WormType
    from ._352 import ZerolBevelGleasonToothTaperOption
else:
    import_structure = {
        "_314": ["AccuracyGrades"],
        "_315": ["AGMAToleranceStandard"],
        "_316": ["BevelHypoidGearDesignSettings"],
        "_317": ["BevelHypoidGearRatingSettings"],
        "_318": ["CentreDistanceChangeMethod"],
        "_319": ["CoefficientOfFrictionCalculationMethod"],
        "_320": ["ConicalGearToothSurface"],
        "_321": ["ContactRatioDataSource"],
        "_322": ["ContactRatioRequirements"],
        "_323": ["CylindricalFlanks"],
        "_324": ["CylindricalMisalignmentDataSource"],
        "_325": ["DeflectionFromBendingOption"],
        "_326": ["GearFlanks"],
        "_327": ["GearNURBSSurface"],
        "_328": ["GearSetDesignGroup"],
        "_329": ["GearSetModes"],
        "_330": ["GearSetOptimisationResult"],
        "_331": ["GearSetOptimisationResults"],
        "_332": ["GearSetOptimiser"],
        "_333": ["Hand"],
        "_334": ["ISOToleranceStandard"],
        "_335": ["LubricationMethods"],
        "_336": ["MicroGeometryInputTypes"],
        "_337": ["MicroGeometryModel"],
        "_338": ["MicropittingCoefficientOfFrictionCalculationMethod"],
        "_339": ["NamedPlanetAngle"],
        "_340": ["PlanetaryDetail"],
        "_341": ["PlanetaryRatingLoadSharingOption"],
        "_342": ["PocketingPowerLossCoefficients"],
        "_343": ["PocketingPowerLossCoefficientsDatabase"],
        "_344": ["QualityGradeTypes"],
        "_345": ["SafetyRequirementsAGMA"],
        "_346": ["SpecificationForTheEffectOfOilKinematicViscosity"],
        "_347": ["SpiralBevelRootLineTilt"],
        "_348": ["SpiralBevelToothTaper"],
        "_349": ["TESpecificationType"],
        "_350": ["WormAddendumFactor"],
        "_351": ["WormType"],
        "_352": ["ZerolBevelGleasonToothTaperOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AccuracyGrades",
    "AGMAToleranceStandard",
    "BevelHypoidGearDesignSettings",
    "BevelHypoidGearRatingSettings",
    "CentreDistanceChangeMethod",
    "CoefficientOfFrictionCalculationMethod",
    "ConicalGearToothSurface",
    "ContactRatioDataSource",
    "ContactRatioRequirements",
    "CylindricalFlanks",
    "CylindricalMisalignmentDataSource",
    "DeflectionFromBendingOption",
    "GearFlanks",
    "GearNURBSSurface",
    "GearSetDesignGroup",
    "GearSetModes",
    "GearSetOptimisationResult",
    "GearSetOptimisationResults",
    "GearSetOptimiser",
    "Hand",
    "ISOToleranceStandard",
    "LubricationMethods",
    "MicroGeometryInputTypes",
    "MicroGeometryModel",
    "MicropittingCoefficientOfFrictionCalculationMethod",
    "NamedPlanetAngle",
    "PlanetaryDetail",
    "PlanetaryRatingLoadSharingOption",
    "PocketingPowerLossCoefficients",
    "PocketingPowerLossCoefficientsDatabase",
    "QualityGradeTypes",
    "SafetyRequirementsAGMA",
    "SpecificationForTheEffectOfOilKinematicViscosity",
    "SpiralBevelRootLineTilt",
    "SpiralBevelToothTaper",
    "TESpecificationType",
    "WormAddendumFactor",
    "WormType",
    "ZerolBevelGleasonToothTaperOption",
)

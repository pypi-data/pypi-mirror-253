"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._451 import AGMAScuffingResultsRow
    from ._452 import CylindricalGearDesignAndRatingSettings
    from ._453 import CylindricalGearDesignAndRatingSettingsDatabase
    from ._454 import CylindricalGearDesignAndRatingSettingsItem
    from ._455 import CylindricalGearDutyCycleRating
    from ._456 import CylindricalGearFlankDutyCycleRating
    from ._457 import CylindricalGearFlankRating
    from ._458 import CylindricalGearMeshRating
    from ._459 import CylindricalGearMicroPittingResults
    from ._460 import CylindricalGearRating
    from ._461 import CylindricalGearRatingGeometryDataSource
    from ._462 import CylindricalGearScuffingResults
    from ._463 import CylindricalGearSetDutyCycleRating
    from ._464 import CylindricalGearSetRating
    from ._465 import CylindricalGearSingleFlankRating
    from ._466 import CylindricalMeshDutyCycleRating
    from ._467 import CylindricalMeshSingleFlankRating
    from ._468 import CylindricalPlasticGearRatingSettings
    from ._469 import CylindricalPlasticGearRatingSettingsDatabase
    from ._470 import CylindricalPlasticGearRatingSettingsItem
    from ._471 import CylindricalRateableMesh
    from ._472 import DynamicFactorMethods
    from ._473 import GearBlankFactorCalculationOptions
    from ._474 import ISOScuffingResultsRow
    from ._475 import MeshRatingForReports
    from ._476 import MicropittingRatingMethod
    from ._477 import MicroPittingResultsRow
    from ._478 import MisalignmentContactPatternEnhancements
    from ._479 import RatingMethod
    from ._480 import ReducedCylindricalGearSetDutyCycleRating
    from ._481 import ScuffingFlashTemperatureRatingMethod
    from ._482 import ScuffingIntegralTemperatureRatingMethod
    from ._483 import ScuffingMethods
    from ._484 import ScuffingResultsRow
    from ._485 import ScuffingResultsRowGear
    from ._486 import TipReliefScuffingOptions
    from ._487 import ToothThicknesses
    from ._488 import VDI2737SafetyFactorReportingObject
else:
    import_structure = {
        "_451": ["AGMAScuffingResultsRow"],
        "_452": ["CylindricalGearDesignAndRatingSettings"],
        "_453": ["CylindricalGearDesignAndRatingSettingsDatabase"],
        "_454": ["CylindricalGearDesignAndRatingSettingsItem"],
        "_455": ["CylindricalGearDutyCycleRating"],
        "_456": ["CylindricalGearFlankDutyCycleRating"],
        "_457": ["CylindricalGearFlankRating"],
        "_458": ["CylindricalGearMeshRating"],
        "_459": ["CylindricalGearMicroPittingResults"],
        "_460": ["CylindricalGearRating"],
        "_461": ["CylindricalGearRatingGeometryDataSource"],
        "_462": ["CylindricalGearScuffingResults"],
        "_463": ["CylindricalGearSetDutyCycleRating"],
        "_464": ["CylindricalGearSetRating"],
        "_465": ["CylindricalGearSingleFlankRating"],
        "_466": ["CylindricalMeshDutyCycleRating"],
        "_467": ["CylindricalMeshSingleFlankRating"],
        "_468": ["CylindricalPlasticGearRatingSettings"],
        "_469": ["CylindricalPlasticGearRatingSettingsDatabase"],
        "_470": ["CylindricalPlasticGearRatingSettingsItem"],
        "_471": ["CylindricalRateableMesh"],
        "_472": ["DynamicFactorMethods"],
        "_473": ["GearBlankFactorCalculationOptions"],
        "_474": ["ISOScuffingResultsRow"],
        "_475": ["MeshRatingForReports"],
        "_476": ["MicropittingRatingMethod"],
        "_477": ["MicroPittingResultsRow"],
        "_478": ["MisalignmentContactPatternEnhancements"],
        "_479": ["RatingMethod"],
        "_480": ["ReducedCylindricalGearSetDutyCycleRating"],
        "_481": ["ScuffingFlashTemperatureRatingMethod"],
        "_482": ["ScuffingIntegralTemperatureRatingMethod"],
        "_483": ["ScuffingMethods"],
        "_484": ["ScuffingResultsRow"],
        "_485": ["ScuffingResultsRowGear"],
        "_486": ["TipReliefScuffingOptions"],
        "_487": ["ToothThicknesses"],
        "_488": ["VDI2737SafetyFactorReportingObject"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAScuffingResultsRow",
    "CylindricalGearDesignAndRatingSettings",
    "CylindricalGearDesignAndRatingSettingsDatabase",
    "CylindricalGearDesignAndRatingSettingsItem",
    "CylindricalGearDutyCycleRating",
    "CylindricalGearFlankDutyCycleRating",
    "CylindricalGearFlankRating",
    "CylindricalGearMeshRating",
    "CylindricalGearMicroPittingResults",
    "CylindricalGearRating",
    "CylindricalGearRatingGeometryDataSource",
    "CylindricalGearScuffingResults",
    "CylindricalGearSetDutyCycleRating",
    "CylindricalGearSetRating",
    "CylindricalGearSingleFlankRating",
    "CylindricalMeshDutyCycleRating",
    "CylindricalMeshSingleFlankRating",
    "CylindricalPlasticGearRatingSettings",
    "CylindricalPlasticGearRatingSettingsDatabase",
    "CylindricalPlasticGearRatingSettingsItem",
    "CylindricalRateableMesh",
    "DynamicFactorMethods",
    "GearBlankFactorCalculationOptions",
    "ISOScuffingResultsRow",
    "MeshRatingForReports",
    "MicropittingRatingMethod",
    "MicroPittingResultsRow",
    "MisalignmentContactPatternEnhancements",
    "RatingMethod",
    "ReducedCylindricalGearSetDutyCycleRating",
    "ScuffingFlashTemperatureRatingMethod",
    "ScuffingIntegralTemperatureRatingMethod",
    "ScuffingMethods",
    "ScuffingResultsRow",
    "ScuffingResultsRowGear",
    "TipReliefScuffingOptions",
    "ToothThicknesses",
    "VDI2737SafetyFactorReportingObject",
)

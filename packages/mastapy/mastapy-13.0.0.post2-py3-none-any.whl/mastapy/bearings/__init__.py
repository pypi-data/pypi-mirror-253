"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1869 import BearingCatalog
    from ._1870 import BasicDynamicLoadRatingCalculationMethod
    from ._1871 import BasicStaticLoadRatingCalculationMethod
    from ._1872 import BearingCageMaterial
    from ._1873 import BearingDampingMatrixOption
    from ._1874 import BearingLoadCaseResultsForPST
    from ._1875 import BearingLoadCaseResultsLightweight
    from ._1876 import BearingMeasurementType
    from ._1877 import BearingModel
    from ._1878 import BearingRow
    from ._1879 import BearingSettings
    from ._1880 import BearingSettingsDatabase
    from ._1881 import BearingSettingsItem
    from ._1882 import BearingStiffnessMatrixOption
    from ._1883 import ExponentAndReductionFactorsInISO16281Calculation
    from ._1884 import FluidFilmTemperatureOptions
    from ._1885 import HybridSteelAll
    from ._1886 import JournalBearingType
    from ._1887 import JournalOilFeedType
    from ._1888 import MountingPointSurfaceFinishes
    from ._1889 import OuterRingMounting
    from ._1890 import RatingLife
    from ._1891 import RollerBearingProfileTypes
    from ._1892 import RollingBearingArrangement
    from ._1893 import RollingBearingDatabase
    from ._1894 import RollingBearingKey
    from ._1895 import RollingBearingRaceType
    from ._1896 import RollingBearingType
    from ._1897 import RotationalDirections
    from ._1898 import SealLocation
    from ._1899 import SKFSettings
    from ._1900 import TiltingPadTypes
else:
    import_structure = {
        "_1869": ["BearingCatalog"],
        "_1870": ["BasicDynamicLoadRatingCalculationMethod"],
        "_1871": ["BasicStaticLoadRatingCalculationMethod"],
        "_1872": ["BearingCageMaterial"],
        "_1873": ["BearingDampingMatrixOption"],
        "_1874": ["BearingLoadCaseResultsForPST"],
        "_1875": ["BearingLoadCaseResultsLightweight"],
        "_1876": ["BearingMeasurementType"],
        "_1877": ["BearingModel"],
        "_1878": ["BearingRow"],
        "_1879": ["BearingSettings"],
        "_1880": ["BearingSettingsDatabase"],
        "_1881": ["BearingSettingsItem"],
        "_1882": ["BearingStiffnessMatrixOption"],
        "_1883": ["ExponentAndReductionFactorsInISO16281Calculation"],
        "_1884": ["FluidFilmTemperatureOptions"],
        "_1885": ["HybridSteelAll"],
        "_1886": ["JournalBearingType"],
        "_1887": ["JournalOilFeedType"],
        "_1888": ["MountingPointSurfaceFinishes"],
        "_1889": ["OuterRingMounting"],
        "_1890": ["RatingLife"],
        "_1891": ["RollerBearingProfileTypes"],
        "_1892": ["RollingBearingArrangement"],
        "_1893": ["RollingBearingDatabase"],
        "_1894": ["RollingBearingKey"],
        "_1895": ["RollingBearingRaceType"],
        "_1896": ["RollingBearingType"],
        "_1897": ["RotationalDirections"],
        "_1898": ["SealLocation"],
        "_1899": ["SKFSettings"],
        "_1900": ["TiltingPadTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingCatalog",
    "BasicDynamicLoadRatingCalculationMethod",
    "BasicStaticLoadRatingCalculationMethod",
    "BearingCageMaterial",
    "BearingDampingMatrixOption",
    "BearingLoadCaseResultsForPST",
    "BearingLoadCaseResultsLightweight",
    "BearingMeasurementType",
    "BearingModel",
    "BearingRow",
    "BearingSettings",
    "BearingSettingsDatabase",
    "BearingSettingsItem",
    "BearingStiffnessMatrixOption",
    "ExponentAndReductionFactorsInISO16281Calculation",
    "FluidFilmTemperatureOptions",
    "HybridSteelAll",
    "JournalBearingType",
    "JournalOilFeedType",
    "MountingPointSurfaceFinishes",
    "OuterRingMounting",
    "RatingLife",
    "RollerBearingProfileTypes",
    "RollingBearingArrangement",
    "RollingBearingDatabase",
    "RollingBearingKey",
    "RollingBearingRaceType",
    "RollingBearingType",
    "RotationalDirections",
    "SealLocation",
    "SKFSettings",
    "TiltingPadTypes",
)

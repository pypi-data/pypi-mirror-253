"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1388 import CustomSplineHalfDesign
    from ._1389 import CustomSplineJointDesign
    from ._1390 import DetailedSplineJointSettings
    from ._1391 import DIN5480SplineHalfDesign
    from ._1392 import DIN5480SplineJointDesign
    from ._1393 import DudleyEffectiveLengthApproximationOption
    from ._1394 import FitTypes
    from ._1395 import GBT3478SplineHalfDesign
    from ._1396 import GBT3478SplineJointDesign
    from ._1397 import HeatTreatmentTypes
    from ._1398 import ISO4156SplineHalfDesign
    from ._1399 import ISO4156SplineJointDesign
    from ._1400 import JISB1603SplineJointDesign
    from ._1401 import ManufacturingTypes
    from ._1402 import Modules
    from ._1403 import PressureAngleTypes
    from ._1404 import RootTypes
    from ._1405 import SAEFatigueLifeFactorTypes
    from ._1406 import SAESplineHalfDesign
    from ._1407 import SAESplineJointDesign
    from ._1408 import SAETorqueCycles
    from ._1409 import SplineDesignTypes
    from ._1410 import FinishingMethods
    from ._1411 import SplineFitClassType
    from ._1412 import SplineFixtureTypes
    from ._1413 import SplineHalfDesign
    from ._1414 import SplineJointDesign
    from ._1415 import SplineMaterial
    from ._1416 import SplineRatingTypes
    from ._1417 import SplineToleranceClassTypes
    from ._1418 import StandardSplineHalfDesign
    from ._1419 import StandardSplineJointDesign
else:
    import_structure = {
        "_1388": ["CustomSplineHalfDesign"],
        "_1389": ["CustomSplineJointDesign"],
        "_1390": ["DetailedSplineJointSettings"],
        "_1391": ["DIN5480SplineHalfDesign"],
        "_1392": ["DIN5480SplineJointDesign"],
        "_1393": ["DudleyEffectiveLengthApproximationOption"],
        "_1394": ["FitTypes"],
        "_1395": ["GBT3478SplineHalfDesign"],
        "_1396": ["GBT3478SplineJointDesign"],
        "_1397": ["HeatTreatmentTypes"],
        "_1398": ["ISO4156SplineHalfDesign"],
        "_1399": ["ISO4156SplineJointDesign"],
        "_1400": ["JISB1603SplineJointDesign"],
        "_1401": ["ManufacturingTypes"],
        "_1402": ["Modules"],
        "_1403": ["PressureAngleTypes"],
        "_1404": ["RootTypes"],
        "_1405": ["SAEFatigueLifeFactorTypes"],
        "_1406": ["SAESplineHalfDesign"],
        "_1407": ["SAESplineJointDesign"],
        "_1408": ["SAETorqueCycles"],
        "_1409": ["SplineDesignTypes"],
        "_1410": ["FinishingMethods"],
        "_1411": ["SplineFitClassType"],
        "_1412": ["SplineFixtureTypes"],
        "_1413": ["SplineHalfDesign"],
        "_1414": ["SplineJointDesign"],
        "_1415": ["SplineMaterial"],
        "_1416": ["SplineRatingTypes"],
        "_1417": ["SplineToleranceClassTypes"],
        "_1418": ["StandardSplineHalfDesign"],
        "_1419": ["StandardSplineJointDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CustomSplineHalfDesign",
    "CustomSplineJointDesign",
    "DetailedSplineJointSettings",
    "DIN5480SplineHalfDesign",
    "DIN5480SplineJointDesign",
    "DudleyEffectiveLengthApproximationOption",
    "FitTypes",
    "GBT3478SplineHalfDesign",
    "GBT3478SplineJointDesign",
    "HeatTreatmentTypes",
    "ISO4156SplineHalfDesign",
    "ISO4156SplineJointDesign",
    "JISB1603SplineJointDesign",
    "ManufacturingTypes",
    "Modules",
    "PressureAngleTypes",
    "RootTypes",
    "SAEFatigueLifeFactorTypes",
    "SAESplineHalfDesign",
    "SAESplineJointDesign",
    "SAETorqueCycles",
    "SplineDesignTypes",
    "FinishingMethods",
    "SplineFitClassType",
    "SplineFixtureTypes",
    "SplineHalfDesign",
    "SplineJointDesign",
    "SplineMaterial",
    "SplineRatingTypes",
    "SplineToleranceClassTypes",
    "StandardSplineHalfDesign",
    "StandardSplineJointDesign",
)

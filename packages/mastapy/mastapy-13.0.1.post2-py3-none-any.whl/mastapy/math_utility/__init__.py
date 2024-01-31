"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1488 import Range
    from ._1489 import AcousticWeighting
    from ._1490 import AlignmentAxis
    from ._1491 import Axis
    from ._1492 import CirclesOnAxis
    from ._1493 import ComplexMatrix
    from ._1494 import ComplexPartDisplayOption
    from ._1495 import ComplexVector
    from ._1496 import ComplexVector3D
    from ._1497 import ComplexVector6D
    from ._1498 import CoordinateSystem3D
    from ._1499 import CoordinateSystemEditor
    from ._1500 import CoordinateSystemForRotation
    from ._1501 import CoordinateSystemForRotationOrigin
    from ._1502 import DataPrecision
    from ._1503 import DegreeOfFreedom
    from ._1504 import DynamicsResponseScalarResult
    from ._1505 import DynamicsResponseScaling
    from ._1506 import Eigenmode
    from ._1507 import Eigenmodes
    from ._1508 import EulerParameters
    from ._1509 import ExtrapolationOptions
    from ._1510 import FacetedBody
    from ._1511 import FacetedSurface
    from ._1512 import FourierSeries
    from ._1513 import GenericMatrix
    from ._1514 import GriddedSurface
    from ._1515 import HarmonicValue
    from ._1516 import InertiaTensor
    from ._1517 import MassProperties
    from ._1518 import MaxMinMean
    from ._1519 import ComplexMagnitudeMethod
    from ._1520 import MultipleFourierSeriesInterpolator
    from ._1521 import Named2DLocation
    from ._1522 import PIDControlUpdateMethod
    from ._1523 import Quaternion
    from ._1524 import RealMatrix
    from ._1525 import RealVector
    from ._1526 import ResultOptionsFor3DVector
    from ._1527 import RotationAxis
    from ._1528 import RoundedOrder
    from ._1529 import SinCurve
    from ._1530 import SquareMatrix
    from ._1531 import StressPoint
    from ._1532 import TransformMatrix3D
    from ._1533 import TranslationRotation
    from ._1534 import Vector2DListAccessor
    from ._1535 import Vector6D
else:
    import_structure = {
        "_1488": ["Range"],
        "_1489": ["AcousticWeighting"],
        "_1490": ["AlignmentAxis"],
        "_1491": ["Axis"],
        "_1492": ["CirclesOnAxis"],
        "_1493": ["ComplexMatrix"],
        "_1494": ["ComplexPartDisplayOption"],
        "_1495": ["ComplexVector"],
        "_1496": ["ComplexVector3D"],
        "_1497": ["ComplexVector6D"],
        "_1498": ["CoordinateSystem3D"],
        "_1499": ["CoordinateSystemEditor"],
        "_1500": ["CoordinateSystemForRotation"],
        "_1501": ["CoordinateSystemForRotationOrigin"],
        "_1502": ["DataPrecision"],
        "_1503": ["DegreeOfFreedom"],
        "_1504": ["DynamicsResponseScalarResult"],
        "_1505": ["DynamicsResponseScaling"],
        "_1506": ["Eigenmode"],
        "_1507": ["Eigenmodes"],
        "_1508": ["EulerParameters"],
        "_1509": ["ExtrapolationOptions"],
        "_1510": ["FacetedBody"],
        "_1511": ["FacetedSurface"],
        "_1512": ["FourierSeries"],
        "_1513": ["GenericMatrix"],
        "_1514": ["GriddedSurface"],
        "_1515": ["HarmonicValue"],
        "_1516": ["InertiaTensor"],
        "_1517": ["MassProperties"],
        "_1518": ["MaxMinMean"],
        "_1519": ["ComplexMagnitudeMethod"],
        "_1520": ["MultipleFourierSeriesInterpolator"],
        "_1521": ["Named2DLocation"],
        "_1522": ["PIDControlUpdateMethod"],
        "_1523": ["Quaternion"],
        "_1524": ["RealMatrix"],
        "_1525": ["RealVector"],
        "_1526": ["ResultOptionsFor3DVector"],
        "_1527": ["RotationAxis"],
        "_1528": ["RoundedOrder"],
        "_1529": ["SinCurve"],
        "_1530": ["SquareMatrix"],
        "_1531": ["StressPoint"],
        "_1532": ["TransformMatrix3D"],
        "_1533": ["TranslationRotation"],
        "_1534": ["Vector2DListAccessor"],
        "_1535": ["Vector6D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Range",
    "AcousticWeighting",
    "AlignmentAxis",
    "Axis",
    "CirclesOnAxis",
    "ComplexMatrix",
    "ComplexPartDisplayOption",
    "ComplexVector",
    "ComplexVector3D",
    "ComplexVector6D",
    "CoordinateSystem3D",
    "CoordinateSystemEditor",
    "CoordinateSystemForRotation",
    "CoordinateSystemForRotationOrigin",
    "DataPrecision",
    "DegreeOfFreedom",
    "DynamicsResponseScalarResult",
    "DynamicsResponseScaling",
    "Eigenmode",
    "Eigenmodes",
    "EulerParameters",
    "ExtrapolationOptions",
    "FacetedBody",
    "FacetedSurface",
    "FourierSeries",
    "GenericMatrix",
    "GriddedSurface",
    "HarmonicValue",
    "InertiaTensor",
    "MassProperties",
    "MaxMinMean",
    "ComplexMagnitudeMethod",
    "MultipleFourierSeriesInterpolator",
    "Named2DLocation",
    "PIDControlUpdateMethod",
    "Quaternion",
    "RealMatrix",
    "RealVector",
    "ResultOptionsFor3DVector",
    "RotationAxis",
    "RoundedOrder",
    "SinCurve",
    "SquareMatrix",
    "StressPoint",
    "TransformMatrix3D",
    "TranslationRotation",
    "Vector2DListAccessor",
    "Vector6D",
)

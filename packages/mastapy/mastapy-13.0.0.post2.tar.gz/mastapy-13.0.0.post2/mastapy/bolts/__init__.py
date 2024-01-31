"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1464 import AxialLoadType
    from ._1465 import BoltedJointMaterial
    from ._1466 import BoltedJointMaterialDatabase
    from ._1467 import BoltGeometry
    from ._1468 import BoltGeometryDatabase
    from ._1469 import BoltMaterial
    from ._1470 import BoltMaterialDatabase
    from ._1471 import BoltSection
    from ._1472 import BoltShankType
    from ._1473 import BoltTypes
    from ._1474 import ClampedSection
    from ._1475 import ClampedSectionMaterialDatabase
    from ._1476 import DetailedBoltDesign
    from ._1477 import DetailedBoltedJointDesign
    from ._1478 import HeadCapTypes
    from ._1479 import JointGeometries
    from ._1480 import JointTypes
    from ._1481 import LoadedBolt
    from ._1482 import RolledBeforeOrAfterHeatTreatment
    from ._1483 import StandardSizes
    from ._1484 import StrengthGrades
    from ._1485 import ThreadTypes
    from ._1486 import TighteningTechniques
else:
    import_structure = {
        "_1464": ["AxialLoadType"],
        "_1465": ["BoltedJointMaterial"],
        "_1466": ["BoltedJointMaterialDatabase"],
        "_1467": ["BoltGeometry"],
        "_1468": ["BoltGeometryDatabase"],
        "_1469": ["BoltMaterial"],
        "_1470": ["BoltMaterialDatabase"],
        "_1471": ["BoltSection"],
        "_1472": ["BoltShankType"],
        "_1473": ["BoltTypes"],
        "_1474": ["ClampedSection"],
        "_1475": ["ClampedSectionMaterialDatabase"],
        "_1476": ["DetailedBoltDesign"],
        "_1477": ["DetailedBoltedJointDesign"],
        "_1478": ["HeadCapTypes"],
        "_1479": ["JointGeometries"],
        "_1480": ["JointTypes"],
        "_1481": ["LoadedBolt"],
        "_1482": ["RolledBeforeOrAfterHeatTreatment"],
        "_1483": ["StandardSizes"],
        "_1484": ["StrengthGrades"],
        "_1485": ["ThreadTypes"],
        "_1486": ["TighteningTechniques"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialLoadType",
    "BoltedJointMaterial",
    "BoltedJointMaterialDatabase",
    "BoltGeometry",
    "BoltGeometryDatabase",
    "BoltMaterial",
    "BoltMaterialDatabase",
    "BoltSection",
    "BoltShankType",
    "BoltTypes",
    "ClampedSection",
    "ClampedSectionMaterialDatabase",
    "DetailedBoltDesign",
    "DetailedBoltedJointDesign",
    "HeadCapTypes",
    "JointGeometries",
    "JointTypes",
    "LoadedBolt",
    "RolledBeforeOrAfterHeatTreatment",
    "StandardSizes",
    "StrengthGrades",
    "ThreadTypes",
    "TighteningTechniques",
)

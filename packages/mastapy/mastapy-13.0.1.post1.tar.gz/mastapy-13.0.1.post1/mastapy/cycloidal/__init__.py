"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1450 import ContactSpecification
    from ._1451 import CrowningSpecificationMethod
    from ._1452 import CycloidalAssemblyDesign
    from ._1453 import CycloidalDiscDesign
    from ._1454 import CycloidalDiscDesignExporter
    from ._1455 import CycloidalDiscMaterial
    from ._1456 import CycloidalDiscMaterialDatabase
    from ._1457 import CycloidalDiscModificationsSpecification
    from ._1458 import DirectionOfMeasuredModifications
    from ._1459 import GeometryToExport
    from ._1460 import NamedDiscPhase
    from ._1461 import RingPinsDesign
    from ._1462 import RingPinsMaterial
    from ._1463 import RingPinsMaterialDatabase
else:
    import_structure = {
        "_1450": ["ContactSpecification"],
        "_1451": ["CrowningSpecificationMethod"],
        "_1452": ["CycloidalAssemblyDesign"],
        "_1453": ["CycloidalDiscDesign"],
        "_1454": ["CycloidalDiscDesignExporter"],
        "_1455": ["CycloidalDiscMaterial"],
        "_1456": ["CycloidalDiscMaterialDatabase"],
        "_1457": ["CycloidalDiscModificationsSpecification"],
        "_1458": ["DirectionOfMeasuredModifications"],
        "_1459": ["GeometryToExport"],
        "_1460": ["NamedDiscPhase"],
        "_1461": ["RingPinsDesign"],
        "_1462": ["RingPinsMaterial"],
        "_1463": ["RingPinsMaterialDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactSpecification",
    "CrowningSpecificationMethod",
    "CycloidalAssemblyDesign",
    "CycloidalDiscDesign",
    "CycloidalDiscDesignExporter",
    "CycloidalDiscMaterial",
    "CycloidalDiscMaterialDatabase",
    "CycloidalDiscModificationsSpecification",
    "DirectionOfMeasuredModifications",
    "GeometryToExport",
    "NamedDiscPhase",
    "RingPinsDesign",
    "RingPinsMaterial",
    "RingPinsMaterialDatabase",
)

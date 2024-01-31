"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._723 import CutterShapeDefinition
    from ._724 import CylindricalGearFormedWheelGrinderTangible
    from ._725 import CylindricalGearHobShape
    from ._726 import CylindricalGearShaperTangible
    from ._727 import CylindricalGearShaverTangible
    from ._728 import CylindricalGearWormGrinderShape
    from ._729 import NamedPoint
    from ._730 import RackShape
else:
    import_structure = {
        "_723": ["CutterShapeDefinition"],
        "_724": ["CylindricalGearFormedWheelGrinderTangible"],
        "_725": ["CylindricalGearHobShape"],
        "_726": ["CylindricalGearShaperTangible"],
        "_727": ["CylindricalGearShaverTangible"],
        "_728": ["CylindricalGearWormGrinderShape"],
        "_729": ["NamedPoint"],
        "_730": ["RackShape"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterShapeDefinition",
    "CylindricalGearFormedWheelGrinderTangible",
    "CylindricalGearHobShape",
    "CylindricalGearShaperTangible",
    "CylindricalGearShaverTangible",
    "CylindricalGearWormGrinderShape",
    "NamedPoint",
    "RackShape",
)

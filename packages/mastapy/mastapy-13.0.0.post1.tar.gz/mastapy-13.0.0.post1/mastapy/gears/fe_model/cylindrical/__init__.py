"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1201 import CylindricalGearFEModel
    from ._1202 import CylindricalGearMeshFEModel
    from ._1203 import CylindricalGearSetFEModel
else:
    import_structure = {
        "_1201": ["CylindricalGearFEModel"],
        "_1202": ["CylindricalGearMeshFEModel"],
        "_1203": ["CylindricalGearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearFEModel",
    "CylindricalGearMeshFEModel",
    "CylindricalGearSetFEModel",
)

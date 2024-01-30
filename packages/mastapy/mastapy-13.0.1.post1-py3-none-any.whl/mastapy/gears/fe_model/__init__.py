"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1197 import GearFEModel
    from ._1198 import GearMeshFEModel
    from ._1199 import GearMeshingElementOptions
    from ._1200 import GearSetFEModel
else:
    import_structure = {
        "_1197": ["GearFEModel"],
        "_1198": ["GearMeshFEModel"],
        "_1199": ["GearMeshingElementOptions"],
        "_1200": ["GearSetFEModel"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearFEModel",
    "GearMeshFEModel",
    "GearMeshingElementOptions",
    "GearSetFEModel",
)

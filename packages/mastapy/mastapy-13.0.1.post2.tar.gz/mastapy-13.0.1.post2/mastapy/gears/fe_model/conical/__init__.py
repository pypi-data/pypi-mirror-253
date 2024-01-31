"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1204 import ConicalGearFEModel
    from ._1205 import ConicalMeshFEModel
    from ._1206 import ConicalSetFEModel
    from ._1207 import FlankDataSource
else:
    import_structure = {
        "_1204": ["ConicalGearFEModel"],
        "_1205": ["ConicalMeshFEModel"],
        "_1206": ["ConicalSetFEModel"],
        "_1207": ["FlankDataSource"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFEModel",
    "ConicalMeshFEModel",
    "ConicalSetFEModel",
    "FlankDataSource",
)

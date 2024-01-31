"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1536 import IndividualContactPosition
    from ._1537 import SurfaceToSurfaceContact
else:
    import_structure = {
        "_1536": ["IndividualContactPosition"],
        "_1537": ["SurfaceToSurfaceContact"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "IndividualContactPosition",
    "SurfaceToSurfaceContact",
)

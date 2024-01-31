"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._395 import StraightBevelGearMeshRating
    from ._396 import StraightBevelGearRating
    from ._397 import StraightBevelGearSetRating
else:
    import_structure = {
        "_395": ["StraightBevelGearMeshRating"],
        "_396": ["StraightBevelGearRating"],
        "_397": ["StraightBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelGearMeshRating",
    "StraightBevelGearRating",
    "StraightBevelGearSetRating",
)

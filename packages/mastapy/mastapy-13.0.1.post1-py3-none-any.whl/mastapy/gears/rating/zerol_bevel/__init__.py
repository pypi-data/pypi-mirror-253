"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._369 import ZerolBevelGearMeshRating
    from ._370 import ZerolBevelGearRating
    from ._371 import ZerolBevelGearSetRating
else:
    import_structure = {
        "_369": ["ZerolBevelGearMeshRating"],
        "_370": ["ZerolBevelGearRating"],
        "_371": ["ZerolBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ZerolBevelGearMeshRating",
    "ZerolBevelGearRating",
    "ZerolBevelGearSetRating",
)

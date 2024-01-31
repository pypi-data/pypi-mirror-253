"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._402 import SpiralBevelGearMeshRating
    from ._403 import SpiralBevelGearRating
    from ._404 import SpiralBevelGearSetRating
else:
    import_structure = {
        "_402": ["SpiralBevelGearMeshRating"],
        "_403": ["SpiralBevelGearRating"],
        "_404": ["SpiralBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpiralBevelGearMeshRating",
    "SpiralBevelGearRating",
    "SpiralBevelGearSetRating",
)

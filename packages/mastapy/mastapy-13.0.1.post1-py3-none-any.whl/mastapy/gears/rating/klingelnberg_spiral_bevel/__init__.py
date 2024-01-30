"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._405 import KlingelnbergCycloPalloidSpiralBevelGearMeshRating
    from ._406 import KlingelnbergCycloPalloidSpiralBevelGearRating
    from ._407 import KlingelnbergCycloPalloidSpiralBevelGearSetRating
else:
    import_structure = {
        "_405": ["KlingelnbergCycloPalloidSpiralBevelGearMeshRating"],
        "_406": ["KlingelnbergCycloPalloidSpiralBevelGearRating"],
        "_407": ["KlingelnbergCycloPalloidSpiralBevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearMeshRating",
    "KlingelnbergCycloPalloidSpiralBevelGearRating",
    "KlingelnbergCycloPalloidSpiralBevelGearSetRating",
)

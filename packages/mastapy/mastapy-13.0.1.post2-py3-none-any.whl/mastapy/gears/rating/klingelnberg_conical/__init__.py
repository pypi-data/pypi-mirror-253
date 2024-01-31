"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._411 import KlingelnbergCycloPalloidConicalGearMeshRating
    from ._412 import KlingelnbergCycloPalloidConicalGearRating
    from ._413 import KlingelnbergCycloPalloidConicalGearSetRating
else:
    import_structure = {
        "_411": ["KlingelnbergCycloPalloidConicalGearMeshRating"],
        "_412": ["KlingelnbergCycloPalloidConicalGearRating"],
        "_413": ["KlingelnbergCycloPalloidConicalGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidConicalGearMeshRating",
    "KlingelnbergCycloPalloidConicalGearRating",
    "KlingelnbergCycloPalloidConicalGearSetRating",
)

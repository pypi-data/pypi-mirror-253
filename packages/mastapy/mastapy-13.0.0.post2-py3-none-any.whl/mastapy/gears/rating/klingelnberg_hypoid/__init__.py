"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._408 import KlingelnbergCycloPalloidHypoidGearMeshRating
    from ._409 import KlingelnbergCycloPalloidHypoidGearRating
    from ._410 import KlingelnbergCycloPalloidHypoidGearSetRating
else:
    import_structure = {
        "_408": ["KlingelnbergCycloPalloidHypoidGearMeshRating"],
        "_409": ["KlingelnbergCycloPalloidHypoidGearRating"],
        "_410": ["KlingelnbergCycloPalloidHypoidGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidHypoidGearMeshRating",
    "KlingelnbergCycloPalloidHypoidGearRating",
    "KlingelnbergCycloPalloidHypoidGearSetRating",
)

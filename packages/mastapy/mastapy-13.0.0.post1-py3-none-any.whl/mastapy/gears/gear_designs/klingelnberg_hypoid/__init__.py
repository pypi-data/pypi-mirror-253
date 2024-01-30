"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._977 import KlingelnbergCycloPalloidHypoidGearDesign
    from ._978 import KlingelnbergCycloPalloidHypoidGearMeshDesign
    from ._979 import KlingelnbergCycloPalloidHypoidGearSetDesign
    from ._980 import KlingelnbergCycloPalloidHypoidMeshedGearDesign
else:
    import_structure = {
        "_977": ["KlingelnbergCycloPalloidHypoidGearDesign"],
        "_978": ["KlingelnbergCycloPalloidHypoidGearMeshDesign"],
        "_979": ["KlingelnbergCycloPalloidHypoidGearSetDesign"],
        "_980": ["KlingelnbergCycloPalloidHypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidHypoidGearDesign",
    "KlingelnbergCycloPalloidHypoidGearMeshDesign",
    "KlingelnbergCycloPalloidHypoidGearSetDesign",
    "KlingelnbergCycloPalloidHypoidMeshedGearDesign",
)

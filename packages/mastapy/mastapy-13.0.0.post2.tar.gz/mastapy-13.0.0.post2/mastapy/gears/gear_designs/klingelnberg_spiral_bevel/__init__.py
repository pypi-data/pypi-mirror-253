"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._973 import KlingelnbergCycloPalloidSpiralBevelGearDesign
    from ._974 import KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
    from ._975 import KlingelnbergCycloPalloidSpiralBevelGearSetDesign
    from ._976 import KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_973": ["KlingelnbergCycloPalloidSpiralBevelGearDesign"],
        "_974": ["KlingelnbergCycloPalloidSpiralBevelGearMeshDesign"],
        "_975": ["KlingelnbergCycloPalloidSpiralBevelGearSetDesign"],
        "_976": ["KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergCycloPalloidSpiralBevelGearDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshDesign",
    "KlingelnbergCycloPalloidSpiralBevelGearSetDesign",
    "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
)

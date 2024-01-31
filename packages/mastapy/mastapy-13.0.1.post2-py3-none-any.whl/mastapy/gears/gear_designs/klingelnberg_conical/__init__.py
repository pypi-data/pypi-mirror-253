"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._981 import KlingelnbergConicalGearDesign
    from ._982 import KlingelnbergConicalGearMeshDesign
    from ._983 import KlingelnbergConicalGearSetDesign
    from ._984 import KlingelnbergConicalMeshedGearDesign
else:
    import_structure = {
        "_981": ["KlingelnbergConicalGearDesign"],
        "_982": ["KlingelnbergConicalGearMeshDesign"],
        "_983": ["KlingelnbergConicalGearSetDesign"],
        "_984": ["KlingelnbergConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergConicalGearDesign",
    "KlingelnbergConicalGearMeshDesign",
    "KlingelnbergConicalGearSetDesign",
    "KlingelnbergConicalMeshedGearDesign",
)

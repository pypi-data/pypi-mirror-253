"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._956 import WormDesign
    from ._957 import WormGearDesign
    from ._958 import WormGearMeshDesign
    from ._959 import WormGearSetDesign
    from ._960 import WormWheelDesign
else:
    import_structure = {
        "_956": ["WormDesign"],
        "_957": ["WormGearDesign"],
        "_958": ["WormGearMeshDesign"],
        "_959": ["WormGearSetDesign"],
        "_960": ["WormWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormDesign",
    "WormGearDesign",
    "WormGearMeshDesign",
    "WormGearSetDesign",
    "WormWheelDesign",
)

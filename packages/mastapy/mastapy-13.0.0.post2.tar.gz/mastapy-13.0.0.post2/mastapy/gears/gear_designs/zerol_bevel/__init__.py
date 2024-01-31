"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._952 import ZerolBevelGearDesign
    from ._953 import ZerolBevelGearMeshDesign
    from ._954 import ZerolBevelGearSetDesign
    from ._955 import ZerolBevelMeshedGearDesign
else:
    import_structure = {
        "_952": ["ZerolBevelGearDesign"],
        "_953": ["ZerolBevelGearMeshDesign"],
        "_954": ["ZerolBevelGearSetDesign"],
        "_955": ["ZerolBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ZerolBevelGearDesign",
    "ZerolBevelGearMeshDesign",
    "ZerolBevelGearSetDesign",
    "ZerolBevelMeshedGearDesign",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._961 import StraightBevelGearDesign
    from ._962 import StraightBevelGearMeshDesign
    from ._963 import StraightBevelGearSetDesign
    from ._964 import StraightBevelMeshedGearDesign
else:
    import_structure = {
        "_961": ["StraightBevelGearDesign"],
        "_962": ["StraightBevelGearMeshDesign"],
        "_963": ["StraightBevelGearSetDesign"],
        "_964": ["StraightBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelGearDesign",
    "StraightBevelGearMeshDesign",
    "StraightBevelGearSetDesign",
    "StraightBevelMeshedGearDesign",
)

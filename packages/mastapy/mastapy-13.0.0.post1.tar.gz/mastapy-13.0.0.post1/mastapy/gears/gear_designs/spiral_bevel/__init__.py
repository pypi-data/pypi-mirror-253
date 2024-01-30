"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._969 import SpiralBevelGearDesign
    from ._970 import SpiralBevelGearMeshDesign
    from ._971 import SpiralBevelGearSetDesign
    from ._972 import SpiralBevelMeshedGearDesign
else:
    import_structure = {
        "_969": ["SpiralBevelGearDesign"],
        "_970": ["SpiralBevelGearMeshDesign"],
        "_971": ["SpiralBevelGearSetDesign"],
        "_972": ["SpiralBevelMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "SpiralBevelGearDesign",
    "SpiralBevelGearMeshDesign",
    "SpiralBevelGearSetDesign",
    "SpiralBevelMeshedGearDesign",
)

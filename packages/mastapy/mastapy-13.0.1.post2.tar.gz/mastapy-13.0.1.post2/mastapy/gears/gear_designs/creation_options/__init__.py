"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1146 import CylindricalGearPairCreationOptions
    from ._1147 import GearSetCreationOptions
    from ._1148 import HypoidGearSetCreationOptions
    from ._1149 import SpiralBevelGearSetCreationOptions
else:
    import_structure = {
        "_1146": ["CylindricalGearPairCreationOptions"],
        "_1147": ["GearSetCreationOptions"],
        "_1148": ["HypoidGearSetCreationOptions"],
        "_1149": ["SpiralBevelGearSetCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearPairCreationOptions",
    "GearSetCreationOptions",
    "HypoidGearSetCreationOptions",
    "SpiralBevelGearSetCreationOptions",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._557 import AGMASpiralBevelGearSingleFlankRating
    from ._558 import AGMASpiralBevelMeshSingleFlankRating
    from ._559 import GleasonSpiralBevelGearSingleFlankRating
    from ._560 import GleasonSpiralBevelMeshSingleFlankRating
    from ._561 import SpiralBevelGearSingleFlankRating
    from ._562 import SpiralBevelMeshSingleFlankRating
    from ._563 import SpiralBevelRateableGear
    from ._564 import SpiralBevelRateableMesh
else:
    import_structure = {
        "_557": ["AGMASpiralBevelGearSingleFlankRating"],
        "_558": ["AGMASpiralBevelMeshSingleFlankRating"],
        "_559": ["GleasonSpiralBevelGearSingleFlankRating"],
        "_560": ["GleasonSpiralBevelMeshSingleFlankRating"],
        "_561": ["SpiralBevelGearSingleFlankRating"],
        "_562": ["SpiralBevelMeshSingleFlankRating"],
        "_563": ["SpiralBevelRateableGear"],
        "_564": ["SpiralBevelRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMASpiralBevelGearSingleFlankRating",
    "AGMASpiralBevelMeshSingleFlankRating",
    "GleasonSpiralBevelGearSingleFlankRating",
    "GleasonSpiralBevelMeshSingleFlankRating",
    "SpiralBevelGearSingleFlankRating",
    "SpiralBevelMeshSingleFlankRating",
    "SpiralBevelRateableGear",
    "SpiralBevelRateableMesh",
)

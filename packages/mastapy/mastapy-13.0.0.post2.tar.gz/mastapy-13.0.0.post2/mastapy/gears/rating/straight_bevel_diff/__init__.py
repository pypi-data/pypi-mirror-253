"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._398 import StraightBevelDiffGearMeshRating
    from ._399 import StraightBevelDiffGearRating
    from ._400 import StraightBevelDiffGearSetRating
    from ._401 import StraightBevelDiffMeshedGearRating
else:
    import_structure = {
        "_398": ["StraightBevelDiffGearMeshRating"],
        "_399": ["StraightBevelDiffGearRating"],
        "_400": ["StraightBevelDiffGearSetRating"],
        "_401": ["StraightBevelDiffMeshedGearRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelDiffGearMeshRating",
    "StraightBevelDiffGearRating",
    "StraightBevelDiffGearSetRating",
    "StraightBevelDiffMeshedGearRating",
)

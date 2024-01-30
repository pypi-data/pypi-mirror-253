"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._554 import BevelGearMeshRating
    from ._555 import BevelGearRating
    from ._556 import BevelGearSetRating
else:
    import_structure = {
        "_554": ["BevelGearMeshRating"],
        "_555": ["BevelGearRating"],
        "_556": ["BevelGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelGearMeshRating",
    "BevelGearRating",
    "BevelGearSetRating",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._438 import HypoidGearMeshRating
    from ._439 import HypoidGearRating
    from ._440 import HypoidGearSetRating
    from ._441 import HypoidRatingMethod
else:
    import_structure = {
        "_438": ["HypoidGearMeshRating"],
        "_439": ["HypoidGearRating"],
        "_440": ["HypoidGearSetRating"],
        "_441": ["HypoidRatingMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "HypoidGearMeshRating",
    "HypoidGearRating",
    "HypoidGearSetRating",
    "HypoidRatingMethod",
)

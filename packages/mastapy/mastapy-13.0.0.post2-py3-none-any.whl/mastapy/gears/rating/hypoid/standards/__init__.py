"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._442 import GleasonHypoidGearSingleFlankRating
    from ._443 import GleasonHypoidMeshSingleFlankRating
    from ._444 import HypoidRateableMesh
else:
    import_structure = {
        "_442": ["GleasonHypoidGearSingleFlankRating"],
        "_443": ["GleasonHypoidMeshSingleFlankRating"],
        "_444": ["HypoidRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GleasonHypoidGearSingleFlankRating",
    "GleasonHypoidMeshSingleFlankRating",
    "HypoidRateableMesh",
)

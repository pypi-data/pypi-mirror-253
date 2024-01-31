"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._372 import WormGearDutyCycleRating
    from ._373 import WormGearMeshRating
    from ._374 import WormGearRating
    from ._375 import WormGearSetDutyCycleRating
    from ._376 import WormGearSetRating
    from ._377 import WormMeshDutyCycleRating
else:
    import_structure = {
        "_372": ["WormGearDutyCycleRating"],
        "_373": ["WormGearMeshRating"],
        "_374": ["WormGearRating"],
        "_375": ["WormGearSetDutyCycleRating"],
        "_376": ["WormGearSetRating"],
        "_377": ["WormMeshDutyCycleRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormGearDutyCycleRating",
    "WormGearMeshRating",
    "WormGearRating",
    "WormGearSetDutyCycleRating",
    "WormGearSetRating",
    "WormMeshDutyCycleRating",
)

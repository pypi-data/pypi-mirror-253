"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._445 import FaceGearDutyCycleRating
    from ._446 import FaceGearMeshDutyCycleRating
    from ._447 import FaceGearMeshRating
    from ._448 import FaceGearRating
    from ._449 import FaceGearSetDutyCycleRating
    from ._450 import FaceGearSetRating
else:
    import_structure = {
        "_445": ["FaceGearDutyCycleRating"],
        "_446": ["FaceGearMeshDutyCycleRating"],
        "_447": ["FaceGearMeshRating"],
        "_448": ["FaceGearRating"],
        "_449": ["FaceGearSetDutyCycleRating"],
        "_450": ["FaceGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearDutyCycleRating",
    "FaceGearMeshDutyCycleRating",
    "FaceGearMeshRating",
    "FaceGearRating",
    "FaceGearSetDutyCycleRating",
    "FaceGearSetRating",
)

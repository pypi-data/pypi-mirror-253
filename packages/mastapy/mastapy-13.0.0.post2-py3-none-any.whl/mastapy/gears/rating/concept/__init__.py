"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._548 import ConceptGearDutyCycleRating
    from ._549 import ConceptGearMeshDutyCycleRating
    from ._550 import ConceptGearMeshRating
    from ._551 import ConceptGearRating
    from ._552 import ConceptGearSetDutyCycleRating
    from ._553 import ConceptGearSetRating
else:
    import_structure = {
        "_548": ["ConceptGearDutyCycleRating"],
        "_549": ["ConceptGearMeshDutyCycleRating"],
        "_550": ["ConceptGearMeshRating"],
        "_551": ["ConceptGearRating"],
        "_552": ["ConceptGearSetDutyCycleRating"],
        "_553": ["ConceptGearSetRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearDutyCycleRating",
    "ConceptGearMeshDutyCycleRating",
    "ConceptGearMeshRating",
    "ConceptGearRating",
    "ConceptGearSetDutyCycleRating",
    "ConceptGearSetRating",
)

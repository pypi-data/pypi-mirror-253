"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._538 import ConicalGearDutyCycleRating
    from ._539 import ConicalGearMeshRating
    from ._540 import ConicalGearRating
    from ._541 import ConicalGearSetDutyCycleRating
    from ._542 import ConicalGearSetRating
    from ._543 import ConicalGearSingleFlankRating
    from ._544 import ConicalMeshDutyCycleRating
    from ._545 import ConicalMeshedGearRating
    from ._546 import ConicalMeshSingleFlankRating
    from ._547 import ConicalRateableMesh
else:
    import_structure = {
        "_538": ["ConicalGearDutyCycleRating"],
        "_539": ["ConicalGearMeshRating"],
        "_540": ["ConicalGearRating"],
        "_541": ["ConicalGearSetDutyCycleRating"],
        "_542": ["ConicalGearSetRating"],
        "_543": ["ConicalGearSingleFlankRating"],
        "_544": ["ConicalMeshDutyCycleRating"],
        "_545": ["ConicalMeshedGearRating"],
        "_546": ["ConicalMeshSingleFlankRating"],
        "_547": ["ConicalRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearDutyCycleRating",
    "ConicalGearMeshRating",
    "ConicalGearRating",
    "ConicalGearSetDutyCycleRating",
    "ConicalGearSetRating",
    "ConicalGearSingleFlankRating",
    "ConicalMeshDutyCycleRating",
    "ConicalMeshedGearRating",
    "ConicalMeshSingleFlankRating",
    "ConicalRateableMesh",
)

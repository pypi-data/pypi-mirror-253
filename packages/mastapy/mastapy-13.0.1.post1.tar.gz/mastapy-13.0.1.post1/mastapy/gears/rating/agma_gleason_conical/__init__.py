"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._565 import AGMAGleasonConicalGearMeshRating
    from ._566 import AGMAGleasonConicalGearRating
    from ._567 import AGMAGleasonConicalGearSetRating
    from ._568 import AGMAGleasonConicalRateableMesh
else:
    import_structure = {
        "_565": ["AGMAGleasonConicalGearMeshRating"],
        "_566": ["AGMAGleasonConicalGearRating"],
        "_567": ["AGMAGleasonConicalGearSetRating"],
        "_568": ["AGMAGleasonConicalRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMeshRating",
    "AGMAGleasonConicalGearRating",
    "AGMAGleasonConicalGearSetRating",
    "AGMAGleasonConicalRateableMesh",
)

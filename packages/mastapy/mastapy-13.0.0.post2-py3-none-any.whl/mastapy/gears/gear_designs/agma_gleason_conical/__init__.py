"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1192 import AGMAGleasonConicalAccuracyGrades
    from ._1193 import AGMAGleasonConicalGearDesign
    from ._1194 import AGMAGleasonConicalGearMeshDesign
    from ._1195 import AGMAGleasonConicalGearSetDesign
    from ._1196 import AGMAGleasonConicalMeshedGearDesign
else:
    import_structure = {
        "_1192": ["AGMAGleasonConicalAccuracyGrades"],
        "_1193": ["AGMAGleasonConicalGearDesign"],
        "_1194": ["AGMAGleasonConicalGearMeshDesign"],
        "_1195": ["AGMAGleasonConicalGearSetDesign"],
        "_1196": ["AGMAGleasonConicalMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalAccuracyGrades",
    "AGMAGleasonConicalGearDesign",
    "AGMAGleasonConicalGearMeshDesign",
    "AGMAGleasonConicalGearSetDesign",
    "AGMAGleasonConicalMeshedGearDesign",
)

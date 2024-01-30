"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1172 import ConicalGearBiasModification
    from ._1173 import ConicalGearFlankMicroGeometry
    from ._1174 import ConicalGearLeadModification
    from ._1175 import ConicalGearProfileModification
else:
    import_structure = {
        "_1172": ["ConicalGearBiasModification"],
        "_1173": ["ConicalGearFlankMicroGeometry"],
        "_1174": ["ConicalGearLeadModification"],
        "_1175": ["ConicalGearProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBiasModification",
    "ConicalGearFlankMicroGeometry",
    "ConicalGearLeadModification",
    "ConicalGearProfileModification",
)

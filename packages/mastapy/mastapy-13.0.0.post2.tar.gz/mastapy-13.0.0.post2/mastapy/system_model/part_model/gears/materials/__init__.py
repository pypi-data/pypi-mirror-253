"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2566 import GearMaterialExpertSystemMaterialDetails
    from ._2567 import GearMaterialExpertSystemMaterialOptions
else:
    import_structure = {
        "_2566": ["GearMaterialExpertSystemMaterialDetails"],
        "_2567": ["GearMaterialExpertSystemMaterialOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMaterialExpertSystemMaterialDetails",
    "GearMaterialExpertSystemMaterialOptions",
)

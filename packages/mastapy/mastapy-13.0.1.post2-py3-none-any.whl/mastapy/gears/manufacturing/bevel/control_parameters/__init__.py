"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._817 import ConicalGearManufacturingControlParameters
    from ._818 import ConicalManufacturingSGMControlParameters
    from ._819 import ConicalManufacturingSGTControlParameters
    from ._820 import ConicalManufacturingSMTControlParameters
else:
    import_structure = {
        "_817": ["ConicalGearManufacturingControlParameters"],
        "_818": ["ConicalManufacturingSGMControlParameters"],
        "_819": ["ConicalManufacturingSGTControlParameters"],
        "_820": ["ConicalManufacturingSMTControlParameters"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearManufacturingControlParameters",
    "ConicalManufacturingSGMControlParameters",
    "ConicalManufacturingSGTControlParameters",
    "ConicalManufacturingSMTControlParameters",
)

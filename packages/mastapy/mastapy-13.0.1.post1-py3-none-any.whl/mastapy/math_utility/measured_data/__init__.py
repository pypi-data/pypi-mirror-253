"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1565 import GriddedSurfaceAccessor
    from ._1566 import LookupTableBase
    from ._1567 import OnedimensionalFunctionLookupTable
    from ._1568 import TwodimensionalFunctionLookupTable
else:
    import_structure = {
        "_1565": ["GriddedSurfaceAccessor"],
        "_1566": ["LookupTableBase"],
        "_1567": ["OnedimensionalFunctionLookupTable"],
        "_1568": ["TwodimensionalFunctionLookupTable"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GriddedSurfaceAccessor",
    "LookupTableBase",
    "OnedimensionalFunctionLookupTable",
    "TwodimensionalFunctionLookupTable",
)

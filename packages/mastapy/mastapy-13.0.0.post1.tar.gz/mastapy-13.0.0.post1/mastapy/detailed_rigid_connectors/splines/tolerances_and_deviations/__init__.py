"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1420 import FitAndTolerance
    from ._1421 import SAESplineTolerances
else:
    import_structure = {
        "_1420": ["FitAndTolerance"],
        "_1421": ["SAESplineTolerances"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FitAndTolerance",
    "SAESplineTolerances",
)

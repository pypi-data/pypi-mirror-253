"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2486 import ConcentricOrParallelPartGroup
    from ._2487 import ConcentricPartGroup
    from ._2488 import ConcentricPartGroupParallelToThis
    from ._2489 import DesignMeasurements
    from ._2490 import ParallelPartGroup
    from ._2491 import ParallelPartGroupSelection
    from ._2492 import PartGroup
else:
    import_structure = {
        "_2486": ["ConcentricOrParallelPartGroup"],
        "_2487": ["ConcentricPartGroup"],
        "_2488": ["ConcentricPartGroupParallelToThis"],
        "_2489": ["DesignMeasurements"],
        "_2490": ["ParallelPartGroup"],
        "_2491": ["ParallelPartGroupSelection"],
        "_2492": ["PartGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConcentricOrParallelPartGroup",
    "ConcentricPartGroup",
    "ConcentricPartGroupParallelToThis",
    "DesignMeasurements",
    "ParallelPartGroup",
    "ParallelPartGroupSelection",
    "PartGroup",
)

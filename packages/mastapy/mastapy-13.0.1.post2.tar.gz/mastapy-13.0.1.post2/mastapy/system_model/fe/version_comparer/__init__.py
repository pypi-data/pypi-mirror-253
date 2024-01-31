"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2412 import DesignResults
    from ._2413 import FESubstructureResults
    from ._2414 import FESubstructureVersionComparer
    from ._2415 import LoadCaseResults
    from ._2416 import LoadCasesToRun
    from ._2417 import NodeComparisonResult
else:
    import_structure = {
        "_2412": ["DesignResults"],
        "_2413": ["FESubstructureResults"],
        "_2414": ["FESubstructureVersionComparer"],
        "_2415": ["LoadCaseResults"],
        "_2416": ["LoadCasesToRun"],
        "_2417": ["NodeComparisonResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignResults",
    "FESubstructureResults",
    "FESubstructureVersionComparer",
    "LoadCaseResults",
    "LoadCasesToRun",
    "NodeComparisonResult",
)

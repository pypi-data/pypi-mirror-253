"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1442 import AssemblyMethods
    from ._1443 import CalculationMethods
    from ._1444 import InterferenceFitDesign
    from ._1445 import InterferenceFitHalfDesign
    from ._1446 import StressRegions
    from ._1447 import Table4JointInterfaceTypes
else:
    import_structure = {
        "_1442": ["AssemblyMethods"],
        "_1443": ["CalculationMethods"],
        "_1444": ["InterferenceFitDesign"],
        "_1445": ["InterferenceFitHalfDesign"],
        "_1446": ["StressRegions"],
        "_1447": ["Table4JointInterfaceTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AssemblyMethods",
    "CalculationMethods",
    "InterferenceFitDesign",
    "InterferenceFitHalfDesign",
    "StressRegions",
    "Table4JointInterfaceTypes",
)

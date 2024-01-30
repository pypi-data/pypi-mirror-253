"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1559 import AbstractForceAndDisplacementResults
    from ._1560 import ForceAndDisplacementResults
    from ._1561 import ForceResults
    from ._1562 import NodeResults
    from ._1563 import OverridableDisplacementBoundaryCondition
    from ._1564 import VectorWithLinearAndAngularComponents
else:
    import_structure = {
        "_1559": ["AbstractForceAndDisplacementResults"],
        "_1560": ["ForceAndDisplacementResults"],
        "_1561": ["ForceResults"],
        "_1562": ["NodeResults"],
        "_1563": ["OverridableDisplacementBoundaryCondition"],
        "_1564": ["VectorWithLinearAndAngularComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractForceAndDisplacementResults",
    "ForceAndDisplacementResults",
    "ForceResults",
    "NodeResults",
    "OverridableDisplacementBoundaryCondition",
    "VectorWithLinearAndAngularComponents",
)

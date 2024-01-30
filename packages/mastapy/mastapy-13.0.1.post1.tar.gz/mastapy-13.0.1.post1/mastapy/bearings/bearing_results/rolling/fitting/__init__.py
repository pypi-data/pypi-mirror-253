"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2110 import InnerRingFittingThermalResults
    from ._2111 import InterferenceComponents
    from ._2112 import OuterRingFittingThermalResults
    from ._2113 import RingFittingThermalResults
else:
    import_structure = {
        "_2110": ["InnerRingFittingThermalResults"],
        "_2111": ["InterferenceComponents"],
        "_2112": ["OuterRingFittingThermalResults"],
        "_2113": ["RingFittingThermalResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "InnerRingFittingThermalResults",
    "InterferenceComponents",
    "OuterRingFittingThermalResults",
    "RingFittingThermalResults",
)

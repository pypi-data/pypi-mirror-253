"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2237 import DesignStateTargetRatio
    from ._2238 import PlanetGearOptions
    from ._2239 import SystemOptimiser
    from ._2240 import SystemOptimiserDetails
    from ._2241 import ToothNumberFinder
else:
    import_structure = {
        "_2237": ["DesignStateTargetRatio"],
        "_2238": ["PlanetGearOptions"],
        "_2239": ["SystemOptimiser"],
        "_2240": ["SystemOptimiserDetails"],
        "_2241": ["ToothNumberFinder"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DesignStateTargetRatio",
    "PlanetGearOptions",
    "SystemOptimiser",
    "SystemOptimiserDetails",
    "ToothNumberFinder",
)

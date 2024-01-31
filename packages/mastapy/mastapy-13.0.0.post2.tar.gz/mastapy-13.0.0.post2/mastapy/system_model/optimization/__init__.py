"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2226 import ConicalGearOptimisationStrategy
    from ._2227 import ConicalGearOptimizationStep
    from ._2228 import ConicalGearOptimizationStrategyDatabase
    from ._2229 import CylindricalGearOptimisationStrategy
    from ._2230 import CylindricalGearOptimizationStep
    from ._2231 import MeasuredAndFactorViewModel
    from ._2232 import MicroGeometryOptimisationTarget
    from ._2233 import OptimizationStep
    from ._2234 import OptimizationStrategy
    from ._2235 import OptimizationStrategyBase
    from ._2236 import OptimizationStrategyDatabase
else:
    import_structure = {
        "_2226": ["ConicalGearOptimisationStrategy"],
        "_2227": ["ConicalGearOptimizationStep"],
        "_2228": ["ConicalGearOptimizationStrategyDatabase"],
        "_2229": ["CylindricalGearOptimisationStrategy"],
        "_2230": ["CylindricalGearOptimizationStep"],
        "_2231": ["MeasuredAndFactorViewModel"],
        "_2232": ["MicroGeometryOptimisationTarget"],
        "_2233": ["OptimizationStep"],
        "_2234": ["OptimizationStrategy"],
        "_2235": ["OptimizationStrategyBase"],
        "_2236": ["OptimizationStrategyDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearOptimisationStrategy",
    "ConicalGearOptimizationStep",
    "ConicalGearOptimizationStrategyDatabase",
    "CylindricalGearOptimisationStrategy",
    "CylindricalGearOptimizationStep",
    "MeasuredAndFactorViewModel",
    "MicroGeometryOptimisationTarget",
    "OptimizationStep",
    "OptimizationStrategy",
    "OptimizationStrategyBase",
    "OptimizationStrategyDatabase",
)

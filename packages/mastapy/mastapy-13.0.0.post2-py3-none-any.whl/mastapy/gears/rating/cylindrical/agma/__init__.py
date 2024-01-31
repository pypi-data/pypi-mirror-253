"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._534 import AGMA2101GearSingleFlankRating
    from ._535 import AGMA2101MeshSingleFlankRating
    from ._536 import AGMA2101RateableMesh
    from ._537 import ThermalReductionFactorFactorsAndExponents
else:
    import_structure = {
        "_534": ["AGMA2101GearSingleFlankRating"],
        "_535": ["AGMA2101MeshSingleFlankRating"],
        "_536": ["AGMA2101RateableMesh"],
        "_537": ["ThermalReductionFactorFactorsAndExponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2101GearSingleFlankRating",
    "AGMA2101MeshSingleFlankRating",
    "AGMA2101RateableMesh",
    "ThermalReductionFactorFactorsAndExponents",
)

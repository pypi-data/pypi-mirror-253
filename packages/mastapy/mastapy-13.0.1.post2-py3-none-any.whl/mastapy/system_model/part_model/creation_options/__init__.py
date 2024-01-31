"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2571 import BeltCreationOptions
    from ._2572 import CycloidalAssemblyCreationOptions
    from ._2573 import CylindricalGearLinearTrainCreationOptions
    from ._2574 import PlanetCarrierCreationOptions
    from ._2575 import ShaftCreationOptions
else:
    import_structure = {
        "_2571": ["BeltCreationOptions"],
        "_2572": ["CycloidalAssemblyCreationOptions"],
        "_2573": ["CylindricalGearLinearTrainCreationOptions"],
        "_2574": ["PlanetCarrierCreationOptions"],
        "_2575": ["ShaftCreationOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltCreationOptions",
    "CycloidalAssemblyCreationOptions",
    "CylindricalGearLinearTrainCreationOptions",
    "PlanetCarrierCreationOptions",
    "ShaftCreationOptions",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._642 import CalculationError
    from ._643 import ChartType
    from ._644 import GearPointCalculationError
    from ._645 import MicroGeometryDefinitionMethod
    from ._646 import MicroGeometryDefinitionType
    from ._647 import PlungeShaverCalculation
    from ._648 import PlungeShaverCalculationInputs
    from ._649 import PlungeShaverGeneration
    from ._650 import PlungeShaverInputsAndMicroGeometry
    from ._651 import PlungeShaverOutputs
    from ._652 import PlungeShaverSettings
    from ._653 import PointOfInterest
    from ._654 import RealPlungeShaverOutputs
    from ._655 import ShaverPointCalculationError
    from ._656 import ShaverPointOfInterest
    from ._657 import VirtualPlungeShaverOutputs
else:
    import_structure = {
        "_642": ["CalculationError"],
        "_643": ["ChartType"],
        "_644": ["GearPointCalculationError"],
        "_645": ["MicroGeometryDefinitionMethod"],
        "_646": ["MicroGeometryDefinitionType"],
        "_647": ["PlungeShaverCalculation"],
        "_648": ["PlungeShaverCalculationInputs"],
        "_649": ["PlungeShaverGeneration"],
        "_650": ["PlungeShaverInputsAndMicroGeometry"],
        "_651": ["PlungeShaverOutputs"],
        "_652": ["PlungeShaverSettings"],
        "_653": ["PointOfInterest"],
        "_654": ["RealPlungeShaverOutputs"],
        "_655": ["ShaverPointCalculationError"],
        "_656": ["ShaverPointOfInterest"],
        "_657": ["VirtualPlungeShaverOutputs"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculationError",
    "ChartType",
    "GearPointCalculationError",
    "MicroGeometryDefinitionMethod",
    "MicroGeometryDefinitionType",
    "PlungeShaverCalculation",
    "PlungeShaverCalculationInputs",
    "PlungeShaverGeneration",
    "PlungeShaverInputsAndMicroGeometry",
    "PlungeShaverOutputs",
    "PlungeShaverSettings",
    "PointOfInterest",
    "RealPlungeShaverOutputs",
    "ShaverPointCalculationError",
    "ShaverPointOfInterest",
    "VirtualPlungeShaverOutputs",
)

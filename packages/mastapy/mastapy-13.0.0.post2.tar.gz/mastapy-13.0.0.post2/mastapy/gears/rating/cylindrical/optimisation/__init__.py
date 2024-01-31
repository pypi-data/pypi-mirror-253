"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._501 import CylindricalGearSetRatingOptimisationHelper
    from ._502 import OptimisationResultsPair
    from ._503 import SafetyFactorOptimisationResults
    from ._504 import SafetyFactorOptimisationStepResult
    from ._505 import SafetyFactorOptimisationStepResultAngle
    from ._506 import SafetyFactorOptimisationStepResultNumber
    from ._507 import SafetyFactorOptimisationStepResultShortLength
else:
    import_structure = {
        "_501": ["CylindricalGearSetRatingOptimisationHelper"],
        "_502": ["OptimisationResultsPair"],
        "_503": ["SafetyFactorOptimisationResults"],
        "_504": ["SafetyFactorOptimisationStepResult"],
        "_505": ["SafetyFactorOptimisationStepResultAngle"],
        "_506": ["SafetyFactorOptimisationStepResultNumber"],
        "_507": ["SafetyFactorOptimisationStepResultShortLength"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearSetRatingOptimisationHelper",
    "OptimisationResultsPair",
    "SafetyFactorOptimisationResults",
    "SafetyFactorOptimisationStepResult",
    "SafetyFactorOptimisationStepResultAngle",
    "SafetyFactorOptimisationStepResultNumber",
    "SafetyFactorOptimisationStepResultShortLength",
)

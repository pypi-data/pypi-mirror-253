"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._93 import AbstractVaryingInputComponent
    from ._94 import AngleInputComponent
    from ._95 import ForceInputComponent
    from ._96 import MomentInputComponent
    from ._97 import NonDimensionalInputComponent
    from ._98 import SinglePointSelectionMethod
    from ._99 import VelocityInputComponent
else:
    import_structure = {
        "_93": ["AbstractVaryingInputComponent"],
        "_94": ["AngleInputComponent"],
        "_95": ["ForceInputComponent"],
        "_96": ["MomentInputComponent"],
        "_97": ["NonDimensionalInputComponent"],
        "_98": ["SinglePointSelectionMethod"],
        "_99": ["VelocityInputComponent"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractVaryingInputComponent",
    "AngleInputComponent",
    "ForceInputComponent",
    "MomentInputComponent",
    "NonDimensionalInputComponent",
    "SinglePointSelectionMethod",
    "VelocityInputComponent",
)

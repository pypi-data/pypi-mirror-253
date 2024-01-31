"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1432 import AGMA6123SplineJointDutyCycleRating
    from ._1433 import GBT17855SplineJointDutyCycleRating
    from ._1434 import SAESplineJointDutyCycleRating
else:
    import_structure = {
        "_1432": ["AGMA6123SplineJointDutyCycleRating"],
        "_1433": ["GBT17855SplineJointDutyCycleRating"],
        "_1434": ["SAESplineJointDutyCycleRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineJointDutyCycleRating",
    "GBT17855SplineJointDutyCycleRating",
    "SAESplineJointDutyCycleRating",
)

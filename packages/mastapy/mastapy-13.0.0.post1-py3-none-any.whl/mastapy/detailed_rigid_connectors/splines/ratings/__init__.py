"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1422 import AGMA6123SplineHalfRating
    from ._1423 import AGMA6123SplineJointRating
    from ._1424 import DIN5466SplineHalfRating
    from ._1425 import DIN5466SplineRating
    from ._1426 import GBT17855SplineHalfRating
    from ._1427 import GBT17855SplineJointRating
    from ._1428 import SAESplineHalfRating
    from ._1429 import SAESplineJointRating
    from ._1430 import SplineHalfRating
    from ._1431 import SplineJointRating
else:
    import_structure = {
        "_1422": ["AGMA6123SplineHalfRating"],
        "_1423": ["AGMA6123SplineJointRating"],
        "_1424": ["DIN5466SplineHalfRating"],
        "_1425": ["DIN5466SplineRating"],
        "_1426": ["GBT17855SplineHalfRating"],
        "_1427": ["GBT17855SplineJointRating"],
        "_1428": ["SAESplineHalfRating"],
        "_1429": ["SAESplineJointRating"],
        "_1430": ["SplineHalfRating"],
        "_1431": ["SplineJointRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA6123SplineHalfRating",
    "AGMA6123SplineJointRating",
    "DIN5466SplineHalfRating",
    "DIN5466SplineRating",
    "GBT17855SplineHalfRating",
    "GBT17855SplineJointRating",
    "SAESplineHalfRating",
    "SAESplineJointRating",
    "SplineHalfRating",
    "SplineJointRating",
)

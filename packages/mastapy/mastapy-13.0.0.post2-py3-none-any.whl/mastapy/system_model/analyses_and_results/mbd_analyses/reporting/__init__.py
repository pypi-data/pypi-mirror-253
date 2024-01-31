"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5522 import AbstractMeasuredDynamicResponseAtTime
    from ._5523 import DynamicForceResultAtTime
    from ._5524 import DynamicForceVector3DResult
    from ._5525 import DynamicTorqueResultAtTime
    from ._5526 import DynamicTorqueVector3DResult
else:
    import_structure = {
        "_5522": ["AbstractMeasuredDynamicResponseAtTime"],
        "_5523": ["DynamicForceResultAtTime"],
        "_5524": ["DynamicForceVector3DResult"],
        "_5525": ["DynamicTorqueResultAtTime"],
        "_5526": ["DynamicTorqueVector3DResult"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractMeasuredDynamicResponseAtTime",
    "DynamicForceResultAtTime",
    "DynamicForceVector3DResult",
    "DynamicTorqueResultAtTime",
    "DynamicTorqueVector3DResult",
)

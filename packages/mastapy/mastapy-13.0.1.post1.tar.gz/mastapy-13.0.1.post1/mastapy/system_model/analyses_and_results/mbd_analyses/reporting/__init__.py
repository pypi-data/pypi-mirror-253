"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5523 import AbstractMeasuredDynamicResponseAtTime
    from ._5524 import DynamicForceResultAtTime
    from ._5525 import DynamicForceVector3DResult
    from ._5526 import DynamicTorqueResultAtTime
    from ._5527 import DynamicTorqueVector3DResult
else:
    import_structure = {
        "_5523": ["AbstractMeasuredDynamicResponseAtTime"],
        "_5524": ["DynamicForceResultAtTime"],
        "_5525": ["DynamicForceVector3DResult"],
        "_5526": ["DynamicTorqueResultAtTime"],
        "_5527": ["DynamicTorqueVector3DResult"],
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

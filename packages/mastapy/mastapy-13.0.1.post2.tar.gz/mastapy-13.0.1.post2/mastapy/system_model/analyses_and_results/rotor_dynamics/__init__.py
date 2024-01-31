"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4026 import RotorDynamicsDrawStyle
    from ._4027 import ShaftComplexShape
    from ._4028 import ShaftForcedComplexShape
    from ._4029 import ShaftModalComplexShape
    from ._4030 import ShaftModalComplexShapeAtSpeeds
    from ._4031 import ShaftModalComplexShapeAtStiffness
else:
    import_structure = {
        "_4026": ["RotorDynamicsDrawStyle"],
        "_4027": ["ShaftComplexShape"],
        "_4028": ["ShaftForcedComplexShape"],
        "_4029": ["ShaftModalComplexShape"],
        "_4030": ["ShaftModalComplexShapeAtSpeeds"],
        "_4031": ["ShaftModalComplexShapeAtStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "RotorDynamicsDrawStyle",
    "ShaftComplexShape",
    "ShaftForcedComplexShape",
    "ShaftModalComplexShape",
    "ShaftModalComplexShapeAtSpeeds",
    "ShaftModalComplexShapeAtStiffness",
)

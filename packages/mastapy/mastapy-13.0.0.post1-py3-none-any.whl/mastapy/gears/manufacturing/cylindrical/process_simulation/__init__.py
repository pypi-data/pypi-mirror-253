"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._639 import CutterProcessSimulation
    from ._640 import FormWheelGrindingProcessSimulation
    from ._641 import ShapingProcessSimulation
else:
    import_structure = {
        "_639": ["CutterProcessSimulation"],
        "_640": ["FormWheelGrindingProcessSimulation"],
        "_641": ["ShapingProcessSimulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterProcessSimulation",
    "FormWheelGrindingProcessSimulation",
    "ShapingProcessSimulation",
)

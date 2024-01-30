"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._813 import PinionFinishCutter
    from ._814 import PinionRoughCutter
    from ._815 import WheelFinishCutter
    from ._816 import WheelRoughCutter
else:
    import_structure = {
        "_813": ["PinionFinishCutter"],
        "_814": ["PinionRoughCutter"],
        "_815": ["WheelFinishCutter"],
        "_816": ["WheelRoughCutter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "PinionFinishCutter",
    "PinionRoughCutter",
    "WheelFinishCutter",
    "WheelRoughCutter",
)

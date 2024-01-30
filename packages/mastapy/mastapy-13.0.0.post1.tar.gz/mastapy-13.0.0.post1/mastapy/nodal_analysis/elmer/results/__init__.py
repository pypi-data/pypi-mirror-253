"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._175 import Data
    from ._176 import Data1D
    from ._177 import Data3D
else:
    import_structure = {
        "_175": ["Data"],
        "_176": ["Data1D"],
        "_177": ["Data3D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Data",
    "Data1D",
    "Data3D",
)

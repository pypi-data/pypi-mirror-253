"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1241 import ElementPropertyClass
    from ._1242 import MaterialPropertyClass
else:
    import_structure = {
        "_1241": ["ElementPropertyClass"],
        "_1242": ["MaterialPropertyClass"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElementPropertyClass",
    "MaterialPropertyClass",
)

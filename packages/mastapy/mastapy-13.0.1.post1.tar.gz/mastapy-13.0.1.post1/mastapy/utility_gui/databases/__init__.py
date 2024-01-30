"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1868 import DatabaseWithSelectedItem
else:
    import_structure = {
        "_1868": ["DatabaseWithSelectedItem"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = ("DatabaseWithSelectedItem",)

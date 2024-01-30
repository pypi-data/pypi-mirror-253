"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1817 import ColumnTitle
    from ._1818 import TextFileDelimiterOptions
else:
    import_structure = {
        "_1817": ["ColumnTitle"],
        "_1818": ["TextFileDelimiterOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ColumnTitle",
    "TextFileDelimiterOptions",
)

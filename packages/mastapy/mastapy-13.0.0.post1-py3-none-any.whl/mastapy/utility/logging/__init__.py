"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1808 import Logger
    from ._1809 import Message
else:
    import_structure = {
        "_1808": ["Logger"],
        "_1809": ["Message"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Logger",
    "Message",
)

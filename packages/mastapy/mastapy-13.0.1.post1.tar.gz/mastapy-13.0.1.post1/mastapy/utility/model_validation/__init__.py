"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1791 import Fix
    from ._1792 import Severity
    from ._1793 import Status
    from ._1794 import StatusItem
    from ._1795 import StatusItemSeverity
else:
    import_structure = {
        "_1791": ["Fix"],
        "_1792": ["Severity"],
        "_1793": ["Status"],
        "_1794": ["StatusItem"],
        "_1795": ["StatusItemSeverity"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Fix",
    "Severity",
    "Status",
    "StatusItem",
    "StatusItemSeverity",
)

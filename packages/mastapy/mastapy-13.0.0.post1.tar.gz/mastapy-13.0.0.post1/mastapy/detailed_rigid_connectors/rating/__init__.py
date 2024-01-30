"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1435 import ShaftHubConnectionRating
else:
    import_structure = {
        "_1435": ["ShaftHubConnectionRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = ("ShaftHubConnectionRating",)

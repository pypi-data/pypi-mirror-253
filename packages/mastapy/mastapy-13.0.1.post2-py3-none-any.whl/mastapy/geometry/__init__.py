"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._306 import ClippingPlane
    from ._307 import DrawStyle
    from ._308 import DrawStyleBase
    from ._309 import PackagingLimits
else:
    import_structure = {
        "_306": ["ClippingPlane"],
        "_307": ["DrawStyle"],
        "_308": ["DrawStyleBase"],
        "_309": ["PackagingLimits"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClippingPlane",
    "DrawStyle",
    "DrawStyleBase",
    "PackagingLimits",
)

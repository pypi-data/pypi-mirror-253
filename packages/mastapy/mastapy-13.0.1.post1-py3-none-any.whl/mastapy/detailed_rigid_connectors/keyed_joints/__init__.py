"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1436 import KeyedJointDesign
    from ._1437 import KeyTypes
    from ._1438 import KeywayJointHalfDesign
    from ._1439 import NumberOfKeys
else:
    import_structure = {
        "_1436": ["KeyedJointDesign"],
        "_1437": ["KeyTypes"],
        "_1438": ["KeywayJointHalfDesign"],
        "_1439": ["NumberOfKeys"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KeyedJointDesign",
    "KeyTypes",
    "KeywayJointHalfDesign",
    "NumberOfKeys",
)

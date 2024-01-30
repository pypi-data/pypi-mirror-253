"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1089 import FinishStockSpecification
    from ._1090 import FinishStockType
    from ._1091 import NominalValueSpecification
    from ._1092 import NoValueSpecification
else:
    import_structure = {
        "_1089": ["FinishStockSpecification"],
        "_1090": ["FinishStockType"],
        "_1091": ["NominalValueSpecification"],
        "_1092": ["NoValueSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FinishStockSpecification",
    "FinishStockType",
    "NominalValueSpecification",
    "NoValueSpecification",
)

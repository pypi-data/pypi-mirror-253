"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1569 import DataScalingOptions
    from ._1570 import DataScalingReferenceValues
    from ._1571 import DataScalingReferenceValuesBase
else:
    import_structure = {
        "_1569": ["DataScalingOptions"],
        "_1570": ["DataScalingReferenceValues"],
        "_1571": ["DataScalingReferenceValuesBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DataScalingOptions",
    "DataScalingReferenceValues",
    "DataScalingReferenceValuesBase",
)

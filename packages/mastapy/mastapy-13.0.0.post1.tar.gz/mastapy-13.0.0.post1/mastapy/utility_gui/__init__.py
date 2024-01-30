"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1847 import ColumnInputOptions
    from ._1848 import DataInputFileOptions
    from ._1849 import DataLoggerItem
    from ._1850 import DataLoggerWithCharts
    from ._1851 import ScalingDrawStyle
else:
    import_structure = {
        "_1847": ["ColumnInputOptions"],
        "_1848": ["DataInputFileOptions"],
        "_1849": ["DataLoggerItem"],
        "_1850": ["DataLoggerWithCharts"],
        "_1851": ["ScalingDrawStyle"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ColumnInputOptions",
    "DataInputFileOptions",
    "DataLoggerItem",
    "DataLoggerWithCharts",
    "ScalingDrawStyle",
)

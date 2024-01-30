"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6537 import ExcelBatchDutyCycleCreator
    from ._6538 import ExcelBatchDutyCycleSpectraCreatorDetails
    from ._6539 import ExcelFileDetails
    from ._6540 import ExcelSheet
    from ._6541 import ExcelSheetDesignStateSelector
    from ._6542 import MASTAFileDetails
else:
    import_structure = {
        "_6537": ["ExcelBatchDutyCycleCreator"],
        "_6538": ["ExcelBatchDutyCycleSpectraCreatorDetails"],
        "_6539": ["ExcelFileDetails"],
        "_6540": ["ExcelSheet"],
        "_6541": ["ExcelSheetDesignStateSelector"],
        "_6542": ["MASTAFileDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ExcelBatchDutyCycleCreator",
    "ExcelBatchDutyCycleSpectraCreatorDetails",
    "ExcelFileDetails",
    "ExcelSheet",
    "ExcelSheetDesignStateSelector",
    "MASTAFileDetails",
)

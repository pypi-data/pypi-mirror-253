"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6536 import ExcelBatchDutyCycleCreator
    from ._6537 import ExcelBatchDutyCycleSpectraCreatorDetails
    from ._6538 import ExcelFileDetails
    from ._6539 import ExcelSheet
    from ._6540 import ExcelSheetDesignStateSelector
    from ._6541 import MASTAFileDetails
else:
    import_structure = {
        "_6536": ["ExcelBatchDutyCycleCreator"],
        "_6537": ["ExcelBatchDutyCycleSpectraCreatorDetails"],
        "_6538": ["ExcelFileDetails"],
        "_6539": ["ExcelSheet"],
        "_6540": ["ExcelSheetDesignStateSelector"],
        "_6541": ["MASTAFileDetails"],
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

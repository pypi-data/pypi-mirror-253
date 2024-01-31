"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._165 import BoundaryConditionType
    from ._166 import FEExportFormat
    from ._167 import FESubstructuringFileFormat
else:
    import_structure = {
        "_165": ["BoundaryConditionType"],
        "_166": ["FEExportFormat"],
        "_167": ["FESubstructuringFileFormat"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoundaryConditionType",
    "FEExportFormat",
    "FESubstructuringFileFormat",
)

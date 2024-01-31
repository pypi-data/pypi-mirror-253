"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._310 import CADFace
    from ._311 import CADFaceGroup
    from ._312 import InternalExternalType
else:
    import_structure = {
        "_310": ["CADFace"],
        "_311": ["CADFaceGroup"],
        "_312": ["InternalExternalType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CADFace",
    "CADFaceGroup",
    "InternalExternalType",
)

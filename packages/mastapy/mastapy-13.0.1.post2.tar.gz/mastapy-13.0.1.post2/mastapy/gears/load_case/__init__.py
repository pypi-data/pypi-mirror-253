"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._873 import GearLoadCaseBase
    from ._874 import GearSetLoadCaseBase
    from ._875 import MeshLoadCase
else:
    import_structure = {
        "_873": ["GearLoadCaseBase"],
        "_874": ["GearSetLoadCaseBase"],
        "_875": ["MeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearLoadCaseBase",
    "GearSetLoadCaseBase",
    "MeshLoadCase",
)

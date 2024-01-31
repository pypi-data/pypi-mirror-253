"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._879 import FaceGearLoadCase
    from ._880 import FaceGearSetLoadCase
    from ._881 import FaceMeshLoadCase
else:
    import_structure = {
        "_879": ["FaceGearLoadCase"],
        "_880": ["FaceGearSetLoadCase"],
        "_881": ["FaceMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearLoadCase",
    "FaceGearSetLoadCase",
    "FaceMeshLoadCase",
)

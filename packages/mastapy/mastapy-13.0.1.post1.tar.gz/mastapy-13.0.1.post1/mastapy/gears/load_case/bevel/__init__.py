"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._891 import BevelLoadCase
    from ._892 import BevelMeshLoadCase
    from ._893 import BevelSetLoadCase
else:
    import_structure = {
        "_891": ["BevelLoadCase"],
        "_892": ["BevelMeshLoadCase"],
        "_893": ["BevelSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelLoadCase",
    "BevelMeshLoadCase",
    "BevelSetLoadCase",
)

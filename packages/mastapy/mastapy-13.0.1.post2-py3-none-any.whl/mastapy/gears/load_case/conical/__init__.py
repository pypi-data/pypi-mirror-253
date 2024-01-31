"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._885 import ConicalGearLoadCase
    from ._886 import ConicalGearSetLoadCase
    from ._887 import ConicalMeshLoadCase
else:
    import_structure = {
        "_885": ["ConicalGearLoadCase"],
        "_886": ["ConicalGearSetLoadCase"],
        "_887": ["ConicalMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearLoadCase",
    "ConicalGearSetLoadCase",
    "ConicalMeshLoadCase",
)

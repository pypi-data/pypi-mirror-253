"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._876 import WormGearLoadCase
    from ._877 import WormGearSetLoadCase
    from ._878 import WormMeshLoadCase
else:
    import_structure = {
        "_876": ["WormGearLoadCase"],
        "_877": ["WormGearSetLoadCase"],
        "_878": ["WormMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "WormGearLoadCase",
    "WormGearSetLoadCase",
    "WormMeshLoadCase",
)

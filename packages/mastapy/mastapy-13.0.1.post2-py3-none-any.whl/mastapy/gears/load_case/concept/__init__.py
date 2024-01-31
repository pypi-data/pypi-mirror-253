"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._888 import ConceptGearLoadCase
    from ._889 import ConceptGearSetLoadCase
    from ._890 import ConceptMeshLoadCase
else:
    import_structure = {
        "_888": ["ConceptGearLoadCase"],
        "_889": ["ConceptGearSetLoadCase"],
        "_890": ["ConceptMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConceptGearLoadCase",
    "ConceptGearSetLoadCase",
    "ConceptMeshLoadCase",
)

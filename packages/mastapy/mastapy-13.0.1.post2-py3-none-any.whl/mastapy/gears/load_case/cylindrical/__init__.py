"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._882 import CylindricalGearLoadCase
    from ._883 import CylindricalGearSetLoadCase
    from ._884 import CylindricalMeshLoadCase
else:
    import_structure = {
        "_882": ["CylindricalGearLoadCase"],
        "_883": ["CylindricalGearSetLoadCase"],
        "_884": ["CylindricalMeshLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLoadCase",
    "CylindricalGearSetLoadCase",
    "CylindricalMeshLoadCase",
)

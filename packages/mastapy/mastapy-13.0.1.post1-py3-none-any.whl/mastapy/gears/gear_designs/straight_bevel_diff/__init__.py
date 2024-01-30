"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._965 import StraightBevelDiffGearDesign
    from ._966 import StraightBevelDiffGearMeshDesign
    from ._967 import StraightBevelDiffGearSetDesign
    from ._968 import StraightBevelDiffMeshedGearDesign
else:
    import_structure = {
        "_965": ["StraightBevelDiffGearDesign"],
        "_966": ["StraightBevelDiffGearMeshDesign"],
        "_967": ["StraightBevelDiffGearSetDesign"],
        "_968": ["StraightBevelDiffMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "StraightBevelDiffGearDesign",
    "StraightBevelDiffGearMeshDesign",
    "StraightBevelDiffGearSetDesign",
    "StraightBevelDiffMeshedGearDesign",
)

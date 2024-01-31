"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._985 import HypoidGearDesign
    from ._986 import HypoidGearMeshDesign
    from ._987 import HypoidGearSetDesign
    from ._988 import HypoidMeshedGearDesign
else:
    import_structure = {
        "_985": ["HypoidGearDesign"],
        "_986": ["HypoidGearMeshDesign"],
        "_987": ["HypoidGearSetDesign"],
        "_988": ["HypoidMeshedGearDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "HypoidGearDesign",
    "HypoidGearMeshDesign",
    "HypoidGearSetDesign",
    "HypoidMeshedGearDesign",
)

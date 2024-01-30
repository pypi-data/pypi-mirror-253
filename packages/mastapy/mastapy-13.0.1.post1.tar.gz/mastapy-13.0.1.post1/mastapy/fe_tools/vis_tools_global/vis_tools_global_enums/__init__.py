"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1234 import BeamSectionType
    from ._1235 import ContactPairConstrainedSurfaceType
    from ._1236 import ContactPairReferenceSurfaceType
    from ._1237 import ElementPropertiesShellWallType
else:
    import_structure = {
        "_1234": ["BeamSectionType"],
        "_1235": ["ContactPairConstrainedSurfaceType"],
        "_1236": ["ContactPairReferenceSurfaceType"],
        "_1237": ["ElementPropertiesShellWallType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeamSectionType",
    "ContactPairConstrainedSurfaceType",
    "ContactPairReferenceSurfaceType",
    "ElementPropertiesShellWallType",
)

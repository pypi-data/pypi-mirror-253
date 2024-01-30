"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1487 import LicenceServer
    from ._7572 import LicenceServerDetails
    from ._7573 import ModuleDetails
    from ._7574 import ModuleLicenceStatus
else:
    import_structure = {
        "_1487": ["LicenceServer"],
        "_7572": ["LicenceServerDetails"],
        "_7573": ["ModuleDetails"],
        "_7574": ["ModuleLicenceStatus"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LicenceServer",
    "LicenceServerDetails",
    "ModuleDetails",
    "ModuleLicenceStatus",
)

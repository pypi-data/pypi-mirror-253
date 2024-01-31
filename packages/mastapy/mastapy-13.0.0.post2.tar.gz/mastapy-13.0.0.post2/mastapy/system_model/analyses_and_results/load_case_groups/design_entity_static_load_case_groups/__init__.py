"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5671 import AbstractAssemblyStaticLoadCaseGroup
    from ._5672 import ComponentStaticLoadCaseGroup
    from ._5673 import ConnectionStaticLoadCaseGroup
    from ._5674 import DesignEntityStaticLoadCaseGroup
    from ._5675 import GearSetStaticLoadCaseGroup
    from ._5676 import PartStaticLoadCaseGroup
else:
    import_structure = {
        "_5671": ["AbstractAssemblyStaticLoadCaseGroup"],
        "_5672": ["ComponentStaticLoadCaseGroup"],
        "_5673": ["ConnectionStaticLoadCaseGroup"],
        "_5674": ["DesignEntityStaticLoadCaseGroup"],
        "_5675": ["GearSetStaticLoadCaseGroup"],
        "_5676": ["PartStaticLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStaticLoadCaseGroup",
    "ComponentStaticLoadCaseGroup",
    "ConnectionStaticLoadCaseGroup",
    "DesignEntityStaticLoadCaseGroup",
    "GearSetStaticLoadCaseGroup",
    "PartStaticLoadCaseGroup",
)

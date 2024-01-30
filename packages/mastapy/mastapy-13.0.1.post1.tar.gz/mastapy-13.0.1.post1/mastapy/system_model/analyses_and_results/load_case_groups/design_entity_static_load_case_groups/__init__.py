"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5672 import AbstractAssemblyStaticLoadCaseGroup
    from ._5673 import ComponentStaticLoadCaseGroup
    from ._5674 import ConnectionStaticLoadCaseGroup
    from ._5675 import DesignEntityStaticLoadCaseGroup
    from ._5676 import GearSetStaticLoadCaseGroup
    from ._5677 import PartStaticLoadCaseGroup
else:
    import_structure = {
        "_5672": ["AbstractAssemblyStaticLoadCaseGroup"],
        "_5673": ["ComponentStaticLoadCaseGroup"],
        "_5674": ["ConnectionStaticLoadCaseGroup"],
        "_5675": ["DesignEntityStaticLoadCaseGroup"],
        "_5676": ["GearSetStaticLoadCaseGroup"],
        "_5677": ["PartStaticLoadCaseGroup"],
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

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._120 import ElementScalarState
    from ._121 import ElementVectorState
    from ._122 import EntityVectorState
    from ._123 import NodeScalarState
    from ._124 import NodeVectorState
else:
    import_structure = {
        "_120": ["ElementScalarState"],
        "_121": ["ElementVectorState"],
        "_122": ["EntityVectorState"],
        "_123": ["NodeScalarState"],
        "_124": ["NodeVectorState"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElementScalarState",
    "ElementVectorState",
    "EntityVectorState",
    "NodeScalarState",
    "NodeVectorState",
)

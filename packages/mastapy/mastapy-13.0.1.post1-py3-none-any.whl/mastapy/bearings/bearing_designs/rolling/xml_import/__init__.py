"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2176 import AbstractXmlVariableAssignment
    from ._2177 import BearingImportFile
    from ._2178 import RollingBearingImporter
    from ._2179 import XmlBearingTypeMapping
    from ._2180 import XMLVariableAssignment
else:
    import_structure = {
        "_2176": ["AbstractXmlVariableAssignment"],
        "_2177": ["BearingImportFile"],
        "_2178": ["RollingBearingImporter"],
        "_2179": ["XmlBearingTypeMapping"],
        "_2180": ["XMLVariableAssignment"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractXmlVariableAssignment",
    "BearingImportFile",
    "RollingBearingImporter",
    "XmlBearingTypeMapping",
    "XMLVariableAssignment",
)

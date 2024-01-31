"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1739 import ScriptingSetup
    from ._1740 import UserDefinedPropertyKey
    from ._1741 import UserSpecifiedData
else:
    import_structure = {
        "_1739": ["ScriptingSetup"],
        "_1740": ["UserDefinedPropertyKey"],
        "_1741": ["UserSpecifiedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ScriptingSetup",
    "UserDefinedPropertyKey",
    "UserSpecifiedData",
)

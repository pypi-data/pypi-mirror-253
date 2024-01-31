"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7562 import ApiEnumForAttribute
    from ._7563 import ApiVersion
    from ._7564 import SMTBitmap
    from ._7566 import MastaPropertyAttribute
    from ._7567 import PythonCommand
    from ._7568 import ScriptingCommand
    from ._7569 import ScriptingExecutionCommand
    from ._7570 import ScriptingObjectCommand
    from ._7571 import ApiVersioning
else:
    import_structure = {
        "_7562": ["ApiEnumForAttribute"],
        "_7563": ["ApiVersion"],
        "_7564": ["SMTBitmap"],
        "_7566": ["MastaPropertyAttribute"],
        "_7567": ["PythonCommand"],
        "_7568": ["ScriptingCommand"],
        "_7569": ["ScriptingExecutionCommand"],
        "_7570": ["ScriptingObjectCommand"],
        "_7571": ["ApiVersioning"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ApiEnumForAttribute",
    "ApiVersion",
    "SMTBitmap",
    "MastaPropertyAttribute",
    "PythonCommand",
    "ScriptingCommand",
    "ScriptingExecutionCommand",
    "ScriptingObjectCommand",
    "ApiVersioning",
)

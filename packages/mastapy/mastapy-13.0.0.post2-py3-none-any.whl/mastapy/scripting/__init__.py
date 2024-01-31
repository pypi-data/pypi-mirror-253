"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7561 import ApiEnumForAttribute
    from ._7562 import ApiVersion
    from ._7563 import SMTBitmap
    from ._7565 import MastaPropertyAttribute
    from ._7566 import PythonCommand
    from ._7567 import ScriptingCommand
    from ._7568 import ScriptingExecutionCommand
    from ._7569 import ScriptingObjectCommand
    from ._7570 import ApiVersioning
else:
    import_structure = {
        "_7561": ["ApiEnumForAttribute"],
        "_7562": ["ApiVersion"],
        "_7563": ["SMTBitmap"],
        "_7565": ["MastaPropertyAttribute"],
        "_7566": ["PythonCommand"],
        "_7567": ["ScriptingCommand"],
        "_7568": ["ScriptingExecutionCommand"],
        "_7569": ["ScriptingObjectCommand"],
        "_7570": ["ApiVersioning"],
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

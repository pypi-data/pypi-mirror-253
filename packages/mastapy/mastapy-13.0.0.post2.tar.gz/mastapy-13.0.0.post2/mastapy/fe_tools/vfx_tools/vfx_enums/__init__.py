"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1239 import ProSolveMpcType
    from ._1240 import ProSolveSolverType
else:
    import_structure = {
        "_1239": ["ProSolveMpcType"],
        "_1240": ["ProSolveSolverType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProSolveMpcType",
    "ProSolveSolverType",
)

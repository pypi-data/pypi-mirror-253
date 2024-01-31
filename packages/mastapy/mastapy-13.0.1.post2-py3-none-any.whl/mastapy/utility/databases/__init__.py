"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1824 import Database
    from ._1825 import DatabaseConnectionSettings
    from ._1826 import DatabaseKey
    from ._1827 import DatabaseSettings
    from ._1828 import NamedDatabase
    from ._1829 import NamedDatabaseItem
    from ._1830 import NamedKey
    from ._1831 import SQLDatabase
else:
    import_structure = {
        "_1824": ["Database"],
        "_1825": ["DatabaseConnectionSettings"],
        "_1826": ["DatabaseKey"],
        "_1827": ["DatabaseSettings"],
        "_1828": ["NamedDatabase"],
        "_1829": ["NamedDatabaseItem"],
        "_1830": ["NamedKey"],
        "_1831": ["SQLDatabase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Database",
    "DatabaseConnectionSettings",
    "DatabaseKey",
    "DatabaseSettings",
    "NamedDatabase",
    "NamedDatabaseItem",
    "NamedKey",
    "SQLDatabase",
)

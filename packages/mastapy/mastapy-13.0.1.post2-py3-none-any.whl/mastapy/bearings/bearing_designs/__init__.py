"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2130 import BearingDesign
    from ._2131 import DetailedBearing
    from ._2132 import DummyRollingBearing
    from ._2133 import LinearBearing
    from ._2134 import NonLinearBearing
else:
    import_structure = {
        "_2130": ["BearingDesign"],
        "_2131": ["DetailedBearing"],
        "_2132": ["DummyRollingBearing"],
        "_2133": ["LinearBearing"],
        "_2134": ["NonLinearBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingDesign",
    "DetailedBearing",
    "DummyRollingBearing",
    "LinearBearing",
    "NonLinearBearing",
)

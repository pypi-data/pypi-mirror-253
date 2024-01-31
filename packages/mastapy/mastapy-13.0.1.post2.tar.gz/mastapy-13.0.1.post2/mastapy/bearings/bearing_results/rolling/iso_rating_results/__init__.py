"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2101 import BallISO2812007Results
    from ._2102 import BallISOTS162812008Results
    from ._2103 import ISO2812007Results
    from ._2104 import ISO762006Results
    from ._2105 import ISOResults
    from ._2106 import ISOTS162812008Results
    from ._2107 import RollerISO2812007Results
    from ._2108 import RollerISOTS162812008Results
    from ._2109 import StressConcentrationMethod
else:
    import_structure = {
        "_2101": ["BallISO2812007Results"],
        "_2102": ["BallISOTS162812008Results"],
        "_2103": ["ISO2812007Results"],
        "_2104": ["ISO762006Results"],
        "_2105": ["ISOResults"],
        "_2106": ["ISOTS162812008Results"],
        "_2107": ["RollerISO2812007Results"],
        "_2108": ["RollerISOTS162812008Results"],
        "_2109": ["StressConcentrationMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallISO2812007Results",
    "BallISOTS162812008Results",
    "ISO2812007Results",
    "ISO762006Results",
    "ISOResults",
    "ISOTS162812008Results",
    "RollerISO2812007Results",
    "RollerISOTS162812008Results",
    "StressConcentrationMethod",
)

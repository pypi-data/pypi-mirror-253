"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2333 import CycloidalDiscAxialLeftSocket
    from ._2334 import CycloidalDiscAxialRightSocket
    from ._2335 import CycloidalDiscCentralBearingConnection
    from ._2336 import CycloidalDiscInnerSocket
    from ._2337 import CycloidalDiscOuterSocket
    from ._2338 import CycloidalDiscPlanetaryBearingConnection
    from ._2339 import CycloidalDiscPlanetaryBearingSocket
    from ._2340 import RingPinsSocket
    from ._2341 import RingPinsToDiscConnection
else:
    import_structure = {
        "_2333": ["CycloidalDiscAxialLeftSocket"],
        "_2334": ["CycloidalDiscAxialRightSocket"],
        "_2335": ["CycloidalDiscCentralBearingConnection"],
        "_2336": ["CycloidalDiscInnerSocket"],
        "_2337": ["CycloidalDiscOuterSocket"],
        "_2338": ["CycloidalDiscPlanetaryBearingConnection"],
        "_2339": ["CycloidalDiscPlanetaryBearingSocket"],
        "_2340": ["RingPinsSocket"],
        "_2341": ["RingPinsToDiscConnection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CycloidalDiscAxialLeftSocket",
    "CycloidalDiscAxialRightSocket",
    "CycloidalDiscCentralBearingConnection",
    "CycloidalDiscInnerSocket",
    "CycloidalDiscOuterSocket",
    "CycloidalDiscPlanetaryBearingConnection",
    "CycloidalDiscPlanetaryBearingSocket",
    "RingPinsSocket",
    "RingPinsToDiscConnection",
)

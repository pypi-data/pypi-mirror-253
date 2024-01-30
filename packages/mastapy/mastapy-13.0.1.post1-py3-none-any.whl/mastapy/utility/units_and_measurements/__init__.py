"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1602 import DegreesMinutesSeconds
    from ._1603 import EnumUnit
    from ._1604 import InverseUnit
    from ._1605 import MeasurementBase
    from ._1606 import MeasurementSettings
    from ._1607 import MeasurementSystem
    from ._1608 import SafetyFactorUnit
    from ._1609 import TimeUnit
    from ._1610 import Unit
    from ._1611 import UnitGradient
else:
    import_structure = {
        "_1602": ["DegreesMinutesSeconds"],
        "_1603": ["EnumUnit"],
        "_1604": ["InverseUnit"],
        "_1605": ["MeasurementBase"],
        "_1606": ["MeasurementSettings"],
        "_1607": ["MeasurementSystem"],
        "_1608": ["SafetyFactorUnit"],
        "_1609": ["TimeUnit"],
        "_1610": ["Unit"],
        "_1611": ["UnitGradient"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DegreesMinutesSeconds",
    "EnumUnit",
    "InverseUnit",
    "MeasurementBase",
    "MeasurementSettings",
    "MeasurementSystem",
    "SafetyFactorUnit",
    "TimeUnit",
    "Unit",
    "UnitGradient",
)

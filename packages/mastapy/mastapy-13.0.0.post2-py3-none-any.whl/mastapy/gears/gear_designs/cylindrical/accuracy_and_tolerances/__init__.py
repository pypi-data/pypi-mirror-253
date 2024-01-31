"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1132 import AGMA2000A88AccuracyGrader
    from ._1133 import AGMA20151A01AccuracyGrader
    from ._1134 import AGMA20151AccuracyGrades
    from ._1135 import AGMAISO13281B14AccuracyGrader
    from ._1136 import CylindricalAccuracyGrader
    from ._1137 import CylindricalAccuracyGraderWithProfileFormAndSlope
    from ._1138 import CylindricalAccuracyGrades
    from ._1139 import CylindricalGearAccuracyTolerances
    from ._1140 import DIN3967SystemOfGearFits
    from ._1141 import ISO132811995AccuracyGrader
    from ._1142 import ISO132812013AccuracyGrader
    from ._1143 import ISO1328AccuracyGraderCommon
    from ._1144 import ISO1328AccuracyGrades
    from ._1145 import OverridableTolerance
else:
    import_structure = {
        "_1132": ["AGMA2000A88AccuracyGrader"],
        "_1133": ["AGMA20151A01AccuracyGrader"],
        "_1134": ["AGMA20151AccuracyGrades"],
        "_1135": ["AGMAISO13281B14AccuracyGrader"],
        "_1136": ["CylindricalAccuracyGrader"],
        "_1137": ["CylindricalAccuracyGraderWithProfileFormAndSlope"],
        "_1138": ["CylindricalAccuracyGrades"],
        "_1139": ["CylindricalGearAccuracyTolerances"],
        "_1140": ["DIN3967SystemOfGearFits"],
        "_1141": ["ISO132811995AccuracyGrader"],
        "_1142": ["ISO132812013AccuracyGrader"],
        "_1143": ["ISO1328AccuracyGraderCommon"],
        "_1144": ["ISO1328AccuracyGrades"],
        "_1145": ["OverridableTolerance"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMA2000A88AccuracyGrader",
    "AGMA20151A01AccuracyGrader",
    "AGMA20151AccuracyGrades",
    "AGMAISO13281B14AccuracyGrader",
    "CylindricalAccuracyGrader",
    "CylindricalAccuracyGraderWithProfileFormAndSlope",
    "CylindricalAccuracyGrades",
    "CylindricalGearAccuracyTolerances",
    "DIN3967SystemOfGearFits",
    "ISO132811995AccuracyGrader",
    "ISO132812013AccuracyGrader",
    "ISO1328AccuracyGraderCommon",
    "ISO1328AccuracyGrades",
    "OverridableTolerance",
)

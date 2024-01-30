"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1208 import CylindricalGearLTCAContactChartDataAsTextFile
    from ._1209 import CylindricalGearLTCAContactCharts
    from ._1210 import CylindricalGearWorstLTCAContactChartDataAsTextFile
    from ._1211 import CylindricalGearWorstLTCAContactCharts
    from ._1212 import GearLTCAContactChartDataAsTextFile
    from ._1213 import GearLTCAContactCharts
    from ._1214 import PointsWithWorstResults
else:
    import_structure = {
        "_1208": ["CylindricalGearLTCAContactChartDataAsTextFile"],
        "_1209": ["CylindricalGearLTCAContactCharts"],
        "_1210": ["CylindricalGearWorstLTCAContactChartDataAsTextFile"],
        "_1211": ["CylindricalGearWorstLTCAContactCharts"],
        "_1212": ["GearLTCAContactChartDataAsTextFile"],
        "_1213": ["GearLTCAContactCharts"],
        "_1214": ["PointsWithWorstResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearLTCAContactChartDataAsTextFile",
    "CylindricalGearLTCAContactCharts",
    "CylindricalGearWorstLTCAContactChartDataAsTextFile",
    "CylindricalGearWorstLTCAContactCharts",
    "GearLTCAContactChartDataAsTextFile",
    "GearLTCAContactCharts",
    "PointsWithWorstResults",
)

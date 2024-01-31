"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1852 import BubbleChartDefinition
    from ._1853 import ConstantLine
    from ._1854 import CustomLineChart
    from ._1855 import CustomTableAndChart
    from ._1856 import LegacyChartMathChartDefinition
    from ._1857 import MatrixVisualisationDefinition
    from ._1858 import ModeConstantLine
    from ._1859 import NDChartDefinition
    from ._1860 import ParallelCoordinatesChartDefinition
    from ._1861 import PointsForSurface
    from ._1862 import ScatterChartDefinition
    from ._1863 import Series2D
    from ._1864 import SMTAxis
    from ._1865 import ThreeDChartDefinition
    from ._1866 import ThreeDVectorChartDefinition
    from ._1867 import TwoDChartDefinition
else:
    import_structure = {
        "_1852": ["BubbleChartDefinition"],
        "_1853": ["ConstantLine"],
        "_1854": ["CustomLineChart"],
        "_1855": ["CustomTableAndChart"],
        "_1856": ["LegacyChartMathChartDefinition"],
        "_1857": ["MatrixVisualisationDefinition"],
        "_1858": ["ModeConstantLine"],
        "_1859": ["NDChartDefinition"],
        "_1860": ["ParallelCoordinatesChartDefinition"],
        "_1861": ["PointsForSurface"],
        "_1862": ["ScatterChartDefinition"],
        "_1863": ["Series2D"],
        "_1864": ["SMTAxis"],
        "_1865": ["ThreeDChartDefinition"],
        "_1866": ["ThreeDVectorChartDefinition"],
        "_1867": ["TwoDChartDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BubbleChartDefinition",
    "ConstantLine",
    "CustomLineChart",
    "CustomTableAndChart",
    "LegacyChartMathChartDefinition",
    "MatrixVisualisationDefinition",
    "ModeConstantLine",
    "NDChartDefinition",
    "ParallelCoordinatesChartDefinition",
    "PointsForSurface",
    "ScatterChartDefinition",
    "Series2D",
    "SMTAxis",
    "ThreeDChartDefinition",
    "ThreeDVectorChartDefinition",
    "TwoDChartDefinition",
)

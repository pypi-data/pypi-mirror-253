"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7535 import AnalysisCase
    from ._7536 import AbstractAnalysisOptions
    from ._7537 import CompoundAnalysisCase
    from ._7538 import ConnectionAnalysisCase
    from ._7539 import ConnectionCompoundAnalysis
    from ._7540 import ConnectionFEAnalysis
    from ._7541 import ConnectionStaticLoadAnalysisCase
    from ._7542 import ConnectionTimeSeriesLoadAnalysisCase
    from ._7543 import DesignEntityCompoundAnalysis
    from ._7544 import FEAnalysis
    from ._7545 import PartAnalysisCase
    from ._7546 import PartCompoundAnalysis
    from ._7547 import PartFEAnalysis
    from ._7548 import PartStaticLoadAnalysisCase
    from ._7549 import PartTimeSeriesLoadAnalysisCase
    from ._7550 import StaticLoadAnalysisCase
    from ._7551 import TimeSeriesLoadAnalysisCase
else:
    import_structure = {
        "_7535": ["AnalysisCase"],
        "_7536": ["AbstractAnalysisOptions"],
        "_7537": ["CompoundAnalysisCase"],
        "_7538": ["ConnectionAnalysisCase"],
        "_7539": ["ConnectionCompoundAnalysis"],
        "_7540": ["ConnectionFEAnalysis"],
        "_7541": ["ConnectionStaticLoadAnalysisCase"],
        "_7542": ["ConnectionTimeSeriesLoadAnalysisCase"],
        "_7543": ["DesignEntityCompoundAnalysis"],
        "_7544": ["FEAnalysis"],
        "_7545": ["PartAnalysisCase"],
        "_7546": ["PartCompoundAnalysis"],
        "_7547": ["PartFEAnalysis"],
        "_7548": ["PartStaticLoadAnalysisCase"],
        "_7549": ["PartTimeSeriesLoadAnalysisCase"],
        "_7550": ["StaticLoadAnalysisCase"],
        "_7551": ["TimeSeriesLoadAnalysisCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AnalysisCase",
    "AbstractAnalysisOptions",
    "CompoundAnalysisCase",
    "ConnectionAnalysisCase",
    "ConnectionCompoundAnalysis",
    "ConnectionFEAnalysis",
    "ConnectionStaticLoadAnalysisCase",
    "ConnectionTimeSeriesLoadAnalysisCase",
    "DesignEntityCompoundAnalysis",
    "FEAnalysis",
    "PartAnalysisCase",
    "PartCompoundAnalysis",
    "PartFEAnalysis",
    "PartStaticLoadAnalysisCase",
    "PartTimeSeriesLoadAnalysisCase",
    "StaticLoadAnalysisCase",
    "TimeSeriesLoadAnalysisCase",
)

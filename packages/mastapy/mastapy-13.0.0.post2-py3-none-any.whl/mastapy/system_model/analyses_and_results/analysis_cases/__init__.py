"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7534 import AnalysisCase
    from ._7535 import AbstractAnalysisOptions
    from ._7536 import CompoundAnalysisCase
    from ._7537 import ConnectionAnalysisCase
    from ._7538 import ConnectionCompoundAnalysis
    from ._7539 import ConnectionFEAnalysis
    from ._7540 import ConnectionStaticLoadAnalysisCase
    from ._7541 import ConnectionTimeSeriesLoadAnalysisCase
    from ._7542 import DesignEntityCompoundAnalysis
    from ._7543 import FEAnalysis
    from ._7544 import PartAnalysisCase
    from ._7545 import PartCompoundAnalysis
    from ._7546 import PartFEAnalysis
    from ._7547 import PartStaticLoadAnalysisCase
    from ._7548 import PartTimeSeriesLoadAnalysisCase
    from ._7549 import StaticLoadAnalysisCase
    from ._7550 import TimeSeriesLoadAnalysisCase
else:
    import_structure = {
        "_7534": ["AnalysisCase"],
        "_7535": ["AbstractAnalysisOptions"],
        "_7536": ["CompoundAnalysisCase"],
        "_7537": ["ConnectionAnalysisCase"],
        "_7538": ["ConnectionCompoundAnalysis"],
        "_7539": ["ConnectionFEAnalysis"],
        "_7540": ["ConnectionStaticLoadAnalysisCase"],
        "_7541": ["ConnectionTimeSeriesLoadAnalysisCase"],
        "_7542": ["DesignEntityCompoundAnalysis"],
        "_7543": ["FEAnalysis"],
        "_7544": ["PartAnalysisCase"],
        "_7545": ["PartCompoundAnalysis"],
        "_7546": ["PartFEAnalysis"],
        "_7547": ["PartStaticLoadAnalysisCase"],
        "_7548": ["PartTimeSeriesLoadAnalysisCase"],
        "_7549": ["StaticLoadAnalysisCase"],
        "_7550": ["TimeSeriesLoadAnalysisCase"],
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

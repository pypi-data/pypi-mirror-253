"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6268 import CombinationAnalysis
    from ._6269 import FlexiblePinAnalysis
    from ._6270 import FlexiblePinAnalysisConceptLevel
    from ._6271 import FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
    from ._6272 import FlexiblePinAnalysisGearAndBearingRating
    from ._6273 import FlexiblePinAnalysisManufactureLevel
    from ._6274 import FlexiblePinAnalysisOptions
    from ._6275 import FlexiblePinAnalysisStopStartAnalysis
    from ._6276 import WindTurbineCertificationReport
else:
    import_structure = {
        "_6268": ["CombinationAnalysis"],
        "_6269": ["FlexiblePinAnalysis"],
        "_6270": ["FlexiblePinAnalysisConceptLevel"],
        "_6271": ["FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass"],
        "_6272": ["FlexiblePinAnalysisGearAndBearingRating"],
        "_6273": ["FlexiblePinAnalysisManufactureLevel"],
        "_6274": ["FlexiblePinAnalysisOptions"],
        "_6275": ["FlexiblePinAnalysisStopStartAnalysis"],
        "_6276": ["WindTurbineCertificationReport"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CombinationAnalysis",
    "FlexiblePinAnalysis",
    "FlexiblePinAnalysisConceptLevel",
    "FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass",
    "FlexiblePinAnalysisGearAndBearingRating",
    "FlexiblePinAnalysisManufactureLevel",
    "FlexiblePinAnalysisOptions",
    "FlexiblePinAnalysisStopStartAnalysis",
    "WindTurbineCertificationReport",
)

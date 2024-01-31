"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6267 import CombinationAnalysis
    from ._6268 import FlexiblePinAnalysis
    from ._6269 import FlexiblePinAnalysisConceptLevel
    from ._6270 import FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass
    from ._6271 import FlexiblePinAnalysisGearAndBearingRating
    from ._6272 import FlexiblePinAnalysisManufactureLevel
    from ._6273 import FlexiblePinAnalysisOptions
    from ._6274 import FlexiblePinAnalysisStopStartAnalysis
    from ._6275 import WindTurbineCertificationReport
else:
    import_structure = {
        "_6267": ["CombinationAnalysis"],
        "_6268": ["FlexiblePinAnalysis"],
        "_6269": ["FlexiblePinAnalysisConceptLevel"],
        "_6270": ["FlexiblePinAnalysisDetailLevelAndPinFatigueOneToothPass"],
        "_6271": ["FlexiblePinAnalysisGearAndBearingRating"],
        "_6272": ["FlexiblePinAnalysisManufactureLevel"],
        "_6273": ["FlexiblePinAnalysisOptions"],
        "_6274": ["FlexiblePinAnalysisStopStartAnalysis"],
        "_6275": ["WindTurbineCertificationReport"],
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

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2261 import AdvancedTimeSteppingAnalysisForModulationModeViewOptions
    from ._2262 import ExcitationAnalysisViewOption
    from ._2263 import ModalContributionViewOptions
else:
    import_structure = {
        "_2261": ["AdvancedTimeSteppingAnalysisForModulationModeViewOptions"],
        "_2262": ["ExcitationAnalysisViewOption"],
        "_2263": ["ModalContributionViewOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
    "ExcitationAnalysisViewOption",
    "ModalContributionViewOptions",
)

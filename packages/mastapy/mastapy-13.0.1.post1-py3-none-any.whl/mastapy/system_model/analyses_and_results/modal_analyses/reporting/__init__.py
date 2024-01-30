"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4716 import CalculateFullFEResultsForMode
    from ._4717 import CampbellDiagramReport
    from ._4718 import ComponentPerModeResult
    from ._4719 import DesignEntityModalAnalysisGroupResults
    from ._4720 import ModalCMSResultsForModeAndFE
    from ._4721 import PerModeResultsReport
    from ._4722 import RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis
    from ._4723 import RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
    from ._4724 import RigidlyConnectedDesignEntityGroupModalAnalysis
    from ._4725 import ShaftPerModeResult
    from ._4726 import SingleExcitationResultsModalAnalysis
    from ._4727 import SingleModeResults
else:
    import_structure = {
        "_4716": ["CalculateFullFEResultsForMode"],
        "_4717": ["CampbellDiagramReport"],
        "_4718": ["ComponentPerModeResult"],
        "_4719": ["DesignEntityModalAnalysisGroupResults"],
        "_4720": ["ModalCMSResultsForModeAndFE"],
        "_4721": ["PerModeResultsReport"],
        "_4722": ["RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis"],
        "_4723": ["RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis"],
        "_4724": ["RigidlyConnectedDesignEntityGroupModalAnalysis"],
        "_4725": ["ShaftPerModeResult"],
        "_4726": ["SingleExcitationResultsModalAnalysis"],
        "_4727": ["SingleModeResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CalculateFullFEResultsForMode",
    "CampbellDiagramReport",
    "ComponentPerModeResult",
    "DesignEntityModalAnalysisGroupResults",
    "ModalCMSResultsForModeAndFE",
    "PerModeResultsReport",
    "RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis",
    "RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis",
    "RigidlyConnectedDesignEntityGroupModalAnalysis",
    "ShaftPerModeResult",
    "SingleExcitationResultsModalAnalysis",
    "SingleModeResults",
)

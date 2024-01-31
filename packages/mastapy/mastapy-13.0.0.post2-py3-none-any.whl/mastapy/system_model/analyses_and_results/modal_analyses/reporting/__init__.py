"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4715 import CalculateFullFEResultsForMode
    from ._4716 import CampbellDiagramReport
    from ._4717 import ComponentPerModeResult
    from ._4718 import DesignEntityModalAnalysisGroupResults
    from ._4719 import ModalCMSResultsForModeAndFE
    from ._4720 import PerModeResultsReport
    from ._4721 import RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis
    from ._4722 import RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis
    from ._4723 import RigidlyConnectedDesignEntityGroupModalAnalysis
    from ._4724 import ShaftPerModeResult
    from ._4725 import SingleExcitationResultsModalAnalysis
    from ._4726 import SingleModeResults
else:
    import_structure = {
        "_4715": ["CalculateFullFEResultsForMode"],
        "_4716": ["CampbellDiagramReport"],
        "_4717": ["ComponentPerModeResult"],
        "_4718": ["DesignEntityModalAnalysisGroupResults"],
        "_4719": ["ModalCMSResultsForModeAndFE"],
        "_4720": ["PerModeResultsReport"],
        "_4721": ["RigidlyConnectedDesignEntityGroupForSingleExcitationModalAnalysis"],
        "_4722": ["RigidlyConnectedDesignEntityGroupForSingleModeModalAnalysis"],
        "_4723": ["RigidlyConnectedDesignEntityGroupModalAnalysis"],
        "_4724": ["ShaftPerModeResult"],
        "_4725": ["SingleExcitationResultsModalAnalysis"],
        "_4726": ["SingleModeResults"],
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

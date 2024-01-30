"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5658 import AbstractDesignStateLoadCaseGroup
    from ._5659 import AbstractLoadCaseGroup
    from ._5660 import AbstractStaticLoadCaseGroup
    from ._5661 import ClutchEngagementStatus
    from ._5662 import ConceptSynchroGearEngagementStatus
    from ._5663 import DesignState
    from ._5664 import DutyCycle
    from ._5665 import GenericClutchEngagementStatus
    from ._5666 import LoadCaseGroupHistograms
    from ._5667 import SubGroupInSingleDesignState
    from ._5668 import SystemOptimisationGearSet
    from ._5669 import SystemOptimiserGearSetOptimisation
    from ._5670 import SystemOptimiserTargets
    from ._5671 import TimeSeriesLoadCaseGroup
else:
    import_structure = {
        "_5658": ["AbstractDesignStateLoadCaseGroup"],
        "_5659": ["AbstractLoadCaseGroup"],
        "_5660": ["AbstractStaticLoadCaseGroup"],
        "_5661": ["ClutchEngagementStatus"],
        "_5662": ["ConceptSynchroGearEngagementStatus"],
        "_5663": ["DesignState"],
        "_5664": ["DutyCycle"],
        "_5665": ["GenericClutchEngagementStatus"],
        "_5666": ["LoadCaseGroupHistograms"],
        "_5667": ["SubGroupInSingleDesignState"],
        "_5668": ["SystemOptimisationGearSet"],
        "_5669": ["SystemOptimiserGearSetOptimisation"],
        "_5670": ["SystemOptimiserTargets"],
        "_5671": ["TimeSeriesLoadCaseGroup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractDesignStateLoadCaseGroup",
    "AbstractLoadCaseGroup",
    "AbstractStaticLoadCaseGroup",
    "ClutchEngagementStatus",
    "ConceptSynchroGearEngagementStatus",
    "DesignState",
    "DutyCycle",
    "GenericClutchEngagementStatus",
    "LoadCaseGroupHistograms",
    "SubGroupInSingleDesignState",
    "SystemOptimisationGearSet",
    "SystemOptimiserGearSetOptimisation",
    "SystemOptimiserTargets",
    "TimeSeriesLoadCaseGroup",
)

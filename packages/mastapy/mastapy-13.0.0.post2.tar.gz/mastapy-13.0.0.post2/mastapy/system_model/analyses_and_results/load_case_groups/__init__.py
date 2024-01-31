"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5657 import AbstractDesignStateLoadCaseGroup
    from ._5658 import AbstractLoadCaseGroup
    from ._5659 import AbstractStaticLoadCaseGroup
    from ._5660 import ClutchEngagementStatus
    from ._5661 import ConceptSynchroGearEngagementStatus
    from ._5662 import DesignState
    from ._5663 import DutyCycle
    from ._5664 import GenericClutchEngagementStatus
    from ._5665 import LoadCaseGroupHistograms
    from ._5666 import SubGroupInSingleDesignState
    from ._5667 import SystemOptimisationGearSet
    from ._5668 import SystemOptimiserGearSetOptimisation
    from ._5669 import SystemOptimiserTargets
    from ._5670 import TimeSeriesLoadCaseGroup
else:
    import_structure = {
        "_5657": ["AbstractDesignStateLoadCaseGroup"],
        "_5658": ["AbstractLoadCaseGroup"],
        "_5659": ["AbstractStaticLoadCaseGroup"],
        "_5660": ["ClutchEngagementStatus"],
        "_5661": ["ConceptSynchroGearEngagementStatus"],
        "_5662": ["DesignState"],
        "_5663": ["DutyCycle"],
        "_5664": ["GenericClutchEngagementStatus"],
        "_5665": ["LoadCaseGroupHistograms"],
        "_5666": ["SubGroupInSingleDesignState"],
        "_5667": ["SystemOptimisationGearSet"],
        "_5668": ["SystemOptimiserGearSetOptimisation"],
        "_5669": ["SystemOptimiserTargets"],
        "_5670": ["TimeSeriesLoadCaseGroup"],
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

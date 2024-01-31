"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._749 import ActiveProfileRangeCalculationSource
    from ._750 import AxialShaverRedressing
    from ._751 import ConventionalShavingDynamics
    from ._752 import ConventionalShavingDynamicsCalculationForDesignedGears
    from ._753 import ConventionalShavingDynamicsCalculationForHobbedGears
    from ._754 import ConventionalShavingDynamicsViewModel
    from ._755 import PlungeShaverDynamics
    from ._756 import PlungeShaverDynamicSettings
    from ._757 import PlungeShaverRedressing
    from ._758 import PlungeShavingDynamicsCalculationForDesignedGears
    from ._759 import PlungeShavingDynamicsCalculationForHobbedGears
    from ._760 import PlungeShavingDynamicsViewModel
    from ._761 import RedressingSettings
    from ._762 import RollAngleRangeRelativeToAccuracy
    from ._763 import RollAngleReportObject
    from ._764 import ShaverRedressing
    from ._765 import ShavingDynamics
    from ._766 import ShavingDynamicsCalculation
    from ._767 import ShavingDynamicsCalculationForDesignedGears
    from ._768 import ShavingDynamicsCalculationForHobbedGears
    from ._769 import ShavingDynamicsConfiguration
    from ._770 import ShavingDynamicsViewModel
    from ._771 import ShavingDynamicsViewModelBase
else:
    import_structure = {
        "_749": ["ActiveProfileRangeCalculationSource"],
        "_750": ["AxialShaverRedressing"],
        "_751": ["ConventionalShavingDynamics"],
        "_752": ["ConventionalShavingDynamicsCalculationForDesignedGears"],
        "_753": ["ConventionalShavingDynamicsCalculationForHobbedGears"],
        "_754": ["ConventionalShavingDynamicsViewModel"],
        "_755": ["PlungeShaverDynamics"],
        "_756": ["PlungeShaverDynamicSettings"],
        "_757": ["PlungeShaverRedressing"],
        "_758": ["PlungeShavingDynamicsCalculationForDesignedGears"],
        "_759": ["PlungeShavingDynamicsCalculationForHobbedGears"],
        "_760": ["PlungeShavingDynamicsViewModel"],
        "_761": ["RedressingSettings"],
        "_762": ["RollAngleRangeRelativeToAccuracy"],
        "_763": ["RollAngleReportObject"],
        "_764": ["ShaverRedressing"],
        "_765": ["ShavingDynamics"],
        "_766": ["ShavingDynamicsCalculation"],
        "_767": ["ShavingDynamicsCalculationForDesignedGears"],
        "_768": ["ShavingDynamicsCalculationForHobbedGears"],
        "_769": ["ShavingDynamicsConfiguration"],
        "_770": ["ShavingDynamicsViewModel"],
        "_771": ["ShavingDynamicsViewModelBase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveProfileRangeCalculationSource",
    "AxialShaverRedressing",
    "ConventionalShavingDynamics",
    "ConventionalShavingDynamicsCalculationForDesignedGears",
    "ConventionalShavingDynamicsCalculationForHobbedGears",
    "ConventionalShavingDynamicsViewModel",
    "PlungeShaverDynamics",
    "PlungeShaverDynamicSettings",
    "PlungeShaverRedressing",
    "PlungeShavingDynamicsCalculationForDesignedGears",
    "PlungeShavingDynamicsCalculationForHobbedGears",
    "PlungeShavingDynamicsViewModel",
    "RedressingSettings",
    "RollAngleRangeRelativeToAccuracy",
    "RollAngleReportObject",
    "ShaverRedressing",
    "ShavingDynamics",
    "ShavingDynamicsCalculation",
    "ShavingDynamicsCalculationForDesignedGears",
    "ShavingDynamicsCalculationForHobbedGears",
    "ShavingDynamicsConfiguration",
    "ShavingDynamicsViewModel",
    "ShavingDynamicsViewModelBase",
)

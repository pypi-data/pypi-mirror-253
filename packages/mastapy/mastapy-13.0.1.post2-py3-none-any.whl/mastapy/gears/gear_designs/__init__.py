"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._940 import BevelHypoidGearDesignSettingsDatabase
    from ._941 import BevelHypoidGearDesignSettingsItem
    from ._942 import BevelHypoidGearRatingSettingsDatabase
    from ._943 import BevelHypoidGearRatingSettingsItem
    from ._944 import DesignConstraint
    from ._945 import DesignConstraintCollectionDatabase
    from ._946 import DesignConstraintsCollection
    from ._947 import GearDesign
    from ._948 import GearDesignComponent
    from ._949 import GearMeshDesign
    from ._950 import GearSetDesign
    from ._951 import SelectedDesignConstraintsCollection
else:
    import_structure = {
        "_940": ["BevelHypoidGearDesignSettingsDatabase"],
        "_941": ["BevelHypoidGearDesignSettingsItem"],
        "_942": ["BevelHypoidGearRatingSettingsDatabase"],
        "_943": ["BevelHypoidGearRatingSettingsItem"],
        "_944": ["DesignConstraint"],
        "_945": ["DesignConstraintCollectionDatabase"],
        "_946": ["DesignConstraintsCollection"],
        "_947": ["GearDesign"],
        "_948": ["GearDesignComponent"],
        "_949": ["GearMeshDesign"],
        "_950": ["GearSetDesign"],
        "_951": ["SelectedDesignConstraintsCollection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelHypoidGearDesignSettingsDatabase",
    "BevelHypoidGearDesignSettingsItem",
    "BevelHypoidGearRatingSettingsDatabase",
    "BevelHypoidGearRatingSettingsItem",
    "DesignConstraint",
    "DesignConstraintCollectionDatabase",
    "DesignConstraintsCollection",
    "GearDesign",
    "GearDesignComponent",
    "GearMeshDesign",
    "GearSetDesign",
    "SelectedDesignConstraintsCollection",
)

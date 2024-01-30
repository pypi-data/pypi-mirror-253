"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._292 import BearingEfficiencyRatingMethod
    from ._293 import CombinedResistiveTorque
    from ._294 import EfficiencyRatingMethod
    from ._295 import IndependentPowerLoss
    from ._296 import IndependentResistiveTorque
    from ._297 import LoadAndSpeedCombinedPowerLoss
    from ._298 import OilPumpDetail
    from ._299 import OilPumpDriveType
    from ._300 import OilSealLossCalculationMethod
    from ._301 import OilSealMaterialType
    from ._302 import PowerLoss
    from ._303 import ResistiveTorque
else:
    import_structure = {
        "_292": ["BearingEfficiencyRatingMethod"],
        "_293": ["CombinedResistiveTorque"],
        "_294": ["EfficiencyRatingMethod"],
        "_295": ["IndependentPowerLoss"],
        "_296": ["IndependentResistiveTorque"],
        "_297": ["LoadAndSpeedCombinedPowerLoss"],
        "_298": ["OilPumpDetail"],
        "_299": ["OilPumpDriveType"],
        "_300": ["OilSealLossCalculationMethod"],
        "_301": ["OilSealMaterialType"],
        "_302": ["PowerLoss"],
        "_303": ["ResistiveTorque"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingEfficiencyRatingMethod",
    "CombinedResistiveTorque",
    "EfficiencyRatingMethod",
    "IndependentPowerLoss",
    "IndependentResistiveTorque",
    "LoadAndSpeedCombinedPowerLoss",
    "OilPumpDetail",
    "OilPumpDriveType",
    "OilSealLossCalculationMethod",
    "OilSealMaterialType",
    "PowerLoss",
    "ResistiveTorque",
)

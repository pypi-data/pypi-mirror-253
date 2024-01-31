"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1150 import ActiveConicalFlank
    from ._1151 import BacklashDistributionRule
    from ._1152 import ConicalFlanks
    from ._1153 import ConicalGearCutter
    from ._1154 import ConicalGearDesign
    from ._1155 import ConicalGearMeshDesign
    from ._1156 import ConicalGearSetDesign
    from ._1157 import ConicalMachineSettingCalculationMethods
    from ._1158 import ConicalManufactureMethods
    from ._1159 import ConicalMeshedGearDesign
    from ._1160 import ConicalMeshMisalignments
    from ._1161 import CutterBladeType
    from ._1162 import CutterGaugeLengths
    from ._1163 import DummyConicalGearCutter
    from ._1164 import FrontEndTypes
    from ._1165 import GleasonSafetyRequirements
    from ._1166 import KIMoSBevelHypoidSingleLoadCaseResultsData
    from ._1167 import KIMoSBevelHypoidSingleRotationAngleResult
    from ._1168 import KlingelnbergFinishingMethods
    from ._1169 import LoadDistributionFactorMethods
    from ._1170 import TopremEntryType
    from ._1171 import TopremLetter
else:
    import_structure = {
        "_1150": ["ActiveConicalFlank"],
        "_1151": ["BacklashDistributionRule"],
        "_1152": ["ConicalFlanks"],
        "_1153": ["ConicalGearCutter"],
        "_1154": ["ConicalGearDesign"],
        "_1155": ["ConicalGearMeshDesign"],
        "_1156": ["ConicalGearSetDesign"],
        "_1157": ["ConicalMachineSettingCalculationMethods"],
        "_1158": ["ConicalManufactureMethods"],
        "_1159": ["ConicalMeshedGearDesign"],
        "_1160": ["ConicalMeshMisalignments"],
        "_1161": ["CutterBladeType"],
        "_1162": ["CutterGaugeLengths"],
        "_1163": ["DummyConicalGearCutter"],
        "_1164": ["FrontEndTypes"],
        "_1165": ["GleasonSafetyRequirements"],
        "_1166": ["KIMoSBevelHypoidSingleLoadCaseResultsData"],
        "_1167": ["KIMoSBevelHypoidSingleRotationAngleResult"],
        "_1168": ["KlingelnbergFinishingMethods"],
        "_1169": ["LoadDistributionFactorMethods"],
        "_1170": ["TopremEntryType"],
        "_1171": ["TopremLetter"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveConicalFlank",
    "BacklashDistributionRule",
    "ConicalFlanks",
    "ConicalGearCutter",
    "ConicalGearDesign",
    "ConicalGearMeshDesign",
    "ConicalGearSetDesign",
    "ConicalMachineSettingCalculationMethods",
    "ConicalManufactureMethods",
    "ConicalMeshedGearDesign",
    "ConicalMeshMisalignments",
    "CutterBladeType",
    "CutterGaugeLengths",
    "DummyConicalGearCutter",
    "FrontEndTypes",
    "GleasonSafetyRequirements",
    "KIMoSBevelHypoidSingleLoadCaseResultsData",
    "KIMoSBevelHypoidSingleRotationAngleResult",
    "KlingelnbergFinishingMethods",
    "LoadDistributionFactorMethods",
    "TopremEntryType",
    "TopremLetter",
)

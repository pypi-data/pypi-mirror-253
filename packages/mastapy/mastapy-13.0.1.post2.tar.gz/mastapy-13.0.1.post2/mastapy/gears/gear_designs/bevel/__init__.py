"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1179 import AGMAGleasonConicalGearGeometryMethods
    from ._1180 import BevelGearDesign
    from ._1181 import BevelGearMeshDesign
    from ._1182 import BevelGearSetDesign
    from ._1183 import BevelMeshedGearDesign
    from ._1184 import DrivenMachineCharacteristicGleason
    from ._1185 import EdgeRadiusType
    from ._1186 import FinishingMethods
    from ._1187 import MachineCharacteristicAGMAKlingelnberg
    from ._1188 import PrimeMoverCharacteristicGleason
    from ._1189 import ToothProportionsInputMethod
    from ._1190 import ToothThicknessSpecificationMethod
    from ._1191 import WheelFinishCutterPointWidthRestrictionMethod
else:
    import_structure = {
        "_1179": ["AGMAGleasonConicalGearGeometryMethods"],
        "_1180": ["BevelGearDesign"],
        "_1181": ["BevelGearMeshDesign"],
        "_1182": ["BevelGearSetDesign"],
        "_1183": ["BevelMeshedGearDesign"],
        "_1184": ["DrivenMachineCharacteristicGleason"],
        "_1185": ["EdgeRadiusType"],
        "_1186": ["FinishingMethods"],
        "_1187": ["MachineCharacteristicAGMAKlingelnberg"],
        "_1188": ["PrimeMoverCharacteristicGleason"],
        "_1189": ["ToothProportionsInputMethod"],
        "_1190": ["ToothThicknessSpecificationMethod"],
        "_1191": ["WheelFinishCutterPointWidthRestrictionMethod"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearGeometryMethods",
    "BevelGearDesign",
    "BevelGearMeshDesign",
    "BevelGearSetDesign",
    "BevelMeshedGearDesign",
    "DrivenMachineCharacteristicGleason",
    "EdgeRadiusType",
    "FinishingMethods",
    "MachineCharacteristicAGMAKlingelnberg",
    "PrimeMoverCharacteristicGleason",
    "ToothProportionsInputMethod",
    "ToothThicknessSpecificationMethod",
    "WheelFinishCutterPointWidthRestrictionMethod",
)

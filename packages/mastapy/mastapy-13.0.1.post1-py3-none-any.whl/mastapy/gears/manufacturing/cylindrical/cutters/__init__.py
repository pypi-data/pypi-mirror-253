"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._703 import CurveInLinkedList
    from ._704 import CustomisableEdgeProfile
    from ._705 import CylindricalFormedWheelGrinderDatabase
    from ._706 import CylindricalGearAbstractCutterDesign
    from ._707 import CylindricalGearFormGrindingWheel
    from ._708 import CylindricalGearGrindingWorm
    from ._709 import CylindricalGearHobDesign
    from ._710 import CylindricalGearPlungeShaver
    from ._711 import CylindricalGearPlungeShaverDatabase
    from ._712 import CylindricalGearRackDesign
    from ._713 import CylindricalGearRealCutterDesign
    from ._714 import CylindricalGearShaper
    from ._715 import CylindricalGearShaver
    from ._716 import CylindricalGearShaverDatabase
    from ._717 import CylindricalWormGrinderDatabase
    from ._718 import InvoluteCutterDesign
    from ._719 import MutableCommon
    from ._720 import MutableCurve
    from ._721 import MutableFillet
    from ._722 import RoughCutterCreationSettings
else:
    import_structure = {
        "_703": ["CurveInLinkedList"],
        "_704": ["CustomisableEdgeProfile"],
        "_705": ["CylindricalFormedWheelGrinderDatabase"],
        "_706": ["CylindricalGearAbstractCutterDesign"],
        "_707": ["CylindricalGearFormGrindingWheel"],
        "_708": ["CylindricalGearGrindingWorm"],
        "_709": ["CylindricalGearHobDesign"],
        "_710": ["CylindricalGearPlungeShaver"],
        "_711": ["CylindricalGearPlungeShaverDatabase"],
        "_712": ["CylindricalGearRackDesign"],
        "_713": ["CylindricalGearRealCutterDesign"],
        "_714": ["CylindricalGearShaper"],
        "_715": ["CylindricalGearShaver"],
        "_716": ["CylindricalGearShaverDatabase"],
        "_717": ["CylindricalWormGrinderDatabase"],
        "_718": ["InvoluteCutterDesign"],
        "_719": ["MutableCommon"],
        "_720": ["MutableCurve"],
        "_721": ["MutableFillet"],
        "_722": ["RoughCutterCreationSettings"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CurveInLinkedList",
    "CustomisableEdgeProfile",
    "CylindricalFormedWheelGrinderDatabase",
    "CylindricalGearAbstractCutterDesign",
    "CylindricalGearFormGrindingWheel",
    "CylindricalGearGrindingWorm",
    "CylindricalGearHobDesign",
    "CylindricalGearPlungeShaver",
    "CylindricalGearPlungeShaverDatabase",
    "CylindricalGearRackDesign",
    "CylindricalGearRealCutterDesign",
    "CylindricalGearShaper",
    "CylindricalGearShaver",
    "CylindricalGearShaverDatabase",
    "CylindricalWormGrinderDatabase",
    "InvoluteCutterDesign",
    "MutableCommon",
    "MutableCurve",
    "MutableFillet",
    "RoughCutterCreationSettings",
)

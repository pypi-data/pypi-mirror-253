"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._583 import AGMACylindricalGearMaterial
    from ._584 import BevelGearAbstractMaterialDatabase
    from ._585 import BevelGearISOMaterial
    from ._586 import BevelGearISOMaterialDatabase
    from ._587 import BevelGearMaterial
    from ._588 import BevelGearMaterialDatabase
    from ._589 import CylindricalGearAGMAMaterialDatabase
    from ._590 import CylindricalGearISOMaterialDatabase
    from ._591 import CylindricalGearMaterial
    from ._592 import CylindricalGearMaterialDatabase
    from ._593 import CylindricalGearPlasticMaterialDatabase
    from ._594 import GearMaterial
    from ._595 import GearMaterialDatabase
    from ._596 import GearMaterialExpertSystemFactorSettings
    from ._597 import ISOCylindricalGearMaterial
    from ._598 import ISOTR1417912001CoefficientOfFrictionConstants
    from ._599 import ISOTR1417912001CoefficientOfFrictionConstantsDatabase
    from ._600 import KlingelnbergConicalGearMaterialDatabase
    from ._601 import KlingelnbergCycloPalloidConicalGearMaterial
    from ._602 import ManufactureRating
    from ._603 import PlasticCylindricalGearMaterial
    from ._604 import PlasticSNCurve
    from ._605 import RatingMethods
    from ._606 import RawMaterial
    from ._607 import RawMaterialDatabase
    from ._608 import SNCurveDefinition
else:
    import_structure = {
        "_583": ["AGMACylindricalGearMaterial"],
        "_584": ["BevelGearAbstractMaterialDatabase"],
        "_585": ["BevelGearISOMaterial"],
        "_586": ["BevelGearISOMaterialDatabase"],
        "_587": ["BevelGearMaterial"],
        "_588": ["BevelGearMaterialDatabase"],
        "_589": ["CylindricalGearAGMAMaterialDatabase"],
        "_590": ["CylindricalGearISOMaterialDatabase"],
        "_591": ["CylindricalGearMaterial"],
        "_592": ["CylindricalGearMaterialDatabase"],
        "_593": ["CylindricalGearPlasticMaterialDatabase"],
        "_594": ["GearMaterial"],
        "_595": ["GearMaterialDatabase"],
        "_596": ["GearMaterialExpertSystemFactorSettings"],
        "_597": ["ISOCylindricalGearMaterial"],
        "_598": ["ISOTR1417912001CoefficientOfFrictionConstants"],
        "_599": ["ISOTR1417912001CoefficientOfFrictionConstantsDatabase"],
        "_600": ["KlingelnbergConicalGearMaterialDatabase"],
        "_601": ["KlingelnbergCycloPalloidConicalGearMaterial"],
        "_602": ["ManufactureRating"],
        "_603": ["PlasticCylindricalGearMaterial"],
        "_604": ["PlasticSNCurve"],
        "_605": ["RatingMethods"],
        "_606": ["RawMaterial"],
        "_607": ["RawMaterialDatabase"],
        "_608": ["SNCurveDefinition"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMACylindricalGearMaterial",
    "BevelGearAbstractMaterialDatabase",
    "BevelGearISOMaterial",
    "BevelGearISOMaterialDatabase",
    "BevelGearMaterial",
    "BevelGearMaterialDatabase",
    "CylindricalGearAGMAMaterialDatabase",
    "CylindricalGearISOMaterialDatabase",
    "CylindricalGearMaterial",
    "CylindricalGearMaterialDatabase",
    "CylindricalGearPlasticMaterialDatabase",
    "GearMaterial",
    "GearMaterialDatabase",
    "GearMaterialExpertSystemFactorSettings",
    "ISOCylindricalGearMaterial",
    "ISOTR1417912001CoefficientOfFrictionConstants",
    "ISOTR1417912001CoefficientOfFrictionConstantsDatabase",
    "KlingelnbergConicalGearMaterialDatabase",
    "KlingelnbergCycloPalloidConicalGearMaterial",
    "ManufactureRating",
    "PlasticCylindricalGearMaterial",
    "PlasticSNCurve",
    "RatingMethods",
    "RawMaterial",
    "RawMaterialDatabase",
    "SNCurveDefinition",
)

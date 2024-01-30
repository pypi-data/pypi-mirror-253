"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2510 import ActiveCylindricalGearSetDesignSelection
    from ._2511 import ActiveGearSetDesignSelection
    from ._2512 import ActiveGearSetDesignSelectionGroup
    from ._2513 import AGMAGleasonConicalGear
    from ._2514 import AGMAGleasonConicalGearSet
    from ._2515 import BevelDifferentialGear
    from ._2516 import BevelDifferentialGearSet
    from ._2517 import BevelDifferentialPlanetGear
    from ._2518 import BevelDifferentialSunGear
    from ._2519 import BevelGear
    from ._2520 import BevelGearSet
    from ._2521 import ConceptGear
    from ._2522 import ConceptGearSet
    from ._2523 import ConicalGear
    from ._2524 import ConicalGearSet
    from ._2525 import CylindricalGear
    from ._2526 import CylindricalGearSet
    from ._2527 import CylindricalPlanetGear
    from ._2528 import FaceGear
    from ._2529 import FaceGearSet
    from ._2530 import Gear
    from ._2531 import GearOrientations
    from ._2532 import GearSet
    from ._2533 import GearSetConfiguration
    from ._2534 import HypoidGear
    from ._2535 import HypoidGearSet
    from ._2536 import KlingelnbergCycloPalloidConicalGear
    from ._2537 import KlingelnbergCycloPalloidConicalGearSet
    from ._2538 import KlingelnbergCycloPalloidHypoidGear
    from ._2539 import KlingelnbergCycloPalloidHypoidGearSet
    from ._2540 import KlingelnbergCycloPalloidSpiralBevelGear
    from ._2541 import KlingelnbergCycloPalloidSpiralBevelGearSet
    from ._2542 import PlanetaryGearSet
    from ._2543 import SpiralBevelGear
    from ._2544 import SpiralBevelGearSet
    from ._2545 import StraightBevelDiffGear
    from ._2546 import StraightBevelDiffGearSet
    from ._2547 import StraightBevelGear
    from ._2548 import StraightBevelGearSet
    from ._2549 import StraightBevelPlanetGear
    from ._2550 import StraightBevelSunGear
    from ._2551 import WormGear
    from ._2552 import WormGearSet
    from ._2553 import ZerolBevelGear
    from ._2554 import ZerolBevelGearSet
else:
    import_structure = {
        "_2510": ["ActiveCylindricalGearSetDesignSelection"],
        "_2511": ["ActiveGearSetDesignSelection"],
        "_2512": ["ActiveGearSetDesignSelectionGroup"],
        "_2513": ["AGMAGleasonConicalGear"],
        "_2514": ["AGMAGleasonConicalGearSet"],
        "_2515": ["BevelDifferentialGear"],
        "_2516": ["BevelDifferentialGearSet"],
        "_2517": ["BevelDifferentialPlanetGear"],
        "_2518": ["BevelDifferentialSunGear"],
        "_2519": ["BevelGear"],
        "_2520": ["BevelGearSet"],
        "_2521": ["ConceptGear"],
        "_2522": ["ConceptGearSet"],
        "_2523": ["ConicalGear"],
        "_2524": ["ConicalGearSet"],
        "_2525": ["CylindricalGear"],
        "_2526": ["CylindricalGearSet"],
        "_2527": ["CylindricalPlanetGear"],
        "_2528": ["FaceGear"],
        "_2529": ["FaceGearSet"],
        "_2530": ["Gear"],
        "_2531": ["GearOrientations"],
        "_2532": ["GearSet"],
        "_2533": ["GearSetConfiguration"],
        "_2534": ["HypoidGear"],
        "_2535": ["HypoidGearSet"],
        "_2536": ["KlingelnbergCycloPalloidConicalGear"],
        "_2537": ["KlingelnbergCycloPalloidConicalGearSet"],
        "_2538": ["KlingelnbergCycloPalloidHypoidGear"],
        "_2539": ["KlingelnbergCycloPalloidHypoidGearSet"],
        "_2540": ["KlingelnbergCycloPalloidSpiralBevelGear"],
        "_2541": ["KlingelnbergCycloPalloidSpiralBevelGearSet"],
        "_2542": ["PlanetaryGearSet"],
        "_2543": ["SpiralBevelGear"],
        "_2544": ["SpiralBevelGearSet"],
        "_2545": ["StraightBevelDiffGear"],
        "_2546": ["StraightBevelDiffGearSet"],
        "_2547": ["StraightBevelGear"],
        "_2548": ["StraightBevelGearSet"],
        "_2549": ["StraightBevelPlanetGear"],
        "_2550": ["StraightBevelSunGear"],
        "_2551": ["WormGear"],
        "_2552": ["WormGearSet"],
        "_2553": ["ZerolBevelGear"],
        "_2554": ["ZerolBevelGearSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveCylindricalGearSetDesignSelection",
    "ActiveGearSetDesignSelection",
    "ActiveGearSetDesignSelectionGroup",
    "AGMAGleasonConicalGear",
    "AGMAGleasonConicalGearSet",
    "BevelDifferentialGear",
    "BevelDifferentialGearSet",
    "BevelDifferentialPlanetGear",
    "BevelDifferentialSunGear",
    "BevelGear",
    "BevelGearSet",
    "ConceptGear",
    "ConceptGearSet",
    "ConicalGear",
    "ConicalGearSet",
    "CylindricalGear",
    "CylindricalGearSet",
    "CylindricalPlanetGear",
    "FaceGear",
    "FaceGearSet",
    "Gear",
    "GearOrientations",
    "GearSet",
    "GearSetConfiguration",
    "HypoidGear",
    "HypoidGearSet",
    "KlingelnbergCycloPalloidConicalGear",
    "KlingelnbergCycloPalloidConicalGearSet",
    "KlingelnbergCycloPalloidHypoidGear",
    "KlingelnbergCycloPalloidHypoidGearSet",
    "KlingelnbergCycloPalloidSpiralBevelGear",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
    "PlanetaryGearSet",
    "SpiralBevelGear",
    "SpiralBevelGearSet",
    "StraightBevelDiffGear",
    "StraightBevelDiffGearSet",
    "StraightBevelGear",
    "StraightBevelGearSet",
    "StraightBevelPlanetGear",
    "StraightBevelSunGear",
    "WormGear",
    "WormGearSet",
    "ZerolBevelGear",
    "ZerolBevelGearSet",
)

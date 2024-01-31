"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2299 import AGMAGleasonConicalGearMesh
    from ._2300 import AGMAGleasonConicalGearTeethSocket
    from ._2301 import BevelDifferentialGearMesh
    from ._2302 import BevelDifferentialGearTeethSocket
    from ._2303 import BevelGearMesh
    from ._2304 import BevelGearTeethSocket
    from ._2305 import ConceptGearMesh
    from ._2306 import ConceptGearTeethSocket
    from ._2307 import ConicalGearMesh
    from ._2308 import ConicalGearTeethSocket
    from ._2309 import CylindricalGearMesh
    from ._2310 import CylindricalGearTeethSocket
    from ._2311 import FaceGearMesh
    from ._2312 import FaceGearTeethSocket
    from ._2313 import GearMesh
    from ._2314 import GearTeethSocket
    from ._2315 import HypoidGearMesh
    from ._2316 import HypoidGearTeethSocket
    from ._2317 import KlingelnbergConicalGearTeethSocket
    from ._2318 import KlingelnbergCycloPalloidConicalGearMesh
    from ._2319 import KlingelnbergCycloPalloidHypoidGearMesh
    from ._2320 import KlingelnbergCycloPalloidSpiralBevelGearMesh
    from ._2321 import KlingelnbergHypoidGearTeethSocket
    from ._2322 import KlingelnbergSpiralBevelGearTeethSocket
    from ._2323 import SpiralBevelGearMesh
    from ._2324 import SpiralBevelGearTeethSocket
    from ._2325 import StraightBevelDiffGearMesh
    from ._2326 import StraightBevelDiffGearTeethSocket
    from ._2327 import StraightBevelGearMesh
    from ._2328 import StraightBevelGearTeethSocket
    from ._2329 import WormGearMesh
    from ._2330 import WormGearTeethSocket
    from ._2331 import ZerolBevelGearMesh
    from ._2332 import ZerolBevelGearTeethSocket
else:
    import_structure = {
        "_2299": ["AGMAGleasonConicalGearMesh"],
        "_2300": ["AGMAGleasonConicalGearTeethSocket"],
        "_2301": ["BevelDifferentialGearMesh"],
        "_2302": ["BevelDifferentialGearTeethSocket"],
        "_2303": ["BevelGearMesh"],
        "_2304": ["BevelGearTeethSocket"],
        "_2305": ["ConceptGearMesh"],
        "_2306": ["ConceptGearTeethSocket"],
        "_2307": ["ConicalGearMesh"],
        "_2308": ["ConicalGearTeethSocket"],
        "_2309": ["CylindricalGearMesh"],
        "_2310": ["CylindricalGearTeethSocket"],
        "_2311": ["FaceGearMesh"],
        "_2312": ["FaceGearTeethSocket"],
        "_2313": ["GearMesh"],
        "_2314": ["GearTeethSocket"],
        "_2315": ["HypoidGearMesh"],
        "_2316": ["HypoidGearTeethSocket"],
        "_2317": ["KlingelnbergConicalGearTeethSocket"],
        "_2318": ["KlingelnbergCycloPalloidConicalGearMesh"],
        "_2319": ["KlingelnbergCycloPalloidHypoidGearMesh"],
        "_2320": ["KlingelnbergCycloPalloidSpiralBevelGearMesh"],
        "_2321": ["KlingelnbergHypoidGearTeethSocket"],
        "_2322": ["KlingelnbergSpiralBevelGearTeethSocket"],
        "_2323": ["SpiralBevelGearMesh"],
        "_2324": ["SpiralBevelGearTeethSocket"],
        "_2325": ["StraightBevelDiffGearMesh"],
        "_2326": ["StraightBevelDiffGearTeethSocket"],
        "_2327": ["StraightBevelGearMesh"],
        "_2328": ["StraightBevelGearTeethSocket"],
        "_2329": ["WormGearMesh"],
        "_2330": ["WormGearTeethSocket"],
        "_2331": ["ZerolBevelGearMesh"],
        "_2332": ["ZerolBevelGearTeethSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AGMAGleasonConicalGearMesh",
    "AGMAGleasonConicalGearTeethSocket",
    "BevelDifferentialGearMesh",
    "BevelDifferentialGearTeethSocket",
    "BevelGearMesh",
    "BevelGearTeethSocket",
    "ConceptGearMesh",
    "ConceptGearTeethSocket",
    "ConicalGearMesh",
    "ConicalGearTeethSocket",
    "CylindricalGearMesh",
    "CylindricalGearTeethSocket",
    "FaceGearMesh",
    "FaceGearTeethSocket",
    "GearMesh",
    "GearTeethSocket",
    "HypoidGearMesh",
    "HypoidGearTeethSocket",
    "KlingelnbergConicalGearTeethSocket",
    "KlingelnbergCycloPalloidConicalGearMesh",
    "KlingelnbergCycloPalloidHypoidGearMesh",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
    "KlingelnbergHypoidGearTeethSocket",
    "KlingelnbergSpiralBevelGearTeethSocket",
    "SpiralBevelGearMesh",
    "SpiralBevelGearTeethSocket",
    "StraightBevelDiffGearMesh",
    "StraightBevelDiffGearTeethSocket",
    "StraightBevelGearMesh",
    "StraightBevelGearTeethSocket",
    "WormGearMesh",
    "WormGearTeethSocket",
    "ZerolBevelGearMesh",
    "ZerolBevelGearTeethSocket",
)

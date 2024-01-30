"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._378 import BevelVirtualCylindricalGearISO10300MethodB2
    from ._379 import BevelVirtualCylindricalGearSetISO10300MethodB1
    from ._380 import BevelVirtualCylindricalGearSetISO10300MethodB2
    from ._381 import HypoidVirtualCylindricalGearISO10300MethodB2
    from ._382 import HypoidVirtualCylindricalGearSetISO10300MethodB1
    from ._383 import HypoidVirtualCylindricalGearSetISO10300MethodB2
    from ._384 import KlingelnbergHypoidVirtualCylindricalGear
    from ._385 import KlingelnbergSpiralBevelVirtualCylindricalGear
    from ._386 import KlingelnbergVirtualCylindricalGear
    from ._387 import KlingelnbergVirtualCylindricalGearSet
    from ._388 import VirtualCylindricalGear
    from ._389 import VirtualCylindricalGearBasic
    from ._390 import VirtualCylindricalGearISO10300MethodB1
    from ._391 import VirtualCylindricalGearISO10300MethodB2
    from ._392 import VirtualCylindricalGearSet
    from ._393 import VirtualCylindricalGearSetISO10300MethodB1
    from ._394 import VirtualCylindricalGearSetISO10300MethodB2
else:
    import_structure = {
        "_378": ["BevelVirtualCylindricalGearISO10300MethodB2"],
        "_379": ["BevelVirtualCylindricalGearSetISO10300MethodB1"],
        "_380": ["BevelVirtualCylindricalGearSetISO10300MethodB2"],
        "_381": ["HypoidVirtualCylindricalGearISO10300MethodB2"],
        "_382": ["HypoidVirtualCylindricalGearSetISO10300MethodB1"],
        "_383": ["HypoidVirtualCylindricalGearSetISO10300MethodB2"],
        "_384": ["KlingelnbergHypoidVirtualCylindricalGear"],
        "_385": ["KlingelnbergSpiralBevelVirtualCylindricalGear"],
        "_386": ["KlingelnbergVirtualCylindricalGear"],
        "_387": ["KlingelnbergVirtualCylindricalGearSet"],
        "_388": ["VirtualCylindricalGear"],
        "_389": ["VirtualCylindricalGearBasic"],
        "_390": ["VirtualCylindricalGearISO10300MethodB1"],
        "_391": ["VirtualCylindricalGearISO10300MethodB2"],
        "_392": ["VirtualCylindricalGearSet"],
        "_393": ["VirtualCylindricalGearSetISO10300MethodB1"],
        "_394": ["VirtualCylindricalGearSetISO10300MethodB2"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelVirtualCylindricalGearISO10300MethodB2",
    "BevelVirtualCylindricalGearSetISO10300MethodB1",
    "BevelVirtualCylindricalGearSetISO10300MethodB2",
    "HypoidVirtualCylindricalGearISO10300MethodB2",
    "HypoidVirtualCylindricalGearSetISO10300MethodB1",
    "HypoidVirtualCylindricalGearSetISO10300MethodB2",
    "KlingelnbergHypoidVirtualCylindricalGear",
    "KlingelnbergSpiralBevelVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGear",
    "KlingelnbergVirtualCylindricalGearSet",
    "VirtualCylindricalGear",
    "VirtualCylindricalGearBasic",
    "VirtualCylindricalGearISO10300MethodB1",
    "VirtualCylindricalGearISO10300MethodB2",
    "VirtualCylindricalGearSet",
    "VirtualCylindricalGearSetISO10300MethodB1",
    "VirtualCylindricalGearSetISO10300MethodB2",
)

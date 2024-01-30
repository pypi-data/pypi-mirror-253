"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._414 import KlingelnbergConicalMeshSingleFlankRating
    from ._415 import KlingelnbergConicalRateableMesh
    from ._416 import KlingelnbergCycloPalloidConicalGearSingleFlankRating
    from ._417 import KlingelnbergCycloPalloidHypoidGearSingleFlankRating
    from ._418 import KlingelnbergCycloPalloidHypoidMeshSingleFlankRating
    from ._419 import KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating
else:
    import_structure = {
        "_414": ["KlingelnbergConicalMeshSingleFlankRating"],
        "_415": ["KlingelnbergConicalRateableMesh"],
        "_416": ["KlingelnbergCycloPalloidConicalGearSingleFlankRating"],
        "_417": ["KlingelnbergCycloPalloidHypoidGearSingleFlankRating"],
        "_418": ["KlingelnbergCycloPalloidHypoidMeshSingleFlankRating"],
        "_419": ["KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "KlingelnbergConicalMeshSingleFlankRating",
    "KlingelnbergConicalRateableMesh",
    "KlingelnbergCycloPalloidConicalGearSingleFlankRating",
    "KlingelnbergCycloPalloidHypoidGearSingleFlankRating",
    "KlingelnbergCycloPalloidHypoidMeshSingleFlankRating",
    "KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating",
)

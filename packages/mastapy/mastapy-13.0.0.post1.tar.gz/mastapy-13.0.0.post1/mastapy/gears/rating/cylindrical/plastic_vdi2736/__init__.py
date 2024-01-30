"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._490 import MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
    from ._491 import PlasticGearVDI2736AbstractGearSingleFlankRating
    from ._492 import PlasticGearVDI2736AbstractMeshSingleFlankRating
    from ._493 import PlasticGearVDI2736AbstractRateableMesh
    from ._494 import PlasticPlasticVDI2736MeshSingleFlankRating
    from ._495 import PlasticSNCurveForTheSpecifiedOperatingConditions
    from ._496 import (
        PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh,
    )
    from ._497 import PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh
    from ._498 import VDI2736MetalPlasticRateableMesh
    from ._499 import VDI2736PlasticMetalRateableMesh
    from ._500 import VDI2736PlasticPlasticRateableMesh
else:
    import_structure = {
        "_490": ["MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating"],
        "_491": ["PlasticGearVDI2736AbstractGearSingleFlankRating"],
        "_492": ["PlasticGearVDI2736AbstractMeshSingleFlankRating"],
        "_493": ["PlasticGearVDI2736AbstractRateableMesh"],
        "_494": ["PlasticPlasticVDI2736MeshSingleFlankRating"],
        "_495": ["PlasticSNCurveForTheSpecifiedOperatingConditions"],
        "_496": [
            "PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh"
        ],
        "_497": ["PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh"],
        "_498": ["VDI2736MetalPlasticRateableMesh"],
        "_499": ["VDI2736PlasticMetalRateableMesh"],
        "_500": ["VDI2736PlasticPlasticRateableMesh"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating",
    "PlasticGearVDI2736AbstractGearSingleFlankRating",
    "PlasticGearVDI2736AbstractMeshSingleFlankRating",
    "PlasticGearVDI2736AbstractRateableMesh",
    "PlasticPlasticVDI2736MeshSingleFlankRating",
    "PlasticSNCurveForTheSpecifiedOperatingConditions",
    "PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh",
    "PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh",
    "VDI2736MetalPlasticRateableMesh",
    "VDI2736PlasticMetalRateableMesh",
    "VDI2736PlasticPlasticRateableMesh",
)

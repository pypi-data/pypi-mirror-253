"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._508 import CylindricalGearToothFatigueFractureResults
    from ._509 import CylindricalGearToothFatigueFractureResultsN1457
    from ._510 import HelicalGearMicroGeometryOption
    from ._511 import ISO63361996GearSingleFlankRating
    from ._512 import ISO63361996MeshSingleFlankRating
    from ._513 import ISO63362006GearSingleFlankRating
    from ._514 import ISO63362006MeshSingleFlankRating
    from ._515 import ISO63362019GearSingleFlankRating
    from ._516 import ISO63362019MeshSingleFlankRating
    from ._517 import ISO6336AbstractGearSingleFlankRating
    from ._518 import ISO6336AbstractMeshSingleFlankRating
    from ._519 import ISO6336AbstractMetalGearSingleFlankRating
    from ._520 import ISO6336AbstractMetalMeshSingleFlankRating
    from ._521 import ISO6336MeanStressInfluenceFactor
    from ._522 import ISO6336MetalRateableMesh
    from ._523 import ISO6336RateableMesh
    from ._524 import ToothFlankFractureAnalysisContactPoint
    from ._525 import ToothFlankFractureAnalysisContactPointCommon
    from ._526 import ToothFlankFractureAnalysisContactPointMethodA
    from ._527 import ToothFlankFractureAnalysisContactPointN1457
    from ._528 import ToothFlankFractureAnalysisPoint
    from ._529 import ToothFlankFractureAnalysisPointN1457
    from ._530 import ToothFlankFractureAnalysisRowN1457
    from ._531 import ToothFlankFractureStressStepAtAnalysisPointN1457
else:
    import_structure = {
        "_508": ["CylindricalGearToothFatigueFractureResults"],
        "_509": ["CylindricalGearToothFatigueFractureResultsN1457"],
        "_510": ["HelicalGearMicroGeometryOption"],
        "_511": ["ISO63361996GearSingleFlankRating"],
        "_512": ["ISO63361996MeshSingleFlankRating"],
        "_513": ["ISO63362006GearSingleFlankRating"],
        "_514": ["ISO63362006MeshSingleFlankRating"],
        "_515": ["ISO63362019GearSingleFlankRating"],
        "_516": ["ISO63362019MeshSingleFlankRating"],
        "_517": ["ISO6336AbstractGearSingleFlankRating"],
        "_518": ["ISO6336AbstractMeshSingleFlankRating"],
        "_519": ["ISO6336AbstractMetalGearSingleFlankRating"],
        "_520": ["ISO6336AbstractMetalMeshSingleFlankRating"],
        "_521": ["ISO6336MeanStressInfluenceFactor"],
        "_522": ["ISO6336MetalRateableMesh"],
        "_523": ["ISO6336RateableMesh"],
        "_524": ["ToothFlankFractureAnalysisContactPoint"],
        "_525": ["ToothFlankFractureAnalysisContactPointCommon"],
        "_526": ["ToothFlankFractureAnalysisContactPointMethodA"],
        "_527": ["ToothFlankFractureAnalysisContactPointN1457"],
        "_528": ["ToothFlankFractureAnalysisPoint"],
        "_529": ["ToothFlankFractureAnalysisPointN1457"],
        "_530": ["ToothFlankFractureAnalysisRowN1457"],
        "_531": ["ToothFlankFractureStressStepAtAnalysisPointN1457"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearToothFatigueFractureResults",
    "CylindricalGearToothFatigueFractureResultsN1457",
    "HelicalGearMicroGeometryOption",
    "ISO63361996GearSingleFlankRating",
    "ISO63361996MeshSingleFlankRating",
    "ISO63362006GearSingleFlankRating",
    "ISO63362006MeshSingleFlankRating",
    "ISO63362019GearSingleFlankRating",
    "ISO63362019MeshSingleFlankRating",
    "ISO6336AbstractGearSingleFlankRating",
    "ISO6336AbstractMeshSingleFlankRating",
    "ISO6336AbstractMetalGearSingleFlankRating",
    "ISO6336AbstractMetalMeshSingleFlankRating",
    "ISO6336MeanStressInfluenceFactor",
    "ISO6336MetalRateableMesh",
    "ISO6336RateableMesh",
    "ToothFlankFractureAnalysisContactPoint",
    "ToothFlankFractureAnalysisContactPointCommon",
    "ToothFlankFractureAnalysisContactPointMethodA",
    "ToothFlankFractureAnalysisContactPointN1457",
    "ToothFlankFractureAnalysisPoint",
    "ToothFlankFractureAnalysisPointN1457",
    "ToothFlankFractureAnalysisRowN1457",
    "ToothFlankFractureStressStepAtAnalysisPointN1457",
)

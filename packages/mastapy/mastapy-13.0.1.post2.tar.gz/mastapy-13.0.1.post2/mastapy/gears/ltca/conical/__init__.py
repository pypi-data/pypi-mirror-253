"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._863 import ConicalGearBendingStiffness
    from ._864 import ConicalGearBendingStiffnessNode
    from ._865 import ConicalGearContactStiffness
    from ._866 import ConicalGearContactStiffnessNode
    from ._867 import ConicalGearLoadDistributionAnalysis
    from ._868 import ConicalGearSetLoadDistributionAnalysis
    from ._869 import ConicalMeshedGearLoadDistributionAnalysis
    from ._870 import ConicalMeshLoadDistributionAnalysis
    from ._871 import ConicalMeshLoadDistributionAtRotation
    from ._872 import ConicalMeshLoadedContactLine
else:
    import_structure = {
        "_863": ["ConicalGearBendingStiffness"],
        "_864": ["ConicalGearBendingStiffnessNode"],
        "_865": ["ConicalGearContactStiffness"],
        "_866": ["ConicalGearContactStiffnessNode"],
        "_867": ["ConicalGearLoadDistributionAnalysis"],
        "_868": ["ConicalGearSetLoadDistributionAnalysis"],
        "_869": ["ConicalMeshedGearLoadDistributionAnalysis"],
        "_870": ["ConicalMeshLoadDistributionAnalysis"],
        "_871": ["ConicalMeshLoadDistributionAtRotation"],
        "_872": ["ConicalMeshLoadedContactLine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearBendingStiffness",
    "ConicalGearBendingStiffnessNode",
    "ConicalGearContactStiffness",
    "ConicalGearContactStiffnessNode",
    "ConicalGearLoadDistributionAnalysis",
    "ConicalGearSetLoadDistributionAnalysis",
    "ConicalMeshedGearLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAnalysis",
    "ConicalMeshLoadDistributionAtRotation",
    "ConicalMeshLoadedContactLine",
)

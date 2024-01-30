"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._851 import CylindricalGearBendingStiffness
    from ._852 import CylindricalGearBendingStiffnessNode
    from ._853 import CylindricalGearContactStiffness
    from ._854 import CylindricalGearContactStiffnessNode
    from ._855 import CylindricalGearFESettings
    from ._856 import CylindricalGearLoadDistributionAnalysis
    from ._857 import CylindricalGearMeshLoadDistributionAnalysis
    from ._858 import CylindricalGearMeshLoadedContactLine
    from ._859 import CylindricalGearMeshLoadedContactPoint
    from ._860 import CylindricalGearSetLoadDistributionAnalysis
    from ._861 import CylindricalMeshLoadDistributionAtRotation
    from ._862 import FaceGearSetLoadDistributionAnalysis
else:
    import_structure = {
        "_851": ["CylindricalGearBendingStiffness"],
        "_852": ["CylindricalGearBendingStiffnessNode"],
        "_853": ["CylindricalGearContactStiffness"],
        "_854": ["CylindricalGearContactStiffnessNode"],
        "_855": ["CylindricalGearFESettings"],
        "_856": ["CylindricalGearLoadDistributionAnalysis"],
        "_857": ["CylindricalGearMeshLoadDistributionAnalysis"],
        "_858": ["CylindricalGearMeshLoadedContactLine"],
        "_859": ["CylindricalGearMeshLoadedContactPoint"],
        "_860": ["CylindricalGearSetLoadDistributionAnalysis"],
        "_861": ["CylindricalMeshLoadDistributionAtRotation"],
        "_862": ["FaceGearSetLoadDistributionAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBendingStiffness",
    "CylindricalGearBendingStiffnessNode",
    "CylindricalGearContactStiffness",
    "CylindricalGearContactStiffnessNode",
    "CylindricalGearFESettings",
    "CylindricalGearLoadDistributionAnalysis",
    "CylindricalGearMeshLoadDistributionAnalysis",
    "CylindricalGearMeshLoadedContactLine",
    "CylindricalGearMeshLoadedContactPoint",
    "CylindricalGearSetLoadDistributionAnalysis",
    "CylindricalMeshLoadDistributionAtRotation",
    "FaceGearSetLoadDistributionAnalysis",
)

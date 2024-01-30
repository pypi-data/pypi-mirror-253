"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._825 import ConicalGearFilletStressResults
    from ._826 import ConicalGearRootFilletStressResults
    from ._827 import ContactResultType
    from ._828 import CylindricalGearFilletNodeStressResults
    from ._829 import CylindricalGearFilletNodeStressResultsColumn
    from ._830 import CylindricalGearFilletNodeStressResultsRow
    from ._831 import CylindricalGearRootFilletStressResults
    from ._832 import CylindricalMeshedGearLoadDistributionAnalysis
    from ._833 import GearBendingStiffness
    from ._834 import GearBendingStiffnessNode
    from ._835 import GearContactStiffness
    from ._836 import GearContactStiffnessNode
    from ._837 import GearFilletNodeStressResults
    from ._838 import GearFilletNodeStressResultsColumn
    from ._839 import GearFilletNodeStressResultsRow
    from ._840 import GearLoadDistributionAnalysis
    from ._841 import GearMeshLoadDistributionAnalysis
    from ._842 import GearMeshLoadDistributionAtRotation
    from ._843 import GearMeshLoadedContactLine
    from ._844 import GearMeshLoadedContactPoint
    from ._845 import GearRootFilletStressResults
    from ._846 import GearSetLoadDistributionAnalysis
    from ._847 import GearStiffness
    from ._848 import GearStiffnessNode
    from ._849 import MeshedGearLoadDistributionAnalysisAtRotation
    from ._850 import UseAdvancedLTCAOptions
else:
    import_structure = {
        "_825": ["ConicalGearFilletStressResults"],
        "_826": ["ConicalGearRootFilletStressResults"],
        "_827": ["ContactResultType"],
        "_828": ["CylindricalGearFilletNodeStressResults"],
        "_829": ["CylindricalGearFilletNodeStressResultsColumn"],
        "_830": ["CylindricalGearFilletNodeStressResultsRow"],
        "_831": ["CylindricalGearRootFilletStressResults"],
        "_832": ["CylindricalMeshedGearLoadDistributionAnalysis"],
        "_833": ["GearBendingStiffness"],
        "_834": ["GearBendingStiffnessNode"],
        "_835": ["GearContactStiffness"],
        "_836": ["GearContactStiffnessNode"],
        "_837": ["GearFilletNodeStressResults"],
        "_838": ["GearFilletNodeStressResultsColumn"],
        "_839": ["GearFilletNodeStressResultsRow"],
        "_840": ["GearLoadDistributionAnalysis"],
        "_841": ["GearMeshLoadDistributionAnalysis"],
        "_842": ["GearMeshLoadDistributionAtRotation"],
        "_843": ["GearMeshLoadedContactLine"],
        "_844": ["GearMeshLoadedContactPoint"],
        "_845": ["GearRootFilletStressResults"],
        "_846": ["GearSetLoadDistributionAnalysis"],
        "_847": ["GearStiffness"],
        "_848": ["GearStiffnessNode"],
        "_849": ["MeshedGearLoadDistributionAnalysisAtRotation"],
        "_850": ["UseAdvancedLTCAOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConicalGearFilletStressResults",
    "ConicalGearRootFilletStressResults",
    "ContactResultType",
    "CylindricalGearFilletNodeStressResults",
    "CylindricalGearFilletNodeStressResultsColumn",
    "CylindricalGearFilletNodeStressResultsRow",
    "CylindricalGearRootFilletStressResults",
    "CylindricalMeshedGearLoadDistributionAnalysis",
    "GearBendingStiffness",
    "GearBendingStiffnessNode",
    "GearContactStiffness",
    "GearContactStiffnessNode",
    "GearFilletNodeStressResults",
    "GearFilletNodeStressResultsColumn",
    "GearFilletNodeStressResultsRow",
    "GearLoadDistributionAnalysis",
    "GearMeshLoadDistributionAnalysis",
    "GearMeshLoadDistributionAtRotation",
    "GearMeshLoadedContactLine",
    "GearMeshLoadedContactPoint",
    "GearRootFilletStressResults",
    "GearSetLoadDistributionAnalysis",
    "GearStiffness",
    "GearStiffnessNode",
    "MeshedGearLoadDistributionAnalysisAtRotation",
    "UseAdvancedLTCAOptions",
)

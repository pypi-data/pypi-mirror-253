"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._894 import CylindricalGearMeshTIFFAnalysis
    from ._895 import CylindricalGearMeshTIFFAnalysisDutyCycle
    from ._896 import CylindricalGearSetTIFFAnalysis
    from ._897 import CylindricalGearSetTIFFAnalysisDutyCycle
    from ._898 import CylindricalGearTIFFAnalysis
    from ._899 import CylindricalGearTIFFAnalysisDutyCycle
    from ._900 import CylindricalGearTwoDimensionalFEAnalysis
    from ._901 import FindleyCriticalPlaneAnalysis
else:
    import_structure = {
        "_894": ["CylindricalGearMeshTIFFAnalysis"],
        "_895": ["CylindricalGearMeshTIFFAnalysisDutyCycle"],
        "_896": ["CylindricalGearSetTIFFAnalysis"],
        "_897": ["CylindricalGearSetTIFFAnalysisDutyCycle"],
        "_898": ["CylindricalGearTIFFAnalysis"],
        "_899": ["CylindricalGearTIFFAnalysisDutyCycle"],
        "_900": ["CylindricalGearTwoDimensionalFEAnalysis"],
        "_901": ["FindleyCriticalPlaneAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshTIFFAnalysis",
    "CylindricalGearMeshTIFFAnalysisDutyCycle",
    "CylindricalGearSetTIFFAnalysis",
    "CylindricalGearSetTIFFAnalysisDutyCycle",
    "CylindricalGearTIFFAnalysis",
    "CylindricalGearTIFFAnalysisDutyCycle",
    "CylindricalGearTwoDimensionalFEAnalysis",
    "FindleyCriticalPlaneAnalysis",
)

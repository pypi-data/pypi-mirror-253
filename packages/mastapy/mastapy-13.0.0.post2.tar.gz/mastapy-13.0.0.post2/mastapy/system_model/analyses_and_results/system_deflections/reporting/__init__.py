"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2842 import CylindricalGearMeshMisalignmentValue
    from ._2843 import FlexibleGearChart
    from ._2844 import GearInMeshDeflectionResults
    from ._2845 import MeshDeflectionResults
    from ._2846 import PlanetCarrierWindup
    from ._2847 import PlanetPinWindup
    from ._2848 import RigidlyConnectedComponentGroupSystemDeflection
    from ._2849 import ShaftSystemDeflectionSectionsReport
    from ._2850 import SplineFlankContactReporting
else:
    import_structure = {
        "_2842": ["CylindricalGearMeshMisalignmentValue"],
        "_2843": ["FlexibleGearChart"],
        "_2844": ["GearInMeshDeflectionResults"],
        "_2845": ["MeshDeflectionResults"],
        "_2846": ["PlanetCarrierWindup"],
        "_2847": ["PlanetPinWindup"],
        "_2848": ["RigidlyConnectedComponentGroupSystemDeflection"],
        "_2849": ["ShaftSystemDeflectionSectionsReport"],
        "_2850": ["SplineFlankContactReporting"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearMeshMisalignmentValue",
    "FlexibleGearChart",
    "GearInMeshDeflectionResults",
    "MeshDeflectionResults",
    "PlanetCarrierWindup",
    "PlanetPinWindup",
    "RigidlyConnectedComponentGroupSystemDeflection",
    "ShaftSystemDeflectionSectionsReport",
    "SplineFlankContactReporting",
)

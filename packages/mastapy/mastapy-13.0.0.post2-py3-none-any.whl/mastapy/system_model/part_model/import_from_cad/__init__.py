"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2493 import AbstractShaftFromCAD
    from ._2494 import ClutchFromCAD
    from ._2495 import ComponentFromCAD
    from ._2496 import ConceptBearingFromCAD
    from ._2497 import ConnectorFromCAD
    from ._2498 import CylindricalGearFromCAD
    from ._2499 import CylindricalGearInPlanetarySetFromCAD
    from ._2500 import CylindricalPlanetGearFromCAD
    from ._2501 import CylindricalRingGearFromCAD
    from ._2502 import CylindricalSunGearFromCAD
    from ._2503 import HousedOrMounted
    from ._2504 import MountableComponentFromCAD
    from ._2505 import PlanetShaftFromCAD
    from ._2506 import PulleyFromCAD
    from ._2507 import RigidConnectorFromCAD
    from ._2508 import RollingBearingFromCAD
    from ._2509 import ShaftFromCAD
else:
    import_structure = {
        "_2493": ["AbstractShaftFromCAD"],
        "_2494": ["ClutchFromCAD"],
        "_2495": ["ComponentFromCAD"],
        "_2496": ["ConceptBearingFromCAD"],
        "_2497": ["ConnectorFromCAD"],
        "_2498": ["CylindricalGearFromCAD"],
        "_2499": ["CylindricalGearInPlanetarySetFromCAD"],
        "_2500": ["CylindricalPlanetGearFromCAD"],
        "_2501": ["CylindricalRingGearFromCAD"],
        "_2502": ["CylindricalSunGearFromCAD"],
        "_2503": ["HousedOrMounted"],
        "_2504": ["MountableComponentFromCAD"],
        "_2505": ["PlanetShaftFromCAD"],
        "_2506": ["PulleyFromCAD"],
        "_2507": ["RigidConnectorFromCAD"],
        "_2508": ["RollingBearingFromCAD"],
        "_2509": ["ShaftFromCAD"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftFromCAD",
    "ClutchFromCAD",
    "ComponentFromCAD",
    "ConceptBearingFromCAD",
    "ConnectorFromCAD",
    "CylindricalGearFromCAD",
    "CylindricalGearInPlanetarySetFromCAD",
    "CylindricalPlanetGearFromCAD",
    "CylindricalRingGearFromCAD",
    "CylindricalSunGearFromCAD",
    "HousedOrMounted",
    "MountableComponentFromCAD",
    "PlanetShaftFromCAD",
    "PulleyFromCAD",
    "RigidConnectorFromCAD",
    "RollingBearingFromCAD",
    "ShaftFromCAD",
)

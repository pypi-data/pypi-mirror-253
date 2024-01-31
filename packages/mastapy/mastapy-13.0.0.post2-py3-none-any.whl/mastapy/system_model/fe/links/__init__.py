"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2418 import FELink
    from ._2419 import ElectricMachineStatorFELink
    from ._2420 import FELinkWithSelection
    from ._2421 import GearMeshFELink
    from ._2422 import GearWithDuplicatedMeshesFELink
    from ._2423 import MultiAngleConnectionFELink
    from ._2424 import MultiNodeConnectorFELink
    from ._2425 import MultiNodeFELink
    from ._2426 import PlanetaryConnectorMultiNodeFELink
    from ._2427 import PlanetBasedFELink
    from ._2428 import PlanetCarrierFELink
    from ._2429 import PointLoadFELink
    from ._2430 import RollingRingConnectionFELink
    from ._2431 import ShaftHubConnectionFELink
    from ._2432 import SingleNodeFELink
else:
    import_structure = {
        "_2418": ["FELink"],
        "_2419": ["ElectricMachineStatorFELink"],
        "_2420": ["FELinkWithSelection"],
        "_2421": ["GearMeshFELink"],
        "_2422": ["GearWithDuplicatedMeshesFELink"],
        "_2423": ["MultiAngleConnectionFELink"],
        "_2424": ["MultiNodeConnectorFELink"],
        "_2425": ["MultiNodeFELink"],
        "_2426": ["PlanetaryConnectorMultiNodeFELink"],
        "_2427": ["PlanetBasedFELink"],
        "_2428": ["PlanetCarrierFELink"],
        "_2429": ["PointLoadFELink"],
        "_2430": ["RollingRingConnectionFELink"],
        "_2431": ["ShaftHubConnectionFELink"],
        "_2432": ["SingleNodeFELink"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FELink",
    "ElectricMachineStatorFELink",
    "FELinkWithSelection",
    "GearMeshFELink",
    "GearWithDuplicatedMeshesFELink",
    "MultiAngleConnectionFELink",
    "MultiNodeConnectorFELink",
    "MultiNodeFELink",
    "PlanetaryConnectorMultiNodeFELink",
    "PlanetBasedFELink",
    "PlanetCarrierFELink",
    "PointLoadFELink",
    "RollingRingConnectionFELink",
    "ShaftHubConnectionFELink",
    "SingleNodeFELink",
)

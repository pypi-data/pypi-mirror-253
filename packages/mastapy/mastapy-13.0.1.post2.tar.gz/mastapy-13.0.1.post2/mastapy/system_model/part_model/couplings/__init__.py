"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2576 import BeltDrive
    from ._2577 import BeltDriveType
    from ._2578 import Clutch
    from ._2579 import ClutchHalf
    from ._2580 import ClutchType
    from ._2581 import ConceptCoupling
    from ._2582 import ConceptCouplingHalf
    from ._2583 import Coupling
    from ._2584 import CouplingHalf
    from ._2585 import CrowningSpecification
    from ._2586 import CVT
    from ._2587 import CVTPulley
    from ._2588 import PartToPartShearCoupling
    from ._2589 import PartToPartShearCouplingHalf
    from ._2590 import Pulley
    from ._2591 import RigidConnectorStiffnessType
    from ._2592 import RigidConnectorTiltStiffnessTypes
    from ._2593 import RigidConnectorToothLocation
    from ._2594 import RigidConnectorToothSpacingType
    from ._2595 import RigidConnectorTypes
    from ._2596 import RollingRing
    from ._2597 import RollingRingAssembly
    from ._2598 import ShaftHubConnection
    from ._2599 import SplineLeadRelief
    from ._2600 import SpringDamper
    from ._2601 import SpringDamperHalf
    from ._2602 import Synchroniser
    from ._2603 import SynchroniserCone
    from ._2604 import SynchroniserHalf
    from ._2605 import SynchroniserPart
    from ._2606 import SynchroniserSleeve
    from ._2607 import TorqueConverter
    from ._2608 import TorqueConverterPump
    from ._2609 import TorqueConverterSpeedRatio
    from ._2610 import TorqueConverterTurbine
else:
    import_structure = {
        "_2576": ["BeltDrive"],
        "_2577": ["BeltDriveType"],
        "_2578": ["Clutch"],
        "_2579": ["ClutchHalf"],
        "_2580": ["ClutchType"],
        "_2581": ["ConceptCoupling"],
        "_2582": ["ConceptCouplingHalf"],
        "_2583": ["Coupling"],
        "_2584": ["CouplingHalf"],
        "_2585": ["CrowningSpecification"],
        "_2586": ["CVT"],
        "_2587": ["CVTPulley"],
        "_2588": ["PartToPartShearCoupling"],
        "_2589": ["PartToPartShearCouplingHalf"],
        "_2590": ["Pulley"],
        "_2591": ["RigidConnectorStiffnessType"],
        "_2592": ["RigidConnectorTiltStiffnessTypes"],
        "_2593": ["RigidConnectorToothLocation"],
        "_2594": ["RigidConnectorToothSpacingType"],
        "_2595": ["RigidConnectorTypes"],
        "_2596": ["RollingRing"],
        "_2597": ["RollingRingAssembly"],
        "_2598": ["ShaftHubConnection"],
        "_2599": ["SplineLeadRelief"],
        "_2600": ["SpringDamper"],
        "_2601": ["SpringDamperHalf"],
        "_2602": ["Synchroniser"],
        "_2603": ["SynchroniserCone"],
        "_2604": ["SynchroniserHalf"],
        "_2605": ["SynchroniserPart"],
        "_2606": ["SynchroniserSleeve"],
        "_2607": ["TorqueConverter"],
        "_2608": ["TorqueConverterPump"],
        "_2609": ["TorqueConverterSpeedRatio"],
        "_2610": ["TorqueConverterTurbine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BeltDrive",
    "BeltDriveType",
    "Clutch",
    "ClutchHalf",
    "ClutchType",
    "ConceptCoupling",
    "ConceptCouplingHalf",
    "Coupling",
    "CouplingHalf",
    "CrowningSpecification",
    "CVT",
    "CVTPulley",
    "PartToPartShearCoupling",
    "PartToPartShearCouplingHalf",
    "Pulley",
    "RigidConnectorStiffnessType",
    "RigidConnectorTiltStiffnessTypes",
    "RigidConnectorToothLocation",
    "RigidConnectorToothSpacingType",
    "RigidConnectorTypes",
    "RollingRing",
    "RollingRingAssembly",
    "ShaftHubConnection",
    "SplineLeadRelief",
    "SpringDamper",
    "SpringDamperHalf",
    "Synchroniser",
    "SynchroniserCone",
    "SynchroniserHalf",
    "SynchroniserPart",
    "SynchroniserSleeve",
    "TorqueConverter",
    "TorqueConverterPump",
    "TorqueConverterSpeedRatio",
    "TorqueConverterTurbine",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6542 import AbstractAssemblyCriticalSpeedAnalysis
    from ._6543 import AbstractShaftCriticalSpeedAnalysis
    from ._6544 import AbstractShaftOrHousingCriticalSpeedAnalysis
    from ._6545 import AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6546 import AGMAGleasonConicalGearCriticalSpeedAnalysis
    from ._6547 import AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
    from ._6548 import AGMAGleasonConicalGearSetCriticalSpeedAnalysis
    from ._6549 import AssemblyCriticalSpeedAnalysis
    from ._6550 import BearingCriticalSpeedAnalysis
    from ._6551 import BeltConnectionCriticalSpeedAnalysis
    from ._6552 import BeltDriveCriticalSpeedAnalysis
    from ._6553 import BevelDifferentialGearCriticalSpeedAnalysis
    from ._6554 import BevelDifferentialGearMeshCriticalSpeedAnalysis
    from ._6555 import BevelDifferentialGearSetCriticalSpeedAnalysis
    from ._6556 import BevelDifferentialPlanetGearCriticalSpeedAnalysis
    from ._6557 import BevelDifferentialSunGearCriticalSpeedAnalysis
    from ._6558 import BevelGearCriticalSpeedAnalysis
    from ._6559 import BevelGearMeshCriticalSpeedAnalysis
    from ._6560 import BevelGearSetCriticalSpeedAnalysis
    from ._6561 import BoltCriticalSpeedAnalysis
    from ._6562 import BoltedJointCriticalSpeedAnalysis
    from ._6563 import ClutchConnectionCriticalSpeedAnalysis
    from ._6564 import ClutchCriticalSpeedAnalysis
    from ._6565 import ClutchHalfCriticalSpeedAnalysis
    from ._6566 import CoaxialConnectionCriticalSpeedAnalysis
    from ._6567 import ComponentCriticalSpeedAnalysis
    from ._6568 import ConceptCouplingConnectionCriticalSpeedAnalysis
    from ._6569 import ConceptCouplingCriticalSpeedAnalysis
    from ._6570 import ConceptCouplingHalfCriticalSpeedAnalysis
    from ._6571 import ConceptGearCriticalSpeedAnalysis
    from ._6572 import ConceptGearMeshCriticalSpeedAnalysis
    from ._6573 import ConceptGearSetCriticalSpeedAnalysis
    from ._6574 import ConicalGearCriticalSpeedAnalysis
    from ._6575 import ConicalGearMeshCriticalSpeedAnalysis
    from ._6576 import ConicalGearSetCriticalSpeedAnalysis
    from ._6577 import ConnectionCriticalSpeedAnalysis
    from ._6578 import ConnectorCriticalSpeedAnalysis
    from ._6579 import CouplingConnectionCriticalSpeedAnalysis
    from ._6580 import CouplingCriticalSpeedAnalysis
    from ._6581 import CouplingHalfCriticalSpeedAnalysis
    from ._6582 import CriticalSpeedAnalysis
    from ._6583 import CriticalSpeedAnalysisDrawStyle
    from ._6584 import CriticalSpeedAnalysisOptions
    from ._6585 import CVTBeltConnectionCriticalSpeedAnalysis
    from ._6586 import CVTCriticalSpeedAnalysis
    from ._6587 import CVTPulleyCriticalSpeedAnalysis
    from ._6588 import CycloidalAssemblyCriticalSpeedAnalysis
    from ._6589 import CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
    from ._6590 import CycloidalDiscCriticalSpeedAnalysis
    from ._6591 import CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
    from ._6592 import CylindricalGearCriticalSpeedAnalysis
    from ._6593 import CylindricalGearMeshCriticalSpeedAnalysis
    from ._6594 import CylindricalGearSetCriticalSpeedAnalysis
    from ._6595 import CylindricalPlanetGearCriticalSpeedAnalysis
    from ._6596 import DatumCriticalSpeedAnalysis
    from ._6597 import ExternalCADModelCriticalSpeedAnalysis
    from ._6598 import FaceGearCriticalSpeedAnalysis
    from ._6599 import FaceGearMeshCriticalSpeedAnalysis
    from ._6600 import FaceGearSetCriticalSpeedAnalysis
    from ._6601 import FEPartCriticalSpeedAnalysis
    from ._6602 import FlexiblePinAssemblyCriticalSpeedAnalysis
    from ._6603 import GearCriticalSpeedAnalysis
    from ._6604 import GearMeshCriticalSpeedAnalysis
    from ._6605 import GearSetCriticalSpeedAnalysis
    from ._6606 import GuideDxfModelCriticalSpeedAnalysis
    from ._6607 import HypoidGearCriticalSpeedAnalysis
    from ._6608 import HypoidGearMeshCriticalSpeedAnalysis
    from ._6609 import HypoidGearSetCriticalSpeedAnalysis
    from ._6610 import InterMountableComponentConnectionCriticalSpeedAnalysis
    from ._6611 import KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
    from ._6612 import KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
    from ._6613 import KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
    from ._6614 import KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
    from ._6615 import KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
    from ._6616 import KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
    from ._6617 import KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
    from ._6618 import KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6619 import KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
    from ._6620 import MassDiscCriticalSpeedAnalysis
    from ._6621 import MeasurementComponentCriticalSpeedAnalysis
    from ._6622 import MountableComponentCriticalSpeedAnalysis
    from ._6623 import OilSealCriticalSpeedAnalysis
    from ._6624 import PartCriticalSpeedAnalysis
    from ._6625 import PartToPartShearCouplingConnectionCriticalSpeedAnalysis
    from ._6626 import PartToPartShearCouplingCriticalSpeedAnalysis
    from ._6627 import PartToPartShearCouplingHalfCriticalSpeedAnalysis
    from ._6628 import PlanetaryConnectionCriticalSpeedAnalysis
    from ._6629 import PlanetaryGearSetCriticalSpeedAnalysis
    from ._6630 import PlanetCarrierCriticalSpeedAnalysis
    from ._6631 import PointLoadCriticalSpeedAnalysis
    from ._6632 import PowerLoadCriticalSpeedAnalysis
    from ._6633 import PulleyCriticalSpeedAnalysis
    from ._6634 import RingPinsCriticalSpeedAnalysis
    from ._6635 import RingPinsToDiscConnectionCriticalSpeedAnalysis
    from ._6636 import RollingRingAssemblyCriticalSpeedAnalysis
    from ._6637 import RollingRingConnectionCriticalSpeedAnalysis
    from ._6638 import RollingRingCriticalSpeedAnalysis
    from ._6639 import RootAssemblyCriticalSpeedAnalysis
    from ._6640 import ShaftCriticalSpeedAnalysis
    from ._6641 import ShaftHubConnectionCriticalSpeedAnalysis
    from ._6642 import ShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6643 import SpecialisedAssemblyCriticalSpeedAnalysis
    from ._6644 import SpiralBevelGearCriticalSpeedAnalysis
    from ._6645 import SpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6646 import SpiralBevelGearSetCriticalSpeedAnalysis
    from ._6647 import SpringDamperConnectionCriticalSpeedAnalysis
    from ._6648 import SpringDamperCriticalSpeedAnalysis
    from ._6649 import SpringDamperHalfCriticalSpeedAnalysis
    from ._6650 import StraightBevelDiffGearCriticalSpeedAnalysis
    from ._6651 import StraightBevelDiffGearMeshCriticalSpeedAnalysis
    from ._6652 import StraightBevelDiffGearSetCriticalSpeedAnalysis
    from ._6653 import StraightBevelGearCriticalSpeedAnalysis
    from ._6654 import StraightBevelGearMeshCriticalSpeedAnalysis
    from ._6655 import StraightBevelGearSetCriticalSpeedAnalysis
    from ._6656 import StraightBevelPlanetGearCriticalSpeedAnalysis
    from ._6657 import StraightBevelSunGearCriticalSpeedAnalysis
    from ._6658 import SynchroniserCriticalSpeedAnalysis
    from ._6659 import SynchroniserHalfCriticalSpeedAnalysis
    from ._6660 import SynchroniserPartCriticalSpeedAnalysis
    from ._6661 import SynchroniserSleeveCriticalSpeedAnalysis
    from ._6662 import TorqueConverterConnectionCriticalSpeedAnalysis
    from ._6663 import TorqueConverterCriticalSpeedAnalysis
    from ._6664 import TorqueConverterPumpCriticalSpeedAnalysis
    from ._6665 import TorqueConverterTurbineCriticalSpeedAnalysis
    from ._6666 import UnbalancedMassCriticalSpeedAnalysis
    from ._6667 import VirtualComponentCriticalSpeedAnalysis
    from ._6668 import WormGearCriticalSpeedAnalysis
    from ._6669 import WormGearMeshCriticalSpeedAnalysis
    from ._6670 import WormGearSetCriticalSpeedAnalysis
    from ._6671 import ZerolBevelGearCriticalSpeedAnalysis
    from ._6672 import ZerolBevelGearMeshCriticalSpeedAnalysis
    from ._6673 import ZerolBevelGearSetCriticalSpeedAnalysis
else:
    import_structure = {
        "_6542": ["AbstractAssemblyCriticalSpeedAnalysis"],
        "_6543": ["AbstractShaftCriticalSpeedAnalysis"],
        "_6544": ["AbstractShaftOrHousingCriticalSpeedAnalysis"],
        "_6545": ["AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6546": ["AGMAGleasonConicalGearCriticalSpeedAnalysis"],
        "_6547": ["AGMAGleasonConicalGearMeshCriticalSpeedAnalysis"],
        "_6548": ["AGMAGleasonConicalGearSetCriticalSpeedAnalysis"],
        "_6549": ["AssemblyCriticalSpeedAnalysis"],
        "_6550": ["BearingCriticalSpeedAnalysis"],
        "_6551": ["BeltConnectionCriticalSpeedAnalysis"],
        "_6552": ["BeltDriveCriticalSpeedAnalysis"],
        "_6553": ["BevelDifferentialGearCriticalSpeedAnalysis"],
        "_6554": ["BevelDifferentialGearMeshCriticalSpeedAnalysis"],
        "_6555": ["BevelDifferentialGearSetCriticalSpeedAnalysis"],
        "_6556": ["BevelDifferentialPlanetGearCriticalSpeedAnalysis"],
        "_6557": ["BevelDifferentialSunGearCriticalSpeedAnalysis"],
        "_6558": ["BevelGearCriticalSpeedAnalysis"],
        "_6559": ["BevelGearMeshCriticalSpeedAnalysis"],
        "_6560": ["BevelGearSetCriticalSpeedAnalysis"],
        "_6561": ["BoltCriticalSpeedAnalysis"],
        "_6562": ["BoltedJointCriticalSpeedAnalysis"],
        "_6563": ["ClutchConnectionCriticalSpeedAnalysis"],
        "_6564": ["ClutchCriticalSpeedAnalysis"],
        "_6565": ["ClutchHalfCriticalSpeedAnalysis"],
        "_6566": ["CoaxialConnectionCriticalSpeedAnalysis"],
        "_6567": ["ComponentCriticalSpeedAnalysis"],
        "_6568": ["ConceptCouplingConnectionCriticalSpeedAnalysis"],
        "_6569": ["ConceptCouplingCriticalSpeedAnalysis"],
        "_6570": ["ConceptCouplingHalfCriticalSpeedAnalysis"],
        "_6571": ["ConceptGearCriticalSpeedAnalysis"],
        "_6572": ["ConceptGearMeshCriticalSpeedAnalysis"],
        "_6573": ["ConceptGearSetCriticalSpeedAnalysis"],
        "_6574": ["ConicalGearCriticalSpeedAnalysis"],
        "_6575": ["ConicalGearMeshCriticalSpeedAnalysis"],
        "_6576": ["ConicalGearSetCriticalSpeedAnalysis"],
        "_6577": ["ConnectionCriticalSpeedAnalysis"],
        "_6578": ["ConnectorCriticalSpeedAnalysis"],
        "_6579": ["CouplingConnectionCriticalSpeedAnalysis"],
        "_6580": ["CouplingCriticalSpeedAnalysis"],
        "_6581": ["CouplingHalfCriticalSpeedAnalysis"],
        "_6582": ["CriticalSpeedAnalysis"],
        "_6583": ["CriticalSpeedAnalysisDrawStyle"],
        "_6584": ["CriticalSpeedAnalysisOptions"],
        "_6585": ["CVTBeltConnectionCriticalSpeedAnalysis"],
        "_6586": ["CVTCriticalSpeedAnalysis"],
        "_6587": ["CVTPulleyCriticalSpeedAnalysis"],
        "_6588": ["CycloidalAssemblyCriticalSpeedAnalysis"],
        "_6589": ["CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis"],
        "_6590": ["CycloidalDiscCriticalSpeedAnalysis"],
        "_6591": ["CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis"],
        "_6592": ["CylindricalGearCriticalSpeedAnalysis"],
        "_6593": ["CylindricalGearMeshCriticalSpeedAnalysis"],
        "_6594": ["CylindricalGearSetCriticalSpeedAnalysis"],
        "_6595": ["CylindricalPlanetGearCriticalSpeedAnalysis"],
        "_6596": ["DatumCriticalSpeedAnalysis"],
        "_6597": ["ExternalCADModelCriticalSpeedAnalysis"],
        "_6598": ["FaceGearCriticalSpeedAnalysis"],
        "_6599": ["FaceGearMeshCriticalSpeedAnalysis"],
        "_6600": ["FaceGearSetCriticalSpeedAnalysis"],
        "_6601": ["FEPartCriticalSpeedAnalysis"],
        "_6602": ["FlexiblePinAssemblyCriticalSpeedAnalysis"],
        "_6603": ["GearCriticalSpeedAnalysis"],
        "_6604": ["GearMeshCriticalSpeedAnalysis"],
        "_6605": ["GearSetCriticalSpeedAnalysis"],
        "_6606": ["GuideDxfModelCriticalSpeedAnalysis"],
        "_6607": ["HypoidGearCriticalSpeedAnalysis"],
        "_6608": ["HypoidGearMeshCriticalSpeedAnalysis"],
        "_6609": ["HypoidGearSetCriticalSpeedAnalysis"],
        "_6610": ["InterMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6611": ["KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis"],
        "_6612": ["KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis"],
        "_6613": ["KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"],
        "_6614": ["KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis"],
        "_6615": ["KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis"],
        "_6616": ["KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis"],
        "_6617": ["KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis"],
        "_6618": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6619": ["KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6620": ["MassDiscCriticalSpeedAnalysis"],
        "_6621": ["MeasurementComponentCriticalSpeedAnalysis"],
        "_6622": ["MountableComponentCriticalSpeedAnalysis"],
        "_6623": ["OilSealCriticalSpeedAnalysis"],
        "_6624": ["PartCriticalSpeedAnalysis"],
        "_6625": ["PartToPartShearCouplingConnectionCriticalSpeedAnalysis"],
        "_6626": ["PartToPartShearCouplingCriticalSpeedAnalysis"],
        "_6627": ["PartToPartShearCouplingHalfCriticalSpeedAnalysis"],
        "_6628": ["PlanetaryConnectionCriticalSpeedAnalysis"],
        "_6629": ["PlanetaryGearSetCriticalSpeedAnalysis"],
        "_6630": ["PlanetCarrierCriticalSpeedAnalysis"],
        "_6631": ["PointLoadCriticalSpeedAnalysis"],
        "_6632": ["PowerLoadCriticalSpeedAnalysis"],
        "_6633": ["PulleyCriticalSpeedAnalysis"],
        "_6634": ["RingPinsCriticalSpeedAnalysis"],
        "_6635": ["RingPinsToDiscConnectionCriticalSpeedAnalysis"],
        "_6636": ["RollingRingAssemblyCriticalSpeedAnalysis"],
        "_6637": ["RollingRingConnectionCriticalSpeedAnalysis"],
        "_6638": ["RollingRingCriticalSpeedAnalysis"],
        "_6639": ["RootAssemblyCriticalSpeedAnalysis"],
        "_6640": ["ShaftCriticalSpeedAnalysis"],
        "_6641": ["ShaftHubConnectionCriticalSpeedAnalysis"],
        "_6642": ["ShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6643": ["SpecialisedAssemblyCriticalSpeedAnalysis"],
        "_6644": ["SpiralBevelGearCriticalSpeedAnalysis"],
        "_6645": ["SpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6646": ["SpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6647": ["SpringDamperConnectionCriticalSpeedAnalysis"],
        "_6648": ["SpringDamperCriticalSpeedAnalysis"],
        "_6649": ["SpringDamperHalfCriticalSpeedAnalysis"],
        "_6650": ["StraightBevelDiffGearCriticalSpeedAnalysis"],
        "_6651": ["StraightBevelDiffGearMeshCriticalSpeedAnalysis"],
        "_6652": ["StraightBevelDiffGearSetCriticalSpeedAnalysis"],
        "_6653": ["StraightBevelGearCriticalSpeedAnalysis"],
        "_6654": ["StraightBevelGearMeshCriticalSpeedAnalysis"],
        "_6655": ["StraightBevelGearSetCriticalSpeedAnalysis"],
        "_6656": ["StraightBevelPlanetGearCriticalSpeedAnalysis"],
        "_6657": ["StraightBevelSunGearCriticalSpeedAnalysis"],
        "_6658": ["SynchroniserCriticalSpeedAnalysis"],
        "_6659": ["SynchroniserHalfCriticalSpeedAnalysis"],
        "_6660": ["SynchroniserPartCriticalSpeedAnalysis"],
        "_6661": ["SynchroniserSleeveCriticalSpeedAnalysis"],
        "_6662": ["TorqueConverterConnectionCriticalSpeedAnalysis"],
        "_6663": ["TorqueConverterCriticalSpeedAnalysis"],
        "_6664": ["TorqueConverterPumpCriticalSpeedAnalysis"],
        "_6665": ["TorqueConverterTurbineCriticalSpeedAnalysis"],
        "_6666": ["UnbalancedMassCriticalSpeedAnalysis"],
        "_6667": ["VirtualComponentCriticalSpeedAnalysis"],
        "_6668": ["WormGearCriticalSpeedAnalysis"],
        "_6669": ["WormGearMeshCriticalSpeedAnalysis"],
        "_6670": ["WormGearSetCriticalSpeedAnalysis"],
        "_6671": ["ZerolBevelGearCriticalSpeedAnalysis"],
        "_6672": ["ZerolBevelGearMeshCriticalSpeedAnalysis"],
        "_6673": ["ZerolBevelGearSetCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCriticalSpeedAnalysis",
    "AbstractShaftCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCriticalSpeedAnalysis",
    "AssemblyCriticalSpeedAnalysis",
    "BearingCriticalSpeedAnalysis",
    "BeltConnectionCriticalSpeedAnalysis",
    "BeltDriveCriticalSpeedAnalysis",
    "BevelDifferentialGearCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCriticalSpeedAnalysis",
    "BevelGearCriticalSpeedAnalysis",
    "BevelGearMeshCriticalSpeedAnalysis",
    "BevelGearSetCriticalSpeedAnalysis",
    "BoltCriticalSpeedAnalysis",
    "BoltedJointCriticalSpeedAnalysis",
    "ClutchConnectionCriticalSpeedAnalysis",
    "ClutchCriticalSpeedAnalysis",
    "ClutchHalfCriticalSpeedAnalysis",
    "CoaxialConnectionCriticalSpeedAnalysis",
    "ComponentCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCriticalSpeedAnalysis",
    "ConceptCouplingCriticalSpeedAnalysis",
    "ConceptCouplingHalfCriticalSpeedAnalysis",
    "ConceptGearCriticalSpeedAnalysis",
    "ConceptGearMeshCriticalSpeedAnalysis",
    "ConceptGearSetCriticalSpeedAnalysis",
    "ConicalGearCriticalSpeedAnalysis",
    "ConicalGearMeshCriticalSpeedAnalysis",
    "ConicalGearSetCriticalSpeedAnalysis",
    "ConnectionCriticalSpeedAnalysis",
    "ConnectorCriticalSpeedAnalysis",
    "CouplingConnectionCriticalSpeedAnalysis",
    "CouplingCriticalSpeedAnalysis",
    "CouplingHalfCriticalSpeedAnalysis",
    "CriticalSpeedAnalysis",
    "CriticalSpeedAnalysisDrawStyle",
    "CriticalSpeedAnalysisOptions",
    "CVTBeltConnectionCriticalSpeedAnalysis",
    "CVTCriticalSpeedAnalysis",
    "CVTPulleyCriticalSpeedAnalysis",
    "CycloidalAssemblyCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis",
    "CycloidalDiscCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis",
    "CylindricalGearCriticalSpeedAnalysis",
    "CylindricalGearMeshCriticalSpeedAnalysis",
    "CylindricalGearSetCriticalSpeedAnalysis",
    "CylindricalPlanetGearCriticalSpeedAnalysis",
    "DatumCriticalSpeedAnalysis",
    "ExternalCADModelCriticalSpeedAnalysis",
    "FaceGearCriticalSpeedAnalysis",
    "FaceGearMeshCriticalSpeedAnalysis",
    "FaceGearSetCriticalSpeedAnalysis",
    "FEPartCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCriticalSpeedAnalysis",
    "GearCriticalSpeedAnalysis",
    "GearMeshCriticalSpeedAnalysis",
    "GearSetCriticalSpeedAnalysis",
    "GuideDxfModelCriticalSpeedAnalysis",
    "HypoidGearCriticalSpeedAnalysis",
    "HypoidGearMeshCriticalSpeedAnalysis",
    "HypoidGearSetCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis",
    "MassDiscCriticalSpeedAnalysis",
    "MeasurementComponentCriticalSpeedAnalysis",
    "MountableComponentCriticalSpeedAnalysis",
    "OilSealCriticalSpeedAnalysis",
    "PartCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCriticalSpeedAnalysis",
    "PartToPartShearCouplingCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCriticalSpeedAnalysis",
    "PlanetaryConnectionCriticalSpeedAnalysis",
    "PlanetaryGearSetCriticalSpeedAnalysis",
    "PlanetCarrierCriticalSpeedAnalysis",
    "PointLoadCriticalSpeedAnalysis",
    "PowerLoadCriticalSpeedAnalysis",
    "PulleyCriticalSpeedAnalysis",
    "RingPinsCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCriticalSpeedAnalysis",
    "RollingRingAssemblyCriticalSpeedAnalysis",
    "RollingRingConnectionCriticalSpeedAnalysis",
    "RollingRingCriticalSpeedAnalysis",
    "RootAssemblyCriticalSpeedAnalysis",
    "ShaftCriticalSpeedAnalysis",
    "ShaftHubConnectionCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCriticalSpeedAnalysis",
    "SpecialisedAssemblyCriticalSpeedAnalysis",
    "SpiralBevelGearCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCriticalSpeedAnalysis",
    "SpiralBevelGearSetCriticalSpeedAnalysis",
    "SpringDamperConnectionCriticalSpeedAnalysis",
    "SpringDamperCriticalSpeedAnalysis",
    "SpringDamperHalfCriticalSpeedAnalysis",
    "StraightBevelDiffGearCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCriticalSpeedAnalysis",
    "StraightBevelGearCriticalSpeedAnalysis",
    "StraightBevelGearMeshCriticalSpeedAnalysis",
    "StraightBevelGearSetCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCriticalSpeedAnalysis",
    "StraightBevelSunGearCriticalSpeedAnalysis",
    "SynchroniserCriticalSpeedAnalysis",
    "SynchroniserHalfCriticalSpeedAnalysis",
    "SynchroniserPartCriticalSpeedAnalysis",
    "SynchroniserSleeveCriticalSpeedAnalysis",
    "TorqueConverterConnectionCriticalSpeedAnalysis",
    "TorqueConverterCriticalSpeedAnalysis",
    "TorqueConverterPumpCriticalSpeedAnalysis",
    "TorqueConverterTurbineCriticalSpeedAnalysis",
    "UnbalancedMassCriticalSpeedAnalysis",
    "VirtualComponentCriticalSpeedAnalysis",
    "WormGearCriticalSpeedAnalysis",
    "WormGearMeshCriticalSpeedAnalysis",
    "WormGearSetCriticalSpeedAnalysis",
    "ZerolBevelGearCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCriticalSpeedAnalysis",
    "ZerolBevelGearSetCriticalSpeedAnalysis",
)

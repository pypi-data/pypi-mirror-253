"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6543 import AbstractAssemblyCriticalSpeedAnalysis
    from ._6544 import AbstractShaftCriticalSpeedAnalysis
    from ._6545 import AbstractShaftOrHousingCriticalSpeedAnalysis
    from ._6546 import AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6547 import AGMAGleasonConicalGearCriticalSpeedAnalysis
    from ._6548 import AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
    from ._6549 import AGMAGleasonConicalGearSetCriticalSpeedAnalysis
    from ._6550 import AssemblyCriticalSpeedAnalysis
    from ._6551 import BearingCriticalSpeedAnalysis
    from ._6552 import BeltConnectionCriticalSpeedAnalysis
    from ._6553 import BeltDriveCriticalSpeedAnalysis
    from ._6554 import BevelDifferentialGearCriticalSpeedAnalysis
    from ._6555 import BevelDifferentialGearMeshCriticalSpeedAnalysis
    from ._6556 import BevelDifferentialGearSetCriticalSpeedAnalysis
    from ._6557 import BevelDifferentialPlanetGearCriticalSpeedAnalysis
    from ._6558 import BevelDifferentialSunGearCriticalSpeedAnalysis
    from ._6559 import BevelGearCriticalSpeedAnalysis
    from ._6560 import BevelGearMeshCriticalSpeedAnalysis
    from ._6561 import BevelGearSetCriticalSpeedAnalysis
    from ._6562 import BoltCriticalSpeedAnalysis
    from ._6563 import BoltedJointCriticalSpeedAnalysis
    from ._6564 import ClutchConnectionCriticalSpeedAnalysis
    from ._6565 import ClutchCriticalSpeedAnalysis
    from ._6566 import ClutchHalfCriticalSpeedAnalysis
    from ._6567 import CoaxialConnectionCriticalSpeedAnalysis
    from ._6568 import ComponentCriticalSpeedAnalysis
    from ._6569 import ConceptCouplingConnectionCriticalSpeedAnalysis
    from ._6570 import ConceptCouplingCriticalSpeedAnalysis
    from ._6571 import ConceptCouplingHalfCriticalSpeedAnalysis
    from ._6572 import ConceptGearCriticalSpeedAnalysis
    from ._6573 import ConceptGearMeshCriticalSpeedAnalysis
    from ._6574 import ConceptGearSetCriticalSpeedAnalysis
    from ._6575 import ConicalGearCriticalSpeedAnalysis
    from ._6576 import ConicalGearMeshCriticalSpeedAnalysis
    from ._6577 import ConicalGearSetCriticalSpeedAnalysis
    from ._6578 import ConnectionCriticalSpeedAnalysis
    from ._6579 import ConnectorCriticalSpeedAnalysis
    from ._6580 import CouplingConnectionCriticalSpeedAnalysis
    from ._6581 import CouplingCriticalSpeedAnalysis
    from ._6582 import CouplingHalfCriticalSpeedAnalysis
    from ._6583 import CriticalSpeedAnalysis
    from ._6584 import CriticalSpeedAnalysisDrawStyle
    from ._6585 import CriticalSpeedAnalysisOptions
    from ._6586 import CVTBeltConnectionCriticalSpeedAnalysis
    from ._6587 import CVTCriticalSpeedAnalysis
    from ._6588 import CVTPulleyCriticalSpeedAnalysis
    from ._6589 import CycloidalAssemblyCriticalSpeedAnalysis
    from ._6590 import CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis
    from ._6591 import CycloidalDiscCriticalSpeedAnalysis
    from ._6592 import CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis
    from ._6593 import CylindricalGearCriticalSpeedAnalysis
    from ._6594 import CylindricalGearMeshCriticalSpeedAnalysis
    from ._6595 import CylindricalGearSetCriticalSpeedAnalysis
    from ._6596 import CylindricalPlanetGearCriticalSpeedAnalysis
    from ._6597 import DatumCriticalSpeedAnalysis
    from ._6598 import ExternalCADModelCriticalSpeedAnalysis
    from ._6599 import FaceGearCriticalSpeedAnalysis
    from ._6600 import FaceGearMeshCriticalSpeedAnalysis
    from ._6601 import FaceGearSetCriticalSpeedAnalysis
    from ._6602 import FEPartCriticalSpeedAnalysis
    from ._6603 import FlexiblePinAssemblyCriticalSpeedAnalysis
    from ._6604 import GearCriticalSpeedAnalysis
    from ._6605 import GearMeshCriticalSpeedAnalysis
    from ._6606 import GearSetCriticalSpeedAnalysis
    from ._6607 import GuideDxfModelCriticalSpeedAnalysis
    from ._6608 import HypoidGearCriticalSpeedAnalysis
    from ._6609 import HypoidGearMeshCriticalSpeedAnalysis
    from ._6610 import HypoidGearSetCriticalSpeedAnalysis
    from ._6611 import InterMountableComponentConnectionCriticalSpeedAnalysis
    from ._6612 import KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
    from ._6613 import KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
    from ._6614 import KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
    from ._6615 import KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
    from ._6616 import KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
    from ._6617 import KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
    from ._6618 import KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
    from ._6619 import KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6620 import KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
    from ._6621 import MassDiscCriticalSpeedAnalysis
    from ._6622 import MeasurementComponentCriticalSpeedAnalysis
    from ._6623 import MountableComponentCriticalSpeedAnalysis
    from ._6624 import OilSealCriticalSpeedAnalysis
    from ._6625 import PartCriticalSpeedAnalysis
    from ._6626 import PartToPartShearCouplingConnectionCriticalSpeedAnalysis
    from ._6627 import PartToPartShearCouplingCriticalSpeedAnalysis
    from ._6628 import PartToPartShearCouplingHalfCriticalSpeedAnalysis
    from ._6629 import PlanetaryConnectionCriticalSpeedAnalysis
    from ._6630 import PlanetaryGearSetCriticalSpeedAnalysis
    from ._6631 import PlanetCarrierCriticalSpeedAnalysis
    from ._6632 import PointLoadCriticalSpeedAnalysis
    from ._6633 import PowerLoadCriticalSpeedAnalysis
    from ._6634 import PulleyCriticalSpeedAnalysis
    from ._6635 import RingPinsCriticalSpeedAnalysis
    from ._6636 import RingPinsToDiscConnectionCriticalSpeedAnalysis
    from ._6637 import RollingRingAssemblyCriticalSpeedAnalysis
    from ._6638 import RollingRingConnectionCriticalSpeedAnalysis
    from ._6639 import RollingRingCriticalSpeedAnalysis
    from ._6640 import RootAssemblyCriticalSpeedAnalysis
    from ._6641 import ShaftCriticalSpeedAnalysis
    from ._6642 import ShaftHubConnectionCriticalSpeedAnalysis
    from ._6643 import ShaftToMountableComponentConnectionCriticalSpeedAnalysis
    from ._6644 import SpecialisedAssemblyCriticalSpeedAnalysis
    from ._6645 import SpiralBevelGearCriticalSpeedAnalysis
    from ._6646 import SpiralBevelGearMeshCriticalSpeedAnalysis
    from ._6647 import SpiralBevelGearSetCriticalSpeedAnalysis
    from ._6648 import SpringDamperConnectionCriticalSpeedAnalysis
    from ._6649 import SpringDamperCriticalSpeedAnalysis
    from ._6650 import SpringDamperHalfCriticalSpeedAnalysis
    from ._6651 import StraightBevelDiffGearCriticalSpeedAnalysis
    from ._6652 import StraightBevelDiffGearMeshCriticalSpeedAnalysis
    from ._6653 import StraightBevelDiffGearSetCriticalSpeedAnalysis
    from ._6654 import StraightBevelGearCriticalSpeedAnalysis
    from ._6655 import StraightBevelGearMeshCriticalSpeedAnalysis
    from ._6656 import StraightBevelGearSetCriticalSpeedAnalysis
    from ._6657 import StraightBevelPlanetGearCriticalSpeedAnalysis
    from ._6658 import StraightBevelSunGearCriticalSpeedAnalysis
    from ._6659 import SynchroniserCriticalSpeedAnalysis
    from ._6660 import SynchroniserHalfCriticalSpeedAnalysis
    from ._6661 import SynchroniserPartCriticalSpeedAnalysis
    from ._6662 import SynchroniserSleeveCriticalSpeedAnalysis
    from ._6663 import TorqueConverterConnectionCriticalSpeedAnalysis
    from ._6664 import TorqueConverterCriticalSpeedAnalysis
    from ._6665 import TorqueConverterPumpCriticalSpeedAnalysis
    from ._6666 import TorqueConverterTurbineCriticalSpeedAnalysis
    from ._6667 import UnbalancedMassCriticalSpeedAnalysis
    from ._6668 import VirtualComponentCriticalSpeedAnalysis
    from ._6669 import WormGearCriticalSpeedAnalysis
    from ._6670 import WormGearMeshCriticalSpeedAnalysis
    from ._6671 import WormGearSetCriticalSpeedAnalysis
    from ._6672 import ZerolBevelGearCriticalSpeedAnalysis
    from ._6673 import ZerolBevelGearMeshCriticalSpeedAnalysis
    from ._6674 import ZerolBevelGearSetCriticalSpeedAnalysis
else:
    import_structure = {
        "_6543": ["AbstractAssemblyCriticalSpeedAnalysis"],
        "_6544": ["AbstractShaftCriticalSpeedAnalysis"],
        "_6545": ["AbstractShaftOrHousingCriticalSpeedAnalysis"],
        "_6546": ["AbstractShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6547": ["AGMAGleasonConicalGearCriticalSpeedAnalysis"],
        "_6548": ["AGMAGleasonConicalGearMeshCriticalSpeedAnalysis"],
        "_6549": ["AGMAGleasonConicalGearSetCriticalSpeedAnalysis"],
        "_6550": ["AssemblyCriticalSpeedAnalysis"],
        "_6551": ["BearingCriticalSpeedAnalysis"],
        "_6552": ["BeltConnectionCriticalSpeedAnalysis"],
        "_6553": ["BeltDriveCriticalSpeedAnalysis"],
        "_6554": ["BevelDifferentialGearCriticalSpeedAnalysis"],
        "_6555": ["BevelDifferentialGearMeshCriticalSpeedAnalysis"],
        "_6556": ["BevelDifferentialGearSetCriticalSpeedAnalysis"],
        "_6557": ["BevelDifferentialPlanetGearCriticalSpeedAnalysis"],
        "_6558": ["BevelDifferentialSunGearCriticalSpeedAnalysis"],
        "_6559": ["BevelGearCriticalSpeedAnalysis"],
        "_6560": ["BevelGearMeshCriticalSpeedAnalysis"],
        "_6561": ["BevelGearSetCriticalSpeedAnalysis"],
        "_6562": ["BoltCriticalSpeedAnalysis"],
        "_6563": ["BoltedJointCriticalSpeedAnalysis"],
        "_6564": ["ClutchConnectionCriticalSpeedAnalysis"],
        "_6565": ["ClutchCriticalSpeedAnalysis"],
        "_6566": ["ClutchHalfCriticalSpeedAnalysis"],
        "_6567": ["CoaxialConnectionCriticalSpeedAnalysis"],
        "_6568": ["ComponentCriticalSpeedAnalysis"],
        "_6569": ["ConceptCouplingConnectionCriticalSpeedAnalysis"],
        "_6570": ["ConceptCouplingCriticalSpeedAnalysis"],
        "_6571": ["ConceptCouplingHalfCriticalSpeedAnalysis"],
        "_6572": ["ConceptGearCriticalSpeedAnalysis"],
        "_6573": ["ConceptGearMeshCriticalSpeedAnalysis"],
        "_6574": ["ConceptGearSetCriticalSpeedAnalysis"],
        "_6575": ["ConicalGearCriticalSpeedAnalysis"],
        "_6576": ["ConicalGearMeshCriticalSpeedAnalysis"],
        "_6577": ["ConicalGearSetCriticalSpeedAnalysis"],
        "_6578": ["ConnectionCriticalSpeedAnalysis"],
        "_6579": ["ConnectorCriticalSpeedAnalysis"],
        "_6580": ["CouplingConnectionCriticalSpeedAnalysis"],
        "_6581": ["CouplingCriticalSpeedAnalysis"],
        "_6582": ["CouplingHalfCriticalSpeedAnalysis"],
        "_6583": ["CriticalSpeedAnalysis"],
        "_6584": ["CriticalSpeedAnalysisDrawStyle"],
        "_6585": ["CriticalSpeedAnalysisOptions"],
        "_6586": ["CVTBeltConnectionCriticalSpeedAnalysis"],
        "_6587": ["CVTCriticalSpeedAnalysis"],
        "_6588": ["CVTPulleyCriticalSpeedAnalysis"],
        "_6589": ["CycloidalAssemblyCriticalSpeedAnalysis"],
        "_6590": ["CycloidalDiscCentralBearingConnectionCriticalSpeedAnalysis"],
        "_6591": ["CycloidalDiscCriticalSpeedAnalysis"],
        "_6592": ["CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis"],
        "_6593": ["CylindricalGearCriticalSpeedAnalysis"],
        "_6594": ["CylindricalGearMeshCriticalSpeedAnalysis"],
        "_6595": ["CylindricalGearSetCriticalSpeedAnalysis"],
        "_6596": ["CylindricalPlanetGearCriticalSpeedAnalysis"],
        "_6597": ["DatumCriticalSpeedAnalysis"],
        "_6598": ["ExternalCADModelCriticalSpeedAnalysis"],
        "_6599": ["FaceGearCriticalSpeedAnalysis"],
        "_6600": ["FaceGearMeshCriticalSpeedAnalysis"],
        "_6601": ["FaceGearSetCriticalSpeedAnalysis"],
        "_6602": ["FEPartCriticalSpeedAnalysis"],
        "_6603": ["FlexiblePinAssemblyCriticalSpeedAnalysis"],
        "_6604": ["GearCriticalSpeedAnalysis"],
        "_6605": ["GearMeshCriticalSpeedAnalysis"],
        "_6606": ["GearSetCriticalSpeedAnalysis"],
        "_6607": ["GuideDxfModelCriticalSpeedAnalysis"],
        "_6608": ["HypoidGearCriticalSpeedAnalysis"],
        "_6609": ["HypoidGearMeshCriticalSpeedAnalysis"],
        "_6610": ["HypoidGearSetCriticalSpeedAnalysis"],
        "_6611": ["InterMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6612": ["KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis"],
        "_6613": ["KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis"],
        "_6614": ["KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis"],
        "_6615": ["KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis"],
        "_6616": ["KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis"],
        "_6617": ["KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis"],
        "_6618": ["KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis"],
        "_6619": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6620": ["KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6621": ["MassDiscCriticalSpeedAnalysis"],
        "_6622": ["MeasurementComponentCriticalSpeedAnalysis"],
        "_6623": ["MountableComponentCriticalSpeedAnalysis"],
        "_6624": ["OilSealCriticalSpeedAnalysis"],
        "_6625": ["PartCriticalSpeedAnalysis"],
        "_6626": ["PartToPartShearCouplingConnectionCriticalSpeedAnalysis"],
        "_6627": ["PartToPartShearCouplingCriticalSpeedAnalysis"],
        "_6628": ["PartToPartShearCouplingHalfCriticalSpeedAnalysis"],
        "_6629": ["PlanetaryConnectionCriticalSpeedAnalysis"],
        "_6630": ["PlanetaryGearSetCriticalSpeedAnalysis"],
        "_6631": ["PlanetCarrierCriticalSpeedAnalysis"],
        "_6632": ["PointLoadCriticalSpeedAnalysis"],
        "_6633": ["PowerLoadCriticalSpeedAnalysis"],
        "_6634": ["PulleyCriticalSpeedAnalysis"],
        "_6635": ["RingPinsCriticalSpeedAnalysis"],
        "_6636": ["RingPinsToDiscConnectionCriticalSpeedAnalysis"],
        "_6637": ["RollingRingAssemblyCriticalSpeedAnalysis"],
        "_6638": ["RollingRingConnectionCriticalSpeedAnalysis"],
        "_6639": ["RollingRingCriticalSpeedAnalysis"],
        "_6640": ["RootAssemblyCriticalSpeedAnalysis"],
        "_6641": ["ShaftCriticalSpeedAnalysis"],
        "_6642": ["ShaftHubConnectionCriticalSpeedAnalysis"],
        "_6643": ["ShaftToMountableComponentConnectionCriticalSpeedAnalysis"],
        "_6644": ["SpecialisedAssemblyCriticalSpeedAnalysis"],
        "_6645": ["SpiralBevelGearCriticalSpeedAnalysis"],
        "_6646": ["SpiralBevelGearMeshCriticalSpeedAnalysis"],
        "_6647": ["SpiralBevelGearSetCriticalSpeedAnalysis"],
        "_6648": ["SpringDamperConnectionCriticalSpeedAnalysis"],
        "_6649": ["SpringDamperCriticalSpeedAnalysis"],
        "_6650": ["SpringDamperHalfCriticalSpeedAnalysis"],
        "_6651": ["StraightBevelDiffGearCriticalSpeedAnalysis"],
        "_6652": ["StraightBevelDiffGearMeshCriticalSpeedAnalysis"],
        "_6653": ["StraightBevelDiffGearSetCriticalSpeedAnalysis"],
        "_6654": ["StraightBevelGearCriticalSpeedAnalysis"],
        "_6655": ["StraightBevelGearMeshCriticalSpeedAnalysis"],
        "_6656": ["StraightBevelGearSetCriticalSpeedAnalysis"],
        "_6657": ["StraightBevelPlanetGearCriticalSpeedAnalysis"],
        "_6658": ["StraightBevelSunGearCriticalSpeedAnalysis"],
        "_6659": ["SynchroniserCriticalSpeedAnalysis"],
        "_6660": ["SynchroniserHalfCriticalSpeedAnalysis"],
        "_6661": ["SynchroniserPartCriticalSpeedAnalysis"],
        "_6662": ["SynchroniserSleeveCriticalSpeedAnalysis"],
        "_6663": ["TorqueConverterConnectionCriticalSpeedAnalysis"],
        "_6664": ["TorqueConverterCriticalSpeedAnalysis"],
        "_6665": ["TorqueConverterPumpCriticalSpeedAnalysis"],
        "_6666": ["TorqueConverterTurbineCriticalSpeedAnalysis"],
        "_6667": ["UnbalancedMassCriticalSpeedAnalysis"],
        "_6668": ["VirtualComponentCriticalSpeedAnalysis"],
        "_6669": ["WormGearCriticalSpeedAnalysis"],
        "_6670": ["WormGearMeshCriticalSpeedAnalysis"],
        "_6671": ["WormGearSetCriticalSpeedAnalysis"],
        "_6672": ["ZerolBevelGearCriticalSpeedAnalysis"],
        "_6673": ["ZerolBevelGearMeshCriticalSpeedAnalysis"],
        "_6674": ["ZerolBevelGearSetCriticalSpeedAnalysis"],
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

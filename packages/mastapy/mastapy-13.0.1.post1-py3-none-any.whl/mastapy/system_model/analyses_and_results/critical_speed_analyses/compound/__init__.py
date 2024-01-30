"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6675 import AbstractAssemblyCompoundCriticalSpeedAnalysis
    from ._6676 import AbstractShaftCompoundCriticalSpeedAnalysis
    from ._6677 import AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
    from ._6678 import (
        AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6679 import AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
    from ._6680 import AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6681 import AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6682 import AssemblyCompoundCriticalSpeedAnalysis
    from ._6683 import BearingCompoundCriticalSpeedAnalysis
    from ._6684 import BeltConnectionCompoundCriticalSpeedAnalysis
    from ._6685 import BeltDriveCompoundCriticalSpeedAnalysis
    from ._6686 import BevelDifferentialGearCompoundCriticalSpeedAnalysis
    from ._6687 import BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
    from ._6688 import BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
    from ._6689 import BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
    from ._6690 import BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
    from ._6691 import BevelGearCompoundCriticalSpeedAnalysis
    from ._6692 import BevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6693 import BevelGearSetCompoundCriticalSpeedAnalysis
    from ._6694 import BoltCompoundCriticalSpeedAnalysis
    from ._6695 import BoltedJointCompoundCriticalSpeedAnalysis
    from ._6696 import ClutchCompoundCriticalSpeedAnalysis
    from ._6697 import ClutchConnectionCompoundCriticalSpeedAnalysis
    from ._6698 import ClutchHalfCompoundCriticalSpeedAnalysis
    from ._6699 import CoaxialConnectionCompoundCriticalSpeedAnalysis
    from ._6700 import ComponentCompoundCriticalSpeedAnalysis
    from ._6701 import ConceptCouplingCompoundCriticalSpeedAnalysis
    from ._6702 import ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6703 import ConceptCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6704 import ConceptGearCompoundCriticalSpeedAnalysis
    from ._6705 import ConceptGearMeshCompoundCriticalSpeedAnalysis
    from ._6706 import ConceptGearSetCompoundCriticalSpeedAnalysis
    from ._6707 import ConicalGearCompoundCriticalSpeedAnalysis
    from ._6708 import ConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6709 import ConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6710 import ConnectionCompoundCriticalSpeedAnalysis
    from ._6711 import ConnectorCompoundCriticalSpeedAnalysis
    from ._6712 import CouplingCompoundCriticalSpeedAnalysis
    from ._6713 import CouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6714 import CouplingHalfCompoundCriticalSpeedAnalysis
    from ._6715 import CVTBeltConnectionCompoundCriticalSpeedAnalysis
    from ._6716 import CVTCompoundCriticalSpeedAnalysis
    from ._6717 import CVTPulleyCompoundCriticalSpeedAnalysis
    from ._6718 import CycloidalAssemblyCompoundCriticalSpeedAnalysis
    from ._6719 import (
        CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6720 import CycloidalDiscCompoundCriticalSpeedAnalysis
    from ._6721 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6722 import CylindricalGearCompoundCriticalSpeedAnalysis
    from ._6723 import CylindricalGearMeshCompoundCriticalSpeedAnalysis
    from ._6724 import CylindricalGearSetCompoundCriticalSpeedAnalysis
    from ._6725 import CylindricalPlanetGearCompoundCriticalSpeedAnalysis
    from ._6726 import DatumCompoundCriticalSpeedAnalysis
    from ._6727 import ExternalCADModelCompoundCriticalSpeedAnalysis
    from ._6728 import FaceGearCompoundCriticalSpeedAnalysis
    from ._6729 import FaceGearMeshCompoundCriticalSpeedAnalysis
    from ._6730 import FaceGearSetCompoundCriticalSpeedAnalysis
    from ._6731 import FEPartCompoundCriticalSpeedAnalysis
    from ._6732 import FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
    from ._6733 import GearCompoundCriticalSpeedAnalysis
    from ._6734 import GearMeshCompoundCriticalSpeedAnalysis
    from ._6735 import GearSetCompoundCriticalSpeedAnalysis
    from ._6736 import GuideDxfModelCompoundCriticalSpeedAnalysis
    from ._6737 import HypoidGearCompoundCriticalSpeedAnalysis
    from ._6738 import HypoidGearMeshCompoundCriticalSpeedAnalysis
    from ._6739 import HypoidGearSetCompoundCriticalSpeedAnalysis
    from ._6740 import InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6741 import KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
    from ._6742 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6743 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6744 import KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
    from ._6745 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6746 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6747 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis,
    )
    from ._6748 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6749 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6750 import MassDiscCompoundCriticalSpeedAnalysis
    from ._6751 import MeasurementComponentCompoundCriticalSpeedAnalysis
    from ._6752 import MountableComponentCompoundCriticalSpeedAnalysis
    from ._6753 import OilSealCompoundCriticalSpeedAnalysis
    from ._6754 import PartCompoundCriticalSpeedAnalysis
    from ._6755 import PartToPartShearCouplingCompoundCriticalSpeedAnalysis
    from ._6756 import PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6757 import PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6758 import PlanetaryConnectionCompoundCriticalSpeedAnalysis
    from ._6759 import PlanetaryGearSetCompoundCriticalSpeedAnalysis
    from ._6760 import PlanetCarrierCompoundCriticalSpeedAnalysis
    from ._6761 import PointLoadCompoundCriticalSpeedAnalysis
    from ._6762 import PowerLoadCompoundCriticalSpeedAnalysis
    from ._6763 import PulleyCompoundCriticalSpeedAnalysis
    from ._6764 import RingPinsCompoundCriticalSpeedAnalysis
    from ._6765 import RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
    from ._6766 import RollingRingAssemblyCompoundCriticalSpeedAnalysis
    from ._6767 import RollingRingCompoundCriticalSpeedAnalysis
    from ._6768 import RollingRingConnectionCompoundCriticalSpeedAnalysis
    from ._6769 import RootAssemblyCompoundCriticalSpeedAnalysis
    from ._6770 import ShaftCompoundCriticalSpeedAnalysis
    from ._6771 import ShaftHubConnectionCompoundCriticalSpeedAnalysis
    from ._6772 import ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6773 import SpecialisedAssemblyCompoundCriticalSpeedAnalysis
    from ._6774 import SpiralBevelGearCompoundCriticalSpeedAnalysis
    from ._6775 import SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6776 import SpiralBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6777 import SpringDamperCompoundCriticalSpeedAnalysis
    from ._6778 import SpringDamperConnectionCompoundCriticalSpeedAnalysis
    from ._6779 import SpringDamperHalfCompoundCriticalSpeedAnalysis
    from ._6780 import StraightBevelDiffGearCompoundCriticalSpeedAnalysis
    from ._6781 import StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
    from ._6782 import StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
    from ._6783 import StraightBevelGearCompoundCriticalSpeedAnalysis
    from ._6784 import StraightBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6785 import StraightBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6786 import StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
    from ._6787 import StraightBevelSunGearCompoundCriticalSpeedAnalysis
    from ._6788 import SynchroniserCompoundCriticalSpeedAnalysis
    from ._6789 import SynchroniserHalfCompoundCriticalSpeedAnalysis
    from ._6790 import SynchroniserPartCompoundCriticalSpeedAnalysis
    from ._6791 import SynchroniserSleeveCompoundCriticalSpeedAnalysis
    from ._6792 import TorqueConverterCompoundCriticalSpeedAnalysis
    from ._6793 import TorqueConverterConnectionCompoundCriticalSpeedAnalysis
    from ._6794 import TorqueConverterPumpCompoundCriticalSpeedAnalysis
    from ._6795 import TorqueConverterTurbineCompoundCriticalSpeedAnalysis
    from ._6796 import UnbalancedMassCompoundCriticalSpeedAnalysis
    from ._6797 import VirtualComponentCompoundCriticalSpeedAnalysis
    from ._6798 import WormGearCompoundCriticalSpeedAnalysis
    from ._6799 import WormGearMeshCompoundCriticalSpeedAnalysis
    from ._6800 import WormGearSetCompoundCriticalSpeedAnalysis
    from ._6801 import ZerolBevelGearCompoundCriticalSpeedAnalysis
    from ._6802 import ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6803 import ZerolBevelGearSetCompoundCriticalSpeedAnalysis
else:
    import_structure = {
        "_6675": ["AbstractAssemblyCompoundCriticalSpeedAnalysis"],
        "_6676": ["AbstractShaftCompoundCriticalSpeedAnalysis"],
        "_6677": ["AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"],
        "_6678": [
            "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6679": ["AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis"],
        "_6680": ["AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6681": ["AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6682": ["AssemblyCompoundCriticalSpeedAnalysis"],
        "_6683": ["BearingCompoundCriticalSpeedAnalysis"],
        "_6684": ["BeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6685": ["BeltDriveCompoundCriticalSpeedAnalysis"],
        "_6686": ["BevelDifferentialGearCompoundCriticalSpeedAnalysis"],
        "_6687": ["BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis"],
        "_6688": ["BevelDifferentialGearSetCompoundCriticalSpeedAnalysis"],
        "_6689": ["BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6690": ["BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"],
        "_6691": ["BevelGearCompoundCriticalSpeedAnalysis"],
        "_6692": ["BevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6693": ["BevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6694": ["BoltCompoundCriticalSpeedAnalysis"],
        "_6695": ["BoltedJointCompoundCriticalSpeedAnalysis"],
        "_6696": ["ClutchCompoundCriticalSpeedAnalysis"],
        "_6697": ["ClutchConnectionCompoundCriticalSpeedAnalysis"],
        "_6698": ["ClutchHalfCompoundCriticalSpeedAnalysis"],
        "_6699": ["CoaxialConnectionCompoundCriticalSpeedAnalysis"],
        "_6700": ["ComponentCompoundCriticalSpeedAnalysis"],
        "_6701": ["ConceptCouplingCompoundCriticalSpeedAnalysis"],
        "_6702": ["ConceptCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6703": ["ConceptCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6704": ["ConceptGearCompoundCriticalSpeedAnalysis"],
        "_6705": ["ConceptGearMeshCompoundCriticalSpeedAnalysis"],
        "_6706": ["ConceptGearSetCompoundCriticalSpeedAnalysis"],
        "_6707": ["ConicalGearCompoundCriticalSpeedAnalysis"],
        "_6708": ["ConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6709": ["ConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6710": ["ConnectionCompoundCriticalSpeedAnalysis"],
        "_6711": ["ConnectorCompoundCriticalSpeedAnalysis"],
        "_6712": ["CouplingCompoundCriticalSpeedAnalysis"],
        "_6713": ["CouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6714": ["CouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6715": ["CVTBeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6716": ["CVTCompoundCriticalSpeedAnalysis"],
        "_6717": ["CVTPulleyCompoundCriticalSpeedAnalysis"],
        "_6718": ["CycloidalAssemblyCompoundCriticalSpeedAnalysis"],
        "_6719": ["CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis"],
        "_6720": ["CycloidalDiscCompoundCriticalSpeedAnalysis"],
        "_6721": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6722": ["CylindricalGearCompoundCriticalSpeedAnalysis"],
        "_6723": ["CylindricalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6724": ["CylindricalGearSetCompoundCriticalSpeedAnalysis"],
        "_6725": ["CylindricalPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6726": ["DatumCompoundCriticalSpeedAnalysis"],
        "_6727": ["ExternalCADModelCompoundCriticalSpeedAnalysis"],
        "_6728": ["FaceGearCompoundCriticalSpeedAnalysis"],
        "_6729": ["FaceGearMeshCompoundCriticalSpeedAnalysis"],
        "_6730": ["FaceGearSetCompoundCriticalSpeedAnalysis"],
        "_6731": ["FEPartCompoundCriticalSpeedAnalysis"],
        "_6732": ["FlexiblePinAssemblyCompoundCriticalSpeedAnalysis"],
        "_6733": ["GearCompoundCriticalSpeedAnalysis"],
        "_6734": ["GearMeshCompoundCriticalSpeedAnalysis"],
        "_6735": ["GearSetCompoundCriticalSpeedAnalysis"],
        "_6736": ["GuideDxfModelCompoundCriticalSpeedAnalysis"],
        "_6737": ["HypoidGearCompoundCriticalSpeedAnalysis"],
        "_6738": ["HypoidGearMeshCompoundCriticalSpeedAnalysis"],
        "_6739": ["HypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6740": ["InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6741": ["KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis"],
        "_6742": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6743": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6744": ["KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis"],
        "_6745": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6746": ["KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6747": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ],
        "_6748": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6749": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6750": ["MassDiscCompoundCriticalSpeedAnalysis"],
        "_6751": ["MeasurementComponentCompoundCriticalSpeedAnalysis"],
        "_6752": ["MountableComponentCompoundCriticalSpeedAnalysis"],
        "_6753": ["OilSealCompoundCriticalSpeedAnalysis"],
        "_6754": ["PartCompoundCriticalSpeedAnalysis"],
        "_6755": ["PartToPartShearCouplingCompoundCriticalSpeedAnalysis"],
        "_6756": ["PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6757": ["PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6758": ["PlanetaryConnectionCompoundCriticalSpeedAnalysis"],
        "_6759": ["PlanetaryGearSetCompoundCriticalSpeedAnalysis"],
        "_6760": ["PlanetCarrierCompoundCriticalSpeedAnalysis"],
        "_6761": ["PointLoadCompoundCriticalSpeedAnalysis"],
        "_6762": ["PowerLoadCompoundCriticalSpeedAnalysis"],
        "_6763": ["PulleyCompoundCriticalSpeedAnalysis"],
        "_6764": ["RingPinsCompoundCriticalSpeedAnalysis"],
        "_6765": ["RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis"],
        "_6766": ["RollingRingAssemblyCompoundCriticalSpeedAnalysis"],
        "_6767": ["RollingRingCompoundCriticalSpeedAnalysis"],
        "_6768": ["RollingRingConnectionCompoundCriticalSpeedAnalysis"],
        "_6769": ["RootAssemblyCompoundCriticalSpeedAnalysis"],
        "_6770": ["ShaftCompoundCriticalSpeedAnalysis"],
        "_6771": ["ShaftHubConnectionCompoundCriticalSpeedAnalysis"],
        "_6772": ["ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6773": ["SpecialisedAssemblyCompoundCriticalSpeedAnalysis"],
        "_6774": ["SpiralBevelGearCompoundCriticalSpeedAnalysis"],
        "_6775": ["SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6776": ["SpiralBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6777": ["SpringDamperCompoundCriticalSpeedAnalysis"],
        "_6778": ["SpringDamperConnectionCompoundCriticalSpeedAnalysis"],
        "_6779": ["SpringDamperHalfCompoundCriticalSpeedAnalysis"],
        "_6780": ["StraightBevelDiffGearCompoundCriticalSpeedAnalysis"],
        "_6781": ["StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis"],
        "_6782": ["StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis"],
        "_6783": ["StraightBevelGearCompoundCriticalSpeedAnalysis"],
        "_6784": ["StraightBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6785": ["StraightBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6786": ["StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6787": ["StraightBevelSunGearCompoundCriticalSpeedAnalysis"],
        "_6788": ["SynchroniserCompoundCriticalSpeedAnalysis"],
        "_6789": ["SynchroniserHalfCompoundCriticalSpeedAnalysis"],
        "_6790": ["SynchroniserPartCompoundCriticalSpeedAnalysis"],
        "_6791": ["SynchroniserSleeveCompoundCriticalSpeedAnalysis"],
        "_6792": ["TorqueConverterCompoundCriticalSpeedAnalysis"],
        "_6793": ["TorqueConverterConnectionCompoundCriticalSpeedAnalysis"],
        "_6794": ["TorqueConverterPumpCompoundCriticalSpeedAnalysis"],
        "_6795": ["TorqueConverterTurbineCompoundCriticalSpeedAnalysis"],
        "_6796": ["UnbalancedMassCompoundCriticalSpeedAnalysis"],
        "_6797": ["VirtualComponentCompoundCriticalSpeedAnalysis"],
        "_6798": ["WormGearCompoundCriticalSpeedAnalysis"],
        "_6799": ["WormGearMeshCompoundCriticalSpeedAnalysis"],
        "_6800": ["WormGearSetCompoundCriticalSpeedAnalysis"],
        "_6801": ["ZerolBevelGearCompoundCriticalSpeedAnalysis"],
        "_6802": ["ZerolBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6803": ["ZerolBevelGearSetCompoundCriticalSpeedAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
    "AbstractShaftCompoundCriticalSpeedAnalysis",
    "AbstractShaftOrHousingCompoundCriticalSpeedAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis",
    "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
    "AssemblyCompoundCriticalSpeedAnalysis",
    "BearingCompoundCriticalSpeedAnalysis",
    "BeltConnectionCompoundCriticalSpeedAnalysis",
    "BeltDriveCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis",
    "BevelDifferentialGearSetCompoundCriticalSpeedAnalysis",
    "BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis",
    "BevelDifferentialSunGearCompoundCriticalSpeedAnalysis",
    "BevelGearCompoundCriticalSpeedAnalysis",
    "BevelGearMeshCompoundCriticalSpeedAnalysis",
    "BevelGearSetCompoundCriticalSpeedAnalysis",
    "BoltCompoundCriticalSpeedAnalysis",
    "BoltedJointCompoundCriticalSpeedAnalysis",
    "ClutchCompoundCriticalSpeedAnalysis",
    "ClutchConnectionCompoundCriticalSpeedAnalysis",
    "ClutchHalfCompoundCriticalSpeedAnalysis",
    "CoaxialConnectionCompoundCriticalSpeedAnalysis",
    "ComponentCompoundCriticalSpeedAnalysis",
    "ConceptCouplingCompoundCriticalSpeedAnalysis",
    "ConceptCouplingConnectionCompoundCriticalSpeedAnalysis",
    "ConceptCouplingHalfCompoundCriticalSpeedAnalysis",
    "ConceptGearCompoundCriticalSpeedAnalysis",
    "ConceptGearMeshCompoundCriticalSpeedAnalysis",
    "ConceptGearSetCompoundCriticalSpeedAnalysis",
    "ConicalGearCompoundCriticalSpeedAnalysis",
    "ConicalGearMeshCompoundCriticalSpeedAnalysis",
    "ConicalGearSetCompoundCriticalSpeedAnalysis",
    "ConnectionCompoundCriticalSpeedAnalysis",
    "ConnectorCompoundCriticalSpeedAnalysis",
    "CouplingCompoundCriticalSpeedAnalysis",
    "CouplingConnectionCompoundCriticalSpeedAnalysis",
    "CouplingHalfCompoundCriticalSpeedAnalysis",
    "CVTBeltConnectionCompoundCriticalSpeedAnalysis",
    "CVTCompoundCriticalSpeedAnalysis",
    "CVTPulleyCompoundCriticalSpeedAnalysis",
    "CycloidalAssemblyCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis",
    "CycloidalDiscCompoundCriticalSpeedAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis",
    "CylindricalGearCompoundCriticalSpeedAnalysis",
    "CylindricalGearMeshCompoundCriticalSpeedAnalysis",
    "CylindricalGearSetCompoundCriticalSpeedAnalysis",
    "CylindricalPlanetGearCompoundCriticalSpeedAnalysis",
    "DatumCompoundCriticalSpeedAnalysis",
    "ExternalCADModelCompoundCriticalSpeedAnalysis",
    "FaceGearCompoundCriticalSpeedAnalysis",
    "FaceGearMeshCompoundCriticalSpeedAnalysis",
    "FaceGearSetCompoundCriticalSpeedAnalysis",
    "FEPartCompoundCriticalSpeedAnalysis",
    "FlexiblePinAssemblyCompoundCriticalSpeedAnalysis",
    "GearCompoundCriticalSpeedAnalysis",
    "GearMeshCompoundCriticalSpeedAnalysis",
    "GearSetCompoundCriticalSpeedAnalysis",
    "GuideDxfModelCompoundCriticalSpeedAnalysis",
    "HypoidGearCompoundCriticalSpeedAnalysis",
    "HypoidGearMeshCompoundCriticalSpeedAnalysis",
    "HypoidGearSetCompoundCriticalSpeedAnalysis",
    "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "MassDiscCompoundCriticalSpeedAnalysis",
    "MeasurementComponentCompoundCriticalSpeedAnalysis",
    "MountableComponentCompoundCriticalSpeedAnalysis",
    "OilSealCompoundCriticalSpeedAnalysis",
    "PartCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis",
    "PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis",
    "PlanetaryConnectionCompoundCriticalSpeedAnalysis",
    "PlanetaryGearSetCompoundCriticalSpeedAnalysis",
    "PlanetCarrierCompoundCriticalSpeedAnalysis",
    "PointLoadCompoundCriticalSpeedAnalysis",
    "PowerLoadCompoundCriticalSpeedAnalysis",
    "PulleyCompoundCriticalSpeedAnalysis",
    "RingPinsCompoundCriticalSpeedAnalysis",
    "RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis",
    "RollingRingAssemblyCompoundCriticalSpeedAnalysis",
    "RollingRingCompoundCriticalSpeedAnalysis",
    "RollingRingConnectionCompoundCriticalSpeedAnalysis",
    "RootAssemblyCompoundCriticalSpeedAnalysis",
    "ShaftCompoundCriticalSpeedAnalysis",
    "ShaftHubConnectionCompoundCriticalSpeedAnalysis",
    "ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    "SpecialisedAssemblyCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
    "SpiralBevelGearSetCompoundCriticalSpeedAnalysis",
    "SpringDamperCompoundCriticalSpeedAnalysis",
    "SpringDamperConnectionCompoundCriticalSpeedAnalysis",
    "SpringDamperHalfCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelGearCompoundCriticalSpeedAnalysis",
    "StraightBevelGearMeshCompoundCriticalSpeedAnalysis",
    "StraightBevelGearSetCompoundCriticalSpeedAnalysis",
    "StraightBevelPlanetGearCompoundCriticalSpeedAnalysis",
    "StraightBevelSunGearCompoundCriticalSpeedAnalysis",
    "SynchroniserCompoundCriticalSpeedAnalysis",
    "SynchroniserHalfCompoundCriticalSpeedAnalysis",
    "SynchroniserPartCompoundCriticalSpeedAnalysis",
    "SynchroniserSleeveCompoundCriticalSpeedAnalysis",
    "TorqueConverterCompoundCriticalSpeedAnalysis",
    "TorqueConverterConnectionCompoundCriticalSpeedAnalysis",
    "TorqueConverterPumpCompoundCriticalSpeedAnalysis",
    "TorqueConverterTurbineCompoundCriticalSpeedAnalysis",
    "UnbalancedMassCompoundCriticalSpeedAnalysis",
    "VirtualComponentCompoundCriticalSpeedAnalysis",
    "WormGearCompoundCriticalSpeedAnalysis",
    "WormGearMeshCompoundCriticalSpeedAnalysis",
    "WormGearSetCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearMeshCompoundCriticalSpeedAnalysis",
    "ZerolBevelGearSetCompoundCriticalSpeedAnalysis",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6674 import AbstractAssemblyCompoundCriticalSpeedAnalysis
    from ._6675 import AbstractShaftCompoundCriticalSpeedAnalysis
    from ._6676 import AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
    from ._6677 import (
        AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6678 import AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
    from ._6679 import AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6680 import AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6681 import AssemblyCompoundCriticalSpeedAnalysis
    from ._6682 import BearingCompoundCriticalSpeedAnalysis
    from ._6683 import BeltConnectionCompoundCriticalSpeedAnalysis
    from ._6684 import BeltDriveCompoundCriticalSpeedAnalysis
    from ._6685 import BevelDifferentialGearCompoundCriticalSpeedAnalysis
    from ._6686 import BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
    from ._6687 import BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
    from ._6688 import BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
    from ._6689 import BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
    from ._6690 import BevelGearCompoundCriticalSpeedAnalysis
    from ._6691 import BevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6692 import BevelGearSetCompoundCriticalSpeedAnalysis
    from ._6693 import BoltCompoundCriticalSpeedAnalysis
    from ._6694 import BoltedJointCompoundCriticalSpeedAnalysis
    from ._6695 import ClutchCompoundCriticalSpeedAnalysis
    from ._6696 import ClutchConnectionCompoundCriticalSpeedAnalysis
    from ._6697 import ClutchHalfCompoundCriticalSpeedAnalysis
    from ._6698 import CoaxialConnectionCompoundCriticalSpeedAnalysis
    from ._6699 import ComponentCompoundCriticalSpeedAnalysis
    from ._6700 import ConceptCouplingCompoundCriticalSpeedAnalysis
    from ._6701 import ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6702 import ConceptCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6703 import ConceptGearCompoundCriticalSpeedAnalysis
    from ._6704 import ConceptGearMeshCompoundCriticalSpeedAnalysis
    from ._6705 import ConceptGearSetCompoundCriticalSpeedAnalysis
    from ._6706 import ConicalGearCompoundCriticalSpeedAnalysis
    from ._6707 import ConicalGearMeshCompoundCriticalSpeedAnalysis
    from ._6708 import ConicalGearSetCompoundCriticalSpeedAnalysis
    from ._6709 import ConnectionCompoundCriticalSpeedAnalysis
    from ._6710 import ConnectorCompoundCriticalSpeedAnalysis
    from ._6711 import CouplingCompoundCriticalSpeedAnalysis
    from ._6712 import CouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6713 import CouplingHalfCompoundCriticalSpeedAnalysis
    from ._6714 import CVTBeltConnectionCompoundCriticalSpeedAnalysis
    from ._6715 import CVTCompoundCriticalSpeedAnalysis
    from ._6716 import CVTPulleyCompoundCriticalSpeedAnalysis
    from ._6717 import CycloidalAssemblyCompoundCriticalSpeedAnalysis
    from ._6718 import (
        CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6719 import CycloidalDiscCompoundCriticalSpeedAnalysis
    from ._6720 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis,
    )
    from ._6721 import CylindricalGearCompoundCriticalSpeedAnalysis
    from ._6722 import CylindricalGearMeshCompoundCriticalSpeedAnalysis
    from ._6723 import CylindricalGearSetCompoundCriticalSpeedAnalysis
    from ._6724 import CylindricalPlanetGearCompoundCriticalSpeedAnalysis
    from ._6725 import DatumCompoundCriticalSpeedAnalysis
    from ._6726 import ExternalCADModelCompoundCriticalSpeedAnalysis
    from ._6727 import FaceGearCompoundCriticalSpeedAnalysis
    from ._6728 import FaceGearMeshCompoundCriticalSpeedAnalysis
    from ._6729 import FaceGearSetCompoundCriticalSpeedAnalysis
    from ._6730 import FEPartCompoundCriticalSpeedAnalysis
    from ._6731 import FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
    from ._6732 import GearCompoundCriticalSpeedAnalysis
    from ._6733 import GearMeshCompoundCriticalSpeedAnalysis
    from ._6734 import GearSetCompoundCriticalSpeedAnalysis
    from ._6735 import GuideDxfModelCompoundCriticalSpeedAnalysis
    from ._6736 import HypoidGearCompoundCriticalSpeedAnalysis
    from ._6737 import HypoidGearMeshCompoundCriticalSpeedAnalysis
    from ._6738 import HypoidGearSetCompoundCriticalSpeedAnalysis
    from ._6739 import InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6740 import KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
    from ._6741 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6742 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6743 import KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
    from ._6744 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6745 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6746 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis,
    )
    from ._6747 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis,
    )
    from ._6748 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis,
    )
    from ._6749 import MassDiscCompoundCriticalSpeedAnalysis
    from ._6750 import MeasurementComponentCompoundCriticalSpeedAnalysis
    from ._6751 import MountableComponentCompoundCriticalSpeedAnalysis
    from ._6752 import OilSealCompoundCriticalSpeedAnalysis
    from ._6753 import PartCompoundCriticalSpeedAnalysis
    from ._6754 import PartToPartShearCouplingCompoundCriticalSpeedAnalysis
    from ._6755 import PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
    from ._6756 import PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
    from ._6757 import PlanetaryConnectionCompoundCriticalSpeedAnalysis
    from ._6758 import PlanetaryGearSetCompoundCriticalSpeedAnalysis
    from ._6759 import PlanetCarrierCompoundCriticalSpeedAnalysis
    from ._6760 import PointLoadCompoundCriticalSpeedAnalysis
    from ._6761 import PowerLoadCompoundCriticalSpeedAnalysis
    from ._6762 import PulleyCompoundCriticalSpeedAnalysis
    from ._6763 import RingPinsCompoundCriticalSpeedAnalysis
    from ._6764 import RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
    from ._6765 import RollingRingAssemblyCompoundCriticalSpeedAnalysis
    from ._6766 import RollingRingCompoundCriticalSpeedAnalysis
    from ._6767 import RollingRingConnectionCompoundCriticalSpeedAnalysis
    from ._6768 import RootAssemblyCompoundCriticalSpeedAnalysis
    from ._6769 import ShaftCompoundCriticalSpeedAnalysis
    from ._6770 import ShaftHubConnectionCompoundCriticalSpeedAnalysis
    from ._6771 import ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis
    from ._6772 import SpecialisedAssemblyCompoundCriticalSpeedAnalysis
    from ._6773 import SpiralBevelGearCompoundCriticalSpeedAnalysis
    from ._6774 import SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6775 import SpiralBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6776 import SpringDamperCompoundCriticalSpeedAnalysis
    from ._6777 import SpringDamperConnectionCompoundCriticalSpeedAnalysis
    from ._6778 import SpringDamperHalfCompoundCriticalSpeedAnalysis
    from ._6779 import StraightBevelDiffGearCompoundCriticalSpeedAnalysis
    from ._6780 import StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
    from ._6781 import StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
    from ._6782 import StraightBevelGearCompoundCriticalSpeedAnalysis
    from ._6783 import StraightBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6784 import StraightBevelGearSetCompoundCriticalSpeedAnalysis
    from ._6785 import StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
    from ._6786 import StraightBevelSunGearCompoundCriticalSpeedAnalysis
    from ._6787 import SynchroniserCompoundCriticalSpeedAnalysis
    from ._6788 import SynchroniserHalfCompoundCriticalSpeedAnalysis
    from ._6789 import SynchroniserPartCompoundCriticalSpeedAnalysis
    from ._6790 import SynchroniserSleeveCompoundCriticalSpeedAnalysis
    from ._6791 import TorqueConverterCompoundCriticalSpeedAnalysis
    from ._6792 import TorqueConverterConnectionCompoundCriticalSpeedAnalysis
    from ._6793 import TorqueConverterPumpCompoundCriticalSpeedAnalysis
    from ._6794 import TorqueConverterTurbineCompoundCriticalSpeedAnalysis
    from ._6795 import UnbalancedMassCompoundCriticalSpeedAnalysis
    from ._6796 import VirtualComponentCompoundCriticalSpeedAnalysis
    from ._6797 import WormGearCompoundCriticalSpeedAnalysis
    from ._6798 import WormGearMeshCompoundCriticalSpeedAnalysis
    from ._6799 import WormGearSetCompoundCriticalSpeedAnalysis
    from ._6800 import ZerolBevelGearCompoundCriticalSpeedAnalysis
    from ._6801 import ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
    from ._6802 import ZerolBevelGearSetCompoundCriticalSpeedAnalysis
else:
    import_structure = {
        "_6674": ["AbstractAssemblyCompoundCriticalSpeedAnalysis"],
        "_6675": ["AbstractShaftCompoundCriticalSpeedAnalysis"],
        "_6676": ["AbstractShaftOrHousingCompoundCriticalSpeedAnalysis"],
        "_6677": [
            "AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6678": ["AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis"],
        "_6679": ["AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6680": ["AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6681": ["AssemblyCompoundCriticalSpeedAnalysis"],
        "_6682": ["BearingCompoundCriticalSpeedAnalysis"],
        "_6683": ["BeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6684": ["BeltDriveCompoundCriticalSpeedAnalysis"],
        "_6685": ["BevelDifferentialGearCompoundCriticalSpeedAnalysis"],
        "_6686": ["BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis"],
        "_6687": ["BevelDifferentialGearSetCompoundCriticalSpeedAnalysis"],
        "_6688": ["BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6689": ["BevelDifferentialSunGearCompoundCriticalSpeedAnalysis"],
        "_6690": ["BevelGearCompoundCriticalSpeedAnalysis"],
        "_6691": ["BevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6692": ["BevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6693": ["BoltCompoundCriticalSpeedAnalysis"],
        "_6694": ["BoltedJointCompoundCriticalSpeedAnalysis"],
        "_6695": ["ClutchCompoundCriticalSpeedAnalysis"],
        "_6696": ["ClutchConnectionCompoundCriticalSpeedAnalysis"],
        "_6697": ["ClutchHalfCompoundCriticalSpeedAnalysis"],
        "_6698": ["CoaxialConnectionCompoundCriticalSpeedAnalysis"],
        "_6699": ["ComponentCompoundCriticalSpeedAnalysis"],
        "_6700": ["ConceptCouplingCompoundCriticalSpeedAnalysis"],
        "_6701": ["ConceptCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6702": ["ConceptCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6703": ["ConceptGearCompoundCriticalSpeedAnalysis"],
        "_6704": ["ConceptGearMeshCompoundCriticalSpeedAnalysis"],
        "_6705": ["ConceptGearSetCompoundCriticalSpeedAnalysis"],
        "_6706": ["ConicalGearCompoundCriticalSpeedAnalysis"],
        "_6707": ["ConicalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6708": ["ConicalGearSetCompoundCriticalSpeedAnalysis"],
        "_6709": ["ConnectionCompoundCriticalSpeedAnalysis"],
        "_6710": ["ConnectorCompoundCriticalSpeedAnalysis"],
        "_6711": ["CouplingCompoundCriticalSpeedAnalysis"],
        "_6712": ["CouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6713": ["CouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6714": ["CVTBeltConnectionCompoundCriticalSpeedAnalysis"],
        "_6715": ["CVTCompoundCriticalSpeedAnalysis"],
        "_6716": ["CVTPulleyCompoundCriticalSpeedAnalysis"],
        "_6717": ["CycloidalAssemblyCompoundCriticalSpeedAnalysis"],
        "_6718": ["CycloidalDiscCentralBearingConnectionCompoundCriticalSpeedAnalysis"],
        "_6719": ["CycloidalDiscCompoundCriticalSpeedAnalysis"],
        "_6720": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis"
        ],
        "_6721": ["CylindricalGearCompoundCriticalSpeedAnalysis"],
        "_6722": ["CylindricalGearMeshCompoundCriticalSpeedAnalysis"],
        "_6723": ["CylindricalGearSetCompoundCriticalSpeedAnalysis"],
        "_6724": ["CylindricalPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6725": ["DatumCompoundCriticalSpeedAnalysis"],
        "_6726": ["ExternalCADModelCompoundCriticalSpeedAnalysis"],
        "_6727": ["FaceGearCompoundCriticalSpeedAnalysis"],
        "_6728": ["FaceGearMeshCompoundCriticalSpeedAnalysis"],
        "_6729": ["FaceGearSetCompoundCriticalSpeedAnalysis"],
        "_6730": ["FEPartCompoundCriticalSpeedAnalysis"],
        "_6731": ["FlexiblePinAssemblyCompoundCriticalSpeedAnalysis"],
        "_6732": ["GearCompoundCriticalSpeedAnalysis"],
        "_6733": ["GearMeshCompoundCriticalSpeedAnalysis"],
        "_6734": ["GearSetCompoundCriticalSpeedAnalysis"],
        "_6735": ["GuideDxfModelCompoundCriticalSpeedAnalysis"],
        "_6736": ["HypoidGearCompoundCriticalSpeedAnalysis"],
        "_6737": ["HypoidGearMeshCompoundCriticalSpeedAnalysis"],
        "_6738": ["HypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6739": ["InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6740": ["KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis"],
        "_6741": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6742": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6743": ["KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis"],
        "_6744": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6745": ["KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis"],
        "_6746": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ],
        "_6747": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis"
        ],
        "_6748": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
        ],
        "_6749": ["MassDiscCompoundCriticalSpeedAnalysis"],
        "_6750": ["MeasurementComponentCompoundCriticalSpeedAnalysis"],
        "_6751": ["MountableComponentCompoundCriticalSpeedAnalysis"],
        "_6752": ["OilSealCompoundCriticalSpeedAnalysis"],
        "_6753": ["PartCompoundCriticalSpeedAnalysis"],
        "_6754": ["PartToPartShearCouplingCompoundCriticalSpeedAnalysis"],
        "_6755": ["PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis"],
        "_6756": ["PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis"],
        "_6757": ["PlanetaryConnectionCompoundCriticalSpeedAnalysis"],
        "_6758": ["PlanetaryGearSetCompoundCriticalSpeedAnalysis"],
        "_6759": ["PlanetCarrierCompoundCriticalSpeedAnalysis"],
        "_6760": ["PointLoadCompoundCriticalSpeedAnalysis"],
        "_6761": ["PowerLoadCompoundCriticalSpeedAnalysis"],
        "_6762": ["PulleyCompoundCriticalSpeedAnalysis"],
        "_6763": ["RingPinsCompoundCriticalSpeedAnalysis"],
        "_6764": ["RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis"],
        "_6765": ["RollingRingAssemblyCompoundCriticalSpeedAnalysis"],
        "_6766": ["RollingRingCompoundCriticalSpeedAnalysis"],
        "_6767": ["RollingRingConnectionCompoundCriticalSpeedAnalysis"],
        "_6768": ["RootAssemblyCompoundCriticalSpeedAnalysis"],
        "_6769": ["ShaftCompoundCriticalSpeedAnalysis"],
        "_6770": ["ShaftHubConnectionCompoundCriticalSpeedAnalysis"],
        "_6771": ["ShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis"],
        "_6772": ["SpecialisedAssemblyCompoundCriticalSpeedAnalysis"],
        "_6773": ["SpiralBevelGearCompoundCriticalSpeedAnalysis"],
        "_6774": ["SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6775": ["SpiralBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6776": ["SpringDamperCompoundCriticalSpeedAnalysis"],
        "_6777": ["SpringDamperConnectionCompoundCriticalSpeedAnalysis"],
        "_6778": ["SpringDamperHalfCompoundCriticalSpeedAnalysis"],
        "_6779": ["StraightBevelDiffGearCompoundCriticalSpeedAnalysis"],
        "_6780": ["StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis"],
        "_6781": ["StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis"],
        "_6782": ["StraightBevelGearCompoundCriticalSpeedAnalysis"],
        "_6783": ["StraightBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6784": ["StraightBevelGearSetCompoundCriticalSpeedAnalysis"],
        "_6785": ["StraightBevelPlanetGearCompoundCriticalSpeedAnalysis"],
        "_6786": ["StraightBevelSunGearCompoundCriticalSpeedAnalysis"],
        "_6787": ["SynchroniserCompoundCriticalSpeedAnalysis"],
        "_6788": ["SynchroniserHalfCompoundCriticalSpeedAnalysis"],
        "_6789": ["SynchroniserPartCompoundCriticalSpeedAnalysis"],
        "_6790": ["SynchroniserSleeveCompoundCriticalSpeedAnalysis"],
        "_6791": ["TorqueConverterCompoundCriticalSpeedAnalysis"],
        "_6792": ["TorqueConverterConnectionCompoundCriticalSpeedAnalysis"],
        "_6793": ["TorqueConverterPumpCompoundCriticalSpeedAnalysis"],
        "_6794": ["TorqueConverterTurbineCompoundCriticalSpeedAnalysis"],
        "_6795": ["UnbalancedMassCompoundCriticalSpeedAnalysis"],
        "_6796": ["VirtualComponentCompoundCriticalSpeedAnalysis"],
        "_6797": ["WormGearCompoundCriticalSpeedAnalysis"],
        "_6798": ["WormGearMeshCompoundCriticalSpeedAnalysis"],
        "_6799": ["WormGearSetCompoundCriticalSpeedAnalysis"],
        "_6800": ["ZerolBevelGearCompoundCriticalSpeedAnalysis"],
        "_6801": ["ZerolBevelGearMeshCompoundCriticalSpeedAnalysis"],
        "_6802": ["ZerolBevelGearSetCompoundCriticalSpeedAnalysis"],
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

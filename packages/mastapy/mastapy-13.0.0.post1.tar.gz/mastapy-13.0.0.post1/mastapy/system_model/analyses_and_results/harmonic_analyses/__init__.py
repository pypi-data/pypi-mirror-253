"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5677 import AbstractAssemblyHarmonicAnalysis
    from ._5678 import AbstractPeriodicExcitationDetail
    from ._5679 import AbstractShaftHarmonicAnalysis
    from ._5680 import AbstractShaftOrHousingHarmonicAnalysis
    from ._5681 import AbstractShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5682 import AGMAGleasonConicalGearHarmonicAnalysis
    from ._5683 import AGMAGleasonConicalGearMeshHarmonicAnalysis
    from ._5684 import AGMAGleasonConicalGearSetHarmonicAnalysis
    from ._5685 import AssemblyHarmonicAnalysis
    from ._5686 import BearingHarmonicAnalysis
    from ._5687 import BeltConnectionHarmonicAnalysis
    from ._5688 import BeltDriveHarmonicAnalysis
    from ._5689 import BevelDifferentialGearHarmonicAnalysis
    from ._5690 import BevelDifferentialGearMeshHarmonicAnalysis
    from ._5691 import BevelDifferentialGearSetHarmonicAnalysis
    from ._5692 import BevelDifferentialPlanetGearHarmonicAnalysis
    from ._5693 import BevelDifferentialSunGearHarmonicAnalysis
    from ._5694 import BevelGearHarmonicAnalysis
    from ._5695 import BevelGearMeshHarmonicAnalysis
    from ._5696 import BevelGearSetHarmonicAnalysis
    from ._5697 import BoltedJointHarmonicAnalysis
    from ._5698 import BoltHarmonicAnalysis
    from ._5699 import ClutchConnectionHarmonicAnalysis
    from ._5700 import ClutchHalfHarmonicAnalysis
    from ._5701 import ClutchHarmonicAnalysis
    from ._5702 import CoaxialConnectionHarmonicAnalysis
    from ._5703 import ComplianceAndForceData
    from ._5704 import ComponentHarmonicAnalysis
    from ._5705 import ConceptCouplingConnectionHarmonicAnalysis
    from ._5706 import ConceptCouplingHalfHarmonicAnalysis
    from ._5707 import ConceptCouplingHarmonicAnalysis
    from ._5708 import ConceptGearHarmonicAnalysis
    from ._5709 import ConceptGearMeshHarmonicAnalysis
    from ._5710 import ConceptGearSetHarmonicAnalysis
    from ._5711 import ConicalGearHarmonicAnalysis
    from ._5712 import ConicalGearMeshHarmonicAnalysis
    from ._5713 import ConicalGearSetHarmonicAnalysis
    from ._5714 import ConnectionHarmonicAnalysis
    from ._5715 import ConnectorHarmonicAnalysis
    from ._5716 import CouplingConnectionHarmonicAnalysis
    from ._5717 import CouplingHalfHarmonicAnalysis
    from ._5718 import CouplingHarmonicAnalysis
    from ._5719 import CVTBeltConnectionHarmonicAnalysis
    from ._5720 import CVTHarmonicAnalysis
    from ._5721 import CVTPulleyHarmonicAnalysis
    from ._5722 import CycloidalAssemblyHarmonicAnalysis
    from ._5723 import CycloidalDiscCentralBearingConnectionHarmonicAnalysis
    from ._5724 import CycloidalDiscHarmonicAnalysis
    from ._5725 import CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
    from ._5726 import CylindricalGearHarmonicAnalysis
    from ._5727 import CylindricalGearMeshHarmonicAnalysis
    from ._5728 import CylindricalGearSetHarmonicAnalysis
    from ._5729 import CylindricalPlanetGearHarmonicAnalysis
    from ._5730 import DatumHarmonicAnalysis
    from ._5731 import DynamicModelForHarmonicAnalysis
    from ._5732 import ElectricMachinePeriodicExcitationDetail
    from ._5733 import ElectricMachineRotorXForcePeriodicExcitationDetail
    from ._5734 import ElectricMachineRotorXMomentPeriodicExcitationDetail
    from ._5735 import ElectricMachineRotorYForcePeriodicExcitationDetail
    from ._5736 import ElectricMachineRotorYMomentPeriodicExcitationDetail
    from ._5737 import ElectricMachineRotorZForcePeriodicExcitationDetail
    from ._5738 import ElectricMachineStatorToothAxialLoadsExcitationDetail
    from ._5739 import ElectricMachineStatorToothLoadsExcitationDetail
    from ._5740 import ElectricMachineStatorToothMomentsExcitationDetail
    from ._5741 import ElectricMachineStatorToothRadialLoadsExcitationDetail
    from ._5742 import ElectricMachineStatorToothTangentialLoadsExcitationDetail
    from ._5743 import ElectricMachineTorqueRipplePeriodicExcitationDetail
    from ._5744 import ExportOutputType
    from ._5745 import ExternalCADModelHarmonicAnalysis
    from ._5746 import FaceGearHarmonicAnalysis
    from ._5747 import FaceGearMeshHarmonicAnalysis
    from ._5748 import FaceGearSetHarmonicAnalysis
    from ._5749 import FEPartHarmonicAnalysis
    from ._5750 import FlexiblePinAssemblyHarmonicAnalysis
    from ._5751 import FrequencyOptionsForHarmonicAnalysisResults
    from ._5752 import GearHarmonicAnalysis
    from ._5753 import GearMeshExcitationDetail
    from ._5754 import GearMeshHarmonicAnalysis
    from ._5755 import GearMeshMisalignmentExcitationDetail
    from ._5756 import GearMeshTEExcitationDetail
    from ._5757 import GearSetHarmonicAnalysis
    from ._5758 import GeneralPeriodicExcitationDetail
    from ._5759 import GuideDxfModelHarmonicAnalysis
    from ._5760 import HarmonicAnalysis
    from ._5761 import HarmonicAnalysisDrawStyle
    from ._5762 import HarmonicAnalysisExportOptions
    from ._5763 import HarmonicAnalysisFEExportOptions
    from ._5764 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._5765 import HarmonicAnalysisOptions
    from ._5766 import HarmonicAnalysisRootAssemblyExportOptions
    from ._5767 import HarmonicAnalysisShaftExportOptions
    from ._5768 import HarmonicAnalysisTorqueInputType
    from ._5769 import HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
    from ._5770 import HypoidGearHarmonicAnalysis
    from ._5771 import HypoidGearMeshHarmonicAnalysis
    from ._5772 import HypoidGearSetHarmonicAnalysis
    from ._5773 import InterMountableComponentConnectionHarmonicAnalysis
    from ._5774 import KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
    from ._5775 import KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
    from ._5776 import KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
    from ._5777 import KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
    from ._5778 import KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
    from ._5779 import KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
    from ._5780 import KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
    from ._5781 import KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
    from ._5782 import KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
    from ._5783 import MassDiscHarmonicAnalysis
    from ._5784 import MeasurementComponentHarmonicAnalysis
    from ._5785 import MountableComponentHarmonicAnalysis
    from ._5786 import OilSealHarmonicAnalysis
    from ._5787 import PartHarmonicAnalysis
    from ._5788 import PartToPartShearCouplingConnectionHarmonicAnalysis
    from ._5789 import PartToPartShearCouplingHalfHarmonicAnalysis
    from ._5790 import PartToPartShearCouplingHarmonicAnalysis
    from ._5791 import PeriodicExcitationWithReferenceShaft
    from ._5792 import PlanetaryConnectionHarmonicAnalysis
    from ._5793 import PlanetaryGearSetHarmonicAnalysis
    from ._5794 import PlanetCarrierHarmonicAnalysis
    from ._5795 import PointLoadHarmonicAnalysis
    from ._5796 import PowerLoadHarmonicAnalysis
    from ._5797 import PulleyHarmonicAnalysis
    from ._5798 import ResponseCacheLevel
    from ._5799 import RingPinsHarmonicAnalysis
    from ._5800 import RingPinsToDiscConnectionHarmonicAnalysis
    from ._5801 import RollingRingAssemblyHarmonicAnalysis
    from ._5802 import RollingRingConnectionHarmonicAnalysis
    from ._5803 import RollingRingHarmonicAnalysis
    from ._5804 import RootAssemblyHarmonicAnalysis
    from ._5805 import ShaftHarmonicAnalysis
    from ._5806 import ShaftHubConnectionHarmonicAnalysis
    from ._5807 import ShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5808 import SingleNodePeriodicExcitationWithReferenceShaft
    from ._5809 import SpecialisedAssemblyHarmonicAnalysis
    from ._5810 import SpeedOptionsForHarmonicAnalysisResults
    from ._5811 import SpiralBevelGearHarmonicAnalysis
    from ._5812 import SpiralBevelGearMeshHarmonicAnalysis
    from ._5813 import SpiralBevelGearSetHarmonicAnalysis
    from ._5814 import SpringDamperConnectionHarmonicAnalysis
    from ._5815 import SpringDamperHalfHarmonicAnalysis
    from ._5816 import SpringDamperHarmonicAnalysis
    from ._5817 import StiffnessOptionsForHarmonicAnalysis
    from ._5818 import StraightBevelDiffGearHarmonicAnalysis
    from ._5819 import StraightBevelDiffGearMeshHarmonicAnalysis
    from ._5820 import StraightBevelDiffGearSetHarmonicAnalysis
    from ._5821 import StraightBevelGearHarmonicAnalysis
    from ._5822 import StraightBevelGearMeshHarmonicAnalysis
    from ._5823 import StraightBevelGearSetHarmonicAnalysis
    from ._5824 import StraightBevelPlanetGearHarmonicAnalysis
    from ._5825 import StraightBevelSunGearHarmonicAnalysis
    from ._5826 import SynchroniserHalfHarmonicAnalysis
    from ._5827 import SynchroniserHarmonicAnalysis
    from ._5828 import SynchroniserPartHarmonicAnalysis
    from ._5829 import SynchroniserSleeveHarmonicAnalysis
    from ._5830 import TorqueConverterConnectionHarmonicAnalysis
    from ._5831 import TorqueConverterHarmonicAnalysis
    from ._5832 import TorqueConverterPumpHarmonicAnalysis
    from ._5833 import TorqueConverterTurbineHarmonicAnalysis
    from ._5834 import UnbalancedMassExcitationDetail
    from ._5835 import UnbalancedMassHarmonicAnalysis
    from ._5836 import VirtualComponentHarmonicAnalysis
    from ._5837 import WormGearHarmonicAnalysis
    from ._5838 import WormGearMeshHarmonicAnalysis
    from ._5839 import WormGearSetHarmonicAnalysis
    from ._5840 import ZerolBevelGearHarmonicAnalysis
    from ._5841 import ZerolBevelGearMeshHarmonicAnalysis
    from ._5842 import ZerolBevelGearSetHarmonicAnalysis
else:
    import_structure = {
        "_5677": ["AbstractAssemblyHarmonicAnalysis"],
        "_5678": ["AbstractPeriodicExcitationDetail"],
        "_5679": ["AbstractShaftHarmonicAnalysis"],
        "_5680": ["AbstractShaftOrHousingHarmonicAnalysis"],
        "_5681": ["AbstractShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5682": ["AGMAGleasonConicalGearHarmonicAnalysis"],
        "_5683": ["AGMAGleasonConicalGearMeshHarmonicAnalysis"],
        "_5684": ["AGMAGleasonConicalGearSetHarmonicAnalysis"],
        "_5685": ["AssemblyHarmonicAnalysis"],
        "_5686": ["BearingHarmonicAnalysis"],
        "_5687": ["BeltConnectionHarmonicAnalysis"],
        "_5688": ["BeltDriveHarmonicAnalysis"],
        "_5689": ["BevelDifferentialGearHarmonicAnalysis"],
        "_5690": ["BevelDifferentialGearMeshHarmonicAnalysis"],
        "_5691": ["BevelDifferentialGearSetHarmonicAnalysis"],
        "_5692": ["BevelDifferentialPlanetGearHarmonicAnalysis"],
        "_5693": ["BevelDifferentialSunGearHarmonicAnalysis"],
        "_5694": ["BevelGearHarmonicAnalysis"],
        "_5695": ["BevelGearMeshHarmonicAnalysis"],
        "_5696": ["BevelGearSetHarmonicAnalysis"],
        "_5697": ["BoltedJointHarmonicAnalysis"],
        "_5698": ["BoltHarmonicAnalysis"],
        "_5699": ["ClutchConnectionHarmonicAnalysis"],
        "_5700": ["ClutchHalfHarmonicAnalysis"],
        "_5701": ["ClutchHarmonicAnalysis"],
        "_5702": ["CoaxialConnectionHarmonicAnalysis"],
        "_5703": ["ComplianceAndForceData"],
        "_5704": ["ComponentHarmonicAnalysis"],
        "_5705": ["ConceptCouplingConnectionHarmonicAnalysis"],
        "_5706": ["ConceptCouplingHalfHarmonicAnalysis"],
        "_5707": ["ConceptCouplingHarmonicAnalysis"],
        "_5708": ["ConceptGearHarmonicAnalysis"],
        "_5709": ["ConceptGearMeshHarmonicAnalysis"],
        "_5710": ["ConceptGearSetHarmonicAnalysis"],
        "_5711": ["ConicalGearHarmonicAnalysis"],
        "_5712": ["ConicalGearMeshHarmonicAnalysis"],
        "_5713": ["ConicalGearSetHarmonicAnalysis"],
        "_5714": ["ConnectionHarmonicAnalysis"],
        "_5715": ["ConnectorHarmonicAnalysis"],
        "_5716": ["CouplingConnectionHarmonicAnalysis"],
        "_5717": ["CouplingHalfHarmonicAnalysis"],
        "_5718": ["CouplingHarmonicAnalysis"],
        "_5719": ["CVTBeltConnectionHarmonicAnalysis"],
        "_5720": ["CVTHarmonicAnalysis"],
        "_5721": ["CVTPulleyHarmonicAnalysis"],
        "_5722": ["CycloidalAssemblyHarmonicAnalysis"],
        "_5723": ["CycloidalDiscCentralBearingConnectionHarmonicAnalysis"],
        "_5724": ["CycloidalDiscHarmonicAnalysis"],
        "_5725": ["CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis"],
        "_5726": ["CylindricalGearHarmonicAnalysis"],
        "_5727": ["CylindricalGearMeshHarmonicAnalysis"],
        "_5728": ["CylindricalGearSetHarmonicAnalysis"],
        "_5729": ["CylindricalPlanetGearHarmonicAnalysis"],
        "_5730": ["DatumHarmonicAnalysis"],
        "_5731": ["DynamicModelForHarmonicAnalysis"],
        "_5732": ["ElectricMachinePeriodicExcitationDetail"],
        "_5733": ["ElectricMachineRotorXForcePeriodicExcitationDetail"],
        "_5734": ["ElectricMachineRotorXMomentPeriodicExcitationDetail"],
        "_5735": ["ElectricMachineRotorYForcePeriodicExcitationDetail"],
        "_5736": ["ElectricMachineRotorYMomentPeriodicExcitationDetail"],
        "_5737": ["ElectricMachineRotorZForcePeriodicExcitationDetail"],
        "_5738": ["ElectricMachineStatorToothAxialLoadsExcitationDetail"],
        "_5739": ["ElectricMachineStatorToothLoadsExcitationDetail"],
        "_5740": ["ElectricMachineStatorToothMomentsExcitationDetail"],
        "_5741": ["ElectricMachineStatorToothRadialLoadsExcitationDetail"],
        "_5742": ["ElectricMachineStatorToothTangentialLoadsExcitationDetail"],
        "_5743": ["ElectricMachineTorqueRipplePeriodicExcitationDetail"],
        "_5744": ["ExportOutputType"],
        "_5745": ["ExternalCADModelHarmonicAnalysis"],
        "_5746": ["FaceGearHarmonicAnalysis"],
        "_5747": ["FaceGearMeshHarmonicAnalysis"],
        "_5748": ["FaceGearSetHarmonicAnalysis"],
        "_5749": ["FEPartHarmonicAnalysis"],
        "_5750": ["FlexiblePinAssemblyHarmonicAnalysis"],
        "_5751": ["FrequencyOptionsForHarmonicAnalysisResults"],
        "_5752": ["GearHarmonicAnalysis"],
        "_5753": ["GearMeshExcitationDetail"],
        "_5754": ["GearMeshHarmonicAnalysis"],
        "_5755": ["GearMeshMisalignmentExcitationDetail"],
        "_5756": ["GearMeshTEExcitationDetail"],
        "_5757": ["GearSetHarmonicAnalysis"],
        "_5758": ["GeneralPeriodicExcitationDetail"],
        "_5759": ["GuideDxfModelHarmonicAnalysis"],
        "_5760": ["HarmonicAnalysis"],
        "_5761": ["HarmonicAnalysisDrawStyle"],
        "_5762": ["HarmonicAnalysisExportOptions"],
        "_5763": ["HarmonicAnalysisFEExportOptions"],
        "_5764": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_5765": ["HarmonicAnalysisOptions"],
        "_5766": ["HarmonicAnalysisRootAssemblyExportOptions"],
        "_5767": ["HarmonicAnalysisShaftExportOptions"],
        "_5768": ["HarmonicAnalysisTorqueInputType"],
        "_5769": ["HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"],
        "_5770": ["HypoidGearHarmonicAnalysis"],
        "_5771": ["HypoidGearMeshHarmonicAnalysis"],
        "_5772": ["HypoidGearSetHarmonicAnalysis"],
        "_5773": ["InterMountableComponentConnectionHarmonicAnalysis"],
        "_5774": ["KlingelnbergCycloPalloidConicalGearHarmonicAnalysis"],
        "_5775": ["KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis"],
        "_5776": ["KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis"],
        "_5777": ["KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis"],
        "_5778": ["KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis"],
        "_5779": ["KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis"],
        "_5780": ["KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis"],
        "_5781": ["KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis"],
        "_5782": ["KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis"],
        "_5783": ["MassDiscHarmonicAnalysis"],
        "_5784": ["MeasurementComponentHarmonicAnalysis"],
        "_5785": ["MountableComponentHarmonicAnalysis"],
        "_5786": ["OilSealHarmonicAnalysis"],
        "_5787": ["PartHarmonicAnalysis"],
        "_5788": ["PartToPartShearCouplingConnectionHarmonicAnalysis"],
        "_5789": ["PartToPartShearCouplingHalfHarmonicAnalysis"],
        "_5790": ["PartToPartShearCouplingHarmonicAnalysis"],
        "_5791": ["PeriodicExcitationWithReferenceShaft"],
        "_5792": ["PlanetaryConnectionHarmonicAnalysis"],
        "_5793": ["PlanetaryGearSetHarmonicAnalysis"],
        "_5794": ["PlanetCarrierHarmonicAnalysis"],
        "_5795": ["PointLoadHarmonicAnalysis"],
        "_5796": ["PowerLoadHarmonicAnalysis"],
        "_5797": ["PulleyHarmonicAnalysis"],
        "_5798": ["ResponseCacheLevel"],
        "_5799": ["RingPinsHarmonicAnalysis"],
        "_5800": ["RingPinsToDiscConnectionHarmonicAnalysis"],
        "_5801": ["RollingRingAssemblyHarmonicAnalysis"],
        "_5802": ["RollingRingConnectionHarmonicAnalysis"],
        "_5803": ["RollingRingHarmonicAnalysis"],
        "_5804": ["RootAssemblyHarmonicAnalysis"],
        "_5805": ["ShaftHarmonicAnalysis"],
        "_5806": ["ShaftHubConnectionHarmonicAnalysis"],
        "_5807": ["ShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5808": ["SingleNodePeriodicExcitationWithReferenceShaft"],
        "_5809": ["SpecialisedAssemblyHarmonicAnalysis"],
        "_5810": ["SpeedOptionsForHarmonicAnalysisResults"],
        "_5811": ["SpiralBevelGearHarmonicAnalysis"],
        "_5812": ["SpiralBevelGearMeshHarmonicAnalysis"],
        "_5813": ["SpiralBevelGearSetHarmonicAnalysis"],
        "_5814": ["SpringDamperConnectionHarmonicAnalysis"],
        "_5815": ["SpringDamperHalfHarmonicAnalysis"],
        "_5816": ["SpringDamperHarmonicAnalysis"],
        "_5817": ["StiffnessOptionsForHarmonicAnalysis"],
        "_5818": ["StraightBevelDiffGearHarmonicAnalysis"],
        "_5819": ["StraightBevelDiffGearMeshHarmonicAnalysis"],
        "_5820": ["StraightBevelDiffGearSetHarmonicAnalysis"],
        "_5821": ["StraightBevelGearHarmonicAnalysis"],
        "_5822": ["StraightBevelGearMeshHarmonicAnalysis"],
        "_5823": ["StraightBevelGearSetHarmonicAnalysis"],
        "_5824": ["StraightBevelPlanetGearHarmonicAnalysis"],
        "_5825": ["StraightBevelSunGearHarmonicAnalysis"],
        "_5826": ["SynchroniserHalfHarmonicAnalysis"],
        "_5827": ["SynchroniserHarmonicAnalysis"],
        "_5828": ["SynchroniserPartHarmonicAnalysis"],
        "_5829": ["SynchroniserSleeveHarmonicAnalysis"],
        "_5830": ["TorqueConverterConnectionHarmonicAnalysis"],
        "_5831": ["TorqueConverterHarmonicAnalysis"],
        "_5832": ["TorqueConverterPumpHarmonicAnalysis"],
        "_5833": ["TorqueConverterTurbineHarmonicAnalysis"],
        "_5834": ["UnbalancedMassExcitationDetail"],
        "_5835": ["UnbalancedMassHarmonicAnalysis"],
        "_5836": ["VirtualComponentHarmonicAnalysis"],
        "_5837": ["WormGearHarmonicAnalysis"],
        "_5838": ["WormGearMeshHarmonicAnalysis"],
        "_5839": ["WormGearSetHarmonicAnalysis"],
        "_5840": ["ZerolBevelGearHarmonicAnalysis"],
        "_5841": ["ZerolBevelGearMeshHarmonicAnalysis"],
        "_5842": ["ZerolBevelGearSetHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyHarmonicAnalysis",
    "AbstractPeriodicExcitationDetail",
    "AbstractShaftHarmonicAnalysis",
    "AbstractShaftOrHousingHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionHarmonicAnalysis",
    "AGMAGleasonConicalGearHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshHarmonicAnalysis",
    "AGMAGleasonConicalGearSetHarmonicAnalysis",
    "AssemblyHarmonicAnalysis",
    "BearingHarmonicAnalysis",
    "BeltConnectionHarmonicAnalysis",
    "BeltDriveHarmonicAnalysis",
    "BevelDifferentialGearHarmonicAnalysis",
    "BevelDifferentialGearMeshHarmonicAnalysis",
    "BevelDifferentialGearSetHarmonicAnalysis",
    "BevelDifferentialPlanetGearHarmonicAnalysis",
    "BevelDifferentialSunGearHarmonicAnalysis",
    "BevelGearHarmonicAnalysis",
    "BevelGearMeshHarmonicAnalysis",
    "BevelGearSetHarmonicAnalysis",
    "BoltedJointHarmonicAnalysis",
    "BoltHarmonicAnalysis",
    "ClutchConnectionHarmonicAnalysis",
    "ClutchHalfHarmonicAnalysis",
    "ClutchHarmonicAnalysis",
    "CoaxialConnectionHarmonicAnalysis",
    "ComplianceAndForceData",
    "ComponentHarmonicAnalysis",
    "ConceptCouplingConnectionHarmonicAnalysis",
    "ConceptCouplingHalfHarmonicAnalysis",
    "ConceptCouplingHarmonicAnalysis",
    "ConceptGearHarmonicAnalysis",
    "ConceptGearMeshHarmonicAnalysis",
    "ConceptGearSetHarmonicAnalysis",
    "ConicalGearHarmonicAnalysis",
    "ConicalGearMeshHarmonicAnalysis",
    "ConicalGearSetHarmonicAnalysis",
    "ConnectionHarmonicAnalysis",
    "ConnectorHarmonicAnalysis",
    "CouplingConnectionHarmonicAnalysis",
    "CouplingHalfHarmonicAnalysis",
    "CouplingHarmonicAnalysis",
    "CVTBeltConnectionHarmonicAnalysis",
    "CVTHarmonicAnalysis",
    "CVTPulleyHarmonicAnalysis",
    "CycloidalAssemblyHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionHarmonicAnalysis",
    "CycloidalDiscHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis",
    "CylindricalGearHarmonicAnalysis",
    "CylindricalGearMeshHarmonicAnalysis",
    "CylindricalGearSetHarmonicAnalysis",
    "CylindricalPlanetGearHarmonicAnalysis",
    "DatumHarmonicAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "ElectricMachinePeriodicExcitationDetail",
    "ElectricMachineRotorXForcePeriodicExcitationDetail",
    "ElectricMachineRotorXMomentPeriodicExcitationDetail",
    "ElectricMachineRotorYForcePeriodicExcitationDetail",
    "ElectricMachineRotorYMomentPeriodicExcitationDetail",
    "ElectricMachineRotorZForcePeriodicExcitationDetail",
    "ElectricMachineStatorToothAxialLoadsExcitationDetail",
    "ElectricMachineStatorToothLoadsExcitationDetail",
    "ElectricMachineStatorToothMomentsExcitationDetail",
    "ElectricMachineStatorToothRadialLoadsExcitationDetail",
    "ElectricMachineStatorToothTangentialLoadsExcitationDetail",
    "ElectricMachineTorqueRipplePeriodicExcitationDetail",
    "ExportOutputType",
    "ExternalCADModelHarmonicAnalysis",
    "FaceGearHarmonicAnalysis",
    "FaceGearMeshHarmonicAnalysis",
    "FaceGearSetHarmonicAnalysis",
    "FEPartHarmonicAnalysis",
    "FlexiblePinAssemblyHarmonicAnalysis",
    "FrequencyOptionsForHarmonicAnalysisResults",
    "GearHarmonicAnalysis",
    "GearMeshExcitationDetail",
    "GearMeshHarmonicAnalysis",
    "GearMeshMisalignmentExcitationDetail",
    "GearMeshTEExcitationDetail",
    "GearSetHarmonicAnalysis",
    "GeneralPeriodicExcitationDetail",
    "GuideDxfModelHarmonicAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisDrawStyle",
    "HarmonicAnalysisExportOptions",
    "HarmonicAnalysisFEExportOptions",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptions",
    "HarmonicAnalysisRootAssemblyExportOptions",
    "HarmonicAnalysisShaftExportOptions",
    "HarmonicAnalysisTorqueInputType",
    "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
    "HypoidGearHarmonicAnalysis",
    "HypoidGearMeshHarmonicAnalysis",
    "HypoidGearSetHarmonicAnalysis",
    "InterMountableComponentConnectionHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis",
    "MassDiscHarmonicAnalysis",
    "MeasurementComponentHarmonicAnalysis",
    "MountableComponentHarmonicAnalysis",
    "OilSealHarmonicAnalysis",
    "PartHarmonicAnalysis",
    "PartToPartShearCouplingConnectionHarmonicAnalysis",
    "PartToPartShearCouplingHalfHarmonicAnalysis",
    "PartToPartShearCouplingHarmonicAnalysis",
    "PeriodicExcitationWithReferenceShaft",
    "PlanetaryConnectionHarmonicAnalysis",
    "PlanetaryGearSetHarmonicAnalysis",
    "PlanetCarrierHarmonicAnalysis",
    "PointLoadHarmonicAnalysis",
    "PowerLoadHarmonicAnalysis",
    "PulleyHarmonicAnalysis",
    "ResponseCacheLevel",
    "RingPinsHarmonicAnalysis",
    "RingPinsToDiscConnectionHarmonicAnalysis",
    "RollingRingAssemblyHarmonicAnalysis",
    "RollingRingConnectionHarmonicAnalysis",
    "RollingRingHarmonicAnalysis",
    "RootAssemblyHarmonicAnalysis",
    "ShaftHarmonicAnalysis",
    "ShaftHubConnectionHarmonicAnalysis",
    "ShaftToMountableComponentConnectionHarmonicAnalysis",
    "SingleNodePeriodicExcitationWithReferenceShaft",
    "SpecialisedAssemblyHarmonicAnalysis",
    "SpeedOptionsForHarmonicAnalysisResults",
    "SpiralBevelGearHarmonicAnalysis",
    "SpiralBevelGearMeshHarmonicAnalysis",
    "SpiralBevelGearSetHarmonicAnalysis",
    "SpringDamperConnectionHarmonicAnalysis",
    "SpringDamperHalfHarmonicAnalysis",
    "SpringDamperHarmonicAnalysis",
    "StiffnessOptionsForHarmonicAnalysis",
    "StraightBevelDiffGearHarmonicAnalysis",
    "StraightBevelDiffGearMeshHarmonicAnalysis",
    "StraightBevelDiffGearSetHarmonicAnalysis",
    "StraightBevelGearHarmonicAnalysis",
    "StraightBevelGearMeshHarmonicAnalysis",
    "StraightBevelGearSetHarmonicAnalysis",
    "StraightBevelPlanetGearHarmonicAnalysis",
    "StraightBevelSunGearHarmonicAnalysis",
    "SynchroniserHalfHarmonicAnalysis",
    "SynchroniserHarmonicAnalysis",
    "SynchroniserPartHarmonicAnalysis",
    "SynchroniserSleeveHarmonicAnalysis",
    "TorqueConverterConnectionHarmonicAnalysis",
    "TorqueConverterHarmonicAnalysis",
    "TorqueConverterPumpHarmonicAnalysis",
    "TorqueConverterTurbineHarmonicAnalysis",
    "UnbalancedMassExcitationDetail",
    "UnbalancedMassHarmonicAnalysis",
    "VirtualComponentHarmonicAnalysis",
    "WormGearHarmonicAnalysis",
    "WormGearMeshHarmonicAnalysis",
    "WormGearSetHarmonicAnalysis",
    "ZerolBevelGearHarmonicAnalysis",
    "ZerolBevelGearMeshHarmonicAnalysis",
    "ZerolBevelGearSetHarmonicAnalysis",
)

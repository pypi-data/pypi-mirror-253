"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5678 import AbstractAssemblyHarmonicAnalysis
    from ._5679 import AbstractPeriodicExcitationDetail
    from ._5680 import AbstractShaftHarmonicAnalysis
    from ._5681 import AbstractShaftOrHousingHarmonicAnalysis
    from ._5682 import AbstractShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5683 import AGMAGleasonConicalGearHarmonicAnalysis
    from ._5684 import AGMAGleasonConicalGearMeshHarmonicAnalysis
    from ._5685 import AGMAGleasonConicalGearSetHarmonicAnalysis
    from ._5686 import AssemblyHarmonicAnalysis
    from ._5687 import BearingHarmonicAnalysis
    from ._5688 import BeltConnectionHarmonicAnalysis
    from ._5689 import BeltDriveHarmonicAnalysis
    from ._5690 import BevelDifferentialGearHarmonicAnalysis
    from ._5691 import BevelDifferentialGearMeshHarmonicAnalysis
    from ._5692 import BevelDifferentialGearSetHarmonicAnalysis
    from ._5693 import BevelDifferentialPlanetGearHarmonicAnalysis
    from ._5694 import BevelDifferentialSunGearHarmonicAnalysis
    from ._5695 import BevelGearHarmonicAnalysis
    from ._5696 import BevelGearMeshHarmonicAnalysis
    from ._5697 import BevelGearSetHarmonicAnalysis
    from ._5698 import BoltedJointHarmonicAnalysis
    from ._5699 import BoltHarmonicAnalysis
    from ._5700 import ClutchConnectionHarmonicAnalysis
    from ._5701 import ClutchHalfHarmonicAnalysis
    from ._5702 import ClutchHarmonicAnalysis
    from ._5703 import CoaxialConnectionHarmonicAnalysis
    from ._5704 import ComplianceAndForceData
    from ._5705 import ComponentHarmonicAnalysis
    from ._5706 import ConceptCouplingConnectionHarmonicAnalysis
    from ._5707 import ConceptCouplingHalfHarmonicAnalysis
    from ._5708 import ConceptCouplingHarmonicAnalysis
    from ._5709 import ConceptGearHarmonicAnalysis
    from ._5710 import ConceptGearMeshHarmonicAnalysis
    from ._5711 import ConceptGearSetHarmonicAnalysis
    from ._5712 import ConicalGearHarmonicAnalysis
    from ._5713 import ConicalGearMeshHarmonicAnalysis
    from ._5714 import ConicalGearSetHarmonicAnalysis
    from ._5715 import ConnectionHarmonicAnalysis
    from ._5716 import ConnectorHarmonicAnalysis
    from ._5717 import CouplingConnectionHarmonicAnalysis
    from ._5718 import CouplingHalfHarmonicAnalysis
    from ._5719 import CouplingHarmonicAnalysis
    from ._5720 import CVTBeltConnectionHarmonicAnalysis
    from ._5721 import CVTHarmonicAnalysis
    from ._5722 import CVTPulleyHarmonicAnalysis
    from ._5723 import CycloidalAssemblyHarmonicAnalysis
    from ._5724 import CycloidalDiscCentralBearingConnectionHarmonicAnalysis
    from ._5725 import CycloidalDiscHarmonicAnalysis
    from ._5726 import CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
    from ._5727 import CylindricalGearHarmonicAnalysis
    from ._5728 import CylindricalGearMeshHarmonicAnalysis
    from ._5729 import CylindricalGearSetHarmonicAnalysis
    from ._5730 import CylindricalPlanetGearHarmonicAnalysis
    from ._5731 import DatumHarmonicAnalysis
    from ._5732 import DynamicModelForHarmonicAnalysis
    from ._5733 import ElectricMachinePeriodicExcitationDetail
    from ._5734 import ElectricMachineRotorXForcePeriodicExcitationDetail
    from ._5735 import ElectricMachineRotorXMomentPeriodicExcitationDetail
    from ._5736 import ElectricMachineRotorYForcePeriodicExcitationDetail
    from ._5737 import ElectricMachineRotorYMomentPeriodicExcitationDetail
    from ._5738 import ElectricMachineRotorZForcePeriodicExcitationDetail
    from ._5739 import ElectricMachineStatorToothAxialLoadsExcitationDetail
    from ._5740 import ElectricMachineStatorToothLoadsExcitationDetail
    from ._5741 import ElectricMachineStatorToothMomentsExcitationDetail
    from ._5742 import ElectricMachineStatorToothRadialLoadsExcitationDetail
    from ._5743 import ElectricMachineStatorToothTangentialLoadsExcitationDetail
    from ._5744 import ElectricMachineTorqueRipplePeriodicExcitationDetail
    from ._5745 import ExportOutputType
    from ._5746 import ExternalCADModelHarmonicAnalysis
    from ._5747 import FaceGearHarmonicAnalysis
    from ._5748 import FaceGearMeshHarmonicAnalysis
    from ._5749 import FaceGearSetHarmonicAnalysis
    from ._5750 import FEPartHarmonicAnalysis
    from ._5751 import FlexiblePinAssemblyHarmonicAnalysis
    from ._5752 import FrequencyOptionsForHarmonicAnalysisResults
    from ._5753 import GearHarmonicAnalysis
    from ._5754 import GearMeshExcitationDetail
    from ._5755 import GearMeshHarmonicAnalysis
    from ._5756 import GearMeshMisalignmentExcitationDetail
    from ._5757 import GearMeshTEExcitationDetail
    from ._5758 import GearSetHarmonicAnalysis
    from ._5759 import GeneralPeriodicExcitationDetail
    from ._5760 import GuideDxfModelHarmonicAnalysis
    from ._5761 import HarmonicAnalysis
    from ._5762 import HarmonicAnalysisDrawStyle
    from ._5763 import HarmonicAnalysisExportOptions
    from ._5764 import HarmonicAnalysisFEExportOptions
    from ._5765 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._5766 import HarmonicAnalysisOptions
    from ._5767 import HarmonicAnalysisRootAssemblyExportOptions
    from ._5768 import HarmonicAnalysisShaftExportOptions
    from ._5769 import HarmonicAnalysisTorqueInputType
    from ._5770 import HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
    from ._5771 import HypoidGearHarmonicAnalysis
    from ._5772 import HypoidGearMeshHarmonicAnalysis
    from ._5773 import HypoidGearSetHarmonicAnalysis
    from ._5774 import InterMountableComponentConnectionHarmonicAnalysis
    from ._5775 import KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
    from ._5776 import KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
    from ._5777 import KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
    from ._5778 import KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
    from ._5779 import KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
    from ._5780 import KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
    from ._5781 import KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
    from ._5782 import KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
    from ._5783 import KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
    from ._5784 import MassDiscHarmonicAnalysis
    from ._5785 import MeasurementComponentHarmonicAnalysis
    from ._5786 import MountableComponentHarmonicAnalysis
    from ._5787 import OilSealHarmonicAnalysis
    from ._5788 import PartHarmonicAnalysis
    from ._5789 import PartToPartShearCouplingConnectionHarmonicAnalysis
    from ._5790 import PartToPartShearCouplingHalfHarmonicAnalysis
    from ._5791 import PartToPartShearCouplingHarmonicAnalysis
    from ._5792 import PeriodicExcitationWithReferenceShaft
    from ._5793 import PlanetaryConnectionHarmonicAnalysis
    from ._5794 import PlanetaryGearSetHarmonicAnalysis
    from ._5795 import PlanetCarrierHarmonicAnalysis
    from ._5796 import PointLoadHarmonicAnalysis
    from ._5797 import PowerLoadHarmonicAnalysis
    from ._5798 import PulleyHarmonicAnalysis
    from ._5799 import ResponseCacheLevel
    from ._5800 import RingPinsHarmonicAnalysis
    from ._5801 import RingPinsToDiscConnectionHarmonicAnalysis
    from ._5802 import RollingRingAssemblyHarmonicAnalysis
    from ._5803 import RollingRingConnectionHarmonicAnalysis
    from ._5804 import RollingRingHarmonicAnalysis
    from ._5805 import RootAssemblyHarmonicAnalysis
    from ._5806 import ShaftHarmonicAnalysis
    from ._5807 import ShaftHubConnectionHarmonicAnalysis
    from ._5808 import ShaftToMountableComponentConnectionHarmonicAnalysis
    from ._5809 import SingleNodePeriodicExcitationWithReferenceShaft
    from ._5810 import SpecialisedAssemblyHarmonicAnalysis
    from ._5811 import SpeedOptionsForHarmonicAnalysisResults
    from ._5812 import SpiralBevelGearHarmonicAnalysis
    from ._5813 import SpiralBevelGearMeshHarmonicAnalysis
    from ._5814 import SpiralBevelGearSetHarmonicAnalysis
    from ._5815 import SpringDamperConnectionHarmonicAnalysis
    from ._5816 import SpringDamperHalfHarmonicAnalysis
    from ._5817 import SpringDamperHarmonicAnalysis
    from ._5818 import StiffnessOptionsForHarmonicAnalysis
    from ._5819 import StraightBevelDiffGearHarmonicAnalysis
    from ._5820 import StraightBevelDiffGearMeshHarmonicAnalysis
    from ._5821 import StraightBevelDiffGearSetHarmonicAnalysis
    from ._5822 import StraightBevelGearHarmonicAnalysis
    from ._5823 import StraightBevelGearMeshHarmonicAnalysis
    from ._5824 import StraightBevelGearSetHarmonicAnalysis
    from ._5825 import StraightBevelPlanetGearHarmonicAnalysis
    from ._5826 import StraightBevelSunGearHarmonicAnalysis
    from ._5827 import SynchroniserHalfHarmonicAnalysis
    from ._5828 import SynchroniserHarmonicAnalysis
    from ._5829 import SynchroniserPartHarmonicAnalysis
    from ._5830 import SynchroniserSleeveHarmonicAnalysis
    from ._5831 import TorqueConverterConnectionHarmonicAnalysis
    from ._5832 import TorqueConverterHarmonicAnalysis
    from ._5833 import TorqueConverterPumpHarmonicAnalysis
    from ._5834 import TorqueConverterTurbineHarmonicAnalysis
    from ._5835 import UnbalancedMassExcitationDetail
    from ._5836 import UnbalancedMassHarmonicAnalysis
    from ._5837 import VirtualComponentHarmonicAnalysis
    from ._5838 import WormGearHarmonicAnalysis
    from ._5839 import WormGearMeshHarmonicAnalysis
    from ._5840 import WormGearSetHarmonicAnalysis
    from ._5841 import ZerolBevelGearHarmonicAnalysis
    from ._5842 import ZerolBevelGearMeshHarmonicAnalysis
    from ._5843 import ZerolBevelGearSetHarmonicAnalysis
else:
    import_structure = {
        "_5678": ["AbstractAssemblyHarmonicAnalysis"],
        "_5679": ["AbstractPeriodicExcitationDetail"],
        "_5680": ["AbstractShaftHarmonicAnalysis"],
        "_5681": ["AbstractShaftOrHousingHarmonicAnalysis"],
        "_5682": ["AbstractShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5683": ["AGMAGleasonConicalGearHarmonicAnalysis"],
        "_5684": ["AGMAGleasonConicalGearMeshHarmonicAnalysis"],
        "_5685": ["AGMAGleasonConicalGearSetHarmonicAnalysis"],
        "_5686": ["AssemblyHarmonicAnalysis"],
        "_5687": ["BearingHarmonicAnalysis"],
        "_5688": ["BeltConnectionHarmonicAnalysis"],
        "_5689": ["BeltDriveHarmonicAnalysis"],
        "_5690": ["BevelDifferentialGearHarmonicAnalysis"],
        "_5691": ["BevelDifferentialGearMeshHarmonicAnalysis"],
        "_5692": ["BevelDifferentialGearSetHarmonicAnalysis"],
        "_5693": ["BevelDifferentialPlanetGearHarmonicAnalysis"],
        "_5694": ["BevelDifferentialSunGearHarmonicAnalysis"],
        "_5695": ["BevelGearHarmonicAnalysis"],
        "_5696": ["BevelGearMeshHarmonicAnalysis"],
        "_5697": ["BevelGearSetHarmonicAnalysis"],
        "_5698": ["BoltedJointHarmonicAnalysis"],
        "_5699": ["BoltHarmonicAnalysis"],
        "_5700": ["ClutchConnectionHarmonicAnalysis"],
        "_5701": ["ClutchHalfHarmonicAnalysis"],
        "_5702": ["ClutchHarmonicAnalysis"],
        "_5703": ["CoaxialConnectionHarmonicAnalysis"],
        "_5704": ["ComplianceAndForceData"],
        "_5705": ["ComponentHarmonicAnalysis"],
        "_5706": ["ConceptCouplingConnectionHarmonicAnalysis"],
        "_5707": ["ConceptCouplingHalfHarmonicAnalysis"],
        "_5708": ["ConceptCouplingHarmonicAnalysis"],
        "_5709": ["ConceptGearHarmonicAnalysis"],
        "_5710": ["ConceptGearMeshHarmonicAnalysis"],
        "_5711": ["ConceptGearSetHarmonicAnalysis"],
        "_5712": ["ConicalGearHarmonicAnalysis"],
        "_5713": ["ConicalGearMeshHarmonicAnalysis"],
        "_5714": ["ConicalGearSetHarmonicAnalysis"],
        "_5715": ["ConnectionHarmonicAnalysis"],
        "_5716": ["ConnectorHarmonicAnalysis"],
        "_5717": ["CouplingConnectionHarmonicAnalysis"],
        "_5718": ["CouplingHalfHarmonicAnalysis"],
        "_5719": ["CouplingHarmonicAnalysis"],
        "_5720": ["CVTBeltConnectionHarmonicAnalysis"],
        "_5721": ["CVTHarmonicAnalysis"],
        "_5722": ["CVTPulleyHarmonicAnalysis"],
        "_5723": ["CycloidalAssemblyHarmonicAnalysis"],
        "_5724": ["CycloidalDiscCentralBearingConnectionHarmonicAnalysis"],
        "_5725": ["CycloidalDiscHarmonicAnalysis"],
        "_5726": ["CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis"],
        "_5727": ["CylindricalGearHarmonicAnalysis"],
        "_5728": ["CylindricalGearMeshHarmonicAnalysis"],
        "_5729": ["CylindricalGearSetHarmonicAnalysis"],
        "_5730": ["CylindricalPlanetGearHarmonicAnalysis"],
        "_5731": ["DatumHarmonicAnalysis"],
        "_5732": ["DynamicModelForHarmonicAnalysis"],
        "_5733": ["ElectricMachinePeriodicExcitationDetail"],
        "_5734": ["ElectricMachineRotorXForcePeriodicExcitationDetail"],
        "_5735": ["ElectricMachineRotorXMomentPeriodicExcitationDetail"],
        "_5736": ["ElectricMachineRotorYForcePeriodicExcitationDetail"],
        "_5737": ["ElectricMachineRotorYMomentPeriodicExcitationDetail"],
        "_5738": ["ElectricMachineRotorZForcePeriodicExcitationDetail"],
        "_5739": ["ElectricMachineStatorToothAxialLoadsExcitationDetail"],
        "_5740": ["ElectricMachineStatorToothLoadsExcitationDetail"],
        "_5741": ["ElectricMachineStatorToothMomentsExcitationDetail"],
        "_5742": ["ElectricMachineStatorToothRadialLoadsExcitationDetail"],
        "_5743": ["ElectricMachineStatorToothTangentialLoadsExcitationDetail"],
        "_5744": ["ElectricMachineTorqueRipplePeriodicExcitationDetail"],
        "_5745": ["ExportOutputType"],
        "_5746": ["ExternalCADModelHarmonicAnalysis"],
        "_5747": ["FaceGearHarmonicAnalysis"],
        "_5748": ["FaceGearMeshHarmonicAnalysis"],
        "_5749": ["FaceGearSetHarmonicAnalysis"],
        "_5750": ["FEPartHarmonicAnalysis"],
        "_5751": ["FlexiblePinAssemblyHarmonicAnalysis"],
        "_5752": ["FrequencyOptionsForHarmonicAnalysisResults"],
        "_5753": ["GearHarmonicAnalysis"],
        "_5754": ["GearMeshExcitationDetail"],
        "_5755": ["GearMeshHarmonicAnalysis"],
        "_5756": ["GearMeshMisalignmentExcitationDetail"],
        "_5757": ["GearMeshTEExcitationDetail"],
        "_5758": ["GearSetHarmonicAnalysis"],
        "_5759": ["GeneralPeriodicExcitationDetail"],
        "_5760": ["GuideDxfModelHarmonicAnalysis"],
        "_5761": ["HarmonicAnalysis"],
        "_5762": ["HarmonicAnalysisDrawStyle"],
        "_5763": ["HarmonicAnalysisExportOptions"],
        "_5764": ["HarmonicAnalysisFEExportOptions"],
        "_5765": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_5766": ["HarmonicAnalysisOptions"],
        "_5767": ["HarmonicAnalysisRootAssemblyExportOptions"],
        "_5768": ["HarmonicAnalysisShaftExportOptions"],
        "_5769": ["HarmonicAnalysisTorqueInputType"],
        "_5770": ["HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"],
        "_5771": ["HypoidGearHarmonicAnalysis"],
        "_5772": ["HypoidGearMeshHarmonicAnalysis"],
        "_5773": ["HypoidGearSetHarmonicAnalysis"],
        "_5774": ["InterMountableComponentConnectionHarmonicAnalysis"],
        "_5775": ["KlingelnbergCycloPalloidConicalGearHarmonicAnalysis"],
        "_5776": ["KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis"],
        "_5777": ["KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis"],
        "_5778": ["KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis"],
        "_5779": ["KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis"],
        "_5780": ["KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis"],
        "_5781": ["KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis"],
        "_5782": ["KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis"],
        "_5783": ["KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis"],
        "_5784": ["MassDiscHarmonicAnalysis"],
        "_5785": ["MeasurementComponentHarmonicAnalysis"],
        "_5786": ["MountableComponentHarmonicAnalysis"],
        "_5787": ["OilSealHarmonicAnalysis"],
        "_5788": ["PartHarmonicAnalysis"],
        "_5789": ["PartToPartShearCouplingConnectionHarmonicAnalysis"],
        "_5790": ["PartToPartShearCouplingHalfHarmonicAnalysis"],
        "_5791": ["PartToPartShearCouplingHarmonicAnalysis"],
        "_5792": ["PeriodicExcitationWithReferenceShaft"],
        "_5793": ["PlanetaryConnectionHarmonicAnalysis"],
        "_5794": ["PlanetaryGearSetHarmonicAnalysis"],
        "_5795": ["PlanetCarrierHarmonicAnalysis"],
        "_5796": ["PointLoadHarmonicAnalysis"],
        "_5797": ["PowerLoadHarmonicAnalysis"],
        "_5798": ["PulleyHarmonicAnalysis"],
        "_5799": ["ResponseCacheLevel"],
        "_5800": ["RingPinsHarmonicAnalysis"],
        "_5801": ["RingPinsToDiscConnectionHarmonicAnalysis"],
        "_5802": ["RollingRingAssemblyHarmonicAnalysis"],
        "_5803": ["RollingRingConnectionHarmonicAnalysis"],
        "_5804": ["RollingRingHarmonicAnalysis"],
        "_5805": ["RootAssemblyHarmonicAnalysis"],
        "_5806": ["ShaftHarmonicAnalysis"],
        "_5807": ["ShaftHubConnectionHarmonicAnalysis"],
        "_5808": ["ShaftToMountableComponentConnectionHarmonicAnalysis"],
        "_5809": ["SingleNodePeriodicExcitationWithReferenceShaft"],
        "_5810": ["SpecialisedAssemblyHarmonicAnalysis"],
        "_5811": ["SpeedOptionsForHarmonicAnalysisResults"],
        "_5812": ["SpiralBevelGearHarmonicAnalysis"],
        "_5813": ["SpiralBevelGearMeshHarmonicAnalysis"],
        "_5814": ["SpiralBevelGearSetHarmonicAnalysis"],
        "_5815": ["SpringDamperConnectionHarmonicAnalysis"],
        "_5816": ["SpringDamperHalfHarmonicAnalysis"],
        "_5817": ["SpringDamperHarmonicAnalysis"],
        "_5818": ["StiffnessOptionsForHarmonicAnalysis"],
        "_5819": ["StraightBevelDiffGearHarmonicAnalysis"],
        "_5820": ["StraightBevelDiffGearMeshHarmonicAnalysis"],
        "_5821": ["StraightBevelDiffGearSetHarmonicAnalysis"],
        "_5822": ["StraightBevelGearHarmonicAnalysis"],
        "_5823": ["StraightBevelGearMeshHarmonicAnalysis"],
        "_5824": ["StraightBevelGearSetHarmonicAnalysis"],
        "_5825": ["StraightBevelPlanetGearHarmonicAnalysis"],
        "_5826": ["StraightBevelSunGearHarmonicAnalysis"],
        "_5827": ["SynchroniserHalfHarmonicAnalysis"],
        "_5828": ["SynchroniserHarmonicAnalysis"],
        "_5829": ["SynchroniserPartHarmonicAnalysis"],
        "_5830": ["SynchroniserSleeveHarmonicAnalysis"],
        "_5831": ["TorqueConverterConnectionHarmonicAnalysis"],
        "_5832": ["TorqueConverterHarmonicAnalysis"],
        "_5833": ["TorqueConverterPumpHarmonicAnalysis"],
        "_5834": ["TorqueConverterTurbineHarmonicAnalysis"],
        "_5835": ["UnbalancedMassExcitationDetail"],
        "_5836": ["UnbalancedMassHarmonicAnalysis"],
        "_5837": ["VirtualComponentHarmonicAnalysis"],
        "_5838": ["WormGearHarmonicAnalysis"],
        "_5839": ["WormGearMeshHarmonicAnalysis"],
        "_5840": ["WormGearSetHarmonicAnalysis"],
        "_5841": ["ZerolBevelGearHarmonicAnalysis"],
        "_5842": ["ZerolBevelGearMeshHarmonicAnalysis"],
        "_5843": ["ZerolBevelGearSetHarmonicAnalysis"],
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

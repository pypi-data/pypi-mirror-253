"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2685 import AbstractAssemblySystemDeflection
    from ._2686 import AbstractShaftOrHousingSystemDeflection
    from ._2687 import AbstractShaftSystemDeflection
    from ._2688 import AbstractShaftToMountableComponentConnectionSystemDeflection
    from ._2689 import AGMAGleasonConicalGearMeshSystemDeflection
    from ._2690 import AGMAGleasonConicalGearSetSystemDeflection
    from ._2691 import AGMAGleasonConicalGearSystemDeflection
    from ._2692 import AssemblySystemDeflection
    from ._2693 import BearingDynamicElementContactPropertyWrapper
    from ._2694 import BearingDynamicElementPropertyWrapper
    from ._2695 import BearingDynamicPostAnalysisResultWrapper
    from ._2696 import BearingDynamicResultsPropertyWrapper
    from ._2697 import BearingDynamicResultsUIWrapper
    from ._2698 import BearingSystemDeflection
    from ._2699 import BeltConnectionSystemDeflection
    from ._2700 import BeltDriveSystemDeflection
    from ._2701 import BevelDifferentialGearMeshSystemDeflection
    from ._2702 import BevelDifferentialGearSetSystemDeflection
    from ._2703 import BevelDifferentialGearSystemDeflection
    from ._2704 import BevelDifferentialPlanetGearSystemDeflection
    from ._2705 import BevelDifferentialSunGearSystemDeflection
    from ._2706 import BevelGearMeshSystemDeflection
    from ._2707 import BevelGearSetSystemDeflection
    from ._2708 import BevelGearSystemDeflection
    from ._2709 import BoltedJointSystemDeflection
    from ._2710 import BoltSystemDeflection
    from ._2711 import ClutchConnectionSystemDeflection
    from ._2712 import ClutchHalfSystemDeflection
    from ._2713 import ClutchSystemDeflection
    from ._2714 import CoaxialConnectionSystemDeflection
    from ._2715 import ComponentSystemDeflection
    from ._2716 import ConcentricPartGroupCombinationSystemDeflectionResults
    from ._2717 import ConceptCouplingConnectionSystemDeflection
    from ._2718 import ConceptCouplingHalfSystemDeflection
    from ._2719 import ConceptCouplingSystemDeflection
    from ._2720 import ConceptGearMeshSystemDeflection
    from ._2721 import ConceptGearSetSystemDeflection
    from ._2722 import ConceptGearSystemDeflection
    from ._2723 import ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2724 import ConicalGearMeshSystemDeflection
    from ._2725 import ConicalGearSetSystemDeflection
    from ._2726 import ConicalGearSystemDeflection
    from ._2727 import ConnectionSystemDeflection
    from ._2728 import ConnectorSystemDeflection
    from ._2729 import CouplingConnectionSystemDeflection
    from ._2730 import CouplingHalfSystemDeflection
    from ._2731 import CouplingSystemDeflection
    from ._2732 import CVTBeltConnectionSystemDeflection
    from ._2733 import CVTPulleySystemDeflection
    from ._2734 import CVTSystemDeflection
    from ._2735 import CycloidalAssemblySystemDeflection
    from ._2736 import CycloidalDiscCentralBearingConnectionSystemDeflection
    from ._2737 import CycloidalDiscPlanetaryBearingConnectionSystemDeflection
    from ._2738 import CycloidalDiscSystemDeflection
    from ._2739 import CylindricalGearMeshSystemDeflection
    from ._2740 import CylindricalGearMeshSystemDeflectionTimestep
    from ._2741 import CylindricalGearMeshSystemDeflectionWithLTCAResults
    from ._2742 import CylindricalGearSetSystemDeflection
    from ._2743 import CylindricalGearSetSystemDeflectionTimestep
    from ._2744 import CylindricalGearSetSystemDeflectionWithLTCAResults
    from ._2745 import CylindricalGearSystemDeflection
    from ._2746 import CylindricalGearSystemDeflectionTimestep
    from ._2747 import CylindricalGearSystemDeflectionWithLTCAResults
    from ._2748 import CylindricalMeshedGearFlankSystemDeflection
    from ._2749 import CylindricalMeshedGearSystemDeflection
    from ._2750 import CylindricalPlanetGearSystemDeflection
    from ._2751 import DatumSystemDeflection
    from ._2752 import ExternalCADModelSystemDeflection
    from ._2753 import FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator
    from ._2754 import FaceGearMeshSystemDeflection
    from ._2755 import FaceGearSetSystemDeflection
    from ._2756 import FaceGearSystemDeflection
    from ._2757 import FEPartSystemDeflection
    from ._2758 import FlexiblePinAssemblySystemDeflection
    from ._2759 import GearMeshSystemDeflection
    from ._2760 import GearSetSystemDeflection
    from ._2761 import GearSystemDeflection
    from ._2762 import GuideDxfModelSystemDeflection
    from ._2763 import HypoidGearMeshSystemDeflection
    from ._2764 import HypoidGearSetSystemDeflection
    from ._2765 import HypoidGearSystemDeflection
    from ._2766 import InformationForContactAtPointAlongFaceWidth
    from ._2767 import InterMountableComponentConnectionSystemDeflection
    from ._2768 import KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
    from ._2769 import KlingelnbergCycloPalloidConicalGearSetSystemDeflection
    from ._2770 import KlingelnbergCycloPalloidConicalGearSystemDeflection
    from ._2771 import KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
    from ._2772 import KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
    from ._2773 import KlingelnbergCycloPalloidHypoidGearSystemDeflection
    from ._2774 import KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
    from ._2775 import KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
    from ._2776 import KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
    from ._2777 import LoadCaseOverallEfficiencyResult
    from ._2778 import LoadSharingFactorReporter
    from ._2779 import MassDiscSystemDeflection
    from ._2780 import MeasurementComponentSystemDeflection
    from ._2781 import MeshSeparationsAtFaceWidth
    from ._2782 import MountableComponentSystemDeflection
    from ._2783 import ObservedPinStiffnessReporter
    from ._2784 import OilSealSystemDeflection
    from ._2785 import PartSystemDeflection
    from ._2786 import PartToPartShearCouplingConnectionSystemDeflection
    from ._2787 import PartToPartShearCouplingHalfSystemDeflection
    from ._2788 import PartToPartShearCouplingSystemDeflection
    from ._2789 import PlanetaryConnectionSystemDeflection
    from ._2790 import PlanetCarrierSystemDeflection
    from ._2791 import PointLoadSystemDeflection
    from ._2792 import PowerLoadSystemDeflection
    from ._2793 import PulleySystemDeflection
    from ._2794 import RingPinsSystemDeflection
    from ._2795 import RingPinsToDiscConnectionSystemDeflection
    from ._2796 import RingPinToDiscContactReporting
    from ._2797 import RollingRingAssemblySystemDeflection
    from ._2798 import RollingRingConnectionSystemDeflection
    from ._2799 import RollingRingSystemDeflection
    from ._2800 import RootAssemblySystemDeflection
    from ._2801 import ShaftHubConnectionSystemDeflection
    from ._2802 import ShaftSectionEndResultsSystemDeflection
    from ._2803 import ShaftSectionSystemDeflection
    from ._2804 import ShaftSystemDeflection
    from ._2805 import ShaftToMountableComponentConnectionSystemDeflection
    from ._2806 import SpecialisedAssemblySystemDeflection
    from ._2807 import SpiralBevelGearMeshSystemDeflection
    from ._2808 import SpiralBevelGearSetSystemDeflection
    from ._2809 import SpiralBevelGearSystemDeflection
    from ._2810 import SpringDamperConnectionSystemDeflection
    from ._2811 import SpringDamperHalfSystemDeflection
    from ._2812 import SpringDamperSystemDeflection
    from ._2813 import StraightBevelDiffGearMeshSystemDeflection
    from ._2814 import StraightBevelDiffGearSetSystemDeflection
    from ._2815 import StraightBevelDiffGearSystemDeflection
    from ._2816 import StraightBevelGearMeshSystemDeflection
    from ._2817 import StraightBevelGearSetSystemDeflection
    from ._2818 import StraightBevelGearSystemDeflection
    from ._2819 import StraightBevelPlanetGearSystemDeflection
    from ._2820 import StraightBevelSunGearSystemDeflection
    from ._2821 import SynchroniserHalfSystemDeflection
    from ._2822 import SynchroniserPartSystemDeflection
    from ._2823 import SynchroniserSleeveSystemDeflection
    from ._2824 import SynchroniserSystemDeflection
    from ._2825 import SystemDeflection
    from ._2826 import SystemDeflectionDrawStyle
    from ._2827 import SystemDeflectionOptions
    from ._2828 import TorqueConverterConnectionSystemDeflection
    from ._2829 import TorqueConverterPumpSystemDeflection
    from ._2830 import TorqueConverterSystemDeflection
    from ._2831 import TorqueConverterTurbineSystemDeflection
    from ._2832 import TorsionalSystemDeflection
    from ._2833 import TransmissionErrorResult
    from ._2834 import UnbalancedMassSystemDeflection
    from ._2835 import VirtualComponentSystemDeflection
    from ._2836 import WormGearMeshSystemDeflection
    from ._2837 import WormGearSetSystemDeflection
    from ._2838 import WormGearSystemDeflection
    from ._2839 import ZerolBevelGearMeshSystemDeflection
    from ._2840 import ZerolBevelGearSetSystemDeflection
    from ._2841 import ZerolBevelGearSystemDeflection
else:
    import_structure = {
        "_2685": ["AbstractAssemblySystemDeflection"],
        "_2686": ["AbstractShaftOrHousingSystemDeflection"],
        "_2687": ["AbstractShaftSystemDeflection"],
        "_2688": ["AbstractShaftToMountableComponentConnectionSystemDeflection"],
        "_2689": ["AGMAGleasonConicalGearMeshSystemDeflection"],
        "_2690": ["AGMAGleasonConicalGearSetSystemDeflection"],
        "_2691": ["AGMAGleasonConicalGearSystemDeflection"],
        "_2692": ["AssemblySystemDeflection"],
        "_2693": ["BearingDynamicElementContactPropertyWrapper"],
        "_2694": ["BearingDynamicElementPropertyWrapper"],
        "_2695": ["BearingDynamicPostAnalysisResultWrapper"],
        "_2696": ["BearingDynamicResultsPropertyWrapper"],
        "_2697": ["BearingDynamicResultsUIWrapper"],
        "_2698": ["BearingSystemDeflection"],
        "_2699": ["BeltConnectionSystemDeflection"],
        "_2700": ["BeltDriveSystemDeflection"],
        "_2701": ["BevelDifferentialGearMeshSystemDeflection"],
        "_2702": ["BevelDifferentialGearSetSystemDeflection"],
        "_2703": ["BevelDifferentialGearSystemDeflection"],
        "_2704": ["BevelDifferentialPlanetGearSystemDeflection"],
        "_2705": ["BevelDifferentialSunGearSystemDeflection"],
        "_2706": ["BevelGearMeshSystemDeflection"],
        "_2707": ["BevelGearSetSystemDeflection"],
        "_2708": ["BevelGearSystemDeflection"],
        "_2709": ["BoltedJointSystemDeflection"],
        "_2710": ["BoltSystemDeflection"],
        "_2711": ["ClutchConnectionSystemDeflection"],
        "_2712": ["ClutchHalfSystemDeflection"],
        "_2713": ["ClutchSystemDeflection"],
        "_2714": ["CoaxialConnectionSystemDeflection"],
        "_2715": ["ComponentSystemDeflection"],
        "_2716": ["ConcentricPartGroupCombinationSystemDeflectionResults"],
        "_2717": ["ConceptCouplingConnectionSystemDeflection"],
        "_2718": ["ConceptCouplingHalfSystemDeflection"],
        "_2719": ["ConceptCouplingSystemDeflection"],
        "_2720": ["ConceptGearMeshSystemDeflection"],
        "_2721": ["ConceptGearSetSystemDeflection"],
        "_2722": ["ConceptGearSystemDeflection"],
        "_2723": ["ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2724": ["ConicalGearMeshSystemDeflection"],
        "_2725": ["ConicalGearSetSystemDeflection"],
        "_2726": ["ConicalGearSystemDeflection"],
        "_2727": ["ConnectionSystemDeflection"],
        "_2728": ["ConnectorSystemDeflection"],
        "_2729": ["CouplingConnectionSystemDeflection"],
        "_2730": ["CouplingHalfSystemDeflection"],
        "_2731": ["CouplingSystemDeflection"],
        "_2732": ["CVTBeltConnectionSystemDeflection"],
        "_2733": ["CVTPulleySystemDeflection"],
        "_2734": ["CVTSystemDeflection"],
        "_2735": ["CycloidalAssemblySystemDeflection"],
        "_2736": ["CycloidalDiscCentralBearingConnectionSystemDeflection"],
        "_2737": ["CycloidalDiscPlanetaryBearingConnectionSystemDeflection"],
        "_2738": ["CycloidalDiscSystemDeflection"],
        "_2739": ["CylindricalGearMeshSystemDeflection"],
        "_2740": ["CylindricalGearMeshSystemDeflectionTimestep"],
        "_2741": ["CylindricalGearMeshSystemDeflectionWithLTCAResults"],
        "_2742": ["CylindricalGearSetSystemDeflection"],
        "_2743": ["CylindricalGearSetSystemDeflectionTimestep"],
        "_2744": ["CylindricalGearSetSystemDeflectionWithLTCAResults"],
        "_2745": ["CylindricalGearSystemDeflection"],
        "_2746": ["CylindricalGearSystemDeflectionTimestep"],
        "_2747": ["CylindricalGearSystemDeflectionWithLTCAResults"],
        "_2748": ["CylindricalMeshedGearFlankSystemDeflection"],
        "_2749": ["CylindricalMeshedGearSystemDeflection"],
        "_2750": ["CylindricalPlanetGearSystemDeflection"],
        "_2751": ["DatumSystemDeflection"],
        "_2752": ["ExternalCADModelSystemDeflection"],
        "_2753": ["FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator"],
        "_2754": ["FaceGearMeshSystemDeflection"],
        "_2755": ["FaceGearSetSystemDeflection"],
        "_2756": ["FaceGearSystemDeflection"],
        "_2757": ["FEPartSystemDeflection"],
        "_2758": ["FlexiblePinAssemblySystemDeflection"],
        "_2759": ["GearMeshSystemDeflection"],
        "_2760": ["GearSetSystemDeflection"],
        "_2761": ["GearSystemDeflection"],
        "_2762": ["GuideDxfModelSystemDeflection"],
        "_2763": ["HypoidGearMeshSystemDeflection"],
        "_2764": ["HypoidGearSetSystemDeflection"],
        "_2765": ["HypoidGearSystemDeflection"],
        "_2766": ["InformationForContactAtPointAlongFaceWidth"],
        "_2767": ["InterMountableComponentConnectionSystemDeflection"],
        "_2768": ["KlingelnbergCycloPalloidConicalGearMeshSystemDeflection"],
        "_2769": ["KlingelnbergCycloPalloidConicalGearSetSystemDeflection"],
        "_2770": ["KlingelnbergCycloPalloidConicalGearSystemDeflection"],
        "_2771": ["KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection"],
        "_2772": ["KlingelnbergCycloPalloidHypoidGearSetSystemDeflection"],
        "_2773": ["KlingelnbergCycloPalloidHypoidGearSystemDeflection"],
        "_2774": ["KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"],
        "_2775": ["KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection"],
        "_2776": ["KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection"],
        "_2777": ["LoadCaseOverallEfficiencyResult"],
        "_2778": ["LoadSharingFactorReporter"],
        "_2779": ["MassDiscSystemDeflection"],
        "_2780": ["MeasurementComponentSystemDeflection"],
        "_2781": ["MeshSeparationsAtFaceWidth"],
        "_2782": ["MountableComponentSystemDeflection"],
        "_2783": ["ObservedPinStiffnessReporter"],
        "_2784": ["OilSealSystemDeflection"],
        "_2785": ["PartSystemDeflection"],
        "_2786": ["PartToPartShearCouplingConnectionSystemDeflection"],
        "_2787": ["PartToPartShearCouplingHalfSystemDeflection"],
        "_2788": ["PartToPartShearCouplingSystemDeflection"],
        "_2789": ["PlanetaryConnectionSystemDeflection"],
        "_2790": ["PlanetCarrierSystemDeflection"],
        "_2791": ["PointLoadSystemDeflection"],
        "_2792": ["PowerLoadSystemDeflection"],
        "_2793": ["PulleySystemDeflection"],
        "_2794": ["RingPinsSystemDeflection"],
        "_2795": ["RingPinsToDiscConnectionSystemDeflection"],
        "_2796": ["RingPinToDiscContactReporting"],
        "_2797": ["RollingRingAssemblySystemDeflection"],
        "_2798": ["RollingRingConnectionSystemDeflection"],
        "_2799": ["RollingRingSystemDeflection"],
        "_2800": ["RootAssemblySystemDeflection"],
        "_2801": ["ShaftHubConnectionSystemDeflection"],
        "_2802": ["ShaftSectionEndResultsSystemDeflection"],
        "_2803": ["ShaftSectionSystemDeflection"],
        "_2804": ["ShaftSystemDeflection"],
        "_2805": ["ShaftToMountableComponentConnectionSystemDeflection"],
        "_2806": ["SpecialisedAssemblySystemDeflection"],
        "_2807": ["SpiralBevelGearMeshSystemDeflection"],
        "_2808": ["SpiralBevelGearSetSystemDeflection"],
        "_2809": ["SpiralBevelGearSystemDeflection"],
        "_2810": ["SpringDamperConnectionSystemDeflection"],
        "_2811": ["SpringDamperHalfSystemDeflection"],
        "_2812": ["SpringDamperSystemDeflection"],
        "_2813": ["StraightBevelDiffGearMeshSystemDeflection"],
        "_2814": ["StraightBevelDiffGearSetSystemDeflection"],
        "_2815": ["StraightBevelDiffGearSystemDeflection"],
        "_2816": ["StraightBevelGearMeshSystemDeflection"],
        "_2817": ["StraightBevelGearSetSystemDeflection"],
        "_2818": ["StraightBevelGearSystemDeflection"],
        "_2819": ["StraightBevelPlanetGearSystemDeflection"],
        "_2820": ["StraightBevelSunGearSystemDeflection"],
        "_2821": ["SynchroniserHalfSystemDeflection"],
        "_2822": ["SynchroniserPartSystemDeflection"],
        "_2823": ["SynchroniserSleeveSystemDeflection"],
        "_2824": ["SynchroniserSystemDeflection"],
        "_2825": ["SystemDeflection"],
        "_2826": ["SystemDeflectionDrawStyle"],
        "_2827": ["SystemDeflectionOptions"],
        "_2828": ["TorqueConverterConnectionSystemDeflection"],
        "_2829": ["TorqueConverterPumpSystemDeflection"],
        "_2830": ["TorqueConverterSystemDeflection"],
        "_2831": ["TorqueConverterTurbineSystemDeflection"],
        "_2832": ["TorsionalSystemDeflection"],
        "_2833": ["TransmissionErrorResult"],
        "_2834": ["UnbalancedMassSystemDeflection"],
        "_2835": ["VirtualComponentSystemDeflection"],
        "_2836": ["WormGearMeshSystemDeflection"],
        "_2837": ["WormGearSetSystemDeflection"],
        "_2838": ["WormGearSystemDeflection"],
        "_2839": ["ZerolBevelGearMeshSystemDeflection"],
        "_2840": ["ZerolBevelGearSetSystemDeflection"],
        "_2841": ["ZerolBevelGearSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblySystemDeflection",
    "AbstractShaftOrHousingSystemDeflection",
    "AbstractShaftSystemDeflection",
    "AbstractShaftToMountableComponentConnectionSystemDeflection",
    "AGMAGleasonConicalGearMeshSystemDeflection",
    "AGMAGleasonConicalGearSetSystemDeflection",
    "AGMAGleasonConicalGearSystemDeflection",
    "AssemblySystemDeflection",
    "BearingDynamicElementContactPropertyWrapper",
    "BearingDynamicElementPropertyWrapper",
    "BearingDynamicPostAnalysisResultWrapper",
    "BearingDynamicResultsPropertyWrapper",
    "BearingDynamicResultsUIWrapper",
    "BearingSystemDeflection",
    "BeltConnectionSystemDeflection",
    "BeltDriveSystemDeflection",
    "BevelDifferentialGearMeshSystemDeflection",
    "BevelDifferentialGearSetSystemDeflection",
    "BevelDifferentialGearSystemDeflection",
    "BevelDifferentialPlanetGearSystemDeflection",
    "BevelDifferentialSunGearSystemDeflection",
    "BevelGearMeshSystemDeflection",
    "BevelGearSetSystemDeflection",
    "BevelGearSystemDeflection",
    "BoltedJointSystemDeflection",
    "BoltSystemDeflection",
    "ClutchConnectionSystemDeflection",
    "ClutchHalfSystemDeflection",
    "ClutchSystemDeflection",
    "CoaxialConnectionSystemDeflection",
    "ComponentSystemDeflection",
    "ConcentricPartGroupCombinationSystemDeflectionResults",
    "ConceptCouplingConnectionSystemDeflection",
    "ConceptCouplingHalfSystemDeflection",
    "ConceptCouplingSystemDeflection",
    "ConceptGearMeshSystemDeflection",
    "ConceptGearSetSystemDeflection",
    "ConceptGearSystemDeflection",
    "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "ConicalGearMeshSystemDeflection",
    "ConicalGearSetSystemDeflection",
    "ConicalGearSystemDeflection",
    "ConnectionSystemDeflection",
    "ConnectorSystemDeflection",
    "CouplingConnectionSystemDeflection",
    "CouplingHalfSystemDeflection",
    "CouplingSystemDeflection",
    "CVTBeltConnectionSystemDeflection",
    "CVTPulleySystemDeflection",
    "CVTSystemDeflection",
    "CycloidalAssemblySystemDeflection",
    "CycloidalDiscCentralBearingConnectionSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionSystemDeflection",
    "CycloidalDiscSystemDeflection",
    "CylindricalGearMeshSystemDeflection",
    "CylindricalGearMeshSystemDeflectionTimestep",
    "CylindricalGearMeshSystemDeflectionWithLTCAResults",
    "CylindricalGearSetSystemDeflection",
    "CylindricalGearSetSystemDeflectionTimestep",
    "CylindricalGearSetSystemDeflectionWithLTCAResults",
    "CylindricalGearSystemDeflection",
    "CylindricalGearSystemDeflectionTimestep",
    "CylindricalGearSystemDeflectionWithLTCAResults",
    "CylindricalMeshedGearFlankSystemDeflection",
    "CylindricalMeshedGearSystemDeflection",
    "CylindricalPlanetGearSystemDeflection",
    "DatumSystemDeflection",
    "ExternalCADModelSystemDeflection",
    "FaceGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    "FaceGearMeshSystemDeflection",
    "FaceGearSetSystemDeflection",
    "FaceGearSystemDeflection",
    "FEPartSystemDeflection",
    "FlexiblePinAssemblySystemDeflection",
    "GearMeshSystemDeflection",
    "GearSetSystemDeflection",
    "GearSystemDeflection",
    "GuideDxfModelSystemDeflection",
    "HypoidGearMeshSystemDeflection",
    "HypoidGearSetSystemDeflection",
    "HypoidGearSystemDeflection",
    "InformationForContactAtPointAlongFaceWidth",
    "InterMountableComponentConnectionSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection",
    "LoadCaseOverallEfficiencyResult",
    "LoadSharingFactorReporter",
    "MassDiscSystemDeflection",
    "MeasurementComponentSystemDeflection",
    "MeshSeparationsAtFaceWidth",
    "MountableComponentSystemDeflection",
    "ObservedPinStiffnessReporter",
    "OilSealSystemDeflection",
    "PartSystemDeflection",
    "PartToPartShearCouplingConnectionSystemDeflection",
    "PartToPartShearCouplingHalfSystemDeflection",
    "PartToPartShearCouplingSystemDeflection",
    "PlanetaryConnectionSystemDeflection",
    "PlanetCarrierSystemDeflection",
    "PointLoadSystemDeflection",
    "PowerLoadSystemDeflection",
    "PulleySystemDeflection",
    "RingPinsSystemDeflection",
    "RingPinsToDiscConnectionSystemDeflection",
    "RingPinToDiscContactReporting",
    "RollingRingAssemblySystemDeflection",
    "RollingRingConnectionSystemDeflection",
    "RollingRingSystemDeflection",
    "RootAssemblySystemDeflection",
    "ShaftHubConnectionSystemDeflection",
    "ShaftSectionEndResultsSystemDeflection",
    "ShaftSectionSystemDeflection",
    "ShaftSystemDeflection",
    "ShaftToMountableComponentConnectionSystemDeflection",
    "SpecialisedAssemblySystemDeflection",
    "SpiralBevelGearMeshSystemDeflection",
    "SpiralBevelGearSetSystemDeflection",
    "SpiralBevelGearSystemDeflection",
    "SpringDamperConnectionSystemDeflection",
    "SpringDamperHalfSystemDeflection",
    "SpringDamperSystemDeflection",
    "StraightBevelDiffGearMeshSystemDeflection",
    "StraightBevelDiffGearSetSystemDeflection",
    "StraightBevelDiffGearSystemDeflection",
    "StraightBevelGearMeshSystemDeflection",
    "StraightBevelGearSetSystemDeflection",
    "StraightBevelGearSystemDeflection",
    "StraightBevelPlanetGearSystemDeflection",
    "StraightBevelSunGearSystemDeflection",
    "SynchroniserHalfSystemDeflection",
    "SynchroniserPartSystemDeflection",
    "SynchroniserSleeveSystemDeflection",
    "SynchroniserSystemDeflection",
    "SystemDeflection",
    "SystemDeflectionDrawStyle",
    "SystemDeflectionOptions",
    "TorqueConverterConnectionSystemDeflection",
    "TorqueConverterPumpSystemDeflection",
    "TorqueConverterSystemDeflection",
    "TorqueConverterTurbineSystemDeflection",
    "TorsionalSystemDeflection",
    "TransmissionErrorResult",
    "UnbalancedMassSystemDeflection",
    "VirtualComponentSystemDeflection",
    "WormGearMeshSystemDeflection",
    "WormGearSetSystemDeflection",
    "WormGearSystemDeflection",
    "ZerolBevelGearMeshSystemDeflection",
    "ZerolBevelGearSetSystemDeflection",
    "ZerolBevelGearSystemDeflection",
)

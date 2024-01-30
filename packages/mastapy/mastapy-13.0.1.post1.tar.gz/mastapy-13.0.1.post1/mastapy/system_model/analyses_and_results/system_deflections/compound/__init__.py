"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2851 import AbstractAssemblyCompoundSystemDeflection
    from ._2852 import AbstractShaftCompoundSystemDeflection
    from ._2853 import AbstractShaftOrHousingCompoundSystemDeflection
    from ._2854 import (
        AbstractShaftToMountableComponentConnectionCompoundSystemDeflection,
    )
    from ._2855 import AGMAGleasonConicalGearCompoundSystemDeflection
    from ._2856 import AGMAGleasonConicalGearMeshCompoundSystemDeflection
    from ._2857 import AGMAGleasonConicalGearSetCompoundSystemDeflection
    from ._2858 import AssemblyCompoundSystemDeflection
    from ._2859 import BearingCompoundSystemDeflection
    from ._2860 import BeltConnectionCompoundSystemDeflection
    from ._2861 import BeltDriveCompoundSystemDeflection
    from ._2862 import BevelDifferentialGearCompoundSystemDeflection
    from ._2863 import BevelDifferentialGearMeshCompoundSystemDeflection
    from ._2864 import BevelDifferentialGearSetCompoundSystemDeflection
    from ._2865 import BevelDifferentialPlanetGearCompoundSystemDeflection
    from ._2866 import BevelDifferentialSunGearCompoundSystemDeflection
    from ._2867 import BevelGearCompoundSystemDeflection
    from ._2868 import BevelGearMeshCompoundSystemDeflection
    from ._2869 import BevelGearSetCompoundSystemDeflection
    from ._2870 import BoltCompoundSystemDeflection
    from ._2871 import BoltedJointCompoundSystemDeflection
    from ._2872 import ClutchCompoundSystemDeflection
    from ._2873 import ClutchConnectionCompoundSystemDeflection
    from ._2874 import ClutchHalfCompoundSystemDeflection
    from ._2875 import CoaxialConnectionCompoundSystemDeflection
    from ._2876 import ComponentCompoundSystemDeflection
    from ._2877 import ConceptCouplingCompoundSystemDeflection
    from ._2878 import ConceptCouplingConnectionCompoundSystemDeflection
    from ._2879 import ConceptCouplingHalfCompoundSystemDeflection
    from ._2880 import ConceptGearCompoundSystemDeflection
    from ._2881 import ConceptGearMeshCompoundSystemDeflection
    from ._2882 import ConceptGearSetCompoundSystemDeflection
    from ._2883 import ConicalGearCompoundSystemDeflection
    from ._2884 import ConicalGearMeshCompoundSystemDeflection
    from ._2885 import ConicalGearSetCompoundSystemDeflection
    from ._2886 import ConnectionCompoundSystemDeflection
    from ._2887 import ConnectorCompoundSystemDeflection
    from ._2888 import CouplingCompoundSystemDeflection
    from ._2889 import CouplingConnectionCompoundSystemDeflection
    from ._2890 import CouplingHalfCompoundSystemDeflection
    from ._2891 import CVTBeltConnectionCompoundSystemDeflection
    from ._2892 import CVTCompoundSystemDeflection
    from ._2893 import CVTPulleyCompoundSystemDeflection
    from ._2894 import CycloidalAssemblyCompoundSystemDeflection
    from ._2895 import CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
    from ._2896 import CycloidalDiscCompoundSystemDeflection
    from ._2897 import CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
    from ._2898 import CylindricalGearCompoundSystemDeflection
    from ._2899 import CylindricalGearMeshCompoundSystemDeflection
    from ._2900 import CylindricalGearSetCompoundSystemDeflection
    from ._2901 import CylindricalPlanetGearCompoundSystemDeflection
    from ._2902 import DatumCompoundSystemDeflection
    from ._2903 import DutyCycleEfficiencyResults
    from ._2904 import ExternalCADModelCompoundSystemDeflection
    from ._2905 import FaceGearCompoundSystemDeflection
    from ._2906 import FaceGearMeshCompoundSystemDeflection
    from ._2907 import FaceGearSetCompoundSystemDeflection
    from ._2908 import FEPartCompoundSystemDeflection
    from ._2909 import FlexiblePinAssemblyCompoundSystemDeflection
    from ._2910 import GearCompoundSystemDeflection
    from ._2911 import GearMeshCompoundSystemDeflection
    from ._2912 import GearSetCompoundSystemDeflection
    from ._2913 import GuideDxfModelCompoundSystemDeflection
    from ._2914 import HypoidGearCompoundSystemDeflection
    from ._2915 import HypoidGearMeshCompoundSystemDeflection
    from ._2916 import HypoidGearSetCompoundSystemDeflection
    from ._2917 import InterMountableComponentConnectionCompoundSystemDeflection
    from ._2918 import KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
    from ._2919 import KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
    from ._2920 import KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
    from ._2921 import KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
    from ._2922 import KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
    from ._2923 import KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
    from ._2924 import KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
    from ._2925 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection,
    )
    from ._2926 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection,
    )
    from ._2927 import MassDiscCompoundSystemDeflection
    from ._2928 import MeasurementComponentCompoundSystemDeflection
    from ._2929 import MountableComponentCompoundSystemDeflection
    from ._2930 import OilSealCompoundSystemDeflection
    from ._2931 import PartCompoundSystemDeflection
    from ._2932 import PartToPartShearCouplingCompoundSystemDeflection
    from ._2933 import PartToPartShearCouplingConnectionCompoundSystemDeflection
    from ._2934 import PartToPartShearCouplingHalfCompoundSystemDeflection
    from ._2935 import PlanetaryConnectionCompoundSystemDeflection
    from ._2936 import PlanetaryGearSetCompoundSystemDeflection
    from ._2937 import PlanetCarrierCompoundSystemDeflection
    from ._2938 import PointLoadCompoundSystemDeflection
    from ._2939 import PowerLoadCompoundSystemDeflection
    from ._2940 import PulleyCompoundSystemDeflection
    from ._2941 import RingPinsCompoundSystemDeflection
    from ._2942 import RingPinsToDiscConnectionCompoundSystemDeflection
    from ._2943 import RollingRingAssemblyCompoundSystemDeflection
    from ._2944 import RollingRingCompoundSystemDeflection
    from ._2945 import RollingRingConnectionCompoundSystemDeflection
    from ._2946 import RootAssemblyCompoundSystemDeflection
    from ._2947 import ShaftCompoundSystemDeflection
    from ._2948 import ShaftDutyCycleSystemDeflection
    from ._2949 import ShaftHubConnectionCompoundSystemDeflection
    from ._2950 import ShaftToMountableComponentConnectionCompoundSystemDeflection
    from ._2951 import SpecialisedAssemblyCompoundSystemDeflection
    from ._2952 import SpiralBevelGearCompoundSystemDeflection
    from ._2953 import SpiralBevelGearMeshCompoundSystemDeflection
    from ._2954 import SpiralBevelGearSetCompoundSystemDeflection
    from ._2955 import SpringDamperCompoundSystemDeflection
    from ._2956 import SpringDamperConnectionCompoundSystemDeflection
    from ._2957 import SpringDamperHalfCompoundSystemDeflection
    from ._2958 import StraightBevelDiffGearCompoundSystemDeflection
    from ._2959 import StraightBevelDiffGearMeshCompoundSystemDeflection
    from ._2960 import StraightBevelDiffGearSetCompoundSystemDeflection
    from ._2961 import StraightBevelGearCompoundSystemDeflection
    from ._2962 import StraightBevelGearMeshCompoundSystemDeflection
    from ._2963 import StraightBevelGearSetCompoundSystemDeflection
    from ._2964 import StraightBevelPlanetGearCompoundSystemDeflection
    from ._2965 import StraightBevelSunGearCompoundSystemDeflection
    from ._2966 import SynchroniserCompoundSystemDeflection
    from ._2967 import SynchroniserHalfCompoundSystemDeflection
    from ._2968 import SynchroniserPartCompoundSystemDeflection
    from ._2969 import SynchroniserSleeveCompoundSystemDeflection
    from ._2970 import TorqueConverterCompoundSystemDeflection
    from ._2971 import TorqueConverterConnectionCompoundSystemDeflection
    from ._2972 import TorqueConverterPumpCompoundSystemDeflection
    from ._2973 import TorqueConverterTurbineCompoundSystemDeflection
    from ._2974 import UnbalancedMassCompoundSystemDeflection
    from ._2975 import VirtualComponentCompoundSystemDeflection
    from ._2976 import WormGearCompoundSystemDeflection
    from ._2977 import WormGearMeshCompoundSystemDeflection
    from ._2978 import WormGearSetCompoundSystemDeflection
    from ._2979 import ZerolBevelGearCompoundSystemDeflection
    from ._2980 import ZerolBevelGearMeshCompoundSystemDeflection
    from ._2981 import ZerolBevelGearSetCompoundSystemDeflection
else:
    import_structure = {
        "_2851": ["AbstractAssemblyCompoundSystemDeflection"],
        "_2852": ["AbstractShaftCompoundSystemDeflection"],
        "_2853": ["AbstractShaftOrHousingCompoundSystemDeflection"],
        "_2854": [
            "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ],
        "_2855": ["AGMAGleasonConicalGearCompoundSystemDeflection"],
        "_2856": ["AGMAGleasonConicalGearMeshCompoundSystemDeflection"],
        "_2857": ["AGMAGleasonConicalGearSetCompoundSystemDeflection"],
        "_2858": ["AssemblyCompoundSystemDeflection"],
        "_2859": ["BearingCompoundSystemDeflection"],
        "_2860": ["BeltConnectionCompoundSystemDeflection"],
        "_2861": ["BeltDriveCompoundSystemDeflection"],
        "_2862": ["BevelDifferentialGearCompoundSystemDeflection"],
        "_2863": ["BevelDifferentialGearMeshCompoundSystemDeflection"],
        "_2864": ["BevelDifferentialGearSetCompoundSystemDeflection"],
        "_2865": ["BevelDifferentialPlanetGearCompoundSystemDeflection"],
        "_2866": ["BevelDifferentialSunGearCompoundSystemDeflection"],
        "_2867": ["BevelGearCompoundSystemDeflection"],
        "_2868": ["BevelGearMeshCompoundSystemDeflection"],
        "_2869": ["BevelGearSetCompoundSystemDeflection"],
        "_2870": ["BoltCompoundSystemDeflection"],
        "_2871": ["BoltedJointCompoundSystemDeflection"],
        "_2872": ["ClutchCompoundSystemDeflection"],
        "_2873": ["ClutchConnectionCompoundSystemDeflection"],
        "_2874": ["ClutchHalfCompoundSystemDeflection"],
        "_2875": ["CoaxialConnectionCompoundSystemDeflection"],
        "_2876": ["ComponentCompoundSystemDeflection"],
        "_2877": ["ConceptCouplingCompoundSystemDeflection"],
        "_2878": ["ConceptCouplingConnectionCompoundSystemDeflection"],
        "_2879": ["ConceptCouplingHalfCompoundSystemDeflection"],
        "_2880": ["ConceptGearCompoundSystemDeflection"],
        "_2881": ["ConceptGearMeshCompoundSystemDeflection"],
        "_2882": ["ConceptGearSetCompoundSystemDeflection"],
        "_2883": ["ConicalGearCompoundSystemDeflection"],
        "_2884": ["ConicalGearMeshCompoundSystemDeflection"],
        "_2885": ["ConicalGearSetCompoundSystemDeflection"],
        "_2886": ["ConnectionCompoundSystemDeflection"],
        "_2887": ["ConnectorCompoundSystemDeflection"],
        "_2888": ["CouplingCompoundSystemDeflection"],
        "_2889": ["CouplingConnectionCompoundSystemDeflection"],
        "_2890": ["CouplingHalfCompoundSystemDeflection"],
        "_2891": ["CVTBeltConnectionCompoundSystemDeflection"],
        "_2892": ["CVTCompoundSystemDeflection"],
        "_2893": ["CVTPulleyCompoundSystemDeflection"],
        "_2894": ["CycloidalAssemblyCompoundSystemDeflection"],
        "_2895": ["CycloidalDiscCentralBearingConnectionCompoundSystemDeflection"],
        "_2896": ["CycloidalDiscCompoundSystemDeflection"],
        "_2897": ["CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection"],
        "_2898": ["CylindricalGearCompoundSystemDeflection"],
        "_2899": ["CylindricalGearMeshCompoundSystemDeflection"],
        "_2900": ["CylindricalGearSetCompoundSystemDeflection"],
        "_2901": ["CylindricalPlanetGearCompoundSystemDeflection"],
        "_2902": ["DatumCompoundSystemDeflection"],
        "_2903": ["DutyCycleEfficiencyResults"],
        "_2904": ["ExternalCADModelCompoundSystemDeflection"],
        "_2905": ["FaceGearCompoundSystemDeflection"],
        "_2906": ["FaceGearMeshCompoundSystemDeflection"],
        "_2907": ["FaceGearSetCompoundSystemDeflection"],
        "_2908": ["FEPartCompoundSystemDeflection"],
        "_2909": ["FlexiblePinAssemblyCompoundSystemDeflection"],
        "_2910": ["GearCompoundSystemDeflection"],
        "_2911": ["GearMeshCompoundSystemDeflection"],
        "_2912": ["GearSetCompoundSystemDeflection"],
        "_2913": ["GuideDxfModelCompoundSystemDeflection"],
        "_2914": ["HypoidGearCompoundSystemDeflection"],
        "_2915": ["HypoidGearMeshCompoundSystemDeflection"],
        "_2916": ["HypoidGearSetCompoundSystemDeflection"],
        "_2917": ["InterMountableComponentConnectionCompoundSystemDeflection"],
        "_2918": ["KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection"],
        "_2919": ["KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection"],
        "_2920": ["KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection"],
        "_2921": ["KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection"],
        "_2922": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"],
        "_2923": ["KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection"],
        "_2924": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection"],
        "_2925": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ],
        "_2926": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection"],
        "_2927": ["MassDiscCompoundSystemDeflection"],
        "_2928": ["MeasurementComponentCompoundSystemDeflection"],
        "_2929": ["MountableComponentCompoundSystemDeflection"],
        "_2930": ["OilSealCompoundSystemDeflection"],
        "_2931": ["PartCompoundSystemDeflection"],
        "_2932": ["PartToPartShearCouplingCompoundSystemDeflection"],
        "_2933": ["PartToPartShearCouplingConnectionCompoundSystemDeflection"],
        "_2934": ["PartToPartShearCouplingHalfCompoundSystemDeflection"],
        "_2935": ["PlanetaryConnectionCompoundSystemDeflection"],
        "_2936": ["PlanetaryGearSetCompoundSystemDeflection"],
        "_2937": ["PlanetCarrierCompoundSystemDeflection"],
        "_2938": ["PointLoadCompoundSystemDeflection"],
        "_2939": ["PowerLoadCompoundSystemDeflection"],
        "_2940": ["PulleyCompoundSystemDeflection"],
        "_2941": ["RingPinsCompoundSystemDeflection"],
        "_2942": ["RingPinsToDiscConnectionCompoundSystemDeflection"],
        "_2943": ["RollingRingAssemblyCompoundSystemDeflection"],
        "_2944": ["RollingRingCompoundSystemDeflection"],
        "_2945": ["RollingRingConnectionCompoundSystemDeflection"],
        "_2946": ["RootAssemblyCompoundSystemDeflection"],
        "_2947": ["ShaftCompoundSystemDeflection"],
        "_2948": ["ShaftDutyCycleSystemDeflection"],
        "_2949": ["ShaftHubConnectionCompoundSystemDeflection"],
        "_2950": ["ShaftToMountableComponentConnectionCompoundSystemDeflection"],
        "_2951": ["SpecialisedAssemblyCompoundSystemDeflection"],
        "_2952": ["SpiralBevelGearCompoundSystemDeflection"],
        "_2953": ["SpiralBevelGearMeshCompoundSystemDeflection"],
        "_2954": ["SpiralBevelGearSetCompoundSystemDeflection"],
        "_2955": ["SpringDamperCompoundSystemDeflection"],
        "_2956": ["SpringDamperConnectionCompoundSystemDeflection"],
        "_2957": ["SpringDamperHalfCompoundSystemDeflection"],
        "_2958": ["StraightBevelDiffGearCompoundSystemDeflection"],
        "_2959": ["StraightBevelDiffGearMeshCompoundSystemDeflection"],
        "_2960": ["StraightBevelDiffGearSetCompoundSystemDeflection"],
        "_2961": ["StraightBevelGearCompoundSystemDeflection"],
        "_2962": ["StraightBevelGearMeshCompoundSystemDeflection"],
        "_2963": ["StraightBevelGearSetCompoundSystemDeflection"],
        "_2964": ["StraightBevelPlanetGearCompoundSystemDeflection"],
        "_2965": ["StraightBevelSunGearCompoundSystemDeflection"],
        "_2966": ["SynchroniserCompoundSystemDeflection"],
        "_2967": ["SynchroniserHalfCompoundSystemDeflection"],
        "_2968": ["SynchroniserPartCompoundSystemDeflection"],
        "_2969": ["SynchroniserSleeveCompoundSystemDeflection"],
        "_2970": ["TorqueConverterCompoundSystemDeflection"],
        "_2971": ["TorqueConverterConnectionCompoundSystemDeflection"],
        "_2972": ["TorqueConverterPumpCompoundSystemDeflection"],
        "_2973": ["TorqueConverterTurbineCompoundSystemDeflection"],
        "_2974": ["UnbalancedMassCompoundSystemDeflection"],
        "_2975": ["VirtualComponentCompoundSystemDeflection"],
        "_2976": ["WormGearCompoundSystemDeflection"],
        "_2977": ["WormGearMeshCompoundSystemDeflection"],
        "_2978": ["WormGearSetCompoundSystemDeflection"],
        "_2979": ["ZerolBevelGearCompoundSystemDeflection"],
        "_2980": ["ZerolBevelGearMeshCompoundSystemDeflection"],
        "_2981": ["ZerolBevelGearSetCompoundSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSystemDeflection",
    "AbstractShaftCompoundSystemDeflection",
    "AbstractShaftOrHousingCompoundSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundSystemDeflection",
    "AGMAGleasonConicalGearCompoundSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundSystemDeflection",
    "AssemblyCompoundSystemDeflection",
    "BearingCompoundSystemDeflection",
    "BeltConnectionCompoundSystemDeflection",
    "BeltDriveCompoundSystemDeflection",
    "BevelDifferentialGearCompoundSystemDeflection",
    "BevelDifferentialGearMeshCompoundSystemDeflection",
    "BevelDifferentialGearSetCompoundSystemDeflection",
    "BevelDifferentialPlanetGearCompoundSystemDeflection",
    "BevelDifferentialSunGearCompoundSystemDeflection",
    "BevelGearCompoundSystemDeflection",
    "BevelGearMeshCompoundSystemDeflection",
    "BevelGearSetCompoundSystemDeflection",
    "BoltCompoundSystemDeflection",
    "BoltedJointCompoundSystemDeflection",
    "ClutchCompoundSystemDeflection",
    "ClutchConnectionCompoundSystemDeflection",
    "ClutchHalfCompoundSystemDeflection",
    "CoaxialConnectionCompoundSystemDeflection",
    "ComponentCompoundSystemDeflection",
    "ConceptCouplingCompoundSystemDeflection",
    "ConceptCouplingConnectionCompoundSystemDeflection",
    "ConceptCouplingHalfCompoundSystemDeflection",
    "ConceptGearCompoundSystemDeflection",
    "ConceptGearMeshCompoundSystemDeflection",
    "ConceptGearSetCompoundSystemDeflection",
    "ConicalGearCompoundSystemDeflection",
    "ConicalGearMeshCompoundSystemDeflection",
    "ConicalGearSetCompoundSystemDeflection",
    "ConnectionCompoundSystemDeflection",
    "ConnectorCompoundSystemDeflection",
    "CouplingCompoundSystemDeflection",
    "CouplingConnectionCompoundSystemDeflection",
    "CouplingHalfCompoundSystemDeflection",
    "CVTBeltConnectionCompoundSystemDeflection",
    "CVTCompoundSystemDeflection",
    "CVTPulleyCompoundSystemDeflection",
    "CycloidalAssemblyCompoundSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundSystemDeflection",
    "CycloidalDiscCompoundSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection",
    "CylindricalGearCompoundSystemDeflection",
    "CylindricalGearMeshCompoundSystemDeflection",
    "CylindricalGearSetCompoundSystemDeflection",
    "CylindricalPlanetGearCompoundSystemDeflection",
    "DatumCompoundSystemDeflection",
    "DutyCycleEfficiencyResults",
    "ExternalCADModelCompoundSystemDeflection",
    "FaceGearCompoundSystemDeflection",
    "FaceGearMeshCompoundSystemDeflection",
    "FaceGearSetCompoundSystemDeflection",
    "FEPartCompoundSystemDeflection",
    "FlexiblePinAssemblyCompoundSystemDeflection",
    "GearCompoundSystemDeflection",
    "GearMeshCompoundSystemDeflection",
    "GearSetCompoundSystemDeflection",
    "GuideDxfModelCompoundSystemDeflection",
    "HypoidGearCompoundSystemDeflection",
    "HypoidGearMeshCompoundSystemDeflection",
    "HypoidGearSetCompoundSystemDeflection",
    "InterMountableComponentConnectionCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
    "MassDiscCompoundSystemDeflection",
    "MeasurementComponentCompoundSystemDeflection",
    "MountableComponentCompoundSystemDeflection",
    "OilSealCompoundSystemDeflection",
    "PartCompoundSystemDeflection",
    "PartToPartShearCouplingCompoundSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundSystemDeflection",
    "PartToPartShearCouplingHalfCompoundSystemDeflection",
    "PlanetaryConnectionCompoundSystemDeflection",
    "PlanetaryGearSetCompoundSystemDeflection",
    "PlanetCarrierCompoundSystemDeflection",
    "PointLoadCompoundSystemDeflection",
    "PowerLoadCompoundSystemDeflection",
    "PulleyCompoundSystemDeflection",
    "RingPinsCompoundSystemDeflection",
    "RingPinsToDiscConnectionCompoundSystemDeflection",
    "RollingRingAssemblyCompoundSystemDeflection",
    "RollingRingCompoundSystemDeflection",
    "RollingRingConnectionCompoundSystemDeflection",
    "RootAssemblyCompoundSystemDeflection",
    "ShaftCompoundSystemDeflection",
    "ShaftDutyCycleSystemDeflection",
    "ShaftHubConnectionCompoundSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundSystemDeflection",
    "SpecialisedAssemblyCompoundSystemDeflection",
    "SpiralBevelGearCompoundSystemDeflection",
    "SpiralBevelGearMeshCompoundSystemDeflection",
    "SpiralBevelGearSetCompoundSystemDeflection",
    "SpringDamperCompoundSystemDeflection",
    "SpringDamperConnectionCompoundSystemDeflection",
    "SpringDamperHalfCompoundSystemDeflection",
    "StraightBevelDiffGearCompoundSystemDeflection",
    "StraightBevelDiffGearMeshCompoundSystemDeflection",
    "StraightBevelDiffGearSetCompoundSystemDeflection",
    "StraightBevelGearCompoundSystemDeflection",
    "StraightBevelGearMeshCompoundSystemDeflection",
    "StraightBevelGearSetCompoundSystemDeflection",
    "StraightBevelPlanetGearCompoundSystemDeflection",
    "StraightBevelSunGearCompoundSystemDeflection",
    "SynchroniserCompoundSystemDeflection",
    "SynchroniserHalfCompoundSystemDeflection",
    "SynchroniserPartCompoundSystemDeflection",
    "SynchroniserSleeveCompoundSystemDeflection",
    "TorqueConverterCompoundSystemDeflection",
    "TorqueConverterConnectionCompoundSystemDeflection",
    "TorqueConverterPumpCompoundSystemDeflection",
    "TorqueConverterTurbineCompoundSystemDeflection",
    "UnbalancedMassCompoundSystemDeflection",
    "VirtualComponentCompoundSystemDeflection",
    "WormGearCompoundSystemDeflection",
    "WormGearMeshCompoundSystemDeflection",
    "WormGearSetCompoundSystemDeflection",
    "ZerolBevelGearCompoundSystemDeflection",
    "ZerolBevelGearMeshCompoundSystemDeflection",
    "ZerolBevelGearSetCompoundSystemDeflection",
)

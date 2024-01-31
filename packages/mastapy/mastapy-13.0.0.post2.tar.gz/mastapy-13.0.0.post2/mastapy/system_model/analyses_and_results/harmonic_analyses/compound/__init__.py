"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5878 import AbstractAssemblyCompoundHarmonicAnalysis
    from ._5879 import AbstractShaftCompoundHarmonicAnalysis
    from ._5880 import AbstractShaftOrHousingCompoundHarmonicAnalysis
    from ._5881 import (
        AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis,
    )
    from ._5882 import AGMAGleasonConicalGearCompoundHarmonicAnalysis
    from ._5883 import AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
    from ._5884 import AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
    from ._5885 import AssemblyCompoundHarmonicAnalysis
    from ._5886 import BearingCompoundHarmonicAnalysis
    from ._5887 import BeltConnectionCompoundHarmonicAnalysis
    from ._5888 import BeltDriveCompoundHarmonicAnalysis
    from ._5889 import BevelDifferentialGearCompoundHarmonicAnalysis
    from ._5890 import BevelDifferentialGearMeshCompoundHarmonicAnalysis
    from ._5891 import BevelDifferentialGearSetCompoundHarmonicAnalysis
    from ._5892 import BevelDifferentialPlanetGearCompoundHarmonicAnalysis
    from ._5893 import BevelDifferentialSunGearCompoundHarmonicAnalysis
    from ._5894 import BevelGearCompoundHarmonicAnalysis
    from ._5895 import BevelGearMeshCompoundHarmonicAnalysis
    from ._5896 import BevelGearSetCompoundHarmonicAnalysis
    from ._5897 import BoltCompoundHarmonicAnalysis
    from ._5898 import BoltedJointCompoundHarmonicAnalysis
    from ._5899 import ClutchCompoundHarmonicAnalysis
    from ._5900 import ClutchConnectionCompoundHarmonicAnalysis
    from ._5901 import ClutchHalfCompoundHarmonicAnalysis
    from ._5902 import CoaxialConnectionCompoundHarmonicAnalysis
    from ._5903 import ComponentCompoundHarmonicAnalysis
    from ._5904 import ConceptCouplingCompoundHarmonicAnalysis
    from ._5905 import ConceptCouplingConnectionCompoundHarmonicAnalysis
    from ._5906 import ConceptCouplingHalfCompoundHarmonicAnalysis
    from ._5907 import ConceptGearCompoundHarmonicAnalysis
    from ._5908 import ConceptGearMeshCompoundHarmonicAnalysis
    from ._5909 import ConceptGearSetCompoundHarmonicAnalysis
    from ._5910 import ConicalGearCompoundHarmonicAnalysis
    from ._5911 import ConicalGearMeshCompoundHarmonicAnalysis
    from ._5912 import ConicalGearSetCompoundHarmonicAnalysis
    from ._5913 import ConnectionCompoundHarmonicAnalysis
    from ._5914 import ConnectorCompoundHarmonicAnalysis
    from ._5915 import CouplingCompoundHarmonicAnalysis
    from ._5916 import CouplingConnectionCompoundHarmonicAnalysis
    from ._5917 import CouplingHalfCompoundHarmonicAnalysis
    from ._5918 import CVTBeltConnectionCompoundHarmonicAnalysis
    from ._5919 import CVTCompoundHarmonicAnalysis
    from ._5920 import CVTPulleyCompoundHarmonicAnalysis
    from ._5921 import CycloidalAssemblyCompoundHarmonicAnalysis
    from ._5922 import CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
    from ._5923 import CycloidalDiscCompoundHarmonicAnalysis
    from ._5924 import CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
    from ._5925 import CylindricalGearCompoundHarmonicAnalysis
    from ._5926 import CylindricalGearMeshCompoundHarmonicAnalysis
    from ._5927 import CylindricalGearSetCompoundHarmonicAnalysis
    from ._5928 import CylindricalPlanetGearCompoundHarmonicAnalysis
    from ._5929 import DatumCompoundHarmonicAnalysis
    from ._5930 import ExternalCADModelCompoundHarmonicAnalysis
    from ._5931 import FaceGearCompoundHarmonicAnalysis
    from ._5932 import FaceGearMeshCompoundHarmonicAnalysis
    from ._5933 import FaceGearSetCompoundHarmonicAnalysis
    from ._5934 import FEPartCompoundHarmonicAnalysis
    from ._5935 import FlexiblePinAssemblyCompoundHarmonicAnalysis
    from ._5936 import GearCompoundHarmonicAnalysis
    from ._5937 import GearMeshCompoundHarmonicAnalysis
    from ._5938 import GearSetCompoundHarmonicAnalysis
    from ._5939 import GuideDxfModelCompoundHarmonicAnalysis
    from ._5940 import HypoidGearCompoundHarmonicAnalysis
    from ._5941 import HypoidGearMeshCompoundHarmonicAnalysis
    from ._5942 import HypoidGearSetCompoundHarmonicAnalysis
    from ._5943 import InterMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5944 import KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
    from ._5945 import KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
    from ._5946 import KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
    from ._5947 import KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
    from ._5948 import KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
    from ._5949 import KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
    from ._5950 import KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
    from ._5951 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis,
    )
    from ._5952 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis,
    )
    from ._5953 import MassDiscCompoundHarmonicAnalysis
    from ._5954 import MeasurementComponentCompoundHarmonicAnalysis
    from ._5955 import MountableComponentCompoundHarmonicAnalysis
    from ._5956 import OilSealCompoundHarmonicAnalysis
    from ._5957 import PartCompoundHarmonicAnalysis
    from ._5958 import PartToPartShearCouplingCompoundHarmonicAnalysis
    from ._5959 import PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
    from ._5960 import PartToPartShearCouplingHalfCompoundHarmonicAnalysis
    from ._5961 import PlanetaryConnectionCompoundHarmonicAnalysis
    from ._5962 import PlanetaryGearSetCompoundHarmonicAnalysis
    from ._5963 import PlanetCarrierCompoundHarmonicAnalysis
    from ._5964 import PointLoadCompoundHarmonicAnalysis
    from ._5965 import PowerLoadCompoundHarmonicAnalysis
    from ._5966 import PulleyCompoundHarmonicAnalysis
    from ._5967 import RingPinsCompoundHarmonicAnalysis
    from ._5968 import RingPinsToDiscConnectionCompoundHarmonicAnalysis
    from ._5969 import RollingRingAssemblyCompoundHarmonicAnalysis
    from ._5970 import RollingRingCompoundHarmonicAnalysis
    from ._5971 import RollingRingConnectionCompoundHarmonicAnalysis
    from ._5972 import RootAssemblyCompoundHarmonicAnalysis
    from ._5973 import ShaftCompoundHarmonicAnalysis
    from ._5974 import ShaftHubConnectionCompoundHarmonicAnalysis
    from ._5975 import ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5976 import SpecialisedAssemblyCompoundHarmonicAnalysis
    from ._5977 import SpiralBevelGearCompoundHarmonicAnalysis
    from ._5978 import SpiralBevelGearMeshCompoundHarmonicAnalysis
    from ._5979 import SpiralBevelGearSetCompoundHarmonicAnalysis
    from ._5980 import SpringDamperCompoundHarmonicAnalysis
    from ._5981 import SpringDamperConnectionCompoundHarmonicAnalysis
    from ._5982 import SpringDamperHalfCompoundHarmonicAnalysis
    from ._5983 import StraightBevelDiffGearCompoundHarmonicAnalysis
    from ._5984 import StraightBevelDiffGearMeshCompoundHarmonicAnalysis
    from ._5985 import StraightBevelDiffGearSetCompoundHarmonicAnalysis
    from ._5986 import StraightBevelGearCompoundHarmonicAnalysis
    from ._5987 import StraightBevelGearMeshCompoundHarmonicAnalysis
    from ._5988 import StraightBevelGearSetCompoundHarmonicAnalysis
    from ._5989 import StraightBevelPlanetGearCompoundHarmonicAnalysis
    from ._5990 import StraightBevelSunGearCompoundHarmonicAnalysis
    from ._5991 import SynchroniserCompoundHarmonicAnalysis
    from ._5992 import SynchroniserHalfCompoundHarmonicAnalysis
    from ._5993 import SynchroniserPartCompoundHarmonicAnalysis
    from ._5994 import SynchroniserSleeveCompoundHarmonicAnalysis
    from ._5995 import TorqueConverterCompoundHarmonicAnalysis
    from ._5996 import TorqueConverterConnectionCompoundHarmonicAnalysis
    from ._5997 import TorqueConverterPumpCompoundHarmonicAnalysis
    from ._5998 import TorqueConverterTurbineCompoundHarmonicAnalysis
    from ._5999 import UnbalancedMassCompoundHarmonicAnalysis
    from ._6000 import VirtualComponentCompoundHarmonicAnalysis
    from ._6001 import WormGearCompoundHarmonicAnalysis
    from ._6002 import WormGearMeshCompoundHarmonicAnalysis
    from ._6003 import WormGearSetCompoundHarmonicAnalysis
    from ._6004 import ZerolBevelGearCompoundHarmonicAnalysis
    from ._6005 import ZerolBevelGearMeshCompoundHarmonicAnalysis
    from ._6006 import ZerolBevelGearSetCompoundHarmonicAnalysis
else:
    import_structure = {
        "_5878": ["AbstractAssemblyCompoundHarmonicAnalysis"],
        "_5879": ["AbstractShaftCompoundHarmonicAnalysis"],
        "_5880": ["AbstractShaftOrHousingCompoundHarmonicAnalysis"],
        "_5881": [
            "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ],
        "_5882": ["AGMAGleasonConicalGearCompoundHarmonicAnalysis"],
        "_5883": ["AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis"],
        "_5884": ["AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"],
        "_5885": ["AssemblyCompoundHarmonicAnalysis"],
        "_5886": ["BearingCompoundHarmonicAnalysis"],
        "_5887": ["BeltConnectionCompoundHarmonicAnalysis"],
        "_5888": ["BeltDriveCompoundHarmonicAnalysis"],
        "_5889": ["BevelDifferentialGearCompoundHarmonicAnalysis"],
        "_5890": ["BevelDifferentialGearMeshCompoundHarmonicAnalysis"],
        "_5891": ["BevelDifferentialGearSetCompoundHarmonicAnalysis"],
        "_5892": ["BevelDifferentialPlanetGearCompoundHarmonicAnalysis"],
        "_5893": ["BevelDifferentialSunGearCompoundHarmonicAnalysis"],
        "_5894": ["BevelGearCompoundHarmonicAnalysis"],
        "_5895": ["BevelGearMeshCompoundHarmonicAnalysis"],
        "_5896": ["BevelGearSetCompoundHarmonicAnalysis"],
        "_5897": ["BoltCompoundHarmonicAnalysis"],
        "_5898": ["BoltedJointCompoundHarmonicAnalysis"],
        "_5899": ["ClutchCompoundHarmonicAnalysis"],
        "_5900": ["ClutchConnectionCompoundHarmonicAnalysis"],
        "_5901": ["ClutchHalfCompoundHarmonicAnalysis"],
        "_5902": ["CoaxialConnectionCompoundHarmonicAnalysis"],
        "_5903": ["ComponentCompoundHarmonicAnalysis"],
        "_5904": ["ConceptCouplingCompoundHarmonicAnalysis"],
        "_5905": ["ConceptCouplingConnectionCompoundHarmonicAnalysis"],
        "_5906": ["ConceptCouplingHalfCompoundHarmonicAnalysis"],
        "_5907": ["ConceptGearCompoundHarmonicAnalysis"],
        "_5908": ["ConceptGearMeshCompoundHarmonicAnalysis"],
        "_5909": ["ConceptGearSetCompoundHarmonicAnalysis"],
        "_5910": ["ConicalGearCompoundHarmonicAnalysis"],
        "_5911": ["ConicalGearMeshCompoundHarmonicAnalysis"],
        "_5912": ["ConicalGearSetCompoundHarmonicAnalysis"],
        "_5913": ["ConnectionCompoundHarmonicAnalysis"],
        "_5914": ["ConnectorCompoundHarmonicAnalysis"],
        "_5915": ["CouplingCompoundHarmonicAnalysis"],
        "_5916": ["CouplingConnectionCompoundHarmonicAnalysis"],
        "_5917": ["CouplingHalfCompoundHarmonicAnalysis"],
        "_5918": ["CVTBeltConnectionCompoundHarmonicAnalysis"],
        "_5919": ["CVTCompoundHarmonicAnalysis"],
        "_5920": ["CVTPulleyCompoundHarmonicAnalysis"],
        "_5921": ["CycloidalAssemblyCompoundHarmonicAnalysis"],
        "_5922": ["CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"],
        "_5923": ["CycloidalDiscCompoundHarmonicAnalysis"],
        "_5924": ["CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis"],
        "_5925": ["CylindricalGearCompoundHarmonicAnalysis"],
        "_5926": ["CylindricalGearMeshCompoundHarmonicAnalysis"],
        "_5927": ["CylindricalGearSetCompoundHarmonicAnalysis"],
        "_5928": ["CylindricalPlanetGearCompoundHarmonicAnalysis"],
        "_5929": ["DatumCompoundHarmonicAnalysis"],
        "_5930": ["ExternalCADModelCompoundHarmonicAnalysis"],
        "_5931": ["FaceGearCompoundHarmonicAnalysis"],
        "_5932": ["FaceGearMeshCompoundHarmonicAnalysis"],
        "_5933": ["FaceGearSetCompoundHarmonicAnalysis"],
        "_5934": ["FEPartCompoundHarmonicAnalysis"],
        "_5935": ["FlexiblePinAssemblyCompoundHarmonicAnalysis"],
        "_5936": ["GearCompoundHarmonicAnalysis"],
        "_5937": ["GearMeshCompoundHarmonicAnalysis"],
        "_5938": ["GearSetCompoundHarmonicAnalysis"],
        "_5939": ["GuideDxfModelCompoundHarmonicAnalysis"],
        "_5940": ["HypoidGearCompoundHarmonicAnalysis"],
        "_5941": ["HypoidGearMeshCompoundHarmonicAnalysis"],
        "_5942": ["HypoidGearSetCompoundHarmonicAnalysis"],
        "_5943": ["InterMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5944": ["KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis"],
        "_5945": ["KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"],
        "_5946": ["KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"],
        "_5947": ["KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis"],
        "_5948": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis"],
        "_5949": ["KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis"],
        "_5950": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis"],
        "_5951": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ],
        "_5952": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5953": ["MassDiscCompoundHarmonicAnalysis"],
        "_5954": ["MeasurementComponentCompoundHarmonicAnalysis"],
        "_5955": ["MountableComponentCompoundHarmonicAnalysis"],
        "_5956": ["OilSealCompoundHarmonicAnalysis"],
        "_5957": ["PartCompoundHarmonicAnalysis"],
        "_5958": ["PartToPartShearCouplingCompoundHarmonicAnalysis"],
        "_5959": ["PartToPartShearCouplingConnectionCompoundHarmonicAnalysis"],
        "_5960": ["PartToPartShearCouplingHalfCompoundHarmonicAnalysis"],
        "_5961": ["PlanetaryConnectionCompoundHarmonicAnalysis"],
        "_5962": ["PlanetaryGearSetCompoundHarmonicAnalysis"],
        "_5963": ["PlanetCarrierCompoundHarmonicAnalysis"],
        "_5964": ["PointLoadCompoundHarmonicAnalysis"],
        "_5965": ["PowerLoadCompoundHarmonicAnalysis"],
        "_5966": ["PulleyCompoundHarmonicAnalysis"],
        "_5967": ["RingPinsCompoundHarmonicAnalysis"],
        "_5968": ["RingPinsToDiscConnectionCompoundHarmonicAnalysis"],
        "_5969": ["RollingRingAssemblyCompoundHarmonicAnalysis"],
        "_5970": ["RollingRingCompoundHarmonicAnalysis"],
        "_5971": ["RollingRingConnectionCompoundHarmonicAnalysis"],
        "_5972": ["RootAssemblyCompoundHarmonicAnalysis"],
        "_5973": ["ShaftCompoundHarmonicAnalysis"],
        "_5974": ["ShaftHubConnectionCompoundHarmonicAnalysis"],
        "_5975": ["ShaftToMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5976": ["SpecialisedAssemblyCompoundHarmonicAnalysis"],
        "_5977": ["SpiralBevelGearCompoundHarmonicAnalysis"],
        "_5978": ["SpiralBevelGearMeshCompoundHarmonicAnalysis"],
        "_5979": ["SpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5980": ["SpringDamperCompoundHarmonicAnalysis"],
        "_5981": ["SpringDamperConnectionCompoundHarmonicAnalysis"],
        "_5982": ["SpringDamperHalfCompoundHarmonicAnalysis"],
        "_5983": ["StraightBevelDiffGearCompoundHarmonicAnalysis"],
        "_5984": ["StraightBevelDiffGearMeshCompoundHarmonicAnalysis"],
        "_5985": ["StraightBevelDiffGearSetCompoundHarmonicAnalysis"],
        "_5986": ["StraightBevelGearCompoundHarmonicAnalysis"],
        "_5987": ["StraightBevelGearMeshCompoundHarmonicAnalysis"],
        "_5988": ["StraightBevelGearSetCompoundHarmonicAnalysis"],
        "_5989": ["StraightBevelPlanetGearCompoundHarmonicAnalysis"],
        "_5990": ["StraightBevelSunGearCompoundHarmonicAnalysis"],
        "_5991": ["SynchroniserCompoundHarmonicAnalysis"],
        "_5992": ["SynchroniserHalfCompoundHarmonicAnalysis"],
        "_5993": ["SynchroniserPartCompoundHarmonicAnalysis"],
        "_5994": ["SynchroniserSleeveCompoundHarmonicAnalysis"],
        "_5995": ["TorqueConverterCompoundHarmonicAnalysis"],
        "_5996": ["TorqueConverterConnectionCompoundHarmonicAnalysis"],
        "_5997": ["TorqueConverterPumpCompoundHarmonicAnalysis"],
        "_5998": ["TorqueConverterTurbineCompoundHarmonicAnalysis"],
        "_5999": ["UnbalancedMassCompoundHarmonicAnalysis"],
        "_6000": ["VirtualComponentCompoundHarmonicAnalysis"],
        "_6001": ["WormGearCompoundHarmonicAnalysis"],
        "_6002": ["WormGearMeshCompoundHarmonicAnalysis"],
        "_6003": ["WormGearSetCompoundHarmonicAnalysis"],
        "_6004": ["ZerolBevelGearCompoundHarmonicAnalysis"],
        "_6005": ["ZerolBevelGearMeshCompoundHarmonicAnalysis"],
        "_6006": ["ZerolBevelGearSetCompoundHarmonicAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundHarmonicAnalysis",
    "AbstractShaftCompoundHarmonicAnalysis",
    "AbstractShaftOrHousingCompoundHarmonicAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
    "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
    "AssemblyCompoundHarmonicAnalysis",
    "BearingCompoundHarmonicAnalysis",
    "BeltConnectionCompoundHarmonicAnalysis",
    "BeltDriveCompoundHarmonicAnalysis",
    "BevelDifferentialGearCompoundHarmonicAnalysis",
    "BevelDifferentialGearMeshCompoundHarmonicAnalysis",
    "BevelDifferentialGearSetCompoundHarmonicAnalysis",
    "BevelDifferentialPlanetGearCompoundHarmonicAnalysis",
    "BevelDifferentialSunGearCompoundHarmonicAnalysis",
    "BevelGearCompoundHarmonicAnalysis",
    "BevelGearMeshCompoundHarmonicAnalysis",
    "BevelGearSetCompoundHarmonicAnalysis",
    "BoltCompoundHarmonicAnalysis",
    "BoltedJointCompoundHarmonicAnalysis",
    "ClutchCompoundHarmonicAnalysis",
    "ClutchConnectionCompoundHarmonicAnalysis",
    "ClutchHalfCompoundHarmonicAnalysis",
    "CoaxialConnectionCompoundHarmonicAnalysis",
    "ComponentCompoundHarmonicAnalysis",
    "ConceptCouplingCompoundHarmonicAnalysis",
    "ConceptCouplingConnectionCompoundHarmonicAnalysis",
    "ConceptCouplingHalfCompoundHarmonicAnalysis",
    "ConceptGearCompoundHarmonicAnalysis",
    "ConceptGearMeshCompoundHarmonicAnalysis",
    "ConceptGearSetCompoundHarmonicAnalysis",
    "ConicalGearCompoundHarmonicAnalysis",
    "ConicalGearMeshCompoundHarmonicAnalysis",
    "ConicalGearSetCompoundHarmonicAnalysis",
    "ConnectionCompoundHarmonicAnalysis",
    "ConnectorCompoundHarmonicAnalysis",
    "CouplingCompoundHarmonicAnalysis",
    "CouplingConnectionCompoundHarmonicAnalysis",
    "CouplingHalfCompoundHarmonicAnalysis",
    "CVTBeltConnectionCompoundHarmonicAnalysis",
    "CVTCompoundHarmonicAnalysis",
    "CVTPulleyCompoundHarmonicAnalysis",
    "CycloidalAssemblyCompoundHarmonicAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis",
    "CycloidalDiscCompoundHarmonicAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis",
    "CylindricalGearCompoundHarmonicAnalysis",
    "CylindricalGearMeshCompoundHarmonicAnalysis",
    "CylindricalGearSetCompoundHarmonicAnalysis",
    "CylindricalPlanetGearCompoundHarmonicAnalysis",
    "DatumCompoundHarmonicAnalysis",
    "ExternalCADModelCompoundHarmonicAnalysis",
    "FaceGearCompoundHarmonicAnalysis",
    "FaceGearMeshCompoundHarmonicAnalysis",
    "FaceGearSetCompoundHarmonicAnalysis",
    "FEPartCompoundHarmonicAnalysis",
    "FlexiblePinAssemblyCompoundHarmonicAnalysis",
    "GearCompoundHarmonicAnalysis",
    "GearMeshCompoundHarmonicAnalysis",
    "GearSetCompoundHarmonicAnalysis",
    "GuideDxfModelCompoundHarmonicAnalysis",
    "HypoidGearCompoundHarmonicAnalysis",
    "HypoidGearMeshCompoundHarmonicAnalysis",
    "HypoidGearSetCompoundHarmonicAnalysis",
    "InterMountableComponentConnectionCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis",
    "MassDiscCompoundHarmonicAnalysis",
    "MeasurementComponentCompoundHarmonicAnalysis",
    "MountableComponentCompoundHarmonicAnalysis",
    "OilSealCompoundHarmonicAnalysis",
    "PartCompoundHarmonicAnalysis",
    "PartToPartShearCouplingCompoundHarmonicAnalysis",
    "PartToPartShearCouplingConnectionCompoundHarmonicAnalysis",
    "PartToPartShearCouplingHalfCompoundHarmonicAnalysis",
    "PlanetaryConnectionCompoundHarmonicAnalysis",
    "PlanetaryGearSetCompoundHarmonicAnalysis",
    "PlanetCarrierCompoundHarmonicAnalysis",
    "PointLoadCompoundHarmonicAnalysis",
    "PowerLoadCompoundHarmonicAnalysis",
    "PulleyCompoundHarmonicAnalysis",
    "RingPinsCompoundHarmonicAnalysis",
    "RingPinsToDiscConnectionCompoundHarmonicAnalysis",
    "RollingRingAssemblyCompoundHarmonicAnalysis",
    "RollingRingCompoundHarmonicAnalysis",
    "RollingRingConnectionCompoundHarmonicAnalysis",
    "RootAssemblyCompoundHarmonicAnalysis",
    "ShaftCompoundHarmonicAnalysis",
    "ShaftHubConnectionCompoundHarmonicAnalysis",
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysis",
    "SpecialisedAssemblyCompoundHarmonicAnalysis",
    "SpiralBevelGearCompoundHarmonicAnalysis",
    "SpiralBevelGearMeshCompoundHarmonicAnalysis",
    "SpiralBevelGearSetCompoundHarmonicAnalysis",
    "SpringDamperCompoundHarmonicAnalysis",
    "SpringDamperConnectionCompoundHarmonicAnalysis",
    "SpringDamperHalfCompoundHarmonicAnalysis",
    "StraightBevelDiffGearCompoundHarmonicAnalysis",
    "StraightBevelDiffGearMeshCompoundHarmonicAnalysis",
    "StraightBevelDiffGearSetCompoundHarmonicAnalysis",
    "StraightBevelGearCompoundHarmonicAnalysis",
    "StraightBevelGearMeshCompoundHarmonicAnalysis",
    "StraightBevelGearSetCompoundHarmonicAnalysis",
    "StraightBevelPlanetGearCompoundHarmonicAnalysis",
    "StraightBevelSunGearCompoundHarmonicAnalysis",
    "SynchroniserCompoundHarmonicAnalysis",
    "SynchroniserHalfCompoundHarmonicAnalysis",
    "SynchroniserPartCompoundHarmonicAnalysis",
    "SynchroniserSleeveCompoundHarmonicAnalysis",
    "TorqueConverterCompoundHarmonicAnalysis",
    "TorqueConverterConnectionCompoundHarmonicAnalysis",
    "TorqueConverterPumpCompoundHarmonicAnalysis",
    "TorqueConverterTurbineCompoundHarmonicAnalysis",
    "UnbalancedMassCompoundHarmonicAnalysis",
    "VirtualComponentCompoundHarmonicAnalysis",
    "WormGearCompoundHarmonicAnalysis",
    "WormGearMeshCompoundHarmonicAnalysis",
    "WormGearSetCompoundHarmonicAnalysis",
    "ZerolBevelGearCompoundHarmonicAnalysis",
    "ZerolBevelGearMeshCompoundHarmonicAnalysis",
    "ZerolBevelGearSetCompoundHarmonicAnalysis",
)

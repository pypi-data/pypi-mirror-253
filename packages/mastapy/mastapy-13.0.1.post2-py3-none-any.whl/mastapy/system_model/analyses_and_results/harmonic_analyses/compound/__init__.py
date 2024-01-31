"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5879 import AbstractAssemblyCompoundHarmonicAnalysis
    from ._5880 import AbstractShaftCompoundHarmonicAnalysis
    from ._5881 import AbstractShaftOrHousingCompoundHarmonicAnalysis
    from ._5882 import (
        AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis,
    )
    from ._5883 import AGMAGleasonConicalGearCompoundHarmonicAnalysis
    from ._5884 import AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
    from ._5885 import AGMAGleasonConicalGearSetCompoundHarmonicAnalysis
    from ._5886 import AssemblyCompoundHarmonicAnalysis
    from ._5887 import BearingCompoundHarmonicAnalysis
    from ._5888 import BeltConnectionCompoundHarmonicAnalysis
    from ._5889 import BeltDriveCompoundHarmonicAnalysis
    from ._5890 import BevelDifferentialGearCompoundHarmonicAnalysis
    from ._5891 import BevelDifferentialGearMeshCompoundHarmonicAnalysis
    from ._5892 import BevelDifferentialGearSetCompoundHarmonicAnalysis
    from ._5893 import BevelDifferentialPlanetGearCompoundHarmonicAnalysis
    from ._5894 import BevelDifferentialSunGearCompoundHarmonicAnalysis
    from ._5895 import BevelGearCompoundHarmonicAnalysis
    from ._5896 import BevelGearMeshCompoundHarmonicAnalysis
    from ._5897 import BevelGearSetCompoundHarmonicAnalysis
    from ._5898 import BoltCompoundHarmonicAnalysis
    from ._5899 import BoltedJointCompoundHarmonicAnalysis
    from ._5900 import ClutchCompoundHarmonicAnalysis
    from ._5901 import ClutchConnectionCompoundHarmonicAnalysis
    from ._5902 import ClutchHalfCompoundHarmonicAnalysis
    from ._5903 import CoaxialConnectionCompoundHarmonicAnalysis
    from ._5904 import ComponentCompoundHarmonicAnalysis
    from ._5905 import ConceptCouplingCompoundHarmonicAnalysis
    from ._5906 import ConceptCouplingConnectionCompoundHarmonicAnalysis
    from ._5907 import ConceptCouplingHalfCompoundHarmonicAnalysis
    from ._5908 import ConceptGearCompoundHarmonicAnalysis
    from ._5909 import ConceptGearMeshCompoundHarmonicAnalysis
    from ._5910 import ConceptGearSetCompoundHarmonicAnalysis
    from ._5911 import ConicalGearCompoundHarmonicAnalysis
    from ._5912 import ConicalGearMeshCompoundHarmonicAnalysis
    from ._5913 import ConicalGearSetCompoundHarmonicAnalysis
    from ._5914 import ConnectionCompoundHarmonicAnalysis
    from ._5915 import ConnectorCompoundHarmonicAnalysis
    from ._5916 import CouplingCompoundHarmonicAnalysis
    from ._5917 import CouplingConnectionCompoundHarmonicAnalysis
    from ._5918 import CouplingHalfCompoundHarmonicAnalysis
    from ._5919 import CVTBeltConnectionCompoundHarmonicAnalysis
    from ._5920 import CVTCompoundHarmonicAnalysis
    from ._5921 import CVTPulleyCompoundHarmonicAnalysis
    from ._5922 import CycloidalAssemblyCompoundHarmonicAnalysis
    from ._5923 import CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis
    from ._5924 import CycloidalDiscCompoundHarmonicAnalysis
    from ._5925 import CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis
    from ._5926 import CylindricalGearCompoundHarmonicAnalysis
    from ._5927 import CylindricalGearMeshCompoundHarmonicAnalysis
    from ._5928 import CylindricalGearSetCompoundHarmonicAnalysis
    from ._5929 import CylindricalPlanetGearCompoundHarmonicAnalysis
    from ._5930 import DatumCompoundHarmonicAnalysis
    from ._5931 import ExternalCADModelCompoundHarmonicAnalysis
    from ._5932 import FaceGearCompoundHarmonicAnalysis
    from ._5933 import FaceGearMeshCompoundHarmonicAnalysis
    from ._5934 import FaceGearSetCompoundHarmonicAnalysis
    from ._5935 import FEPartCompoundHarmonicAnalysis
    from ._5936 import FlexiblePinAssemblyCompoundHarmonicAnalysis
    from ._5937 import GearCompoundHarmonicAnalysis
    from ._5938 import GearMeshCompoundHarmonicAnalysis
    from ._5939 import GearSetCompoundHarmonicAnalysis
    from ._5940 import GuideDxfModelCompoundHarmonicAnalysis
    from ._5941 import HypoidGearCompoundHarmonicAnalysis
    from ._5942 import HypoidGearMeshCompoundHarmonicAnalysis
    from ._5943 import HypoidGearSetCompoundHarmonicAnalysis
    from ._5944 import InterMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5945 import KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
    from ._5946 import KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
    from ._5947 import KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis
    from ._5948 import KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis
    from ._5949 import KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
    from ._5950 import KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis
    from ._5951 import KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis
    from ._5952 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis,
    )
    from ._5953 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis,
    )
    from ._5954 import MassDiscCompoundHarmonicAnalysis
    from ._5955 import MeasurementComponentCompoundHarmonicAnalysis
    from ._5956 import MountableComponentCompoundHarmonicAnalysis
    from ._5957 import OilSealCompoundHarmonicAnalysis
    from ._5958 import PartCompoundHarmonicAnalysis
    from ._5959 import PartToPartShearCouplingCompoundHarmonicAnalysis
    from ._5960 import PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
    from ._5961 import PartToPartShearCouplingHalfCompoundHarmonicAnalysis
    from ._5962 import PlanetaryConnectionCompoundHarmonicAnalysis
    from ._5963 import PlanetaryGearSetCompoundHarmonicAnalysis
    from ._5964 import PlanetCarrierCompoundHarmonicAnalysis
    from ._5965 import PointLoadCompoundHarmonicAnalysis
    from ._5966 import PowerLoadCompoundHarmonicAnalysis
    from ._5967 import PulleyCompoundHarmonicAnalysis
    from ._5968 import RingPinsCompoundHarmonicAnalysis
    from ._5969 import RingPinsToDiscConnectionCompoundHarmonicAnalysis
    from ._5970 import RollingRingAssemblyCompoundHarmonicAnalysis
    from ._5971 import RollingRingCompoundHarmonicAnalysis
    from ._5972 import RollingRingConnectionCompoundHarmonicAnalysis
    from ._5973 import RootAssemblyCompoundHarmonicAnalysis
    from ._5974 import ShaftCompoundHarmonicAnalysis
    from ._5975 import ShaftHubConnectionCompoundHarmonicAnalysis
    from ._5976 import ShaftToMountableComponentConnectionCompoundHarmonicAnalysis
    from ._5977 import SpecialisedAssemblyCompoundHarmonicAnalysis
    from ._5978 import SpiralBevelGearCompoundHarmonicAnalysis
    from ._5979 import SpiralBevelGearMeshCompoundHarmonicAnalysis
    from ._5980 import SpiralBevelGearSetCompoundHarmonicAnalysis
    from ._5981 import SpringDamperCompoundHarmonicAnalysis
    from ._5982 import SpringDamperConnectionCompoundHarmonicAnalysis
    from ._5983 import SpringDamperHalfCompoundHarmonicAnalysis
    from ._5984 import StraightBevelDiffGearCompoundHarmonicAnalysis
    from ._5985 import StraightBevelDiffGearMeshCompoundHarmonicAnalysis
    from ._5986 import StraightBevelDiffGearSetCompoundHarmonicAnalysis
    from ._5987 import StraightBevelGearCompoundHarmonicAnalysis
    from ._5988 import StraightBevelGearMeshCompoundHarmonicAnalysis
    from ._5989 import StraightBevelGearSetCompoundHarmonicAnalysis
    from ._5990 import StraightBevelPlanetGearCompoundHarmonicAnalysis
    from ._5991 import StraightBevelSunGearCompoundHarmonicAnalysis
    from ._5992 import SynchroniserCompoundHarmonicAnalysis
    from ._5993 import SynchroniserHalfCompoundHarmonicAnalysis
    from ._5994 import SynchroniserPartCompoundHarmonicAnalysis
    from ._5995 import SynchroniserSleeveCompoundHarmonicAnalysis
    from ._5996 import TorqueConverterCompoundHarmonicAnalysis
    from ._5997 import TorqueConverterConnectionCompoundHarmonicAnalysis
    from ._5998 import TorqueConverterPumpCompoundHarmonicAnalysis
    from ._5999 import TorqueConverterTurbineCompoundHarmonicAnalysis
    from ._6000 import UnbalancedMassCompoundHarmonicAnalysis
    from ._6001 import VirtualComponentCompoundHarmonicAnalysis
    from ._6002 import WormGearCompoundHarmonicAnalysis
    from ._6003 import WormGearMeshCompoundHarmonicAnalysis
    from ._6004 import WormGearSetCompoundHarmonicAnalysis
    from ._6005 import ZerolBevelGearCompoundHarmonicAnalysis
    from ._6006 import ZerolBevelGearMeshCompoundHarmonicAnalysis
    from ._6007 import ZerolBevelGearSetCompoundHarmonicAnalysis
else:
    import_structure = {
        "_5879": ["AbstractAssemblyCompoundHarmonicAnalysis"],
        "_5880": ["AbstractShaftCompoundHarmonicAnalysis"],
        "_5881": ["AbstractShaftOrHousingCompoundHarmonicAnalysis"],
        "_5882": [
            "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysis"
        ],
        "_5883": ["AGMAGleasonConicalGearCompoundHarmonicAnalysis"],
        "_5884": ["AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis"],
        "_5885": ["AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"],
        "_5886": ["AssemblyCompoundHarmonicAnalysis"],
        "_5887": ["BearingCompoundHarmonicAnalysis"],
        "_5888": ["BeltConnectionCompoundHarmonicAnalysis"],
        "_5889": ["BeltDriveCompoundHarmonicAnalysis"],
        "_5890": ["BevelDifferentialGearCompoundHarmonicAnalysis"],
        "_5891": ["BevelDifferentialGearMeshCompoundHarmonicAnalysis"],
        "_5892": ["BevelDifferentialGearSetCompoundHarmonicAnalysis"],
        "_5893": ["BevelDifferentialPlanetGearCompoundHarmonicAnalysis"],
        "_5894": ["BevelDifferentialSunGearCompoundHarmonicAnalysis"],
        "_5895": ["BevelGearCompoundHarmonicAnalysis"],
        "_5896": ["BevelGearMeshCompoundHarmonicAnalysis"],
        "_5897": ["BevelGearSetCompoundHarmonicAnalysis"],
        "_5898": ["BoltCompoundHarmonicAnalysis"],
        "_5899": ["BoltedJointCompoundHarmonicAnalysis"],
        "_5900": ["ClutchCompoundHarmonicAnalysis"],
        "_5901": ["ClutchConnectionCompoundHarmonicAnalysis"],
        "_5902": ["ClutchHalfCompoundHarmonicAnalysis"],
        "_5903": ["CoaxialConnectionCompoundHarmonicAnalysis"],
        "_5904": ["ComponentCompoundHarmonicAnalysis"],
        "_5905": ["ConceptCouplingCompoundHarmonicAnalysis"],
        "_5906": ["ConceptCouplingConnectionCompoundHarmonicAnalysis"],
        "_5907": ["ConceptCouplingHalfCompoundHarmonicAnalysis"],
        "_5908": ["ConceptGearCompoundHarmonicAnalysis"],
        "_5909": ["ConceptGearMeshCompoundHarmonicAnalysis"],
        "_5910": ["ConceptGearSetCompoundHarmonicAnalysis"],
        "_5911": ["ConicalGearCompoundHarmonicAnalysis"],
        "_5912": ["ConicalGearMeshCompoundHarmonicAnalysis"],
        "_5913": ["ConicalGearSetCompoundHarmonicAnalysis"],
        "_5914": ["ConnectionCompoundHarmonicAnalysis"],
        "_5915": ["ConnectorCompoundHarmonicAnalysis"],
        "_5916": ["CouplingCompoundHarmonicAnalysis"],
        "_5917": ["CouplingConnectionCompoundHarmonicAnalysis"],
        "_5918": ["CouplingHalfCompoundHarmonicAnalysis"],
        "_5919": ["CVTBeltConnectionCompoundHarmonicAnalysis"],
        "_5920": ["CVTCompoundHarmonicAnalysis"],
        "_5921": ["CVTPulleyCompoundHarmonicAnalysis"],
        "_5922": ["CycloidalAssemblyCompoundHarmonicAnalysis"],
        "_5923": ["CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysis"],
        "_5924": ["CycloidalDiscCompoundHarmonicAnalysis"],
        "_5925": ["CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysis"],
        "_5926": ["CylindricalGearCompoundHarmonicAnalysis"],
        "_5927": ["CylindricalGearMeshCompoundHarmonicAnalysis"],
        "_5928": ["CylindricalGearSetCompoundHarmonicAnalysis"],
        "_5929": ["CylindricalPlanetGearCompoundHarmonicAnalysis"],
        "_5930": ["DatumCompoundHarmonicAnalysis"],
        "_5931": ["ExternalCADModelCompoundHarmonicAnalysis"],
        "_5932": ["FaceGearCompoundHarmonicAnalysis"],
        "_5933": ["FaceGearMeshCompoundHarmonicAnalysis"],
        "_5934": ["FaceGearSetCompoundHarmonicAnalysis"],
        "_5935": ["FEPartCompoundHarmonicAnalysis"],
        "_5936": ["FlexiblePinAssemblyCompoundHarmonicAnalysis"],
        "_5937": ["GearCompoundHarmonicAnalysis"],
        "_5938": ["GearMeshCompoundHarmonicAnalysis"],
        "_5939": ["GearSetCompoundHarmonicAnalysis"],
        "_5940": ["GuideDxfModelCompoundHarmonicAnalysis"],
        "_5941": ["HypoidGearCompoundHarmonicAnalysis"],
        "_5942": ["HypoidGearMeshCompoundHarmonicAnalysis"],
        "_5943": ["HypoidGearSetCompoundHarmonicAnalysis"],
        "_5944": ["InterMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5945": ["KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis"],
        "_5946": ["KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis"],
        "_5947": ["KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysis"],
        "_5948": ["KlingelnbergCycloPalloidHypoidGearCompoundHarmonicAnalysis"],
        "_5949": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis"],
        "_5950": ["KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysis"],
        "_5951": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis"],
        "_5952": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis"
        ],
        "_5953": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5954": ["MassDiscCompoundHarmonicAnalysis"],
        "_5955": ["MeasurementComponentCompoundHarmonicAnalysis"],
        "_5956": ["MountableComponentCompoundHarmonicAnalysis"],
        "_5957": ["OilSealCompoundHarmonicAnalysis"],
        "_5958": ["PartCompoundHarmonicAnalysis"],
        "_5959": ["PartToPartShearCouplingCompoundHarmonicAnalysis"],
        "_5960": ["PartToPartShearCouplingConnectionCompoundHarmonicAnalysis"],
        "_5961": ["PartToPartShearCouplingHalfCompoundHarmonicAnalysis"],
        "_5962": ["PlanetaryConnectionCompoundHarmonicAnalysis"],
        "_5963": ["PlanetaryGearSetCompoundHarmonicAnalysis"],
        "_5964": ["PlanetCarrierCompoundHarmonicAnalysis"],
        "_5965": ["PointLoadCompoundHarmonicAnalysis"],
        "_5966": ["PowerLoadCompoundHarmonicAnalysis"],
        "_5967": ["PulleyCompoundHarmonicAnalysis"],
        "_5968": ["RingPinsCompoundHarmonicAnalysis"],
        "_5969": ["RingPinsToDiscConnectionCompoundHarmonicAnalysis"],
        "_5970": ["RollingRingAssemblyCompoundHarmonicAnalysis"],
        "_5971": ["RollingRingCompoundHarmonicAnalysis"],
        "_5972": ["RollingRingConnectionCompoundHarmonicAnalysis"],
        "_5973": ["RootAssemblyCompoundHarmonicAnalysis"],
        "_5974": ["ShaftCompoundHarmonicAnalysis"],
        "_5975": ["ShaftHubConnectionCompoundHarmonicAnalysis"],
        "_5976": ["ShaftToMountableComponentConnectionCompoundHarmonicAnalysis"],
        "_5977": ["SpecialisedAssemblyCompoundHarmonicAnalysis"],
        "_5978": ["SpiralBevelGearCompoundHarmonicAnalysis"],
        "_5979": ["SpiralBevelGearMeshCompoundHarmonicAnalysis"],
        "_5980": ["SpiralBevelGearSetCompoundHarmonicAnalysis"],
        "_5981": ["SpringDamperCompoundHarmonicAnalysis"],
        "_5982": ["SpringDamperConnectionCompoundHarmonicAnalysis"],
        "_5983": ["SpringDamperHalfCompoundHarmonicAnalysis"],
        "_5984": ["StraightBevelDiffGearCompoundHarmonicAnalysis"],
        "_5985": ["StraightBevelDiffGearMeshCompoundHarmonicAnalysis"],
        "_5986": ["StraightBevelDiffGearSetCompoundHarmonicAnalysis"],
        "_5987": ["StraightBevelGearCompoundHarmonicAnalysis"],
        "_5988": ["StraightBevelGearMeshCompoundHarmonicAnalysis"],
        "_5989": ["StraightBevelGearSetCompoundHarmonicAnalysis"],
        "_5990": ["StraightBevelPlanetGearCompoundHarmonicAnalysis"],
        "_5991": ["StraightBevelSunGearCompoundHarmonicAnalysis"],
        "_5992": ["SynchroniserCompoundHarmonicAnalysis"],
        "_5993": ["SynchroniserHalfCompoundHarmonicAnalysis"],
        "_5994": ["SynchroniserPartCompoundHarmonicAnalysis"],
        "_5995": ["SynchroniserSleeveCompoundHarmonicAnalysis"],
        "_5996": ["TorqueConverterCompoundHarmonicAnalysis"],
        "_5997": ["TorqueConverterConnectionCompoundHarmonicAnalysis"],
        "_5998": ["TorqueConverterPumpCompoundHarmonicAnalysis"],
        "_5999": ["TorqueConverterTurbineCompoundHarmonicAnalysis"],
        "_6000": ["UnbalancedMassCompoundHarmonicAnalysis"],
        "_6001": ["VirtualComponentCompoundHarmonicAnalysis"],
        "_6002": ["WormGearCompoundHarmonicAnalysis"],
        "_6003": ["WormGearMeshCompoundHarmonicAnalysis"],
        "_6004": ["WormGearSetCompoundHarmonicAnalysis"],
        "_6005": ["ZerolBevelGearCompoundHarmonicAnalysis"],
        "_6006": ["ZerolBevelGearMeshCompoundHarmonicAnalysis"],
        "_6007": ["ZerolBevelGearSetCompoundHarmonicAnalysis"],
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

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4988 import AbstractAssemblyCompoundModalAnalysisAtAStiffness
    from ._4989 import AbstractShaftCompoundModalAnalysisAtAStiffness
    from ._4990 import AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
    from ._4991 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._4992 import AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
    from ._4993 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._4994 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._4995 import AssemblyCompoundModalAnalysisAtAStiffness
    from ._4996 import BearingCompoundModalAnalysisAtAStiffness
    from ._4997 import BeltConnectionCompoundModalAnalysisAtAStiffness
    from ._4998 import BeltDriveCompoundModalAnalysisAtAStiffness
    from ._4999 import BevelDifferentialGearCompoundModalAnalysisAtAStiffness
    from ._5000 import BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
    from ._5001 import BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
    from ._5002 import BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5003 import BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
    from ._5004 import BevelGearCompoundModalAnalysisAtAStiffness
    from ._5005 import BevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5006 import BevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5007 import BoltCompoundModalAnalysisAtAStiffness
    from ._5008 import BoltedJointCompoundModalAnalysisAtAStiffness
    from ._5009 import ClutchCompoundModalAnalysisAtAStiffness
    from ._5010 import ClutchConnectionCompoundModalAnalysisAtAStiffness
    from ._5011 import ClutchHalfCompoundModalAnalysisAtAStiffness
    from ._5012 import CoaxialConnectionCompoundModalAnalysisAtAStiffness
    from ._5013 import ComponentCompoundModalAnalysisAtAStiffness
    from ._5014 import ConceptCouplingCompoundModalAnalysisAtAStiffness
    from ._5015 import ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5016 import ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5017 import ConceptGearCompoundModalAnalysisAtAStiffness
    from ._5018 import ConceptGearMeshCompoundModalAnalysisAtAStiffness
    from ._5019 import ConceptGearSetCompoundModalAnalysisAtAStiffness
    from ._5020 import ConicalGearCompoundModalAnalysisAtAStiffness
    from ._5021 import ConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5022 import ConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5023 import ConnectionCompoundModalAnalysisAtAStiffness
    from ._5024 import ConnectorCompoundModalAnalysisAtAStiffness
    from ._5025 import CouplingCompoundModalAnalysisAtAStiffness
    from ._5026 import CouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5027 import CouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5028 import CVTBeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5029 import CVTCompoundModalAnalysisAtAStiffness
    from ._5030 import CVTPulleyCompoundModalAnalysisAtAStiffness
    from ._5031 import CycloidalAssemblyCompoundModalAnalysisAtAStiffness
    from ._5032 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5033 import CycloidalDiscCompoundModalAnalysisAtAStiffness
    from ._5034 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5035 import CylindricalGearCompoundModalAnalysisAtAStiffness
    from ._5036 import CylindricalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5037 import CylindricalGearSetCompoundModalAnalysisAtAStiffness
    from ._5038 import CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5039 import DatumCompoundModalAnalysisAtAStiffness
    from ._5040 import ExternalCADModelCompoundModalAnalysisAtAStiffness
    from ._5041 import FaceGearCompoundModalAnalysisAtAStiffness
    from ._5042 import FaceGearMeshCompoundModalAnalysisAtAStiffness
    from ._5043 import FaceGearSetCompoundModalAnalysisAtAStiffness
    from ._5044 import FEPartCompoundModalAnalysisAtAStiffness
    from ._5045 import FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
    from ._5046 import GearCompoundModalAnalysisAtAStiffness
    from ._5047 import GearMeshCompoundModalAnalysisAtAStiffness
    from ._5048 import GearSetCompoundModalAnalysisAtAStiffness
    from ._5049 import GuideDxfModelCompoundModalAnalysisAtAStiffness
    from ._5050 import HypoidGearCompoundModalAnalysisAtAStiffness
    from ._5051 import HypoidGearMeshCompoundModalAnalysisAtAStiffness
    from ._5052 import HypoidGearSetCompoundModalAnalysisAtAStiffness
    from ._5053 import (
        InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5054 import (
        KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5055 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5056 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5057 import (
        KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5058 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5059 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5060 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5061 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5062 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5063 import MassDiscCompoundModalAnalysisAtAStiffness
    from ._5064 import MeasurementComponentCompoundModalAnalysisAtAStiffness
    from ._5065 import MountableComponentCompoundModalAnalysisAtAStiffness
    from ._5066 import OilSealCompoundModalAnalysisAtAStiffness
    from ._5067 import PartCompoundModalAnalysisAtAStiffness
    from ._5068 import PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
    from ._5069 import (
        PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5070 import PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5071 import PlanetaryConnectionCompoundModalAnalysisAtAStiffness
    from ._5072 import PlanetaryGearSetCompoundModalAnalysisAtAStiffness
    from ._5073 import PlanetCarrierCompoundModalAnalysisAtAStiffness
    from ._5074 import PointLoadCompoundModalAnalysisAtAStiffness
    from ._5075 import PowerLoadCompoundModalAnalysisAtAStiffness
    from ._5076 import PulleyCompoundModalAnalysisAtAStiffness
    from ._5077 import RingPinsCompoundModalAnalysisAtAStiffness
    from ._5078 import RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
    from ._5079 import RollingRingAssemblyCompoundModalAnalysisAtAStiffness
    from ._5080 import RollingRingCompoundModalAnalysisAtAStiffness
    from ._5081 import RollingRingConnectionCompoundModalAnalysisAtAStiffness
    from ._5082 import RootAssemblyCompoundModalAnalysisAtAStiffness
    from ._5083 import ShaftCompoundModalAnalysisAtAStiffness
    from ._5084 import ShaftHubConnectionCompoundModalAnalysisAtAStiffness
    from ._5085 import (
        ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5086 import SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
    from ._5087 import SpiralBevelGearCompoundModalAnalysisAtAStiffness
    from ._5088 import SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5089 import SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5090 import SpringDamperCompoundModalAnalysisAtAStiffness
    from ._5091 import SpringDamperConnectionCompoundModalAnalysisAtAStiffness
    from ._5092 import SpringDamperHalfCompoundModalAnalysisAtAStiffness
    from ._5093 import StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
    from ._5094 import StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
    from ._5095 import StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
    from ._5096 import StraightBevelGearCompoundModalAnalysisAtAStiffness
    from ._5097 import StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5098 import StraightBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5099 import StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5100 import StraightBevelSunGearCompoundModalAnalysisAtAStiffness
    from ._5101 import SynchroniserCompoundModalAnalysisAtAStiffness
    from ._5102 import SynchroniserHalfCompoundModalAnalysisAtAStiffness
    from ._5103 import SynchroniserPartCompoundModalAnalysisAtAStiffness
    from ._5104 import SynchroniserSleeveCompoundModalAnalysisAtAStiffness
    from ._5105 import TorqueConverterCompoundModalAnalysisAtAStiffness
    from ._5106 import TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
    from ._5107 import TorqueConverterPumpCompoundModalAnalysisAtAStiffness
    from ._5108 import TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
    from ._5109 import UnbalancedMassCompoundModalAnalysisAtAStiffness
    from ._5110 import VirtualComponentCompoundModalAnalysisAtAStiffness
    from ._5111 import WormGearCompoundModalAnalysisAtAStiffness
    from ._5112 import WormGearMeshCompoundModalAnalysisAtAStiffness
    from ._5113 import WormGearSetCompoundModalAnalysisAtAStiffness
    from ._5114 import ZerolBevelGearCompoundModalAnalysisAtAStiffness
    from ._5115 import ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5116 import ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
else:
    import_structure = {
        "_4988": ["AbstractAssemblyCompoundModalAnalysisAtAStiffness"],
        "_4989": ["AbstractShaftCompoundModalAnalysisAtAStiffness"],
        "_4990": ["AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness"],
        "_4991": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_4992": ["AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness"],
        "_4993": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_4994": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_4995": ["AssemblyCompoundModalAnalysisAtAStiffness"],
        "_4996": ["BearingCompoundModalAnalysisAtAStiffness"],
        "_4997": ["BeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_4998": ["BeltDriveCompoundModalAnalysisAtAStiffness"],
        "_4999": ["BevelDifferentialGearCompoundModalAnalysisAtAStiffness"],
        "_5000": ["BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5001": ["BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness"],
        "_5002": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5003": ["BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness"],
        "_5004": ["BevelGearCompoundModalAnalysisAtAStiffness"],
        "_5005": ["BevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5006": ["BevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5007": ["BoltCompoundModalAnalysisAtAStiffness"],
        "_5008": ["BoltedJointCompoundModalAnalysisAtAStiffness"],
        "_5009": ["ClutchCompoundModalAnalysisAtAStiffness"],
        "_5010": ["ClutchConnectionCompoundModalAnalysisAtAStiffness"],
        "_5011": ["ClutchHalfCompoundModalAnalysisAtAStiffness"],
        "_5012": ["CoaxialConnectionCompoundModalAnalysisAtAStiffness"],
        "_5013": ["ComponentCompoundModalAnalysisAtAStiffness"],
        "_5014": ["ConceptCouplingCompoundModalAnalysisAtAStiffness"],
        "_5015": ["ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5016": ["ConceptCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5017": ["ConceptGearCompoundModalAnalysisAtAStiffness"],
        "_5018": ["ConceptGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5019": ["ConceptGearSetCompoundModalAnalysisAtAStiffness"],
        "_5020": ["ConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5021": ["ConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5022": ["ConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5023": ["ConnectionCompoundModalAnalysisAtAStiffness"],
        "_5024": ["ConnectorCompoundModalAnalysisAtAStiffness"],
        "_5025": ["CouplingCompoundModalAnalysisAtAStiffness"],
        "_5026": ["CouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5027": ["CouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5028": ["CVTBeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5029": ["CVTCompoundModalAnalysisAtAStiffness"],
        "_5030": ["CVTPulleyCompoundModalAnalysisAtAStiffness"],
        "_5031": ["CycloidalAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5032": [
            "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5033": ["CycloidalDiscCompoundModalAnalysisAtAStiffness"],
        "_5034": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5035": ["CylindricalGearCompoundModalAnalysisAtAStiffness"],
        "_5036": ["CylindricalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5037": ["CylindricalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5038": ["CylindricalPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5039": ["DatumCompoundModalAnalysisAtAStiffness"],
        "_5040": ["ExternalCADModelCompoundModalAnalysisAtAStiffness"],
        "_5041": ["FaceGearCompoundModalAnalysisAtAStiffness"],
        "_5042": ["FaceGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5043": ["FaceGearSetCompoundModalAnalysisAtAStiffness"],
        "_5044": ["FEPartCompoundModalAnalysisAtAStiffness"],
        "_5045": ["FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5046": ["GearCompoundModalAnalysisAtAStiffness"],
        "_5047": ["GearMeshCompoundModalAnalysisAtAStiffness"],
        "_5048": ["GearSetCompoundModalAnalysisAtAStiffness"],
        "_5049": ["GuideDxfModelCompoundModalAnalysisAtAStiffness"],
        "_5050": ["HypoidGearCompoundModalAnalysisAtAStiffness"],
        "_5051": ["HypoidGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5052": ["HypoidGearSetCompoundModalAnalysisAtAStiffness"],
        "_5053": ["InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"],
        "_5054": [
            "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5055": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5056": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5057": [
            "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5058": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5059": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5060": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5061": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5062": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5063": ["MassDiscCompoundModalAnalysisAtAStiffness"],
        "_5064": ["MeasurementComponentCompoundModalAnalysisAtAStiffness"],
        "_5065": ["MountableComponentCompoundModalAnalysisAtAStiffness"],
        "_5066": ["OilSealCompoundModalAnalysisAtAStiffness"],
        "_5067": ["PartCompoundModalAnalysisAtAStiffness"],
        "_5068": ["PartToPartShearCouplingCompoundModalAnalysisAtAStiffness"],
        "_5069": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5070": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5071": ["PlanetaryConnectionCompoundModalAnalysisAtAStiffness"],
        "_5072": ["PlanetaryGearSetCompoundModalAnalysisAtAStiffness"],
        "_5073": ["PlanetCarrierCompoundModalAnalysisAtAStiffness"],
        "_5074": ["PointLoadCompoundModalAnalysisAtAStiffness"],
        "_5075": ["PowerLoadCompoundModalAnalysisAtAStiffness"],
        "_5076": ["PulleyCompoundModalAnalysisAtAStiffness"],
        "_5077": ["RingPinsCompoundModalAnalysisAtAStiffness"],
        "_5078": ["RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness"],
        "_5079": ["RollingRingAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5080": ["RollingRingCompoundModalAnalysisAtAStiffness"],
        "_5081": ["RollingRingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5082": ["RootAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5083": ["ShaftCompoundModalAnalysisAtAStiffness"],
        "_5084": ["ShaftHubConnectionCompoundModalAnalysisAtAStiffness"],
        "_5085": [
            "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5086": ["SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5087": ["SpiralBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5088": ["SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5089": ["SpiralBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5090": ["SpringDamperCompoundModalAnalysisAtAStiffness"],
        "_5091": ["SpringDamperConnectionCompoundModalAnalysisAtAStiffness"],
        "_5092": ["SpringDamperHalfCompoundModalAnalysisAtAStiffness"],
        "_5093": ["StraightBevelDiffGearCompoundModalAnalysisAtAStiffness"],
        "_5094": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5095": ["StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness"],
        "_5096": ["StraightBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5097": ["StraightBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5098": ["StraightBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5099": ["StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5100": ["StraightBevelSunGearCompoundModalAnalysisAtAStiffness"],
        "_5101": ["SynchroniserCompoundModalAnalysisAtAStiffness"],
        "_5102": ["SynchroniserHalfCompoundModalAnalysisAtAStiffness"],
        "_5103": ["SynchroniserPartCompoundModalAnalysisAtAStiffness"],
        "_5104": ["SynchroniserSleeveCompoundModalAnalysisAtAStiffness"],
        "_5105": ["TorqueConverterCompoundModalAnalysisAtAStiffness"],
        "_5106": ["TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"],
        "_5107": ["TorqueConverterPumpCompoundModalAnalysisAtAStiffness"],
        "_5108": ["TorqueConverterTurbineCompoundModalAnalysisAtAStiffness"],
        "_5109": ["UnbalancedMassCompoundModalAnalysisAtAStiffness"],
        "_5110": ["VirtualComponentCompoundModalAnalysisAtAStiffness"],
        "_5111": ["WormGearCompoundModalAnalysisAtAStiffness"],
        "_5112": ["WormGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5113": ["WormGearSetCompoundModalAnalysisAtAStiffness"],
        "_5114": ["ZerolBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5115": ["ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5116": ["ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtAStiffness",
    "AbstractShaftCompoundModalAnalysisAtAStiffness",
    "AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness",
    "AssemblyCompoundModalAnalysisAtAStiffness",
    "BearingCompoundModalAnalysisAtAStiffness",
    "BeltConnectionCompoundModalAnalysisAtAStiffness",
    "BeltDriveCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness",
    "BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness",
    "BevelGearCompoundModalAnalysisAtAStiffness",
    "BevelGearMeshCompoundModalAnalysisAtAStiffness",
    "BevelGearSetCompoundModalAnalysisAtAStiffness",
    "BoltCompoundModalAnalysisAtAStiffness",
    "BoltedJointCompoundModalAnalysisAtAStiffness",
    "ClutchCompoundModalAnalysisAtAStiffness",
    "ClutchConnectionCompoundModalAnalysisAtAStiffness",
    "ClutchHalfCompoundModalAnalysisAtAStiffness",
    "CoaxialConnectionCompoundModalAnalysisAtAStiffness",
    "ComponentCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "ConceptCouplingHalfCompoundModalAnalysisAtAStiffness",
    "ConceptGearCompoundModalAnalysisAtAStiffness",
    "ConceptGearMeshCompoundModalAnalysisAtAStiffness",
    "ConceptGearSetCompoundModalAnalysisAtAStiffness",
    "ConicalGearCompoundModalAnalysisAtAStiffness",
    "ConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "ConicalGearSetCompoundModalAnalysisAtAStiffness",
    "ConnectionCompoundModalAnalysisAtAStiffness",
    "ConnectorCompoundModalAnalysisAtAStiffness",
    "CouplingCompoundModalAnalysisAtAStiffness",
    "CouplingConnectionCompoundModalAnalysisAtAStiffness",
    "CouplingHalfCompoundModalAnalysisAtAStiffness",
    "CVTBeltConnectionCompoundModalAnalysisAtAStiffness",
    "CVTCompoundModalAnalysisAtAStiffness",
    "CVTPulleyCompoundModalAnalysisAtAStiffness",
    "CycloidalAssemblyCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscCompoundModalAnalysisAtAStiffness",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness",
    "CylindricalGearCompoundModalAnalysisAtAStiffness",
    "CylindricalGearMeshCompoundModalAnalysisAtAStiffness",
    "CylindricalGearSetCompoundModalAnalysisAtAStiffness",
    "CylindricalPlanetGearCompoundModalAnalysisAtAStiffness",
    "DatumCompoundModalAnalysisAtAStiffness",
    "ExternalCADModelCompoundModalAnalysisAtAStiffness",
    "FaceGearCompoundModalAnalysisAtAStiffness",
    "FaceGearMeshCompoundModalAnalysisAtAStiffness",
    "FaceGearSetCompoundModalAnalysisAtAStiffness",
    "FEPartCompoundModalAnalysisAtAStiffness",
    "FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness",
    "GearCompoundModalAnalysisAtAStiffness",
    "GearMeshCompoundModalAnalysisAtAStiffness",
    "GearSetCompoundModalAnalysisAtAStiffness",
    "GuideDxfModelCompoundModalAnalysisAtAStiffness",
    "HypoidGearCompoundModalAnalysisAtAStiffness",
    "HypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "HypoidGearSetCompoundModalAnalysisAtAStiffness",
    "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "MassDiscCompoundModalAnalysisAtAStiffness",
    "MeasurementComponentCompoundModalAnalysisAtAStiffness",
    "MountableComponentCompoundModalAnalysisAtAStiffness",
    "OilSealCompoundModalAnalysisAtAStiffness",
    "PartCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness",
    "PlanetaryConnectionCompoundModalAnalysisAtAStiffness",
    "PlanetaryGearSetCompoundModalAnalysisAtAStiffness",
    "PlanetCarrierCompoundModalAnalysisAtAStiffness",
    "PointLoadCompoundModalAnalysisAtAStiffness",
    "PowerLoadCompoundModalAnalysisAtAStiffness",
    "PulleyCompoundModalAnalysisAtAStiffness",
    "RingPinsCompoundModalAnalysisAtAStiffness",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness",
    "RollingRingAssemblyCompoundModalAnalysisAtAStiffness",
    "RollingRingCompoundModalAnalysisAtAStiffness",
    "RollingRingConnectionCompoundModalAnalysisAtAStiffness",
    "RootAssemblyCompoundModalAnalysisAtAStiffness",
    "ShaftCompoundModalAnalysisAtAStiffness",
    "ShaftHubConnectionCompoundModalAnalysisAtAStiffness",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    "SpecialisedAssemblyCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "SpiralBevelGearSetCompoundModalAnalysisAtAStiffness",
    "SpringDamperCompoundModalAnalysisAtAStiffness",
    "SpringDamperConnectionCompoundModalAnalysisAtAStiffness",
    "SpringDamperHalfCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "StraightBevelGearSetCompoundModalAnalysisAtAStiffness",
    "StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness",
    "StraightBevelSunGearCompoundModalAnalysisAtAStiffness",
    "SynchroniserCompoundModalAnalysisAtAStiffness",
    "SynchroniserHalfCompoundModalAnalysisAtAStiffness",
    "SynchroniserPartCompoundModalAnalysisAtAStiffness",
    "SynchroniserSleeveCompoundModalAnalysisAtAStiffness",
    "TorqueConverterCompoundModalAnalysisAtAStiffness",
    "TorqueConverterConnectionCompoundModalAnalysisAtAStiffness",
    "TorqueConverterPumpCompoundModalAnalysisAtAStiffness",
    "TorqueConverterTurbineCompoundModalAnalysisAtAStiffness",
    "UnbalancedMassCompoundModalAnalysisAtAStiffness",
    "VirtualComponentCompoundModalAnalysisAtAStiffness",
    "WormGearCompoundModalAnalysisAtAStiffness",
    "WormGearMeshCompoundModalAnalysisAtAStiffness",
    "WormGearSetCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness",
    "ZerolBevelGearSetCompoundModalAnalysisAtAStiffness",
)

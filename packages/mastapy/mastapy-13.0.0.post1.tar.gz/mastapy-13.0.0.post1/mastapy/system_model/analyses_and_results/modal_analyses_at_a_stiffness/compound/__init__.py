"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4987 import AbstractAssemblyCompoundModalAnalysisAtAStiffness
    from ._4988 import AbstractShaftCompoundModalAnalysisAtAStiffness
    from ._4989 import AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
    from ._4990 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._4991 import AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
    from ._4992 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._4993 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._4994 import AssemblyCompoundModalAnalysisAtAStiffness
    from ._4995 import BearingCompoundModalAnalysisAtAStiffness
    from ._4996 import BeltConnectionCompoundModalAnalysisAtAStiffness
    from ._4997 import BeltDriveCompoundModalAnalysisAtAStiffness
    from ._4998 import BevelDifferentialGearCompoundModalAnalysisAtAStiffness
    from ._4999 import BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
    from ._5000 import BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
    from ._5001 import BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5002 import BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
    from ._5003 import BevelGearCompoundModalAnalysisAtAStiffness
    from ._5004 import BevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5005 import BevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5006 import BoltCompoundModalAnalysisAtAStiffness
    from ._5007 import BoltedJointCompoundModalAnalysisAtAStiffness
    from ._5008 import ClutchCompoundModalAnalysisAtAStiffness
    from ._5009 import ClutchConnectionCompoundModalAnalysisAtAStiffness
    from ._5010 import ClutchHalfCompoundModalAnalysisAtAStiffness
    from ._5011 import CoaxialConnectionCompoundModalAnalysisAtAStiffness
    from ._5012 import ComponentCompoundModalAnalysisAtAStiffness
    from ._5013 import ConceptCouplingCompoundModalAnalysisAtAStiffness
    from ._5014 import ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5015 import ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5016 import ConceptGearCompoundModalAnalysisAtAStiffness
    from ._5017 import ConceptGearMeshCompoundModalAnalysisAtAStiffness
    from ._5018 import ConceptGearSetCompoundModalAnalysisAtAStiffness
    from ._5019 import ConicalGearCompoundModalAnalysisAtAStiffness
    from ._5020 import ConicalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5021 import ConicalGearSetCompoundModalAnalysisAtAStiffness
    from ._5022 import ConnectionCompoundModalAnalysisAtAStiffness
    from ._5023 import ConnectorCompoundModalAnalysisAtAStiffness
    from ._5024 import CouplingCompoundModalAnalysisAtAStiffness
    from ._5025 import CouplingConnectionCompoundModalAnalysisAtAStiffness
    from ._5026 import CouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5027 import CVTBeltConnectionCompoundModalAnalysisAtAStiffness
    from ._5028 import CVTCompoundModalAnalysisAtAStiffness
    from ._5029 import CVTPulleyCompoundModalAnalysisAtAStiffness
    from ._5030 import CycloidalAssemblyCompoundModalAnalysisAtAStiffness
    from ._5031 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5032 import CycloidalDiscCompoundModalAnalysisAtAStiffness
    from ._5033 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5034 import CylindricalGearCompoundModalAnalysisAtAStiffness
    from ._5035 import CylindricalGearMeshCompoundModalAnalysisAtAStiffness
    from ._5036 import CylindricalGearSetCompoundModalAnalysisAtAStiffness
    from ._5037 import CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5038 import DatumCompoundModalAnalysisAtAStiffness
    from ._5039 import ExternalCADModelCompoundModalAnalysisAtAStiffness
    from ._5040 import FaceGearCompoundModalAnalysisAtAStiffness
    from ._5041 import FaceGearMeshCompoundModalAnalysisAtAStiffness
    from ._5042 import FaceGearSetCompoundModalAnalysisAtAStiffness
    from ._5043 import FEPartCompoundModalAnalysisAtAStiffness
    from ._5044 import FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
    from ._5045 import GearCompoundModalAnalysisAtAStiffness
    from ._5046 import GearMeshCompoundModalAnalysisAtAStiffness
    from ._5047 import GearSetCompoundModalAnalysisAtAStiffness
    from ._5048 import GuideDxfModelCompoundModalAnalysisAtAStiffness
    from ._5049 import HypoidGearCompoundModalAnalysisAtAStiffness
    from ._5050 import HypoidGearMeshCompoundModalAnalysisAtAStiffness
    from ._5051 import HypoidGearSetCompoundModalAnalysisAtAStiffness
    from ._5052 import (
        InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5053 import (
        KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5054 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5055 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5056 import (
        KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5057 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5058 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5059 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness,
    )
    from ._5060 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness,
    )
    from ._5061 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness,
    )
    from ._5062 import MassDiscCompoundModalAnalysisAtAStiffness
    from ._5063 import MeasurementComponentCompoundModalAnalysisAtAStiffness
    from ._5064 import MountableComponentCompoundModalAnalysisAtAStiffness
    from ._5065 import OilSealCompoundModalAnalysisAtAStiffness
    from ._5066 import PartCompoundModalAnalysisAtAStiffness
    from ._5067 import PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
    from ._5068 import (
        PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5069 import PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
    from ._5070 import PlanetaryConnectionCompoundModalAnalysisAtAStiffness
    from ._5071 import PlanetaryGearSetCompoundModalAnalysisAtAStiffness
    from ._5072 import PlanetCarrierCompoundModalAnalysisAtAStiffness
    from ._5073 import PointLoadCompoundModalAnalysisAtAStiffness
    from ._5074 import PowerLoadCompoundModalAnalysisAtAStiffness
    from ._5075 import PulleyCompoundModalAnalysisAtAStiffness
    from ._5076 import RingPinsCompoundModalAnalysisAtAStiffness
    from ._5077 import RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
    from ._5078 import RollingRingAssemblyCompoundModalAnalysisAtAStiffness
    from ._5079 import RollingRingCompoundModalAnalysisAtAStiffness
    from ._5080 import RollingRingConnectionCompoundModalAnalysisAtAStiffness
    from ._5081 import RootAssemblyCompoundModalAnalysisAtAStiffness
    from ._5082 import ShaftCompoundModalAnalysisAtAStiffness
    from ._5083 import ShaftHubConnectionCompoundModalAnalysisAtAStiffness
    from ._5084 import (
        ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness,
    )
    from ._5085 import SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
    from ._5086 import SpiralBevelGearCompoundModalAnalysisAtAStiffness
    from ._5087 import SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5088 import SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5089 import SpringDamperCompoundModalAnalysisAtAStiffness
    from ._5090 import SpringDamperConnectionCompoundModalAnalysisAtAStiffness
    from ._5091 import SpringDamperHalfCompoundModalAnalysisAtAStiffness
    from ._5092 import StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
    from ._5093 import StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
    from ._5094 import StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
    from ._5095 import StraightBevelGearCompoundModalAnalysisAtAStiffness
    from ._5096 import StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5097 import StraightBevelGearSetCompoundModalAnalysisAtAStiffness
    from ._5098 import StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
    from ._5099 import StraightBevelSunGearCompoundModalAnalysisAtAStiffness
    from ._5100 import SynchroniserCompoundModalAnalysisAtAStiffness
    from ._5101 import SynchroniserHalfCompoundModalAnalysisAtAStiffness
    from ._5102 import SynchroniserPartCompoundModalAnalysisAtAStiffness
    from ._5103 import SynchroniserSleeveCompoundModalAnalysisAtAStiffness
    from ._5104 import TorqueConverterCompoundModalAnalysisAtAStiffness
    from ._5105 import TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
    from ._5106 import TorqueConverterPumpCompoundModalAnalysisAtAStiffness
    from ._5107 import TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
    from ._5108 import UnbalancedMassCompoundModalAnalysisAtAStiffness
    from ._5109 import VirtualComponentCompoundModalAnalysisAtAStiffness
    from ._5110 import WormGearCompoundModalAnalysisAtAStiffness
    from ._5111 import WormGearMeshCompoundModalAnalysisAtAStiffness
    from ._5112 import WormGearSetCompoundModalAnalysisAtAStiffness
    from ._5113 import ZerolBevelGearCompoundModalAnalysisAtAStiffness
    from ._5114 import ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
    from ._5115 import ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
else:
    import_structure = {
        "_4987": ["AbstractAssemblyCompoundModalAnalysisAtAStiffness"],
        "_4988": ["AbstractShaftCompoundModalAnalysisAtAStiffness"],
        "_4989": ["AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness"],
        "_4990": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_4991": ["AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness"],
        "_4992": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_4993": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_4994": ["AssemblyCompoundModalAnalysisAtAStiffness"],
        "_4995": ["BearingCompoundModalAnalysisAtAStiffness"],
        "_4996": ["BeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_4997": ["BeltDriveCompoundModalAnalysisAtAStiffness"],
        "_4998": ["BevelDifferentialGearCompoundModalAnalysisAtAStiffness"],
        "_4999": ["BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5000": ["BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness"],
        "_5001": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5002": ["BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness"],
        "_5003": ["BevelGearCompoundModalAnalysisAtAStiffness"],
        "_5004": ["BevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5005": ["BevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5006": ["BoltCompoundModalAnalysisAtAStiffness"],
        "_5007": ["BoltedJointCompoundModalAnalysisAtAStiffness"],
        "_5008": ["ClutchCompoundModalAnalysisAtAStiffness"],
        "_5009": ["ClutchConnectionCompoundModalAnalysisAtAStiffness"],
        "_5010": ["ClutchHalfCompoundModalAnalysisAtAStiffness"],
        "_5011": ["CoaxialConnectionCompoundModalAnalysisAtAStiffness"],
        "_5012": ["ComponentCompoundModalAnalysisAtAStiffness"],
        "_5013": ["ConceptCouplingCompoundModalAnalysisAtAStiffness"],
        "_5014": ["ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5015": ["ConceptCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5016": ["ConceptGearCompoundModalAnalysisAtAStiffness"],
        "_5017": ["ConceptGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5018": ["ConceptGearSetCompoundModalAnalysisAtAStiffness"],
        "_5019": ["ConicalGearCompoundModalAnalysisAtAStiffness"],
        "_5020": ["ConicalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5021": ["ConicalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5022": ["ConnectionCompoundModalAnalysisAtAStiffness"],
        "_5023": ["ConnectorCompoundModalAnalysisAtAStiffness"],
        "_5024": ["CouplingCompoundModalAnalysisAtAStiffness"],
        "_5025": ["CouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5026": ["CouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5027": ["CVTBeltConnectionCompoundModalAnalysisAtAStiffness"],
        "_5028": ["CVTCompoundModalAnalysisAtAStiffness"],
        "_5029": ["CVTPulleyCompoundModalAnalysisAtAStiffness"],
        "_5030": ["CycloidalAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5031": [
            "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5032": ["CycloidalDiscCompoundModalAnalysisAtAStiffness"],
        "_5033": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5034": ["CylindricalGearCompoundModalAnalysisAtAStiffness"],
        "_5035": ["CylindricalGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5036": ["CylindricalGearSetCompoundModalAnalysisAtAStiffness"],
        "_5037": ["CylindricalPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5038": ["DatumCompoundModalAnalysisAtAStiffness"],
        "_5039": ["ExternalCADModelCompoundModalAnalysisAtAStiffness"],
        "_5040": ["FaceGearCompoundModalAnalysisAtAStiffness"],
        "_5041": ["FaceGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5042": ["FaceGearSetCompoundModalAnalysisAtAStiffness"],
        "_5043": ["FEPartCompoundModalAnalysisAtAStiffness"],
        "_5044": ["FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5045": ["GearCompoundModalAnalysisAtAStiffness"],
        "_5046": ["GearMeshCompoundModalAnalysisAtAStiffness"],
        "_5047": ["GearSetCompoundModalAnalysisAtAStiffness"],
        "_5048": ["GuideDxfModelCompoundModalAnalysisAtAStiffness"],
        "_5049": ["HypoidGearCompoundModalAnalysisAtAStiffness"],
        "_5050": ["HypoidGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5051": ["HypoidGearSetCompoundModalAnalysisAtAStiffness"],
        "_5052": ["InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"],
        "_5053": [
            "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5054": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5055": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5056": [
            "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5057": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5058": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5059": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness"
        ],
        "_5060": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"
        ],
        "_5061": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness"
        ],
        "_5062": ["MassDiscCompoundModalAnalysisAtAStiffness"],
        "_5063": ["MeasurementComponentCompoundModalAnalysisAtAStiffness"],
        "_5064": ["MountableComponentCompoundModalAnalysisAtAStiffness"],
        "_5065": ["OilSealCompoundModalAnalysisAtAStiffness"],
        "_5066": ["PartCompoundModalAnalysisAtAStiffness"],
        "_5067": ["PartToPartShearCouplingCompoundModalAnalysisAtAStiffness"],
        "_5068": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5069": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness"],
        "_5070": ["PlanetaryConnectionCompoundModalAnalysisAtAStiffness"],
        "_5071": ["PlanetaryGearSetCompoundModalAnalysisAtAStiffness"],
        "_5072": ["PlanetCarrierCompoundModalAnalysisAtAStiffness"],
        "_5073": ["PointLoadCompoundModalAnalysisAtAStiffness"],
        "_5074": ["PowerLoadCompoundModalAnalysisAtAStiffness"],
        "_5075": ["PulleyCompoundModalAnalysisAtAStiffness"],
        "_5076": ["RingPinsCompoundModalAnalysisAtAStiffness"],
        "_5077": ["RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness"],
        "_5078": ["RollingRingAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5079": ["RollingRingCompoundModalAnalysisAtAStiffness"],
        "_5080": ["RollingRingConnectionCompoundModalAnalysisAtAStiffness"],
        "_5081": ["RootAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5082": ["ShaftCompoundModalAnalysisAtAStiffness"],
        "_5083": ["ShaftHubConnectionCompoundModalAnalysisAtAStiffness"],
        "_5084": [
            "ShaftToMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
        ],
        "_5085": ["SpecialisedAssemblyCompoundModalAnalysisAtAStiffness"],
        "_5086": ["SpiralBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5087": ["SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5088": ["SpiralBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5089": ["SpringDamperCompoundModalAnalysisAtAStiffness"],
        "_5090": ["SpringDamperConnectionCompoundModalAnalysisAtAStiffness"],
        "_5091": ["SpringDamperHalfCompoundModalAnalysisAtAStiffness"],
        "_5092": ["StraightBevelDiffGearCompoundModalAnalysisAtAStiffness"],
        "_5093": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5094": ["StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness"],
        "_5095": ["StraightBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5096": ["StraightBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5097": ["StraightBevelGearSetCompoundModalAnalysisAtAStiffness"],
        "_5098": ["StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness"],
        "_5099": ["StraightBevelSunGearCompoundModalAnalysisAtAStiffness"],
        "_5100": ["SynchroniserCompoundModalAnalysisAtAStiffness"],
        "_5101": ["SynchroniserHalfCompoundModalAnalysisAtAStiffness"],
        "_5102": ["SynchroniserPartCompoundModalAnalysisAtAStiffness"],
        "_5103": ["SynchroniserSleeveCompoundModalAnalysisAtAStiffness"],
        "_5104": ["TorqueConverterCompoundModalAnalysisAtAStiffness"],
        "_5105": ["TorqueConverterConnectionCompoundModalAnalysisAtAStiffness"],
        "_5106": ["TorqueConverterPumpCompoundModalAnalysisAtAStiffness"],
        "_5107": ["TorqueConverterTurbineCompoundModalAnalysisAtAStiffness"],
        "_5108": ["UnbalancedMassCompoundModalAnalysisAtAStiffness"],
        "_5109": ["VirtualComponentCompoundModalAnalysisAtAStiffness"],
        "_5110": ["WormGearCompoundModalAnalysisAtAStiffness"],
        "_5111": ["WormGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5112": ["WormGearSetCompoundModalAnalysisAtAStiffness"],
        "_5113": ["ZerolBevelGearCompoundModalAnalysisAtAStiffness"],
        "_5114": ["ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness"],
        "_5115": ["ZerolBevelGearSetCompoundModalAnalysisAtAStiffness"],
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

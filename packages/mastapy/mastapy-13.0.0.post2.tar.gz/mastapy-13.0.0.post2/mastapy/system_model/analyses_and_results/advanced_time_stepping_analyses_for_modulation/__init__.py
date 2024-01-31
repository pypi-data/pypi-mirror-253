"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7005 import AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7006 import AbstractShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7007 import AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
    from ._7008 import (
        AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7009 import AdvancedTimeSteppingAnalysisForModulation
    from ._7010 import AtsamExcitationsOrOthers
    from ._7011 import AtsamNaturalFrequencyViewOption
    from ._7012 import AdvancedTimeSteppingAnalysisForModulationOptions
    from ._7013 import AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7014 import (
        AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7015 import (
        AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7016 import AssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7017 import ATSAMResultsVsLargeTimeStepSettings
    from ._7018 import BearingAdvancedTimeSteppingAnalysisForModulation
    from ._7019 import BeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7020 import BeltDriveAdvancedTimeSteppingAnalysisForModulation
    from ._7021 import BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
    from ._7022 import (
        BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7023 import BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7024 import (
        BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7025 import BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7026 import BevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7027 import BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7028 import BevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7029 import BoltAdvancedTimeSteppingAnalysisForModulation
    from ._7030 import BoltedJointAdvancedTimeSteppingAnalysisForModulation
    from ._7031 import ClutchAdvancedTimeSteppingAnalysisForModulation
    from ._7032 import ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7033 import ClutchHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7034 import CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7035 import ComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7036 import ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7037 import (
        ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7038 import ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7039 import ConceptGearAdvancedTimeSteppingAnalysisForModulation
    from ._7040 import ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7041 import ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7042 import ConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7043 import ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7044 import ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7045 import ConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7046 import ConnectorAdvancedTimeSteppingAnalysisForModulation
    from ._7047 import CouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7048 import CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7049 import CouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7050 import CVTAdvancedTimeSteppingAnalysisForModulation
    from ._7051 import CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7052 import CVTPulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7053 import CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7054 import CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7055 import (
        CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7056 import (
        CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7057 import CylindricalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7058 import CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7059 import CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7060 import CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7061 import DatumAdvancedTimeSteppingAnalysisForModulation
    from ._7062 import ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
    from ._7063 import FaceGearAdvancedTimeSteppingAnalysisForModulation
    from ._7064 import FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7065 import FaceGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7066 import FEPartAdvancedTimeSteppingAnalysisForModulation
    from ._7067 import FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7068 import GearAdvancedTimeSteppingAnalysisForModulation
    from ._7069 import GearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7070 import GearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7071 import GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
    from ._7072 import (
        HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7073 import HypoidGearAdvancedTimeSteppingAnalysisForModulation
    from ._7074 import HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7075 import HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7076 import (
        InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7077 import (
        KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7078 import (
        KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7079 import (
        KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7080 import (
        KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7081 import (
        KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7082 import (
        KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7083 import (
        KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7084 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7085 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7086 import MassDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7087 import MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7088 import MountableComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7089 import OilSealAdvancedTimeSteppingAnalysisForModulation
    from ._7090 import PartAdvancedTimeSteppingAnalysisForModulation
    from ._7091 import PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7092 import (
        PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7093 import (
        PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7094 import PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7095 import PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7096 import PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
    from ._7097 import PointLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7098 import PowerLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7099 import PulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7100 import RingPinsAdvancedTimeSteppingAnalysisForModulation
    from ._7101 import RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7102 import RollingRingAdvancedTimeSteppingAnalysisForModulation
    from ._7103 import RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7104 import RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7105 import RootAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7106 import ShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7107 import ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7108 import (
        ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7109 import SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7110 import SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7111 import SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7112 import SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7113 import SpringDamperAdvancedTimeSteppingAnalysisForModulation
    from ._7114 import SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7115 import SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7116 import StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
    from ._7117 import (
        StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7118 import StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7119 import StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7120 import StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7121 import StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7122 import StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7123 import StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7124 import SynchroniserAdvancedTimeSteppingAnalysisForModulation
    from ._7125 import SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7126 import SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
    from ._7127 import SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
    from ._7128 import TorqueConverterAdvancedTimeSteppingAnalysisForModulation
    from ._7129 import (
        TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7130 import TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
    from ._7131 import TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
    from ._7132 import UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
    from ._7133 import VirtualComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7134 import WormGearAdvancedTimeSteppingAnalysisForModulation
    from ._7135 import WormGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7136 import WormGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7137 import ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7138 import ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7139 import ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
else:
    import_structure = {
        "_7005": ["AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7006": ["AbstractShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7007": ["AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"],
        "_7008": [
            "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7009": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_7010": ["AtsamExcitationsOrOthers"],
        "_7011": ["AtsamNaturalFrequencyViewOption"],
        "_7012": ["AdvancedTimeSteppingAnalysisForModulationOptions"],
        "_7013": ["AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7014": [
            "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7015": ["AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7016": ["AssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7017": ["ATSAMResultsVsLargeTimeStepSettings"],
        "_7018": ["BearingAdvancedTimeSteppingAnalysisForModulation"],
        "_7019": ["BeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7020": ["BeltDriveAdvancedTimeSteppingAnalysisForModulation"],
        "_7021": ["BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7022": ["BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7023": ["BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7024": [
            "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7025": ["BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7026": ["BevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7027": ["BevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7028": ["BevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7029": ["BoltAdvancedTimeSteppingAnalysisForModulation"],
        "_7030": ["BoltedJointAdvancedTimeSteppingAnalysisForModulation"],
        "_7031": ["ClutchAdvancedTimeSteppingAnalysisForModulation"],
        "_7032": ["ClutchConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7033": ["ClutchHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7034": ["CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7035": ["ComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7036": ["ConceptCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7037": ["ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7038": ["ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7039": ["ConceptGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7040": ["ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7041": ["ConceptGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7042": ["ConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7043": ["ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7044": ["ConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7045": ["ConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7046": ["ConnectorAdvancedTimeSteppingAnalysisForModulation"],
        "_7047": ["CouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7048": ["CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7049": ["CouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7050": ["CVTAdvancedTimeSteppingAnalysisForModulation"],
        "_7051": ["CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7052": ["CVTPulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7053": ["CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7054": ["CycloidalDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7055": [
            "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7056": [
            "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7057": ["CylindricalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7058": ["CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7059": ["CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7060": ["CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7061": ["DatumAdvancedTimeSteppingAnalysisForModulation"],
        "_7062": ["ExternalCADModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7063": ["FaceGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7064": ["FaceGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7065": ["FaceGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7066": ["FEPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7067": ["FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7068": ["GearAdvancedTimeSteppingAnalysisForModulation"],
        "_7069": ["GearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7070": ["GearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7071": ["GuideDxfModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7072": [
            "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7073": ["HypoidGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7074": ["HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7075": ["HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7076": [
            "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7077": [
            "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7078": [
            "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7079": [
            "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7080": [
            "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7081": [
            "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7082": [
            "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7083": [
            "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7084": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7085": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7086": ["MassDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7087": ["MeasurementComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7088": ["MountableComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7089": ["OilSealAdvancedTimeSteppingAnalysisForModulation"],
        "_7090": ["PartAdvancedTimeSteppingAnalysisForModulation"],
        "_7091": ["PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7092": [
            "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7093": [
            "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7094": ["PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7095": ["PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7096": ["PlanetCarrierAdvancedTimeSteppingAnalysisForModulation"],
        "_7097": ["PointLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7098": ["PowerLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7099": ["PulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7100": ["RingPinsAdvancedTimeSteppingAnalysisForModulation"],
        "_7101": ["RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7102": ["RollingRingAdvancedTimeSteppingAnalysisForModulation"],
        "_7103": ["RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7104": ["RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7105": ["RootAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7106": ["ShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7107": ["ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7108": [
            "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7109": ["SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7110": ["SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7111": ["SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7112": ["SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7113": ["SpringDamperAdvancedTimeSteppingAnalysisForModulation"],
        "_7114": ["SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7115": ["SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7116": ["StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7117": ["StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7118": ["StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7119": ["StraightBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7120": ["StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7121": ["StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7122": ["StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7123": ["StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7124": ["SynchroniserAdvancedTimeSteppingAnalysisForModulation"],
        "_7125": ["SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7126": ["SynchroniserPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7127": ["SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation"],
        "_7128": ["TorqueConverterAdvancedTimeSteppingAnalysisForModulation"],
        "_7129": ["TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7130": ["TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation"],
        "_7131": ["TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation"],
        "_7132": ["UnbalancedMassAdvancedTimeSteppingAnalysisForModulation"],
        "_7133": ["VirtualComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7134": ["WormGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7135": ["WormGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7136": ["WormGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7137": ["ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7138": ["ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7139": ["ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "AdvancedTimeSteppingAnalysisForModulation",
    "AtsamExcitationsOrOthers",
    "AtsamNaturalFrequencyViewOption",
    "AdvancedTimeSteppingAnalysisForModulationOptions",
    "AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ATSAMResultsVsLargeTimeStepSettings",
    "BearingAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "BoltAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointAdvancedTimeSteppingAnalysisForModulation",
    "ClutchAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ComponentAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorAdvancedTimeSteppingAnalysisForModulation",
    "CouplingAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "CVTAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "DatumAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetAdvancedTimeSteppingAnalysisForModulation",
    "FEPartAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "GearAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshAdvancedTimeSteppingAnalysisForModulation",
    "GearSetAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    "OilSealAdvancedTimeSteppingAnalysisForModulation",
    "PartAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadAdvancedTimeSteppingAnalysisForModulation",
    "PulleyAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "ShaftAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
    "WormGearAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)

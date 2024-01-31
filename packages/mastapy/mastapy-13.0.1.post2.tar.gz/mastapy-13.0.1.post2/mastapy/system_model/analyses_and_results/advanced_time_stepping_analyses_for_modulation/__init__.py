"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7006 import AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7007 import AbstractShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7008 import AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
    from ._7009 import (
        AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7010 import AdvancedTimeSteppingAnalysisForModulation
    from ._7011 import AtsamExcitationsOrOthers
    from ._7012 import AtsamNaturalFrequencyViewOption
    from ._7013 import AdvancedTimeSteppingAnalysisForModulationOptions
    from ._7014 import AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7015 import (
        AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7016 import (
        AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7017 import AssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7018 import ATSAMResultsVsLargeTimeStepSettings
    from ._7019 import BearingAdvancedTimeSteppingAnalysisForModulation
    from ._7020 import BeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7021 import BeltDriveAdvancedTimeSteppingAnalysisForModulation
    from ._7022 import BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
    from ._7023 import (
        BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7024 import BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7025 import (
        BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7026 import BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7027 import BevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7028 import BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7029 import BevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7030 import BoltAdvancedTimeSteppingAnalysisForModulation
    from ._7031 import BoltedJointAdvancedTimeSteppingAnalysisForModulation
    from ._7032 import ClutchAdvancedTimeSteppingAnalysisForModulation
    from ._7033 import ClutchConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7034 import ClutchHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7035 import CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7036 import ComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7037 import ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7038 import (
        ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7039 import ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7040 import ConceptGearAdvancedTimeSteppingAnalysisForModulation
    from ._7041 import ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7042 import ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7043 import ConicalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7044 import ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7045 import ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7046 import ConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7047 import ConnectorAdvancedTimeSteppingAnalysisForModulation
    from ._7048 import CouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7049 import CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7050 import CouplingHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7051 import CVTAdvancedTimeSteppingAnalysisForModulation
    from ._7052 import CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7053 import CVTPulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7054 import CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7055 import CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7056 import (
        CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7057 import (
        CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7058 import CylindricalGearAdvancedTimeSteppingAnalysisForModulation
    from ._7059 import CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7060 import CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7061 import CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7062 import DatumAdvancedTimeSteppingAnalysisForModulation
    from ._7063 import ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
    from ._7064 import FaceGearAdvancedTimeSteppingAnalysisForModulation
    from ._7065 import FaceGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7066 import FaceGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7067 import FEPartAdvancedTimeSteppingAnalysisForModulation
    from ._7068 import FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7069 import GearAdvancedTimeSteppingAnalysisForModulation
    from ._7070 import GearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7071 import GearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7072 import GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
    from ._7073 import (
        HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7074 import HypoidGearAdvancedTimeSteppingAnalysisForModulation
    from ._7075 import HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7076 import HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7077 import (
        InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7078 import (
        KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7079 import (
        KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7080 import (
        KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7081 import (
        KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7082 import (
        KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7083 import (
        KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7084 import (
        KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7085 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7086 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7087 import MassDiscAdvancedTimeSteppingAnalysisForModulation
    from ._7088 import MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7089 import MountableComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7090 import OilSealAdvancedTimeSteppingAnalysisForModulation
    from ._7091 import PartAdvancedTimeSteppingAnalysisForModulation
    from ._7092 import PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
    from ._7093 import (
        PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7094 import (
        PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7095 import PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7096 import PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7097 import PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
    from ._7098 import PointLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7099 import PowerLoadAdvancedTimeSteppingAnalysisForModulation
    from ._7100 import PulleyAdvancedTimeSteppingAnalysisForModulation
    from ._7101 import RingPinsAdvancedTimeSteppingAnalysisForModulation
    from ._7102 import RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7103 import RollingRingAdvancedTimeSteppingAnalysisForModulation
    from ._7104 import RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7105 import RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7106 import RootAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7107 import ShaftAdvancedTimeSteppingAnalysisForModulation
    from ._7108 import ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7109 import (
        ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7110 import SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
    from ._7111 import SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7112 import SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7113 import SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7114 import SpringDamperAdvancedTimeSteppingAnalysisForModulation
    from ._7115 import SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation
    from ._7116 import SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7117 import StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
    from ._7118 import (
        StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7119 import StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7120 import StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7121 import StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7122 import StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7123 import StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
    from ._7124 import StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
    from ._7125 import SynchroniserAdvancedTimeSteppingAnalysisForModulation
    from ._7126 import SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
    from ._7127 import SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
    from ._7128 import SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
    from ._7129 import TorqueConverterAdvancedTimeSteppingAnalysisForModulation
    from ._7130 import (
        TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7131 import TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
    from ._7132 import TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
    from ._7133 import UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
    from ._7134 import VirtualComponentAdvancedTimeSteppingAnalysisForModulation
    from ._7135 import WormGearAdvancedTimeSteppingAnalysisForModulation
    from ._7136 import WormGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7137 import WormGearSetAdvancedTimeSteppingAnalysisForModulation
    from ._7138 import ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
    from ._7139 import ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
    from ._7140 import ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
else:
    import_structure = {
        "_7006": ["AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7007": ["AbstractShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7008": ["AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation"],
        "_7009": [
            "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7010": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_7011": ["AtsamExcitationsOrOthers"],
        "_7012": ["AtsamNaturalFrequencyViewOption"],
        "_7013": ["AdvancedTimeSteppingAnalysisForModulationOptions"],
        "_7014": ["AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7015": [
            "AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7016": ["AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7017": ["AssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7018": ["ATSAMResultsVsLargeTimeStepSettings"],
        "_7019": ["BearingAdvancedTimeSteppingAnalysisForModulation"],
        "_7020": ["BeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7021": ["BeltDriveAdvancedTimeSteppingAnalysisForModulation"],
        "_7022": ["BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7023": ["BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7024": ["BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7025": [
            "BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7026": ["BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7027": ["BevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7028": ["BevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7029": ["BevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7030": ["BoltAdvancedTimeSteppingAnalysisForModulation"],
        "_7031": ["BoltedJointAdvancedTimeSteppingAnalysisForModulation"],
        "_7032": ["ClutchAdvancedTimeSteppingAnalysisForModulation"],
        "_7033": ["ClutchConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7034": ["ClutchHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7035": ["CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7036": ["ComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7037": ["ConceptCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7038": ["ConceptCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7039": ["ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7040": ["ConceptGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7041": ["ConceptGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7042": ["ConceptGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7043": ["ConicalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7044": ["ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7045": ["ConicalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7046": ["ConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7047": ["ConnectorAdvancedTimeSteppingAnalysisForModulation"],
        "_7048": ["CouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7049": ["CouplingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7050": ["CouplingHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7051": ["CVTAdvancedTimeSteppingAnalysisForModulation"],
        "_7052": ["CVTBeltConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7053": ["CVTPulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7054": ["CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7055": ["CycloidalDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7056": [
            "CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7057": [
            "CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7058": ["CylindricalGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7059": ["CylindricalGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7060": ["CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7061": ["CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7062": ["DatumAdvancedTimeSteppingAnalysisForModulation"],
        "_7063": ["ExternalCADModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7064": ["FaceGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7065": ["FaceGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7066": ["FaceGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7067": ["FEPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7068": ["FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7069": ["GearAdvancedTimeSteppingAnalysisForModulation"],
        "_7070": ["GearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7071": ["GearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7072": ["GuideDxfModelAdvancedTimeSteppingAnalysisForModulation"],
        "_7073": [
            "HarmonicAnalysisOptionsForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7074": ["HypoidGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7075": ["HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7076": ["HypoidGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7077": [
            "InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7078": [
            "KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7079": [
            "KlingelnbergCycloPalloidConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7080": [
            "KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7081": [
            "KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7082": [
            "KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7083": [
            "KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7084": [
            "KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7085": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7086": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7087": ["MassDiscAdvancedTimeSteppingAnalysisForModulation"],
        "_7088": ["MeasurementComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7089": ["MountableComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7090": ["OilSealAdvancedTimeSteppingAnalysisForModulation"],
        "_7091": ["PartAdvancedTimeSteppingAnalysisForModulation"],
        "_7092": ["PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation"],
        "_7093": [
            "PartToPartShearCouplingConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7094": [
            "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7095": ["PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7096": ["PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7097": ["PlanetCarrierAdvancedTimeSteppingAnalysisForModulation"],
        "_7098": ["PointLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7099": ["PowerLoadAdvancedTimeSteppingAnalysisForModulation"],
        "_7100": ["PulleyAdvancedTimeSteppingAnalysisForModulation"],
        "_7101": ["RingPinsAdvancedTimeSteppingAnalysisForModulation"],
        "_7102": ["RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7103": ["RollingRingAdvancedTimeSteppingAnalysisForModulation"],
        "_7104": ["RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7105": ["RollingRingConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7106": ["RootAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7107": ["ShaftAdvancedTimeSteppingAnalysisForModulation"],
        "_7108": ["ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7109": [
            "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7110": ["SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation"],
        "_7111": ["SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7112": ["SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7113": ["SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7114": ["SpringDamperAdvancedTimeSteppingAnalysisForModulation"],
        "_7115": ["SpringDamperConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7116": ["SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7117": ["StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7118": ["StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7119": ["StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7120": ["StraightBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7121": ["StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7122": ["StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7123": ["StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7124": ["StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7125": ["SynchroniserAdvancedTimeSteppingAnalysisForModulation"],
        "_7126": ["SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation"],
        "_7127": ["SynchroniserPartAdvancedTimeSteppingAnalysisForModulation"],
        "_7128": ["SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation"],
        "_7129": ["TorqueConverterAdvancedTimeSteppingAnalysisForModulation"],
        "_7130": ["TorqueConverterConnectionAdvancedTimeSteppingAnalysisForModulation"],
        "_7131": ["TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation"],
        "_7132": ["TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation"],
        "_7133": ["UnbalancedMassAdvancedTimeSteppingAnalysisForModulation"],
        "_7134": ["VirtualComponentAdvancedTimeSteppingAnalysisForModulation"],
        "_7135": ["WormGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7136": ["WormGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7137": ["WormGearSetAdvancedTimeSteppingAnalysisForModulation"],
        "_7138": ["ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation"],
        "_7139": ["ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"],
        "_7140": ["ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation"],
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

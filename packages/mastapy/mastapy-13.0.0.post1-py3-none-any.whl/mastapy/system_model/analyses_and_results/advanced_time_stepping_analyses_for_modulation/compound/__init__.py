"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7140 import AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7141 import AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7142 import (
        AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7143 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7144 import (
        AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7145 import (
        AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7146 import (
        AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7147 import AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7148 import BearingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7149 import BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7150 import BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7151 import (
        BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7152 import (
        BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7153 import (
        BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7154 import (
        BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7155 import (
        BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7156 import BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7157 import BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7158 import BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7159 import BoltCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7160 import BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7161 import ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7162 import ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7163 import ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7164 import (
        CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7165 import ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7166 import ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7167 import (
        ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7168 import (
        ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7169 import ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7170 import ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7171 import ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7172 import ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7173 import ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7174 import ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7175 import ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7176 import ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7177 import CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7178 import (
        CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7179 import CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7180 import (
        CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7181 import CVTCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7182 import CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7183 import (
        CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7184 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7185 import CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7186 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7187 import CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7188 import (
        CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7189 import (
        CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7190 import (
        CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7191 import DatumCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7192 import ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7193 import FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7194 import FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7195 import FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7196 import FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7197 import (
        FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7198 import GearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7199 import GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7200 import GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7201 import GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7202 import HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7203 import HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7204 import HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7205 import (
        InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7206 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7207 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7208 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7209 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7210 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7211 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7212 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7213 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7214 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7215 import MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7216 import (
        MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7217 import (
        MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7218 import OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7219 import PartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7220 import (
        PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7221 import (
        PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7222 import (
        PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7223 import (
        PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7224 import PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7225 import PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7226 import PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7227 import PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7228 import PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7229 import RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7230 import (
        RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7231 import (
        RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7232 import RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7233 import (
        RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7234 import RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7235 import ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7236 import (
        ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7237 import (
        ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7238 import (
        SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7239 import SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7240 import (
        SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7241 import (
        SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7242 import SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7243 import (
        SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7244 import SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7245 import (
        StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7246 import (
        StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7247 import (
        StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7248 import (
        StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7249 import (
        StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7250 import (
        StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7251 import (
        StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7252 import (
        StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7253 import SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7254 import SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7255 import SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7256 import (
        SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7257 import TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7258 import (
        TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7259 import (
        TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7260 import (
        TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7261 import UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7262 import VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7263 import WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7264 import WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7265 import WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7266 import ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7267 import (
        ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7268 import (
        ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
else:
    import_structure = {
        "_7140": ["AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7141": ["AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7142": [
            "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7143": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7144": [
            "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7145": [
            "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7146": [
            "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7147": ["AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7148": ["BearingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7149": ["BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7150": ["BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7151": [
            "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7152": [
            "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7153": [
            "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7154": [
            "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7155": [
            "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7156": ["BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7157": ["BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7158": ["BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7159": ["BoltCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7160": ["BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7161": ["ClutchCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7162": ["ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7163": ["ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7164": ["CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7165": ["ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7166": ["ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7167": [
            "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7168": [
            "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7169": ["ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7170": ["ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7171": ["ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7172": ["ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7173": ["ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7174": ["ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7175": ["ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7176": ["ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7177": ["CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7178": [
            "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7179": ["CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7180": ["CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7181": ["CVTCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7182": ["CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7183": ["CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7184": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7185": ["CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7186": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7187": ["CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7188": [
            "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7189": [
            "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7190": [
            "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7191": ["DatumCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7192": ["ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7193": ["FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7194": ["FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7195": ["FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7196": ["FEPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7197": [
            "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7198": ["GearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7199": ["GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7200": ["GearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7201": ["GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7202": ["HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7203": ["HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7204": ["HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7205": [
            "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7206": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7207": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7208": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7209": [
            "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7210": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7211": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7212": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7213": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7214": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7215": ["MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7216": [
            "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7217": [
            "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7218": ["OilSealCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7219": ["PartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7220": [
            "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7221": [
            "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7222": [
            "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7223": [
            "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7224": ["PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7225": ["PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7226": ["PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7227": ["PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7228": ["PulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7229": ["RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7230": [
            "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7231": [
            "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7232": ["RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7233": [
            "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7234": ["RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7235": ["ShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7236": [
            "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7237": [
            "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7238": [
            "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7239": ["SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7240": [
            "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7241": [
            "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7242": ["SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7243": [
            "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7244": ["SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7245": [
            "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7246": [
            "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7247": [
            "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7248": ["StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7249": [
            "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7250": [
            "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7251": [
            "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7252": [
            "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7253": ["SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7254": ["SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7255": ["SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7256": [
            "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7257": ["TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7258": [
            "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7259": [
            "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7260": [
            "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7261": ["UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7262": ["VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7263": ["WormGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7264": ["WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7265": ["WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7266": ["ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7267": [
            "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7268": ["ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BearingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltCompoundAdvancedTimeSteppingAnalysisForModulation",
    "BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "DatumCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FEPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "OilSealCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation",
    "PulleyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation",
    "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation",
    "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation",
    "UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation",
    "VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    "ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)

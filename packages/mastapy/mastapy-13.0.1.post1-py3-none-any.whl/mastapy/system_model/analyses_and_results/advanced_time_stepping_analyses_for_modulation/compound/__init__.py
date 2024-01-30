"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7141 import AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7142 import AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7143 import (
        AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7144 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7145 import (
        AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7146 import (
        AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7147 import (
        AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7148 import AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7149 import BearingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7150 import BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7151 import BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7152 import (
        BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7153 import (
        BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7154 import (
        BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7155 import (
        BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7156 import (
        BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7157 import BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7158 import BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7159 import BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7160 import BoltCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7161 import BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7162 import ClutchCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7163 import ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7164 import ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7165 import (
        CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7166 import ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7167 import ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7168 import (
        ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7169 import (
        ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7170 import ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7171 import ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7172 import ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7173 import ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7174 import ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7175 import ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7176 import ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7177 import ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7178 import CouplingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7179 import (
        CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7180 import CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7181 import (
        CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7182 import CVTCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7183 import CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7184 import (
        CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7185 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7186 import CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7187 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7188 import CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7189 import (
        CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7190 import (
        CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7191 import (
        CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7192 import DatumCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7193 import ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7194 import FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7195 import FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7196 import FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7197 import FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7198 import (
        FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7199 import GearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7200 import GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7201 import GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7202 import GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7203 import HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7204 import HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7205 import HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7206 import (
        InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7207 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7208 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7209 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7210 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7211 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7212 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7213 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7214 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7215 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7216 import MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7217 import (
        MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7218 import (
        MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7219 import OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7220 import PartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7221 import (
        PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7222 import (
        PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7223 import (
        PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7224 import (
        PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7225 import PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7226 import PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7227 import PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7228 import PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7229 import PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7230 import RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7231 import (
        RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7232 import (
        RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7233 import RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7234 import (
        RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7235 import RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7236 import ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7237 import (
        ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7238 import (
        ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7239 import (
        SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7240 import SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7241 import (
        SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7242 import (
        SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7243 import SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7244 import (
        SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7245 import SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7246 import (
        StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7247 import (
        StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7248 import (
        StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7249 import (
        StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7250 import (
        StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7251 import (
        StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7252 import (
        StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7253 import (
        StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7254 import SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7255 import SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7256 import SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7257 import (
        SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7258 import TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7259 import (
        TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7260 import (
        TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7261 import (
        TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7262 import UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7263 import VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7264 import WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7265 import WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7266 import WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7267 import ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
    from ._7268 import (
        ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._7269 import (
        ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation,
    )
else:
    import_structure = {
        "_7141": ["AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7142": ["AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7143": [
            "AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7144": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7145": [
            "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7146": [
            "AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7147": [
            "AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7148": ["AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7149": ["BearingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7150": ["BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7151": ["BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7152": [
            "BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7153": [
            "BevelDifferentialGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7154": [
            "BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7155": [
            "BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7156": [
            "BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7157": ["BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7158": ["BevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7159": ["BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7160": ["BoltCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7161": ["BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7162": ["ClutchCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7163": ["ClutchConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7164": ["ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7165": ["CoaxialConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7166": ["ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7167": ["ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7168": [
            "ConceptCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7169": [
            "ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7170": ["ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7171": ["ConceptGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7172": ["ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7173": ["ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7174": ["ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7175": ["ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7176": ["ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7177": ["ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7178": ["CouplingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7179": [
            "CouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7180": ["CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7181": ["CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7182": ["CVTCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7183": ["CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7184": ["CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7185": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7186": ["CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7187": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7188": ["CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7189": [
            "CylindricalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7190": [
            "CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7191": [
            "CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7192": ["DatumCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7193": ["ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7194": ["FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7195": ["FaceGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7196": ["FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7197": ["FEPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7198": [
            "FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7199": ["GearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7200": ["GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7201": ["GearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7202": ["GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7203": ["HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7204": ["HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7205": ["HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7206": [
            "InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7207": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7208": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7209": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7210": [
            "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7211": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7212": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7213": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7214": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7215": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7216": ["MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7217": [
            "MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7218": [
            "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7219": ["OilSealCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7220": ["PartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7221": [
            "PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7222": [
            "PartToPartShearCouplingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7223": [
            "PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7224": [
            "PlanetaryConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7225": ["PlanetaryGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7226": ["PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7227": ["PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7228": ["PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7229": ["PulleyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7230": ["RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7231": [
            "RingPinsToDiscConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7232": [
            "RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7233": ["RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7234": [
            "RollingRingConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7235": ["RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7236": ["ShaftCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7237": [
            "ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7238": [
            "ShaftToMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7239": [
            "SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7240": ["SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7241": [
            "SpiralBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7242": [
            "SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7243": ["SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7244": [
            "SpringDamperConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7245": ["SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7246": [
            "StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7247": [
            "StraightBevelDiffGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7248": [
            "StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7249": ["StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7250": [
            "StraightBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7251": [
            "StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7252": [
            "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7253": [
            "StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7254": ["SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7255": ["SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7256": ["SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7257": [
            "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7258": ["TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7259": [
            "TorqueConverterConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7260": [
            "TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7261": [
            "TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7262": ["UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7263": ["VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7264": ["WormGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7265": ["WormGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7266": ["WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7267": ["ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_7268": [
            "ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_7269": ["ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"],
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

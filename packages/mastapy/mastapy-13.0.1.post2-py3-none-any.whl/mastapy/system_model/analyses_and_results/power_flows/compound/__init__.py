"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4167 import AbstractAssemblyCompoundPowerFlow
    from ._4168 import AbstractShaftCompoundPowerFlow
    from ._4169 import AbstractShaftOrHousingCompoundPowerFlow
    from ._4170 import AbstractShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4171 import AGMAGleasonConicalGearCompoundPowerFlow
    from ._4172 import AGMAGleasonConicalGearMeshCompoundPowerFlow
    from ._4173 import AGMAGleasonConicalGearSetCompoundPowerFlow
    from ._4174 import AssemblyCompoundPowerFlow
    from ._4175 import BearingCompoundPowerFlow
    from ._4176 import BeltConnectionCompoundPowerFlow
    from ._4177 import BeltDriveCompoundPowerFlow
    from ._4178 import BevelDifferentialGearCompoundPowerFlow
    from ._4179 import BevelDifferentialGearMeshCompoundPowerFlow
    from ._4180 import BevelDifferentialGearSetCompoundPowerFlow
    from ._4181 import BevelDifferentialPlanetGearCompoundPowerFlow
    from ._4182 import BevelDifferentialSunGearCompoundPowerFlow
    from ._4183 import BevelGearCompoundPowerFlow
    from ._4184 import BevelGearMeshCompoundPowerFlow
    from ._4185 import BevelGearSetCompoundPowerFlow
    from ._4186 import BoltCompoundPowerFlow
    from ._4187 import BoltedJointCompoundPowerFlow
    from ._4188 import ClutchCompoundPowerFlow
    from ._4189 import ClutchConnectionCompoundPowerFlow
    from ._4190 import ClutchHalfCompoundPowerFlow
    from ._4191 import CoaxialConnectionCompoundPowerFlow
    from ._4192 import ComponentCompoundPowerFlow
    from ._4193 import ConceptCouplingCompoundPowerFlow
    from ._4194 import ConceptCouplingConnectionCompoundPowerFlow
    from ._4195 import ConceptCouplingHalfCompoundPowerFlow
    from ._4196 import ConceptGearCompoundPowerFlow
    from ._4197 import ConceptGearMeshCompoundPowerFlow
    from ._4198 import ConceptGearSetCompoundPowerFlow
    from ._4199 import ConicalGearCompoundPowerFlow
    from ._4200 import ConicalGearMeshCompoundPowerFlow
    from ._4201 import ConicalGearSetCompoundPowerFlow
    from ._4202 import ConnectionCompoundPowerFlow
    from ._4203 import ConnectorCompoundPowerFlow
    from ._4204 import CouplingCompoundPowerFlow
    from ._4205 import CouplingConnectionCompoundPowerFlow
    from ._4206 import CouplingHalfCompoundPowerFlow
    from ._4207 import CVTBeltConnectionCompoundPowerFlow
    from ._4208 import CVTCompoundPowerFlow
    from ._4209 import CVTPulleyCompoundPowerFlow
    from ._4210 import CycloidalAssemblyCompoundPowerFlow
    from ._4211 import CycloidalDiscCentralBearingConnectionCompoundPowerFlow
    from ._4212 import CycloidalDiscCompoundPowerFlow
    from ._4213 import CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
    from ._4214 import CylindricalGearCompoundPowerFlow
    from ._4215 import CylindricalGearMeshCompoundPowerFlow
    from ._4216 import CylindricalGearSetCompoundPowerFlow
    from ._4217 import CylindricalPlanetGearCompoundPowerFlow
    from ._4218 import DatumCompoundPowerFlow
    from ._4219 import ExternalCADModelCompoundPowerFlow
    from ._4220 import FaceGearCompoundPowerFlow
    from ._4221 import FaceGearMeshCompoundPowerFlow
    from ._4222 import FaceGearSetCompoundPowerFlow
    from ._4223 import FEPartCompoundPowerFlow
    from ._4224 import FlexiblePinAssemblyCompoundPowerFlow
    from ._4225 import GearCompoundPowerFlow
    from ._4226 import GearMeshCompoundPowerFlow
    from ._4227 import GearSetCompoundPowerFlow
    from ._4228 import GuideDxfModelCompoundPowerFlow
    from ._4229 import HypoidGearCompoundPowerFlow
    from ._4230 import HypoidGearMeshCompoundPowerFlow
    from ._4231 import HypoidGearSetCompoundPowerFlow
    from ._4232 import InterMountableComponentConnectionCompoundPowerFlow
    from ._4233 import KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
    from ._4234 import KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
    from ._4235 import KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
    from ._4236 import KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
    from ._4237 import KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
    from ._4238 import KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
    from ._4239 import KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
    from ._4240 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
    from ._4241 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
    from ._4242 import MassDiscCompoundPowerFlow
    from ._4243 import MeasurementComponentCompoundPowerFlow
    from ._4244 import MountableComponentCompoundPowerFlow
    from ._4245 import OilSealCompoundPowerFlow
    from ._4246 import PartCompoundPowerFlow
    from ._4247 import PartToPartShearCouplingCompoundPowerFlow
    from ._4248 import PartToPartShearCouplingConnectionCompoundPowerFlow
    from ._4249 import PartToPartShearCouplingHalfCompoundPowerFlow
    from ._4250 import PlanetaryConnectionCompoundPowerFlow
    from ._4251 import PlanetaryGearSetCompoundPowerFlow
    from ._4252 import PlanetCarrierCompoundPowerFlow
    from ._4253 import PointLoadCompoundPowerFlow
    from ._4254 import PowerLoadCompoundPowerFlow
    from ._4255 import PulleyCompoundPowerFlow
    from ._4256 import RingPinsCompoundPowerFlow
    from ._4257 import RingPinsToDiscConnectionCompoundPowerFlow
    from ._4258 import RollingRingAssemblyCompoundPowerFlow
    from ._4259 import RollingRingCompoundPowerFlow
    from ._4260 import RollingRingConnectionCompoundPowerFlow
    from ._4261 import RootAssemblyCompoundPowerFlow
    from ._4262 import ShaftCompoundPowerFlow
    from ._4263 import ShaftHubConnectionCompoundPowerFlow
    from ._4264 import ShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4265 import SpecialisedAssemblyCompoundPowerFlow
    from ._4266 import SpiralBevelGearCompoundPowerFlow
    from ._4267 import SpiralBevelGearMeshCompoundPowerFlow
    from ._4268 import SpiralBevelGearSetCompoundPowerFlow
    from ._4269 import SpringDamperCompoundPowerFlow
    from ._4270 import SpringDamperConnectionCompoundPowerFlow
    from ._4271 import SpringDamperHalfCompoundPowerFlow
    from ._4272 import StraightBevelDiffGearCompoundPowerFlow
    from ._4273 import StraightBevelDiffGearMeshCompoundPowerFlow
    from ._4274 import StraightBevelDiffGearSetCompoundPowerFlow
    from ._4275 import StraightBevelGearCompoundPowerFlow
    from ._4276 import StraightBevelGearMeshCompoundPowerFlow
    from ._4277 import StraightBevelGearSetCompoundPowerFlow
    from ._4278 import StraightBevelPlanetGearCompoundPowerFlow
    from ._4279 import StraightBevelSunGearCompoundPowerFlow
    from ._4280 import SynchroniserCompoundPowerFlow
    from ._4281 import SynchroniserHalfCompoundPowerFlow
    from ._4282 import SynchroniserPartCompoundPowerFlow
    from ._4283 import SynchroniserSleeveCompoundPowerFlow
    from ._4284 import TorqueConverterCompoundPowerFlow
    from ._4285 import TorqueConverterConnectionCompoundPowerFlow
    from ._4286 import TorqueConverterPumpCompoundPowerFlow
    from ._4287 import TorqueConverterTurbineCompoundPowerFlow
    from ._4288 import UnbalancedMassCompoundPowerFlow
    from ._4289 import VirtualComponentCompoundPowerFlow
    from ._4290 import WormGearCompoundPowerFlow
    from ._4291 import WormGearMeshCompoundPowerFlow
    from ._4292 import WormGearSetCompoundPowerFlow
    from ._4293 import ZerolBevelGearCompoundPowerFlow
    from ._4294 import ZerolBevelGearMeshCompoundPowerFlow
    from ._4295 import ZerolBevelGearSetCompoundPowerFlow
else:
    import_structure = {
        "_4167": ["AbstractAssemblyCompoundPowerFlow"],
        "_4168": ["AbstractShaftCompoundPowerFlow"],
        "_4169": ["AbstractShaftOrHousingCompoundPowerFlow"],
        "_4170": ["AbstractShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4171": ["AGMAGleasonConicalGearCompoundPowerFlow"],
        "_4172": ["AGMAGleasonConicalGearMeshCompoundPowerFlow"],
        "_4173": ["AGMAGleasonConicalGearSetCompoundPowerFlow"],
        "_4174": ["AssemblyCompoundPowerFlow"],
        "_4175": ["BearingCompoundPowerFlow"],
        "_4176": ["BeltConnectionCompoundPowerFlow"],
        "_4177": ["BeltDriveCompoundPowerFlow"],
        "_4178": ["BevelDifferentialGearCompoundPowerFlow"],
        "_4179": ["BevelDifferentialGearMeshCompoundPowerFlow"],
        "_4180": ["BevelDifferentialGearSetCompoundPowerFlow"],
        "_4181": ["BevelDifferentialPlanetGearCompoundPowerFlow"],
        "_4182": ["BevelDifferentialSunGearCompoundPowerFlow"],
        "_4183": ["BevelGearCompoundPowerFlow"],
        "_4184": ["BevelGearMeshCompoundPowerFlow"],
        "_4185": ["BevelGearSetCompoundPowerFlow"],
        "_4186": ["BoltCompoundPowerFlow"],
        "_4187": ["BoltedJointCompoundPowerFlow"],
        "_4188": ["ClutchCompoundPowerFlow"],
        "_4189": ["ClutchConnectionCompoundPowerFlow"],
        "_4190": ["ClutchHalfCompoundPowerFlow"],
        "_4191": ["CoaxialConnectionCompoundPowerFlow"],
        "_4192": ["ComponentCompoundPowerFlow"],
        "_4193": ["ConceptCouplingCompoundPowerFlow"],
        "_4194": ["ConceptCouplingConnectionCompoundPowerFlow"],
        "_4195": ["ConceptCouplingHalfCompoundPowerFlow"],
        "_4196": ["ConceptGearCompoundPowerFlow"],
        "_4197": ["ConceptGearMeshCompoundPowerFlow"],
        "_4198": ["ConceptGearSetCompoundPowerFlow"],
        "_4199": ["ConicalGearCompoundPowerFlow"],
        "_4200": ["ConicalGearMeshCompoundPowerFlow"],
        "_4201": ["ConicalGearSetCompoundPowerFlow"],
        "_4202": ["ConnectionCompoundPowerFlow"],
        "_4203": ["ConnectorCompoundPowerFlow"],
        "_4204": ["CouplingCompoundPowerFlow"],
        "_4205": ["CouplingConnectionCompoundPowerFlow"],
        "_4206": ["CouplingHalfCompoundPowerFlow"],
        "_4207": ["CVTBeltConnectionCompoundPowerFlow"],
        "_4208": ["CVTCompoundPowerFlow"],
        "_4209": ["CVTPulleyCompoundPowerFlow"],
        "_4210": ["CycloidalAssemblyCompoundPowerFlow"],
        "_4211": ["CycloidalDiscCentralBearingConnectionCompoundPowerFlow"],
        "_4212": ["CycloidalDiscCompoundPowerFlow"],
        "_4213": ["CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow"],
        "_4214": ["CylindricalGearCompoundPowerFlow"],
        "_4215": ["CylindricalGearMeshCompoundPowerFlow"],
        "_4216": ["CylindricalGearSetCompoundPowerFlow"],
        "_4217": ["CylindricalPlanetGearCompoundPowerFlow"],
        "_4218": ["DatumCompoundPowerFlow"],
        "_4219": ["ExternalCADModelCompoundPowerFlow"],
        "_4220": ["FaceGearCompoundPowerFlow"],
        "_4221": ["FaceGearMeshCompoundPowerFlow"],
        "_4222": ["FaceGearSetCompoundPowerFlow"],
        "_4223": ["FEPartCompoundPowerFlow"],
        "_4224": ["FlexiblePinAssemblyCompoundPowerFlow"],
        "_4225": ["GearCompoundPowerFlow"],
        "_4226": ["GearMeshCompoundPowerFlow"],
        "_4227": ["GearSetCompoundPowerFlow"],
        "_4228": ["GuideDxfModelCompoundPowerFlow"],
        "_4229": ["HypoidGearCompoundPowerFlow"],
        "_4230": ["HypoidGearMeshCompoundPowerFlow"],
        "_4231": ["HypoidGearSetCompoundPowerFlow"],
        "_4232": ["InterMountableComponentConnectionCompoundPowerFlow"],
        "_4233": ["KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"],
        "_4234": ["KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow"],
        "_4235": ["KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow"],
        "_4236": ["KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow"],
        "_4237": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow"],
        "_4238": ["KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow"],
        "_4239": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow"],
        "_4240": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow"],
        "_4241": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow"],
        "_4242": ["MassDiscCompoundPowerFlow"],
        "_4243": ["MeasurementComponentCompoundPowerFlow"],
        "_4244": ["MountableComponentCompoundPowerFlow"],
        "_4245": ["OilSealCompoundPowerFlow"],
        "_4246": ["PartCompoundPowerFlow"],
        "_4247": ["PartToPartShearCouplingCompoundPowerFlow"],
        "_4248": ["PartToPartShearCouplingConnectionCompoundPowerFlow"],
        "_4249": ["PartToPartShearCouplingHalfCompoundPowerFlow"],
        "_4250": ["PlanetaryConnectionCompoundPowerFlow"],
        "_4251": ["PlanetaryGearSetCompoundPowerFlow"],
        "_4252": ["PlanetCarrierCompoundPowerFlow"],
        "_4253": ["PointLoadCompoundPowerFlow"],
        "_4254": ["PowerLoadCompoundPowerFlow"],
        "_4255": ["PulleyCompoundPowerFlow"],
        "_4256": ["RingPinsCompoundPowerFlow"],
        "_4257": ["RingPinsToDiscConnectionCompoundPowerFlow"],
        "_4258": ["RollingRingAssemblyCompoundPowerFlow"],
        "_4259": ["RollingRingCompoundPowerFlow"],
        "_4260": ["RollingRingConnectionCompoundPowerFlow"],
        "_4261": ["RootAssemblyCompoundPowerFlow"],
        "_4262": ["ShaftCompoundPowerFlow"],
        "_4263": ["ShaftHubConnectionCompoundPowerFlow"],
        "_4264": ["ShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4265": ["SpecialisedAssemblyCompoundPowerFlow"],
        "_4266": ["SpiralBevelGearCompoundPowerFlow"],
        "_4267": ["SpiralBevelGearMeshCompoundPowerFlow"],
        "_4268": ["SpiralBevelGearSetCompoundPowerFlow"],
        "_4269": ["SpringDamperCompoundPowerFlow"],
        "_4270": ["SpringDamperConnectionCompoundPowerFlow"],
        "_4271": ["SpringDamperHalfCompoundPowerFlow"],
        "_4272": ["StraightBevelDiffGearCompoundPowerFlow"],
        "_4273": ["StraightBevelDiffGearMeshCompoundPowerFlow"],
        "_4274": ["StraightBevelDiffGearSetCompoundPowerFlow"],
        "_4275": ["StraightBevelGearCompoundPowerFlow"],
        "_4276": ["StraightBevelGearMeshCompoundPowerFlow"],
        "_4277": ["StraightBevelGearSetCompoundPowerFlow"],
        "_4278": ["StraightBevelPlanetGearCompoundPowerFlow"],
        "_4279": ["StraightBevelSunGearCompoundPowerFlow"],
        "_4280": ["SynchroniserCompoundPowerFlow"],
        "_4281": ["SynchroniserHalfCompoundPowerFlow"],
        "_4282": ["SynchroniserPartCompoundPowerFlow"],
        "_4283": ["SynchroniserSleeveCompoundPowerFlow"],
        "_4284": ["TorqueConverterCompoundPowerFlow"],
        "_4285": ["TorqueConverterConnectionCompoundPowerFlow"],
        "_4286": ["TorqueConverterPumpCompoundPowerFlow"],
        "_4287": ["TorqueConverterTurbineCompoundPowerFlow"],
        "_4288": ["UnbalancedMassCompoundPowerFlow"],
        "_4289": ["VirtualComponentCompoundPowerFlow"],
        "_4290": ["WormGearCompoundPowerFlow"],
        "_4291": ["WormGearMeshCompoundPowerFlow"],
        "_4292": ["WormGearSetCompoundPowerFlow"],
        "_4293": ["ZerolBevelGearCompoundPowerFlow"],
        "_4294": ["ZerolBevelGearMeshCompoundPowerFlow"],
        "_4295": ["ZerolBevelGearSetCompoundPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundPowerFlow",
    "AbstractShaftCompoundPowerFlow",
    "AbstractShaftOrHousingCompoundPowerFlow",
    "AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    "AGMAGleasonConicalGearCompoundPowerFlow",
    "AGMAGleasonConicalGearMeshCompoundPowerFlow",
    "AGMAGleasonConicalGearSetCompoundPowerFlow",
    "AssemblyCompoundPowerFlow",
    "BearingCompoundPowerFlow",
    "BeltConnectionCompoundPowerFlow",
    "BeltDriveCompoundPowerFlow",
    "BevelDifferentialGearCompoundPowerFlow",
    "BevelDifferentialGearMeshCompoundPowerFlow",
    "BevelDifferentialGearSetCompoundPowerFlow",
    "BevelDifferentialPlanetGearCompoundPowerFlow",
    "BevelDifferentialSunGearCompoundPowerFlow",
    "BevelGearCompoundPowerFlow",
    "BevelGearMeshCompoundPowerFlow",
    "BevelGearSetCompoundPowerFlow",
    "BoltCompoundPowerFlow",
    "BoltedJointCompoundPowerFlow",
    "ClutchCompoundPowerFlow",
    "ClutchConnectionCompoundPowerFlow",
    "ClutchHalfCompoundPowerFlow",
    "CoaxialConnectionCompoundPowerFlow",
    "ComponentCompoundPowerFlow",
    "ConceptCouplingCompoundPowerFlow",
    "ConceptCouplingConnectionCompoundPowerFlow",
    "ConceptCouplingHalfCompoundPowerFlow",
    "ConceptGearCompoundPowerFlow",
    "ConceptGearMeshCompoundPowerFlow",
    "ConceptGearSetCompoundPowerFlow",
    "ConicalGearCompoundPowerFlow",
    "ConicalGearMeshCompoundPowerFlow",
    "ConicalGearSetCompoundPowerFlow",
    "ConnectionCompoundPowerFlow",
    "ConnectorCompoundPowerFlow",
    "CouplingCompoundPowerFlow",
    "CouplingConnectionCompoundPowerFlow",
    "CouplingHalfCompoundPowerFlow",
    "CVTBeltConnectionCompoundPowerFlow",
    "CVTCompoundPowerFlow",
    "CVTPulleyCompoundPowerFlow",
    "CycloidalAssemblyCompoundPowerFlow",
    "CycloidalDiscCentralBearingConnectionCompoundPowerFlow",
    "CycloidalDiscCompoundPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow",
    "CylindricalGearCompoundPowerFlow",
    "CylindricalGearMeshCompoundPowerFlow",
    "CylindricalGearSetCompoundPowerFlow",
    "CylindricalPlanetGearCompoundPowerFlow",
    "DatumCompoundPowerFlow",
    "ExternalCADModelCompoundPowerFlow",
    "FaceGearCompoundPowerFlow",
    "FaceGearMeshCompoundPowerFlow",
    "FaceGearSetCompoundPowerFlow",
    "FEPartCompoundPowerFlow",
    "FlexiblePinAssemblyCompoundPowerFlow",
    "GearCompoundPowerFlow",
    "GearMeshCompoundPowerFlow",
    "GearSetCompoundPowerFlow",
    "GuideDxfModelCompoundPowerFlow",
    "HypoidGearCompoundPowerFlow",
    "HypoidGearMeshCompoundPowerFlow",
    "HypoidGearSetCompoundPowerFlow",
    "InterMountableComponentConnectionCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow",
    "MassDiscCompoundPowerFlow",
    "MeasurementComponentCompoundPowerFlow",
    "MountableComponentCompoundPowerFlow",
    "OilSealCompoundPowerFlow",
    "PartCompoundPowerFlow",
    "PartToPartShearCouplingCompoundPowerFlow",
    "PartToPartShearCouplingConnectionCompoundPowerFlow",
    "PartToPartShearCouplingHalfCompoundPowerFlow",
    "PlanetaryConnectionCompoundPowerFlow",
    "PlanetaryGearSetCompoundPowerFlow",
    "PlanetCarrierCompoundPowerFlow",
    "PointLoadCompoundPowerFlow",
    "PowerLoadCompoundPowerFlow",
    "PulleyCompoundPowerFlow",
    "RingPinsCompoundPowerFlow",
    "RingPinsToDiscConnectionCompoundPowerFlow",
    "RollingRingAssemblyCompoundPowerFlow",
    "RollingRingCompoundPowerFlow",
    "RollingRingConnectionCompoundPowerFlow",
    "RootAssemblyCompoundPowerFlow",
    "ShaftCompoundPowerFlow",
    "ShaftHubConnectionCompoundPowerFlow",
    "ShaftToMountableComponentConnectionCompoundPowerFlow",
    "SpecialisedAssemblyCompoundPowerFlow",
    "SpiralBevelGearCompoundPowerFlow",
    "SpiralBevelGearMeshCompoundPowerFlow",
    "SpiralBevelGearSetCompoundPowerFlow",
    "SpringDamperCompoundPowerFlow",
    "SpringDamperConnectionCompoundPowerFlow",
    "SpringDamperHalfCompoundPowerFlow",
    "StraightBevelDiffGearCompoundPowerFlow",
    "StraightBevelDiffGearMeshCompoundPowerFlow",
    "StraightBevelDiffGearSetCompoundPowerFlow",
    "StraightBevelGearCompoundPowerFlow",
    "StraightBevelGearMeshCompoundPowerFlow",
    "StraightBevelGearSetCompoundPowerFlow",
    "StraightBevelPlanetGearCompoundPowerFlow",
    "StraightBevelSunGearCompoundPowerFlow",
    "SynchroniserCompoundPowerFlow",
    "SynchroniserHalfCompoundPowerFlow",
    "SynchroniserPartCompoundPowerFlow",
    "SynchroniserSleeveCompoundPowerFlow",
    "TorqueConverterCompoundPowerFlow",
    "TorqueConverterConnectionCompoundPowerFlow",
    "TorqueConverterPumpCompoundPowerFlow",
    "TorqueConverterTurbineCompoundPowerFlow",
    "UnbalancedMassCompoundPowerFlow",
    "VirtualComponentCompoundPowerFlow",
    "WormGearCompoundPowerFlow",
    "WormGearMeshCompoundPowerFlow",
    "WormGearSetCompoundPowerFlow",
    "ZerolBevelGearCompoundPowerFlow",
    "ZerolBevelGearMeshCompoundPowerFlow",
    "ZerolBevelGearSetCompoundPowerFlow",
)

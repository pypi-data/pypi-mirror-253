"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4166 import AbstractAssemblyCompoundPowerFlow
    from ._4167 import AbstractShaftCompoundPowerFlow
    from ._4168 import AbstractShaftOrHousingCompoundPowerFlow
    from ._4169 import AbstractShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4170 import AGMAGleasonConicalGearCompoundPowerFlow
    from ._4171 import AGMAGleasonConicalGearMeshCompoundPowerFlow
    from ._4172 import AGMAGleasonConicalGearSetCompoundPowerFlow
    from ._4173 import AssemblyCompoundPowerFlow
    from ._4174 import BearingCompoundPowerFlow
    from ._4175 import BeltConnectionCompoundPowerFlow
    from ._4176 import BeltDriveCompoundPowerFlow
    from ._4177 import BevelDifferentialGearCompoundPowerFlow
    from ._4178 import BevelDifferentialGearMeshCompoundPowerFlow
    from ._4179 import BevelDifferentialGearSetCompoundPowerFlow
    from ._4180 import BevelDifferentialPlanetGearCompoundPowerFlow
    from ._4181 import BevelDifferentialSunGearCompoundPowerFlow
    from ._4182 import BevelGearCompoundPowerFlow
    from ._4183 import BevelGearMeshCompoundPowerFlow
    from ._4184 import BevelGearSetCompoundPowerFlow
    from ._4185 import BoltCompoundPowerFlow
    from ._4186 import BoltedJointCompoundPowerFlow
    from ._4187 import ClutchCompoundPowerFlow
    from ._4188 import ClutchConnectionCompoundPowerFlow
    from ._4189 import ClutchHalfCompoundPowerFlow
    from ._4190 import CoaxialConnectionCompoundPowerFlow
    from ._4191 import ComponentCompoundPowerFlow
    from ._4192 import ConceptCouplingCompoundPowerFlow
    from ._4193 import ConceptCouplingConnectionCompoundPowerFlow
    from ._4194 import ConceptCouplingHalfCompoundPowerFlow
    from ._4195 import ConceptGearCompoundPowerFlow
    from ._4196 import ConceptGearMeshCompoundPowerFlow
    from ._4197 import ConceptGearSetCompoundPowerFlow
    from ._4198 import ConicalGearCompoundPowerFlow
    from ._4199 import ConicalGearMeshCompoundPowerFlow
    from ._4200 import ConicalGearSetCompoundPowerFlow
    from ._4201 import ConnectionCompoundPowerFlow
    from ._4202 import ConnectorCompoundPowerFlow
    from ._4203 import CouplingCompoundPowerFlow
    from ._4204 import CouplingConnectionCompoundPowerFlow
    from ._4205 import CouplingHalfCompoundPowerFlow
    from ._4206 import CVTBeltConnectionCompoundPowerFlow
    from ._4207 import CVTCompoundPowerFlow
    from ._4208 import CVTPulleyCompoundPowerFlow
    from ._4209 import CycloidalAssemblyCompoundPowerFlow
    from ._4210 import CycloidalDiscCentralBearingConnectionCompoundPowerFlow
    from ._4211 import CycloidalDiscCompoundPowerFlow
    from ._4212 import CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
    from ._4213 import CylindricalGearCompoundPowerFlow
    from ._4214 import CylindricalGearMeshCompoundPowerFlow
    from ._4215 import CylindricalGearSetCompoundPowerFlow
    from ._4216 import CylindricalPlanetGearCompoundPowerFlow
    from ._4217 import DatumCompoundPowerFlow
    from ._4218 import ExternalCADModelCompoundPowerFlow
    from ._4219 import FaceGearCompoundPowerFlow
    from ._4220 import FaceGearMeshCompoundPowerFlow
    from ._4221 import FaceGearSetCompoundPowerFlow
    from ._4222 import FEPartCompoundPowerFlow
    from ._4223 import FlexiblePinAssemblyCompoundPowerFlow
    from ._4224 import GearCompoundPowerFlow
    from ._4225 import GearMeshCompoundPowerFlow
    from ._4226 import GearSetCompoundPowerFlow
    from ._4227 import GuideDxfModelCompoundPowerFlow
    from ._4228 import HypoidGearCompoundPowerFlow
    from ._4229 import HypoidGearMeshCompoundPowerFlow
    from ._4230 import HypoidGearSetCompoundPowerFlow
    from ._4231 import InterMountableComponentConnectionCompoundPowerFlow
    from ._4232 import KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
    from ._4233 import KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow
    from ._4234 import KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
    from ._4235 import KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
    from ._4236 import KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow
    from ._4237 import KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
    from ._4238 import KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
    from ._4239 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow
    from ._4240 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
    from ._4241 import MassDiscCompoundPowerFlow
    from ._4242 import MeasurementComponentCompoundPowerFlow
    from ._4243 import MountableComponentCompoundPowerFlow
    from ._4244 import OilSealCompoundPowerFlow
    from ._4245 import PartCompoundPowerFlow
    from ._4246 import PartToPartShearCouplingCompoundPowerFlow
    from ._4247 import PartToPartShearCouplingConnectionCompoundPowerFlow
    from ._4248 import PartToPartShearCouplingHalfCompoundPowerFlow
    from ._4249 import PlanetaryConnectionCompoundPowerFlow
    from ._4250 import PlanetaryGearSetCompoundPowerFlow
    from ._4251 import PlanetCarrierCompoundPowerFlow
    from ._4252 import PointLoadCompoundPowerFlow
    from ._4253 import PowerLoadCompoundPowerFlow
    from ._4254 import PulleyCompoundPowerFlow
    from ._4255 import RingPinsCompoundPowerFlow
    from ._4256 import RingPinsToDiscConnectionCompoundPowerFlow
    from ._4257 import RollingRingAssemblyCompoundPowerFlow
    from ._4258 import RollingRingCompoundPowerFlow
    from ._4259 import RollingRingConnectionCompoundPowerFlow
    from ._4260 import RootAssemblyCompoundPowerFlow
    from ._4261 import ShaftCompoundPowerFlow
    from ._4262 import ShaftHubConnectionCompoundPowerFlow
    from ._4263 import ShaftToMountableComponentConnectionCompoundPowerFlow
    from ._4264 import SpecialisedAssemblyCompoundPowerFlow
    from ._4265 import SpiralBevelGearCompoundPowerFlow
    from ._4266 import SpiralBevelGearMeshCompoundPowerFlow
    from ._4267 import SpiralBevelGearSetCompoundPowerFlow
    from ._4268 import SpringDamperCompoundPowerFlow
    from ._4269 import SpringDamperConnectionCompoundPowerFlow
    from ._4270 import SpringDamperHalfCompoundPowerFlow
    from ._4271 import StraightBevelDiffGearCompoundPowerFlow
    from ._4272 import StraightBevelDiffGearMeshCompoundPowerFlow
    from ._4273 import StraightBevelDiffGearSetCompoundPowerFlow
    from ._4274 import StraightBevelGearCompoundPowerFlow
    from ._4275 import StraightBevelGearMeshCompoundPowerFlow
    from ._4276 import StraightBevelGearSetCompoundPowerFlow
    from ._4277 import StraightBevelPlanetGearCompoundPowerFlow
    from ._4278 import StraightBevelSunGearCompoundPowerFlow
    from ._4279 import SynchroniserCompoundPowerFlow
    from ._4280 import SynchroniserHalfCompoundPowerFlow
    from ._4281 import SynchroniserPartCompoundPowerFlow
    from ._4282 import SynchroniserSleeveCompoundPowerFlow
    from ._4283 import TorqueConverterCompoundPowerFlow
    from ._4284 import TorqueConverterConnectionCompoundPowerFlow
    from ._4285 import TorqueConverterPumpCompoundPowerFlow
    from ._4286 import TorqueConverterTurbineCompoundPowerFlow
    from ._4287 import UnbalancedMassCompoundPowerFlow
    from ._4288 import VirtualComponentCompoundPowerFlow
    from ._4289 import WormGearCompoundPowerFlow
    from ._4290 import WormGearMeshCompoundPowerFlow
    from ._4291 import WormGearSetCompoundPowerFlow
    from ._4292 import ZerolBevelGearCompoundPowerFlow
    from ._4293 import ZerolBevelGearMeshCompoundPowerFlow
    from ._4294 import ZerolBevelGearSetCompoundPowerFlow
else:
    import_structure = {
        "_4166": ["AbstractAssemblyCompoundPowerFlow"],
        "_4167": ["AbstractShaftCompoundPowerFlow"],
        "_4168": ["AbstractShaftOrHousingCompoundPowerFlow"],
        "_4169": ["AbstractShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4170": ["AGMAGleasonConicalGearCompoundPowerFlow"],
        "_4171": ["AGMAGleasonConicalGearMeshCompoundPowerFlow"],
        "_4172": ["AGMAGleasonConicalGearSetCompoundPowerFlow"],
        "_4173": ["AssemblyCompoundPowerFlow"],
        "_4174": ["BearingCompoundPowerFlow"],
        "_4175": ["BeltConnectionCompoundPowerFlow"],
        "_4176": ["BeltDriveCompoundPowerFlow"],
        "_4177": ["BevelDifferentialGearCompoundPowerFlow"],
        "_4178": ["BevelDifferentialGearMeshCompoundPowerFlow"],
        "_4179": ["BevelDifferentialGearSetCompoundPowerFlow"],
        "_4180": ["BevelDifferentialPlanetGearCompoundPowerFlow"],
        "_4181": ["BevelDifferentialSunGearCompoundPowerFlow"],
        "_4182": ["BevelGearCompoundPowerFlow"],
        "_4183": ["BevelGearMeshCompoundPowerFlow"],
        "_4184": ["BevelGearSetCompoundPowerFlow"],
        "_4185": ["BoltCompoundPowerFlow"],
        "_4186": ["BoltedJointCompoundPowerFlow"],
        "_4187": ["ClutchCompoundPowerFlow"],
        "_4188": ["ClutchConnectionCompoundPowerFlow"],
        "_4189": ["ClutchHalfCompoundPowerFlow"],
        "_4190": ["CoaxialConnectionCompoundPowerFlow"],
        "_4191": ["ComponentCompoundPowerFlow"],
        "_4192": ["ConceptCouplingCompoundPowerFlow"],
        "_4193": ["ConceptCouplingConnectionCompoundPowerFlow"],
        "_4194": ["ConceptCouplingHalfCompoundPowerFlow"],
        "_4195": ["ConceptGearCompoundPowerFlow"],
        "_4196": ["ConceptGearMeshCompoundPowerFlow"],
        "_4197": ["ConceptGearSetCompoundPowerFlow"],
        "_4198": ["ConicalGearCompoundPowerFlow"],
        "_4199": ["ConicalGearMeshCompoundPowerFlow"],
        "_4200": ["ConicalGearSetCompoundPowerFlow"],
        "_4201": ["ConnectionCompoundPowerFlow"],
        "_4202": ["ConnectorCompoundPowerFlow"],
        "_4203": ["CouplingCompoundPowerFlow"],
        "_4204": ["CouplingConnectionCompoundPowerFlow"],
        "_4205": ["CouplingHalfCompoundPowerFlow"],
        "_4206": ["CVTBeltConnectionCompoundPowerFlow"],
        "_4207": ["CVTCompoundPowerFlow"],
        "_4208": ["CVTPulleyCompoundPowerFlow"],
        "_4209": ["CycloidalAssemblyCompoundPowerFlow"],
        "_4210": ["CycloidalDiscCentralBearingConnectionCompoundPowerFlow"],
        "_4211": ["CycloidalDiscCompoundPowerFlow"],
        "_4212": ["CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow"],
        "_4213": ["CylindricalGearCompoundPowerFlow"],
        "_4214": ["CylindricalGearMeshCompoundPowerFlow"],
        "_4215": ["CylindricalGearSetCompoundPowerFlow"],
        "_4216": ["CylindricalPlanetGearCompoundPowerFlow"],
        "_4217": ["DatumCompoundPowerFlow"],
        "_4218": ["ExternalCADModelCompoundPowerFlow"],
        "_4219": ["FaceGearCompoundPowerFlow"],
        "_4220": ["FaceGearMeshCompoundPowerFlow"],
        "_4221": ["FaceGearSetCompoundPowerFlow"],
        "_4222": ["FEPartCompoundPowerFlow"],
        "_4223": ["FlexiblePinAssemblyCompoundPowerFlow"],
        "_4224": ["GearCompoundPowerFlow"],
        "_4225": ["GearMeshCompoundPowerFlow"],
        "_4226": ["GearSetCompoundPowerFlow"],
        "_4227": ["GuideDxfModelCompoundPowerFlow"],
        "_4228": ["HypoidGearCompoundPowerFlow"],
        "_4229": ["HypoidGearMeshCompoundPowerFlow"],
        "_4230": ["HypoidGearSetCompoundPowerFlow"],
        "_4231": ["InterMountableComponentConnectionCompoundPowerFlow"],
        "_4232": ["KlingelnbergCycloPalloidConicalGearCompoundPowerFlow"],
        "_4233": ["KlingelnbergCycloPalloidConicalGearMeshCompoundPowerFlow"],
        "_4234": ["KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow"],
        "_4235": ["KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow"],
        "_4236": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow"],
        "_4237": ["KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow"],
        "_4238": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow"],
        "_4239": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundPowerFlow"],
        "_4240": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow"],
        "_4241": ["MassDiscCompoundPowerFlow"],
        "_4242": ["MeasurementComponentCompoundPowerFlow"],
        "_4243": ["MountableComponentCompoundPowerFlow"],
        "_4244": ["OilSealCompoundPowerFlow"],
        "_4245": ["PartCompoundPowerFlow"],
        "_4246": ["PartToPartShearCouplingCompoundPowerFlow"],
        "_4247": ["PartToPartShearCouplingConnectionCompoundPowerFlow"],
        "_4248": ["PartToPartShearCouplingHalfCompoundPowerFlow"],
        "_4249": ["PlanetaryConnectionCompoundPowerFlow"],
        "_4250": ["PlanetaryGearSetCompoundPowerFlow"],
        "_4251": ["PlanetCarrierCompoundPowerFlow"],
        "_4252": ["PointLoadCompoundPowerFlow"],
        "_4253": ["PowerLoadCompoundPowerFlow"],
        "_4254": ["PulleyCompoundPowerFlow"],
        "_4255": ["RingPinsCompoundPowerFlow"],
        "_4256": ["RingPinsToDiscConnectionCompoundPowerFlow"],
        "_4257": ["RollingRingAssemblyCompoundPowerFlow"],
        "_4258": ["RollingRingCompoundPowerFlow"],
        "_4259": ["RollingRingConnectionCompoundPowerFlow"],
        "_4260": ["RootAssemblyCompoundPowerFlow"],
        "_4261": ["ShaftCompoundPowerFlow"],
        "_4262": ["ShaftHubConnectionCompoundPowerFlow"],
        "_4263": ["ShaftToMountableComponentConnectionCompoundPowerFlow"],
        "_4264": ["SpecialisedAssemblyCompoundPowerFlow"],
        "_4265": ["SpiralBevelGearCompoundPowerFlow"],
        "_4266": ["SpiralBevelGearMeshCompoundPowerFlow"],
        "_4267": ["SpiralBevelGearSetCompoundPowerFlow"],
        "_4268": ["SpringDamperCompoundPowerFlow"],
        "_4269": ["SpringDamperConnectionCompoundPowerFlow"],
        "_4270": ["SpringDamperHalfCompoundPowerFlow"],
        "_4271": ["StraightBevelDiffGearCompoundPowerFlow"],
        "_4272": ["StraightBevelDiffGearMeshCompoundPowerFlow"],
        "_4273": ["StraightBevelDiffGearSetCompoundPowerFlow"],
        "_4274": ["StraightBevelGearCompoundPowerFlow"],
        "_4275": ["StraightBevelGearMeshCompoundPowerFlow"],
        "_4276": ["StraightBevelGearSetCompoundPowerFlow"],
        "_4277": ["StraightBevelPlanetGearCompoundPowerFlow"],
        "_4278": ["StraightBevelSunGearCompoundPowerFlow"],
        "_4279": ["SynchroniserCompoundPowerFlow"],
        "_4280": ["SynchroniserHalfCompoundPowerFlow"],
        "_4281": ["SynchroniserPartCompoundPowerFlow"],
        "_4282": ["SynchroniserSleeveCompoundPowerFlow"],
        "_4283": ["TorqueConverterCompoundPowerFlow"],
        "_4284": ["TorqueConverterConnectionCompoundPowerFlow"],
        "_4285": ["TorqueConverterPumpCompoundPowerFlow"],
        "_4286": ["TorqueConverterTurbineCompoundPowerFlow"],
        "_4287": ["UnbalancedMassCompoundPowerFlow"],
        "_4288": ["VirtualComponentCompoundPowerFlow"],
        "_4289": ["WormGearCompoundPowerFlow"],
        "_4290": ["WormGearMeshCompoundPowerFlow"],
        "_4291": ["WormGearSetCompoundPowerFlow"],
        "_4292": ["ZerolBevelGearCompoundPowerFlow"],
        "_4293": ["ZerolBevelGearMeshCompoundPowerFlow"],
        "_4294": ["ZerolBevelGearSetCompoundPowerFlow"],
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

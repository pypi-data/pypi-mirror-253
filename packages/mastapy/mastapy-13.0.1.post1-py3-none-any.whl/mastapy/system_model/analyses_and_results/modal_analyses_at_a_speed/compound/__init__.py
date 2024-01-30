"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5247 import AbstractAssemblyCompoundModalAnalysisAtASpeed
    from ._5248 import AbstractShaftCompoundModalAnalysisAtASpeed
    from ._5249 import AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
    from ._5250 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5251 import AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
    from ._5252 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5253 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5254 import AssemblyCompoundModalAnalysisAtASpeed
    from ._5255 import BearingCompoundModalAnalysisAtASpeed
    from ._5256 import BeltConnectionCompoundModalAnalysisAtASpeed
    from ._5257 import BeltDriveCompoundModalAnalysisAtASpeed
    from ._5258 import BevelDifferentialGearCompoundModalAnalysisAtASpeed
    from ._5259 import BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
    from ._5260 import BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
    from ._5261 import BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
    from ._5262 import BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
    from ._5263 import BevelGearCompoundModalAnalysisAtASpeed
    from ._5264 import BevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5265 import BevelGearSetCompoundModalAnalysisAtASpeed
    from ._5266 import BoltCompoundModalAnalysisAtASpeed
    from ._5267 import BoltedJointCompoundModalAnalysisAtASpeed
    from ._5268 import ClutchCompoundModalAnalysisAtASpeed
    from ._5269 import ClutchConnectionCompoundModalAnalysisAtASpeed
    from ._5270 import ClutchHalfCompoundModalAnalysisAtASpeed
    from ._5271 import CoaxialConnectionCompoundModalAnalysisAtASpeed
    from ._5272 import ComponentCompoundModalAnalysisAtASpeed
    from ._5273 import ConceptCouplingCompoundModalAnalysisAtASpeed
    from ._5274 import ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5275 import ConceptCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5276 import ConceptGearCompoundModalAnalysisAtASpeed
    from ._5277 import ConceptGearMeshCompoundModalAnalysisAtASpeed
    from ._5278 import ConceptGearSetCompoundModalAnalysisAtASpeed
    from ._5279 import ConicalGearCompoundModalAnalysisAtASpeed
    from ._5280 import ConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5281 import ConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5282 import ConnectionCompoundModalAnalysisAtASpeed
    from ._5283 import ConnectorCompoundModalAnalysisAtASpeed
    from ._5284 import CouplingCompoundModalAnalysisAtASpeed
    from ._5285 import CouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5286 import CouplingHalfCompoundModalAnalysisAtASpeed
    from ._5287 import CVTBeltConnectionCompoundModalAnalysisAtASpeed
    from ._5288 import CVTCompoundModalAnalysisAtASpeed
    from ._5289 import CVTPulleyCompoundModalAnalysisAtASpeed
    from ._5290 import CycloidalAssemblyCompoundModalAnalysisAtASpeed
    from ._5291 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5292 import CycloidalDiscCompoundModalAnalysisAtASpeed
    from ._5293 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5294 import CylindricalGearCompoundModalAnalysisAtASpeed
    from ._5295 import CylindricalGearMeshCompoundModalAnalysisAtASpeed
    from ._5296 import CylindricalGearSetCompoundModalAnalysisAtASpeed
    from ._5297 import CylindricalPlanetGearCompoundModalAnalysisAtASpeed
    from ._5298 import DatumCompoundModalAnalysisAtASpeed
    from ._5299 import ExternalCADModelCompoundModalAnalysisAtASpeed
    from ._5300 import FaceGearCompoundModalAnalysisAtASpeed
    from ._5301 import FaceGearMeshCompoundModalAnalysisAtASpeed
    from ._5302 import FaceGearSetCompoundModalAnalysisAtASpeed
    from ._5303 import FEPartCompoundModalAnalysisAtASpeed
    from ._5304 import FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
    from ._5305 import GearCompoundModalAnalysisAtASpeed
    from ._5306 import GearMeshCompoundModalAnalysisAtASpeed
    from ._5307 import GearSetCompoundModalAnalysisAtASpeed
    from ._5308 import GuideDxfModelCompoundModalAnalysisAtASpeed
    from ._5309 import HypoidGearCompoundModalAnalysisAtASpeed
    from ._5310 import HypoidGearMeshCompoundModalAnalysisAtASpeed
    from ._5311 import HypoidGearSetCompoundModalAnalysisAtASpeed
    from ._5312 import InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5313 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
    from ._5314 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5315 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5316 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
    from ._5317 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5318 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5319 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed,
    )
    from ._5320 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5321 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5322 import MassDiscCompoundModalAnalysisAtASpeed
    from ._5323 import MeasurementComponentCompoundModalAnalysisAtASpeed
    from ._5324 import MountableComponentCompoundModalAnalysisAtASpeed
    from ._5325 import OilSealCompoundModalAnalysisAtASpeed
    from ._5326 import PartCompoundModalAnalysisAtASpeed
    from ._5327 import PartToPartShearCouplingCompoundModalAnalysisAtASpeed
    from ._5328 import PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5329 import PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5330 import PlanetaryConnectionCompoundModalAnalysisAtASpeed
    from ._5331 import PlanetaryGearSetCompoundModalAnalysisAtASpeed
    from ._5332 import PlanetCarrierCompoundModalAnalysisAtASpeed
    from ._5333 import PointLoadCompoundModalAnalysisAtASpeed
    from ._5334 import PowerLoadCompoundModalAnalysisAtASpeed
    from ._5335 import PulleyCompoundModalAnalysisAtASpeed
    from ._5336 import RingPinsCompoundModalAnalysisAtASpeed
    from ._5337 import RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
    from ._5338 import RollingRingAssemblyCompoundModalAnalysisAtASpeed
    from ._5339 import RollingRingCompoundModalAnalysisAtASpeed
    from ._5340 import RollingRingConnectionCompoundModalAnalysisAtASpeed
    from ._5341 import RootAssemblyCompoundModalAnalysisAtASpeed
    from ._5342 import ShaftCompoundModalAnalysisAtASpeed
    from ._5343 import ShaftHubConnectionCompoundModalAnalysisAtASpeed
    from ._5344 import ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5345 import SpecialisedAssemblyCompoundModalAnalysisAtASpeed
    from ._5346 import SpiralBevelGearCompoundModalAnalysisAtASpeed
    from ._5347 import SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5348 import SpiralBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5349 import SpringDamperCompoundModalAnalysisAtASpeed
    from ._5350 import SpringDamperConnectionCompoundModalAnalysisAtASpeed
    from ._5351 import SpringDamperHalfCompoundModalAnalysisAtASpeed
    from ._5352 import StraightBevelDiffGearCompoundModalAnalysisAtASpeed
    from ._5353 import StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
    from ._5354 import StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
    from ._5355 import StraightBevelGearCompoundModalAnalysisAtASpeed
    from ._5356 import StraightBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5357 import StraightBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5358 import StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
    from ._5359 import StraightBevelSunGearCompoundModalAnalysisAtASpeed
    from ._5360 import SynchroniserCompoundModalAnalysisAtASpeed
    from ._5361 import SynchroniserHalfCompoundModalAnalysisAtASpeed
    from ._5362 import SynchroniserPartCompoundModalAnalysisAtASpeed
    from ._5363 import SynchroniserSleeveCompoundModalAnalysisAtASpeed
    from ._5364 import TorqueConverterCompoundModalAnalysisAtASpeed
    from ._5365 import TorqueConverterConnectionCompoundModalAnalysisAtASpeed
    from ._5366 import TorqueConverterPumpCompoundModalAnalysisAtASpeed
    from ._5367 import TorqueConverterTurbineCompoundModalAnalysisAtASpeed
    from ._5368 import UnbalancedMassCompoundModalAnalysisAtASpeed
    from ._5369 import VirtualComponentCompoundModalAnalysisAtASpeed
    from ._5370 import WormGearCompoundModalAnalysisAtASpeed
    from ._5371 import WormGearMeshCompoundModalAnalysisAtASpeed
    from ._5372 import WormGearSetCompoundModalAnalysisAtASpeed
    from ._5373 import ZerolBevelGearCompoundModalAnalysisAtASpeed
    from ._5374 import ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5375 import ZerolBevelGearSetCompoundModalAnalysisAtASpeed
else:
    import_structure = {
        "_5247": ["AbstractAssemblyCompoundModalAnalysisAtASpeed"],
        "_5248": ["AbstractShaftCompoundModalAnalysisAtASpeed"],
        "_5249": ["AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"],
        "_5250": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5251": ["AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"],
        "_5252": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5253": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5254": ["AssemblyCompoundModalAnalysisAtASpeed"],
        "_5255": ["BearingCompoundModalAnalysisAtASpeed"],
        "_5256": ["BeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5257": ["BeltDriveCompoundModalAnalysisAtASpeed"],
        "_5258": ["BevelDifferentialGearCompoundModalAnalysisAtASpeed"],
        "_5259": ["BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed"],
        "_5260": ["BevelDifferentialGearSetCompoundModalAnalysisAtASpeed"],
        "_5261": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5262": ["BevelDifferentialSunGearCompoundModalAnalysisAtASpeed"],
        "_5263": ["BevelGearCompoundModalAnalysisAtASpeed"],
        "_5264": ["BevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5265": ["BevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5266": ["BoltCompoundModalAnalysisAtASpeed"],
        "_5267": ["BoltedJointCompoundModalAnalysisAtASpeed"],
        "_5268": ["ClutchCompoundModalAnalysisAtASpeed"],
        "_5269": ["ClutchConnectionCompoundModalAnalysisAtASpeed"],
        "_5270": ["ClutchHalfCompoundModalAnalysisAtASpeed"],
        "_5271": ["CoaxialConnectionCompoundModalAnalysisAtASpeed"],
        "_5272": ["ComponentCompoundModalAnalysisAtASpeed"],
        "_5273": ["ConceptCouplingCompoundModalAnalysisAtASpeed"],
        "_5274": ["ConceptCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5275": ["ConceptCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5276": ["ConceptGearCompoundModalAnalysisAtASpeed"],
        "_5277": ["ConceptGearMeshCompoundModalAnalysisAtASpeed"],
        "_5278": ["ConceptGearSetCompoundModalAnalysisAtASpeed"],
        "_5279": ["ConicalGearCompoundModalAnalysisAtASpeed"],
        "_5280": ["ConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5281": ["ConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5282": ["ConnectionCompoundModalAnalysisAtASpeed"],
        "_5283": ["ConnectorCompoundModalAnalysisAtASpeed"],
        "_5284": ["CouplingCompoundModalAnalysisAtASpeed"],
        "_5285": ["CouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5286": ["CouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5287": ["CVTBeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5288": ["CVTCompoundModalAnalysisAtASpeed"],
        "_5289": ["CVTPulleyCompoundModalAnalysisAtASpeed"],
        "_5290": ["CycloidalAssemblyCompoundModalAnalysisAtASpeed"],
        "_5291": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed"],
        "_5292": ["CycloidalDiscCompoundModalAnalysisAtASpeed"],
        "_5293": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5294": ["CylindricalGearCompoundModalAnalysisAtASpeed"],
        "_5295": ["CylindricalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5296": ["CylindricalGearSetCompoundModalAnalysisAtASpeed"],
        "_5297": ["CylindricalPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5298": ["DatumCompoundModalAnalysisAtASpeed"],
        "_5299": ["ExternalCADModelCompoundModalAnalysisAtASpeed"],
        "_5300": ["FaceGearCompoundModalAnalysisAtASpeed"],
        "_5301": ["FaceGearMeshCompoundModalAnalysisAtASpeed"],
        "_5302": ["FaceGearSetCompoundModalAnalysisAtASpeed"],
        "_5303": ["FEPartCompoundModalAnalysisAtASpeed"],
        "_5304": ["FlexiblePinAssemblyCompoundModalAnalysisAtASpeed"],
        "_5305": ["GearCompoundModalAnalysisAtASpeed"],
        "_5306": ["GearMeshCompoundModalAnalysisAtASpeed"],
        "_5307": ["GearSetCompoundModalAnalysisAtASpeed"],
        "_5308": ["GuideDxfModelCompoundModalAnalysisAtASpeed"],
        "_5309": ["HypoidGearCompoundModalAnalysisAtASpeed"],
        "_5310": ["HypoidGearMeshCompoundModalAnalysisAtASpeed"],
        "_5311": ["HypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5312": ["InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5313": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed"],
        "_5314": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5315": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5316": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed"],
        "_5317": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5318": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5319": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ],
        "_5320": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5321": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5322": ["MassDiscCompoundModalAnalysisAtASpeed"],
        "_5323": ["MeasurementComponentCompoundModalAnalysisAtASpeed"],
        "_5324": ["MountableComponentCompoundModalAnalysisAtASpeed"],
        "_5325": ["OilSealCompoundModalAnalysisAtASpeed"],
        "_5326": ["PartCompoundModalAnalysisAtASpeed"],
        "_5327": ["PartToPartShearCouplingCompoundModalAnalysisAtASpeed"],
        "_5328": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5329": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5330": ["PlanetaryConnectionCompoundModalAnalysisAtASpeed"],
        "_5331": ["PlanetaryGearSetCompoundModalAnalysisAtASpeed"],
        "_5332": ["PlanetCarrierCompoundModalAnalysisAtASpeed"],
        "_5333": ["PointLoadCompoundModalAnalysisAtASpeed"],
        "_5334": ["PowerLoadCompoundModalAnalysisAtASpeed"],
        "_5335": ["PulleyCompoundModalAnalysisAtASpeed"],
        "_5336": ["RingPinsCompoundModalAnalysisAtASpeed"],
        "_5337": ["RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed"],
        "_5338": ["RollingRingAssemblyCompoundModalAnalysisAtASpeed"],
        "_5339": ["RollingRingCompoundModalAnalysisAtASpeed"],
        "_5340": ["RollingRingConnectionCompoundModalAnalysisAtASpeed"],
        "_5341": ["RootAssemblyCompoundModalAnalysisAtASpeed"],
        "_5342": ["ShaftCompoundModalAnalysisAtASpeed"],
        "_5343": ["ShaftHubConnectionCompoundModalAnalysisAtASpeed"],
        "_5344": ["ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5345": ["SpecialisedAssemblyCompoundModalAnalysisAtASpeed"],
        "_5346": ["SpiralBevelGearCompoundModalAnalysisAtASpeed"],
        "_5347": ["SpiralBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5348": ["SpiralBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5349": ["SpringDamperCompoundModalAnalysisAtASpeed"],
        "_5350": ["SpringDamperConnectionCompoundModalAnalysisAtASpeed"],
        "_5351": ["SpringDamperHalfCompoundModalAnalysisAtASpeed"],
        "_5352": ["StraightBevelDiffGearCompoundModalAnalysisAtASpeed"],
        "_5353": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed"],
        "_5354": ["StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed"],
        "_5355": ["StraightBevelGearCompoundModalAnalysisAtASpeed"],
        "_5356": ["StraightBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5357": ["StraightBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5358": ["StraightBevelPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5359": ["StraightBevelSunGearCompoundModalAnalysisAtASpeed"],
        "_5360": ["SynchroniserCompoundModalAnalysisAtASpeed"],
        "_5361": ["SynchroniserHalfCompoundModalAnalysisAtASpeed"],
        "_5362": ["SynchroniserPartCompoundModalAnalysisAtASpeed"],
        "_5363": ["SynchroniserSleeveCompoundModalAnalysisAtASpeed"],
        "_5364": ["TorqueConverterCompoundModalAnalysisAtASpeed"],
        "_5365": ["TorqueConverterConnectionCompoundModalAnalysisAtASpeed"],
        "_5366": ["TorqueConverterPumpCompoundModalAnalysisAtASpeed"],
        "_5367": ["TorqueConverterTurbineCompoundModalAnalysisAtASpeed"],
        "_5368": ["UnbalancedMassCompoundModalAnalysisAtASpeed"],
        "_5369": ["VirtualComponentCompoundModalAnalysisAtASpeed"],
        "_5370": ["WormGearCompoundModalAnalysisAtASpeed"],
        "_5371": ["WormGearMeshCompoundModalAnalysisAtASpeed"],
        "_5372": ["WormGearSetCompoundModalAnalysisAtASpeed"],
        "_5373": ["ZerolBevelGearCompoundModalAnalysisAtASpeed"],
        "_5374": ["ZerolBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5375": ["ZerolBevelGearSetCompoundModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysisAtASpeed",
    "AbstractShaftCompoundModalAnalysisAtASpeed",
    "AbstractShaftOrHousingCompoundModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
    "AssemblyCompoundModalAnalysisAtASpeed",
    "BearingCompoundModalAnalysisAtASpeed",
    "BeltConnectionCompoundModalAnalysisAtASpeed",
    "BeltDriveCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed",
    "BevelDifferentialGearSetCompoundModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed",
    "BevelDifferentialSunGearCompoundModalAnalysisAtASpeed",
    "BevelGearCompoundModalAnalysisAtASpeed",
    "BevelGearMeshCompoundModalAnalysisAtASpeed",
    "BevelGearSetCompoundModalAnalysisAtASpeed",
    "BoltCompoundModalAnalysisAtASpeed",
    "BoltedJointCompoundModalAnalysisAtASpeed",
    "ClutchCompoundModalAnalysisAtASpeed",
    "ClutchConnectionCompoundModalAnalysisAtASpeed",
    "ClutchHalfCompoundModalAnalysisAtASpeed",
    "CoaxialConnectionCompoundModalAnalysisAtASpeed",
    "ComponentCompoundModalAnalysisAtASpeed",
    "ConceptCouplingCompoundModalAnalysisAtASpeed",
    "ConceptCouplingConnectionCompoundModalAnalysisAtASpeed",
    "ConceptCouplingHalfCompoundModalAnalysisAtASpeed",
    "ConceptGearCompoundModalAnalysisAtASpeed",
    "ConceptGearMeshCompoundModalAnalysisAtASpeed",
    "ConceptGearSetCompoundModalAnalysisAtASpeed",
    "ConicalGearCompoundModalAnalysisAtASpeed",
    "ConicalGearMeshCompoundModalAnalysisAtASpeed",
    "ConicalGearSetCompoundModalAnalysisAtASpeed",
    "ConnectionCompoundModalAnalysisAtASpeed",
    "ConnectorCompoundModalAnalysisAtASpeed",
    "CouplingCompoundModalAnalysisAtASpeed",
    "CouplingConnectionCompoundModalAnalysisAtASpeed",
    "CouplingHalfCompoundModalAnalysisAtASpeed",
    "CVTBeltConnectionCompoundModalAnalysisAtASpeed",
    "CVTCompoundModalAnalysisAtASpeed",
    "CVTPulleyCompoundModalAnalysisAtASpeed",
    "CycloidalAssemblyCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed",
    "CycloidalDiscCompoundModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed",
    "CylindricalGearCompoundModalAnalysisAtASpeed",
    "CylindricalGearMeshCompoundModalAnalysisAtASpeed",
    "CylindricalGearSetCompoundModalAnalysisAtASpeed",
    "CylindricalPlanetGearCompoundModalAnalysisAtASpeed",
    "DatumCompoundModalAnalysisAtASpeed",
    "ExternalCADModelCompoundModalAnalysisAtASpeed",
    "FaceGearCompoundModalAnalysisAtASpeed",
    "FaceGearMeshCompoundModalAnalysisAtASpeed",
    "FaceGearSetCompoundModalAnalysisAtASpeed",
    "FEPartCompoundModalAnalysisAtASpeed",
    "FlexiblePinAssemblyCompoundModalAnalysisAtASpeed",
    "GearCompoundModalAnalysisAtASpeed",
    "GearMeshCompoundModalAnalysisAtASpeed",
    "GearSetCompoundModalAnalysisAtASpeed",
    "GuideDxfModelCompoundModalAnalysisAtASpeed",
    "HypoidGearCompoundModalAnalysisAtASpeed",
    "HypoidGearMeshCompoundModalAnalysisAtASpeed",
    "HypoidGearSetCompoundModalAnalysisAtASpeed",
    "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "MassDiscCompoundModalAnalysisAtASpeed",
    "MeasurementComponentCompoundModalAnalysisAtASpeed",
    "MountableComponentCompoundModalAnalysisAtASpeed",
    "OilSealCompoundModalAnalysisAtASpeed",
    "PartCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
    "PlanetaryConnectionCompoundModalAnalysisAtASpeed",
    "PlanetaryGearSetCompoundModalAnalysisAtASpeed",
    "PlanetCarrierCompoundModalAnalysisAtASpeed",
    "PointLoadCompoundModalAnalysisAtASpeed",
    "PowerLoadCompoundModalAnalysisAtASpeed",
    "PulleyCompoundModalAnalysisAtASpeed",
    "RingPinsCompoundModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed",
    "RollingRingAssemblyCompoundModalAnalysisAtASpeed",
    "RollingRingCompoundModalAnalysisAtASpeed",
    "RollingRingConnectionCompoundModalAnalysisAtASpeed",
    "RootAssemblyCompoundModalAnalysisAtASpeed",
    "ShaftCompoundModalAnalysisAtASpeed",
    "ShaftHubConnectionCompoundModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    "SpecialisedAssemblyCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearMeshCompoundModalAnalysisAtASpeed",
    "SpiralBevelGearSetCompoundModalAnalysisAtASpeed",
    "SpringDamperCompoundModalAnalysisAtASpeed",
    "SpringDamperConnectionCompoundModalAnalysisAtASpeed",
    "SpringDamperHalfCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelGearCompoundModalAnalysisAtASpeed",
    "StraightBevelGearMeshCompoundModalAnalysisAtASpeed",
    "StraightBevelGearSetCompoundModalAnalysisAtASpeed",
    "StraightBevelPlanetGearCompoundModalAnalysisAtASpeed",
    "StraightBevelSunGearCompoundModalAnalysisAtASpeed",
    "SynchroniserCompoundModalAnalysisAtASpeed",
    "SynchroniserHalfCompoundModalAnalysisAtASpeed",
    "SynchroniserPartCompoundModalAnalysisAtASpeed",
    "SynchroniserSleeveCompoundModalAnalysisAtASpeed",
    "TorqueConverterCompoundModalAnalysisAtASpeed",
    "TorqueConverterConnectionCompoundModalAnalysisAtASpeed",
    "TorqueConverterPumpCompoundModalAnalysisAtASpeed",
    "TorqueConverterTurbineCompoundModalAnalysisAtASpeed",
    "UnbalancedMassCompoundModalAnalysisAtASpeed",
    "VirtualComponentCompoundModalAnalysisAtASpeed",
    "WormGearCompoundModalAnalysisAtASpeed",
    "WormGearMeshCompoundModalAnalysisAtASpeed",
    "WormGearSetCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearMeshCompoundModalAnalysisAtASpeed",
    "ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5246 import AbstractAssemblyCompoundModalAnalysisAtASpeed
    from ._5247 import AbstractShaftCompoundModalAnalysisAtASpeed
    from ._5248 import AbstractShaftOrHousingCompoundModalAnalysisAtASpeed
    from ._5249 import (
        AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5250 import AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
    from ._5251 import AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5252 import AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5253 import AssemblyCompoundModalAnalysisAtASpeed
    from ._5254 import BearingCompoundModalAnalysisAtASpeed
    from ._5255 import BeltConnectionCompoundModalAnalysisAtASpeed
    from ._5256 import BeltDriveCompoundModalAnalysisAtASpeed
    from ._5257 import BevelDifferentialGearCompoundModalAnalysisAtASpeed
    from ._5258 import BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
    from ._5259 import BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
    from ._5260 import BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
    from ._5261 import BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
    from ._5262 import BevelGearCompoundModalAnalysisAtASpeed
    from ._5263 import BevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5264 import BevelGearSetCompoundModalAnalysisAtASpeed
    from ._5265 import BoltCompoundModalAnalysisAtASpeed
    from ._5266 import BoltedJointCompoundModalAnalysisAtASpeed
    from ._5267 import ClutchCompoundModalAnalysisAtASpeed
    from ._5268 import ClutchConnectionCompoundModalAnalysisAtASpeed
    from ._5269 import ClutchHalfCompoundModalAnalysisAtASpeed
    from ._5270 import CoaxialConnectionCompoundModalAnalysisAtASpeed
    from ._5271 import ComponentCompoundModalAnalysisAtASpeed
    from ._5272 import ConceptCouplingCompoundModalAnalysisAtASpeed
    from ._5273 import ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5274 import ConceptCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5275 import ConceptGearCompoundModalAnalysisAtASpeed
    from ._5276 import ConceptGearMeshCompoundModalAnalysisAtASpeed
    from ._5277 import ConceptGearSetCompoundModalAnalysisAtASpeed
    from ._5278 import ConicalGearCompoundModalAnalysisAtASpeed
    from ._5279 import ConicalGearMeshCompoundModalAnalysisAtASpeed
    from ._5280 import ConicalGearSetCompoundModalAnalysisAtASpeed
    from ._5281 import ConnectionCompoundModalAnalysisAtASpeed
    from ._5282 import ConnectorCompoundModalAnalysisAtASpeed
    from ._5283 import CouplingCompoundModalAnalysisAtASpeed
    from ._5284 import CouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5285 import CouplingHalfCompoundModalAnalysisAtASpeed
    from ._5286 import CVTBeltConnectionCompoundModalAnalysisAtASpeed
    from ._5287 import CVTCompoundModalAnalysisAtASpeed
    from ._5288 import CVTPulleyCompoundModalAnalysisAtASpeed
    from ._5289 import CycloidalAssemblyCompoundModalAnalysisAtASpeed
    from ._5290 import (
        CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5291 import CycloidalDiscCompoundModalAnalysisAtASpeed
    from ._5292 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed,
    )
    from ._5293 import CylindricalGearCompoundModalAnalysisAtASpeed
    from ._5294 import CylindricalGearMeshCompoundModalAnalysisAtASpeed
    from ._5295 import CylindricalGearSetCompoundModalAnalysisAtASpeed
    from ._5296 import CylindricalPlanetGearCompoundModalAnalysisAtASpeed
    from ._5297 import DatumCompoundModalAnalysisAtASpeed
    from ._5298 import ExternalCADModelCompoundModalAnalysisAtASpeed
    from ._5299 import FaceGearCompoundModalAnalysisAtASpeed
    from ._5300 import FaceGearMeshCompoundModalAnalysisAtASpeed
    from ._5301 import FaceGearSetCompoundModalAnalysisAtASpeed
    from ._5302 import FEPartCompoundModalAnalysisAtASpeed
    from ._5303 import FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
    from ._5304 import GearCompoundModalAnalysisAtASpeed
    from ._5305 import GearMeshCompoundModalAnalysisAtASpeed
    from ._5306 import GearSetCompoundModalAnalysisAtASpeed
    from ._5307 import GuideDxfModelCompoundModalAnalysisAtASpeed
    from ._5308 import HypoidGearCompoundModalAnalysisAtASpeed
    from ._5309 import HypoidGearMeshCompoundModalAnalysisAtASpeed
    from ._5310 import HypoidGearSetCompoundModalAnalysisAtASpeed
    from ._5311 import InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5312 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
    from ._5313 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5314 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5315 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
    from ._5316 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5317 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5318 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed,
    )
    from ._5319 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed,
    )
    from ._5320 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed,
    )
    from ._5321 import MassDiscCompoundModalAnalysisAtASpeed
    from ._5322 import MeasurementComponentCompoundModalAnalysisAtASpeed
    from ._5323 import MountableComponentCompoundModalAnalysisAtASpeed
    from ._5324 import OilSealCompoundModalAnalysisAtASpeed
    from ._5325 import PartCompoundModalAnalysisAtASpeed
    from ._5326 import PartToPartShearCouplingCompoundModalAnalysisAtASpeed
    from ._5327 import PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
    from ._5328 import PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed
    from ._5329 import PlanetaryConnectionCompoundModalAnalysisAtASpeed
    from ._5330 import PlanetaryGearSetCompoundModalAnalysisAtASpeed
    from ._5331 import PlanetCarrierCompoundModalAnalysisAtASpeed
    from ._5332 import PointLoadCompoundModalAnalysisAtASpeed
    from ._5333 import PowerLoadCompoundModalAnalysisAtASpeed
    from ._5334 import PulleyCompoundModalAnalysisAtASpeed
    from ._5335 import RingPinsCompoundModalAnalysisAtASpeed
    from ._5336 import RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
    from ._5337 import RollingRingAssemblyCompoundModalAnalysisAtASpeed
    from ._5338 import RollingRingCompoundModalAnalysisAtASpeed
    from ._5339 import RollingRingConnectionCompoundModalAnalysisAtASpeed
    from ._5340 import RootAssemblyCompoundModalAnalysisAtASpeed
    from ._5341 import ShaftCompoundModalAnalysisAtASpeed
    from ._5342 import ShaftHubConnectionCompoundModalAnalysisAtASpeed
    from ._5343 import ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed
    from ._5344 import SpecialisedAssemblyCompoundModalAnalysisAtASpeed
    from ._5345 import SpiralBevelGearCompoundModalAnalysisAtASpeed
    from ._5346 import SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5347 import SpiralBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5348 import SpringDamperCompoundModalAnalysisAtASpeed
    from ._5349 import SpringDamperConnectionCompoundModalAnalysisAtASpeed
    from ._5350 import SpringDamperHalfCompoundModalAnalysisAtASpeed
    from ._5351 import StraightBevelDiffGearCompoundModalAnalysisAtASpeed
    from ._5352 import StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
    from ._5353 import StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
    from ._5354 import StraightBevelGearCompoundModalAnalysisAtASpeed
    from ._5355 import StraightBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5356 import StraightBevelGearSetCompoundModalAnalysisAtASpeed
    from ._5357 import StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
    from ._5358 import StraightBevelSunGearCompoundModalAnalysisAtASpeed
    from ._5359 import SynchroniserCompoundModalAnalysisAtASpeed
    from ._5360 import SynchroniserHalfCompoundModalAnalysisAtASpeed
    from ._5361 import SynchroniserPartCompoundModalAnalysisAtASpeed
    from ._5362 import SynchroniserSleeveCompoundModalAnalysisAtASpeed
    from ._5363 import TorqueConverterCompoundModalAnalysisAtASpeed
    from ._5364 import TorqueConverterConnectionCompoundModalAnalysisAtASpeed
    from ._5365 import TorqueConverterPumpCompoundModalAnalysisAtASpeed
    from ._5366 import TorqueConverterTurbineCompoundModalAnalysisAtASpeed
    from ._5367 import UnbalancedMassCompoundModalAnalysisAtASpeed
    from ._5368 import VirtualComponentCompoundModalAnalysisAtASpeed
    from ._5369 import WormGearCompoundModalAnalysisAtASpeed
    from ._5370 import WormGearMeshCompoundModalAnalysisAtASpeed
    from ._5371 import WormGearSetCompoundModalAnalysisAtASpeed
    from ._5372 import ZerolBevelGearCompoundModalAnalysisAtASpeed
    from ._5373 import ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
    from ._5374 import ZerolBevelGearSetCompoundModalAnalysisAtASpeed
else:
    import_structure = {
        "_5246": ["AbstractAssemblyCompoundModalAnalysisAtASpeed"],
        "_5247": ["AbstractShaftCompoundModalAnalysisAtASpeed"],
        "_5248": ["AbstractShaftOrHousingCompoundModalAnalysisAtASpeed"],
        "_5249": [
            "AbstractShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5250": ["AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed"],
        "_5251": ["AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5252": ["AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5253": ["AssemblyCompoundModalAnalysisAtASpeed"],
        "_5254": ["BearingCompoundModalAnalysisAtASpeed"],
        "_5255": ["BeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5256": ["BeltDriveCompoundModalAnalysisAtASpeed"],
        "_5257": ["BevelDifferentialGearCompoundModalAnalysisAtASpeed"],
        "_5258": ["BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed"],
        "_5259": ["BevelDifferentialGearSetCompoundModalAnalysisAtASpeed"],
        "_5260": ["BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5261": ["BevelDifferentialSunGearCompoundModalAnalysisAtASpeed"],
        "_5262": ["BevelGearCompoundModalAnalysisAtASpeed"],
        "_5263": ["BevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5264": ["BevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5265": ["BoltCompoundModalAnalysisAtASpeed"],
        "_5266": ["BoltedJointCompoundModalAnalysisAtASpeed"],
        "_5267": ["ClutchCompoundModalAnalysisAtASpeed"],
        "_5268": ["ClutchConnectionCompoundModalAnalysisAtASpeed"],
        "_5269": ["ClutchHalfCompoundModalAnalysisAtASpeed"],
        "_5270": ["CoaxialConnectionCompoundModalAnalysisAtASpeed"],
        "_5271": ["ComponentCompoundModalAnalysisAtASpeed"],
        "_5272": ["ConceptCouplingCompoundModalAnalysisAtASpeed"],
        "_5273": ["ConceptCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5274": ["ConceptCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5275": ["ConceptGearCompoundModalAnalysisAtASpeed"],
        "_5276": ["ConceptGearMeshCompoundModalAnalysisAtASpeed"],
        "_5277": ["ConceptGearSetCompoundModalAnalysisAtASpeed"],
        "_5278": ["ConicalGearCompoundModalAnalysisAtASpeed"],
        "_5279": ["ConicalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5280": ["ConicalGearSetCompoundModalAnalysisAtASpeed"],
        "_5281": ["ConnectionCompoundModalAnalysisAtASpeed"],
        "_5282": ["ConnectorCompoundModalAnalysisAtASpeed"],
        "_5283": ["CouplingCompoundModalAnalysisAtASpeed"],
        "_5284": ["CouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5285": ["CouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5286": ["CVTBeltConnectionCompoundModalAnalysisAtASpeed"],
        "_5287": ["CVTCompoundModalAnalysisAtASpeed"],
        "_5288": ["CVTPulleyCompoundModalAnalysisAtASpeed"],
        "_5289": ["CycloidalAssemblyCompoundModalAnalysisAtASpeed"],
        "_5290": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysisAtASpeed"],
        "_5291": ["CycloidalDiscCompoundModalAnalysisAtASpeed"],
        "_5292": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysisAtASpeed"
        ],
        "_5293": ["CylindricalGearCompoundModalAnalysisAtASpeed"],
        "_5294": ["CylindricalGearMeshCompoundModalAnalysisAtASpeed"],
        "_5295": ["CylindricalGearSetCompoundModalAnalysisAtASpeed"],
        "_5296": ["CylindricalPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5297": ["DatumCompoundModalAnalysisAtASpeed"],
        "_5298": ["ExternalCADModelCompoundModalAnalysisAtASpeed"],
        "_5299": ["FaceGearCompoundModalAnalysisAtASpeed"],
        "_5300": ["FaceGearMeshCompoundModalAnalysisAtASpeed"],
        "_5301": ["FaceGearSetCompoundModalAnalysisAtASpeed"],
        "_5302": ["FEPartCompoundModalAnalysisAtASpeed"],
        "_5303": ["FlexiblePinAssemblyCompoundModalAnalysisAtASpeed"],
        "_5304": ["GearCompoundModalAnalysisAtASpeed"],
        "_5305": ["GearMeshCompoundModalAnalysisAtASpeed"],
        "_5306": ["GearSetCompoundModalAnalysisAtASpeed"],
        "_5307": ["GuideDxfModelCompoundModalAnalysisAtASpeed"],
        "_5308": ["HypoidGearCompoundModalAnalysisAtASpeed"],
        "_5309": ["HypoidGearMeshCompoundModalAnalysisAtASpeed"],
        "_5310": ["HypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5311": ["InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5312": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed"],
        "_5313": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5314": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5315": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed"],
        "_5316": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5317": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed"],
        "_5318": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed"
        ],
        "_5319": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed"
        ],
        "_5320": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed"
        ],
        "_5321": ["MassDiscCompoundModalAnalysisAtASpeed"],
        "_5322": ["MeasurementComponentCompoundModalAnalysisAtASpeed"],
        "_5323": ["MountableComponentCompoundModalAnalysisAtASpeed"],
        "_5324": ["OilSealCompoundModalAnalysisAtASpeed"],
        "_5325": ["PartCompoundModalAnalysisAtASpeed"],
        "_5326": ["PartToPartShearCouplingCompoundModalAnalysisAtASpeed"],
        "_5327": ["PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed"],
        "_5328": ["PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed"],
        "_5329": ["PlanetaryConnectionCompoundModalAnalysisAtASpeed"],
        "_5330": ["PlanetaryGearSetCompoundModalAnalysisAtASpeed"],
        "_5331": ["PlanetCarrierCompoundModalAnalysisAtASpeed"],
        "_5332": ["PointLoadCompoundModalAnalysisAtASpeed"],
        "_5333": ["PowerLoadCompoundModalAnalysisAtASpeed"],
        "_5334": ["PulleyCompoundModalAnalysisAtASpeed"],
        "_5335": ["RingPinsCompoundModalAnalysisAtASpeed"],
        "_5336": ["RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed"],
        "_5337": ["RollingRingAssemblyCompoundModalAnalysisAtASpeed"],
        "_5338": ["RollingRingCompoundModalAnalysisAtASpeed"],
        "_5339": ["RollingRingConnectionCompoundModalAnalysisAtASpeed"],
        "_5340": ["RootAssemblyCompoundModalAnalysisAtASpeed"],
        "_5341": ["ShaftCompoundModalAnalysisAtASpeed"],
        "_5342": ["ShaftHubConnectionCompoundModalAnalysisAtASpeed"],
        "_5343": ["ShaftToMountableComponentConnectionCompoundModalAnalysisAtASpeed"],
        "_5344": ["SpecialisedAssemblyCompoundModalAnalysisAtASpeed"],
        "_5345": ["SpiralBevelGearCompoundModalAnalysisAtASpeed"],
        "_5346": ["SpiralBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5347": ["SpiralBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5348": ["SpringDamperCompoundModalAnalysisAtASpeed"],
        "_5349": ["SpringDamperConnectionCompoundModalAnalysisAtASpeed"],
        "_5350": ["SpringDamperHalfCompoundModalAnalysisAtASpeed"],
        "_5351": ["StraightBevelDiffGearCompoundModalAnalysisAtASpeed"],
        "_5352": ["StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed"],
        "_5353": ["StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed"],
        "_5354": ["StraightBevelGearCompoundModalAnalysisAtASpeed"],
        "_5355": ["StraightBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5356": ["StraightBevelGearSetCompoundModalAnalysisAtASpeed"],
        "_5357": ["StraightBevelPlanetGearCompoundModalAnalysisAtASpeed"],
        "_5358": ["StraightBevelSunGearCompoundModalAnalysisAtASpeed"],
        "_5359": ["SynchroniserCompoundModalAnalysisAtASpeed"],
        "_5360": ["SynchroniserHalfCompoundModalAnalysisAtASpeed"],
        "_5361": ["SynchroniserPartCompoundModalAnalysisAtASpeed"],
        "_5362": ["SynchroniserSleeveCompoundModalAnalysisAtASpeed"],
        "_5363": ["TorqueConverterCompoundModalAnalysisAtASpeed"],
        "_5364": ["TorqueConverterConnectionCompoundModalAnalysisAtASpeed"],
        "_5365": ["TorqueConverterPumpCompoundModalAnalysisAtASpeed"],
        "_5366": ["TorqueConverterTurbineCompoundModalAnalysisAtASpeed"],
        "_5367": ["UnbalancedMassCompoundModalAnalysisAtASpeed"],
        "_5368": ["VirtualComponentCompoundModalAnalysisAtASpeed"],
        "_5369": ["WormGearCompoundModalAnalysisAtASpeed"],
        "_5370": ["WormGearMeshCompoundModalAnalysisAtASpeed"],
        "_5371": ["WormGearSetCompoundModalAnalysisAtASpeed"],
        "_5372": ["ZerolBevelGearCompoundModalAnalysisAtASpeed"],
        "_5373": ["ZerolBevelGearMeshCompoundModalAnalysisAtASpeed"],
        "_5374": ["ZerolBevelGearSetCompoundModalAnalysisAtASpeed"],
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

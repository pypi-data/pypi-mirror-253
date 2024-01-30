"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7269 import AbstractAssemblyAdvancedSystemDeflection
    from ._7270 import AbstractShaftAdvancedSystemDeflection
    from ._7271 import AbstractShaftOrHousingAdvancedSystemDeflection
    from ._7272 import (
        AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection,
    )
    from ._7273 import AdvancedSystemDeflection
    from ._7274 import AdvancedSystemDeflectionOptions
    from ._7275 import AdvancedSystemDeflectionSubAnalysis
    from ._7276 import AGMAGleasonConicalGearAdvancedSystemDeflection
    from ._7277 import AGMAGleasonConicalGearMeshAdvancedSystemDeflection
    from ._7278 import AGMAGleasonConicalGearSetAdvancedSystemDeflection
    from ._7279 import AssemblyAdvancedSystemDeflection
    from ._7280 import BearingAdvancedSystemDeflection
    from ._7281 import BeltConnectionAdvancedSystemDeflection
    from ._7282 import BeltDriveAdvancedSystemDeflection
    from ._7283 import BevelDifferentialGearAdvancedSystemDeflection
    from ._7284 import BevelDifferentialGearMeshAdvancedSystemDeflection
    from ._7285 import BevelDifferentialGearSetAdvancedSystemDeflection
    from ._7286 import BevelDifferentialPlanetGearAdvancedSystemDeflection
    from ._7287 import BevelDifferentialSunGearAdvancedSystemDeflection
    from ._7288 import BevelGearAdvancedSystemDeflection
    from ._7289 import BevelGearMeshAdvancedSystemDeflection
    from ._7290 import BevelGearSetAdvancedSystemDeflection
    from ._7291 import BoltAdvancedSystemDeflection
    from ._7292 import BoltedJointAdvancedSystemDeflection
    from ._7293 import ClutchAdvancedSystemDeflection
    from ._7294 import ClutchConnectionAdvancedSystemDeflection
    from ._7295 import ClutchHalfAdvancedSystemDeflection
    from ._7296 import CoaxialConnectionAdvancedSystemDeflection
    from ._7297 import ComponentAdvancedSystemDeflection
    from ._7298 import ConceptCouplingAdvancedSystemDeflection
    from ._7299 import ConceptCouplingConnectionAdvancedSystemDeflection
    from ._7300 import ConceptCouplingHalfAdvancedSystemDeflection
    from ._7301 import ConceptGearAdvancedSystemDeflection
    from ._7302 import ConceptGearMeshAdvancedSystemDeflection
    from ._7303 import ConceptGearSetAdvancedSystemDeflection
    from ._7304 import ConicalGearAdvancedSystemDeflection
    from ._7305 import ConicalGearMeshAdvancedSystemDeflection
    from ._7306 import ConicalGearSetAdvancedSystemDeflection
    from ._7307 import ConnectionAdvancedSystemDeflection
    from ._7308 import ConnectorAdvancedSystemDeflection
    from ._7309 import ContactChartPerToothPass
    from ._7310 import CouplingAdvancedSystemDeflection
    from ._7311 import CouplingConnectionAdvancedSystemDeflection
    from ._7312 import CouplingHalfAdvancedSystemDeflection
    from ._7313 import CVTAdvancedSystemDeflection
    from ._7314 import CVTBeltConnectionAdvancedSystemDeflection
    from ._7315 import CVTPulleyAdvancedSystemDeflection
    from ._7316 import CycloidalAssemblyAdvancedSystemDeflection
    from ._7317 import CycloidalDiscAdvancedSystemDeflection
    from ._7318 import CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
    from ._7319 import CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
    from ._7320 import CylindricalGearAdvancedSystemDeflection
    from ._7321 import CylindricalGearMeshAdvancedSystemDeflection
    from ._7322 import CylindricalGearSetAdvancedSystemDeflection
    from ._7323 import CylindricalMeshedGearAdvancedSystemDeflection
    from ._7324 import CylindricalPlanetGearAdvancedSystemDeflection
    from ._7325 import DatumAdvancedSystemDeflection
    from ._7326 import ExternalCADModelAdvancedSystemDeflection
    from ._7327 import FaceGearAdvancedSystemDeflection
    from ._7328 import FaceGearMeshAdvancedSystemDeflection
    from ._7329 import FaceGearSetAdvancedSystemDeflection
    from ._7330 import FEPartAdvancedSystemDeflection
    from ._7331 import FlexiblePinAssemblyAdvancedSystemDeflection
    from ._7332 import GearAdvancedSystemDeflection
    from ._7333 import GearMeshAdvancedSystemDeflection
    from ._7334 import GearSetAdvancedSystemDeflection
    from ._7335 import GuideDxfModelAdvancedSystemDeflection
    from ._7336 import HypoidGearAdvancedSystemDeflection
    from ._7337 import HypoidGearMeshAdvancedSystemDeflection
    from ._7338 import HypoidGearSetAdvancedSystemDeflection
    from ._7339 import InterMountableComponentConnectionAdvancedSystemDeflection
    from ._7340 import KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
    from ._7341 import KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
    from ._7342 import KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
    from ._7343 import KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
    from ._7344 import KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
    from ._7345 import KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
    from ._7346 import KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
    from ._7347 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection,
    )
    from ._7348 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection,
    )
    from ._7349 import UseLtcaInAsdOption
    from ._7350 import MassDiscAdvancedSystemDeflection
    from ._7351 import MeasurementComponentAdvancedSystemDeflection
    from ._7352 import MountableComponentAdvancedSystemDeflection
    from ._7353 import OilSealAdvancedSystemDeflection
    from ._7354 import PartAdvancedSystemDeflection
    from ._7355 import PartToPartShearCouplingAdvancedSystemDeflection
    from ._7356 import PartToPartShearCouplingConnectionAdvancedSystemDeflection
    from ._7357 import PartToPartShearCouplingHalfAdvancedSystemDeflection
    from ._7358 import PlanetaryConnectionAdvancedSystemDeflection
    from ._7359 import PlanetaryGearSetAdvancedSystemDeflection
    from ._7360 import PlanetCarrierAdvancedSystemDeflection
    from ._7361 import PointLoadAdvancedSystemDeflection
    from ._7362 import PowerLoadAdvancedSystemDeflection
    from ._7363 import PulleyAdvancedSystemDeflection
    from ._7364 import RingPinsAdvancedSystemDeflection
    from ._7365 import RingPinsToDiscConnectionAdvancedSystemDeflection
    from ._7366 import RollingRingAdvancedSystemDeflection
    from ._7367 import RollingRingAssemblyAdvancedSystemDeflection
    from ._7368 import RollingRingConnectionAdvancedSystemDeflection
    from ._7369 import RootAssemblyAdvancedSystemDeflection
    from ._7370 import ShaftAdvancedSystemDeflection
    from ._7371 import ShaftHubConnectionAdvancedSystemDeflection
    from ._7372 import ShaftToMountableComponentConnectionAdvancedSystemDeflection
    from ._7373 import SpecialisedAssemblyAdvancedSystemDeflection
    from ._7374 import SpiralBevelGearAdvancedSystemDeflection
    from ._7375 import SpiralBevelGearMeshAdvancedSystemDeflection
    from ._7376 import SpiralBevelGearSetAdvancedSystemDeflection
    from ._7377 import SpringDamperAdvancedSystemDeflection
    from ._7378 import SpringDamperConnectionAdvancedSystemDeflection
    from ._7379 import SpringDamperHalfAdvancedSystemDeflection
    from ._7380 import StraightBevelDiffGearAdvancedSystemDeflection
    from ._7381 import StraightBevelDiffGearMeshAdvancedSystemDeflection
    from ._7382 import StraightBevelDiffGearSetAdvancedSystemDeflection
    from ._7383 import StraightBevelGearAdvancedSystemDeflection
    from ._7384 import StraightBevelGearMeshAdvancedSystemDeflection
    from ._7385 import StraightBevelGearSetAdvancedSystemDeflection
    from ._7386 import StraightBevelPlanetGearAdvancedSystemDeflection
    from ._7387 import StraightBevelSunGearAdvancedSystemDeflection
    from ._7388 import SynchroniserAdvancedSystemDeflection
    from ._7389 import SynchroniserHalfAdvancedSystemDeflection
    from ._7390 import SynchroniserPartAdvancedSystemDeflection
    from ._7391 import SynchroniserSleeveAdvancedSystemDeflection
    from ._7392 import TorqueConverterAdvancedSystemDeflection
    from ._7393 import TorqueConverterConnectionAdvancedSystemDeflection
    from ._7394 import TorqueConverterPumpAdvancedSystemDeflection
    from ._7395 import TorqueConverterTurbineAdvancedSystemDeflection
    from ._7396 import TransmissionErrorToOtherPowerLoad
    from ._7397 import UnbalancedMassAdvancedSystemDeflection
    from ._7398 import VirtualComponentAdvancedSystemDeflection
    from ._7399 import WormGearAdvancedSystemDeflection
    from ._7400 import WormGearMeshAdvancedSystemDeflection
    from ._7401 import WormGearSetAdvancedSystemDeflection
    from ._7402 import ZerolBevelGearAdvancedSystemDeflection
    from ._7403 import ZerolBevelGearMeshAdvancedSystemDeflection
    from ._7404 import ZerolBevelGearSetAdvancedSystemDeflection
else:
    import_structure = {
        "_7269": ["AbstractAssemblyAdvancedSystemDeflection"],
        "_7270": ["AbstractShaftAdvancedSystemDeflection"],
        "_7271": ["AbstractShaftOrHousingAdvancedSystemDeflection"],
        "_7272": [
            "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ],
        "_7273": ["AdvancedSystemDeflection"],
        "_7274": ["AdvancedSystemDeflectionOptions"],
        "_7275": ["AdvancedSystemDeflectionSubAnalysis"],
        "_7276": ["AGMAGleasonConicalGearAdvancedSystemDeflection"],
        "_7277": ["AGMAGleasonConicalGearMeshAdvancedSystemDeflection"],
        "_7278": ["AGMAGleasonConicalGearSetAdvancedSystemDeflection"],
        "_7279": ["AssemblyAdvancedSystemDeflection"],
        "_7280": ["BearingAdvancedSystemDeflection"],
        "_7281": ["BeltConnectionAdvancedSystemDeflection"],
        "_7282": ["BeltDriveAdvancedSystemDeflection"],
        "_7283": ["BevelDifferentialGearAdvancedSystemDeflection"],
        "_7284": ["BevelDifferentialGearMeshAdvancedSystemDeflection"],
        "_7285": ["BevelDifferentialGearSetAdvancedSystemDeflection"],
        "_7286": ["BevelDifferentialPlanetGearAdvancedSystemDeflection"],
        "_7287": ["BevelDifferentialSunGearAdvancedSystemDeflection"],
        "_7288": ["BevelGearAdvancedSystemDeflection"],
        "_7289": ["BevelGearMeshAdvancedSystemDeflection"],
        "_7290": ["BevelGearSetAdvancedSystemDeflection"],
        "_7291": ["BoltAdvancedSystemDeflection"],
        "_7292": ["BoltedJointAdvancedSystemDeflection"],
        "_7293": ["ClutchAdvancedSystemDeflection"],
        "_7294": ["ClutchConnectionAdvancedSystemDeflection"],
        "_7295": ["ClutchHalfAdvancedSystemDeflection"],
        "_7296": ["CoaxialConnectionAdvancedSystemDeflection"],
        "_7297": ["ComponentAdvancedSystemDeflection"],
        "_7298": ["ConceptCouplingAdvancedSystemDeflection"],
        "_7299": ["ConceptCouplingConnectionAdvancedSystemDeflection"],
        "_7300": ["ConceptCouplingHalfAdvancedSystemDeflection"],
        "_7301": ["ConceptGearAdvancedSystemDeflection"],
        "_7302": ["ConceptGearMeshAdvancedSystemDeflection"],
        "_7303": ["ConceptGearSetAdvancedSystemDeflection"],
        "_7304": ["ConicalGearAdvancedSystemDeflection"],
        "_7305": ["ConicalGearMeshAdvancedSystemDeflection"],
        "_7306": ["ConicalGearSetAdvancedSystemDeflection"],
        "_7307": ["ConnectionAdvancedSystemDeflection"],
        "_7308": ["ConnectorAdvancedSystemDeflection"],
        "_7309": ["ContactChartPerToothPass"],
        "_7310": ["CouplingAdvancedSystemDeflection"],
        "_7311": ["CouplingConnectionAdvancedSystemDeflection"],
        "_7312": ["CouplingHalfAdvancedSystemDeflection"],
        "_7313": ["CVTAdvancedSystemDeflection"],
        "_7314": ["CVTBeltConnectionAdvancedSystemDeflection"],
        "_7315": ["CVTPulleyAdvancedSystemDeflection"],
        "_7316": ["CycloidalAssemblyAdvancedSystemDeflection"],
        "_7317": ["CycloidalDiscAdvancedSystemDeflection"],
        "_7318": ["CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"],
        "_7319": ["CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection"],
        "_7320": ["CylindricalGearAdvancedSystemDeflection"],
        "_7321": ["CylindricalGearMeshAdvancedSystemDeflection"],
        "_7322": ["CylindricalGearSetAdvancedSystemDeflection"],
        "_7323": ["CylindricalMeshedGearAdvancedSystemDeflection"],
        "_7324": ["CylindricalPlanetGearAdvancedSystemDeflection"],
        "_7325": ["DatumAdvancedSystemDeflection"],
        "_7326": ["ExternalCADModelAdvancedSystemDeflection"],
        "_7327": ["FaceGearAdvancedSystemDeflection"],
        "_7328": ["FaceGearMeshAdvancedSystemDeflection"],
        "_7329": ["FaceGearSetAdvancedSystemDeflection"],
        "_7330": ["FEPartAdvancedSystemDeflection"],
        "_7331": ["FlexiblePinAssemblyAdvancedSystemDeflection"],
        "_7332": ["GearAdvancedSystemDeflection"],
        "_7333": ["GearMeshAdvancedSystemDeflection"],
        "_7334": ["GearSetAdvancedSystemDeflection"],
        "_7335": ["GuideDxfModelAdvancedSystemDeflection"],
        "_7336": ["HypoidGearAdvancedSystemDeflection"],
        "_7337": ["HypoidGearMeshAdvancedSystemDeflection"],
        "_7338": ["HypoidGearSetAdvancedSystemDeflection"],
        "_7339": ["InterMountableComponentConnectionAdvancedSystemDeflection"],
        "_7340": ["KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"],
        "_7341": ["KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection"],
        "_7342": ["KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"],
        "_7343": ["KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection"],
        "_7344": ["KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection"],
        "_7345": ["KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection"],
        "_7346": ["KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection"],
        "_7347": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ],
        "_7348": ["KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection"],
        "_7349": ["UseLtcaInAsdOption"],
        "_7350": ["MassDiscAdvancedSystemDeflection"],
        "_7351": ["MeasurementComponentAdvancedSystemDeflection"],
        "_7352": ["MountableComponentAdvancedSystemDeflection"],
        "_7353": ["OilSealAdvancedSystemDeflection"],
        "_7354": ["PartAdvancedSystemDeflection"],
        "_7355": ["PartToPartShearCouplingAdvancedSystemDeflection"],
        "_7356": ["PartToPartShearCouplingConnectionAdvancedSystemDeflection"],
        "_7357": ["PartToPartShearCouplingHalfAdvancedSystemDeflection"],
        "_7358": ["PlanetaryConnectionAdvancedSystemDeflection"],
        "_7359": ["PlanetaryGearSetAdvancedSystemDeflection"],
        "_7360": ["PlanetCarrierAdvancedSystemDeflection"],
        "_7361": ["PointLoadAdvancedSystemDeflection"],
        "_7362": ["PowerLoadAdvancedSystemDeflection"],
        "_7363": ["PulleyAdvancedSystemDeflection"],
        "_7364": ["RingPinsAdvancedSystemDeflection"],
        "_7365": ["RingPinsToDiscConnectionAdvancedSystemDeflection"],
        "_7366": ["RollingRingAdvancedSystemDeflection"],
        "_7367": ["RollingRingAssemblyAdvancedSystemDeflection"],
        "_7368": ["RollingRingConnectionAdvancedSystemDeflection"],
        "_7369": ["RootAssemblyAdvancedSystemDeflection"],
        "_7370": ["ShaftAdvancedSystemDeflection"],
        "_7371": ["ShaftHubConnectionAdvancedSystemDeflection"],
        "_7372": ["ShaftToMountableComponentConnectionAdvancedSystemDeflection"],
        "_7373": ["SpecialisedAssemblyAdvancedSystemDeflection"],
        "_7374": ["SpiralBevelGearAdvancedSystemDeflection"],
        "_7375": ["SpiralBevelGearMeshAdvancedSystemDeflection"],
        "_7376": ["SpiralBevelGearSetAdvancedSystemDeflection"],
        "_7377": ["SpringDamperAdvancedSystemDeflection"],
        "_7378": ["SpringDamperConnectionAdvancedSystemDeflection"],
        "_7379": ["SpringDamperHalfAdvancedSystemDeflection"],
        "_7380": ["StraightBevelDiffGearAdvancedSystemDeflection"],
        "_7381": ["StraightBevelDiffGearMeshAdvancedSystemDeflection"],
        "_7382": ["StraightBevelDiffGearSetAdvancedSystemDeflection"],
        "_7383": ["StraightBevelGearAdvancedSystemDeflection"],
        "_7384": ["StraightBevelGearMeshAdvancedSystemDeflection"],
        "_7385": ["StraightBevelGearSetAdvancedSystemDeflection"],
        "_7386": ["StraightBevelPlanetGearAdvancedSystemDeflection"],
        "_7387": ["StraightBevelSunGearAdvancedSystemDeflection"],
        "_7388": ["SynchroniserAdvancedSystemDeflection"],
        "_7389": ["SynchroniserHalfAdvancedSystemDeflection"],
        "_7390": ["SynchroniserPartAdvancedSystemDeflection"],
        "_7391": ["SynchroniserSleeveAdvancedSystemDeflection"],
        "_7392": ["TorqueConverterAdvancedSystemDeflection"],
        "_7393": ["TorqueConverterConnectionAdvancedSystemDeflection"],
        "_7394": ["TorqueConverterPumpAdvancedSystemDeflection"],
        "_7395": ["TorqueConverterTurbineAdvancedSystemDeflection"],
        "_7396": ["TransmissionErrorToOtherPowerLoad"],
        "_7397": ["UnbalancedMassAdvancedSystemDeflection"],
        "_7398": ["VirtualComponentAdvancedSystemDeflection"],
        "_7399": ["WormGearAdvancedSystemDeflection"],
        "_7400": ["WormGearMeshAdvancedSystemDeflection"],
        "_7401": ["WormGearSetAdvancedSystemDeflection"],
        "_7402": ["ZerolBevelGearAdvancedSystemDeflection"],
        "_7403": ["ZerolBevelGearMeshAdvancedSystemDeflection"],
        "_7404": ["ZerolBevelGearSetAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyAdvancedSystemDeflection",
    "AbstractShaftAdvancedSystemDeflection",
    "AbstractShaftOrHousingAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "AdvancedSystemDeflection",
    "AdvancedSystemDeflectionOptions",
    "AdvancedSystemDeflectionSubAnalysis",
    "AGMAGleasonConicalGearAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetAdvancedSystemDeflection",
    "AssemblyAdvancedSystemDeflection",
    "BearingAdvancedSystemDeflection",
    "BeltConnectionAdvancedSystemDeflection",
    "BeltDriveAdvancedSystemDeflection",
    "BevelDifferentialGearAdvancedSystemDeflection",
    "BevelDifferentialGearMeshAdvancedSystemDeflection",
    "BevelDifferentialGearSetAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearAdvancedSystemDeflection",
    "BevelDifferentialSunGearAdvancedSystemDeflection",
    "BevelGearAdvancedSystemDeflection",
    "BevelGearMeshAdvancedSystemDeflection",
    "BevelGearSetAdvancedSystemDeflection",
    "BoltAdvancedSystemDeflection",
    "BoltedJointAdvancedSystemDeflection",
    "ClutchAdvancedSystemDeflection",
    "ClutchConnectionAdvancedSystemDeflection",
    "ClutchHalfAdvancedSystemDeflection",
    "CoaxialConnectionAdvancedSystemDeflection",
    "ComponentAdvancedSystemDeflection",
    "ConceptCouplingAdvancedSystemDeflection",
    "ConceptCouplingConnectionAdvancedSystemDeflection",
    "ConceptCouplingHalfAdvancedSystemDeflection",
    "ConceptGearAdvancedSystemDeflection",
    "ConceptGearMeshAdvancedSystemDeflection",
    "ConceptGearSetAdvancedSystemDeflection",
    "ConicalGearAdvancedSystemDeflection",
    "ConicalGearMeshAdvancedSystemDeflection",
    "ConicalGearSetAdvancedSystemDeflection",
    "ConnectionAdvancedSystemDeflection",
    "ConnectorAdvancedSystemDeflection",
    "ContactChartPerToothPass",
    "CouplingAdvancedSystemDeflection",
    "CouplingConnectionAdvancedSystemDeflection",
    "CouplingHalfAdvancedSystemDeflection",
    "CVTAdvancedSystemDeflection",
    "CVTBeltConnectionAdvancedSystemDeflection",
    "CVTPulleyAdvancedSystemDeflection",
    "CycloidalAssemblyAdvancedSystemDeflection",
    "CycloidalDiscAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection",
    "CylindricalGearAdvancedSystemDeflection",
    "CylindricalGearMeshAdvancedSystemDeflection",
    "CylindricalGearSetAdvancedSystemDeflection",
    "CylindricalMeshedGearAdvancedSystemDeflection",
    "CylindricalPlanetGearAdvancedSystemDeflection",
    "DatumAdvancedSystemDeflection",
    "ExternalCADModelAdvancedSystemDeflection",
    "FaceGearAdvancedSystemDeflection",
    "FaceGearMeshAdvancedSystemDeflection",
    "FaceGearSetAdvancedSystemDeflection",
    "FEPartAdvancedSystemDeflection",
    "FlexiblePinAssemblyAdvancedSystemDeflection",
    "GearAdvancedSystemDeflection",
    "GearMeshAdvancedSystemDeflection",
    "GearSetAdvancedSystemDeflection",
    "GuideDxfModelAdvancedSystemDeflection",
    "HypoidGearAdvancedSystemDeflection",
    "HypoidGearMeshAdvancedSystemDeflection",
    "HypoidGearSetAdvancedSystemDeflection",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection",
    "UseLtcaInAsdOption",
    "MassDiscAdvancedSystemDeflection",
    "MeasurementComponentAdvancedSystemDeflection",
    "MountableComponentAdvancedSystemDeflection",
    "OilSealAdvancedSystemDeflection",
    "PartAdvancedSystemDeflection",
    "PartToPartShearCouplingAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfAdvancedSystemDeflection",
    "PlanetaryConnectionAdvancedSystemDeflection",
    "PlanetaryGearSetAdvancedSystemDeflection",
    "PlanetCarrierAdvancedSystemDeflection",
    "PointLoadAdvancedSystemDeflection",
    "PowerLoadAdvancedSystemDeflection",
    "PulleyAdvancedSystemDeflection",
    "RingPinsAdvancedSystemDeflection",
    "RingPinsToDiscConnectionAdvancedSystemDeflection",
    "RollingRingAdvancedSystemDeflection",
    "RollingRingAssemblyAdvancedSystemDeflection",
    "RollingRingConnectionAdvancedSystemDeflection",
    "RootAssemblyAdvancedSystemDeflection",
    "ShaftAdvancedSystemDeflection",
    "ShaftHubConnectionAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionAdvancedSystemDeflection",
    "SpecialisedAssemblyAdvancedSystemDeflection",
    "SpiralBevelGearAdvancedSystemDeflection",
    "SpiralBevelGearMeshAdvancedSystemDeflection",
    "SpiralBevelGearSetAdvancedSystemDeflection",
    "SpringDamperAdvancedSystemDeflection",
    "SpringDamperConnectionAdvancedSystemDeflection",
    "SpringDamperHalfAdvancedSystemDeflection",
    "StraightBevelDiffGearAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshAdvancedSystemDeflection",
    "StraightBevelDiffGearSetAdvancedSystemDeflection",
    "StraightBevelGearAdvancedSystemDeflection",
    "StraightBevelGearMeshAdvancedSystemDeflection",
    "StraightBevelGearSetAdvancedSystemDeflection",
    "StraightBevelPlanetGearAdvancedSystemDeflection",
    "StraightBevelSunGearAdvancedSystemDeflection",
    "SynchroniserAdvancedSystemDeflection",
    "SynchroniserHalfAdvancedSystemDeflection",
    "SynchroniserPartAdvancedSystemDeflection",
    "SynchroniserSleeveAdvancedSystemDeflection",
    "TorqueConverterAdvancedSystemDeflection",
    "TorqueConverterConnectionAdvancedSystemDeflection",
    "TorqueConverterPumpAdvancedSystemDeflection",
    "TorqueConverterTurbineAdvancedSystemDeflection",
    "TransmissionErrorToOtherPowerLoad",
    "UnbalancedMassAdvancedSystemDeflection",
    "VirtualComponentAdvancedSystemDeflection",
    "WormGearAdvancedSystemDeflection",
    "WormGearMeshAdvancedSystemDeflection",
    "WormGearSetAdvancedSystemDeflection",
    "ZerolBevelGearAdvancedSystemDeflection",
    "ZerolBevelGearMeshAdvancedSystemDeflection",
    "ZerolBevelGearSetAdvancedSystemDeflection",
)

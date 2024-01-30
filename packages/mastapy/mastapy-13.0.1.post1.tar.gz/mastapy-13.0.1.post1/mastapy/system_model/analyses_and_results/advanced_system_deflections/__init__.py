"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7270 import AbstractAssemblyAdvancedSystemDeflection
    from ._7271 import AbstractShaftAdvancedSystemDeflection
    from ._7272 import AbstractShaftOrHousingAdvancedSystemDeflection
    from ._7273 import (
        AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection,
    )
    from ._7274 import AdvancedSystemDeflection
    from ._7275 import AdvancedSystemDeflectionOptions
    from ._7276 import AdvancedSystemDeflectionSubAnalysis
    from ._7277 import AGMAGleasonConicalGearAdvancedSystemDeflection
    from ._7278 import AGMAGleasonConicalGearMeshAdvancedSystemDeflection
    from ._7279 import AGMAGleasonConicalGearSetAdvancedSystemDeflection
    from ._7280 import AssemblyAdvancedSystemDeflection
    from ._7281 import BearingAdvancedSystemDeflection
    from ._7282 import BeltConnectionAdvancedSystemDeflection
    from ._7283 import BeltDriveAdvancedSystemDeflection
    from ._7284 import BevelDifferentialGearAdvancedSystemDeflection
    from ._7285 import BevelDifferentialGearMeshAdvancedSystemDeflection
    from ._7286 import BevelDifferentialGearSetAdvancedSystemDeflection
    from ._7287 import BevelDifferentialPlanetGearAdvancedSystemDeflection
    from ._7288 import BevelDifferentialSunGearAdvancedSystemDeflection
    from ._7289 import BevelGearAdvancedSystemDeflection
    from ._7290 import BevelGearMeshAdvancedSystemDeflection
    from ._7291 import BevelGearSetAdvancedSystemDeflection
    from ._7292 import BoltAdvancedSystemDeflection
    from ._7293 import BoltedJointAdvancedSystemDeflection
    from ._7294 import ClutchAdvancedSystemDeflection
    from ._7295 import ClutchConnectionAdvancedSystemDeflection
    from ._7296 import ClutchHalfAdvancedSystemDeflection
    from ._7297 import CoaxialConnectionAdvancedSystemDeflection
    from ._7298 import ComponentAdvancedSystemDeflection
    from ._7299 import ConceptCouplingAdvancedSystemDeflection
    from ._7300 import ConceptCouplingConnectionAdvancedSystemDeflection
    from ._7301 import ConceptCouplingHalfAdvancedSystemDeflection
    from ._7302 import ConceptGearAdvancedSystemDeflection
    from ._7303 import ConceptGearMeshAdvancedSystemDeflection
    from ._7304 import ConceptGearSetAdvancedSystemDeflection
    from ._7305 import ConicalGearAdvancedSystemDeflection
    from ._7306 import ConicalGearMeshAdvancedSystemDeflection
    from ._7307 import ConicalGearSetAdvancedSystemDeflection
    from ._7308 import ConnectionAdvancedSystemDeflection
    from ._7309 import ConnectorAdvancedSystemDeflection
    from ._7310 import ContactChartPerToothPass
    from ._7311 import CouplingAdvancedSystemDeflection
    from ._7312 import CouplingConnectionAdvancedSystemDeflection
    from ._7313 import CouplingHalfAdvancedSystemDeflection
    from ._7314 import CVTAdvancedSystemDeflection
    from ._7315 import CVTBeltConnectionAdvancedSystemDeflection
    from ._7316 import CVTPulleyAdvancedSystemDeflection
    from ._7317 import CycloidalAssemblyAdvancedSystemDeflection
    from ._7318 import CycloidalDiscAdvancedSystemDeflection
    from ._7319 import CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
    from ._7320 import CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
    from ._7321 import CylindricalGearAdvancedSystemDeflection
    from ._7322 import CylindricalGearMeshAdvancedSystemDeflection
    from ._7323 import CylindricalGearSetAdvancedSystemDeflection
    from ._7324 import CylindricalMeshedGearAdvancedSystemDeflection
    from ._7325 import CylindricalPlanetGearAdvancedSystemDeflection
    from ._7326 import DatumAdvancedSystemDeflection
    from ._7327 import ExternalCADModelAdvancedSystemDeflection
    from ._7328 import FaceGearAdvancedSystemDeflection
    from ._7329 import FaceGearMeshAdvancedSystemDeflection
    from ._7330 import FaceGearSetAdvancedSystemDeflection
    from ._7331 import FEPartAdvancedSystemDeflection
    from ._7332 import FlexiblePinAssemblyAdvancedSystemDeflection
    from ._7333 import GearAdvancedSystemDeflection
    from ._7334 import GearMeshAdvancedSystemDeflection
    from ._7335 import GearSetAdvancedSystemDeflection
    from ._7336 import GuideDxfModelAdvancedSystemDeflection
    from ._7337 import HypoidGearAdvancedSystemDeflection
    from ._7338 import HypoidGearMeshAdvancedSystemDeflection
    from ._7339 import HypoidGearSetAdvancedSystemDeflection
    from ._7340 import InterMountableComponentConnectionAdvancedSystemDeflection
    from ._7341 import KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
    from ._7342 import KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
    from ._7343 import KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
    from ._7344 import KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
    from ._7345 import KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
    from ._7346 import KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
    from ._7347 import KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
    from ._7348 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection,
    )
    from ._7349 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection,
    )
    from ._7350 import UseLtcaInAsdOption
    from ._7351 import MassDiscAdvancedSystemDeflection
    from ._7352 import MeasurementComponentAdvancedSystemDeflection
    from ._7353 import MountableComponentAdvancedSystemDeflection
    from ._7354 import OilSealAdvancedSystemDeflection
    from ._7355 import PartAdvancedSystemDeflection
    from ._7356 import PartToPartShearCouplingAdvancedSystemDeflection
    from ._7357 import PartToPartShearCouplingConnectionAdvancedSystemDeflection
    from ._7358 import PartToPartShearCouplingHalfAdvancedSystemDeflection
    from ._7359 import PlanetaryConnectionAdvancedSystemDeflection
    from ._7360 import PlanetaryGearSetAdvancedSystemDeflection
    from ._7361 import PlanetCarrierAdvancedSystemDeflection
    from ._7362 import PointLoadAdvancedSystemDeflection
    from ._7363 import PowerLoadAdvancedSystemDeflection
    from ._7364 import PulleyAdvancedSystemDeflection
    from ._7365 import RingPinsAdvancedSystemDeflection
    from ._7366 import RingPinsToDiscConnectionAdvancedSystemDeflection
    from ._7367 import RollingRingAdvancedSystemDeflection
    from ._7368 import RollingRingAssemblyAdvancedSystemDeflection
    from ._7369 import RollingRingConnectionAdvancedSystemDeflection
    from ._7370 import RootAssemblyAdvancedSystemDeflection
    from ._7371 import ShaftAdvancedSystemDeflection
    from ._7372 import ShaftHubConnectionAdvancedSystemDeflection
    from ._7373 import ShaftToMountableComponentConnectionAdvancedSystemDeflection
    from ._7374 import SpecialisedAssemblyAdvancedSystemDeflection
    from ._7375 import SpiralBevelGearAdvancedSystemDeflection
    from ._7376 import SpiralBevelGearMeshAdvancedSystemDeflection
    from ._7377 import SpiralBevelGearSetAdvancedSystemDeflection
    from ._7378 import SpringDamperAdvancedSystemDeflection
    from ._7379 import SpringDamperConnectionAdvancedSystemDeflection
    from ._7380 import SpringDamperHalfAdvancedSystemDeflection
    from ._7381 import StraightBevelDiffGearAdvancedSystemDeflection
    from ._7382 import StraightBevelDiffGearMeshAdvancedSystemDeflection
    from ._7383 import StraightBevelDiffGearSetAdvancedSystemDeflection
    from ._7384 import StraightBevelGearAdvancedSystemDeflection
    from ._7385 import StraightBevelGearMeshAdvancedSystemDeflection
    from ._7386 import StraightBevelGearSetAdvancedSystemDeflection
    from ._7387 import StraightBevelPlanetGearAdvancedSystemDeflection
    from ._7388 import StraightBevelSunGearAdvancedSystemDeflection
    from ._7389 import SynchroniserAdvancedSystemDeflection
    from ._7390 import SynchroniserHalfAdvancedSystemDeflection
    from ._7391 import SynchroniserPartAdvancedSystemDeflection
    from ._7392 import SynchroniserSleeveAdvancedSystemDeflection
    from ._7393 import TorqueConverterAdvancedSystemDeflection
    from ._7394 import TorqueConverterConnectionAdvancedSystemDeflection
    from ._7395 import TorqueConverterPumpAdvancedSystemDeflection
    from ._7396 import TorqueConverterTurbineAdvancedSystemDeflection
    from ._7397 import TransmissionErrorToOtherPowerLoad
    from ._7398 import UnbalancedMassAdvancedSystemDeflection
    from ._7399 import VirtualComponentAdvancedSystemDeflection
    from ._7400 import WormGearAdvancedSystemDeflection
    from ._7401 import WormGearMeshAdvancedSystemDeflection
    from ._7402 import WormGearSetAdvancedSystemDeflection
    from ._7403 import ZerolBevelGearAdvancedSystemDeflection
    from ._7404 import ZerolBevelGearMeshAdvancedSystemDeflection
    from ._7405 import ZerolBevelGearSetAdvancedSystemDeflection
else:
    import_structure = {
        "_7270": ["AbstractAssemblyAdvancedSystemDeflection"],
        "_7271": ["AbstractShaftAdvancedSystemDeflection"],
        "_7272": ["AbstractShaftOrHousingAdvancedSystemDeflection"],
        "_7273": [
            "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
        ],
        "_7274": ["AdvancedSystemDeflection"],
        "_7275": ["AdvancedSystemDeflectionOptions"],
        "_7276": ["AdvancedSystemDeflectionSubAnalysis"],
        "_7277": ["AGMAGleasonConicalGearAdvancedSystemDeflection"],
        "_7278": ["AGMAGleasonConicalGearMeshAdvancedSystemDeflection"],
        "_7279": ["AGMAGleasonConicalGearSetAdvancedSystemDeflection"],
        "_7280": ["AssemblyAdvancedSystemDeflection"],
        "_7281": ["BearingAdvancedSystemDeflection"],
        "_7282": ["BeltConnectionAdvancedSystemDeflection"],
        "_7283": ["BeltDriveAdvancedSystemDeflection"],
        "_7284": ["BevelDifferentialGearAdvancedSystemDeflection"],
        "_7285": ["BevelDifferentialGearMeshAdvancedSystemDeflection"],
        "_7286": ["BevelDifferentialGearSetAdvancedSystemDeflection"],
        "_7287": ["BevelDifferentialPlanetGearAdvancedSystemDeflection"],
        "_7288": ["BevelDifferentialSunGearAdvancedSystemDeflection"],
        "_7289": ["BevelGearAdvancedSystemDeflection"],
        "_7290": ["BevelGearMeshAdvancedSystemDeflection"],
        "_7291": ["BevelGearSetAdvancedSystemDeflection"],
        "_7292": ["BoltAdvancedSystemDeflection"],
        "_7293": ["BoltedJointAdvancedSystemDeflection"],
        "_7294": ["ClutchAdvancedSystemDeflection"],
        "_7295": ["ClutchConnectionAdvancedSystemDeflection"],
        "_7296": ["ClutchHalfAdvancedSystemDeflection"],
        "_7297": ["CoaxialConnectionAdvancedSystemDeflection"],
        "_7298": ["ComponentAdvancedSystemDeflection"],
        "_7299": ["ConceptCouplingAdvancedSystemDeflection"],
        "_7300": ["ConceptCouplingConnectionAdvancedSystemDeflection"],
        "_7301": ["ConceptCouplingHalfAdvancedSystemDeflection"],
        "_7302": ["ConceptGearAdvancedSystemDeflection"],
        "_7303": ["ConceptGearMeshAdvancedSystemDeflection"],
        "_7304": ["ConceptGearSetAdvancedSystemDeflection"],
        "_7305": ["ConicalGearAdvancedSystemDeflection"],
        "_7306": ["ConicalGearMeshAdvancedSystemDeflection"],
        "_7307": ["ConicalGearSetAdvancedSystemDeflection"],
        "_7308": ["ConnectionAdvancedSystemDeflection"],
        "_7309": ["ConnectorAdvancedSystemDeflection"],
        "_7310": ["ContactChartPerToothPass"],
        "_7311": ["CouplingAdvancedSystemDeflection"],
        "_7312": ["CouplingConnectionAdvancedSystemDeflection"],
        "_7313": ["CouplingHalfAdvancedSystemDeflection"],
        "_7314": ["CVTAdvancedSystemDeflection"],
        "_7315": ["CVTBeltConnectionAdvancedSystemDeflection"],
        "_7316": ["CVTPulleyAdvancedSystemDeflection"],
        "_7317": ["CycloidalAssemblyAdvancedSystemDeflection"],
        "_7318": ["CycloidalDiscAdvancedSystemDeflection"],
        "_7319": ["CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"],
        "_7320": ["CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection"],
        "_7321": ["CylindricalGearAdvancedSystemDeflection"],
        "_7322": ["CylindricalGearMeshAdvancedSystemDeflection"],
        "_7323": ["CylindricalGearSetAdvancedSystemDeflection"],
        "_7324": ["CylindricalMeshedGearAdvancedSystemDeflection"],
        "_7325": ["CylindricalPlanetGearAdvancedSystemDeflection"],
        "_7326": ["DatumAdvancedSystemDeflection"],
        "_7327": ["ExternalCADModelAdvancedSystemDeflection"],
        "_7328": ["FaceGearAdvancedSystemDeflection"],
        "_7329": ["FaceGearMeshAdvancedSystemDeflection"],
        "_7330": ["FaceGearSetAdvancedSystemDeflection"],
        "_7331": ["FEPartAdvancedSystemDeflection"],
        "_7332": ["FlexiblePinAssemblyAdvancedSystemDeflection"],
        "_7333": ["GearAdvancedSystemDeflection"],
        "_7334": ["GearMeshAdvancedSystemDeflection"],
        "_7335": ["GearSetAdvancedSystemDeflection"],
        "_7336": ["GuideDxfModelAdvancedSystemDeflection"],
        "_7337": ["HypoidGearAdvancedSystemDeflection"],
        "_7338": ["HypoidGearMeshAdvancedSystemDeflection"],
        "_7339": ["HypoidGearSetAdvancedSystemDeflection"],
        "_7340": ["InterMountableComponentConnectionAdvancedSystemDeflection"],
        "_7341": ["KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection"],
        "_7342": ["KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection"],
        "_7343": ["KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"],
        "_7344": ["KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection"],
        "_7345": ["KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection"],
        "_7346": ["KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection"],
        "_7347": ["KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection"],
        "_7348": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ],
        "_7349": ["KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection"],
        "_7350": ["UseLtcaInAsdOption"],
        "_7351": ["MassDiscAdvancedSystemDeflection"],
        "_7352": ["MeasurementComponentAdvancedSystemDeflection"],
        "_7353": ["MountableComponentAdvancedSystemDeflection"],
        "_7354": ["OilSealAdvancedSystemDeflection"],
        "_7355": ["PartAdvancedSystemDeflection"],
        "_7356": ["PartToPartShearCouplingAdvancedSystemDeflection"],
        "_7357": ["PartToPartShearCouplingConnectionAdvancedSystemDeflection"],
        "_7358": ["PartToPartShearCouplingHalfAdvancedSystemDeflection"],
        "_7359": ["PlanetaryConnectionAdvancedSystemDeflection"],
        "_7360": ["PlanetaryGearSetAdvancedSystemDeflection"],
        "_7361": ["PlanetCarrierAdvancedSystemDeflection"],
        "_7362": ["PointLoadAdvancedSystemDeflection"],
        "_7363": ["PowerLoadAdvancedSystemDeflection"],
        "_7364": ["PulleyAdvancedSystemDeflection"],
        "_7365": ["RingPinsAdvancedSystemDeflection"],
        "_7366": ["RingPinsToDiscConnectionAdvancedSystemDeflection"],
        "_7367": ["RollingRingAdvancedSystemDeflection"],
        "_7368": ["RollingRingAssemblyAdvancedSystemDeflection"],
        "_7369": ["RollingRingConnectionAdvancedSystemDeflection"],
        "_7370": ["RootAssemblyAdvancedSystemDeflection"],
        "_7371": ["ShaftAdvancedSystemDeflection"],
        "_7372": ["ShaftHubConnectionAdvancedSystemDeflection"],
        "_7373": ["ShaftToMountableComponentConnectionAdvancedSystemDeflection"],
        "_7374": ["SpecialisedAssemblyAdvancedSystemDeflection"],
        "_7375": ["SpiralBevelGearAdvancedSystemDeflection"],
        "_7376": ["SpiralBevelGearMeshAdvancedSystemDeflection"],
        "_7377": ["SpiralBevelGearSetAdvancedSystemDeflection"],
        "_7378": ["SpringDamperAdvancedSystemDeflection"],
        "_7379": ["SpringDamperConnectionAdvancedSystemDeflection"],
        "_7380": ["SpringDamperHalfAdvancedSystemDeflection"],
        "_7381": ["StraightBevelDiffGearAdvancedSystemDeflection"],
        "_7382": ["StraightBevelDiffGearMeshAdvancedSystemDeflection"],
        "_7383": ["StraightBevelDiffGearSetAdvancedSystemDeflection"],
        "_7384": ["StraightBevelGearAdvancedSystemDeflection"],
        "_7385": ["StraightBevelGearMeshAdvancedSystemDeflection"],
        "_7386": ["StraightBevelGearSetAdvancedSystemDeflection"],
        "_7387": ["StraightBevelPlanetGearAdvancedSystemDeflection"],
        "_7388": ["StraightBevelSunGearAdvancedSystemDeflection"],
        "_7389": ["SynchroniserAdvancedSystemDeflection"],
        "_7390": ["SynchroniserHalfAdvancedSystemDeflection"],
        "_7391": ["SynchroniserPartAdvancedSystemDeflection"],
        "_7392": ["SynchroniserSleeveAdvancedSystemDeflection"],
        "_7393": ["TorqueConverterAdvancedSystemDeflection"],
        "_7394": ["TorqueConverterConnectionAdvancedSystemDeflection"],
        "_7395": ["TorqueConverterPumpAdvancedSystemDeflection"],
        "_7396": ["TorqueConverterTurbineAdvancedSystemDeflection"],
        "_7397": ["TransmissionErrorToOtherPowerLoad"],
        "_7398": ["UnbalancedMassAdvancedSystemDeflection"],
        "_7399": ["VirtualComponentAdvancedSystemDeflection"],
        "_7400": ["WormGearAdvancedSystemDeflection"],
        "_7401": ["WormGearMeshAdvancedSystemDeflection"],
        "_7402": ["WormGearSetAdvancedSystemDeflection"],
        "_7403": ["ZerolBevelGearAdvancedSystemDeflection"],
        "_7404": ["ZerolBevelGearMeshAdvancedSystemDeflection"],
        "_7405": ["ZerolBevelGearSetAdvancedSystemDeflection"],
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

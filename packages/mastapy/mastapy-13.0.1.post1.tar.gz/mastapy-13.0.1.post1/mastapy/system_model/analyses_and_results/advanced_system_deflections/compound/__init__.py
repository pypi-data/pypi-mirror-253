"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7406 import AbstractAssemblyCompoundAdvancedSystemDeflection
    from ._7407 import AbstractShaftCompoundAdvancedSystemDeflection
    from ._7408 import AbstractShaftOrHousingCompoundAdvancedSystemDeflection
    from ._7409 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7410 import AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
    from ._7411 import AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7412 import AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
    from ._7413 import AssemblyCompoundAdvancedSystemDeflection
    from ._7414 import BearingCompoundAdvancedSystemDeflection
    from ._7415 import BeltConnectionCompoundAdvancedSystemDeflection
    from ._7416 import BeltDriveCompoundAdvancedSystemDeflection
    from ._7417 import BevelDifferentialGearCompoundAdvancedSystemDeflection
    from ._7418 import BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
    from ._7419 import BevelDifferentialGearSetCompoundAdvancedSystemDeflection
    from ._7420 import BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
    from ._7421 import BevelDifferentialSunGearCompoundAdvancedSystemDeflection
    from ._7422 import BevelGearCompoundAdvancedSystemDeflection
    from ._7423 import BevelGearMeshCompoundAdvancedSystemDeflection
    from ._7424 import BevelGearSetCompoundAdvancedSystemDeflection
    from ._7425 import BoltCompoundAdvancedSystemDeflection
    from ._7426 import BoltedJointCompoundAdvancedSystemDeflection
    from ._7427 import ClutchCompoundAdvancedSystemDeflection
    from ._7428 import ClutchConnectionCompoundAdvancedSystemDeflection
    from ._7429 import ClutchHalfCompoundAdvancedSystemDeflection
    from ._7430 import CoaxialConnectionCompoundAdvancedSystemDeflection
    from ._7431 import ComponentCompoundAdvancedSystemDeflection
    from ._7432 import ConceptCouplingCompoundAdvancedSystemDeflection
    from ._7433 import ConceptCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7434 import ConceptCouplingHalfCompoundAdvancedSystemDeflection
    from ._7435 import ConceptGearCompoundAdvancedSystemDeflection
    from ._7436 import ConceptGearMeshCompoundAdvancedSystemDeflection
    from ._7437 import ConceptGearSetCompoundAdvancedSystemDeflection
    from ._7438 import ConicalGearCompoundAdvancedSystemDeflection
    from ._7439 import ConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7440 import ConicalGearSetCompoundAdvancedSystemDeflection
    from ._7441 import ConnectionCompoundAdvancedSystemDeflection
    from ._7442 import ConnectorCompoundAdvancedSystemDeflection
    from ._7443 import CouplingCompoundAdvancedSystemDeflection
    from ._7444 import CouplingConnectionCompoundAdvancedSystemDeflection
    from ._7445 import CouplingHalfCompoundAdvancedSystemDeflection
    from ._7446 import CVTBeltConnectionCompoundAdvancedSystemDeflection
    from ._7447 import CVTCompoundAdvancedSystemDeflection
    from ._7448 import CVTPulleyCompoundAdvancedSystemDeflection
    from ._7449 import CycloidalAssemblyCompoundAdvancedSystemDeflection
    from ._7450 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7451 import CycloidalDiscCompoundAdvancedSystemDeflection
    from ._7452 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7453 import CylindricalGearCompoundAdvancedSystemDeflection
    from ._7454 import CylindricalGearMeshCompoundAdvancedSystemDeflection
    from ._7455 import CylindricalGearSetCompoundAdvancedSystemDeflection
    from ._7456 import CylindricalPlanetGearCompoundAdvancedSystemDeflection
    from ._7457 import DatumCompoundAdvancedSystemDeflection
    from ._7458 import ExternalCADModelCompoundAdvancedSystemDeflection
    from ._7459 import FaceGearCompoundAdvancedSystemDeflection
    from ._7460 import FaceGearMeshCompoundAdvancedSystemDeflection
    from ._7461 import FaceGearSetCompoundAdvancedSystemDeflection
    from ._7462 import FEPartCompoundAdvancedSystemDeflection
    from ._7463 import FlexiblePinAssemblyCompoundAdvancedSystemDeflection
    from ._7464 import GearCompoundAdvancedSystemDeflection
    from ._7465 import GearMeshCompoundAdvancedSystemDeflection
    from ._7466 import GearSetCompoundAdvancedSystemDeflection
    from ._7467 import GuideDxfModelCompoundAdvancedSystemDeflection
    from ._7468 import HypoidGearCompoundAdvancedSystemDeflection
    from ._7469 import HypoidGearMeshCompoundAdvancedSystemDeflection
    from ._7470 import HypoidGearSetCompoundAdvancedSystemDeflection
    from ._7471 import InterMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7472 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection,
    )
    from ._7473 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7474 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7475 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection,
    )
    from ._7476 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7477 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7478 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection,
    )
    from ._7479 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7480 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7481 import MassDiscCompoundAdvancedSystemDeflection
    from ._7482 import MeasurementComponentCompoundAdvancedSystemDeflection
    from ._7483 import MountableComponentCompoundAdvancedSystemDeflection
    from ._7484 import OilSealCompoundAdvancedSystemDeflection
    from ._7485 import PartCompoundAdvancedSystemDeflection
    from ._7486 import PartToPartShearCouplingCompoundAdvancedSystemDeflection
    from ._7487 import PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7488 import PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
    from ._7489 import PlanetaryConnectionCompoundAdvancedSystemDeflection
    from ._7490 import PlanetaryGearSetCompoundAdvancedSystemDeflection
    from ._7491 import PlanetCarrierCompoundAdvancedSystemDeflection
    from ._7492 import PointLoadCompoundAdvancedSystemDeflection
    from ._7493 import PowerLoadCompoundAdvancedSystemDeflection
    from ._7494 import PulleyCompoundAdvancedSystemDeflection
    from ._7495 import RingPinsCompoundAdvancedSystemDeflection
    from ._7496 import RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
    from ._7497 import RollingRingAssemblyCompoundAdvancedSystemDeflection
    from ._7498 import RollingRingCompoundAdvancedSystemDeflection
    from ._7499 import RollingRingConnectionCompoundAdvancedSystemDeflection
    from ._7500 import RootAssemblyCompoundAdvancedSystemDeflection
    from ._7501 import ShaftCompoundAdvancedSystemDeflection
    from ._7502 import ShaftHubConnectionCompoundAdvancedSystemDeflection
    from ._7503 import (
        ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7504 import SpecialisedAssemblyCompoundAdvancedSystemDeflection
    from ._7505 import SpiralBevelGearCompoundAdvancedSystemDeflection
    from ._7506 import SpiralBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7507 import SpiralBevelGearSetCompoundAdvancedSystemDeflection
    from ._7508 import SpringDamperCompoundAdvancedSystemDeflection
    from ._7509 import SpringDamperConnectionCompoundAdvancedSystemDeflection
    from ._7510 import SpringDamperHalfCompoundAdvancedSystemDeflection
    from ._7511 import StraightBevelDiffGearCompoundAdvancedSystemDeflection
    from ._7512 import StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
    from ._7513 import StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
    from ._7514 import StraightBevelGearCompoundAdvancedSystemDeflection
    from ._7515 import StraightBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7516 import StraightBevelGearSetCompoundAdvancedSystemDeflection
    from ._7517 import StraightBevelPlanetGearCompoundAdvancedSystemDeflection
    from ._7518 import StraightBevelSunGearCompoundAdvancedSystemDeflection
    from ._7519 import SynchroniserCompoundAdvancedSystemDeflection
    from ._7520 import SynchroniserHalfCompoundAdvancedSystemDeflection
    from ._7521 import SynchroniserPartCompoundAdvancedSystemDeflection
    from ._7522 import SynchroniserSleeveCompoundAdvancedSystemDeflection
    from ._7523 import TorqueConverterCompoundAdvancedSystemDeflection
    from ._7524 import TorqueConverterConnectionCompoundAdvancedSystemDeflection
    from ._7525 import TorqueConverterPumpCompoundAdvancedSystemDeflection
    from ._7526 import TorqueConverterTurbineCompoundAdvancedSystemDeflection
    from ._7527 import UnbalancedMassCompoundAdvancedSystemDeflection
    from ._7528 import VirtualComponentCompoundAdvancedSystemDeflection
    from ._7529 import WormGearCompoundAdvancedSystemDeflection
    from ._7530 import WormGearMeshCompoundAdvancedSystemDeflection
    from ._7531 import WormGearSetCompoundAdvancedSystemDeflection
    from ._7532 import ZerolBevelGearCompoundAdvancedSystemDeflection
    from ._7533 import ZerolBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7534 import ZerolBevelGearSetCompoundAdvancedSystemDeflection
else:
    import_structure = {
        "_7406": ["AbstractAssemblyCompoundAdvancedSystemDeflection"],
        "_7407": ["AbstractShaftCompoundAdvancedSystemDeflection"],
        "_7408": ["AbstractShaftOrHousingCompoundAdvancedSystemDeflection"],
        "_7409": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7410": ["AGMAGleasonConicalGearCompoundAdvancedSystemDeflection"],
        "_7411": ["AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7412": ["AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7413": ["AssemblyCompoundAdvancedSystemDeflection"],
        "_7414": ["BearingCompoundAdvancedSystemDeflection"],
        "_7415": ["BeltConnectionCompoundAdvancedSystemDeflection"],
        "_7416": ["BeltDriveCompoundAdvancedSystemDeflection"],
        "_7417": ["BevelDifferentialGearCompoundAdvancedSystemDeflection"],
        "_7418": ["BevelDifferentialGearMeshCompoundAdvancedSystemDeflection"],
        "_7419": ["BevelDifferentialGearSetCompoundAdvancedSystemDeflection"],
        "_7420": ["BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection"],
        "_7421": ["BevelDifferentialSunGearCompoundAdvancedSystemDeflection"],
        "_7422": ["BevelGearCompoundAdvancedSystemDeflection"],
        "_7423": ["BevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7424": ["BevelGearSetCompoundAdvancedSystemDeflection"],
        "_7425": ["BoltCompoundAdvancedSystemDeflection"],
        "_7426": ["BoltedJointCompoundAdvancedSystemDeflection"],
        "_7427": ["ClutchCompoundAdvancedSystemDeflection"],
        "_7428": ["ClutchConnectionCompoundAdvancedSystemDeflection"],
        "_7429": ["ClutchHalfCompoundAdvancedSystemDeflection"],
        "_7430": ["CoaxialConnectionCompoundAdvancedSystemDeflection"],
        "_7431": ["ComponentCompoundAdvancedSystemDeflection"],
        "_7432": ["ConceptCouplingCompoundAdvancedSystemDeflection"],
        "_7433": ["ConceptCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7434": ["ConceptCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7435": ["ConceptGearCompoundAdvancedSystemDeflection"],
        "_7436": ["ConceptGearMeshCompoundAdvancedSystemDeflection"],
        "_7437": ["ConceptGearSetCompoundAdvancedSystemDeflection"],
        "_7438": ["ConicalGearCompoundAdvancedSystemDeflection"],
        "_7439": ["ConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7440": ["ConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7441": ["ConnectionCompoundAdvancedSystemDeflection"],
        "_7442": ["ConnectorCompoundAdvancedSystemDeflection"],
        "_7443": ["CouplingCompoundAdvancedSystemDeflection"],
        "_7444": ["CouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7445": ["CouplingHalfCompoundAdvancedSystemDeflection"],
        "_7446": ["CVTBeltConnectionCompoundAdvancedSystemDeflection"],
        "_7447": ["CVTCompoundAdvancedSystemDeflection"],
        "_7448": ["CVTPulleyCompoundAdvancedSystemDeflection"],
        "_7449": ["CycloidalAssemblyCompoundAdvancedSystemDeflection"],
        "_7450": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7451": ["CycloidalDiscCompoundAdvancedSystemDeflection"],
        "_7452": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7453": ["CylindricalGearCompoundAdvancedSystemDeflection"],
        "_7454": ["CylindricalGearMeshCompoundAdvancedSystemDeflection"],
        "_7455": ["CylindricalGearSetCompoundAdvancedSystemDeflection"],
        "_7456": ["CylindricalPlanetGearCompoundAdvancedSystemDeflection"],
        "_7457": ["DatumCompoundAdvancedSystemDeflection"],
        "_7458": ["ExternalCADModelCompoundAdvancedSystemDeflection"],
        "_7459": ["FaceGearCompoundAdvancedSystemDeflection"],
        "_7460": ["FaceGearMeshCompoundAdvancedSystemDeflection"],
        "_7461": ["FaceGearSetCompoundAdvancedSystemDeflection"],
        "_7462": ["FEPartCompoundAdvancedSystemDeflection"],
        "_7463": ["FlexiblePinAssemblyCompoundAdvancedSystemDeflection"],
        "_7464": ["GearCompoundAdvancedSystemDeflection"],
        "_7465": ["GearMeshCompoundAdvancedSystemDeflection"],
        "_7466": ["GearSetCompoundAdvancedSystemDeflection"],
        "_7467": ["GuideDxfModelCompoundAdvancedSystemDeflection"],
        "_7468": ["HypoidGearCompoundAdvancedSystemDeflection"],
        "_7469": ["HypoidGearMeshCompoundAdvancedSystemDeflection"],
        "_7470": ["HypoidGearSetCompoundAdvancedSystemDeflection"],
        "_7471": ["InterMountableComponentConnectionCompoundAdvancedSystemDeflection"],
        "_7472": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ],
        "_7473": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7474": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7475": ["KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection"],
        "_7476": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7477": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7478": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
        ],
        "_7479": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7480": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7481": ["MassDiscCompoundAdvancedSystemDeflection"],
        "_7482": ["MeasurementComponentCompoundAdvancedSystemDeflection"],
        "_7483": ["MountableComponentCompoundAdvancedSystemDeflection"],
        "_7484": ["OilSealCompoundAdvancedSystemDeflection"],
        "_7485": ["PartCompoundAdvancedSystemDeflection"],
        "_7486": ["PartToPartShearCouplingCompoundAdvancedSystemDeflection"],
        "_7487": ["PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7488": ["PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7489": ["PlanetaryConnectionCompoundAdvancedSystemDeflection"],
        "_7490": ["PlanetaryGearSetCompoundAdvancedSystemDeflection"],
        "_7491": ["PlanetCarrierCompoundAdvancedSystemDeflection"],
        "_7492": ["PointLoadCompoundAdvancedSystemDeflection"],
        "_7493": ["PowerLoadCompoundAdvancedSystemDeflection"],
        "_7494": ["PulleyCompoundAdvancedSystemDeflection"],
        "_7495": ["RingPinsCompoundAdvancedSystemDeflection"],
        "_7496": ["RingPinsToDiscConnectionCompoundAdvancedSystemDeflection"],
        "_7497": ["RollingRingAssemblyCompoundAdvancedSystemDeflection"],
        "_7498": ["RollingRingCompoundAdvancedSystemDeflection"],
        "_7499": ["RollingRingConnectionCompoundAdvancedSystemDeflection"],
        "_7500": ["RootAssemblyCompoundAdvancedSystemDeflection"],
        "_7501": ["ShaftCompoundAdvancedSystemDeflection"],
        "_7502": ["ShaftHubConnectionCompoundAdvancedSystemDeflection"],
        "_7503": [
            "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7504": ["SpecialisedAssemblyCompoundAdvancedSystemDeflection"],
        "_7505": ["SpiralBevelGearCompoundAdvancedSystemDeflection"],
        "_7506": ["SpiralBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7507": ["SpiralBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7508": ["SpringDamperCompoundAdvancedSystemDeflection"],
        "_7509": ["SpringDamperConnectionCompoundAdvancedSystemDeflection"],
        "_7510": ["SpringDamperHalfCompoundAdvancedSystemDeflection"],
        "_7511": ["StraightBevelDiffGearCompoundAdvancedSystemDeflection"],
        "_7512": ["StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection"],
        "_7513": ["StraightBevelDiffGearSetCompoundAdvancedSystemDeflection"],
        "_7514": ["StraightBevelGearCompoundAdvancedSystemDeflection"],
        "_7515": ["StraightBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7516": ["StraightBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7517": ["StraightBevelPlanetGearCompoundAdvancedSystemDeflection"],
        "_7518": ["StraightBevelSunGearCompoundAdvancedSystemDeflection"],
        "_7519": ["SynchroniserCompoundAdvancedSystemDeflection"],
        "_7520": ["SynchroniserHalfCompoundAdvancedSystemDeflection"],
        "_7521": ["SynchroniserPartCompoundAdvancedSystemDeflection"],
        "_7522": ["SynchroniserSleeveCompoundAdvancedSystemDeflection"],
        "_7523": ["TorqueConverterCompoundAdvancedSystemDeflection"],
        "_7524": ["TorqueConverterConnectionCompoundAdvancedSystemDeflection"],
        "_7525": ["TorqueConverterPumpCompoundAdvancedSystemDeflection"],
        "_7526": ["TorqueConverterTurbineCompoundAdvancedSystemDeflection"],
        "_7527": ["UnbalancedMassCompoundAdvancedSystemDeflection"],
        "_7528": ["VirtualComponentCompoundAdvancedSystemDeflection"],
        "_7529": ["WormGearCompoundAdvancedSystemDeflection"],
        "_7530": ["WormGearMeshCompoundAdvancedSystemDeflection"],
        "_7531": ["WormGearSetCompoundAdvancedSystemDeflection"],
        "_7532": ["ZerolBevelGearCompoundAdvancedSystemDeflection"],
        "_7533": ["ZerolBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7534": ["ZerolBevelGearSetCompoundAdvancedSystemDeflection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundAdvancedSystemDeflection",
    "AbstractShaftCompoundAdvancedSystemDeflection",
    "AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    "AssemblyCompoundAdvancedSystemDeflection",
    "BearingCompoundAdvancedSystemDeflection",
    "BeltConnectionCompoundAdvancedSystemDeflection",
    "BeltDriveCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearMeshCompoundAdvancedSystemDeflection",
    "BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
    "BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection",
    "BevelDifferentialSunGearCompoundAdvancedSystemDeflection",
    "BevelGearCompoundAdvancedSystemDeflection",
    "BevelGearMeshCompoundAdvancedSystemDeflection",
    "BevelGearSetCompoundAdvancedSystemDeflection",
    "BoltCompoundAdvancedSystemDeflection",
    "BoltedJointCompoundAdvancedSystemDeflection",
    "ClutchCompoundAdvancedSystemDeflection",
    "ClutchConnectionCompoundAdvancedSystemDeflection",
    "ClutchHalfCompoundAdvancedSystemDeflection",
    "CoaxialConnectionCompoundAdvancedSystemDeflection",
    "ComponentCompoundAdvancedSystemDeflection",
    "ConceptCouplingCompoundAdvancedSystemDeflection",
    "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
    "ConceptCouplingHalfCompoundAdvancedSystemDeflection",
    "ConceptGearCompoundAdvancedSystemDeflection",
    "ConceptGearMeshCompoundAdvancedSystemDeflection",
    "ConceptGearSetCompoundAdvancedSystemDeflection",
    "ConicalGearCompoundAdvancedSystemDeflection",
    "ConicalGearMeshCompoundAdvancedSystemDeflection",
    "ConicalGearSetCompoundAdvancedSystemDeflection",
    "ConnectionCompoundAdvancedSystemDeflection",
    "ConnectorCompoundAdvancedSystemDeflection",
    "CouplingCompoundAdvancedSystemDeflection",
    "CouplingConnectionCompoundAdvancedSystemDeflection",
    "CouplingHalfCompoundAdvancedSystemDeflection",
    "CVTBeltConnectionCompoundAdvancedSystemDeflection",
    "CVTCompoundAdvancedSystemDeflection",
    "CVTPulleyCompoundAdvancedSystemDeflection",
    "CycloidalAssemblyCompoundAdvancedSystemDeflection",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
    "CycloidalDiscCompoundAdvancedSystemDeflection",
    "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection",
    "CylindricalGearCompoundAdvancedSystemDeflection",
    "CylindricalGearMeshCompoundAdvancedSystemDeflection",
    "CylindricalGearSetCompoundAdvancedSystemDeflection",
    "CylindricalPlanetGearCompoundAdvancedSystemDeflection",
    "DatumCompoundAdvancedSystemDeflection",
    "ExternalCADModelCompoundAdvancedSystemDeflection",
    "FaceGearCompoundAdvancedSystemDeflection",
    "FaceGearMeshCompoundAdvancedSystemDeflection",
    "FaceGearSetCompoundAdvancedSystemDeflection",
    "FEPartCompoundAdvancedSystemDeflection",
    "FlexiblePinAssemblyCompoundAdvancedSystemDeflection",
    "GearCompoundAdvancedSystemDeflection",
    "GearMeshCompoundAdvancedSystemDeflection",
    "GearSetCompoundAdvancedSystemDeflection",
    "GuideDxfModelCompoundAdvancedSystemDeflection",
    "HypoidGearCompoundAdvancedSystemDeflection",
    "HypoidGearMeshCompoundAdvancedSystemDeflection",
    "HypoidGearSetCompoundAdvancedSystemDeflection",
    "InterMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "MassDiscCompoundAdvancedSystemDeflection",
    "MeasurementComponentCompoundAdvancedSystemDeflection",
    "MountableComponentCompoundAdvancedSystemDeflection",
    "OilSealCompoundAdvancedSystemDeflection",
    "PartCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection",
    "PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection",
    "PlanetaryConnectionCompoundAdvancedSystemDeflection",
    "PlanetaryGearSetCompoundAdvancedSystemDeflection",
    "PlanetCarrierCompoundAdvancedSystemDeflection",
    "PointLoadCompoundAdvancedSystemDeflection",
    "PowerLoadCompoundAdvancedSystemDeflection",
    "PulleyCompoundAdvancedSystemDeflection",
    "RingPinsCompoundAdvancedSystemDeflection",
    "RingPinsToDiscConnectionCompoundAdvancedSystemDeflection",
    "RollingRingAssemblyCompoundAdvancedSystemDeflection",
    "RollingRingCompoundAdvancedSystemDeflection",
    "RollingRingConnectionCompoundAdvancedSystemDeflection",
    "RootAssemblyCompoundAdvancedSystemDeflection",
    "ShaftCompoundAdvancedSystemDeflection",
    "ShaftHubConnectionCompoundAdvancedSystemDeflection",
    "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
    "SpiralBevelGearCompoundAdvancedSystemDeflection",
    "SpiralBevelGearMeshCompoundAdvancedSystemDeflection",
    "SpiralBevelGearSetCompoundAdvancedSystemDeflection",
    "SpringDamperCompoundAdvancedSystemDeflection",
    "SpringDamperConnectionCompoundAdvancedSystemDeflection",
    "SpringDamperHalfCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelDiffGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelGearCompoundAdvancedSystemDeflection",
    "StraightBevelGearMeshCompoundAdvancedSystemDeflection",
    "StraightBevelGearSetCompoundAdvancedSystemDeflection",
    "StraightBevelPlanetGearCompoundAdvancedSystemDeflection",
    "StraightBevelSunGearCompoundAdvancedSystemDeflection",
    "SynchroniserCompoundAdvancedSystemDeflection",
    "SynchroniserHalfCompoundAdvancedSystemDeflection",
    "SynchroniserPartCompoundAdvancedSystemDeflection",
    "SynchroniserSleeveCompoundAdvancedSystemDeflection",
    "TorqueConverterCompoundAdvancedSystemDeflection",
    "TorqueConverterConnectionCompoundAdvancedSystemDeflection",
    "TorqueConverterPumpCompoundAdvancedSystemDeflection",
    "TorqueConverterTurbineCompoundAdvancedSystemDeflection",
    "UnbalancedMassCompoundAdvancedSystemDeflection",
    "VirtualComponentCompoundAdvancedSystemDeflection",
    "WormGearCompoundAdvancedSystemDeflection",
    "WormGearMeshCompoundAdvancedSystemDeflection",
    "WormGearSetCompoundAdvancedSystemDeflection",
    "ZerolBevelGearCompoundAdvancedSystemDeflection",
    "ZerolBevelGearMeshCompoundAdvancedSystemDeflection",
    "ZerolBevelGearSetCompoundAdvancedSystemDeflection",
)

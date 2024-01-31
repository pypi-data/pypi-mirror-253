"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._7405 import AbstractAssemblyCompoundAdvancedSystemDeflection
    from ._7406 import AbstractShaftCompoundAdvancedSystemDeflection
    from ._7407 import AbstractShaftOrHousingCompoundAdvancedSystemDeflection
    from ._7408 import (
        AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7409 import AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
    from ._7410 import AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7411 import AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
    from ._7412 import AssemblyCompoundAdvancedSystemDeflection
    from ._7413 import BearingCompoundAdvancedSystemDeflection
    from ._7414 import BeltConnectionCompoundAdvancedSystemDeflection
    from ._7415 import BeltDriveCompoundAdvancedSystemDeflection
    from ._7416 import BevelDifferentialGearCompoundAdvancedSystemDeflection
    from ._7417 import BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
    from ._7418 import BevelDifferentialGearSetCompoundAdvancedSystemDeflection
    from ._7419 import BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
    from ._7420 import BevelDifferentialSunGearCompoundAdvancedSystemDeflection
    from ._7421 import BevelGearCompoundAdvancedSystemDeflection
    from ._7422 import BevelGearMeshCompoundAdvancedSystemDeflection
    from ._7423 import BevelGearSetCompoundAdvancedSystemDeflection
    from ._7424 import BoltCompoundAdvancedSystemDeflection
    from ._7425 import BoltedJointCompoundAdvancedSystemDeflection
    from ._7426 import ClutchCompoundAdvancedSystemDeflection
    from ._7427 import ClutchConnectionCompoundAdvancedSystemDeflection
    from ._7428 import ClutchHalfCompoundAdvancedSystemDeflection
    from ._7429 import CoaxialConnectionCompoundAdvancedSystemDeflection
    from ._7430 import ComponentCompoundAdvancedSystemDeflection
    from ._7431 import ConceptCouplingCompoundAdvancedSystemDeflection
    from ._7432 import ConceptCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7433 import ConceptCouplingHalfCompoundAdvancedSystemDeflection
    from ._7434 import ConceptGearCompoundAdvancedSystemDeflection
    from ._7435 import ConceptGearMeshCompoundAdvancedSystemDeflection
    from ._7436 import ConceptGearSetCompoundAdvancedSystemDeflection
    from ._7437 import ConicalGearCompoundAdvancedSystemDeflection
    from ._7438 import ConicalGearMeshCompoundAdvancedSystemDeflection
    from ._7439 import ConicalGearSetCompoundAdvancedSystemDeflection
    from ._7440 import ConnectionCompoundAdvancedSystemDeflection
    from ._7441 import ConnectorCompoundAdvancedSystemDeflection
    from ._7442 import CouplingCompoundAdvancedSystemDeflection
    from ._7443 import CouplingConnectionCompoundAdvancedSystemDeflection
    from ._7444 import CouplingHalfCompoundAdvancedSystemDeflection
    from ._7445 import CVTBeltConnectionCompoundAdvancedSystemDeflection
    from ._7446 import CVTCompoundAdvancedSystemDeflection
    from ._7447 import CVTPulleyCompoundAdvancedSystemDeflection
    from ._7448 import CycloidalAssemblyCompoundAdvancedSystemDeflection
    from ._7449 import (
        CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7450 import CycloidalDiscCompoundAdvancedSystemDeflection
    from ._7451 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7452 import CylindricalGearCompoundAdvancedSystemDeflection
    from ._7453 import CylindricalGearMeshCompoundAdvancedSystemDeflection
    from ._7454 import CylindricalGearSetCompoundAdvancedSystemDeflection
    from ._7455 import CylindricalPlanetGearCompoundAdvancedSystemDeflection
    from ._7456 import DatumCompoundAdvancedSystemDeflection
    from ._7457 import ExternalCADModelCompoundAdvancedSystemDeflection
    from ._7458 import FaceGearCompoundAdvancedSystemDeflection
    from ._7459 import FaceGearMeshCompoundAdvancedSystemDeflection
    from ._7460 import FaceGearSetCompoundAdvancedSystemDeflection
    from ._7461 import FEPartCompoundAdvancedSystemDeflection
    from ._7462 import FlexiblePinAssemblyCompoundAdvancedSystemDeflection
    from ._7463 import GearCompoundAdvancedSystemDeflection
    from ._7464 import GearMeshCompoundAdvancedSystemDeflection
    from ._7465 import GearSetCompoundAdvancedSystemDeflection
    from ._7466 import GuideDxfModelCompoundAdvancedSystemDeflection
    from ._7467 import HypoidGearCompoundAdvancedSystemDeflection
    from ._7468 import HypoidGearMeshCompoundAdvancedSystemDeflection
    from ._7469 import HypoidGearSetCompoundAdvancedSystemDeflection
    from ._7470 import InterMountableComponentConnectionCompoundAdvancedSystemDeflection
    from ._7471 import (
        KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection,
    )
    from ._7472 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7473 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7474 import (
        KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection,
    )
    from ._7475 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7476 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7477 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection,
    )
    from ._7478 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection,
    )
    from ._7479 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection,
    )
    from ._7480 import MassDiscCompoundAdvancedSystemDeflection
    from ._7481 import MeasurementComponentCompoundAdvancedSystemDeflection
    from ._7482 import MountableComponentCompoundAdvancedSystemDeflection
    from ._7483 import OilSealCompoundAdvancedSystemDeflection
    from ._7484 import PartCompoundAdvancedSystemDeflection
    from ._7485 import PartToPartShearCouplingCompoundAdvancedSystemDeflection
    from ._7486 import PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
    from ._7487 import PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
    from ._7488 import PlanetaryConnectionCompoundAdvancedSystemDeflection
    from ._7489 import PlanetaryGearSetCompoundAdvancedSystemDeflection
    from ._7490 import PlanetCarrierCompoundAdvancedSystemDeflection
    from ._7491 import PointLoadCompoundAdvancedSystemDeflection
    from ._7492 import PowerLoadCompoundAdvancedSystemDeflection
    from ._7493 import PulleyCompoundAdvancedSystemDeflection
    from ._7494 import RingPinsCompoundAdvancedSystemDeflection
    from ._7495 import RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
    from ._7496 import RollingRingAssemblyCompoundAdvancedSystemDeflection
    from ._7497 import RollingRingCompoundAdvancedSystemDeflection
    from ._7498 import RollingRingConnectionCompoundAdvancedSystemDeflection
    from ._7499 import RootAssemblyCompoundAdvancedSystemDeflection
    from ._7500 import ShaftCompoundAdvancedSystemDeflection
    from ._7501 import ShaftHubConnectionCompoundAdvancedSystemDeflection
    from ._7502 import (
        ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection,
    )
    from ._7503 import SpecialisedAssemblyCompoundAdvancedSystemDeflection
    from ._7504 import SpiralBevelGearCompoundAdvancedSystemDeflection
    from ._7505 import SpiralBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7506 import SpiralBevelGearSetCompoundAdvancedSystemDeflection
    from ._7507 import SpringDamperCompoundAdvancedSystemDeflection
    from ._7508 import SpringDamperConnectionCompoundAdvancedSystemDeflection
    from ._7509 import SpringDamperHalfCompoundAdvancedSystemDeflection
    from ._7510 import StraightBevelDiffGearCompoundAdvancedSystemDeflection
    from ._7511 import StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
    from ._7512 import StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
    from ._7513 import StraightBevelGearCompoundAdvancedSystemDeflection
    from ._7514 import StraightBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7515 import StraightBevelGearSetCompoundAdvancedSystemDeflection
    from ._7516 import StraightBevelPlanetGearCompoundAdvancedSystemDeflection
    from ._7517 import StraightBevelSunGearCompoundAdvancedSystemDeflection
    from ._7518 import SynchroniserCompoundAdvancedSystemDeflection
    from ._7519 import SynchroniserHalfCompoundAdvancedSystemDeflection
    from ._7520 import SynchroniserPartCompoundAdvancedSystemDeflection
    from ._7521 import SynchroniserSleeveCompoundAdvancedSystemDeflection
    from ._7522 import TorqueConverterCompoundAdvancedSystemDeflection
    from ._7523 import TorqueConverterConnectionCompoundAdvancedSystemDeflection
    from ._7524 import TorqueConverterPumpCompoundAdvancedSystemDeflection
    from ._7525 import TorqueConverterTurbineCompoundAdvancedSystemDeflection
    from ._7526 import UnbalancedMassCompoundAdvancedSystemDeflection
    from ._7527 import VirtualComponentCompoundAdvancedSystemDeflection
    from ._7528 import WormGearCompoundAdvancedSystemDeflection
    from ._7529 import WormGearMeshCompoundAdvancedSystemDeflection
    from ._7530 import WormGearSetCompoundAdvancedSystemDeflection
    from ._7531 import ZerolBevelGearCompoundAdvancedSystemDeflection
    from ._7532 import ZerolBevelGearMeshCompoundAdvancedSystemDeflection
    from ._7533 import ZerolBevelGearSetCompoundAdvancedSystemDeflection
else:
    import_structure = {
        "_7405": ["AbstractAssemblyCompoundAdvancedSystemDeflection"],
        "_7406": ["AbstractShaftCompoundAdvancedSystemDeflection"],
        "_7407": ["AbstractShaftOrHousingCompoundAdvancedSystemDeflection"],
        "_7408": [
            "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7409": ["AGMAGleasonConicalGearCompoundAdvancedSystemDeflection"],
        "_7410": ["AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7411": ["AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7412": ["AssemblyCompoundAdvancedSystemDeflection"],
        "_7413": ["BearingCompoundAdvancedSystemDeflection"],
        "_7414": ["BeltConnectionCompoundAdvancedSystemDeflection"],
        "_7415": ["BeltDriveCompoundAdvancedSystemDeflection"],
        "_7416": ["BevelDifferentialGearCompoundAdvancedSystemDeflection"],
        "_7417": ["BevelDifferentialGearMeshCompoundAdvancedSystemDeflection"],
        "_7418": ["BevelDifferentialGearSetCompoundAdvancedSystemDeflection"],
        "_7419": ["BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection"],
        "_7420": ["BevelDifferentialSunGearCompoundAdvancedSystemDeflection"],
        "_7421": ["BevelGearCompoundAdvancedSystemDeflection"],
        "_7422": ["BevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7423": ["BevelGearSetCompoundAdvancedSystemDeflection"],
        "_7424": ["BoltCompoundAdvancedSystemDeflection"],
        "_7425": ["BoltedJointCompoundAdvancedSystemDeflection"],
        "_7426": ["ClutchCompoundAdvancedSystemDeflection"],
        "_7427": ["ClutchConnectionCompoundAdvancedSystemDeflection"],
        "_7428": ["ClutchHalfCompoundAdvancedSystemDeflection"],
        "_7429": ["CoaxialConnectionCompoundAdvancedSystemDeflection"],
        "_7430": ["ComponentCompoundAdvancedSystemDeflection"],
        "_7431": ["ConceptCouplingCompoundAdvancedSystemDeflection"],
        "_7432": ["ConceptCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7433": ["ConceptCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7434": ["ConceptGearCompoundAdvancedSystemDeflection"],
        "_7435": ["ConceptGearMeshCompoundAdvancedSystemDeflection"],
        "_7436": ["ConceptGearSetCompoundAdvancedSystemDeflection"],
        "_7437": ["ConicalGearCompoundAdvancedSystemDeflection"],
        "_7438": ["ConicalGearMeshCompoundAdvancedSystemDeflection"],
        "_7439": ["ConicalGearSetCompoundAdvancedSystemDeflection"],
        "_7440": ["ConnectionCompoundAdvancedSystemDeflection"],
        "_7441": ["ConnectorCompoundAdvancedSystemDeflection"],
        "_7442": ["CouplingCompoundAdvancedSystemDeflection"],
        "_7443": ["CouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7444": ["CouplingHalfCompoundAdvancedSystemDeflection"],
        "_7445": ["CVTBeltConnectionCompoundAdvancedSystemDeflection"],
        "_7446": ["CVTCompoundAdvancedSystemDeflection"],
        "_7447": ["CVTPulleyCompoundAdvancedSystemDeflection"],
        "_7448": ["CycloidalAssemblyCompoundAdvancedSystemDeflection"],
        "_7449": [
            "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7450": ["CycloidalDiscCompoundAdvancedSystemDeflection"],
        "_7451": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7452": ["CylindricalGearCompoundAdvancedSystemDeflection"],
        "_7453": ["CylindricalGearMeshCompoundAdvancedSystemDeflection"],
        "_7454": ["CylindricalGearSetCompoundAdvancedSystemDeflection"],
        "_7455": ["CylindricalPlanetGearCompoundAdvancedSystemDeflection"],
        "_7456": ["DatumCompoundAdvancedSystemDeflection"],
        "_7457": ["ExternalCADModelCompoundAdvancedSystemDeflection"],
        "_7458": ["FaceGearCompoundAdvancedSystemDeflection"],
        "_7459": ["FaceGearMeshCompoundAdvancedSystemDeflection"],
        "_7460": ["FaceGearSetCompoundAdvancedSystemDeflection"],
        "_7461": ["FEPartCompoundAdvancedSystemDeflection"],
        "_7462": ["FlexiblePinAssemblyCompoundAdvancedSystemDeflection"],
        "_7463": ["GearCompoundAdvancedSystemDeflection"],
        "_7464": ["GearMeshCompoundAdvancedSystemDeflection"],
        "_7465": ["GearSetCompoundAdvancedSystemDeflection"],
        "_7466": ["GuideDxfModelCompoundAdvancedSystemDeflection"],
        "_7467": ["HypoidGearCompoundAdvancedSystemDeflection"],
        "_7468": ["HypoidGearMeshCompoundAdvancedSystemDeflection"],
        "_7469": ["HypoidGearSetCompoundAdvancedSystemDeflection"],
        "_7470": ["InterMountableComponentConnectionCompoundAdvancedSystemDeflection"],
        "_7471": [
            "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ],
        "_7472": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7473": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7474": ["KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection"],
        "_7475": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7476": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7477": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
        ],
        "_7478": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection"
        ],
        "_7479": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection"
        ],
        "_7480": ["MassDiscCompoundAdvancedSystemDeflection"],
        "_7481": ["MeasurementComponentCompoundAdvancedSystemDeflection"],
        "_7482": ["MountableComponentCompoundAdvancedSystemDeflection"],
        "_7483": ["OilSealCompoundAdvancedSystemDeflection"],
        "_7484": ["PartCompoundAdvancedSystemDeflection"],
        "_7485": ["PartToPartShearCouplingCompoundAdvancedSystemDeflection"],
        "_7486": ["PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection"],
        "_7487": ["PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection"],
        "_7488": ["PlanetaryConnectionCompoundAdvancedSystemDeflection"],
        "_7489": ["PlanetaryGearSetCompoundAdvancedSystemDeflection"],
        "_7490": ["PlanetCarrierCompoundAdvancedSystemDeflection"],
        "_7491": ["PointLoadCompoundAdvancedSystemDeflection"],
        "_7492": ["PowerLoadCompoundAdvancedSystemDeflection"],
        "_7493": ["PulleyCompoundAdvancedSystemDeflection"],
        "_7494": ["RingPinsCompoundAdvancedSystemDeflection"],
        "_7495": ["RingPinsToDiscConnectionCompoundAdvancedSystemDeflection"],
        "_7496": ["RollingRingAssemblyCompoundAdvancedSystemDeflection"],
        "_7497": ["RollingRingCompoundAdvancedSystemDeflection"],
        "_7498": ["RollingRingConnectionCompoundAdvancedSystemDeflection"],
        "_7499": ["RootAssemblyCompoundAdvancedSystemDeflection"],
        "_7500": ["ShaftCompoundAdvancedSystemDeflection"],
        "_7501": ["ShaftHubConnectionCompoundAdvancedSystemDeflection"],
        "_7502": [
            "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
        ],
        "_7503": ["SpecialisedAssemblyCompoundAdvancedSystemDeflection"],
        "_7504": ["SpiralBevelGearCompoundAdvancedSystemDeflection"],
        "_7505": ["SpiralBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7506": ["SpiralBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7507": ["SpringDamperCompoundAdvancedSystemDeflection"],
        "_7508": ["SpringDamperConnectionCompoundAdvancedSystemDeflection"],
        "_7509": ["SpringDamperHalfCompoundAdvancedSystemDeflection"],
        "_7510": ["StraightBevelDiffGearCompoundAdvancedSystemDeflection"],
        "_7511": ["StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection"],
        "_7512": ["StraightBevelDiffGearSetCompoundAdvancedSystemDeflection"],
        "_7513": ["StraightBevelGearCompoundAdvancedSystemDeflection"],
        "_7514": ["StraightBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7515": ["StraightBevelGearSetCompoundAdvancedSystemDeflection"],
        "_7516": ["StraightBevelPlanetGearCompoundAdvancedSystemDeflection"],
        "_7517": ["StraightBevelSunGearCompoundAdvancedSystemDeflection"],
        "_7518": ["SynchroniserCompoundAdvancedSystemDeflection"],
        "_7519": ["SynchroniserHalfCompoundAdvancedSystemDeflection"],
        "_7520": ["SynchroniserPartCompoundAdvancedSystemDeflection"],
        "_7521": ["SynchroniserSleeveCompoundAdvancedSystemDeflection"],
        "_7522": ["TorqueConverterCompoundAdvancedSystemDeflection"],
        "_7523": ["TorqueConverterConnectionCompoundAdvancedSystemDeflection"],
        "_7524": ["TorqueConverterPumpCompoundAdvancedSystemDeflection"],
        "_7525": ["TorqueConverterTurbineCompoundAdvancedSystemDeflection"],
        "_7526": ["UnbalancedMassCompoundAdvancedSystemDeflection"],
        "_7527": ["VirtualComponentCompoundAdvancedSystemDeflection"],
        "_7528": ["WormGearCompoundAdvancedSystemDeflection"],
        "_7529": ["WormGearMeshCompoundAdvancedSystemDeflection"],
        "_7530": ["WormGearSetCompoundAdvancedSystemDeflection"],
        "_7531": ["ZerolBevelGearCompoundAdvancedSystemDeflection"],
        "_7532": ["ZerolBevelGearMeshCompoundAdvancedSystemDeflection"],
        "_7533": ["ZerolBevelGearSetCompoundAdvancedSystemDeflection"],
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

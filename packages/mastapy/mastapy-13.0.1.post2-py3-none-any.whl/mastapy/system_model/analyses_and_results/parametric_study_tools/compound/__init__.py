"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4443 import AbstractAssemblyCompoundParametricStudyTool
    from ._4444 import AbstractShaftCompoundParametricStudyTool
    from ._4445 import AbstractShaftOrHousingCompoundParametricStudyTool
    from ._4446 import (
        AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool,
    )
    from ._4447 import AGMAGleasonConicalGearCompoundParametricStudyTool
    from ._4448 import AGMAGleasonConicalGearMeshCompoundParametricStudyTool
    from ._4449 import AGMAGleasonConicalGearSetCompoundParametricStudyTool
    from ._4450 import AssemblyCompoundParametricStudyTool
    from ._4451 import BearingCompoundParametricStudyTool
    from ._4452 import BeltConnectionCompoundParametricStudyTool
    from ._4453 import BeltDriveCompoundParametricStudyTool
    from ._4454 import BevelDifferentialGearCompoundParametricStudyTool
    from ._4455 import BevelDifferentialGearMeshCompoundParametricStudyTool
    from ._4456 import BevelDifferentialGearSetCompoundParametricStudyTool
    from ._4457 import BevelDifferentialPlanetGearCompoundParametricStudyTool
    from ._4458 import BevelDifferentialSunGearCompoundParametricStudyTool
    from ._4459 import BevelGearCompoundParametricStudyTool
    from ._4460 import BevelGearMeshCompoundParametricStudyTool
    from ._4461 import BevelGearSetCompoundParametricStudyTool
    from ._4462 import BoltCompoundParametricStudyTool
    from ._4463 import BoltedJointCompoundParametricStudyTool
    from ._4464 import ClutchCompoundParametricStudyTool
    from ._4465 import ClutchConnectionCompoundParametricStudyTool
    from ._4466 import ClutchHalfCompoundParametricStudyTool
    from ._4467 import CoaxialConnectionCompoundParametricStudyTool
    from ._4468 import ComponentCompoundParametricStudyTool
    from ._4469 import ConceptCouplingCompoundParametricStudyTool
    from ._4470 import ConceptCouplingConnectionCompoundParametricStudyTool
    from ._4471 import ConceptCouplingHalfCompoundParametricStudyTool
    from ._4472 import ConceptGearCompoundParametricStudyTool
    from ._4473 import ConceptGearMeshCompoundParametricStudyTool
    from ._4474 import ConceptGearSetCompoundParametricStudyTool
    from ._4475 import ConicalGearCompoundParametricStudyTool
    from ._4476 import ConicalGearMeshCompoundParametricStudyTool
    from ._4477 import ConicalGearSetCompoundParametricStudyTool
    from ._4478 import ConnectionCompoundParametricStudyTool
    from ._4479 import ConnectorCompoundParametricStudyTool
    from ._4480 import CouplingCompoundParametricStudyTool
    from ._4481 import CouplingConnectionCompoundParametricStudyTool
    from ._4482 import CouplingHalfCompoundParametricStudyTool
    from ._4483 import CVTBeltConnectionCompoundParametricStudyTool
    from ._4484 import CVTCompoundParametricStudyTool
    from ._4485 import CVTPulleyCompoundParametricStudyTool
    from ._4486 import CycloidalAssemblyCompoundParametricStudyTool
    from ._4487 import CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
    from ._4488 import CycloidalDiscCompoundParametricStudyTool
    from ._4489 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool,
    )
    from ._4490 import CylindricalGearCompoundParametricStudyTool
    from ._4491 import CylindricalGearMeshCompoundParametricStudyTool
    from ._4492 import CylindricalGearSetCompoundParametricStudyTool
    from ._4493 import CylindricalPlanetGearCompoundParametricStudyTool
    from ._4494 import DatumCompoundParametricStudyTool
    from ._4495 import ExternalCADModelCompoundParametricStudyTool
    from ._4496 import FaceGearCompoundParametricStudyTool
    from ._4497 import FaceGearMeshCompoundParametricStudyTool
    from ._4498 import FaceGearSetCompoundParametricStudyTool
    from ._4499 import FEPartCompoundParametricStudyTool
    from ._4500 import FlexiblePinAssemblyCompoundParametricStudyTool
    from ._4501 import GearCompoundParametricStudyTool
    from ._4502 import GearMeshCompoundParametricStudyTool
    from ._4503 import GearSetCompoundParametricStudyTool
    from ._4504 import GuideDxfModelCompoundParametricStudyTool
    from ._4505 import HypoidGearCompoundParametricStudyTool
    from ._4506 import HypoidGearMeshCompoundParametricStudyTool
    from ._4507 import HypoidGearSetCompoundParametricStudyTool
    from ._4508 import InterMountableComponentConnectionCompoundParametricStudyTool
    from ._4509 import KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
    from ._4510 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool,
    )
    from ._4511 import KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
    from ._4512 import KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
    from ._4513 import KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
    from ._4514 import KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
    from ._4515 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool,
    )
    from ._4516 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool,
    )
    from ._4517 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool,
    )
    from ._4518 import MassDiscCompoundParametricStudyTool
    from ._4519 import MeasurementComponentCompoundParametricStudyTool
    from ._4520 import MountableComponentCompoundParametricStudyTool
    from ._4521 import OilSealCompoundParametricStudyTool
    from ._4522 import PartCompoundParametricStudyTool
    from ._4523 import PartToPartShearCouplingCompoundParametricStudyTool
    from ._4524 import PartToPartShearCouplingConnectionCompoundParametricStudyTool
    from ._4525 import PartToPartShearCouplingHalfCompoundParametricStudyTool
    from ._4526 import PlanetaryConnectionCompoundParametricStudyTool
    from ._4527 import PlanetaryGearSetCompoundParametricStudyTool
    from ._4528 import PlanetCarrierCompoundParametricStudyTool
    from ._4529 import PointLoadCompoundParametricStudyTool
    from ._4530 import PowerLoadCompoundParametricStudyTool
    from ._4531 import PulleyCompoundParametricStudyTool
    from ._4532 import RingPinsCompoundParametricStudyTool
    from ._4533 import RingPinsToDiscConnectionCompoundParametricStudyTool
    from ._4534 import RollingRingAssemblyCompoundParametricStudyTool
    from ._4535 import RollingRingCompoundParametricStudyTool
    from ._4536 import RollingRingConnectionCompoundParametricStudyTool
    from ._4537 import RootAssemblyCompoundParametricStudyTool
    from ._4538 import ShaftCompoundParametricStudyTool
    from ._4539 import ShaftHubConnectionCompoundParametricStudyTool
    from ._4540 import ShaftToMountableComponentConnectionCompoundParametricStudyTool
    from ._4541 import SpecialisedAssemblyCompoundParametricStudyTool
    from ._4542 import SpiralBevelGearCompoundParametricStudyTool
    from ._4543 import SpiralBevelGearMeshCompoundParametricStudyTool
    from ._4544 import SpiralBevelGearSetCompoundParametricStudyTool
    from ._4545 import SpringDamperCompoundParametricStudyTool
    from ._4546 import SpringDamperConnectionCompoundParametricStudyTool
    from ._4547 import SpringDamperHalfCompoundParametricStudyTool
    from ._4548 import StraightBevelDiffGearCompoundParametricStudyTool
    from ._4549 import StraightBevelDiffGearMeshCompoundParametricStudyTool
    from ._4550 import StraightBevelDiffGearSetCompoundParametricStudyTool
    from ._4551 import StraightBevelGearCompoundParametricStudyTool
    from ._4552 import StraightBevelGearMeshCompoundParametricStudyTool
    from ._4553 import StraightBevelGearSetCompoundParametricStudyTool
    from ._4554 import StraightBevelPlanetGearCompoundParametricStudyTool
    from ._4555 import StraightBevelSunGearCompoundParametricStudyTool
    from ._4556 import SynchroniserCompoundParametricStudyTool
    from ._4557 import SynchroniserHalfCompoundParametricStudyTool
    from ._4558 import SynchroniserPartCompoundParametricStudyTool
    from ._4559 import SynchroniserSleeveCompoundParametricStudyTool
    from ._4560 import TorqueConverterCompoundParametricStudyTool
    from ._4561 import TorqueConverterConnectionCompoundParametricStudyTool
    from ._4562 import TorqueConverterPumpCompoundParametricStudyTool
    from ._4563 import TorqueConverterTurbineCompoundParametricStudyTool
    from ._4564 import UnbalancedMassCompoundParametricStudyTool
    from ._4565 import VirtualComponentCompoundParametricStudyTool
    from ._4566 import WormGearCompoundParametricStudyTool
    from ._4567 import WormGearMeshCompoundParametricStudyTool
    from ._4568 import WormGearSetCompoundParametricStudyTool
    from ._4569 import ZerolBevelGearCompoundParametricStudyTool
    from ._4570 import ZerolBevelGearMeshCompoundParametricStudyTool
    from ._4571 import ZerolBevelGearSetCompoundParametricStudyTool
else:
    import_structure = {
        "_4443": ["AbstractAssemblyCompoundParametricStudyTool"],
        "_4444": ["AbstractShaftCompoundParametricStudyTool"],
        "_4445": ["AbstractShaftOrHousingCompoundParametricStudyTool"],
        "_4446": [
            "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool"
        ],
        "_4447": ["AGMAGleasonConicalGearCompoundParametricStudyTool"],
        "_4448": ["AGMAGleasonConicalGearMeshCompoundParametricStudyTool"],
        "_4449": ["AGMAGleasonConicalGearSetCompoundParametricStudyTool"],
        "_4450": ["AssemblyCompoundParametricStudyTool"],
        "_4451": ["BearingCompoundParametricStudyTool"],
        "_4452": ["BeltConnectionCompoundParametricStudyTool"],
        "_4453": ["BeltDriveCompoundParametricStudyTool"],
        "_4454": ["BevelDifferentialGearCompoundParametricStudyTool"],
        "_4455": ["BevelDifferentialGearMeshCompoundParametricStudyTool"],
        "_4456": ["BevelDifferentialGearSetCompoundParametricStudyTool"],
        "_4457": ["BevelDifferentialPlanetGearCompoundParametricStudyTool"],
        "_4458": ["BevelDifferentialSunGearCompoundParametricStudyTool"],
        "_4459": ["BevelGearCompoundParametricStudyTool"],
        "_4460": ["BevelGearMeshCompoundParametricStudyTool"],
        "_4461": ["BevelGearSetCompoundParametricStudyTool"],
        "_4462": ["BoltCompoundParametricStudyTool"],
        "_4463": ["BoltedJointCompoundParametricStudyTool"],
        "_4464": ["ClutchCompoundParametricStudyTool"],
        "_4465": ["ClutchConnectionCompoundParametricStudyTool"],
        "_4466": ["ClutchHalfCompoundParametricStudyTool"],
        "_4467": ["CoaxialConnectionCompoundParametricStudyTool"],
        "_4468": ["ComponentCompoundParametricStudyTool"],
        "_4469": ["ConceptCouplingCompoundParametricStudyTool"],
        "_4470": ["ConceptCouplingConnectionCompoundParametricStudyTool"],
        "_4471": ["ConceptCouplingHalfCompoundParametricStudyTool"],
        "_4472": ["ConceptGearCompoundParametricStudyTool"],
        "_4473": ["ConceptGearMeshCompoundParametricStudyTool"],
        "_4474": ["ConceptGearSetCompoundParametricStudyTool"],
        "_4475": ["ConicalGearCompoundParametricStudyTool"],
        "_4476": ["ConicalGearMeshCompoundParametricStudyTool"],
        "_4477": ["ConicalGearSetCompoundParametricStudyTool"],
        "_4478": ["ConnectionCompoundParametricStudyTool"],
        "_4479": ["ConnectorCompoundParametricStudyTool"],
        "_4480": ["CouplingCompoundParametricStudyTool"],
        "_4481": ["CouplingConnectionCompoundParametricStudyTool"],
        "_4482": ["CouplingHalfCompoundParametricStudyTool"],
        "_4483": ["CVTBeltConnectionCompoundParametricStudyTool"],
        "_4484": ["CVTCompoundParametricStudyTool"],
        "_4485": ["CVTPulleyCompoundParametricStudyTool"],
        "_4486": ["CycloidalAssemblyCompoundParametricStudyTool"],
        "_4487": ["CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"],
        "_4488": ["CycloidalDiscCompoundParametricStudyTool"],
        "_4489": ["CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool"],
        "_4490": ["CylindricalGearCompoundParametricStudyTool"],
        "_4491": ["CylindricalGearMeshCompoundParametricStudyTool"],
        "_4492": ["CylindricalGearSetCompoundParametricStudyTool"],
        "_4493": ["CylindricalPlanetGearCompoundParametricStudyTool"],
        "_4494": ["DatumCompoundParametricStudyTool"],
        "_4495": ["ExternalCADModelCompoundParametricStudyTool"],
        "_4496": ["FaceGearCompoundParametricStudyTool"],
        "_4497": ["FaceGearMeshCompoundParametricStudyTool"],
        "_4498": ["FaceGearSetCompoundParametricStudyTool"],
        "_4499": ["FEPartCompoundParametricStudyTool"],
        "_4500": ["FlexiblePinAssemblyCompoundParametricStudyTool"],
        "_4501": ["GearCompoundParametricStudyTool"],
        "_4502": ["GearMeshCompoundParametricStudyTool"],
        "_4503": ["GearSetCompoundParametricStudyTool"],
        "_4504": ["GuideDxfModelCompoundParametricStudyTool"],
        "_4505": ["HypoidGearCompoundParametricStudyTool"],
        "_4506": ["HypoidGearMeshCompoundParametricStudyTool"],
        "_4507": ["HypoidGearSetCompoundParametricStudyTool"],
        "_4508": ["InterMountableComponentConnectionCompoundParametricStudyTool"],
        "_4509": ["KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool"],
        "_4510": ["KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool"],
        "_4511": ["KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool"],
        "_4512": ["KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"],
        "_4513": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool"],
        "_4514": ["KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool"],
        "_4515": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool"],
        "_4516": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool"
        ],
        "_4517": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool"
        ],
        "_4518": ["MassDiscCompoundParametricStudyTool"],
        "_4519": ["MeasurementComponentCompoundParametricStudyTool"],
        "_4520": ["MountableComponentCompoundParametricStudyTool"],
        "_4521": ["OilSealCompoundParametricStudyTool"],
        "_4522": ["PartCompoundParametricStudyTool"],
        "_4523": ["PartToPartShearCouplingCompoundParametricStudyTool"],
        "_4524": ["PartToPartShearCouplingConnectionCompoundParametricStudyTool"],
        "_4525": ["PartToPartShearCouplingHalfCompoundParametricStudyTool"],
        "_4526": ["PlanetaryConnectionCompoundParametricStudyTool"],
        "_4527": ["PlanetaryGearSetCompoundParametricStudyTool"],
        "_4528": ["PlanetCarrierCompoundParametricStudyTool"],
        "_4529": ["PointLoadCompoundParametricStudyTool"],
        "_4530": ["PowerLoadCompoundParametricStudyTool"],
        "_4531": ["PulleyCompoundParametricStudyTool"],
        "_4532": ["RingPinsCompoundParametricStudyTool"],
        "_4533": ["RingPinsToDiscConnectionCompoundParametricStudyTool"],
        "_4534": ["RollingRingAssemblyCompoundParametricStudyTool"],
        "_4535": ["RollingRingCompoundParametricStudyTool"],
        "_4536": ["RollingRingConnectionCompoundParametricStudyTool"],
        "_4537": ["RootAssemblyCompoundParametricStudyTool"],
        "_4538": ["ShaftCompoundParametricStudyTool"],
        "_4539": ["ShaftHubConnectionCompoundParametricStudyTool"],
        "_4540": ["ShaftToMountableComponentConnectionCompoundParametricStudyTool"],
        "_4541": ["SpecialisedAssemblyCompoundParametricStudyTool"],
        "_4542": ["SpiralBevelGearCompoundParametricStudyTool"],
        "_4543": ["SpiralBevelGearMeshCompoundParametricStudyTool"],
        "_4544": ["SpiralBevelGearSetCompoundParametricStudyTool"],
        "_4545": ["SpringDamperCompoundParametricStudyTool"],
        "_4546": ["SpringDamperConnectionCompoundParametricStudyTool"],
        "_4547": ["SpringDamperHalfCompoundParametricStudyTool"],
        "_4548": ["StraightBevelDiffGearCompoundParametricStudyTool"],
        "_4549": ["StraightBevelDiffGearMeshCompoundParametricStudyTool"],
        "_4550": ["StraightBevelDiffGearSetCompoundParametricStudyTool"],
        "_4551": ["StraightBevelGearCompoundParametricStudyTool"],
        "_4552": ["StraightBevelGearMeshCompoundParametricStudyTool"],
        "_4553": ["StraightBevelGearSetCompoundParametricStudyTool"],
        "_4554": ["StraightBevelPlanetGearCompoundParametricStudyTool"],
        "_4555": ["StraightBevelSunGearCompoundParametricStudyTool"],
        "_4556": ["SynchroniserCompoundParametricStudyTool"],
        "_4557": ["SynchroniserHalfCompoundParametricStudyTool"],
        "_4558": ["SynchroniserPartCompoundParametricStudyTool"],
        "_4559": ["SynchroniserSleeveCompoundParametricStudyTool"],
        "_4560": ["TorqueConverterCompoundParametricStudyTool"],
        "_4561": ["TorqueConverterConnectionCompoundParametricStudyTool"],
        "_4562": ["TorqueConverterPumpCompoundParametricStudyTool"],
        "_4563": ["TorqueConverterTurbineCompoundParametricStudyTool"],
        "_4564": ["UnbalancedMassCompoundParametricStudyTool"],
        "_4565": ["VirtualComponentCompoundParametricStudyTool"],
        "_4566": ["WormGearCompoundParametricStudyTool"],
        "_4567": ["WormGearMeshCompoundParametricStudyTool"],
        "_4568": ["WormGearSetCompoundParametricStudyTool"],
        "_4569": ["ZerolBevelGearCompoundParametricStudyTool"],
        "_4570": ["ZerolBevelGearMeshCompoundParametricStudyTool"],
        "_4571": ["ZerolBevelGearSetCompoundParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundParametricStudyTool",
    "AbstractShaftCompoundParametricStudyTool",
    "AbstractShaftOrHousingCompoundParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "AGMAGleasonConicalGearCompoundParametricStudyTool",
    "AGMAGleasonConicalGearMeshCompoundParametricStudyTool",
    "AGMAGleasonConicalGearSetCompoundParametricStudyTool",
    "AssemblyCompoundParametricStudyTool",
    "BearingCompoundParametricStudyTool",
    "BeltConnectionCompoundParametricStudyTool",
    "BeltDriveCompoundParametricStudyTool",
    "BevelDifferentialGearCompoundParametricStudyTool",
    "BevelDifferentialGearMeshCompoundParametricStudyTool",
    "BevelDifferentialGearSetCompoundParametricStudyTool",
    "BevelDifferentialPlanetGearCompoundParametricStudyTool",
    "BevelDifferentialSunGearCompoundParametricStudyTool",
    "BevelGearCompoundParametricStudyTool",
    "BevelGearMeshCompoundParametricStudyTool",
    "BevelGearSetCompoundParametricStudyTool",
    "BoltCompoundParametricStudyTool",
    "BoltedJointCompoundParametricStudyTool",
    "ClutchCompoundParametricStudyTool",
    "ClutchConnectionCompoundParametricStudyTool",
    "ClutchHalfCompoundParametricStudyTool",
    "CoaxialConnectionCompoundParametricStudyTool",
    "ComponentCompoundParametricStudyTool",
    "ConceptCouplingCompoundParametricStudyTool",
    "ConceptCouplingConnectionCompoundParametricStudyTool",
    "ConceptCouplingHalfCompoundParametricStudyTool",
    "ConceptGearCompoundParametricStudyTool",
    "ConceptGearMeshCompoundParametricStudyTool",
    "ConceptGearSetCompoundParametricStudyTool",
    "ConicalGearCompoundParametricStudyTool",
    "ConicalGearMeshCompoundParametricStudyTool",
    "ConicalGearSetCompoundParametricStudyTool",
    "ConnectionCompoundParametricStudyTool",
    "ConnectorCompoundParametricStudyTool",
    "CouplingCompoundParametricStudyTool",
    "CouplingConnectionCompoundParametricStudyTool",
    "CouplingHalfCompoundParametricStudyTool",
    "CVTBeltConnectionCompoundParametricStudyTool",
    "CVTCompoundParametricStudyTool",
    "CVTPulleyCompoundParametricStudyTool",
    "CycloidalAssemblyCompoundParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool",
    "CycloidalDiscCompoundParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool",
    "CylindricalGearCompoundParametricStudyTool",
    "CylindricalGearMeshCompoundParametricStudyTool",
    "CylindricalGearSetCompoundParametricStudyTool",
    "CylindricalPlanetGearCompoundParametricStudyTool",
    "DatumCompoundParametricStudyTool",
    "ExternalCADModelCompoundParametricStudyTool",
    "FaceGearCompoundParametricStudyTool",
    "FaceGearMeshCompoundParametricStudyTool",
    "FaceGearSetCompoundParametricStudyTool",
    "FEPartCompoundParametricStudyTool",
    "FlexiblePinAssemblyCompoundParametricStudyTool",
    "GearCompoundParametricStudyTool",
    "GearMeshCompoundParametricStudyTool",
    "GearSetCompoundParametricStudyTool",
    "GuideDxfModelCompoundParametricStudyTool",
    "HypoidGearCompoundParametricStudyTool",
    "HypoidGearMeshCompoundParametricStudyTool",
    "HypoidGearSetCompoundParametricStudyTool",
    "InterMountableComponentConnectionCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool",
    "MassDiscCompoundParametricStudyTool",
    "MeasurementComponentCompoundParametricStudyTool",
    "MountableComponentCompoundParametricStudyTool",
    "OilSealCompoundParametricStudyTool",
    "PartCompoundParametricStudyTool",
    "PartToPartShearCouplingCompoundParametricStudyTool",
    "PartToPartShearCouplingConnectionCompoundParametricStudyTool",
    "PartToPartShearCouplingHalfCompoundParametricStudyTool",
    "PlanetaryConnectionCompoundParametricStudyTool",
    "PlanetaryGearSetCompoundParametricStudyTool",
    "PlanetCarrierCompoundParametricStudyTool",
    "PointLoadCompoundParametricStudyTool",
    "PowerLoadCompoundParametricStudyTool",
    "PulleyCompoundParametricStudyTool",
    "RingPinsCompoundParametricStudyTool",
    "RingPinsToDiscConnectionCompoundParametricStudyTool",
    "RollingRingAssemblyCompoundParametricStudyTool",
    "RollingRingCompoundParametricStudyTool",
    "RollingRingConnectionCompoundParametricStudyTool",
    "RootAssemblyCompoundParametricStudyTool",
    "ShaftCompoundParametricStudyTool",
    "ShaftHubConnectionCompoundParametricStudyTool",
    "ShaftToMountableComponentConnectionCompoundParametricStudyTool",
    "SpecialisedAssemblyCompoundParametricStudyTool",
    "SpiralBevelGearCompoundParametricStudyTool",
    "SpiralBevelGearMeshCompoundParametricStudyTool",
    "SpiralBevelGearSetCompoundParametricStudyTool",
    "SpringDamperCompoundParametricStudyTool",
    "SpringDamperConnectionCompoundParametricStudyTool",
    "SpringDamperHalfCompoundParametricStudyTool",
    "StraightBevelDiffGearCompoundParametricStudyTool",
    "StraightBevelDiffGearMeshCompoundParametricStudyTool",
    "StraightBevelDiffGearSetCompoundParametricStudyTool",
    "StraightBevelGearCompoundParametricStudyTool",
    "StraightBevelGearMeshCompoundParametricStudyTool",
    "StraightBevelGearSetCompoundParametricStudyTool",
    "StraightBevelPlanetGearCompoundParametricStudyTool",
    "StraightBevelSunGearCompoundParametricStudyTool",
    "SynchroniserCompoundParametricStudyTool",
    "SynchroniserHalfCompoundParametricStudyTool",
    "SynchroniserPartCompoundParametricStudyTool",
    "SynchroniserSleeveCompoundParametricStudyTool",
    "TorqueConverterCompoundParametricStudyTool",
    "TorqueConverterConnectionCompoundParametricStudyTool",
    "TorqueConverterPumpCompoundParametricStudyTool",
    "TorqueConverterTurbineCompoundParametricStudyTool",
    "UnbalancedMassCompoundParametricStudyTool",
    "VirtualComponentCompoundParametricStudyTool",
    "WormGearCompoundParametricStudyTool",
    "WormGearMeshCompoundParametricStudyTool",
    "WormGearSetCompoundParametricStudyTool",
    "ZerolBevelGearCompoundParametricStudyTool",
    "ZerolBevelGearMeshCompoundParametricStudyTool",
    "ZerolBevelGearSetCompoundParametricStudyTool",
)

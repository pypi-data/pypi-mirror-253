"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4442 import AbstractAssemblyCompoundParametricStudyTool
    from ._4443 import AbstractShaftCompoundParametricStudyTool
    from ._4444 import AbstractShaftOrHousingCompoundParametricStudyTool
    from ._4445 import (
        AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool,
    )
    from ._4446 import AGMAGleasonConicalGearCompoundParametricStudyTool
    from ._4447 import AGMAGleasonConicalGearMeshCompoundParametricStudyTool
    from ._4448 import AGMAGleasonConicalGearSetCompoundParametricStudyTool
    from ._4449 import AssemblyCompoundParametricStudyTool
    from ._4450 import BearingCompoundParametricStudyTool
    from ._4451 import BeltConnectionCompoundParametricStudyTool
    from ._4452 import BeltDriveCompoundParametricStudyTool
    from ._4453 import BevelDifferentialGearCompoundParametricStudyTool
    from ._4454 import BevelDifferentialGearMeshCompoundParametricStudyTool
    from ._4455 import BevelDifferentialGearSetCompoundParametricStudyTool
    from ._4456 import BevelDifferentialPlanetGearCompoundParametricStudyTool
    from ._4457 import BevelDifferentialSunGearCompoundParametricStudyTool
    from ._4458 import BevelGearCompoundParametricStudyTool
    from ._4459 import BevelGearMeshCompoundParametricStudyTool
    from ._4460 import BevelGearSetCompoundParametricStudyTool
    from ._4461 import BoltCompoundParametricStudyTool
    from ._4462 import BoltedJointCompoundParametricStudyTool
    from ._4463 import ClutchCompoundParametricStudyTool
    from ._4464 import ClutchConnectionCompoundParametricStudyTool
    from ._4465 import ClutchHalfCompoundParametricStudyTool
    from ._4466 import CoaxialConnectionCompoundParametricStudyTool
    from ._4467 import ComponentCompoundParametricStudyTool
    from ._4468 import ConceptCouplingCompoundParametricStudyTool
    from ._4469 import ConceptCouplingConnectionCompoundParametricStudyTool
    from ._4470 import ConceptCouplingHalfCompoundParametricStudyTool
    from ._4471 import ConceptGearCompoundParametricStudyTool
    from ._4472 import ConceptGearMeshCompoundParametricStudyTool
    from ._4473 import ConceptGearSetCompoundParametricStudyTool
    from ._4474 import ConicalGearCompoundParametricStudyTool
    from ._4475 import ConicalGearMeshCompoundParametricStudyTool
    from ._4476 import ConicalGearSetCompoundParametricStudyTool
    from ._4477 import ConnectionCompoundParametricStudyTool
    from ._4478 import ConnectorCompoundParametricStudyTool
    from ._4479 import CouplingCompoundParametricStudyTool
    from ._4480 import CouplingConnectionCompoundParametricStudyTool
    from ._4481 import CouplingHalfCompoundParametricStudyTool
    from ._4482 import CVTBeltConnectionCompoundParametricStudyTool
    from ._4483 import CVTCompoundParametricStudyTool
    from ._4484 import CVTPulleyCompoundParametricStudyTool
    from ._4485 import CycloidalAssemblyCompoundParametricStudyTool
    from ._4486 import CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
    from ._4487 import CycloidalDiscCompoundParametricStudyTool
    from ._4488 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool,
    )
    from ._4489 import CylindricalGearCompoundParametricStudyTool
    from ._4490 import CylindricalGearMeshCompoundParametricStudyTool
    from ._4491 import CylindricalGearSetCompoundParametricStudyTool
    from ._4492 import CylindricalPlanetGearCompoundParametricStudyTool
    from ._4493 import DatumCompoundParametricStudyTool
    from ._4494 import ExternalCADModelCompoundParametricStudyTool
    from ._4495 import FaceGearCompoundParametricStudyTool
    from ._4496 import FaceGearMeshCompoundParametricStudyTool
    from ._4497 import FaceGearSetCompoundParametricStudyTool
    from ._4498 import FEPartCompoundParametricStudyTool
    from ._4499 import FlexiblePinAssemblyCompoundParametricStudyTool
    from ._4500 import GearCompoundParametricStudyTool
    from ._4501 import GearMeshCompoundParametricStudyTool
    from ._4502 import GearSetCompoundParametricStudyTool
    from ._4503 import GuideDxfModelCompoundParametricStudyTool
    from ._4504 import HypoidGearCompoundParametricStudyTool
    from ._4505 import HypoidGearMeshCompoundParametricStudyTool
    from ._4506 import HypoidGearSetCompoundParametricStudyTool
    from ._4507 import InterMountableComponentConnectionCompoundParametricStudyTool
    from ._4508 import KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
    from ._4509 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool,
    )
    from ._4510 import KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
    from ._4511 import KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
    from ._4512 import KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool
    from ._4513 import KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
    from ._4514 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool,
    )
    from ._4515 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool,
    )
    from ._4516 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool,
    )
    from ._4517 import MassDiscCompoundParametricStudyTool
    from ._4518 import MeasurementComponentCompoundParametricStudyTool
    from ._4519 import MountableComponentCompoundParametricStudyTool
    from ._4520 import OilSealCompoundParametricStudyTool
    from ._4521 import PartCompoundParametricStudyTool
    from ._4522 import PartToPartShearCouplingCompoundParametricStudyTool
    from ._4523 import PartToPartShearCouplingConnectionCompoundParametricStudyTool
    from ._4524 import PartToPartShearCouplingHalfCompoundParametricStudyTool
    from ._4525 import PlanetaryConnectionCompoundParametricStudyTool
    from ._4526 import PlanetaryGearSetCompoundParametricStudyTool
    from ._4527 import PlanetCarrierCompoundParametricStudyTool
    from ._4528 import PointLoadCompoundParametricStudyTool
    from ._4529 import PowerLoadCompoundParametricStudyTool
    from ._4530 import PulleyCompoundParametricStudyTool
    from ._4531 import RingPinsCompoundParametricStudyTool
    from ._4532 import RingPinsToDiscConnectionCompoundParametricStudyTool
    from ._4533 import RollingRingAssemblyCompoundParametricStudyTool
    from ._4534 import RollingRingCompoundParametricStudyTool
    from ._4535 import RollingRingConnectionCompoundParametricStudyTool
    from ._4536 import RootAssemblyCompoundParametricStudyTool
    from ._4537 import ShaftCompoundParametricStudyTool
    from ._4538 import ShaftHubConnectionCompoundParametricStudyTool
    from ._4539 import ShaftToMountableComponentConnectionCompoundParametricStudyTool
    from ._4540 import SpecialisedAssemblyCompoundParametricStudyTool
    from ._4541 import SpiralBevelGearCompoundParametricStudyTool
    from ._4542 import SpiralBevelGearMeshCompoundParametricStudyTool
    from ._4543 import SpiralBevelGearSetCompoundParametricStudyTool
    from ._4544 import SpringDamperCompoundParametricStudyTool
    from ._4545 import SpringDamperConnectionCompoundParametricStudyTool
    from ._4546 import SpringDamperHalfCompoundParametricStudyTool
    from ._4547 import StraightBevelDiffGearCompoundParametricStudyTool
    from ._4548 import StraightBevelDiffGearMeshCompoundParametricStudyTool
    from ._4549 import StraightBevelDiffGearSetCompoundParametricStudyTool
    from ._4550 import StraightBevelGearCompoundParametricStudyTool
    from ._4551 import StraightBevelGearMeshCompoundParametricStudyTool
    from ._4552 import StraightBevelGearSetCompoundParametricStudyTool
    from ._4553 import StraightBevelPlanetGearCompoundParametricStudyTool
    from ._4554 import StraightBevelSunGearCompoundParametricStudyTool
    from ._4555 import SynchroniserCompoundParametricStudyTool
    from ._4556 import SynchroniserHalfCompoundParametricStudyTool
    from ._4557 import SynchroniserPartCompoundParametricStudyTool
    from ._4558 import SynchroniserSleeveCompoundParametricStudyTool
    from ._4559 import TorqueConverterCompoundParametricStudyTool
    from ._4560 import TorqueConverterConnectionCompoundParametricStudyTool
    from ._4561 import TorqueConverterPumpCompoundParametricStudyTool
    from ._4562 import TorqueConverterTurbineCompoundParametricStudyTool
    from ._4563 import UnbalancedMassCompoundParametricStudyTool
    from ._4564 import VirtualComponentCompoundParametricStudyTool
    from ._4565 import WormGearCompoundParametricStudyTool
    from ._4566 import WormGearMeshCompoundParametricStudyTool
    from ._4567 import WormGearSetCompoundParametricStudyTool
    from ._4568 import ZerolBevelGearCompoundParametricStudyTool
    from ._4569 import ZerolBevelGearMeshCompoundParametricStudyTool
    from ._4570 import ZerolBevelGearSetCompoundParametricStudyTool
else:
    import_structure = {
        "_4442": ["AbstractAssemblyCompoundParametricStudyTool"],
        "_4443": ["AbstractShaftCompoundParametricStudyTool"],
        "_4444": ["AbstractShaftOrHousingCompoundParametricStudyTool"],
        "_4445": [
            "AbstractShaftToMountableComponentConnectionCompoundParametricStudyTool"
        ],
        "_4446": ["AGMAGleasonConicalGearCompoundParametricStudyTool"],
        "_4447": ["AGMAGleasonConicalGearMeshCompoundParametricStudyTool"],
        "_4448": ["AGMAGleasonConicalGearSetCompoundParametricStudyTool"],
        "_4449": ["AssemblyCompoundParametricStudyTool"],
        "_4450": ["BearingCompoundParametricStudyTool"],
        "_4451": ["BeltConnectionCompoundParametricStudyTool"],
        "_4452": ["BeltDriveCompoundParametricStudyTool"],
        "_4453": ["BevelDifferentialGearCompoundParametricStudyTool"],
        "_4454": ["BevelDifferentialGearMeshCompoundParametricStudyTool"],
        "_4455": ["BevelDifferentialGearSetCompoundParametricStudyTool"],
        "_4456": ["BevelDifferentialPlanetGearCompoundParametricStudyTool"],
        "_4457": ["BevelDifferentialSunGearCompoundParametricStudyTool"],
        "_4458": ["BevelGearCompoundParametricStudyTool"],
        "_4459": ["BevelGearMeshCompoundParametricStudyTool"],
        "_4460": ["BevelGearSetCompoundParametricStudyTool"],
        "_4461": ["BoltCompoundParametricStudyTool"],
        "_4462": ["BoltedJointCompoundParametricStudyTool"],
        "_4463": ["ClutchCompoundParametricStudyTool"],
        "_4464": ["ClutchConnectionCompoundParametricStudyTool"],
        "_4465": ["ClutchHalfCompoundParametricStudyTool"],
        "_4466": ["CoaxialConnectionCompoundParametricStudyTool"],
        "_4467": ["ComponentCompoundParametricStudyTool"],
        "_4468": ["ConceptCouplingCompoundParametricStudyTool"],
        "_4469": ["ConceptCouplingConnectionCompoundParametricStudyTool"],
        "_4470": ["ConceptCouplingHalfCompoundParametricStudyTool"],
        "_4471": ["ConceptGearCompoundParametricStudyTool"],
        "_4472": ["ConceptGearMeshCompoundParametricStudyTool"],
        "_4473": ["ConceptGearSetCompoundParametricStudyTool"],
        "_4474": ["ConicalGearCompoundParametricStudyTool"],
        "_4475": ["ConicalGearMeshCompoundParametricStudyTool"],
        "_4476": ["ConicalGearSetCompoundParametricStudyTool"],
        "_4477": ["ConnectionCompoundParametricStudyTool"],
        "_4478": ["ConnectorCompoundParametricStudyTool"],
        "_4479": ["CouplingCompoundParametricStudyTool"],
        "_4480": ["CouplingConnectionCompoundParametricStudyTool"],
        "_4481": ["CouplingHalfCompoundParametricStudyTool"],
        "_4482": ["CVTBeltConnectionCompoundParametricStudyTool"],
        "_4483": ["CVTCompoundParametricStudyTool"],
        "_4484": ["CVTPulleyCompoundParametricStudyTool"],
        "_4485": ["CycloidalAssemblyCompoundParametricStudyTool"],
        "_4486": ["CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool"],
        "_4487": ["CycloidalDiscCompoundParametricStudyTool"],
        "_4488": ["CycloidalDiscPlanetaryBearingConnectionCompoundParametricStudyTool"],
        "_4489": ["CylindricalGearCompoundParametricStudyTool"],
        "_4490": ["CylindricalGearMeshCompoundParametricStudyTool"],
        "_4491": ["CylindricalGearSetCompoundParametricStudyTool"],
        "_4492": ["CylindricalPlanetGearCompoundParametricStudyTool"],
        "_4493": ["DatumCompoundParametricStudyTool"],
        "_4494": ["ExternalCADModelCompoundParametricStudyTool"],
        "_4495": ["FaceGearCompoundParametricStudyTool"],
        "_4496": ["FaceGearMeshCompoundParametricStudyTool"],
        "_4497": ["FaceGearSetCompoundParametricStudyTool"],
        "_4498": ["FEPartCompoundParametricStudyTool"],
        "_4499": ["FlexiblePinAssemblyCompoundParametricStudyTool"],
        "_4500": ["GearCompoundParametricStudyTool"],
        "_4501": ["GearMeshCompoundParametricStudyTool"],
        "_4502": ["GearSetCompoundParametricStudyTool"],
        "_4503": ["GuideDxfModelCompoundParametricStudyTool"],
        "_4504": ["HypoidGearCompoundParametricStudyTool"],
        "_4505": ["HypoidGearMeshCompoundParametricStudyTool"],
        "_4506": ["HypoidGearSetCompoundParametricStudyTool"],
        "_4507": ["InterMountableComponentConnectionCompoundParametricStudyTool"],
        "_4508": ["KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool"],
        "_4509": ["KlingelnbergCycloPalloidConicalGearMeshCompoundParametricStudyTool"],
        "_4510": ["KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool"],
        "_4511": ["KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool"],
        "_4512": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundParametricStudyTool"],
        "_4513": ["KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool"],
        "_4514": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool"],
        "_4515": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundParametricStudyTool"
        ],
        "_4516": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool"
        ],
        "_4517": ["MassDiscCompoundParametricStudyTool"],
        "_4518": ["MeasurementComponentCompoundParametricStudyTool"],
        "_4519": ["MountableComponentCompoundParametricStudyTool"],
        "_4520": ["OilSealCompoundParametricStudyTool"],
        "_4521": ["PartCompoundParametricStudyTool"],
        "_4522": ["PartToPartShearCouplingCompoundParametricStudyTool"],
        "_4523": ["PartToPartShearCouplingConnectionCompoundParametricStudyTool"],
        "_4524": ["PartToPartShearCouplingHalfCompoundParametricStudyTool"],
        "_4525": ["PlanetaryConnectionCompoundParametricStudyTool"],
        "_4526": ["PlanetaryGearSetCompoundParametricStudyTool"],
        "_4527": ["PlanetCarrierCompoundParametricStudyTool"],
        "_4528": ["PointLoadCompoundParametricStudyTool"],
        "_4529": ["PowerLoadCompoundParametricStudyTool"],
        "_4530": ["PulleyCompoundParametricStudyTool"],
        "_4531": ["RingPinsCompoundParametricStudyTool"],
        "_4532": ["RingPinsToDiscConnectionCompoundParametricStudyTool"],
        "_4533": ["RollingRingAssemblyCompoundParametricStudyTool"],
        "_4534": ["RollingRingCompoundParametricStudyTool"],
        "_4535": ["RollingRingConnectionCompoundParametricStudyTool"],
        "_4536": ["RootAssemblyCompoundParametricStudyTool"],
        "_4537": ["ShaftCompoundParametricStudyTool"],
        "_4538": ["ShaftHubConnectionCompoundParametricStudyTool"],
        "_4539": ["ShaftToMountableComponentConnectionCompoundParametricStudyTool"],
        "_4540": ["SpecialisedAssemblyCompoundParametricStudyTool"],
        "_4541": ["SpiralBevelGearCompoundParametricStudyTool"],
        "_4542": ["SpiralBevelGearMeshCompoundParametricStudyTool"],
        "_4543": ["SpiralBevelGearSetCompoundParametricStudyTool"],
        "_4544": ["SpringDamperCompoundParametricStudyTool"],
        "_4545": ["SpringDamperConnectionCompoundParametricStudyTool"],
        "_4546": ["SpringDamperHalfCompoundParametricStudyTool"],
        "_4547": ["StraightBevelDiffGearCompoundParametricStudyTool"],
        "_4548": ["StraightBevelDiffGearMeshCompoundParametricStudyTool"],
        "_4549": ["StraightBevelDiffGearSetCompoundParametricStudyTool"],
        "_4550": ["StraightBevelGearCompoundParametricStudyTool"],
        "_4551": ["StraightBevelGearMeshCompoundParametricStudyTool"],
        "_4552": ["StraightBevelGearSetCompoundParametricStudyTool"],
        "_4553": ["StraightBevelPlanetGearCompoundParametricStudyTool"],
        "_4554": ["StraightBevelSunGearCompoundParametricStudyTool"],
        "_4555": ["SynchroniserCompoundParametricStudyTool"],
        "_4556": ["SynchroniserHalfCompoundParametricStudyTool"],
        "_4557": ["SynchroniserPartCompoundParametricStudyTool"],
        "_4558": ["SynchroniserSleeveCompoundParametricStudyTool"],
        "_4559": ["TorqueConverterCompoundParametricStudyTool"],
        "_4560": ["TorqueConverterConnectionCompoundParametricStudyTool"],
        "_4561": ["TorqueConverterPumpCompoundParametricStudyTool"],
        "_4562": ["TorqueConverterTurbineCompoundParametricStudyTool"],
        "_4563": ["UnbalancedMassCompoundParametricStudyTool"],
        "_4564": ["VirtualComponentCompoundParametricStudyTool"],
        "_4565": ["WormGearCompoundParametricStudyTool"],
        "_4566": ["WormGearMeshCompoundParametricStudyTool"],
        "_4567": ["WormGearSetCompoundParametricStudyTool"],
        "_4568": ["ZerolBevelGearCompoundParametricStudyTool"],
        "_4569": ["ZerolBevelGearMeshCompoundParametricStudyTool"],
        "_4570": ["ZerolBevelGearSetCompoundParametricStudyTool"],
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

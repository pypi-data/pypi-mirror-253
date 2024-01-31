"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3375 import AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3376 import AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3377 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3378 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3379 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3380 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3381 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3382 import AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3383 import BearingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3384 import BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3385 import BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3386 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3387 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3388 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3389 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3390 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3391 import BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3392 import BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3393 import BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3394 import BoltCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3395 import BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3396 import ClutchCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3397 import ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3398 import ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3399 import CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3400 import ComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3401 import ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3402 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3403 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3404 import ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3405 import ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3406 import ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3407 import ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3408 import ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3409 import ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3410 import ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3411 import ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3412 import CouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3413 import CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3414 import CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3415 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3416 import CVTCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3417 import CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3418 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3419 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3420 import CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3421 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3422 import CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3423 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3424 import CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3425 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3426 import DatumCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3427 import ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3428 import FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3429 import FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3430 import FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3431 import FEPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3432 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3433 import GearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3434 import GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3435 import GearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3436 import GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3437 import HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3438 import HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3439 import HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3440 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3441 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3442 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3443 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3444 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3445 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3446 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3447 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3448 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3449 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3450 import MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3451 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3452 import MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3453 import OilSealCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3454 import PartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3455 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3456 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3457 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3458 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3459 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3460 import PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3461 import PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3462 import PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3463 import PulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3464 import RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3465 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3466 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3467 import RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3468 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3469 import RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3470 import ShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3471 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3472 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3473 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3474 import SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3475 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3476 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3477 import SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3478 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3479 import SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3480 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3481 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3482 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3483 import StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3484 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3485 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3486 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3487 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3488 import SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3489 import SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3490 import SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3491 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3492 import TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3493 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3494 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3495 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3496 import UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3497 import VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3498 import WormGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3499 import WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3500 import WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3501 import ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3502 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3503 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
else:
    import_structure = {
        "_3375": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3376": ["AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3377": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3378": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3379": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3380": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3381": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3382": ["AssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3383": ["BearingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3384": ["BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3385": ["BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3386": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3387": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3388": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3389": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3390": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3391": ["BevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3392": ["BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3393": ["BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3394": ["BoltCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3395": ["BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3396": ["ClutchCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3397": ["ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3398": ["ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3399": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3400": ["ComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3401": ["ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3402": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3403": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3404": ["ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3405": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3406": ["ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3407": ["ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3408": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3409": ["ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3410": ["ConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3411": ["ConnectorCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3412": ["CouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3413": ["CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3414": ["CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3415": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3416": ["CVTCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3417": ["CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3418": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3419": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3420": ["CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3421": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3422": ["CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3423": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3424": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3425": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3426": ["DatumCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3427": ["ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3428": ["FaceGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3429": ["FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3430": ["FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3431": ["FEPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3432": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3433": ["GearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3434": ["GearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3435": ["GearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3436": ["GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3437": ["HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3438": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3439": ["HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3440": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3441": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3442": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3443": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3444": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3445": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3446": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3447": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3448": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3449": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3450": ["MassDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3451": ["MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3452": ["MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3453": ["OilSealCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3454": ["PartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3455": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3456": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3457": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3458": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3459": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3460": ["PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3461": ["PointLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3462": ["PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3463": ["PulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3464": ["RingPinsCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3465": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3466": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3467": ["RollingRingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3468": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3469": ["RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3470": ["ShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3471": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3472": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3473": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3474": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3475": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3476": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3477": ["SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3478": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3479": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3480": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3481": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3482": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3483": ["StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3484": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3485": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3486": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3487": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3488": ["SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3489": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3490": ["SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3491": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3492": ["TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3493": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3494": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3495": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3496": ["UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3497": ["VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3498": ["WormGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3499": ["WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3500": ["WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3501": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3502": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3503": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "AssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "BearingCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "DatumCompoundSteadyStateSynchronousResponseOnAShaft",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "FEPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "MassDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "OilSealCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft",
    "PointLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft",
    "VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)

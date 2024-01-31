"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3634 import AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3635 import AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3636 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3637 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3638 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3639 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3640 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3641 import AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3642 import BearingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3643 import BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3644 import BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3645 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3646 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3647 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3648 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3649 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3650 import BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3651 import BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3652 import BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3653 import BoltCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3654 import BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3655 import ClutchCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3656 import ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3657 import ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3658 import CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3659 import ComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3660 import ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3661 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3662 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3663 import ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3664 import ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3665 import ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3666 import ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3667 import ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3668 import ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3669 import ConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3670 import ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3671 import CouplingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3672 import CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3673 import CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3674 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3675 import CVTCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3676 import CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3677 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3678 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3679 import CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3680 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3681 import CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3682 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3683 import CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3684 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3685 import DatumCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3686 import ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3687 import FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3688 import FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3689 import FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3690 import FEPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3691 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3692 import GearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3693 import GearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3694 import GearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3695 import GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3696 import HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3697 import HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3698 import HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3699 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3700 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3701 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3702 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3703 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3704 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3705 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3706 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3707 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3708 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3709 import MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3710 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3711 import MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3712 import OilSealCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3713 import PartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3714 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3715 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3716 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3717 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3718 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3719 import PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3720 import PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3721 import PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3722 import PulleyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3723 import RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3724 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3725 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3726 import RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3727 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3728 import RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3729 import ShaftCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3730 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3731 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3732 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3733 import SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3734 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3735 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3736 import SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3737 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3738 import SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3739 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3740 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3741 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3742 import StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3743 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3744 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3745 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3746 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3747 import SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3748 import SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3749 import SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3750 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3751 import TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3752 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3753 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3754 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from ._3755 import UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3756 import VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3757 import WormGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3758 import WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3759 import WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3760 import ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3761 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed
    from ._3762 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
else:
    import_structure = {
        "_3634": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3635": ["AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3636": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3637": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3638": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3639": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3640": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3641": ["AssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3642": ["BearingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3643": ["BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3644": ["BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3645": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3646": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3647": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3648": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3649": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3650": ["BevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3651": ["BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3652": ["BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3653": ["BoltCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3654": ["BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3655": ["ClutchCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3656": ["ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3657": ["ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3658": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3659": ["ComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3660": ["ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3661": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3662": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3663": ["ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3664": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3665": ["ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3666": ["ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3667": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3668": ["ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3669": ["ConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3670": ["ConnectorCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3671": ["CouplingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3672": ["CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3673": ["CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3674": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3675": ["CVTCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3676": ["CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3677": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3678": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3679": ["CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3680": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3681": ["CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3682": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3683": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3684": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3685": ["DatumCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3686": ["ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3687": ["FaceGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3688": ["FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3689": ["FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3690": ["FEPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3691": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3692": ["GearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3693": ["GearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3694": ["GearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3695": ["GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3696": ["HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3697": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3698": ["HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3699": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3700": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3701": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3702": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3703": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3704": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3705": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3706": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3707": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3708": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3709": ["MassDiscCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3710": ["MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3711": ["MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3712": ["OilSealCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3713": ["PartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3714": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3715": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3716": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3717": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3718": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3719": ["PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3720": ["PointLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3721": ["PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3722": ["PulleyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3723": ["RingPinsCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3724": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3725": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3726": ["RollingRingCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3727": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3728": ["RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3729": ["ShaftCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3730": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3731": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3732": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3733": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3734": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3735": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3736": ["SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3737": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3738": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3739": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3740": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3741": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3742": ["StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3743": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3744": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3745": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3746": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3747": ["SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3748": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3749": ["SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3750": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3751": ["TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3752": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3753": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3754": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_3755": ["UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3756": ["VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3757": ["WormGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3758": ["WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3759": ["WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3760": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3761": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed"],
        "_3762": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "AssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "BearingCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltCompoundSteadyStateSynchronousResponseAtASpeed",
    "BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ConnectorCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTCompoundSteadyStateSynchronousResponseAtASpeed",
    "CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "DatumCompoundSteadyStateSynchronousResponseAtASpeed",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "FEPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "GearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "MassDiscCompoundSteadyStateSynchronousResponseAtASpeed",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "OilSealCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed",
    "PointLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed",
    "PulleyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsCompoundSteadyStateSynchronousResponseAtASpeed",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingCompoundSteadyStateSynchronousResponseAtASpeed",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed",
    "VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)

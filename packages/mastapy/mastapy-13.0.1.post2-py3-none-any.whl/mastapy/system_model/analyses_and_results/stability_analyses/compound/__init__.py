"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3897 import AbstractAssemblyCompoundStabilityAnalysis
    from ._3898 import AbstractShaftCompoundStabilityAnalysis
    from ._3899 import AbstractShaftOrHousingCompoundStabilityAnalysis
    from ._3900 import (
        AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis,
    )
    from ._3901 import AGMAGleasonConicalGearCompoundStabilityAnalysis
    from ._3902 import AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
    from ._3903 import AGMAGleasonConicalGearSetCompoundStabilityAnalysis
    from ._3904 import AssemblyCompoundStabilityAnalysis
    from ._3905 import BearingCompoundStabilityAnalysis
    from ._3906 import BeltConnectionCompoundStabilityAnalysis
    from ._3907 import BeltDriveCompoundStabilityAnalysis
    from ._3908 import BevelDifferentialGearCompoundStabilityAnalysis
    from ._3909 import BevelDifferentialGearMeshCompoundStabilityAnalysis
    from ._3910 import BevelDifferentialGearSetCompoundStabilityAnalysis
    from ._3911 import BevelDifferentialPlanetGearCompoundStabilityAnalysis
    from ._3912 import BevelDifferentialSunGearCompoundStabilityAnalysis
    from ._3913 import BevelGearCompoundStabilityAnalysis
    from ._3914 import BevelGearMeshCompoundStabilityAnalysis
    from ._3915 import BevelGearSetCompoundStabilityAnalysis
    from ._3916 import BoltCompoundStabilityAnalysis
    from ._3917 import BoltedJointCompoundStabilityAnalysis
    from ._3918 import ClutchCompoundStabilityAnalysis
    from ._3919 import ClutchConnectionCompoundStabilityAnalysis
    from ._3920 import ClutchHalfCompoundStabilityAnalysis
    from ._3921 import CoaxialConnectionCompoundStabilityAnalysis
    from ._3922 import ComponentCompoundStabilityAnalysis
    from ._3923 import ConceptCouplingCompoundStabilityAnalysis
    from ._3924 import ConceptCouplingConnectionCompoundStabilityAnalysis
    from ._3925 import ConceptCouplingHalfCompoundStabilityAnalysis
    from ._3926 import ConceptGearCompoundStabilityAnalysis
    from ._3927 import ConceptGearMeshCompoundStabilityAnalysis
    from ._3928 import ConceptGearSetCompoundStabilityAnalysis
    from ._3929 import ConicalGearCompoundStabilityAnalysis
    from ._3930 import ConicalGearMeshCompoundStabilityAnalysis
    from ._3931 import ConicalGearSetCompoundStabilityAnalysis
    from ._3932 import ConnectionCompoundStabilityAnalysis
    from ._3933 import ConnectorCompoundStabilityAnalysis
    from ._3934 import CouplingCompoundStabilityAnalysis
    from ._3935 import CouplingConnectionCompoundStabilityAnalysis
    from ._3936 import CouplingHalfCompoundStabilityAnalysis
    from ._3937 import CVTBeltConnectionCompoundStabilityAnalysis
    from ._3938 import CVTCompoundStabilityAnalysis
    from ._3939 import CVTPulleyCompoundStabilityAnalysis
    from ._3940 import CycloidalAssemblyCompoundStabilityAnalysis
    from ._3941 import CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
    from ._3942 import CycloidalDiscCompoundStabilityAnalysis
    from ._3943 import CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
    from ._3944 import CylindricalGearCompoundStabilityAnalysis
    from ._3945 import CylindricalGearMeshCompoundStabilityAnalysis
    from ._3946 import CylindricalGearSetCompoundStabilityAnalysis
    from ._3947 import CylindricalPlanetGearCompoundStabilityAnalysis
    from ._3948 import DatumCompoundStabilityAnalysis
    from ._3949 import ExternalCADModelCompoundStabilityAnalysis
    from ._3950 import FaceGearCompoundStabilityAnalysis
    from ._3951 import FaceGearMeshCompoundStabilityAnalysis
    from ._3952 import FaceGearSetCompoundStabilityAnalysis
    from ._3953 import FEPartCompoundStabilityAnalysis
    from ._3954 import FlexiblePinAssemblyCompoundStabilityAnalysis
    from ._3955 import GearCompoundStabilityAnalysis
    from ._3956 import GearMeshCompoundStabilityAnalysis
    from ._3957 import GearSetCompoundStabilityAnalysis
    from ._3958 import GuideDxfModelCompoundStabilityAnalysis
    from ._3959 import HypoidGearCompoundStabilityAnalysis
    from ._3960 import HypoidGearMeshCompoundStabilityAnalysis
    from ._3961 import HypoidGearSetCompoundStabilityAnalysis
    from ._3962 import InterMountableComponentConnectionCompoundStabilityAnalysis
    from ._3963 import KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
    from ._3964 import KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
    from ._3965 import KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
    from ._3966 import KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
    from ._3967 import KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
    from ._3968 import KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
    from ._3969 import KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
    from ._3970 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis,
    )
    from ._3971 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis,
    )
    from ._3972 import MassDiscCompoundStabilityAnalysis
    from ._3973 import MeasurementComponentCompoundStabilityAnalysis
    from ._3974 import MountableComponentCompoundStabilityAnalysis
    from ._3975 import OilSealCompoundStabilityAnalysis
    from ._3976 import PartCompoundStabilityAnalysis
    from ._3977 import PartToPartShearCouplingCompoundStabilityAnalysis
    from ._3978 import PartToPartShearCouplingConnectionCompoundStabilityAnalysis
    from ._3979 import PartToPartShearCouplingHalfCompoundStabilityAnalysis
    from ._3980 import PlanetaryConnectionCompoundStabilityAnalysis
    from ._3981 import PlanetaryGearSetCompoundStabilityAnalysis
    from ._3982 import PlanetCarrierCompoundStabilityAnalysis
    from ._3983 import PointLoadCompoundStabilityAnalysis
    from ._3984 import PowerLoadCompoundStabilityAnalysis
    from ._3985 import PulleyCompoundStabilityAnalysis
    from ._3986 import RingPinsCompoundStabilityAnalysis
    from ._3987 import RingPinsToDiscConnectionCompoundStabilityAnalysis
    from ._3988 import RollingRingAssemblyCompoundStabilityAnalysis
    from ._3989 import RollingRingCompoundStabilityAnalysis
    from ._3990 import RollingRingConnectionCompoundStabilityAnalysis
    from ._3991 import RootAssemblyCompoundStabilityAnalysis
    from ._3992 import ShaftCompoundStabilityAnalysis
    from ._3993 import ShaftHubConnectionCompoundStabilityAnalysis
    from ._3994 import ShaftToMountableComponentConnectionCompoundStabilityAnalysis
    from ._3995 import SpecialisedAssemblyCompoundStabilityAnalysis
    from ._3996 import SpiralBevelGearCompoundStabilityAnalysis
    from ._3997 import SpiralBevelGearMeshCompoundStabilityAnalysis
    from ._3998 import SpiralBevelGearSetCompoundStabilityAnalysis
    from ._3999 import SpringDamperCompoundStabilityAnalysis
    from ._4000 import SpringDamperConnectionCompoundStabilityAnalysis
    from ._4001 import SpringDamperHalfCompoundStabilityAnalysis
    from ._4002 import StraightBevelDiffGearCompoundStabilityAnalysis
    from ._4003 import StraightBevelDiffGearMeshCompoundStabilityAnalysis
    from ._4004 import StraightBevelDiffGearSetCompoundStabilityAnalysis
    from ._4005 import StraightBevelGearCompoundStabilityAnalysis
    from ._4006 import StraightBevelGearMeshCompoundStabilityAnalysis
    from ._4007 import StraightBevelGearSetCompoundStabilityAnalysis
    from ._4008 import StraightBevelPlanetGearCompoundStabilityAnalysis
    from ._4009 import StraightBevelSunGearCompoundStabilityAnalysis
    from ._4010 import SynchroniserCompoundStabilityAnalysis
    from ._4011 import SynchroniserHalfCompoundStabilityAnalysis
    from ._4012 import SynchroniserPartCompoundStabilityAnalysis
    from ._4013 import SynchroniserSleeveCompoundStabilityAnalysis
    from ._4014 import TorqueConverterCompoundStabilityAnalysis
    from ._4015 import TorqueConverterConnectionCompoundStabilityAnalysis
    from ._4016 import TorqueConverterPumpCompoundStabilityAnalysis
    from ._4017 import TorqueConverterTurbineCompoundStabilityAnalysis
    from ._4018 import UnbalancedMassCompoundStabilityAnalysis
    from ._4019 import VirtualComponentCompoundStabilityAnalysis
    from ._4020 import WormGearCompoundStabilityAnalysis
    from ._4021 import WormGearMeshCompoundStabilityAnalysis
    from ._4022 import WormGearSetCompoundStabilityAnalysis
    from ._4023 import ZerolBevelGearCompoundStabilityAnalysis
    from ._4024 import ZerolBevelGearMeshCompoundStabilityAnalysis
    from ._4025 import ZerolBevelGearSetCompoundStabilityAnalysis
else:
    import_structure = {
        "_3897": ["AbstractAssemblyCompoundStabilityAnalysis"],
        "_3898": ["AbstractShaftCompoundStabilityAnalysis"],
        "_3899": ["AbstractShaftOrHousingCompoundStabilityAnalysis"],
        "_3900": [
            "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ],
        "_3901": ["AGMAGleasonConicalGearCompoundStabilityAnalysis"],
        "_3902": ["AGMAGleasonConicalGearMeshCompoundStabilityAnalysis"],
        "_3903": ["AGMAGleasonConicalGearSetCompoundStabilityAnalysis"],
        "_3904": ["AssemblyCompoundStabilityAnalysis"],
        "_3905": ["BearingCompoundStabilityAnalysis"],
        "_3906": ["BeltConnectionCompoundStabilityAnalysis"],
        "_3907": ["BeltDriveCompoundStabilityAnalysis"],
        "_3908": ["BevelDifferentialGearCompoundStabilityAnalysis"],
        "_3909": ["BevelDifferentialGearMeshCompoundStabilityAnalysis"],
        "_3910": ["BevelDifferentialGearSetCompoundStabilityAnalysis"],
        "_3911": ["BevelDifferentialPlanetGearCompoundStabilityAnalysis"],
        "_3912": ["BevelDifferentialSunGearCompoundStabilityAnalysis"],
        "_3913": ["BevelGearCompoundStabilityAnalysis"],
        "_3914": ["BevelGearMeshCompoundStabilityAnalysis"],
        "_3915": ["BevelGearSetCompoundStabilityAnalysis"],
        "_3916": ["BoltCompoundStabilityAnalysis"],
        "_3917": ["BoltedJointCompoundStabilityAnalysis"],
        "_3918": ["ClutchCompoundStabilityAnalysis"],
        "_3919": ["ClutchConnectionCompoundStabilityAnalysis"],
        "_3920": ["ClutchHalfCompoundStabilityAnalysis"],
        "_3921": ["CoaxialConnectionCompoundStabilityAnalysis"],
        "_3922": ["ComponentCompoundStabilityAnalysis"],
        "_3923": ["ConceptCouplingCompoundStabilityAnalysis"],
        "_3924": ["ConceptCouplingConnectionCompoundStabilityAnalysis"],
        "_3925": ["ConceptCouplingHalfCompoundStabilityAnalysis"],
        "_3926": ["ConceptGearCompoundStabilityAnalysis"],
        "_3927": ["ConceptGearMeshCompoundStabilityAnalysis"],
        "_3928": ["ConceptGearSetCompoundStabilityAnalysis"],
        "_3929": ["ConicalGearCompoundStabilityAnalysis"],
        "_3930": ["ConicalGearMeshCompoundStabilityAnalysis"],
        "_3931": ["ConicalGearSetCompoundStabilityAnalysis"],
        "_3932": ["ConnectionCompoundStabilityAnalysis"],
        "_3933": ["ConnectorCompoundStabilityAnalysis"],
        "_3934": ["CouplingCompoundStabilityAnalysis"],
        "_3935": ["CouplingConnectionCompoundStabilityAnalysis"],
        "_3936": ["CouplingHalfCompoundStabilityAnalysis"],
        "_3937": ["CVTBeltConnectionCompoundStabilityAnalysis"],
        "_3938": ["CVTCompoundStabilityAnalysis"],
        "_3939": ["CVTPulleyCompoundStabilityAnalysis"],
        "_3940": ["CycloidalAssemblyCompoundStabilityAnalysis"],
        "_3941": ["CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis"],
        "_3942": ["CycloidalDiscCompoundStabilityAnalysis"],
        "_3943": ["CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis"],
        "_3944": ["CylindricalGearCompoundStabilityAnalysis"],
        "_3945": ["CylindricalGearMeshCompoundStabilityAnalysis"],
        "_3946": ["CylindricalGearSetCompoundStabilityAnalysis"],
        "_3947": ["CylindricalPlanetGearCompoundStabilityAnalysis"],
        "_3948": ["DatumCompoundStabilityAnalysis"],
        "_3949": ["ExternalCADModelCompoundStabilityAnalysis"],
        "_3950": ["FaceGearCompoundStabilityAnalysis"],
        "_3951": ["FaceGearMeshCompoundStabilityAnalysis"],
        "_3952": ["FaceGearSetCompoundStabilityAnalysis"],
        "_3953": ["FEPartCompoundStabilityAnalysis"],
        "_3954": ["FlexiblePinAssemblyCompoundStabilityAnalysis"],
        "_3955": ["GearCompoundStabilityAnalysis"],
        "_3956": ["GearMeshCompoundStabilityAnalysis"],
        "_3957": ["GearSetCompoundStabilityAnalysis"],
        "_3958": ["GuideDxfModelCompoundStabilityAnalysis"],
        "_3959": ["HypoidGearCompoundStabilityAnalysis"],
        "_3960": ["HypoidGearMeshCompoundStabilityAnalysis"],
        "_3961": ["HypoidGearSetCompoundStabilityAnalysis"],
        "_3962": ["InterMountableComponentConnectionCompoundStabilityAnalysis"],
        "_3963": ["KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis"],
        "_3964": ["KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis"],
        "_3965": ["KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis"],
        "_3966": ["KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis"],
        "_3967": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis"],
        "_3968": ["KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis"],
        "_3969": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis"],
        "_3970": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ],
        "_3971": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ],
        "_3972": ["MassDiscCompoundStabilityAnalysis"],
        "_3973": ["MeasurementComponentCompoundStabilityAnalysis"],
        "_3974": ["MountableComponentCompoundStabilityAnalysis"],
        "_3975": ["OilSealCompoundStabilityAnalysis"],
        "_3976": ["PartCompoundStabilityAnalysis"],
        "_3977": ["PartToPartShearCouplingCompoundStabilityAnalysis"],
        "_3978": ["PartToPartShearCouplingConnectionCompoundStabilityAnalysis"],
        "_3979": ["PartToPartShearCouplingHalfCompoundStabilityAnalysis"],
        "_3980": ["PlanetaryConnectionCompoundStabilityAnalysis"],
        "_3981": ["PlanetaryGearSetCompoundStabilityAnalysis"],
        "_3982": ["PlanetCarrierCompoundStabilityAnalysis"],
        "_3983": ["PointLoadCompoundStabilityAnalysis"],
        "_3984": ["PowerLoadCompoundStabilityAnalysis"],
        "_3985": ["PulleyCompoundStabilityAnalysis"],
        "_3986": ["RingPinsCompoundStabilityAnalysis"],
        "_3987": ["RingPinsToDiscConnectionCompoundStabilityAnalysis"],
        "_3988": ["RollingRingAssemblyCompoundStabilityAnalysis"],
        "_3989": ["RollingRingCompoundStabilityAnalysis"],
        "_3990": ["RollingRingConnectionCompoundStabilityAnalysis"],
        "_3991": ["RootAssemblyCompoundStabilityAnalysis"],
        "_3992": ["ShaftCompoundStabilityAnalysis"],
        "_3993": ["ShaftHubConnectionCompoundStabilityAnalysis"],
        "_3994": ["ShaftToMountableComponentConnectionCompoundStabilityAnalysis"],
        "_3995": ["SpecialisedAssemblyCompoundStabilityAnalysis"],
        "_3996": ["SpiralBevelGearCompoundStabilityAnalysis"],
        "_3997": ["SpiralBevelGearMeshCompoundStabilityAnalysis"],
        "_3998": ["SpiralBevelGearSetCompoundStabilityAnalysis"],
        "_3999": ["SpringDamperCompoundStabilityAnalysis"],
        "_4000": ["SpringDamperConnectionCompoundStabilityAnalysis"],
        "_4001": ["SpringDamperHalfCompoundStabilityAnalysis"],
        "_4002": ["StraightBevelDiffGearCompoundStabilityAnalysis"],
        "_4003": ["StraightBevelDiffGearMeshCompoundStabilityAnalysis"],
        "_4004": ["StraightBevelDiffGearSetCompoundStabilityAnalysis"],
        "_4005": ["StraightBevelGearCompoundStabilityAnalysis"],
        "_4006": ["StraightBevelGearMeshCompoundStabilityAnalysis"],
        "_4007": ["StraightBevelGearSetCompoundStabilityAnalysis"],
        "_4008": ["StraightBevelPlanetGearCompoundStabilityAnalysis"],
        "_4009": ["StraightBevelSunGearCompoundStabilityAnalysis"],
        "_4010": ["SynchroniserCompoundStabilityAnalysis"],
        "_4011": ["SynchroniserHalfCompoundStabilityAnalysis"],
        "_4012": ["SynchroniserPartCompoundStabilityAnalysis"],
        "_4013": ["SynchroniserSleeveCompoundStabilityAnalysis"],
        "_4014": ["TorqueConverterCompoundStabilityAnalysis"],
        "_4015": ["TorqueConverterConnectionCompoundStabilityAnalysis"],
        "_4016": ["TorqueConverterPumpCompoundStabilityAnalysis"],
        "_4017": ["TorqueConverterTurbineCompoundStabilityAnalysis"],
        "_4018": ["UnbalancedMassCompoundStabilityAnalysis"],
        "_4019": ["VirtualComponentCompoundStabilityAnalysis"],
        "_4020": ["WormGearCompoundStabilityAnalysis"],
        "_4021": ["WormGearMeshCompoundStabilityAnalysis"],
        "_4022": ["WormGearSetCompoundStabilityAnalysis"],
        "_4023": ["ZerolBevelGearCompoundStabilityAnalysis"],
        "_4024": ["ZerolBevelGearMeshCompoundStabilityAnalysis"],
        "_4025": ["ZerolBevelGearSetCompoundStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundStabilityAnalysis",
    "AbstractShaftCompoundStabilityAnalysis",
    "AbstractShaftOrHousingCompoundStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearMeshCompoundStabilityAnalysis",
    "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
    "AssemblyCompoundStabilityAnalysis",
    "BearingCompoundStabilityAnalysis",
    "BeltConnectionCompoundStabilityAnalysis",
    "BeltDriveCompoundStabilityAnalysis",
    "BevelDifferentialGearCompoundStabilityAnalysis",
    "BevelDifferentialGearMeshCompoundStabilityAnalysis",
    "BevelDifferentialGearSetCompoundStabilityAnalysis",
    "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
    "BevelDifferentialSunGearCompoundStabilityAnalysis",
    "BevelGearCompoundStabilityAnalysis",
    "BevelGearMeshCompoundStabilityAnalysis",
    "BevelGearSetCompoundStabilityAnalysis",
    "BoltCompoundStabilityAnalysis",
    "BoltedJointCompoundStabilityAnalysis",
    "ClutchCompoundStabilityAnalysis",
    "ClutchConnectionCompoundStabilityAnalysis",
    "ClutchHalfCompoundStabilityAnalysis",
    "CoaxialConnectionCompoundStabilityAnalysis",
    "ComponentCompoundStabilityAnalysis",
    "ConceptCouplingCompoundStabilityAnalysis",
    "ConceptCouplingConnectionCompoundStabilityAnalysis",
    "ConceptCouplingHalfCompoundStabilityAnalysis",
    "ConceptGearCompoundStabilityAnalysis",
    "ConceptGearMeshCompoundStabilityAnalysis",
    "ConceptGearSetCompoundStabilityAnalysis",
    "ConicalGearCompoundStabilityAnalysis",
    "ConicalGearMeshCompoundStabilityAnalysis",
    "ConicalGearSetCompoundStabilityAnalysis",
    "ConnectionCompoundStabilityAnalysis",
    "ConnectorCompoundStabilityAnalysis",
    "CouplingCompoundStabilityAnalysis",
    "CouplingConnectionCompoundStabilityAnalysis",
    "CouplingHalfCompoundStabilityAnalysis",
    "CVTBeltConnectionCompoundStabilityAnalysis",
    "CVTCompoundStabilityAnalysis",
    "CVTPulleyCompoundStabilityAnalysis",
    "CycloidalAssemblyCompoundStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis",
    "CycloidalDiscCompoundStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis",
    "CylindricalGearCompoundStabilityAnalysis",
    "CylindricalGearMeshCompoundStabilityAnalysis",
    "CylindricalGearSetCompoundStabilityAnalysis",
    "CylindricalPlanetGearCompoundStabilityAnalysis",
    "DatumCompoundStabilityAnalysis",
    "ExternalCADModelCompoundStabilityAnalysis",
    "FaceGearCompoundStabilityAnalysis",
    "FaceGearMeshCompoundStabilityAnalysis",
    "FaceGearSetCompoundStabilityAnalysis",
    "FEPartCompoundStabilityAnalysis",
    "FlexiblePinAssemblyCompoundStabilityAnalysis",
    "GearCompoundStabilityAnalysis",
    "GearMeshCompoundStabilityAnalysis",
    "GearSetCompoundStabilityAnalysis",
    "GuideDxfModelCompoundStabilityAnalysis",
    "HypoidGearCompoundStabilityAnalysis",
    "HypoidGearMeshCompoundStabilityAnalysis",
    "HypoidGearSetCompoundStabilityAnalysis",
    "InterMountableComponentConnectionCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis",
    "MassDiscCompoundStabilityAnalysis",
    "MeasurementComponentCompoundStabilityAnalysis",
    "MountableComponentCompoundStabilityAnalysis",
    "OilSealCompoundStabilityAnalysis",
    "PartCompoundStabilityAnalysis",
    "PartToPartShearCouplingCompoundStabilityAnalysis",
    "PartToPartShearCouplingConnectionCompoundStabilityAnalysis",
    "PartToPartShearCouplingHalfCompoundStabilityAnalysis",
    "PlanetaryConnectionCompoundStabilityAnalysis",
    "PlanetaryGearSetCompoundStabilityAnalysis",
    "PlanetCarrierCompoundStabilityAnalysis",
    "PointLoadCompoundStabilityAnalysis",
    "PowerLoadCompoundStabilityAnalysis",
    "PulleyCompoundStabilityAnalysis",
    "RingPinsCompoundStabilityAnalysis",
    "RingPinsToDiscConnectionCompoundStabilityAnalysis",
    "RollingRingAssemblyCompoundStabilityAnalysis",
    "RollingRingCompoundStabilityAnalysis",
    "RollingRingConnectionCompoundStabilityAnalysis",
    "RootAssemblyCompoundStabilityAnalysis",
    "ShaftCompoundStabilityAnalysis",
    "ShaftHubConnectionCompoundStabilityAnalysis",
    "ShaftToMountableComponentConnectionCompoundStabilityAnalysis",
    "SpecialisedAssemblyCompoundStabilityAnalysis",
    "SpiralBevelGearCompoundStabilityAnalysis",
    "SpiralBevelGearMeshCompoundStabilityAnalysis",
    "SpiralBevelGearSetCompoundStabilityAnalysis",
    "SpringDamperCompoundStabilityAnalysis",
    "SpringDamperConnectionCompoundStabilityAnalysis",
    "SpringDamperHalfCompoundStabilityAnalysis",
    "StraightBevelDiffGearCompoundStabilityAnalysis",
    "StraightBevelDiffGearMeshCompoundStabilityAnalysis",
    "StraightBevelDiffGearSetCompoundStabilityAnalysis",
    "StraightBevelGearCompoundStabilityAnalysis",
    "StraightBevelGearMeshCompoundStabilityAnalysis",
    "StraightBevelGearSetCompoundStabilityAnalysis",
    "StraightBevelPlanetGearCompoundStabilityAnalysis",
    "StraightBevelSunGearCompoundStabilityAnalysis",
    "SynchroniserCompoundStabilityAnalysis",
    "SynchroniserHalfCompoundStabilityAnalysis",
    "SynchroniserPartCompoundStabilityAnalysis",
    "SynchroniserSleeveCompoundStabilityAnalysis",
    "TorqueConverterCompoundStabilityAnalysis",
    "TorqueConverterConnectionCompoundStabilityAnalysis",
    "TorqueConverterPumpCompoundStabilityAnalysis",
    "TorqueConverterTurbineCompoundStabilityAnalysis",
    "UnbalancedMassCompoundStabilityAnalysis",
    "VirtualComponentCompoundStabilityAnalysis",
    "WormGearCompoundStabilityAnalysis",
    "WormGearMeshCompoundStabilityAnalysis",
    "WormGearSetCompoundStabilityAnalysis",
    "ZerolBevelGearCompoundStabilityAnalysis",
    "ZerolBevelGearMeshCompoundStabilityAnalysis",
    "ZerolBevelGearSetCompoundStabilityAnalysis",
)

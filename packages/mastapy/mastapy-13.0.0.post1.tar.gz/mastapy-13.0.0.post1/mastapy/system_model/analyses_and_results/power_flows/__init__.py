"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4032 import AbstractAssemblyPowerFlow
    from ._4033 import AbstractShaftOrHousingPowerFlow
    from ._4034 import AbstractShaftPowerFlow
    from ._4035 import AbstractShaftToMountableComponentConnectionPowerFlow
    from ._4036 import AGMAGleasonConicalGearMeshPowerFlow
    from ._4037 import AGMAGleasonConicalGearPowerFlow
    from ._4038 import AGMAGleasonConicalGearSetPowerFlow
    from ._4039 import AssemblyPowerFlow
    from ._4040 import BearingPowerFlow
    from ._4041 import BeltConnectionPowerFlow
    from ._4042 import BeltDrivePowerFlow
    from ._4043 import BevelDifferentialGearMeshPowerFlow
    from ._4044 import BevelDifferentialGearPowerFlow
    from ._4045 import BevelDifferentialGearSetPowerFlow
    from ._4046 import BevelDifferentialPlanetGearPowerFlow
    from ._4047 import BevelDifferentialSunGearPowerFlow
    from ._4048 import BevelGearMeshPowerFlow
    from ._4049 import BevelGearPowerFlow
    from ._4050 import BevelGearSetPowerFlow
    from ._4051 import BoltedJointPowerFlow
    from ._4052 import BoltPowerFlow
    from ._4053 import ClutchConnectionPowerFlow
    from ._4054 import ClutchHalfPowerFlow
    from ._4055 import ClutchPowerFlow
    from ._4056 import CoaxialConnectionPowerFlow
    from ._4057 import ComponentPowerFlow
    from ._4058 import ConceptCouplingConnectionPowerFlow
    from ._4059 import ConceptCouplingHalfPowerFlow
    from ._4060 import ConceptCouplingPowerFlow
    from ._4061 import ConceptGearMeshPowerFlow
    from ._4062 import ConceptGearPowerFlow
    from ._4063 import ConceptGearSetPowerFlow
    from ._4064 import ConicalGearMeshPowerFlow
    from ._4065 import ConicalGearPowerFlow
    from ._4066 import ConicalGearSetPowerFlow
    from ._4067 import ConnectionPowerFlow
    from ._4068 import ConnectorPowerFlow
    from ._4069 import CouplingConnectionPowerFlow
    from ._4070 import CouplingHalfPowerFlow
    from ._4071 import CouplingPowerFlow
    from ._4072 import CVTBeltConnectionPowerFlow
    from ._4073 import CVTPowerFlow
    from ._4074 import CVTPulleyPowerFlow
    from ._4075 import CycloidalAssemblyPowerFlow
    from ._4076 import CycloidalDiscCentralBearingConnectionPowerFlow
    from ._4077 import CycloidalDiscPlanetaryBearingConnectionPowerFlow
    from ._4078 import CycloidalDiscPowerFlow
    from ._4079 import CylindricalGearGeometricEntityDrawStyle
    from ._4080 import CylindricalGearMeshPowerFlow
    from ._4081 import CylindricalGearPowerFlow
    from ._4082 import CylindricalGearSetPowerFlow
    from ._4083 import CylindricalPlanetGearPowerFlow
    from ._4084 import DatumPowerFlow
    from ._4085 import ExternalCADModelPowerFlow
    from ._4086 import FaceGearMeshPowerFlow
    from ._4087 import FaceGearPowerFlow
    from ._4088 import FaceGearSetPowerFlow
    from ._4089 import FastPowerFlowSolution
    from ._4090 import FEPartPowerFlow
    from ._4091 import FlexiblePinAssemblyPowerFlow
    from ._4092 import GearMeshPowerFlow
    from ._4093 import GearPowerFlow
    from ._4094 import GearSetPowerFlow
    from ._4095 import GuideDxfModelPowerFlow
    from ._4096 import HypoidGearMeshPowerFlow
    from ._4097 import HypoidGearPowerFlow
    from ._4098 import HypoidGearSetPowerFlow
    from ._4099 import InterMountableComponentConnectionPowerFlow
    from ._4100 import KlingelnbergCycloPalloidConicalGearMeshPowerFlow
    from ._4101 import KlingelnbergCycloPalloidConicalGearPowerFlow
    from ._4102 import KlingelnbergCycloPalloidConicalGearSetPowerFlow
    from ._4103 import KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
    from ._4104 import KlingelnbergCycloPalloidHypoidGearPowerFlow
    from ._4105 import KlingelnbergCycloPalloidHypoidGearSetPowerFlow
    from ._4106 import KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
    from ._4107 import KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
    from ._4108 import KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
    from ._4109 import MassDiscPowerFlow
    from ._4110 import MeasurementComponentPowerFlow
    from ._4111 import MountableComponentPowerFlow
    from ._4112 import OilSealPowerFlow
    from ._4113 import PartPowerFlow
    from ._4114 import PartToPartShearCouplingConnectionPowerFlow
    from ._4115 import PartToPartShearCouplingHalfPowerFlow
    from ._4116 import PartToPartShearCouplingPowerFlow
    from ._4117 import PlanetaryConnectionPowerFlow
    from ._4118 import PlanetaryGearSetPowerFlow
    from ._4119 import PlanetCarrierPowerFlow
    from ._4120 import PointLoadPowerFlow
    from ._4121 import PowerFlow
    from ._4122 import PowerFlowDrawStyle
    from ._4123 import PowerLoadPowerFlow
    from ._4124 import PulleyPowerFlow
    from ._4125 import RingPinsPowerFlow
    from ._4126 import RingPinsToDiscConnectionPowerFlow
    from ._4127 import RollingRingAssemblyPowerFlow
    from ._4128 import RollingRingConnectionPowerFlow
    from ._4129 import RollingRingPowerFlow
    from ._4130 import RootAssemblyPowerFlow
    from ._4131 import ShaftHubConnectionPowerFlow
    from ._4132 import ShaftPowerFlow
    from ._4133 import ShaftToMountableComponentConnectionPowerFlow
    from ._4134 import SpecialisedAssemblyPowerFlow
    from ._4135 import SpiralBevelGearMeshPowerFlow
    from ._4136 import SpiralBevelGearPowerFlow
    from ._4137 import SpiralBevelGearSetPowerFlow
    from ._4138 import SpringDamperConnectionPowerFlow
    from ._4139 import SpringDamperHalfPowerFlow
    from ._4140 import SpringDamperPowerFlow
    from ._4141 import StraightBevelDiffGearMeshPowerFlow
    from ._4142 import StraightBevelDiffGearPowerFlow
    from ._4143 import StraightBevelDiffGearSetPowerFlow
    from ._4144 import StraightBevelGearMeshPowerFlow
    from ._4145 import StraightBevelGearPowerFlow
    from ._4146 import StraightBevelGearSetPowerFlow
    from ._4147 import StraightBevelPlanetGearPowerFlow
    from ._4148 import StraightBevelSunGearPowerFlow
    from ._4149 import SynchroniserHalfPowerFlow
    from ._4150 import SynchroniserPartPowerFlow
    from ._4151 import SynchroniserPowerFlow
    from ._4152 import SynchroniserSleevePowerFlow
    from ._4153 import ToothPassingHarmonic
    from ._4154 import TorqueConverterConnectionPowerFlow
    from ._4155 import TorqueConverterPowerFlow
    from ._4156 import TorqueConverterPumpPowerFlow
    from ._4157 import TorqueConverterTurbinePowerFlow
    from ._4158 import UnbalancedMassPowerFlow
    from ._4159 import VirtualComponentPowerFlow
    from ._4160 import WormGearMeshPowerFlow
    from ._4161 import WormGearPowerFlow
    from ._4162 import WormGearSetPowerFlow
    from ._4163 import ZerolBevelGearMeshPowerFlow
    from ._4164 import ZerolBevelGearPowerFlow
    from ._4165 import ZerolBevelGearSetPowerFlow
else:
    import_structure = {
        "_4032": ["AbstractAssemblyPowerFlow"],
        "_4033": ["AbstractShaftOrHousingPowerFlow"],
        "_4034": ["AbstractShaftPowerFlow"],
        "_4035": ["AbstractShaftToMountableComponentConnectionPowerFlow"],
        "_4036": ["AGMAGleasonConicalGearMeshPowerFlow"],
        "_4037": ["AGMAGleasonConicalGearPowerFlow"],
        "_4038": ["AGMAGleasonConicalGearSetPowerFlow"],
        "_4039": ["AssemblyPowerFlow"],
        "_4040": ["BearingPowerFlow"],
        "_4041": ["BeltConnectionPowerFlow"],
        "_4042": ["BeltDrivePowerFlow"],
        "_4043": ["BevelDifferentialGearMeshPowerFlow"],
        "_4044": ["BevelDifferentialGearPowerFlow"],
        "_4045": ["BevelDifferentialGearSetPowerFlow"],
        "_4046": ["BevelDifferentialPlanetGearPowerFlow"],
        "_4047": ["BevelDifferentialSunGearPowerFlow"],
        "_4048": ["BevelGearMeshPowerFlow"],
        "_4049": ["BevelGearPowerFlow"],
        "_4050": ["BevelGearSetPowerFlow"],
        "_4051": ["BoltedJointPowerFlow"],
        "_4052": ["BoltPowerFlow"],
        "_4053": ["ClutchConnectionPowerFlow"],
        "_4054": ["ClutchHalfPowerFlow"],
        "_4055": ["ClutchPowerFlow"],
        "_4056": ["CoaxialConnectionPowerFlow"],
        "_4057": ["ComponentPowerFlow"],
        "_4058": ["ConceptCouplingConnectionPowerFlow"],
        "_4059": ["ConceptCouplingHalfPowerFlow"],
        "_4060": ["ConceptCouplingPowerFlow"],
        "_4061": ["ConceptGearMeshPowerFlow"],
        "_4062": ["ConceptGearPowerFlow"],
        "_4063": ["ConceptGearSetPowerFlow"],
        "_4064": ["ConicalGearMeshPowerFlow"],
        "_4065": ["ConicalGearPowerFlow"],
        "_4066": ["ConicalGearSetPowerFlow"],
        "_4067": ["ConnectionPowerFlow"],
        "_4068": ["ConnectorPowerFlow"],
        "_4069": ["CouplingConnectionPowerFlow"],
        "_4070": ["CouplingHalfPowerFlow"],
        "_4071": ["CouplingPowerFlow"],
        "_4072": ["CVTBeltConnectionPowerFlow"],
        "_4073": ["CVTPowerFlow"],
        "_4074": ["CVTPulleyPowerFlow"],
        "_4075": ["CycloidalAssemblyPowerFlow"],
        "_4076": ["CycloidalDiscCentralBearingConnectionPowerFlow"],
        "_4077": ["CycloidalDiscPlanetaryBearingConnectionPowerFlow"],
        "_4078": ["CycloidalDiscPowerFlow"],
        "_4079": ["CylindricalGearGeometricEntityDrawStyle"],
        "_4080": ["CylindricalGearMeshPowerFlow"],
        "_4081": ["CylindricalGearPowerFlow"],
        "_4082": ["CylindricalGearSetPowerFlow"],
        "_4083": ["CylindricalPlanetGearPowerFlow"],
        "_4084": ["DatumPowerFlow"],
        "_4085": ["ExternalCADModelPowerFlow"],
        "_4086": ["FaceGearMeshPowerFlow"],
        "_4087": ["FaceGearPowerFlow"],
        "_4088": ["FaceGearSetPowerFlow"],
        "_4089": ["FastPowerFlowSolution"],
        "_4090": ["FEPartPowerFlow"],
        "_4091": ["FlexiblePinAssemblyPowerFlow"],
        "_4092": ["GearMeshPowerFlow"],
        "_4093": ["GearPowerFlow"],
        "_4094": ["GearSetPowerFlow"],
        "_4095": ["GuideDxfModelPowerFlow"],
        "_4096": ["HypoidGearMeshPowerFlow"],
        "_4097": ["HypoidGearPowerFlow"],
        "_4098": ["HypoidGearSetPowerFlow"],
        "_4099": ["InterMountableComponentConnectionPowerFlow"],
        "_4100": ["KlingelnbergCycloPalloidConicalGearMeshPowerFlow"],
        "_4101": ["KlingelnbergCycloPalloidConicalGearPowerFlow"],
        "_4102": ["KlingelnbergCycloPalloidConicalGearSetPowerFlow"],
        "_4103": ["KlingelnbergCycloPalloidHypoidGearMeshPowerFlow"],
        "_4104": ["KlingelnbergCycloPalloidHypoidGearPowerFlow"],
        "_4105": ["KlingelnbergCycloPalloidHypoidGearSetPowerFlow"],
        "_4106": ["KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow"],
        "_4107": ["KlingelnbergCycloPalloidSpiralBevelGearPowerFlow"],
        "_4108": ["KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow"],
        "_4109": ["MassDiscPowerFlow"],
        "_4110": ["MeasurementComponentPowerFlow"],
        "_4111": ["MountableComponentPowerFlow"],
        "_4112": ["OilSealPowerFlow"],
        "_4113": ["PartPowerFlow"],
        "_4114": ["PartToPartShearCouplingConnectionPowerFlow"],
        "_4115": ["PartToPartShearCouplingHalfPowerFlow"],
        "_4116": ["PartToPartShearCouplingPowerFlow"],
        "_4117": ["PlanetaryConnectionPowerFlow"],
        "_4118": ["PlanetaryGearSetPowerFlow"],
        "_4119": ["PlanetCarrierPowerFlow"],
        "_4120": ["PointLoadPowerFlow"],
        "_4121": ["PowerFlow"],
        "_4122": ["PowerFlowDrawStyle"],
        "_4123": ["PowerLoadPowerFlow"],
        "_4124": ["PulleyPowerFlow"],
        "_4125": ["RingPinsPowerFlow"],
        "_4126": ["RingPinsToDiscConnectionPowerFlow"],
        "_4127": ["RollingRingAssemblyPowerFlow"],
        "_4128": ["RollingRingConnectionPowerFlow"],
        "_4129": ["RollingRingPowerFlow"],
        "_4130": ["RootAssemblyPowerFlow"],
        "_4131": ["ShaftHubConnectionPowerFlow"],
        "_4132": ["ShaftPowerFlow"],
        "_4133": ["ShaftToMountableComponentConnectionPowerFlow"],
        "_4134": ["SpecialisedAssemblyPowerFlow"],
        "_4135": ["SpiralBevelGearMeshPowerFlow"],
        "_4136": ["SpiralBevelGearPowerFlow"],
        "_4137": ["SpiralBevelGearSetPowerFlow"],
        "_4138": ["SpringDamperConnectionPowerFlow"],
        "_4139": ["SpringDamperHalfPowerFlow"],
        "_4140": ["SpringDamperPowerFlow"],
        "_4141": ["StraightBevelDiffGearMeshPowerFlow"],
        "_4142": ["StraightBevelDiffGearPowerFlow"],
        "_4143": ["StraightBevelDiffGearSetPowerFlow"],
        "_4144": ["StraightBevelGearMeshPowerFlow"],
        "_4145": ["StraightBevelGearPowerFlow"],
        "_4146": ["StraightBevelGearSetPowerFlow"],
        "_4147": ["StraightBevelPlanetGearPowerFlow"],
        "_4148": ["StraightBevelSunGearPowerFlow"],
        "_4149": ["SynchroniserHalfPowerFlow"],
        "_4150": ["SynchroniserPartPowerFlow"],
        "_4151": ["SynchroniserPowerFlow"],
        "_4152": ["SynchroniserSleevePowerFlow"],
        "_4153": ["ToothPassingHarmonic"],
        "_4154": ["TorqueConverterConnectionPowerFlow"],
        "_4155": ["TorqueConverterPowerFlow"],
        "_4156": ["TorqueConverterPumpPowerFlow"],
        "_4157": ["TorqueConverterTurbinePowerFlow"],
        "_4158": ["UnbalancedMassPowerFlow"],
        "_4159": ["VirtualComponentPowerFlow"],
        "_4160": ["WormGearMeshPowerFlow"],
        "_4161": ["WormGearPowerFlow"],
        "_4162": ["WormGearSetPowerFlow"],
        "_4163": ["ZerolBevelGearMeshPowerFlow"],
        "_4164": ["ZerolBevelGearPowerFlow"],
        "_4165": ["ZerolBevelGearSetPowerFlow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyPowerFlow",
    "AbstractShaftOrHousingPowerFlow",
    "AbstractShaftPowerFlow",
    "AbstractShaftToMountableComponentConnectionPowerFlow",
    "AGMAGleasonConicalGearMeshPowerFlow",
    "AGMAGleasonConicalGearPowerFlow",
    "AGMAGleasonConicalGearSetPowerFlow",
    "AssemblyPowerFlow",
    "BearingPowerFlow",
    "BeltConnectionPowerFlow",
    "BeltDrivePowerFlow",
    "BevelDifferentialGearMeshPowerFlow",
    "BevelDifferentialGearPowerFlow",
    "BevelDifferentialGearSetPowerFlow",
    "BevelDifferentialPlanetGearPowerFlow",
    "BevelDifferentialSunGearPowerFlow",
    "BevelGearMeshPowerFlow",
    "BevelGearPowerFlow",
    "BevelGearSetPowerFlow",
    "BoltedJointPowerFlow",
    "BoltPowerFlow",
    "ClutchConnectionPowerFlow",
    "ClutchHalfPowerFlow",
    "ClutchPowerFlow",
    "CoaxialConnectionPowerFlow",
    "ComponentPowerFlow",
    "ConceptCouplingConnectionPowerFlow",
    "ConceptCouplingHalfPowerFlow",
    "ConceptCouplingPowerFlow",
    "ConceptGearMeshPowerFlow",
    "ConceptGearPowerFlow",
    "ConceptGearSetPowerFlow",
    "ConicalGearMeshPowerFlow",
    "ConicalGearPowerFlow",
    "ConicalGearSetPowerFlow",
    "ConnectionPowerFlow",
    "ConnectorPowerFlow",
    "CouplingConnectionPowerFlow",
    "CouplingHalfPowerFlow",
    "CouplingPowerFlow",
    "CVTBeltConnectionPowerFlow",
    "CVTPowerFlow",
    "CVTPulleyPowerFlow",
    "CycloidalAssemblyPowerFlow",
    "CycloidalDiscCentralBearingConnectionPowerFlow",
    "CycloidalDiscPlanetaryBearingConnectionPowerFlow",
    "CycloidalDiscPowerFlow",
    "CylindricalGearGeometricEntityDrawStyle",
    "CylindricalGearMeshPowerFlow",
    "CylindricalGearPowerFlow",
    "CylindricalGearSetPowerFlow",
    "CylindricalPlanetGearPowerFlow",
    "DatumPowerFlow",
    "ExternalCADModelPowerFlow",
    "FaceGearMeshPowerFlow",
    "FaceGearPowerFlow",
    "FaceGearSetPowerFlow",
    "FastPowerFlowSolution",
    "FEPartPowerFlow",
    "FlexiblePinAssemblyPowerFlow",
    "GearMeshPowerFlow",
    "GearPowerFlow",
    "GearSetPowerFlow",
    "GuideDxfModelPowerFlow",
    "HypoidGearMeshPowerFlow",
    "HypoidGearPowerFlow",
    "HypoidGearSetPowerFlow",
    "InterMountableComponentConnectionPowerFlow",
    "KlingelnbergCycloPalloidConicalGearMeshPowerFlow",
    "KlingelnbergCycloPalloidConicalGearPowerFlow",
    "KlingelnbergCycloPalloidConicalGearSetPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearMeshPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearPowerFlow",
    "KlingelnbergCycloPalloidHypoidGearSetPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearPowerFlow",
    "KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow",
    "MassDiscPowerFlow",
    "MeasurementComponentPowerFlow",
    "MountableComponentPowerFlow",
    "OilSealPowerFlow",
    "PartPowerFlow",
    "PartToPartShearCouplingConnectionPowerFlow",
    "PartToPartShearCouplingHalfPowerFlow",
    "PartToPartShearCouplingPowerFlow",
    "PlanetaryConnectionPowerFlow",
    "PlanetaryGearSetPowerFlow",
    "PlanetCarrierPowerFlow",
    "PointLoadPowerFlow",
    "PowerFlow",
    "PowerFlowDrawStyle",
    "PowerLoadPowerFlow",
    "PulleyPowerFlow",
    "RingPinsPowerFlow",
    "RingPinsToDiscConnectionPowerFlow",
    "RollingRingAssemblyPowerFlow",
    "RollingRingConnectionPowerFlow",
    "RollingRingPowerFlow",
    "RootAssemblyPowerFlow",
    "ShaftHubConnectionPowerFlow",
    "ShaftPowerFlow",
    "ShaftToMountableComponentConnectionPowerFlow",
    "SpecialisedAssemblyPowerFlow",
    "SpiralBevelGearMeshPowerFlow",
    "SpiralBevelGearPowerFlow",
    "SpiralBevelGearSetPowerFlow",
    "SpringDamperConnectionPowerFlow",
    "SpringDamperHalfPowerFlow",
    "SpringDamperPowerFlow",
    "StraightBevelDiffGearMeshPowerFlow",
    "StraightBevelDiffGearPowerFlow",
    "StraightBevelDiffGearSetPowerFlow",
    "StraightBevelGearMeshPowerFlow",
    "StraightBevelGearPowerFlow",
    "StraightBevelGearSetPowerFlow",
    "StraightBevelPlanetGearPowerFlow",
    "StraightBevelSunGearPowerFlow",
    "SynchroniserHalfPowerFlow",
    "SynchroniserPartPowerFlow",
    "SynchroniserPowerFlow",
    "SynchroniserSleevePowerFlow",
    "ToothPassingHarmonic",
    "TorqueConverterConnectionPowerFlow",
    "TorqueConverterPowerFlow",
    "TorqueConverterPumpPowerFlow",
    "TorqueConverterTurbinePowerFlow",
    "UnbalancedMassPowerFlow",
    "VirtualComponentPowerFlow",
    "WormGearMeshPowerFlow",
    "WormGearPowerFlow",
    "WormGearSetPowerFlow",
    "ZerolBevelGearMeshPowerFlow",
    "ZerolBevelGearPowerFlow",
    "ZerolBevelGearSetPowerFlow",
)

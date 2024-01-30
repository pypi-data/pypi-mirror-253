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
    from ._4089 import FastPowerFlow
    from ._4090 import FastPowerFlowSolution
    from ._4091 import FEPartPowerFlow
    from ._4092 import FlexiblePinAssemblyPowerFlow
    from ._4093 import GearMeshPowerFlow
    from ._4094 import GearPowerFlow
    from ._4095 import GearSetPowerFlow
    from ._4096 import GuideDxfModelPowerFlow
    from ._4097 import HypoidGearMeshPowerFlow
    from ._4098 import HypoidGearPowerFlow
    from ._4099 import HypoidGearSetPowerFlow
    from ._4100 import InterMountableComponentConnectionPowerFlow
    from ._4101 import KlingelnbergCycloPalloidConicalGearMeshPowerFlow
    from ._4102 import KlingelnbergCycloPalloidConicalGearPowerFlow
    from ._4103 import KlingelnbergCycloPalloidConicalGearSetPowerFlow
    from ._4104 import KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
    from ._4105 import KlingelnbergCycloPalloidHypoidGearPowerFlow
    from ._4106 import KlingelnbergCycloPalloidHypoidGearSetPowerFlow
    from ._4107 import KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
    from ._4108 import KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
    from ._4109 import KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow
    from ._4110 import MassDiscPowerFlow
    from ._4111 import MeasurementComponentPowerFlow
    from ._4112 import MountableComponentPowerFlow
    from ._4113 import OilSealPowerFlow
    from ._4114 import PartPowerFlow
    from ._4115 import PartToPartShearCouplingConnectionPowerFlow
    from ._4116 import PartToPartShearCouplingHalfPowerFlow
    from ._4117 import PartToPartShearCouplingPowerFlow
    from ._4118 import PlanetaryConnectionPowerFlow
    from ._4119 import PlanetaryGearSetPowerFlow
    from ._4120 import PlanetCarrierPowerFlow
    from ._4121 import PointLoadPowerFlow
    from ._4122 import PowerFlow
    from ._4123 import PowerFlowDrawStyle
    from ._4124 import PowerLoadPowerFlow
    from ._4125 import PulleyPowerFlow
    from ._4126 import RingPinsPowerFlow
    from ._4127 import RingPinsToDiscConnectionPowerFlow
    from ._4128 import RollingRingAssemblyPowerFlow
    from ._4129 import RollingRingConnectionPowerFlow
    from ._4130 import RollingRingPowerFlow
    from ._4131 import RootAssemblyPowerFlow
    from ._4132 import ShaftHubConnectionPowerFlow
    from ._4133 import ShaftPowerFlow
    from ._4134 import ShaftToMountableComponentConnectionPowerFlow
    from ._4135 import SpecialisedAssemblyPowerFlow
    from ._4136 import SpiralBevelGearMeshPowerFlow
    from ._4137 import SpiralBevelGearPowerFlow
    from ._4138 import SpiralBevelGearSetPowerFlow
    from ._4139 import SpringDamperConnectionPowerFlow
    from ._4140 import SpringDamperHalfPowerFlow
    from ._4141 import SpringDamperPowerFlow
    from ._4142 import StraightBevelDiffGearMeshPowerFlow
    from ._4143 import StraightBevelDiffGearPowerFlow
    from ._4144 import StraightBevelDiffGearSetPowerFlow
    from ._4145 import StraightBevelGearMeshPowerFlow
    from ._4146 import StraightBevelGearPowerFlow
    from ._4147 import StraightBevelGearSetPowerFlow
    from ._4148 import StraightBevelPlanetGearPowerFlow
    from ._4149 import StraightBevelSunGearPowerFlow
    from ._4150 import SynchroniserHalfPowerFlow
    from ._4151 import SynchroniserPartPowerFlow
    from ._4152 import SynchroniserPowerFlow
    from ._4153 import SynchroniserSleevePowerFlow
    from ._4154 import ToothPassingHarmonic
    from ._4155 import TorqueConverterConnectionPowerFlow
    from ._4156 import TorqueConverterPowerFlow
    from ._4157 import TorqueConverterPumpPowerFlow
    from ._4158 import TorqueConverterTurbinePowerFlow
    from ._4159 import UnbalancedMassPowerFlow
    from ._4160 import VirtualComponentPowerFlow
    from ._4161 import WormGearMeshPowerFlow
    from ._4162 import WormGearPowerFlow
    from ._4163 import WormGearSetPowerFlow
    from ._4164 import ZerolBevelGearMeshPowerFlow
    from ._4165 import ZerolBevelGearPowerFlow
    from ._4166 import ZerolBevelGearSetPowerFlow
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
        "_4089": ["FastPowerFlow"],
        "_4090": ["FastPowerFlowSolution"],
        "_4091": ["FEPartPowerFlow"],
        "_4092": ["FlexiblePinAssemblyPowerFlow"],
        "_4093": ["GearMeshPowerFlow"],
        "_4094": ["GearPowerFlow"],
        "_4095": ["GearSetPowerFlow"],
        "_4096": ["GuideDxfModelPowerFlow"],
        "_4097": ["HypoidGearMeshPowerFlow"],
        "_4098": ["HypoidGearPowerFlow"],
        "_4099": ["HypoidGearSetPowerFlow"],
        "_4100": ["InterMountableComponentConnectionPowerFlow"],
        "_4101": ["KlingelnbergCycloPalloidConicalGearMeshPowerFlow"],
        "_4102": ["KlingelnbergCycloPalloidConicalGearPowerFlow"],
        "_4103": ["KlingelnbergCycloPalloidConicalGearSetPowerFlow"],
        "_4104": ["KlingelnbergCycloPalloidHypoidGearMeshPowerFlow"],
        "_4105": ["KlingelnbergCycloPalloidHypoidGearPowerFlow"],
        "_4106": ["KlingelnbergCycloPalloidHypoidGearSetPowerFlow"],
        "_4107": ["KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow"],
        "_4108": ["KlingelnbergCycloPalloidSpiralBevelGearPowerFlow"],
        "_4109": ["KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow"],
        "_4110": ["MassDiscPowerFlow"],
        "_4111": ["MeasurementComponentPowerFlow"],
        "_4112": ["MountableComponentPowerFlow"],
        "_4113": ["OilSealPowerFlow"],
        "_4114": ["PartPowerFlow"],
        "_4115": ["PartToPartShearCouplingConnectionPowerFlow"],
        "_4116": ["PartToPartShearCouplingHalfPowerFlow"],
        "_4117": ["PartToPartShearCouplingPowerFlow"],
        "_4118": ["PlanetaryConnectionPowerFlow"],
        "_4119": ["PlanetaryGearSetPowerFlow"],
        "_4120": ["PlanetCarrierPowerFlow"],
        "_4121": ["PointLoadPowerFlow"],
        "_4122": ["PowerFlow"],
        "_4123": ["PowerFlowDrawStyle"],
        "_4124": ["PowerLoadPowerFlow"],
        "_4125": ["PulleyPowerFlow"],
        "_4126": ["RingPinsPowerFlow"],
        "_4127": ["RingPinsToDiscConnectionPowerFlow"],
        "_4128": ["RollingRingAssemblyPowerFlow"],
        "_4129": ["RollingRingConnectionPowerFlow"],
        "_4130": ["RollingRingPowerFlow"],
        "_4131": ["RootAssemblyPowerFlow"],
        "_4132": ["ShaftHubConnectionPowerFlow"],
        "_4133": ["ShaftPowerFlow"],
        "_4134": ["ShaftToMountableComponentConnectionPowerFlow"],
        "_4135": ["SpecialisedAssemblyPowerFlow"],
        "_4136": ["SpiralBevelGearMeshPowerFlow"],
        "_4137": ["SpiralBevelGearPowerFlow"],
        "_4138": ["SpiralBevelGearSetPowerFlow"],
        "_4139": ["SpringDamperConnectionPowerFlow"],
        "_4140": ["SpringDamperHalfPowerFlow"],
        "_4141": ["SpringDamperPowerFlow"],
        "_4142": ["StraightBevelDiffGearMeshPowerFlow"],
        "_4143": ["StraightBevelDiffGearPowerFlow"],
        "_4144": ["StraightBevelDiffGearSetPowerFlow"],
        "_4145": ["StraightBevelGearMeshPowerFlow"],
        "_4146": ["StraightBevelGearPowerFlow"],
        "_4147": ["StraightBevelGearSetPowerFlow"],
        "_4148": ["StraightBevelPlanetGearPowerFlow"],
        "_4149": ["StraightBevelSunGearPowerFlow"],
        "_4150": ["SynchroniserHalfPowerFlow"],
        "_4151": ["SynchroniserPartPowerFlow"],
        "_4152": ["SynchroniserPowerFlow"],
        "_4153": ["SynchroniserSleevePowerFlow"],
        "_4154": ["ToothPassingHarmonic"],
        "_4155": ["TorqueConverterConnectionPowerFlow"],
        "_4156": ["TorqueConverterPowerFlow"],
        "_4157": ["TorqueConverterPumpPowerFlow"],
        "_4158": ["TorqueConverterTurbinePowerFlow"],
        "_4159": ["UnbalancedMassPowerFlow"],
        "_4160": ["VirtualComponentPowerFlow"],
        "_4161": ["WormGearMeshPowerFlow"],
        "_4162": ["WormGearPowerFlow"],
        "_4163": ["WormGearSetPowerFlow"],
        "_4164": ["ZerolBevelGearMeshPowerFlow"],
        "_4165": ["ZerolBevelGearPowerFlow"],
        "_4166": ["ZerolBevelGearSetPowerFlow"],
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
    "FastPowerFlow",
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

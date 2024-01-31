"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4295 import AbstractAssemblyParametricStudyTool
    from ._4296 import AbstractShaftOrHousingParametricStudyTool
    from ._4297 import AbstractShaftParametricStudyTool
    from ._4298 import AbstractShaftToMountableComponentConnectionParametricStudyTool
    from ._4299 import AGMAGleasonConicalGearMeshParametricStudyTool
    from ._4300 import AGMAGleasonConicalGearParametricStudyTool
    from ._4301 import AGMAGleasonConicalGearSetParametricStudyTool
    from ._4302 import AssemblyParametricStudyTool
    from ._4303 import BearingParametricStudyTool
    from ._4304 import BeltConnectionParametricStudyTool
    from ._4305 import BeltDriveParametricStudyTool
    from ._4306 import BevelDifferentialGearMeshParametricStudyTool
    from ._4307 import BevelDifferentialGearParametricStudyTool
    from ._4308 import BevelDifferentialGearSetParametricStudyTool
    from ._4309 import BevelDifferentialPlanetGearParametricStudyTool
    from ._4310 import BevelDifferentialSunGearParametricStudyTool
    from ._4311 import BevelGearMeshParametricStudyTool
    from ._4312 import BevelGearParametricStudyTool
    from ._4313 import BevelGearSetParametricStudyTool
    from ._4314 import BoltedJointParametricStudyTool
    from ._4315 import BoltParametricStudyTool
    from ._4316 import ClutchConnectionParametricStudyTool
    from ._4317 import ClutchHalfParametricStudyTool
    from ._4318 import ClutchParametricStudyTool
    from ._4319 import CoaxialConnectionParametricStudyTool
    from ._4320 import ComponentParametricStudyTool
    from ._4321 import ConceptCouplingConnectionParametricStudyTool
    from ._4322 import ConceptCouplingHalfParametricStudyTool
    from ._4323 import ConceptCouplingParametricStudyTool
    from ._4324 import ConceptGearMeshParametricStudyTool
    from ._4325 import ConceptGearParametricStudyTool
    from ._4326 import ConceptGearSetParametricStudyTool
    from ._4327 import ConicalGearMeshParametricStudyTool
    from ._4328 import ConicalGearParametricStudyTool
    from ._4329 import ConicalGearSetParametricStudyTool
    from ._4330 import ConnectionParametricStudyTool
    from ._4331 import ConnectorParametricStudyTool
    from ._4332 import CouplingConnectionParametricStudyTool
    from ._4333 import CouplingHalfParametricStudyTool
    from ._4334 import CouplingParametricStudyTool
    from ._4335 import CVTBeltConnectionParametricStudyTool
    from ._4336 import CVTParametricStudyTool
    from ._4337 import CVTPulleyParametricStudyTool
    from ._4338 import CycloidalAssemblyParametricStudyTool
    from ._4339 import CycloidalDiscCentralBearingConnectionParametricStudyTool
    from ._4340 import CycloidalDiscParametricStudyTool
    from ._4341 import CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
    from ._4342 import CylindricalGearMeshParametricStudyTool
    from ._4343 import CylindricalGearParametricStudyTool
    from ._4344 import CylindricalGearSetParametricStudyTool
    from ._4345 import CylindricalPlanetGearParametricStudyTool
    from ._4346 import DatumParametricStudyTool
    from ._4347 import DesignOfExperimentsVariableSetter
    from ._4348 import DoeValueSpecificationOption
    from ._4349 import DutyCycleResultsForAllComponents
    from ._4350 import DutyCycleResultsForAllGearSets
    from ._4351 import DutyCycleResultsForRootAssembly
    from ._4352 import DutyCycleResultsForSingleBearing
    from ._4353 import DutyCycleResultsForSingleShaft
    from ._4354 import ExternalCADModelParametricStudyTool
    from ._4355 import FaceGearMeshParametricStudyTool
    from ._4356 import FaceGearParametricStudyTool
    from ._4357 import FaceGearSetParametricStudyTool
    from ._4358 import FEPartParametricStudyTool
    from ._4359 import FlexiblePinAssemblyParametricStudyTool
    from ._4360 import GearMeshParametricStudyTool
    from ._4361 import GearParametricStudyTool
    from ._4362 import GearSetParametricStudyTool
    from ._4363 import GuideDxfModelParametricStudyTool
    from ._4364 import HypoidGearMeshParametricStudyTool
    from ._4365 import HypoidGearParametricStudyTool
    from ._4366 import HypoidGearSetParametricStudyTool
    from ._4367 import InterMountableComponentConnectionParametricStudyTool
    from ._4368 import KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
    from ._4369 import KlingelnbergCycloPalloidConicalGearParametricStudyTool
    from ._4370 import KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
    from ._4371 import KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
    from ._4372 import KlingelnbergCycloPalloidHypoidGearParametricStudyTool
    from ._4373 import KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
    from ._4374 import KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
    from ._4375 import KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
    from ._4376 import KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
    from ._4377 import MassDiscParametricStudyTool
    from ._4378 import MeasurementComponentParametricStudyTool
    from ._4379 import MonteCarloDistribution
    from ._4380 import MountableComponentParametricStudyTool
    from ._4381 import OilSealParametricStudyTool
    from ._4382 import ParametricStudyDimension
    from ._4383 import ParametricStudyDOEResultVariable
    from ._4384 import ParametricStudyDOEResultVariableForParallelCoordinatesPlot
    from ._4385 import ParametricStudyHistogram
    from ._4386 import ParametricStudyStaticLoad
    from ._4387 import ParametricStudyTool
    from ._4388 import ParametricStudyToolOptions
    from ._4389 import ParametricStudyToolResultsForReporting
    from ._4390 import ParametricStudyToolStepResult
    from ._4391 import ParametricStudyVariable
    from ._4392 import PartParametricStudyTool
    from ._4393 import PartToPartShearCouplingConnectionParametricStudyTool
    from ._4394 import PartToPartShearCouplingHalfParametricStudyTool
    from ._4395 import PartToPartShearCouplingParametricStudyTool
    from ._4396 import PlanetaryConnectionParametricStudyTool
    from ._4397 import PlanetaryGearSetParametricStudyTool
    from ._4398 import PlanetCarrierParametricStudyTool
    from ._4399 import PointLoadParametricStudyTool
    from ._4400 import PowerLoadParametricStudyTool
    from ._4401 import PulleyParametricStudyTool
    from ._4402 import RingPinsParametricStudyTool
    from ._4403 import RingPinsToDiscConnectionParametricStudyTool
    from ._4404 import RollingRingAssemblyParametricStudyTool
    from ._4405 import RollingRingConnectionParametricStudyTool
    from ._4406 import RollingRingParametricStudyTool
    from ._4407 import RootAssemblyParametricStudyTool
    from ._4408 import ShaftHubConnectionParametricStudyTool
    from ._4409 import ShaftParametricStudyTool
    from ._4410 import ShaftToMountableComponentConnectionParametricStudyTool
    from ._4411 import SpecialisedAssemblyParametricStudyTool
    from ._4412 import SpiralBevelGearMeshParametricStudyTool
    from ._4413 import SpiralBevelGearParametricStudyTool
    from ._4414 import SpiralBevelGearSetParametricStudyTool
    from ._4415 import SpringDamperConnectionParametricStudyTool
    from ._4416 import SpringDamperHalfParametricStudyTool
    from ._4417 import SpringDamperParametricStudyTool
    from ._4418 import StraightBevelDiffGearMeshParametricStudyTool
    from ._4419 import StraightBevelDiffGearParametricStudyTool
    from ._4420 import StraightBevelDiffGearSetParametricStudyTool
    from ._4421 import StraightBevelGearMeshParametricStudyTool
    from ._4422 import StraightBevelGearParametricStudyTool
    from ._4423 import StraightBevelGearSetParametricStudyTool
    from ._4424 import StraightBevelPlanetGearParametricStudyTool
    from ._4425 import StraightBevelSunGearParametricStudyTool
    from ._4426 import SynchroniserHalfParametricStudyTool
    from ._4427 import SynchroniserParametricStudyTool
    from ._4428 import SynchroniserPartParametricStudyTool
    from ._4429 import SynchroniserSleeveParametricStudyTool
    from ._4430 import TorqueConverterConnectionParametricStudyTool
    from ._4431 import TorqueConverterParametricStudyTool
    from ._4432 import TorqueConverterPumpParametricStudyTool
    from ._4433 import TorqueConverterTurbineParametricStudyTool
    from ._4434 import UnbalancedMassParametricStudyTool
    from ._4435 import VirtualComponentParametricStudyTool
    from ._4436 import WormGearMeshParametricStudyTool
    from ._4437 import WormGearParametricStudyTool
    from ._4438 import WormGearSetParametricStudyTool
    from ._4439 import ZerolBevelGearMeshParametricStudyTool
    from ._4440 import ZerolBevelGearParametricStudyTool
    from ._4441 import ZerolBevelGearSetParametricStudyTool
else:
    import_structure = {
        "_4295": ["AbstractAssemblyParametricStudyTool"],
        "_4296": ["AbstractShaftOrHousingParametricStudyTool"],
        "_4297": ["AbstractShaftParametricStudyTool"],
        "_4298": ["AbstractShaftToMountableComponentConnectionParametricStudyTool"],
        "_4299": ["AGMAGleasonConicalGearMeshParametricStudyTool"],
        "_4300": ["AGMAGleasonConicalGearParametricStudyTool"],
        "_4301": ["AGMAGleasonConicalGearSetParametricStudyTool"],
        "_4302": ["AssemblyParametricStudyTool"],
        "_4303": ["BearingParametricStudyTool"],
        "_4304": ["BeltConnectionParametricStudyTool"],
        "_4305": ["BeltDriveParametricStudyTool"],
        "_4306": ["BevelDifferentialGearMeshParametricStudyTool"],
        "_4307": ["BevelDifferentialGearParametricStudyTool"],
        "_4308": ["BevelDifferentialGearSetParametricStudyTool"],
        "_4309": ["BevelDifferentialPlanetGearParametricStudyTool"],
        "_4310": ["BevelDifferentialSunGearParametricStudyTool"],
        "_4311": ["BevelGearMeshParametricStudyTool"],
        "_4312": ["BevelGearParametricStudyTool"],
        "_4313": ["BevelGearSetParametricStudyTool"],
        "_4314": ["BoltedJointParametricStudyTool"],
        "_4315": ["BoltParametricStudyTool"],
        "_4316": ["ClutchConnectionParametricStudyTool"],
        "_4317": ["ClutchHalfParametricStudyTool"],
        "_4318": ["ClutchParametricStudyTool"],
        "_4319": ["CoaxialConnectionParametricStudyTool"],
        "_4320": ["ComponentParametricStudyTool"],
        "_4321": ["ConceptCouplingConnectionParametricStudyTool"],
        "_4322": ["ConceptCouplingHalfParametricStudyTool"],
        "_4323": ["ConceptCouplingParametricStudyTool"],
        "_4324": ["ConceptGearMeshParametricStudyTool"],
        "_4325": ["ConceptGearParametricStudyTool"],
        "_4326": ["ConceptGearSetParametricStudyTool"],
        "_4327": ["ConicalGearMeshParametricStudyTool"],
        "_4328": ["ConicalGearParametricStudyTool"],
        "_4329": ["ConicalGearSetParametricStudyTool"],
        "_4330": ["ConnectionParametricStudyTool"],
        "_4331": ["ConnectorParametricStudyTool"],
        "_4332": ["CouplingConnectionParametricStudyTool"],
        "_4333": ["CouplingHalfParametricStudyTool"],
        "_4334": ["CouplingParametricStudyTool"],
        "_4335": ["CVTBeltConnectionParametricStudyTool"],
        "_4336": ["CVTParametricStudyTool"],
        "_4337": ["CVTPulleyParametricStudyTool"],
        "_4338": ["CycloidalAssemblyParametricStudyTool"],
        "_4339": ["CycloidalDiscCentralBearingConnectionParametricStudyTool"],
        "_4340": ["CycloidalDiscParametricStudyTool"],
        "_4341": ["CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"],
        "_4342": ["CylindricalGearMeshParametricStudyTool"],
        "_4343": ["CylindricalGearParametricStudyTool"],
        "_4344": ["CylindricalGearSetParametricStudyTool"],
        "_4345": ["CylindricalPlanetGearParametricStudyTool"],
        "_4346": ["DatumParametricStudyTool"],
        "_4347": ["DesignOfExperimentsVariableSetter"],
        "_4348": ["DoeValueSpecificationOption"],
        "_4349": ["DutyCycleResultsForAllComponents"],
        "_4350": ["DutyCycleResultsForAllGearSets"],
        "_4351": ["DutyCycleResultsForRootAssembly"],
        "_4352": ["DutyCycleResultsForSingleBearing"],
        "_4353": ["DutyCycleResultsForSingleShaft"],
        "_4354": ["ExternalCADModelParametricStudyTool"],
        "_4355": ["FaceGearMeshParametricStudyTool"],
        "_4356": ["FaceGearParametricStudyTool"],
        "_4357": ["FaceGearSetParametricStudyTool"],
        "_4358": ["FEPartParametricStudyTool"],
        "_4359": ["FlexiblePinAssemblyParametricStudyTool"],
        "_4360": ["GearMeshParametricStudyTool"],
        "_4361": ["GearParametricStudyTool"],
        "_4362": ["GearSetParametricStudyTool"],
        "_4363": ["GuideDxfModelParametricStudyTool"],
        "_4364": ["HypoidGearMeshParametricStudyTool"],
        "_4365": ["HypoidGearParametricStudyTool"],
        "_4366": ["HypoidGearSetParametricStudyTool"],
        "_4367": ["InterMountableComponentConnectionParametricStudyTool"],
        "_4368": ["KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool"],
        "_4369": ["KlingelnbergCycloPalloidConicalGearParametricStudyTool"],
        "_4370": ["KlingelnbergCycloPalloidConicalGearSetParametricStudyTool"],
        "_4371": ["KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool"],
        "_4372": ["KlingelnbergCycloPalloidHypoidGearParametricStudyTool"],
        "_4373": ["KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool"],
        "_4374": ["KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool"],
        "_4375": ["KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool"],
        "_4376": ["KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool"],
        "_4377": ["MassDiscParametricStudyTool"],
        "_4378": ["MeasurementComponentParametricStudyTool"],
        "_4379": ["MonteCarloDistribution"],
        "_4380": ["MountableComponentParametricStudyTool"],
        "_4381": ["OilSealParametricStudyTool"],
        "_4382": ["ParametricStudyDimension"],
        "_4383": ["ParametricStudyDOEResultVariable"],
        "_4384": ["ParametricStudyDOEResultVariableForParallelCoordinatesPlot"],
        "_4385": ["ParametricStudyHistogram"],
        "_4386": ["ParametricStudyStaticLoad"],
        "_4387": ["ParametricStudyTool"],
        "_4388": ["ParametricStudyToolOptions"],
        "_4389": ["ParametricStudyToolResultsForReporting"],
        "_4390": ["ParametricStudyToolStepResult"],
        "_4391": ["ParametricStudyVariable"],
        "_4392": ["PartParametricStudyTool"],
        "_4393": ["PartToPartShearCouplingConnectionParametricStudyTool"],
        "_4394": ["PartToPartShearCouplingHalfParametricStudyTool"],
        "_4395": ["PartToPartShearCouplingParametricStudyTool"],
        "_4396": ["PlanetaryConnectionParametricStudyTool"],
        "_4397": ["PlanetaryGearSetParametricStudyTool"],
        "_4398": ["PlanetCarrierParametricStudyTool"],
        "_4399": ["PointLoadParametricStudyTool"],
        "_4400": ["PowerLoadParametricStudyTool"],
        "_4401": ["PulleyParametricStudyTool"],
        "_4402": ["RingPinsParametricStudyTool"],
        "_4403": ["RingPinsToDiscConnectionParametricStudyTool"],
        "_4404": ["RollingRingAssemblyParametricStudyTool"],
        "_4405": ["RollingRingConnectionParametricStudyTool"],
        "_4406": ["RollingRingParametricStudyTool"],
        "_4407": ["RootAssemblyParametricStudyTool"],
        "_4408": ["ShaftHubConnectionParametricStudyTool"],
        "_4409": ["ShaftParametricStudyTool"],
        "_4410": ["ShaftToMountableComponentConnectionParametricStudyTool"],
        "_4411": ["SpecialisedAssemblyParametricStudyTool"],
        "_4412": ["SpiralBevelGearMeshParametricStudyTool"],
        "_4413": ["SpiralBevelGearParametricStudyTool"],
        "_4414": ["SpiralBevelGearSetParametricStudyTool"],
        "_4415": ["SpringDamperConnectionParametricStudyTool"],
        "_4416": ["SpringDamperHalfParametricStudyTool"],
        "_4417": ["SpringDamperParametricStudyTool"],
        "_4418": ["StraightBevelDiffGearMeshParametricStudyTool"],
        "_4419": ["StraightBevelDiffGearParametricStudyTool"],
        "_4420": ["StraightBevelDiffGearSetParametricStudyTool"],
        "_4421": ["StraightBevelGearMeshParametricStudyTool"],
        "_4422": ["StraightBevelGearParametricStudyTool"],
        "_4423": ["StraightBevelGearSetParametricStudyTool"],
        "_4424": ["StraightBevelPlanetGearParametricStudyTool"],
        "_4425": ["StraightBevelSunGearParametricStudyTool"],
        "_4426": ["SynchroniserHalfParametricStudyTool"],
        "_4427": ["SynchroniserParametricStudyTool"],
        "_4428": ["SynchroniserPartParametricStudyTool"],
        "_4429": ["SynchroniserSleeveParametricStudyTool"],
        "_4430": ["TorqueConverterConnectionParametricStudyTool"],
        "_4431": ["TorqueConverterParametricStudyTool"],
        "_4432": ["TorqueConverterPumpParametricStudyTool"],
        "_4433": ["TorqueConverterTurbineParametricStudyTool"],
        "_4434": ["UnbalancedMassParametricStudyTool"],
        "_4435": ["VirtualComponentParametricStudyTool"],
        "_4436": ["WormGearMeshParametricStudyTool"],
        "_4437": ["WormGearParametricStudyTool"],
        "_4438": ["WormGearSetParametricStudyTool"],
        "_4439": ["ZerolBevelGearMeshParametricStudyTool"],
        "_4440": ["ZerolBevelGearParametricStudyTool"],
        "_4441": ["ZerolBevelGearSetParametricStudyTool"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyParametricStudyTool",
    "AbstractShaftOrHousingParametricStudyTool",
    "AbstractShaftParametricStudyTool",
    "AbstractShaftToMountableComponentConnectionParametricStudyTool",
    "AGMAGleasonConicalGearMeshParametricStudyTool",
    "AGMAGleasonConicalGearParametricStudyTool",
    "AGMAGleasonConicalGearSetParametricStudyTool",
    "AssemblyParametricStudyTool",
    "BearingParametricStudyTool",
    "BeltConnectionParametricStudyTool",
    "BeltDriveParametricStudyTool",
    "BevelDifferentialGearMeshParametricStudyTool",
    "BevelDifferentialGearParametricStudyTool",
    "BevelDifferentialGearSetParametricStudyTool",
    "BevelDifferentialPlanetGearParametricStudyTool",
    "BevelDifferentialSunGearParametricStudyTool",
    "BevelGearMeshParametricStudyTool",
    "BevelGearParametricStudyTool",
    "BevelGearSetParametricStudyTool",
    "BoltedJointParametricStudyTool",
    "BoltParametricStudyTool",
    "ClutchConnectionParametricStudyTool",
    "ClutchHalfParametricStudyTool",
    "ClutchParametricStudyTool",
    "CoaxialConnectionParametricStudyTool",
    "ComponentParametricStudyTool",
    "ConceptCouplingConnectionParametricStudyTool",
    "ConceptCouplingHalfParametricStudyTool",
    "ConceptCouplingParametricStudyTool",
    "ConceptGearMeshParametricStudyTool",
    "ConceptGearParametricStudyTool",
    "ConceptGearSetParametricStudyTool",
    "ConicalGearMeshParametricStudyTool",
    "ConicalGearParametricStudyTool",
    "ConicalGearSetParametricStudyTool",
    "ConnectionParametricStudyTool",
    "ConnectorParametricStudyTool",
    "CouplingConnectionParametricStudyTool",
    "CouplingHalfParametricStudyTool",
    "CouplingParametricStudyTool",
    "CVTBeltConnectionParametricStudyTool",
    "CVTParametricStudyTool",
    "CVTPulleyParametricStudyTool",
    "CycloidalAssemblyParametricStudyTool",
    "CycloidalDiscCentralBearingConnectionParametricStudyTool",
    "CycloidalDiscParametricStudyTool",
    "CycloidalDiscPlanetaryBearingConnectionParametricStudyTool",
    "CylindricalGearMeshParametricStudyTool",
    "CylindricalGearParametricStudyTool",
    "CylindricalGearSetParametricStudyTool",
    "CylindricalPlanetGearParametricStudyTool",
    "DatumParametricStudyTool",
    "DesignOfExperimentsVariableSetter",
    "DoeValueSpecificationOption",
    "DutyCycleResultsForAllComponents",
    "DutyCycleResultsForAllGearSets",
    "DutyCycleResultsForRootAssembly",
    "DutyCycleResultsForSingleBearing",
    "DutyCycleResultsForSingleShaft",
    "ExternalCADModelParametricStudyTool",
    "FaceGearMeshParametricStudyTool",
    "FaceGearParametricStudyTool",
    "FaceGearSetParametricStudyTool",
    "FEPartParametricStudyTool",
    "FlexiblePinAssemblyParametricStudyTool",
    "GearMeshParametricStudyTool",
    "GearParametricStudyTool",
    "GearSetParametricStudyTool",
    "GuideDxfModelParametricStudyTool",
    "HypoidGearMeshParametricStudyTool",
    "HypoidGearParametricStudyTool",
    "HypoidGearSetParametricStudyTool",
    "InterMountableComponentConnectionParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearParametricStudyTool",
    "KlingelnbergCycloPalloidConicalGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearParametricStudyTool",
    "KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool",
    "KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool",
    "MassDiscParametricStudyTool",
    "MeasurementComponentParametricStudyTool",
    "MonteCarloDistribution",
    "MountableComponentParametricStudyTool",
    "OilSealParametricStudyTool",
    "ParametricStudyDimension",
    "ParametricStudyDOEResultVariable",
    "ParametricStudyDOEResultVariableForParallelCoordinatesPlot",
    "ParametricStudyHistogram",
    "ParametricStudyStaticLoad",
    "ParametricStudyTool",
    "ParametricStudyToolOptions",
    "ParametricStudyToolResultsForReporting",
    "ParametricStudyToolStepResult",
    "ParametricStudyVariable",
    "PartParametricStudyTool",
    "PartToPartShearCouplingConnectionParametricStudyTool",
    "PartToPartShearCouplingHalfParametricStudyTool",
    "PartToPartShearCouplingParametricStudyTool",
    "PlanetaryConnectionParametricStudyTool",
    "PlanetaryGearSetParametricStudyTool",
    "PlanetCarrierParametricStudyTool",
    "PointLoadParametricStudyTool",
    "PowerLoadParametricStudyTool",
    "PulleyParametricStudyTool",
    "RingPinsParametricStudyTool",
    "RingPinsToDiscConnectionParametricStudyTool",
    "RollingRingAssemblyParametricStudyTool",
    "RollingRingConnectionParametricStudyTool",
    "RollingRingParametricStudyTool",
    "RootAssemblyParametricStudyTool",
    "ShaftHubConnectionParametricStudyTool",
    "ShaftParametricStudyTool",
    "ShaftToMountableComponentConnectionParametricStudyTool",
    "SpecialisedAssemblyParametricStudyTool",
    "SpiralBevelGearMeshParametricStudyTool",
    "SpiralBevelGearParametricStudyTool",
    "SpiralBevelGearSetParametricStudyTool",
    "SpringDamperConnectionParametricStudyTool",
    "SpringDamperHalfParametricStudyTool",
    "SpringDamperParametricStudyTool",
    "StraightBevelDiffGearMeshParametricStudyTool",
    "StraightBevelDiffGearParametricStudyTool",
    "StraightBevelDiffGearSetParametricStudyTool",
    "StraightBevelGearMeshParametricStudyTool",
    "StraightBevelGearParametricStudyTool",
    "StraightBevelGearSetParametricStudyTool",
    "StraightBevelPlanetGearParametricStudyTool",
    "StraightBevelSunGearParametricStudyTool",
    "SynchroniserHalfParametricStudyTool",
    "SynchroniserParametricStudyTool",
    "SynchroniserPartParametricStudyTool",
    "SynchroniserSleeveParametricStudyTool",
    "TorqueConverterConnectionParametricStudyTool",
    "TorqueConverterParametricStudyTool",
    "TorqueConverterPumpParametricStudyTool",
    "TorqueConverterTurbineParametricStudyTool",
    "UnbalancedMassParametricStudyTool",
    "VirtualComponentParametricStudyTool",
    "WormGearMeshParametricStudyTool",
    "WormGearParametricStudyTool",
    "WormGearSetParametricStudyTool",
    "ZerolBevelGearMeshParametricStudyTool",
    "ZerolBevelGearParametricStudyTool",
    "ZerolBevelGearSetParametricStudyTool",
)

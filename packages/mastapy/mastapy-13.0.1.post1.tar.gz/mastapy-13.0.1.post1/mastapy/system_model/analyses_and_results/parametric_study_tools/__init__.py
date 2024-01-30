"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4296 import AbstractAssemblyParametricStudyTool
    from ._4297 import AbstractShaftOrHousingParametricStudyTool
    from ._4298 import AbstractShaftParametricStudyTool
    from ._4299 import AbstractShaftToMountableComponentConnectionParametricStudyTool
    from ._4300 import AGMAGleasonConicalGearMeshParametricStudyTool
    from ._4301 import AGMAGleasonConicalGearParametricStudyTool
    from ._4302 import AGMAGleasonConicalGearSetParametricStudyTool
    from ._4303 import AssemblyParametricStudyTool
    from ._4304 import BearingParametricStudyTool
    from ._4305 import BeltConnectionParametricStudyTool
    from ._4306 import BeltDriveParametricStudyTool
    from ._4307 import BevelDifferentialGearMeshParametricStudyTool
    from ._4308 import BevelDifferentialGearParametricStudyTool
    from ._4309 import BevelDifferentialGearSetParametricStudyTool
    from ._4310 import BevelDifferentialPlanetGearParametricStudyTool
    from ._4311 import BevelDifferentialSunGearParametricStudyTool
    from ._4312 import BevelGearMeshParametricStudyTool
    from ._4313 import BevelGearParametricStudyTool
    from ._4314 import BevelGearSetParametricStudyTool
    from ._4315 import BoltedJointParametricStudyTool
    from ._4316 import BoltParametricStudyTool
    from ._4317 import ClutchConnectionParametricStudyTool
    from ._4318 import ClutchHalfParametricStudyTool
    from ._4319 import ClutchParametricStudyTool
    from ._4320 import CoaxialConnectionParametricStudyTool
    from ._4321 import ComponentParametricStudyTool
    from ._4322 import ConceptCouplingConnectionParametricStudyTool
    from ._4323 import ConceptCouplingHalfParametricStudyTool
    from ._4324 import ConceptCouplingParametricStudyTool
    from ._4325 import ConceptGearMeshParametricStudyTool
    from ._4326 import ConceptGearParametricStudyTool
    from ._4327 import ConceptGearSetParametricStudyTool
    from ._4328 import ConicalGearMeshParametricStudyTool
    from ._4329 import ConicalGearParametricStudyTool
    from ._4330 import ConicalGearSetParametricStudyTool
    from ._4331 import ConnectionParametricStudyTool
    from ._4332 import ConnectorParametricStudyTool
    from ._4333 import CouplingConnectionParametricStudyTool
    from ._4334 import CouplingHalfParametricStudyTool
    from ._4335 import CouplingParametricStudyTool
    from ._4336 import CVTBeltConnectionParametricStudyTool
    from ._4337 import CVTParametricStudyTool
    from ._4338 import CVTPulleyParametricStudyTool
    from ._4339 import CycloidalAssemblyParametricStudyTool
    from ._4340 import CycloidalDiscCentralBearingConnectionParametricStudyTool
    from ._4341 import CycloidalDiscParametricStudyTool
    from ._4342 import CycloidalDiscPlanetaryBearingConnectionParametricStudyTool
    from ._4343 import CylindricalGearMeshParametricStudyTool
    from ._4344 import CylindricalGearParametricStudyTool
    from ._4345 import CylindricalGearSetParametricStudyTool
    from ._4346 import CylindricalPlanetGearParametricStudyTool
    from ._4347 import DatumParametricStudyTool
    from ._4348 import DesignOfExperimentsVariableSetter
    from ._4349 import DoeValueSpecificationOption
    from ._4350 import DutyCycleResultsForAllComponents
    from ._4351 import DutyCycleResultsForAllGearSets
    from ._4352 import DutyCycleResultsForRootAssembly
    from ._4353 import DutyCycleResultsForSingleBearing
    from ._4354 import DutyCycleResultsForSingleShaft
    from ._4355 import ExternalCADModelParametricStudyTool
    from ._4356 import FaceGearMeshParametricStudyTool
    from ._4357 import FaceGearParametricStudyTool
    from ._4358 import FaceGearSetParametricStudyTool
    from ._4359 import FEPartParametricStudyTool
    from ._4360 import FlexiblePinAssemblyParametricStudyTool
    from ._4361 import GearMeshParametricStudyTool
    from ._4362 import GearParametricStudyTool
    from ._4363 import GearSetParametricStudyTool
    from ._4364 import GuideDxfModelParametricStudyTool
    from ._4365 import HypoidGearMeshParametricStudyTool
    from ._4366 import HypoidGearParametricStudyTool
    from ._4367 import HypoidGearSetParametricStudyTool
    from ._4368 import InterMountableComponentConnectionParametricStudyTool
    from ._4369 import KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool
    from ._4370 import KlingelnbergCycloPalloidConicalGearParametricStudyTool
    from ._4371 import KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
    from ._4372 import KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool
    from ._4373 import KlingelnbergCycloPalloidHypoidGearParametricStudyTool
    from ._4374 import KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
    from ._4375 import KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool
    from ._4376 import KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
    from ._4377 import KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
    from ._4378 import MassDiscParametricStudyTool
    from ._4379 import MeasurementComponentParametricStudyTool
    from ._4380 import MonteCarloDistribution
    from ._4381 import MountableComponentParametricStudyTool
    from ._4382 import OilSealParametricStudyTool
    from ._4383 import ParametricStudyDimension
    from ._4384 import ParametricStudyDOEResultVariable
    from ._4385 import ParametricStudyDOEResultVariableForParallelCoordinatesPlot
    from ._4386 import ParametricStudyHistogram
    from ._4387 import ParametricStudyStaticLoad
    from ._4388 import ParametricStudyTool
    from ._4389 import ParametricStudyToolOptions
    from ._4390 import ParametricStudyToolResultsForReporting
    from ._4391 import ParametricStudyToolStepResult
    from ._4392 import ParametricStudyVariable
    from ._4393 import PartParametricStudyTool
    from ._4394 import PartToPartShearCouplingConnectionParametricStudyTool
    from ._4395 import PartToPartShearCouplingHalfParametricStudyTool
    from ._4396 import PartToPartShearCouplingParametricStudyTool
    from ._4397 import PlanetaryConnectionParametricStudyTool
    from ._4398 import PlanetaryGearSetParametricStudyTool
    from ._4399 import PlanetCarrierParametricStudyTool
    from ._4400 import PointLoadParametricStudyTool
    from ._4401 import PowerLoadParametricStudyTool
    from ._4402 import PulleyParametricStudyTool
    from ._4403 import RingPinsParametricStudyTool
    from ._4404 import RingPinsToDiscConnectionParametricStudyTool
    from ._4405 import RollingRingAssemblyParametricStudyTool
    from ._4406 import RollingRingConnectionParametricStudyTool
    from ._4407 import RollingRingParametricStudyTool
    from ._4408 import RootAssemblyParametricStudyTool
    from ._4409 import ShaftHubConnectionParametricStudyTool
    from ._4410 import ShaftParametricStudyTool
    from ._4411 import ShaftToMountableComponentConnectionParametricStudyTool
    from ._4412 import SpecialisedAssemblyParametricStudyTool
    from ._4413 import SpiralBevelGearMeshParametricStudyTool
    from ._4414 import SpiralBevelGearParametricStudyTool
    from ._4415 import SpiralBevelGearSetParametricStudyTool
    from ._4416 import SpringDamperConnectionParametricStudyTool
    from ._4417 import SpringDamperHalfParametricStudyTool
    from ._4418 import SpringDamperParametricStudyTool
    from ._4419 import StraightBevelDiffGearMeshParametricStudyTool
    from ._4420 import StraightBevelDiffGearParametricStudyTool
    from ._4421 import StraightBevelDiffGearSetParametricStudyTool
    from ._4422 import StraightBevelGearMeshParametricStudyTool
    from ._4423 import StraightBevelGearParametricStudyTool
    from ._4424 import StraightBevelGearSetParametricStudyTool
    from ._4425 import StraightBevelPlanetGearParametricStudyTool
    from ._4426 import StraightBevelSunGearParametricStudyTool
    from ._4427 import SynchroniserHalfParametricStudyTool
    from ._4428 import SynchroniserParametricStudyTool
    from ._4429 import SynchroniserPartParametricStudyTool
    from ._4430 import SynchroniserSleeveParametricStudyTool
    from ._4431 import TorqueConverterConnectionParametricStudyTool
    from ._4432 import TorqueConverterParametricStudyTool
    from ._4433 import TorqueConverterPumpParametricStudyTool
    from ._4434 import TorqueConverterTurbineParametricStudyTool
    from ._4435 import UnbalancedMassParametricStudyTool
    from ._4436 import VirtualComponentParametricStudyTool
    from ._4437 import WormGearMeshParametricStudyTool
    from ._4438 import WormGearParametricStudyTool
    from ._4439 import WormGearSetParametricStudyTool
    from ._4440 import ZerolBevelGearMeshParametricStudyTool
    from ._4441 import ZerolBevelGearParametricStudyTool
    from ._4442 import ZerolBevelGearSetParametricStudyTool
else:
    import_structure = {
        "_4296": ["AbstractAssemblyParametricStudyTool"],
        "_4297": ["AbstractShaftOrHousingParametricStudyTool"],
        "_4298": ["AbstractShaftParametricStudyTool"],
        "_4299": ["AbstractShaftToMountableComponentConnectionParametricStudyTool"],
        "_4300": ["AGMAGleasonConicalGearMeshParametricStudyTool"],
        "_4301": ["AGMAGleasonConicalGearParametricStudyTool"],
        "_4302": ["AGMAGleasonConicalGearSetParametricStudyTool"],
        "_4303": ["AssemblyParametricStudyTool"],
        "_4304": ["BearingParametricStudyTool"],
        "_4305": ["BeltConnectionParametricStudyTool"],
        "_4306": ["BeltDriveParametricStudyTool"],
        "_4307": ["BevelDifferentialGearMeshParametricStudyTool"],
        "_4308": ["BevelDifferentialGearParametricStudyTool"],
        "_4309": ["BevelDifferentialGearSetParametricStudyTool"],
        "_4310": ["BevelDifferentialPlanetGearParametricStudyTool"],
        "_4311": ["BevelDifferentialSunGearParametricStudyTool"],
        "_4312": ["BevelGearMeshParametricStudyTool"],
        "_4313": ["BevelGearParametricStudyTool"],
        "_4314": ["BevelGearSetParametricStudyTool"],
        "_4315": ["BoltedJointParametricStudyTool"],
        "_4316": ["BoltParametricStudyTool"],
        "_4317": ["ClutchConnectionParametricStudyTool"],
        "_4318": ["ClutchHalfParametricStudyTool"],
        "_4319": ["ClutchParametricStudyTool"],
        "_4320": ["CoaxialConnectionParametricStudyTool"],
        "_4321": ["ComponentParametricStudyTool"],
        "_4322": ["ConceptCouplingConnectionParametricStudyTool"],
        "_4323": ["ConceptCouplingHalfParametricStudyTool"],
        "_4324": ["ConceptCouplingParametricStudyTool"],
        "_4325": ["ConceptGearMeshParametricStudyTool"],
        "_4326": ["ConceptGearParametricStudyTool"],
        "_4327": ["ConceptGearSetParametricStudyTool"],
        "_4328": ["ConicalGearMeshParametricStudyTool"],
        "_4329": ["ConicalGearParametricStudyTool"],
        "_4330": ["ConicalGearSetParametricStudyTool"],
        "_4331": ["ConnectionParametricStudyTool"],
        "_4332": ["ConnectorParametricStudyTool"],
        "_4333": ["CouplingConnectionParametricStudyTool"],
        "_4334": ["CouplingHalfParametricStudyTool"],
        "_4335": ["CouplingParametricStudyTool"],
        "_4336": ["CVTBeltConnectionParametricStudyTool"],
        "_4337": ["CVTParametricStudyTool"],
        "_4338": ["CVTPulleyParametricStudyTool"],
        "_4339": ["CycloidalAssemblyParametricStudyTool"],
        "_4340": ["CycloidalDiscCentralBearingConnectionParametricStudyTool"],
        "_4341": ["CycloidalDiscParametricStudyTool"],
        "_4342": ["CycloidalDiscPlanetaryBearingConnectionParametricStudyTool"],
        "_4343": ["CylindricalGearMeshParametricStudyTool"],
        "_4344": ["CylindricalGearParametricStudyTool"],
        "_4345": ["CylindricalGearSetParametricStudyTool"],
        "_4346": ["CylindricalPlanetGearParametricStudyTool"],
        "_4347": ["DatumParametricStudyTool"],
        "_4348": ["DesignOfExperimentsVariableSetter"],
        "_4349": ["DoeValueSpecificationOption"],
        "_4350": ["DutyCycleResultsForAllComponents"],
        "_4351": ["DutyCycleResultsForAllGearSets"],
        "_4352": ["DutyCycleResultsForRootAssembly"],
        "_4353": ["DutyCycleResultsForSingleBearing"],
        "_4354": ["DutyCycleResultsForSingleShaft"],
        "_4355": ["ExternalCADModelParametricStudyTool"],
        "_4356": ["FaceGearMeshParametricStudyTool"],
        "_4357": ["FaceGearParametricStudyTool"],
        "_4358": ["FaceGearSetParametricStudyTool"],
        "_4359": ["FEPartParametricStudyTool"],
        "_4360": ["FlexiblePinAssemblyParametricStudyTool"],
        "_4361": ["GearMeshParametricStudyTool"],
        "_4362": ["GearParametricStudyTool"],
        "_4363": ["GearSetParametricStudyTool"],
        "_4364": ["GuideDxfModelParametricStudyTool"],
        "_4365": ["HypoidGearMeshParametricStudyTool"],
        "_4366": ["HypoidGearParametricStudyTool"],
        "_4367": ["HypoidGearSetParametricStudyTool"],
        "_4368": ["InterMountableComponentConnectionParametricStudyTool"],
        "_4369": ["KlingelnbergCycloPalloidConicalGearMeshParametricStudyTool"],
        "_4370": ["KlingelnbergCycloPalloidConicalGearParametricStudyTool"],
        "_4371": ["KlingelnbergCycloPalloidConicalGearSetParametricStudyTool"],
        "_4372": ["KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool"],
        "_4373": ["KlingelnbergCycloPalloidHypoidGearParametricStudyTool"],
        "_4374": ["KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool"],
        "_4375": ["KlingelnbergCycloPalloidSpiralBevelGearMeshParametricStudyTool"],
        "_4376": ["KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool"],
        "_4377": ["KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool"],
        "_4378": ["MassDiscParametricStudyTool"],
        "_4379": ["MeasurementComponentParametricStudyTool"],
        "_4380": ["MonteCarloDistribution"],
        "_4381": ["MountableComponentParametricStudyTool"],
        "_4382": ["OilSealParametricStudyTool"],
        "_4383": ["ParametricStudyDimension"],
        "_4384": ["ParametricStudyDOEResultVariable"],
        "_4385": ["ParametricStudyDOEResultVariableForParallelCoordinatesPlot"],
        "_4386": ["ParametricStudyHistogram"],
        "_4387": ["ParametricStudyStaticLoad"],
        "_4388": ["ParametricStudyTool"],
        "_4389": ["ParametricStudyToolOptions"],
        "_4390": ["ParametricStudyToolResultsForReporting"],
        "_4391": ["ParametricStudyToolStepResult"],
        "_4392": ["ParametricStudyVariable"],
        "_4393": ["PartParametricStudyTool"],
        "_4394": ["PartToPartShearCouplingConnectionParametricStudyTool"],
        "_4395": ["PartToPartShearCouplingHalfParametricStudyTool"],
        "_4396": ["PartToPartShearCouplingParametricStudyTool"],
        "_4397": ["PlanetaryConnectionParametricStudyTool"],
        "_4398": ["PlanetaryGearSetParametricStudyTool"],
        "_4399": ["PlanetCarrierParametricStudyTool"],
        "_4400": ["PointLoadParametricStudyTool"],
        "_4401": ["PowerLoadParametricStudyTool"],
        "_4402": ["PulleyParametricStudyTool"],
        "_4403": ["RingPinsParametricStudyTool"],
        "_4404": ["RingPinsToDiscConnectionParametricStudyTool"],
        "_4405": ["RollingRingAssemblyParametricStudyTool"],
        "_4406": ["RollingRingConnectionParametricStudyTool"],
        "_4407": ["RollingRingParametricStudyTool"],
        "_4408": ["RootAssemblyParametricStudyTool"],
        "_4409": ["ShaftHubConnectionParametricStudyTool"],
        "_4410": ["ShaftParametricStudyTool"],
        "_4411": ["ShaftToMountableComponentConnectionParametricStudyTool"],
        "_4412": ["SpecialisedAssemblyParametricStudyTool"],
        "_4413": ["SpiralBevelGearMeshParametricStudyTool"],
        "_4414": ["SpiralBevelGearParametricStudyTool"],
        "_4415": ["SpiralBevelGearSetParametricStudyTool"],
        "_4416": ["SpringDamperConnectionParametricStudyTool"],
        "_4417": ["SpringDamperHalfParametricStudyTool"],
        "_4418": ["SpringDamperParametricStudyTool"],
        "_4419": ["StraightBevelDiffGearMeshParametricStudyTool"],
        "_4420": ["StraightBevelDiffGearParametricStudyTool"],
        "_4421": ["StraightBevelDiffGearSetParametricStudyTool"],
        "_4422": ["StraightBevelGearMeshParametricStudyTool"],
        "_4423": ["StraightBevelGearParametricStudyTool"],
        "_4424": ["StraightBevelGearSetParametricStudyTool"],
        "_4425": ["StraightBevelPlanetGearParametricStudyTool"],
        "_4426": ["StraightBevelSunGearParametricStudyTool"],
        "_4427": ["SynchroniserHalfParametricStudyTool"],
        "_4428": ["SynchroniserParametricStudyTool"],
        "_4429": ["SynchroniserPartParametricStudyTool"],
        "_4430": ["SynchroniserSleeveParametricStudyTool"],
        "_4431": ["TorqueConverterConnectionParametricStudyTool"],
        "_4432": ["TorqueConverterParametricStudyTool"],
        "_4433": ["TorqueConverterPumpParametricStudyTool"],
        "_4434": ["TorqueConverterTurbineParametricStudyTool"],
        "_4435": ["UnbalancedMassParametricStudyTool"],
        "_4436": ["VirtualComponentParametricStudyTool"],
        "_4437": ["WormGearMeshParametricStudyTool"],
        "_4438": ["WormGearParametricStudyTool"],
        "_4439": ["WormGearSetParametricStudyTool"],
        "_4440": ["ZerolBevelGearMeshParametricStudyTool"],
        "_4441": ["ZerolBevelGearParametricStudyTool"],
        "_4442": ["ZerolBevelGearSetParametricStudyTool"],
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

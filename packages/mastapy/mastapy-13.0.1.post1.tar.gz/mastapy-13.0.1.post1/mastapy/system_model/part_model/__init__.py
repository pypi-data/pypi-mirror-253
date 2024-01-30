"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2433 import Assembly
    from ._2434 import AbstractAssembly
    from ._2435 import AbstractShaft
    from ._2436 import AbstractShaftOrHousing
    from ._2437 import AGMALoadSharingTableApplicationLevel
    from ._2438 import AxialInternalClearanceTolerance
    from ._2439 import Bearing
    from ._2440 import BearingF0InputMethod
    from ._2441 import BearingRaceMountingOptions
    from ._2442 import Bolt
    from ._2443 import BoltedJoint
    from ._2444 import Component
    from ._2445 import ComponentsConnectedResult
    from ._2446 import ConnectedSockets
    from ._2447 import Connector
    from ._2448 import Datum
    from ._2449 import ElectricMachineSearchRegionSpecificationMethod
    from ._2450 import EnginePartLoad
    from ._2451 import EngineSpeed
    from ._2452 import ExternalCADModel
    from ._2453 import FEPart
    from ._2454 import FlexiblePinAssembly
    from ._2455 import GuideDxfModel
    from ._2456 import GuideImage
    from ._2457 import GuideModelUsage
    from ._2458 import InnerBearingRaceMountingOptions
    from ._2459 import InternalClearanceTolerance
    from ._2460 import LoadSharingModes
    from ._2461 import LoadSharingSettings
    from ._2462 import MassDisc
    from ._2463 import MeasurementComponent
    from ._2464 import MountableComponent
    from ._2465 import OilLevelSpecification
    from ._2466 import OilSeal
    from ._2467 import OuterBearingRaceMountingOptions
    from ._2468 import Part
    from ._2469 import PlanetCarrier
    from ._2470 import PlanetCarrierSettings
    from ._2471 import PointLoad
    from ._2472 import PowerLoad
    from ._2473 import RadialInternalClearanceTolerance
    from ._2474 import RootAssembly
    from ._2475 import ShaftDiameterModificationDueToRollingBearingRing
    from ._2476 import SpecialisedAssembly
    from ._2477 import UnbalancedMass
    from ._2478 import UnbalancedMassInclusionOption
    from ._2479 import VirtualComponent
    from ._2480 import WindTurbineBladeModeDetails
    from ._2481 import WindTurbineSingleBladeDetails
else:
    import_structure = {
        "_2433": ["Assembly"],
        "_2434": ["AbstractAssembly"],
        "_2435": ["AbstractShaft"],
        "_2436": ["AbstractShaftOrHousing"],
        "_2437": ["AGMALoadSharingTableApplicationLevel"],
        "_2438": ["AxialInternalClearanceTolerance"],
        "_2439": ["Bearing"],
        "_2440": ["BearingF0InputMethod"],
        "_2441": ["BearingRaceMountingOptions"],
        "_2442": ["Bolt"],
        "_2443": ["BoltedJoint"],
        "_2444": ["Component"],
        "_2445": ["ComponentsConnectedResult"],
        "_2446": ["ConnectedSockets"],
        "_2447": ["Connector"],
        "_2448": ["Datum"],
        "_2449": ["ElectricMachineSearchRegionSpecificationMethod"],
        "_2450": ["EnginePartLoad"],
        "_2451": ["EngineSpeed"],
        "_2452": ["ExternalCADModel"],
        "_2453": ["FEPart"],
        "_2454": ["FlexiblePinAssembly"],
        "_2455": ["GuideDxfModel"],
        "_2456": ["GuideImage"],
        "_2457": ["GuideModelUsage"],
        "_2458": ["InnerBearingRaceMountingOptions"],
        "_2459": ["InternalClearanceTolerance"],
        "_2460": ["LoadSharingModes"],
        "_2461": ["LoadSharingSettings"],
        "_2462": ["MassDisc"],
        "_2463": ["MeasurementComponent"],
        "_2464": ["MountableComponent"],
        "_2465": ["OilLevelSpecification"],
        "_2466": ["OilSeal"],
        "_2467": ["OuterBearingRaceMountingOptions"],
        "_2468": ["Part"],
        "_2469": ["PlanetCarrier"],
        "_2470": ["PlanetCarrierSettings"],
        "_2471": ["PointLoad"],
        "_2472": ["PowerLoad"],
        "_2473": ["RadialInternalClearanceTolerance"],
        "_2474": ["RootAssembly"],
        "_2475": ["ShaftDiameterModificationDueToRollingBearingRing"],
        "_2476": ["SpecialisedAssembly"],
        "_2477": ["UnbalancedMass"],
        "_2478": ["UnbalancedMassInclusionOption"],
        "_2479": ["VirtualComponent"],
        "_2480": ["WindTurbineBladeModeDetails"],
        "_2481": ["WindTurbineSingleBladeDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Assembly",
    "AbstractAssembly",
    "AbstractShaft",
    "AbstractShaftOrHousing",
    "AGMALoadSharingTableApplicationLevel",
    "AxialInternalClearanceTolerance",
    "Bearing",
    "BearingF0InputMethod",
    "BearingRaceMountingOptions",
    "Bolt",
    "BoltedJoint",
    "Component",
    "ComponentsConnectedResult",
    "ConnectedSockets",
    "Connector",
    "Datum",
    "ElectricMachineSearchRegionSpecificationMethod",
    "EnginePartLoad",
    "EngineSpeed",
    "ExternalCADModel",
    "FEPart",
    "FlexiblePinAssembly",
    "GuideDxfModel",
    "GuideImage",
    "GuideModelUsage",
    "InnerBearingRaceMountingOptions",
    "InternalClearanceTolerance",
    "LoadSharingModes",
    "LoadSharingSettings",
    "MassDisc",
    "MeasurementComponent",
    "MountableComponent",
    "OilLevelSpecification",
    "OilSeal",
    "OuterBearingRaceMountingOptions",
    "Part",
    "PlanetCarrier",
    "PlanetCarrierSettings",
    "PointLoad",
    "PowerLoad",
    "RadialInternalClearanceTolerance",
    "RootAssembly",
    "ShaftDiameterModificationDueToRollingBearingRing",
    "SpecialisedAssembly",
    "UnbalancedMass",
    "UnbalancedMassInclusionOption",
    "VirtualComponent",
    "WindTurbineBladeModeDetails",
    "WindTurbineSingleBladeDetails",
)

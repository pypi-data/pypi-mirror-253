"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2355 import AlignConnectedComponentOptions
    from ._2356 import AlignmentMethod
    from ._2357 import AlignmentMethodForRaceBearing
    from ._2358 import AlignmentUsingAxialNodePositions
    from ._2359 import AngleSource
    from ._2360 import BaseFEWithSelection
    from ._2361 import BatchOperations
    from ._2362 import BearingNodeAlignmentOption
    from ._2363 import BearingNodeOption
    from ._2364 import BearingRaceNodeLink
    from ._2365 import BearingRacePosition
    from ._2366 import ComponentOrientationOption
    from ._2367 import ContactPairWithSelection
    from ._2368 import CoordinateSystemWithSelection
    from ._2369 import CreateConnectedComponentOptions
    from ._2370 import DegreeOfFreedomBoundaryCondition
    from ._2371 import DegreeOfFreedomBoundaryConditionAngular
    from ._2372 import DegreeOfFreedomBoundaryConditionLinear
    from ._2373 import ElectricMachineDataSet
    from ._2374 import ElectricMachineDynamicLoadData
    from ._2375 import ElementFaceGroupWithSelection
    from ._2376 import ElementPropertiesWithSelection
    from ._2377 import FEEntityGroupWithSelection
    from ._2378 import FEExportSettings
    from ._2379 import FEPartDRIVASurfaceSelection
    from ._2380 import FEPartWithBatchOptions
    from ._2381 import FEStiffnessGeometry
    from ._2382 import FEStiffnessTester
    from ._2383 import FESubstructure
    from ._2384 import FESubstructureExportOptions
    from ._2385 import FESubstructureNode
    from ._2386 import FESubstructureNodeModeShape
    from ._2387 import FESubstructureNodeModeShapes
    from ._2388 import FESubstructureType
    from ._2389 import FESubstructureWithBatchOptions
    from ._2390 import FESubstructureWithSelection
    from ._2391 import FESubstructureWithSelectionComponents
    from ._2392 import FESubstructureWithSelectionForHarmonicAnalysis
    from ._2393 import FESubstructureWithSelectionForModalAnalysis
    from ._2394 import FESubstructureWithSelectionForStaticAnalysis
    from ._2395 import GearMeshingOptions
    from ._2396 import IndependentMASTACreatedCondensationNode
    from ._2397 import LinkComponentAxialPositionErrorReporter
    from ._2398 import LinkNodeSource
    from ._2399 import MaterialPropertiesWithSelection
    from ._2400 import NodeBoundaryConditionStaticAnalysis
    from ._2401 import NodeGroupWithSelection
    from ._2402 import NodeSelectionDepthOption
    from ._2403 import OptionsWhenExternalFEFileAlreadyExists
    from ._2404 import PerLinkExportOptions
    from ._2405 import PerNodeExportOptions
    from ._2406 import RaceBearingFE
    from ._2407 import RaceBearingFESystemDeflection
    from ._2408 import RaceBearingFEWithSelection
    from ._2409 import ReplacedShaftSelectionHelper
    from ._2410 import SystemDeflectionFEExportOptions
    from ._2411 import ThermalExpansionOption
else:
    import_structure = {
        "_2355": ["AlignConnectedComponentOptions"],
        "_2356": ["AlignmentMethod"],
        "_2357": ["AlignmentMethodForRaceBearing"],
        "_2358": ["AlignmentUsingAxialNodePositions"],
        "_2359": ["AngleSource"],
        "_2360": ["BaseFEWithSelection"],
        "_2361": ["BatchOperations"],
        "_2362": ["BearingNodeAlignmentOption"],
        "_2363": ["BearingNodeOption"],
        "_2364": ["BearingRaceNodeLink"],
        "_2365": ["BearingRacePosition"],
        "_2366": ["ComponentOrientationOption"],
        "_2367": ["ContactPairWithSelection"],
        "_2368": ["CoordinateSystemWithSelection"],
        "_2369": ["CreateConnectedComponentOptions"],
        "_2370": ["DegreeOfFreedomBoundaryCondition"],
        "_2371": ["DegreeOfFreedomBoundaryConditionAngular"],
        "_2372": ["DegreeOfFreedomBoundaryConditionLinear"],
        "_2373": ["ElectricMachineDataSet"],
        "_2374": ["ElectricMachineDynamicLoadData"],
        "_2375": ["ElementFaceGroupWithSelection"],
        "_2376": ["ElementPropertiesWithSelection"],
        "_2377": ["FEEntityGroupWithSelection"],
        "_2378": ["FEExportSettings"],
        "_2379": ["FEPartDRIVASurfaceSelection"],
        "_2380": ["FEPartWithBatchOptions"],
        "_2381": ["FEStiffnessGeometry"],
        "_2382": ["FEStiffnessTester"],
        "_2383": ["FESubstructure"],
        "_2384": ["FESubstructureExportOptions"],
        "_2385": ["FESubstructureNode"],
        "_2386": ["FESubstructureNodeModeShape"],
        "_2387": ["FESubstructureNodeModeShapes"],
        "_2388": ["FESubstructureType"],
        "_2389": ["FESubstructureWithBatchOptions"],
        "_2390": ["FESubstructureWithSelection"],
        "_2391": ["FESubstructureWithSelectionComponents"],
        "_2392": ["FESubstructureWithSelectionForHarmonicAnalysis"],
        "_2393": ["FESubstructureWithSelectionForModalAnalysis"],
        "_2394": ["FESubstructureWithSelectionForStaticAnalysis"],
        "_2395": ["GearMeshingOptions"],
        "_2396": ["IndependentMASTACreatedCondensationNode"],
        "_2397": ["LinkComponentAxialPositionErrorReporter"],
        "_2398": ["LinkNodeSource"],
        "_2399": ["MaterialPropertiesWithSelection"],
        "_2400": ["NodeBoundaryConditionStaticAnalysis"],
        "_2401": ["NodeGroupWithSelection"],
        "_2402": ["NodeSelectionDepthOption"],
        "_2403": ["OptionsWhenExternalFEFileAlreadyExists"],
        "_2404": ["PerLinkExportOptions"],
        "_2405": ["PerNodeExportOptions"],
        "_2406": ["RaceBearingFE"],
        "_2407": ["RaceBearingFESystemDeflection"],
        "_2408": ["RaceBearingFEWithSelection"],
        "_2409": ["ReplacedShaftSelectionHelper"],
        "_2410": ["SystemDeflectionFEExportOptions"],
        "_2411": ["ThermalExpansionOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AlignConnectedComponentOptions",
    "AlignmentMethod",
    "AlignmentMethodForRaceBearing",
    "AlignmentUsingAxialNodePositions",
    "AngleSource",
    "BaseFEWithSelection",
    "BatchOperations",
    "BearingNodeAlignmentOption",
    "BearingNodeOption",
    "BearingRaceNodeLink",
    "BearingRacePosition",
    "ComponentOrientationOption",
    "ContactPairWithSelection",
    "CoordinateSystemWithSelection",
    "CreateConnectedComponentOptions",
    "DegreeOfFreedomBoundaryCondition",
    "DegreeOfFreedomBoundaryConditionAngular",
    "DegreeOfFreedomBoundaryConditionLinear",
    "ElectricMachineDataSet",
    "ElectricMachineDynamicLoadData",
    "ElementFaceGroupWithSelection",
    "ElementPropertiesWithSelection",
    "FEEntityGroupWithSelection",
    "FEExportSettings",
    "FEPartDRIVASurfaceSelection",
    "FEPartWithBatchOptions",
    "FEStiffnessGeometry",
    "FEStiffnessTester",
    "FESubstructure",
    "FESubstructureExportOptions",
    "FESubstructureNode",
    "FESubstructureNodeModeShape",
    "FESubstructureNodeModeShapes",
    "FESubstructureType",
    "FESubstructureWithBatchOptions",
    "FESubstructureWithSelection",
    "FESubstructureWithSelectionComponents",
    "FESubstructureWithSelectionForHarmonicAnalysis",
    "FESubstructureWithSelectionForModalAnalysis",
    "FESubstructureWithSelectionForStaticAnalysis",
    "GearMeshingOptions",
    "IndependentMASTACreatedCondensationNode",
    "LinkComponentAxialPositionErrorReporter",
    "LinkNodeSource",
    "MaterialPropertiesWithSelection",
    "NodeBoundaryConditionStaticAnalysis",
    "NodeGroupWithSelection",
    "NodeSelectionDepthOption",
    "OptionsWhenExternalFEFileAlreadyExists",
    "PerLinkExportOptions",
    "PerNodeExportOptions",
    "RaceBearingFE",
    "RaceBearingFESystemDeflection",
    "RaceBearingFEWithSelection",
    "ReplacedShaftSelectionHelper",
    "SystemDeflectionFEExportOptions",
    "ThermalExpansionOption",
)

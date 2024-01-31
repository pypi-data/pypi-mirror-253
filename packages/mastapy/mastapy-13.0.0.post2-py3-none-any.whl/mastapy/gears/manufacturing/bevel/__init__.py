"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._772 import AbstractTCA
    from ._773 import BevelMachineSettingOptimizationResult
    from ._774 import ConicalFlankDeviationsData
    from ._775 import ConicalGearManufacturingAnalysis
    from ._776 import ConicalGearManufacturingConfig
    from ._777 import ConicalGearMicroGeometryConfig
    from ._778 import ConicalGearMicroGeometryConfigBase
    from ._779 import ConicalMeshedGearManufacturingAnalysis
    from ._780 import ConicalMeshedWheelFlankManufacturingConfig
    from ._781 import ConicalMeshFlankManufacturingConfig
    from ._782 import ConicalMeshFlankMicroGeometryConfig
    from ._783 import ConicalMeshFlankNURBSMicroGeometryConfig
    from ._784 import ConicalMeshManufacturingAnalysis
    from ._785 import ConicalMeshManufacturingConfig
    from ._786 import ConicalMeshMicroGeometryConfig
    from ._787 import ConicalMeshMicroGeometryConfigBase
    from ._788 import ConicalPinionManufacturingConfig
    from ._789 import ConicalPinionMicroGeometryConfig
    from ._790 import ConicalSetManufacturingAnalysis
    from ._791 import ConicalSetManufacturingConfig
    from ._792 import ConicalSetMicroGeometryConfig
    from ._793 import ConicalSetMicroGeometryConfigBase
    from ._794 import ConicalWheelManufacturingConfig
    from ._795 import EaseOffBasedTCA
    from ._796 import FlankMeasurementBorder
    from ._797 import HypoidAdvancedLibrary
    from ._798 import MachineTypes
    from ._799 import ManufacturingMachine
    from ._800 import ManufacturingMachineDatabase
    from ._801 import PinionBevelGeneratingModifiedRollMachineSettings
    from ._802 import PinionBevelGeneratingTiltMachineSettings
    from ._803 import PinionConcave
    from ._804 import PinionConicalMachineSettingsSpecified
    from ._805 import PinionConvex
    from ._806 import PinionFinishMachineSettings
    from ._807 import PinionHypoidFormateTiltMachineSettings
    from ._808 import PinionHypoidGeneratingTiltMachineSettings
    from ._809 import PinionMachineSettingsSMT
    from ._810 import PinionRoughMachineSetting
    from ._811 import Wheel
    from ._812 import WheelFormatMachineTypes
else:
    import_structure = {
        "_772": ["AbstractTCA"],
        "_773": ["BevelMachineSettingOptimizationResult"],
        "_774": ["ConicalFlankDeviationsData"],
        "_775": ["ConicalGearManufacturingAnalysis"],
        "_776": ["ConicalGearManufacturingConfig"],
        "_777": ["ConicalGearMicroGeometryConfig"],
        "_778": ["ConicalGearMicroGeometryConfigBase"],
        "_779": ["ConicalMeshedGearManufacturingAnalysis"],
        "_780": ["ConicalMeshedWheelFlankManufacturingConfig"],
        "_781": ["ConicalMeshFlankManufacturingConfig"],
        "_782": ["ConicalMeshFlankMicroGeometryConfig"],
        "_783": ["ConicalMeshFlankNURBSMicroGeometryConfig"],
        "_784": ["ConicalMeshManufacturingAnalysis"],
        "_785": ["ConicalMeshManufacturingConfig"],
        "_786": ["ConicalMeshMicroGeometryConfig"],
        "_787": ["ConicalMeshMicroGeometryConfigBase"],
        "_788": ["ConicalPinionManufacturingConfig"],
        "_789": ["ConicalPinionMicroGeometryConfig"],
        "_790": ["ConicalSetManufacturingAnalysis"],
        "_791": ["ConicalSetManufacturingConfig"],
        "_792": ["ConicalSetMicroGeometryConfig"],
        "_793": ["ConicalSetMicroGeometryConfigBase"],
        "_794": ["ConicalWheelManufacturingConfig"],
        "_795": ["EaseOffBasedTCA"],
        "_796": ["FlankMeasurementBorder"],
        "_797": ["HypoidAdvancedLibrary"],
        "_798": ["MachineTypes"],
        "_799": ["ManufacturingMachine"],
        "_800": ["ManufacturingMachineDatabase"],
        "_801": ["PinionBevelGeneratingModifiedRollMachineSettings"],
        "_802": ["PinionBevelGeneratingTiltMachineSettings"],
        "_803": ["PinionConcave"],
        "_804": ["PinionConicalMachineSettingsSpecified"],
        "_805": ["PinionConvex"],
        "_806": ["PinionFinishMachineSettings"],
        "_807": ["PinionHypoidFormateTiltMachineSettings"],
        "_808": ["PinionHypoidGeneratingTiltMachineSettings"],
        "_809": ["PinionMachineSettingsSMT"],
        "_810": ["PinionRoughMachineSetting"],
        "_811": ["Wheel"],
        "_812": ["WheelFormatMachineTypes"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractTCA",
    "BevelMachineSettingOptimizationResult",
    "ConicalFlankDeviationsData",
    "ConicalGearManufacturingAnalysis",
    "ConicalGearManufacturingConfig",
    "ConicalGearMicroGeometryConfig",
    "ConicalGearMicroGeometryConfigBase",
    "ConicalMeshedGearManufacturingAnalysis",
    "ConicalMeshedWheelFlankManufacturingConfig",
    "ConicalMeshFlankManufacturingConfig",
    "ConicalMeshFlankMicroGeometryConfig",
    "ConicalMeshFlankNURBSMicroGeometryConfig",
    "ConicalMeshManufacturingAnalysis",
    "ConicalMeshManufacturingConfig",
    "ConicalMeshMicroGeometryConfig",
    "ConicalMeshMicroGeometryConfigBase",
    "ConicalPinionManufacturingConfig",
    "ConicalPinionMicroGeometryConfig",
    "ConicalSetManufacturingAnalysis",
    "ConicalSetManufacturingConfig",
    "ConicalSetMicroGeometryConfig",
    "ConicalSetMicroGeometryConfigBase",
    "ConicalWheelManufacturingConfig",
    "EaseOffBasedTCA",
    "FlankMeasurementBorder",
    "HypoidAdvancedLibrary",
    "MachineTypes",
    "ManufacturingMachine",
    "ManufacturingMachineDatabase",
    "PinionBevelGeneratingModifiedRollMachineSettings",
    "PinionBevelGeneratingTiltMachineSettings",
    "PinionConcave",
    "PinionConicalMachineSettingsSpecified",
    "PinionConvex",
    "PinionFinishMachineSettings",
    "PinionHypoidFormateTiltMachineSettings",
    "PinionHypoidGeneratingTiltMachineSettings",
    "PinionMachineSettingsSMT",
    "PinionRoughMachineSetting",
    "Wheel",
    "WheelFormatMachineTypes",
)

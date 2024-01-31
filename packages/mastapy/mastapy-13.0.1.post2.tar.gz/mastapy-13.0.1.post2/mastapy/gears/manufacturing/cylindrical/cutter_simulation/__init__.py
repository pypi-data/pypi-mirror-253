"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._731 import CutterSimulationCalc
    from ._732 import CylindricalCutterSimulatableGear
    from ._733 import CylindricalGearSpecification
    from ._734 import CylindricalManufacturedRealGearInMesh
    from ._735 import CylindricalManufacturedVirtualGearInMesh
    from ._736 import FinishCutterSimulation
    from ._737 import FinishStockPoint
    from ._738 import FormWheelGrindingSimulationCalculator
    from ._739 import GearCutterSimulation
    from ._740 import HobSimulationCalculator
    from ._741 import ManufacturingOperationConstraints
    from ._742 import ManufacturingProcessControls
    from ._743 import RackSimulationCalculator
    from ._744 import RoughCutterSimulation
    from ._745 import ShaperSimulationCalculator
    from ._746 import ShavingSimulationCalculator
    from ._747 import VirtualSimulationCalculator
    from ._748 import WormGrinderSimulationCalculator
else:
    import_structure = {
        "_731": ["CutterSimulationCalc"],
        "_732": ["CylindricalCutterSimulatableGear"],
        "_733": ["CylindricalGearSpecification"],
        "_734": ["CylindricalManufacturedRealGearInMesh"],
        "_735": ["CylindricalManufacturedVirtualGearInMesh"],
        "_736": ["FinishCutterSimulation"],
        "_737": ["FinishStockPoint"],
        "_738": ["FormWheelGrindingSimulationCalculator"],
        "_739": ["GearCutterSimulation"],
        "_740": ["HobSimulationCalculator"],
        "_741": ["ManufacturingOperationConstraints"],
        "_742": ["ManufacturingProcessControls"],
        "_743": ["RackSimulationCalculator"],
        "_744": ["RoughCutterSimulation"],
        "_745": ["ShaperSimulationCalculator"],
        "_746": ["ShavingSimulationCalculator"],
        "_747": ["VirtualSimulationCalculator"],
        "_748": ["WormGrinderSimulationCalculator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterSimulationCalc",
    "CylindricalCutterSimulatableGear",
    "CylindricalGearSpecification",
    "CylindricalManufacturedRealGearInMesh",
    "CylindricalManufacturedVirtualGearInMesh",
    "FinishCutterSimulation",
    "FinishStockPoint",
    "FormWheelGrindingSimulationCalculator",
    "GearCutterSimulation",
    "HobSimulationCalculator",
    "ManufacturingOperationConstraints",
    "ManufacturingProcessControls",
    "RackSimulationCalculator",
    "RoughCutterSimulation",
    "ShaperSimulationCalculator",
    "ShavingSimulationCalculator",
    "VirtualSimulationCalculator",
    "WormGrinderSimulationCalculator",
)

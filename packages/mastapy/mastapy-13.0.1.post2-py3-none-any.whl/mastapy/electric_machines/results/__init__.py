"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1320 import DynamicForceResults
    from ._1321 import EfficiencyResults
    from ._1322 import ElectricMachineDQModel
    from ._1323 import ElectricMachineMechanicalResults
    from ._1324 import ElectricMachineMechanicalResultsViewable
    from ._1325 import ElectricMachineResults
    from ._1326 import ElectricMachineResultsForConductorTurn
    from ._1327 import ElectricMachineResultsForConductorTurnAtTimeStep
    from ._1328 import ElectricMachineResultsForLineToLine
    from ._1329 import ElectricMachineResultsForOpenCircuitAndOnLoad
    from ._1330 import ElectricMachineResultsForPhase
    from ._1331 import ElectricMachineResultsForPhaseAtTimeStep
    from ._1332 import ElectricMachineResultsForStatorToothAtTimeStep
    from ._1333 import ElectricMachineResultsLineToLineAtTimeStep
    from ._1334 import ElectricMachineResultsTimeStep
    from ._1335 import ElectricMachineResultsTimeStepAtLocation
    from ._1336 import ElectricMachineResultsViewable
    from ._1337 import ElectricMachineForceViewOptions
    from ._1339 import LinearDQModel
    from ._1340 import MaximumTorqueResultsPoints
    from ._1341 import NonLinearDQModel
    from ._1342 import NonLinearDQModelGeneratorSettings
    from ._1343 import OnLoadElectricMachineResults
    from ._1344 import OpenCircuitElectricMachineResults
else:
    import_structure = {
        "_1320": ["DynamicForceResults"],
        "_1321": ["EfficiencyResults"],
        "_1322": ["ElectricMachineDQModel"],
        "_1323": ["ElectricMachineMechanicalResults"],
        "_1324": ["ElectricMachineMechanicalResultsViewable"],
        "_1325": ["ElectricMachineResults"],
        "_1326": ["ElectricMachineResultsForConductorTurn"],
        "_1327": ["ElectricMachineResultsForConductorTurnAtTimeStep"],
        "_1328": ["ElectricMachineResultsForLineToLine"],
        "_1329": ["ElectricMachineResultsForOpenCircuitAndOnLoad"],
        "_1330": ["ElectricMachineResultsForPhase"],
        "_1331": ["ElectricMachineResultsForPhaseAtTimeStep"],
        "_1332": ["ElectricMachineResultsForStatorToothAtTimeStep"],
        "_1333": ["ElectricMachineResultsLineToLineAtTimeStep"],
        "_1334": ["ElectricMachineResultsTimeStep"],
        "_1335": ["ElectricMachineResultsTimeStepAtLocation"],
        "_1336": ["ElectricMachineResultsViewable"],
        "_1337": ["ElectricMachineForceViewOptions"],
        "_1339": ["LinearDQModel"],
        "_1340": ["MaximumTorqueResultsPoints"],
        "_1341": ["NonLinearDQModel"],
        "_1342": ["NonLinearDQModelGeneratorSettings"],
        "_1343": ["OnLoadElectricMachineResults"],
        "_1344": ["OpenCircuitElectricMachineResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DynamicForceResults",
    "EfficiencyResults",
    "ElectricMachineDQModel",
    "ElectricMachineMechanicalResults",
    "ElectricMachineMechanicalResultsViewable",
    "ElectricMachineResults",
    "ElectricMachineResultsForConductorTurn",
    "ElectricMachineResultsForConductorTurnAtTimeStep",
    "ElectricMachineResultsForLineToLine",
    "ElectricMachineResultsForOpenCircuitAndOnLoad",
    "ElectricMachineResultsForPhase",
    "ElectricMachineResultsForPhaseAtTimeStep",
    "ElectricMachineResultsForStatorToothAtTimeStep",
    "ElectricMachineResultsLineToLineAtTimeStep",
    "ElectricMachineResultsTimeStep",
    "ElectricMachineResultsTimeStepAtLocation",
    "ElectricMachineResultsViewable",
    "ElectricMachineForceViewOptions",
    "LinearDQModel",
    "MaximumTorqueResultsPoints",
    "NonLinearDQModel",
    "NonLinearDQModelGeneratorSettings",
    "OnLoadElectricMachineResults",
    "OpenCircuitElectricMachineResults",
)

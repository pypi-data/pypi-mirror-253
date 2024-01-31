"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1345 import BasicDynamicForceLoadCase
    from ._1346 import DynamicForceAnalysis
    from ._1347 import DynamicForceLoadCase
    from ._1348 import DynamicForcesOperatingPoint
    from ._1349 import EfficiencyMapAnalysis
    from ._1350 import EfficiencyMapLoadCase
    from ._1351 import ElectricMachineAnalysis
    from ._1352 import ElectricMachineBasicMechanicalLossSettings
    from ._1353 import ElectricMachineControlStrategy
    from ._1354 import ElectricMachineEfficiencyMapSettings
    from ._1355 import ElectricMachineFEAnalysis
    from ._1356 import ElectricMachineFEMechanicalAnalysis
    from ._1357 import ElectricMachineLoadCase
    from ._1358 import ElectricMachineLoadCaseBase
    from ._1359 import ElectricMachineLoadCaseGroup
    from ._1360 import ElectricMachineMechanicalLoadCase
    from ._1361 import EndWindingInductanceMethod
    from ._1362 import LeadingOrLagging
    from ._1363 import LoadCaseType
    from ._1364 import LoadCaseTypeSelector
    from ._1365 import MotoringOrGenerating
    from ._1366 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1367 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1368 import OperatingPointsSpecificationMethod
    from ._1369 import SingleOperatingPointAnalysis
    from ._1370 import SlotDetailForAnalysis
    from ._1371 import SpecifyTorqueOrCurrent
    from ._1372 import SpeedPointsDistribution
    from ._1373 import SpeedTorqueCurveAnalysis
    from ._1374 import SpeedTorqueCurveLoadCase
    from ._1375 import SpeedTorqueLoadCase
    from ._1376 import Temperatures
else:
    import_structure = {
        "_1345": ["BasicDynamicForceLoadCase"],
        "_1346": ["DynamicForceAnalysis"],
        "_1347": ["DynamicForceLoadCase"],
        "_1348": ["DynamicForcesOperatingPoint"],
        "_1349": ["EfficiencyMapAnalysis"],
        "_1350": ["EfficiencyMapLoadCase"],
        "_1351": ["ElectricMachineAnalysis"],
        "_1352": ["ElectricMachineBasicMechanicalLossSettings"],
        "_1353": ["ElectricMachineControlStrategy"],
        "_1354": ["ElectricMachineEfficiencyMapSettings"],
        "_1355": ["ElectricMachineFEAnalysis"],
        "_1356": ["ElectricMachineFEMechanicalAnalysis"],
        "_1357": ["ElectricMachineLoadCase"],
        "_1358": ["ElectricMachineLoadCaseBase"],
        "_1359": ["ElectricMachineLoadCaseGroup"],
        "_1360": ["ElectricMachineMechanicalLoadCase"],
        "_1361": ["EndWindingInductanceMethod"],
        "_1362": ["LeadingOrLagging"],
        "_1363": ["LoadCaseType"],
        "_1364": ["LoadCaseTypeSelector"],
        "_1365": ["MotoringOrGenerating"],
        "_1366": ["NonLinearDQModelMultipleOperatingPointsLoadCase"],
        "_1367": ["NumberOfStepsPerOperatingPointSpecificationMethod"],
        "_1368": ["OperatingPointsSpecificationMethod"],
        "_1369": ["SingleOperatingPointAnalysis"],
        "_1370": ["SlotDetailForAnalysis"],
        "_1371": ["SpecifyTorqueOrCurrent"],
        "_1372": ["SpeedPointsDistribution"],
        "_1373": ["SpeedTorqueCurveAnalysis"],
        "_1374": ["SpeedTorqueCurveLoadCase"],
        "_1375": ["SpeedTorqueLoadCase"],
        "_1376": ["Temperatures"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicDynamicForceLoadCase",
    "DynamicForceAnalysis",
    "DynamicForceLoadCase",
    "DynamicForcesOperatingPoint",
    "EfficiencyMapAnalysis",
    "EfficiencyMapLoadCase",
    "ElectricMachineAnalysis",
    "ElectricMachineBasicMechanicalLossSettings",
    "ElectricMachineControlStrategy",
    "ElectricMachineEfficiencyMapSettings",
    "ElectricMachineFEAnalysis",
    "ElectricMachineFEMechanicalAnalysis",
    "ElectricMachineLoadCase",
    "ElectricMachineLoadCaseBase",
    "ElectricMachineLoadCaseGroup",
    "ElectricMachineMechanicalLoadCase",
    "EndWindingInductanceMethod",
    "LeadingOrLagging",
    "LoadCaseType",
    "LoadCaseTypeSelector",
    "MotoringOrGenerating",
    "NonLinearDQModelMultipleOperatingPointsLoadCase",
    "NumberOfStepsPerOperatingPointSpecificationMethod",
    "OperatingPointsSpecificationMethod",
    "SingleOperatingPointAnalysis",
    "SlotDetailForAnalysis",
    "SpecifyTorqueOrCurrent",
    "SpeedPointsDistribution",
    "SpeedTorqueCurveAnalysis",
    "SpeedTorqueCurveLoadCase",
    "SpeedTorqueLoadCase",
    "Temperatures",
)

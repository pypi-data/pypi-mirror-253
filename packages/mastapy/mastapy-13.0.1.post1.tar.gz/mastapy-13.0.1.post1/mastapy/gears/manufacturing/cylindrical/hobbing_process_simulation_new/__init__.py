"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._658 import ActiveProcessMethod
    from ._659 import AnalysisMethod
    from ._660 import CalculateLeadDeviationAccuracy
    from ._661 import CalculatePitchDeviationAccuracy
    from ._662 import CalculateProfileDeviationAccuracy
    from ._663 import CentreDistanceOffsetMethod
    from ._664 import CutterHeadSlideError
    from ._665 import GearMountingError
    from ._666 import HobbingProcessCalculation
    from ._667 import HobbingProcessGearShape
    from ._668 import HobbingProcessLeadCalculation
    from ._669 import HobbingProcessMarkOnShaft
    from ._670 import HobbingProcessPitchCalculation
    from ._671 import HobbingProcessProfileCalculation
    from ._672 import HobbingProcessSimulationInput
    from ._673 import HobbingProcessSimulationNew
    from ._674 import HobbingProcessSimulationViewModel
    from ._675 import HobbingProcessTotalModificationCalculation
    from ._676 import HobManufactureError
    from ._677 import HobResharpeningError
    from ._678 import ManufacturedQualityGrade
    from ._679 import MountingError
    from ._680 import ProcessCalculation
    from ._681 import ProcessGearShape
    from ._682 import ProcessLeadCalculation
    from ._683 import ProcessPitchCalculation
    from ._684 import ProcessProfileCalculation
    from ._685 import ProcessSimulationInput
    from ._686 import ProcessSimulationNew
    from ._687 import ProcessSimulationViewModel
    from ._688 import ProcessTotalModificationCalculation
    from ._689 import RackManufactureError
    from ._690 import RackMountingError
    from ._691 import WormGrinderManufactureError
    from ._692 import WormGrindingCutterCalculation
    from ._693 import WormGrindingLeadCalculation
    from ._694 import WormGrindingProcessCalculation
    from ._695 import WormGrindingProcessGearShape
    from ._696 import WormGrindingProcessMarkOnShaft
    from ._697 import WormGrindingProcessPitchCalculation
    from ._698 import WormGrindingProcessProfileCalculation
    from ._699 import WormGrindingProcessSimulationInput
    from ._700 import WormGrindingProcessSimulationNew
    from ._701 import WormGrindingProcessSimulationViewModel
    from ._702 import WormGrindingProcessTotalModificationCalculation
else:
    import_structure = {
        "_658": ["ActiveProcessMethod"],
        "_659": ["AnalysisMethod"],
        "_660": ["CalculateLeadDeviationAccuracy"],
        "_661": ["CalculatePitchDeviationAccuracy"],
        "_662": ["CalculateProfileDeviationAccuracy"],
        "_663": ["CentreDistanceOffsetMethod"],
        "_664": ["CutterHeadSlideError"],
        "_665": ["GearMountingError"],
        "_666": ["HobbingProcessCalculation"],
        "_667": ["HobbingProcessGearShape"],
        "_668": ["HobbingProcessLeadCalculation"],
        "_669": ["HobbingProcessMarkOnShaft"],
        "_670": ["HobbingProcessPitchCalculation"],
        "_671": ["HobbingProcessProfileCalculation"],
        "_672": ["HobbingProcessSimulationInput"],
        "_673": ["HobbingProcessSimulationNew"],
        "_674": ["HobbingProcessSimulationViewModel"],
        "_675": ["HobbingProcessTotalModificationCalculation"],
        "_676": ["HobManufactureError"],
        "_677": ["HobResharpeningError"],
        "_678": ["ManufacturedQualityGrade"],
        "_679": ["MountingError"],
        "_680": ["ProcessCalculation"],
        "_681": ["ProcessGearShape"],
        "_682": ["ProcessLeadCalculation"],
        "_683": ["ProcessPitchCalculation"],
        "_684": ["ProcessProfileCalculation"],
        "_685": ["ProcessSimulationInput"],
        "_686": ["ProcessSimulationNew"],
        "_687": ["ProcessSimulationViewModel"],
        "_688": ["ProcessTotalModificationCalculation"],
        "_689": ["RackManufactureError"],
        "_690": ["RackMountingError"],
        "_691": ["WormGrinderManufactureError"],
        "_692": ["WormGrindingCutterCalculation"],
        "_693": ["WormGrindingLeadCalculation"],
        "_694": ["WormGrindingProcessCalculation"],
        "_695": ["WormGrindingProcessGearShape"],
        "_696": ["WormGrindingProcessMarkOnShaft"],
        "_697": ["WormGrindingProcessPitchCalculation"],
        "_698": ["WormGrindingProcessProfileCalculation"],
        "_699": ["WormGrindingProcessSimulationInput"],
        "_700": ["WormGrindingProcessSimulationNew"],
        "_701": ["WormGrindingProcessSimulationViewModel"],
        "_702": ["WormGrindingProcessTotalModificationCalculation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveProcessMethod",
    "AnalysisMethod",
    "CalculateLeadDeviationAccuracy",
    "CalculatePitchDeviationAccuracy",
    "CalculateProfileDeviationAccuracy",
    "CentreDistanceOffsetMethod",
    "CutterHeadSlideError",
    "GearMountingError",
    "HobbingProcessCalculation",
    "HobbingProcessGearShape",
    "HobbingProcessLeadCalculation",
    "HobbingProcessMarkOnShaft",
    "HobbingProcessPitchCalculation",
    "HobbingProcessProfileCalculation",
    "HobbingProcessSimulationInput",
    "HobbingProcessSimulationNew",
    "HobbingProcessSimulationViewModel",
    "HobbingProcessTotalModificationCalculation",
    "HobManufactureError",
    "HobResharpeningError",
    "ManufacturedQualityGrade",
    "MountingError",
    "ProcessCalculation",
    "ProcessGearShape",
    "ProcessLeadCalculation",
    "ProcessPitchCalculation",
    "ProcessProfileCalculation",
    "ProcessSimulationInput",
    "ProcessSimulationNew",
    "ProcessSimulationViewModel",
    "ProcessTotalModificationCalculation",
    "RackManufactureError",
    "RackMountingError",
    "WormGrinderManufactureError",
    "WormGrindingCutterCalculation",
    "WormGrindingLeadCalculation",
    "WormGrindingProcessCalculation",
    "WormGrindingProcessGearShape",
    "WormGrindingProcessMarkOnShaft",
    "WormGrindingProcessPitchCalculation",
    "WormGrindingProcessProfileCalculation",
    "WormGrindingProcessSimulationInput",
    "WormGrindingProcessSimulationNew",
    "WormGrindingProcessSimulationViewModel",
    "WormGrindingProcessTotalModificationCalculation",
)

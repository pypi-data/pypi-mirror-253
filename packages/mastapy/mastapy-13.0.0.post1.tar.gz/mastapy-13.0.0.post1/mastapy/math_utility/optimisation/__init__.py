"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1538 import AbstractOptimisable
    from ._1539 import DesignSpaceSearchStrategyDatabase
    from ._1540 import InputSetter
    from ._1541 import MicroGeometryDesignSpaceSearchStrategyDatabase
    from ._1542 import Optimisable
    from ._1543 import OptimisationHistory
    from ._1544 import OptimizationInput
    from ._1545 import OptimizationVariable
    from ._1546 import ParetoOptimisationFilter
    from ._1547 import ParetoOptimisationInput
    from ._1548 import ParetoOptimisationOutput
    from ._1549 import ParetoOptimisationStrategy
    from ._1550 import ParetoOptimisationStrategyBars
    from ._1551 import ParetoOptimisationStrategyChartInformation
    from ._1552 import ParetoOptimisationStrategyDatabase
    from ._1553 import ParetoOptimisationVariable
    from ._1554 import ParetoOptimisationVariableBase
    from ._1555 import PropertyTargetForDominantCandidateSearch
    from ._1556 import ReportingOptimizationInput
    from ._1557 import SpecifyOptimisationInputAs
    from ._1558 import TargetingPropertyTo
else:
    import_structure = {
        "_1538": ["AbstractOptimisable"],
        "_1539": ["DesignSpaceSearchStrategyDatabase"],
        "_1540": ["InputSetter"],
        "_1541": ["MicroGeometryDesignSpaceSearchStrategyDatabase"],
        "_1542": ["Optimisable"],
        "_1543": ["OptimisationHistory"],
        "_1544": ["OptimizationInput"],
        "_1545": ["OptimizationVariable"],
        "_1546": ["ParetoOptimisationFilter"],
        "_1547": ["ParetoOptimisationInput"],
        "_1548": ["ParetoOptimisationOutput"],
        "_1549": ["ParetoOptimisationStrategy"],
        "_1550": ["ParetoOptimisationStrategyBars"],
        "_1551": ["ParetoOptimisationStrategyChartInformation"],
        "_1552": ["ParetoOptimisationStrategyDatabase"],
        "_1553": ["ParetoOptimisationVariable"],
        "_1554": ["ParetoOptimisationVariableBase"],
        "_1555": ["PropertyTargetForDominantCandidateSearch"],
        "_1556": ["ReportingOptimizationInput"],
        "_1557": ["SpecifyOptimisationInputAs"],
        "_1558": ["TargetingPropertyTo"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractOptimisable",
    "DesignSpaceSearchStrategyDatabase",
    "InputSetter",
    "MicroGeometryDesignSpaceSearchStrategyDatabase",
    "Optimisable",
    "OptimisationHistory",
    "OptimizationInput",
    "OptimizationVariable",
    "ParetoOptimisationFilter",
    "ParetoOptimisationInput",
    "ParetoOptimisationOutput",
    "ParetoOptimisationStrategy",
    "ParetoOptimisationStrategyBars",
    "ParetoOptimisationStrategyChartInformation",
    "ParetoOptimisationStrategyDatabase",
    "ParetoOptimisationVariable",
    "ParetoOptimisationVariableBase",
    "PropertyTargetForDominantCandidateSearch",
    "ReportingOptimizationInput",
    "SpecifyOptimisationInputAs",
    "TargetingPropertyTo",
)

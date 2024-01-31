"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._168 import ContactType
    from ._169 import ElectricMachineAnalysisPeriod
    from ._170 import ElmerResults
    from ._171 import ElmerResultsFromElectroMagneticAnalysis
    from ._172 import ElmerResultsViewable
    from ._173 import ElmerResultType
    from ._174 import MechanicalContactSpecification
else:
    import_structure = {
        "_168": ["ContactType"],
        "_169": ["ElectricMachineAnalysisPeriod"],
        "_170": ["ElmerResults"],
        "_171": ["ElmerResultsFromElectroMagneticAnalysis"],
        "_172": ["ElmerResultsViewable"],
        "_173": ["ElmerResultType"],
        "_174": ["MechanicalContactSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactType",
    "ElectricMachineAnalysisPeriod",
    "ElmerResults",
    "ElmerResultsFromElectroMagneticAnalysis",
    "ElmerResultsViewable",
    "ElmerResultType",
    "MechanicalContactSpecification",
)

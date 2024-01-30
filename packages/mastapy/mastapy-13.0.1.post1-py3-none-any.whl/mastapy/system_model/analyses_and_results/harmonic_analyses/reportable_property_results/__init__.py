"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5854 import AbstractSingleWhineAnalysisResultsPropertyAccessor
    from ._5855 import DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic
    from ._5856 import DataPointForResponseOfANodeAtAFrequencyToAHarmonic
    from ._5857 import FEPartHarmonicAnalysisResultsPropertyAccessor
    from ._5858 import FEPartSingleWhineAnalysisResultsPropertyAccessor
    from ._5859 import HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
    from ._5860 import HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
    from ._5861 import HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic
    from ._5862 import HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
    from ._5863 import HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
    from ._5864 import HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
    from ._5865 import HarmonicAnalysisResultsPropertyAccessor
    from ._5866 import ResultsForMultipleOrders
    from ._5867 import ResultsForMultipleOrdersForFESurface
    from ._5868 import ResultsForMultipleOrdersForGroups
    from ._5869 import ResultsForOrder
    from ._5870 import ResultsForOrderIncludingGroups
    from ._5871 import ResultsForOrderIncludingNodes
    from ._5872 import ResultsForOrderIncludingSurfaces
    from ._5873 import ResultsForResponseOfAComponentOrSurfaceInAHarmonic
    from ._5874 import ResultsForResponseOfANodeOnAHarmonic
    from ._5875 import ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic
    from ._5876 import RootAssemblyHarmonicAnalysisResultsPropertyAccessor
    from ._5877 import RootAssemblySingleWhineAnalysisResultsPropertyAccessor
    from ._5878 import SingleWhineAnalysisResultsPropertyAccessor
else:
    import_structure = {
        "_5854": ["AbstractSingleWhineAnalysisResultsPropertyAccessor"],
        "_5855": ["DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic"],
        "_5856": ["DataPointForResponseOfANodeAtAFrequencyToAHarmonic"],
        "_5857": ["FEPartHarmonicAnalysisResultsPropertyAccessor"],
        "_5858": ["FEPartSingleWhineAnalysisResultsPropertyAccessor"],
        "_5859": ["HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic"],
        "_5860": ["HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic"],
        "_5861": ["HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic"],
        "_5862": ["HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic"],
        "_5863": ["HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic"],
        "_5864": ["HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic"],
        "_5865": ["HarmonicAnalysisResultsPropertyAccessor"],
        "_5866": ["ResultsForMultipleOrders"],
        "_5867": ["ResultsForMultipleOrdersForFESurface"],
        "_5868": ["ResultsForMultipleOrdersForGroups"],
        "_5869": ["ResultsForOrder"],
        "_5870": ["ResultsForOrderIncludingGroups"],
        "_5871": ["ResultsForOrderIncludingNodes"],
        "_5872": ["ResultsForOrderIncludingSurfaces"],
        "_5873": ["ResultsForResponseOfAComponentOrSurfaceInAHarmonic"],
        "_5874": ["ResultsForResponseOfANodeOnAHarmonic"],
        "_5875": ["ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic"],
        "_5876": ["RootAssemblyHarmonicAnalysisResultsPropertyAccessor"],
        "_5877": ["RootAssemblySingleWhineAnalysisResultsPropertyAccessor"],
        "_5878": ["SingleWhineAnalysisResultsPropertyAccessor"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractSingleWhineAnalysisResultsPropertyAccessor",
    "DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic",
    "DataPointForResponseOfANodeAtAFrequencyToAHarmonic",
    "FEPartHarmonicAnalysisResultsPropertyAccessor",
    "FEPartSingleWhineAnalysisResultsPropertyAccessor",
    "HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic",
    "HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic",
    "HarmonicAnalysisResultsPropertyAccessor",
    "ResultsForMultipleOrders",
    "ResultsForMultipleOrdersForFESurface",
    "ResultsForMultipleOrdersForGroups",
    "ResultsForOrder",
    "ResultsForOrderIncludingGroups",
    "ResultsForOrderIncludingNodes",
    "ResultsForOrderIncludingSurfaces",
    "ResultsForResponseOfAComponentOrSurfaceInAHarmonic",
    "ResultsForResponseOfANodeOnAHarmonic",
    "ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic",
    "RootAssemblyHarmonicAnalysisResultsPropertyAccessor",
    "RootAssemblySingleWhineAnalysisResultsPropertyAccessor",
    "SingleWhineAnalysisResultsPropertyAccessor",
)

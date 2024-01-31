"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5853 import AbstractSingleWhineAnalysisResultsPropertyAccessor
    from ._5854 import DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic
    from ._5855 import DataPointForResponseOfANodeAtAFrequencyToAHarmonic
    from ._5856 import FEPartHarmonicAnalysisResultsPropertyAccessor
    from ._5857 import FEPartSingleWhineAnalysisResultsPropertyAccessor
    from ._5858 import HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic
    from ._5859 import HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic
    from ._5860 import HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic
    from ._5861 import HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic
    from ._5862 import HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic
    from ._5863 import HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
    from ._5864 import HarmonicAnalysisResultsPropertyAccessor
    from ._5865 import ResultsForMultipleOrders
    from ._5866 import ResultsForMultipleOrdersForFESurface
    from ._5867 import ResultsForMultipleOrdersForGroups
    from ._5868 import ResultsForOrder
    from ._5869 import ResultsForOrderIncludingGroups
    from ._5870 import ResultsForOrderIncludingNodes
    from ._5871 import ResultsForOrderIncludingSurfaces
    from ._5872 import ResultsForResponseOfAComponentOrSurfaceInAHarmonic
    from ._5873 import ResultsForResponseOfANodeOnAHarmonic
    from ._5874 import ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic
    from ._5875 import RootAssemblyHarmonicAnalysisResultsPropertyAccessor
    from ._5876 import RootAssemblySingleWhineAnalysisResultsPropertyAccessor
    from ._5877 import SingleWhineAnalysisResultsPropertyAccessor
else:
    import_structure = {
        "_5853": ["AbstractSingleWhineAnalysisResultsPropertyAccessor"],
        "_5854": ["DataPointForResponseOfAComponentOrSurfaceAtAFrequencyToAHarmonic"],
        "_5855": ["DataPointForResponseOfANodeAtAFrequencyToAHarmonic"],
        "_5856": ["FEPartHarmonicAnalysisResultsPropertyAccessor"],
        "_5857": ["FEPartSingleWhineAnalysisResultsPropertyAccessor"],
        "_5858": ["HarmonicAnalysisCombinedForMultipleSurfacesWithinAHarmonic"],
        "_5859": ["HarmonicAnalysisResultsBrokenDownByComponentWithinAHarmonic"],
        "_5860": ["HarmonicAnalysisResultsBrokenDownByGroupsWithinAHarmonic"],
        "_5861": ["HarmonicAnalysisResultsBrokenDownByLocationWithinAHarmonic"],
        "_5862": ["HarmonicAnalysisResultsBrokenDownByNodeWithinAHarmonic"],
        "_5863": ["HarmonicAnalysisResultsBrokenDownBySurfaceWithinAHarmonic"],
        "_5864": ["HarmonicAnalysisResultsPropertyAccessor"],
        "_5865": ["ResultsForMultipleOrders"],
        "_5866": ["ResultsForMultipleOrdersForFESurface"],
        "_5867": ["ResultsForMultipleOrdersForGroups"],
        "_5868": ["ResultsForOrder"],
        "_5869": ["ResultsForOrderIncludingGroups"],
        "_5870": ["ResultsForOrderIncludingNodes"],
        "_5871": ["ResultsForOrderIncludingSurfaces"],
        "_5872": ["ResultsForResponseOfAComponentOrSurfaceInAHarmonic"],
        "_5873": ["ResultsForResponseOfANodeOnAHarmonic"],
        "_5874": ["ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic"],
        "_5875": ["RootAssemblyHarmonicAnalysisResultsPropertyAccessor"],
        "_5876": ["RootAssemblySingleWhineAnalysisResultsPropertyAccessor"],
        "_5877": ["SingleWhineAnalysisResultsPropertyAccessor"],
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

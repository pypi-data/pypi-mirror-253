"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1215 import AbstractGearAnalysis
    from ._1216 import AbstractGearMeshAnalysis
    from ._1217 import AbstractGearSetAnalysis
    from ._1218 import GearDesignAnalysis
    from ._1219 import GearImplementationAnalysis
    from ._1220 import GearImplementationAnalysisDutyCycle
    from ._1221 import GearImplementationDetail
    from ._1222 import GearMeshDesignAnalysis
    from ._1223 import GearMeshImplementationAnalysis
    from ._1224 import GearMeshImplementationAnalysisDutyCycle
    from ._1225 import GearMeshImplementationDetail
    from ._1226 import GearSetDesignAnalysis
    from ._1227 import GearSetGroupDutyCycle
    from ._1228 import GearSetImplementationAnalysis
    from ._1229 import GearSetImplementationAnalysisAbstract
    from ._1230 import GearSetImplementationAnalysisDutyCycle
    from ._1231 import GearSetImplementationDetail
else:
    import_structure = {
        "_1215": ["AbstractGearAnalysis"],
        "_1216": ["AbstractGearMeshAnalysis"],
        "_1217": ["AbstractGearSetAnalysis"],
        "_1218": ["GearDesignAnalysis"],
        "_1219": ["GearImplementationAnalysis"],
        "_1220": ["GearImplementationAnalysisDutyCycle"],
        "_1221": ["GearImplementationDetail"],
        "_1222": ["GearMeshDesignAnalysis"],
        "_1223": ["GearMeshImplementationAnalysis"],
        "_1224": ["GearMeshImplementationAnalysisDutyCycle"],
        "_1225": ["GearMeshImplementationDetail"],
        "_1226": ["GearSetDesignAnalysis"],
        "_1227": ["GearSetGroupDutyCycle"],
        "_1228": ["GearSetImplementationAnalysis"],
        "_1229": ["GearSetImplementationAnalysisAbstract"],
        "_1230": ["GearSetImplementationAnalysisDutyCycle"],
        "_1231": ["GearSetImplementationDetail"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearAnalysis",
    "AbstractGearMeshAnalysis",
    "AbstractGearSetAnalysis",
    "GearDesignAnalysis",
    "GearImplementationAnalysis",
    "GearImplementationAnalysisDutyCycle",
    "GearImplementationDetail",
    "GearMeshDesignAnalysis",
    "GearMeshImplementationAnalysis",
    "GearMeshImplementationAnalysisDutyCycle",
    "GearMeshImplementationDetail",
    "GearSetDesignAnalysis",
    "GearSetGroupDutyCycle",
    "GearSetImplementationAnalysis",
    "GearSetImplementationAnalysisAbstract",
    "GearSetImplementationAnalysisDutyCycle",
    "GearSetImplementationDetail",
)

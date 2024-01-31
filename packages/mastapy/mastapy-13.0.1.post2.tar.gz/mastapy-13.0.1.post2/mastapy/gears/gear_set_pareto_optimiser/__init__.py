"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._902 import BarForPareto
    from ._903 import CandidateDisplayChoice
    from ._904 import ChartInfoBase
    from ._905 import CylindricalGearSetParetoOptimiser
    from ._906 import DesignSpaceSearchBase
    from ._907 import DesignSpaceSearchCandidateBase
    from ._908 import FaceGearSetParetoOptimiser
    from ._909 import GearNameMapper
    from ._910 import GearNamePicker
    from ._911 import GearSetOptimiserCandidate
    from ._912 import GearSetParetoOptimiser
    from ._913 import HypoidGearSetParetoOptimiser
    from ._914 import InputSliderForPareto
    from ._915 import LargerOrSmaller
    from ._916 import MicroGeometryDesignSpaceSearch
    from ._917 import MicroGeometryDesignSpaceSearchCandidate
    from ._918 import MicroGeometryDesignSpaceSearchChartInformation
    from ._919 import MicroGeometryGearSetDesignSpaceSearch
    from ._920 import MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
    from ._921 import MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
    from ._922 import OptimisationTarget
    from ._923 import ParetoConicalRatingOptimisationStrategyDatabase
    from ._924 import ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
    from ._925 import ParetoCylindricalGearSetOptimisationStrategyDatabase
    from ._926 import ParetoCylindricalRatingOptimisationStrategyDatabase
    from ._927 import ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
    from ._928 import ParetoFaceGearSetOptimisationStrategyDatabase
    from ._929 import ParetoFaceRatingOptimisationStrategyDatabase
    from ._930 import ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
    from ._931 import ParetoHypoidGearSetOptimisationStrategyDatabase
    from ._932 import ParetoOptimiserChartInformation
    from ._933 import ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._934 import ParetoSpiralBevelGearSetOptimisationStrategyDatabase
    from ._935 import ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._936 import ParetoStraightBevelGearSetOptimisationStrategyDatabase
    from ._937 import ReasonsForInvalidDesigns
    from ._938 import SpiralBevelGearSetParetoOptimiser
    from ._939 import StraightBevelGearSetParetoOptimiser
else:
    import_structure = {
        "_902": ["BarForPareto"],
        "_903": ["CandidateDisplayChoice"],
        "_904": ["ChartInfoBase"],
        "_905": ["CylindricalGearSetParetoOptimiser"],
        "_906": ["DesignSpaceSearchBase"],
        "_907": ["DesignSpaceSearchCandidateBase"],
        "_908": ["FaceGearSetParetoOptimiser"],
        "_909": ["GearNameMapper"],
        "_910": ["GearNamePicker"],
        "_911": ["GearSetOptimiserCandidate"],
        "_912": ["GearSetParetoOptimiser"],
        "_913": ["HypoidGearSetParetoOptimiser"],
        "_914": ["InputSliderForPareto"],
        "_915": ["LargerOrSmaller"],
        "_916": ["MicroGeometryDesignSpaceSearch"],
        "_917": ["MicroGeometryDesignSpaceSearchCandidate"],
        "_918": ["MicroGeometryDesignSpaceSearchChartInformation"],
        "_919": ["MicroGeometryGearSetDesignSpaceSearch"],
        "_920": ["MicroGeometryGearSetDesignSpaceSearchStrategyDatabase"],
        "_921": ["MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase"],
        "_922": ["OptimisationTarget"],
        "_923": ["ParetoConicalRatingOptimisationStrategyDatabase"],
        "_924": ["ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase"],
        "_925": ["ParetoCylindricalGearSetOptimisationStrategyDatabase"],
        "_926": ["ParetoCylindricalRatingOptimisationStrategyDatabase"],
        "_927": ["ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase"],
        "_928": ["ParetoFaceGearSetOptimisationStrategyDatabase"],
        "_929": ["ParetoFaceRatingOptimisationStrategyDatabase"],
        "_930": ["ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase"],
        "_931": ["ParetoHypoidGearSetOptimisationStrategyDatabase"],
        "_932": ["ParetoOptimiserChartInformation"],
        "_933": ["ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_934": ["ParetoSpiralBevelGearSetOptimisationStrategyDatabase"],
        "_935": ["ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_936": ["ParetoStraightBevelGearSetOptimisationStrategyDatabase"],
        "_937": ["ReasonsForInvalidDesigns"],
        "_938": ["SpiralBevelGearSetParetoOptimiser"],
        "_939": ["StraightBevelGearSetParetoOptimiser"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BarForPareto",
    "CandidateDisplayChoice",
    "ChartInfoBase",
    "CylindricalGearSetParetoOptimiser",
    "DesignSpaceSearchBase",
    "DesignSpaceSearchCandidateBase",
    "FaceGearSetParetoOptimiser",
    "GearNameMapper",
    "GearNamePicker",
    "GearSetOptimiserCandidate",
    "GearSetParetoOptimiser",
    "HypoidGearSetParetoOptimiser",
    "InputSliderForPareto",
    "LargerOrSmaller",
    "MicroGeometryDesignSpaceSearch",
    "MicroGeometryDesignSpaceSearchCandidate",
    "MicroGeometryDesignSpaceSearchChartInformation",
    "MicroGeometryGearSetDesignSpaceSearch",
    "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
    "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
    "OptimisationTarget",
    "ParetoConicalRatingOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetOptimisationStrategyDatabase",
    "ParetoCylindricalRatingOptimisationStrategyDatabase",
    "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoFaceGearSetOptimisationStrategyDatabase",
    "ParetoFaceRatingOptimisationStrategyDatabase",
    "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoHypoidGearSetOptimisationStrategyDatabase",
    "ParetoOptimiserChartInformation",
    "ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetOptimisationStrategyDatabase",
    "ReasonsForInvalidDesigns",
    "SpiralBevelGearSetParetoOptimiser",
    "StraightBevelGearSetParetoOptimiser",
)

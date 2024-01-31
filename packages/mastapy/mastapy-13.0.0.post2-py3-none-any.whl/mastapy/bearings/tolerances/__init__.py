"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1901 import BearingConnectionComponent
    from ._1902 import InternalClearanceClass
    from ._1903 import BearingToleranceClass
    from ._1904 import BearingToleranceDefinitionOptions
    from ._1905 import FitType
    from ._1906 import InnerRingTolerance
    from ._1907 import InnerSupportTolerance
    from ._1908 import InterferenceDetail
    from ._1909 import InterferenceTolerance
    from ._1910 import ITDesignation
    from ._1911 import MountingSleeveDiameterDetail
    from ._1912 import OuterRingTolerance
    from ._1913 import OuterSupportTolerance
    from ._1914 import RaceDetail
    from ._1915 import RaceRoundnessAtAngle
    from ._1916 import RadialSpecificationMethod
    from ._1917 import RingTolerance
    from ._1918 import RoundnessSpecification
    from ._1919 import RoundnessSpecificationType
    from ._1920 import SupportDetail
    from ._1921 import SupportMaterialSource
    from ._1922 import SupportTolerance
    from ._1923 import SupportToleranceLocationDesignation
    from ._1924 import ToleranceCombination
    from ._1925 import TypeOfFit
else:
    import_structure = {
        "_1901": ["BearingConnectionComponent"],
        "_1902": ["InternalClearanceClass"],
        "_1903": ["BearingToleranceClass"],
        "_1904": ["BearingToleranceDefinitionOptions"],
        "_1905": ["FitType"],
        "_1906": ["InnerRingTolerance"],
        "_1907": ["InnerSupportTolerance"],
        "_1908": ["InterferenceDetail"],
        "_1909": ["InterferenceTolerance"],
        "_1910": ["ITDesignation"],
        "_1911": ["MountingSleeveDiameterDetail"],
        "_1912": ["OuterRingTolerance"],
        "_1913": ["OuterSupportTolerance"],
        "_1914": ["RaceDetail"],
        "_1915": ["RaceRoundnessAtAngle"],
        "_1916": ["RadialSpecificationMethod"],
        "_1917": ["RingTolerance"],
        "_1918": ["RoundnessSpecification"],
        "_1919": ["RoundnessSpecificationType"],
        "_1920": ["SupportDetail"],
        "_1921": ["SupportMaterialSource"],
        "_1922": ["SupportTolerance"],
        "_1923": ["SupportToleranceLocationDesignation"],
        "_1924": ["ToleranceCombination"],
        "_1925": ["TypeOfFit"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BearingConnectionComponent",
    "InternalClearanceClass",
    "BearingToleranceClass",
    "BearingToleranceDefinitionOptions",
    "FitType",
    "InnerRingTolerance",
    "InnerSupportTolerance",
    "InterferenceDetail",
    "InterferenceTolerance",
    "ITDesignation",
    "MountingSleeveDiameterDetail",
    "OuterRingTolerance",
    "OuterSupportTolerance",
    "RaceDetail",
    "RaceRoundnessAtAngle",
    "RadialSpecificationMethod",
    "RingTolerance",
    "RoundnessSpecification",
    "RoundnessSpecificationType",
    "SupportDetail",
    "SupportMaterialSource",
    "SupportTolerance",
    "SupportToleranceLocationDesignation",
    "ToleranceCombination",
    "TypeOfFit",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1834 import EnumWithSelectedValue
    from ._1836 import DeletableCollectionMember
    from ._1837 import DutyCyclePropertySummary
    from ._1838 import DutyCyclePropertySummaryForce
    from ._1839 import DutyCyclePropertySummaryPercentage
    from ._1840 import DutyCyclePropertySummarySmallAngle
    from ._1841 import DutyCyclePropertySummaryStress
    from ._1842 import DutyCyclePropertySummaryVeryShortLength
    from ._1843 import EnumWithBoolean
    from ._1844 import NamedRangeWithOverridableMinAndMax
    from ._1845 import TypedObjectsWithOption
else:
    import_structure = {
        "_1834": ["EnumWithSelectedValue"],
        "_1836": ["DeletableCollectionMember"],
        "_1837": ["DutyCyclePropertySummary"],
        "_1838": ["DutyCyclePropertySummaryForce"],
        "_1839": ["DutyCyclePropertySummaryPercentage"],
        "_1840": ["DutyCyclePropertySummarySmallAngle"],
        "_1841": ["DutyCyclePropertySummaryStress"],
        "_1842": ["DutyCyclePropertySummaryVeryShortLength"],
        "_1843": ["EnumWithBoolean"],
        "_1844": ["NamedRangeWithOverridableMinAndMax"],
        "_1845": ["TypedObjectsWithOption"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "EnumWithSelectedValue",
    "DeletableCollectionMember",
    "DutyCyclePropertySummary",
    "DutyCyclePropertySummaryForce",
    "DutyCyclePropertySummaryPercentage",
    "DutyCyclePropertySummarySmallAngle",
    "DutyCyclePropertySummaryStress",
    "DutyCyclePropertySummaryVeryShortLength",
    "EnumWithBoolean",
    "NamedRangeWithOverridableMinAndMax",
    "TypedObjectsWithOption",
)

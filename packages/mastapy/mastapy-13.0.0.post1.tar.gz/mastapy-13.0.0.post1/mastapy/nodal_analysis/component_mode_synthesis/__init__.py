"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._223 import AddNodeToGroupByID
    from ._224 import CMSElementFaceGroup
    from ._225 import CMSElementFaceGroupOfAllFreeFaces
    from ._226 import CMSModel
    from ._227 import CMSNodeGroup
    from ._228 import CMSOptions
    from ._229 import CMSResults
    from ._230 import HarmonicCMSResults
    from ._231 import ModalCMSResults
    from ._232 import RealCMSResults
    from ._233 import ReductionModeType
    from ._234 import SoftwareUsedForReductionType
    from ._235 import StaticCMSResults
else:
    import_structure = {
        "_223": ["AddNodeToGroupByID"],
        "_224": ["CMSElementFaceGroup"],
        "_225": ["CMSElementFaceGroupOfAllFreeFaces"],
        "_226": ["CMSModel"],
        "_227": ["CMSNodeGroup"],
        "_228": ["CMSOptions"],
        "_229": ["CMSResults"],
        "_230": ["HarmonicCMSResults"],
        "_231": ["ModalCMSResults"],
        "_232": ["RealCMSResults"],
        "_233": ["ReductionModeType"],
        "_234": ["SoftwareUsedForReductionType"],
        "_235": ["StaticCMSResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AddNodeToGroupByID",
    "CMSElementFaceGroup",
    "CMSElementFaceGroupOfAllFreeFaces",
    "CMSModel",
    "CMSNodeGroup",
    "CMSOptions",
    "CMSResults",
    "HarmonicCMSResults",
    "ModalCMSResults",
    "RealCMSResults",
    "ReductionModeType",
    "SoftwareUsedForReductionType",
    "StaticCMSResults",
)

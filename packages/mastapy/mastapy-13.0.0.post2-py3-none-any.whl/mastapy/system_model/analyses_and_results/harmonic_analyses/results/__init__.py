"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5843 import ConnectedComponentType
    from ._5844 import ExcitationSourceSelection
    from ._5845 import ExcitationSourceSelectionBase
    from ._5846 import ExcitationSourceSelectionGroup
    from ._5847 import HarmonicSelection
    from ._5848 import ModalContributionDisplayMethod
    from ._5849 import ModalContributionFilteringMethod
    from ._5850 import ResultLocationSelectionGroup
    from ._5851 import ResultLocationSelectionGroups
    from ._5852 import ResultNodeSelection
else:
    import_structure = {
        "_5843": ["ConnectedComponentType"],
        "_5844": ["ExcitationSourceSelection"],
        "_5845": ["ExcitationSourceSelectionBase"],
        "_5846": ["ExcitationSourceSelectionGroup"],
        "_5847": ["HarmonicSelection"],
        "_5848": ["ModalContributionDisplayMethod"],
        "_5849": ["ModalContributionFilteringMethod"],
        "_5850": ["ResultLocationSelectionGroup"],
        "_5851": ["ResultLocationSelectionGroups"],
        "_5852": ["ResultNodeSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ConnectedComponentType",
    "ExcitationSourceSelection",
    "ExcitationSourceSelectionBase",
    "ExcitationSourceSelectionGroup",
    "HarmonicSelection",
    "ModalContributionDisplayMethod",
    "ModalContributionFilteringMethod",
    "ResultLocationSelectionGroup",
    "ResultLocationSelectionGroups",
    "ResultNodeSelection",
)

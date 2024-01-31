"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5844 import ConnectedComponentType
    from ._5845 import ExcitationSourceSelection
    from ._5846 import ExcitationSourceSelectionBase
    from ._5847 import ExcitationSourceSelectionGroup
    from ._5848 import HarmonicSelection
    from ._5849 import ModalContributionDisplayMethod
    from ._5850 import ModalContributionFilteringMethod
    from ._5851 import ResultLocationSelectionGroup
    from ._5852 import ResultLocationSelectionGroups
    from ._5853 import ResultNodeSelection
else:
    import_structure = {
        "_5844": ["ConnectedComponentType"],
        "_5845": ["ExcitationSourceSelection"],
        "_5846": ["ExcitationSourceSelectionBase"],
        "_5847": ["ExcitationSourceSelectionGroup"],
        "_5848": ["HarmonicSelection"],
        "_5849": ["ModalContributionDisplayMethod"],
        "_5850": ["ModalContributionFilteringMethod"],
        "_5851": ["ResultLocationSelectionGroup"],
        "_5852": ["ResultLocationSelectionGroups"],
        "_5853": ["ResultNodeSelection"],
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

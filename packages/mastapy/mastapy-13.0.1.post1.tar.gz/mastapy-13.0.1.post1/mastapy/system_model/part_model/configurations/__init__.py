"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2611 import ActiveFESubstructureSelection
    from ._2612 import ActiveFESubstructureSelectionGroup
    from ._2613 import ActiveShaftDesignSelection
    from ._2614 import ActiveShaftDesignSelectionGroup
    from ._2615 import BearingDetailConfiguration
    from ._2616 import BearingDetailSelection
    from ._2617 import PartDetailConfiguration
    from ._2618 import PartDetailSelection
else:
    import_structure = {
        "_2611": ["ActiveFESubstructureSelection"],
        "_2612": ["ActiveFESubstructureSelectionGroup"],
        "_2613": ["ActiveShaftDesignSelection"],
        "_2614": ["ActiveShaftDesignSelectionGroup"],
        "_2615": ["BearingDetailConfiguration"],
        "_2616": ["BearingDetailSelection"],
        "_2617": ["PartDetailConfiguration"],
        "_2618": ["PartDetailSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ActiveFESubstructureSelection",
    "ActiveFESubstructureSelectionGroup",
    "ActiveShaftDesignSelection",
    "ActiveShaftDesignSelectionGroup",
    "BearingDetailConfiguration",
    "BearingDetailSelection",
    "PartDetailConfiguration",
    "PartDetailSelection",
)

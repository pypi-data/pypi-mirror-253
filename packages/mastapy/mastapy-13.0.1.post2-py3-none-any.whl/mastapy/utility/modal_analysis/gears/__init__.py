"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1797 import GearMeshForTE
    from ._1798 import GearOrderForTE
    from ._1799 import GearPositions
    from ._1800 import HarmonicOrderForTE
    from ._1801 import LabelOnlyOrder
    from ._1802 import OrderForTE
    from ._1803 import OrderSelector
    from ._1804 import OrderWithRadius
    from ._1805 import RollingBearingOrder
    from ._1806 import ShaftOrderForTE
    from ._1807 import UserDefinedOrderForTE
else:
    import_structure = {
        "_1797": ["GearMeshForTE"],
        "_1798": ["GearOrderForTE"],
        "_1799": ["GearPositions"],
        "_1800": ["HarmonicOrderForTE"],
        "_1801": ["LabelOnlyOrder"],
        "_1802": ["OrderForTE"],
        "_1803": ["OrderSelector"],
        "_1804": ["OrderWithRadius"],
        "_1805": ["RollingBearingOrder"],
        "_1806": ["ShaftOrderForTE"],
        "_1807": ["UserDefinedOrderForTE"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GearMeshForTE",
    "GearOrderForTE",
    "GearPositions",
    "HarmonicOrderForTE",
    "LabelOnlyOrder",
    "OrderForTE",
    "OrderSelector",
    "OrderWithRadius",
    "RollingBearingOrder",
    "ShaftOrderForTE",
    "UserDefinedOrderForTE",
)

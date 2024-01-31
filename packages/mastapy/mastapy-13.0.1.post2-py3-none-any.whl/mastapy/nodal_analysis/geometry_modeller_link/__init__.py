"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._152 import BaseGeometryModellerDimension
    from ._153 import GeometryModellerAngleDimension
    from ._154 import GeometryModellerCountDimension
    from ._155 import GeometryModellerDesignInformation
    from ._156 import GeometryModellerDimension
    from ._157 import GeometryModellerDimensions
    from ._158 import GeometryModellerDimensionType
    from ._159 import GeometryModellerLengthDimension
    from ._160 import GeometryModellerSettings
    from ._161 import GeometryModellerUnitlessDimension
    from ._162 import MeshRequest
    from ._163 import MeshRequestResult
    from ._164 import RepositionComponentDetails
else:
    import_structure = {
        "_152": ["BaseGeometryModellerDimension"],
        "_153": ["GeometryModellerAngleDimension"],
        "_154": ["GeometryModellerCountDimension"],
        "_155": ["GeometryModellerDesignInformation"],
        "_156": ["GeometryModellerDimension"],
        "_157": ["GeometryModellerDimensions"],
        "_158": ["GeometryModellerDimensionType"],
        "_159": ["GeometryModellerLengthDimension"],
        "_160": ["GeometryModellerSettings"],
        "_161": ["GeometryModellerUnitlessDimension"],
        "_162": ["MeshRequest"],
        "_163": ["MeshRequestResult"],
        "_164": ["RepositionComponentDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BaseGeometryModellerDimension",
    "GeometryModellerAngleDimension",
    "GeometryModellerCountDimension",
    "GeometryModellerDesignInformation",
    "GeometryModellerDimension",
    "GeometryModellerDimensions",
    "GeometryModellerDimensionType",
    "GeometryModellerLengthDimension",
    "GeometryModellerSettings",
    "GeometryModellerUnitlessDimension",
    "MeshRequest",
    "MeshRequestResult",
    "RepositionComponentDetails",
)

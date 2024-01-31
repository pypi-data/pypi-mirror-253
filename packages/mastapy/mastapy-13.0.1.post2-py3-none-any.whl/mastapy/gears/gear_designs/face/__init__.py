"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._989 import FaceGearDesign
    from ._990 import FaceGearDiameterFaceWidthSpecificationMethod
    from ._991 import FaceGearMeshDesign
    from ._992 import FaceGearMeshMicroGeometry
    from ._993 import FaceGearMicroGeometry
    from ._994 import FaceGearPinionDesign
    from ._995 import FaceGearSetDesign
    from ._996 import FaceGearSetMicroGeometry
    from ._997 import FaceGearWheelDesign
else:
    import_structure = {
        "_989": ["FaceGearDesign"],
        "_990": ["FaceGearDiameterFaceWidthSpecificationMethod"],
        "_991": ["FaceGearMeshDesign"],
        "_992": ["FaceGearMeshMicroGeometry"],
        "_993": ["FaceGearMicroGeometry"],
        "_994": ["FaceGearPinionDesign"],
        "_995": ["FaceGearSetDesign"],
        "_996": ["FaceGearSetMicroGeometry"],
        "_997": ["FaceGearWheelDesign"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FaceGearDesign",
    "FaceGearDiameterFaceWidthSpecificationMethod",
    "FaceGearMeshDesign",
    "FaceGearMeshMicroGeometry",
    "FaceGearMicroGeometry",
    "FaceGearPinionDesign",
    "FaceGearSetDesign",
    "FaceGearSetMicroGeometry",
    "FaceGearWheelDesign",
)

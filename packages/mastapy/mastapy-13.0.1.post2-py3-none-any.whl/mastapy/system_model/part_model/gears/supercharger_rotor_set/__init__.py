"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2555 import BoostPressureInputOptions
    from ._2556 import InputPowerInputOptions
    from ._2557 import PressureRatioInputOptions
    from ._2558 import RotorSetDataInputFileOptions
    from ._2559 import RotorSetMeasuredPoint
    from ._2560 import RotorSpeedInputOptions
    from ._2561 import SuperchargerMap
    from ._2562 import SuperchargerMaps
    from ._2563 import SuperchargerRotorSet
    from ._2564 import SuperchargerRotorSetDatabase
    from ._2565 import YVariableForImportedData
else:
    import_structure = {
        "_2555": ["BoostPressureInputOptions"],
        "_2556": ["InputPowerInputOptions"],
        "_2557": ["PressureRatioInputOptions"],
        "_2558": ["RotorSetDataInputFileOptions"],
        "_2559": ["RotorSetMeasuredPoint"],
        "_2560": ["RotorSpeedInputOptions"],
        "_2561": ["SuperchargerMap"],
        "_2562": ["SuperchargerMaps"],
        "_2563": ["SuperchargerRotorSet"],
        "_2564": ["SuperchargerRotorSetDatabase"],
        "_2565": ["YVariableForImportedData"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BoostPressureInputOptions",
    "InputPowerInputOptions",
    "PressureRatioInputOptions",
    "RotorSetDataInputFileOptions",
    "RotorSetMeasuredPoint",
    "RotorSpeedInputOptions",
    "SuperchargerMap",
    "SuperchargerMaps",
    "SuperchargerRotorSet",
    "SuperchargerRotorSetDatabase",
    "YVariableForImportedData",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1377 import ElectricMachineHarmonicLoadDataBase
    from ._1378 import ForceDisplayOption
    from ._1379 import HarmonicLoadDataBase
    from ._1380 import HarmonicLoadDataControlExcitationOptionBase
    from ._1381 import HarmonicLoadDataType
    from ._1382 import SpeedDependentHarmonicLoadData
    from ._1383 import StatorToothInterpolator
    from ._1384 import StatorToothLoadInterpolator
    from ._1385 import StatorToothMomentInterpolator
else:
    import_structure = {
        "_1377": ["ElectricMachineHarmonicLoadDataBase"],
        "_1378": ["ForceDisplayOption"],
        "_1379": ["HarmonicLoadDataBase"],
        "_1380": ["HarmonicLoadDataControlExcitationOptionBase"],
        "_1381": ["HarmonicLoadDataType"],
        "_1382": ["SpeedDependentHarmonicLoadData"],
        "_1383": ["StatorToothInterpolator"],
        "_1384": ["StatorToothLoadInterpolator"],
        "_1385": ["StatorToothMomentInterpolator"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ElectricMachineHarmonicLoadDataBase",
    "ForceDisplayOption",
    "HarmonicLoadDataBase",
    "HarmonicLoadDataControlExcitationOptionBase",
    "HarmonicLoadDataType",
    "SpeedDependentHarmonicLoadData",
    "StatorToothInterpolator",
    "StatorToothLoadInterpolator",
    "StatorToothMomentInterpolator",
)

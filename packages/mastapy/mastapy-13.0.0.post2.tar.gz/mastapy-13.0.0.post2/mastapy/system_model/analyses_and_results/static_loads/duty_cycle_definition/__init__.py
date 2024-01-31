"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6988 import AdditionalForcesObtainedFrom
    from ._6989 import BoostPressureLoadCaseInputOptions
    from ._6990 import DesignStateOptions
    from ._6991 import DestinationDesignState
    from ._6992 import ForceInputOptions
    from ._6993 import GearRatioInputOptions
    from ._6994 import LoadCaseNameOptions
    from ._6995 import MomentInputOptions
    from ._6996 import MultiTimeSeriesDataInputFileOptions
    from ._6997 import PointLoadInputOptions
    from ._6998 import PowerLoadInputOptions
    from ._6999 import RampOrSteadyStateInputOptions
    from ._7000 import SpeedInputOptions
    from ._7001 import TimeSeriesImporter
    from ._7002 import TimeStepInputOptions
    from ._7003 import TorqueInputOptions
    from ._7004 import TorqueValuesObtainedFrom
else:
    import_structure = {
        "_6988": ["AdditionalForcesObtainedFrom"],
        "_6989": ["BoostPressureLoadCaseInputOptions"],
        "_6990": ["DesignStateOptions"],
        "_6991": ["DestinationDesignState"],
        "_6992": ["ForceInputOptions"],
        "_6993": ["GearRatioInputOptions"],
        "_6994": ["LoadCaseNameOptions"],
        "_6995": ["MomentInputOptions"],
        "_6996": ["MultiTimeSeriesDataInputFileOptions"],
        "_6997": ["PointLoadInputOptions"],
        "_6998": ["PowerLoadInputOptions"],
        "_6999": ["RampOrSteadyStateInputOptions"],
        "_7000": ["SpeedInputOptions"],
        "_7001": ["TimeSeriesImporter"],
        "_7002": ["TimeStepInputOptions"],
        "_7003": ["TorqueInputOptions"],
        "_7004": ["TorqueValuesObtainedFrom"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdditionalForcesObtainedFrom",
    "BoostPressureLoadCaseInputOptions",
    "DesignStateOptions",
    "DestinationDesignState",
    "ForceInputOptions",
    "GearRatioInputOptions",
    "LoadCaseNameOptions",
    "MomentInputOptions",
    "MultiTimeSeriesDataInputFileOptions",
    "PointLoadInputOptions",
    "PowerLoadInputOptions",
    "RampOrSteadyStateInputOptions",
    "SpeedInputOptions",
    "TimeSeriesImporter",
    "TimeStepInputOptions",
    "TorqueInputOptions",
    "TorqueValuesObtainedFrom",
)

"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6989 import AdditionalForcesObtainedFrom
    from ._6990 import BoostPressureLoadCaseInputOptions
    from ._6991 import DesignStateOptions
    from ._6992 import DestinationDesignState
    from ._6993 import ForceInputOptions
    from ._6994 import GearRatioInputOptions
    from ._6995 import LoadCaseNameOptions
    from ._6996 import MomentInputOptions
    from ._6997 import MultiTimeSeriesDataInputFileOptions
    from ._6998 import PointLoadInputOptions
    from ._6999 import PowerLoadInputOptions
    from ._7000 import RampOrSteadyStateInputOptions
    from ._7001 import SpeedInputOptions
    from ._7002 import TimeSeriesImporter
    from ._7003 import TimeStepInputOptions
    from ._7004 import TorqueInputOptions
    from ._7005 import TorqueValuesObtainedFrom
else:
    import_structure = {
        "_6989": ["AdditionalForcesObtainedFrom"],
        "_6990": ["BoostPressureLoadCaseInputOptions"],
        "_6991": ["DesignStateOptions"],
        "_6992": ["DestinationDesignState"],
        "_6993": ["ForceInputOptions"],
        "_6994": ["GearRatioInputOptions"],
        "_6995": ["LoadCaseNameOptions"],
        "_6996": ["MomentInputOptions"],
        "_6997": ["MultiTimeSeriesDataInputFileOptions"],
        "_6998": ["PointLoadInputOptions"],
        "_6999": ["PowerLoadInputOptions"],
        "_7000": ["RampOrSteadyStateInputOptions"],
        "_7001": ["SpeedInputOptions"],
        "_7002": ["TimeSeriesImporter"],
        "_7003": ["TimeStepInputOptions"],
        "_7004": ["TorqueInputOptions"],
        "_7005": ["TorqueValuesObtainedFrom"],
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

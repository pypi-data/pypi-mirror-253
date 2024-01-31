"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2076 import AdjustedSpeed
    from ._2077 import AdjustmentFactors
    from ._2078 import BearingLoads
    from ._2079 import BearingRatingLife
    from ._2080 import DynamicAxialLoadCarryingCapacity
    from ._2081 import Frequencies
    from ._2082 import FrequencyOfOverRolling
    from ._2083 import Friction
    from ._2084 import FrictionalMoment
    from ._2085 import FrictionSources
    from ._2086 import Grease
    from ._2087 import GreaseLifeAndRelubricationInterval
    from ._2088 import GreaseQuantity
    from ._2089 import InitialFill
    from ._2090 import LifeModel
    from ._2091 import MinimumLoad
    from ._2092 import OperatingViscosity
    from ._2093 import PermissibleAxialLoad
    from ._2094 import RotationalFrequency
    from ._2095 import SKFAuthentication
    from ._2096 import SKFCalculationResult
    from ._2097 import SKFCredentials
    from ._2098 import SKFModuleResults
    from ._2099 import StaticSafetyFactors
    from ._2100 import Viscosities
else:
    import_structure = {
        "_2076": ["AdjustedSpeed"],
        "_2077": ["AdjustmentFactors"],
        "_2078": ["BearingLoads"],
        "_2079": ["BearingRatingLife"],
        "_2080": ["DynamicAxialLoadCarryingCapacity"],
        "_2081": ["Frequencies"],
        "_2082": ["FrequencyOfOverRolling"],
        "_2083": ["Friction"],
        "_2084": ["FrictionalMoment"],
        "_2085": ["FrictionSources"],
        "_2086": ["Grease"],
        "_2087": ["GreaseLifeAndRelubricationInterval"],
        "_2088": ["GreaseQuantity"],
        "_2089": ["InitialFill"],
        "_2090": ["LifeModel"],
        "_2091": ["MinimumLoad"],
        "_2092": ["OperatingViscosity"],
        "_2093": ["PermissibleAxialLoad"],
        "_2094": ["RotationalFrequency"],
        "_2095": ["SKFAuthentication"],
        "_2096": ["SKFCalculationResult"],
        "_2097": ["SKFCredentials"],
        "_2098": ["SKFModuleResults"],
        "_2099": ["StaticSafetyFactors"],
        "_2100": ["Viscosities"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdjustedSpeed",
    "AdjustmentFactors",
    "BearingLoads",
    "BearingRatingLife",
    "DynamicAxialLoadCarryingCapacity",
    "Frequencies",
    "FrequencyOfOverRolling",
    "Friction",
    "FrictionalMoment",
    "FrictionSources",
    "Grease",
    "GreaseLifeAndRelubricationInterval",
    "GreaseQuantity",
    "InitialFill",
    "LifeModel",
    "MinimumLoad",
    "OperatingViscosity",
    "PermissibleAxialLoad",
    "RotationalFrequency",
    "SKFAuthentication",
    "SKFCalculationResult",
    "SKFCredentials",
    "SKFModuleResults",
    "StaticSafetyFactors",
    "Viscosities",
)

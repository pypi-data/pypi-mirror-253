"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2135 import AngularContactBallBearing
    from ._2136 import AngularContactThrustBallBearing
    from ._2137 import AsymmetricSphericalRollerBearing
    from ._2138 import AxialThrustCylindricalRollerBearing
    from ._2139 import AxialThrustNeedleRollerBearing
    from ._2140 import BallBearing
    from ._2141 import BallBearingShoulderDefinition
    from ._2142 import BarrelRollerBearing
    from ._2143 import BearingProtection
    from ._2144 import BearingProtectionDetailsModifier
    from ._2145 import BearingProtectionLevel
    from ._2146 import BearingTypeExtraInformation
    from ._2147 import CageBridgeShape
    from ._2148 import CrossedRollerBearing
    from ._2149 import CylindricalRollerBearing
    from ._2150 import DeepGrooveBallBearing
    from ._2151 import DiameterSeries
    from ._2152 import FatigueLoadLimitCalculationMethodEnum
    from ._2153 import FourPointContactAngleDefinition
    from ._2154 import FourPointContactBallBearing
    from ._2155 import GeometricConstants
    from ._2156 import GeometricConstantsForRollingFrictionalMoments
    from ._2157 import GeometricConstantsForSlidingFrictionalMoments
    from ._2158 import HeightSeries
    from ._2159 import MultiPointContactBallBearing
    from ._2160 import NeedleRollerBearing
    from ._2161 import NonBarrelRollerBearing
    from ._2162 import RollerBearing
    from ._2163 import RollerEndShape
    from ._2164 import RollerRibDetail
    from ._2165 import RollingBearing
    from ._2166 import SelfAligningBallBearing
    from ._2167 import SKFSealFrictionalMomentConstants
    from ._2168 import SleeveType
    from ._2169 import SphericalRollerBearing
    from ._2170 import SphericalRollerThrustBearing
    from ._2171 import TaperRollerBearing
    from ._2172 import ThreePointContactBallBearing
    from ._2173 import ThrustBallBearing
    from ._2174 import ToroidalRollerBearing
    from ._2175 import WidthSeries
else:
    import_structure = {
        "_2135": ["AngularContactBallBearing"],
        "_2136": ["AngularContactThrustBallBearing"],
        "_2137": ["AsymmetricSphericalRollerBearing"],
        "_2138": ["AxialThrustCylindricalRollerBearing"],
        "_2139": ["AxialThrustNeedleRollerBearing"],
        "_2140": ["BallBearing"],
        "_2141": ["BallBearingShoulderDefinition"],
        "_2142": ["BarrelRollerBearing"],
        "_2143": ["BearingProtection"],
        "_2144": ["BearingProtectionDetailsModifier"],
        "_2145": ["BearingProtectionLevel"],
        "_2146": ["BearingTypeExtraInformation"],
        "_2147": ["CageBridgeShape"],
        "_2148": ["CrossedRollerBearing"],
        "_2149": ["CylindricalRollerBearing"],
        "_2150": ["DeepGrooveBallBearing"],
        "_2151": ["DiameterSeries"],
        "_2152": ["FatigueLoadLimitCalculationMethodEnum"],
        "_2153": ["FourPointContactAngleDefinition"],
        "_2154": ["FourPointContactBallBearing"],
        "_2155": ["GeometricConstants"],
        "_2156": ["GeometricConstantsForRollingFrictionalMoments"],
        "_2157": ["GeometricConstantsForSlidingFrictionalMoments"],
        "_2158": ["HeightSeries"],
        "_2159": ["MultiPointContactBallBearing"],
        "_2160": ["NeedleRollerBearing"],
        "_2161": ["NonBarrelRollerBearing"],
        "_2162": ["RollerBearing"],
        "_2163": ["RollerEndShape"],
        "_2164": ["RollerRibDetail"],
        "_2165": ["RollingBearing"],
        "_2166": ["SelfAligningBallBearing"],
        "_2167": ["SKFSealFrictionalMomentConstants"],
        "_2168": ["SleeveType"],
        "_2169": ["SphericalRollerBearing"],
        "_2170": ["SphericalRollerThrustBearing"],
        "_2171": ["TaperRollerBearing"],
        "_2172": ["ThreePointContactBallBearing"],
        "_2173": ["ThrustBallBearing"],
        "_2174": ["ToroidalRollerBearing"],
        "_2175": ["WidthSeries"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AngularContactBallBearing",
    "AngularContactThrustBallBearing",
    "AsymmetricSphericalRollerBearing",
    "AxialThrustCylindricalRollerBearing",
    "AxialThrustNeedleRollerBearing",
    "BallBearing",
    "BallBearingShoulderDefinition",
    "BarrelRollerBearing",
    "BearingProtection",
    "BearingProtectionDetailsModifier",
    "BearingProtectionLevel",
    "BearingTypeExtraInformation",
    "CageBridgeShape",
    "CrossedRollerBearing",
    "CylindricalRollerBearing",
    "DeepGrooveBallBearing",
    "DiameterSeries",
    "FatigueLoadLimitCalculationMethodEnum",
    "FourPointContactAngleDefinition",
    "FourPointContactBallBearing",
    "GeometricConstants",
    "GeometricConstantsForRollingFrictionalMoments",
    "GeometricConstantsForSlidingFrictionalMoments",
    "HeightSeries",
    "MultiPointContactBallBearing",
    "NeedleRollerBearing",
    "NonBarrelRollerBearing",
    "RollerBearing",
    "RollerEndShape",
    "RollerRibDetail",
    "RollingBearing",
    "SelfAligningBallBearing",
    "SKFSealFrictionalMomentConstants",
    "SleeveType",
    "SphericalRollerBearing",
    "SphericalRollerThrustBearing",
    "TaperRollerBearing",
    "ThreePointContactBallBearing",
    "ThrustBallBearing",
    "ToroidalRollerBearing",
    "WidthSeries",
)

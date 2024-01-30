"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1966 import BallBearingAnalysisMethod
    from ._1967 import BallBearingContactCalculation
    from ._1968 import BallBearingRaceContactGeometry
    from ._1969 import DIN7322010Results
    from ._1970 import ForceAtLaminaGroupReportable
    from ._1971 import ForceAtLaminaReportable
    from ._1972 import FrictionModelForGyroscopicMoment
    from ._1973 import InternalClearance
    from ._1974 import ISO14179Settings
    from ._1975 import ISO14179SettingsDatabase
    from ._1976 import ISO14179SettingsPerBearingType
    from ._1977 import ISO153122018Results
    from ._1978 import ISOTR1417912001Results
    from ._1979 import ISOTR141792001Results
    from ._1980 import ISOTR1417922001Results
    from ._1981 import LoadedAbstractSphericalRollerBearingStripLoadResults
    from ._1982 import LoadedAngularContactBallBearingElement
    from ._1983 import LoadedAngularContactBallBearingResults
    from ._1984 import LoadedAngularContactBallBearingRow
    from ._1985 import LoadedAngularContactThrustBallBearingElement
    from ._1986 import LoadedAngularContactThrustBallBearingResults
    from ._1987 import LoadedAngularContactThrustBallBearingRow
    from ._1988 import LoadedAsymmetricSphericalRollerBearingElement
    from ._1989 import LoadedAsymmetricSphericalRollerBearingResults
    from ._1990 import LoadedAsymmetricSphericalRollerBearingRow
    from ._1991 import LoadedAsymmetricSphericalRollerBearingStripLoadResults
    from ._1992 import LoadedAxialThrustCylindricalRollerBearingDutyCycle
    from ._1993 import LoadedAxialThrustCylindricalRollerBearingElement
    from ._1994 import LoadedAxialThrustCylindricalRollerBearingResults
    from ._1995 import LoadedAxialThrustCylindricalRollerBearingRow
    from ._1996 import LoadedAxialThrustNeedleRollerBearingElement
    from ._1997 import LoadedAxialThrustNeedleRollerBearingResults
    from ._1998 import LoadedAxialThrustNeedleRollerBearingRow
    from ._1999 import LoadedBallBearingDutyCycle
    from ._2000 import LoadedBallBearingElement
    from ._2001 import LoadedBallBearingRaceResults
    from ._2002 import LoadedBallBearingResults
    from ._2003 import LoadedBallBearingRow
    from ._2004 import LoadedCrossedRollerBearingElement
    from ._2005 import LoadedCrossedRollerBearingResults
    from ._2006 import LoadedCrossedRollerBearingRow
    from ._2007 import LoadedCylindricalRollerBearingDutyCycle
    from ._2008 import LoadedCylindricalRollerBearingElement
    from ._2009 import LoadedCylindricalRollerBearingResults
    from ._2010 import LoadedCylindricalRollerBearingRow
    from ._2011 import LoadedDeepGrooveBallBearingElement
    from ._2012 import LoadedDeepGrooveBallBearingResults
    from ._2013 import LoadedDeepGrooveBallBearingRow
    from ._2014 import LoadedElement
    from ._2015 import LoadedFourPointContactBallBearingElement
    from ._2016 import LoadedFourPointContactBallBearingRaceResults
    from ._2017 import LoadedFourPointContactBallBearingResults
    from ._2018 import LoadedFourPointContactBallBearingRow
    from ._2019 import LoadedMultiPointContactBallBearingElement
    from ._2020 import LoadedNeedleRollerBearingElement
    from ._2021 import LoadedNeedleRollerBearingResults
    from ._2022 import LoadedNeedleRollerBearingRow
    from ._2023 import LoadedNonBarrelRollerBearingDutyCycle
    from ._2024 import LoadedNonBarrelRollerBearingResults
    from ._2025 import LoadedNonBarrelRollerBearingRow
    from ._2026 import LoadedNonBarrelRollerBearingStripLoadResults
    from ._2027 import LoadedNonBarrelRollerElement
    from ._2028 import LoadedRollerBearingElement
    from ._2029 import LoadedRollerBearingResults
    from ._2030 import LoadedRollerBearingRow
    from ._2031 import LoadedRollerStripLoadResults
    from ._2032 import LoadedRollingBearingRaceResults
    from ._2033 import LoadedRollingBearingResults
    from ._2034 import LoadedRollingBearingRow
    from ._2035 import LoadedSelfAligningBallBearingElement
    from ._2036 import LoadedSelfAligningBallBearingResults
    from ._2037 import LoadedSelfAligningBallBearingRow
    from ._2038 import LoadedSphericalRadialRollerBearingElement
    from ._2039 import LoadedSphericalRollerBearingElement
    from ._2040 import LoadedSphericalRollerRadialBearingResults
    from ._2041 import LoadedSphericalRollerRadialBearingRow
    from ._2042 import LoadedSphericalRollerRadialBearingStripLoadResults
    from ._2043 import LoadedSphericalRollerThrustBearingResults
    from ._2044 import LoadedSphericalRollerThrustBearingRow
    from ._2045 import LoadedSphericalThrustRollerBearingElement
    from ._2046 import LoadedTaperRollerBearingDutyCycle
    from ._2047 import LoadedTaperRollerBearingElement
    from ._2048 import LoadedTaperRollerBearingResults
    from ._2049 import LoadedTaperRollerBearingRow
    from ._2050 import LoadedThreePointContactBallBearingElement
    from ._2051 import LoadedThreePointContactBallBearingResults
    from ._2052 import LoadedThreePointContactBallBearingRow
    from ._2053 import LoadedThrustBallBearingElement
    from ._2054 import LoadedThrustBallBearingResults
    from ._2055 import LoadedThrustBallBearingRow
    from ._2056 import LoadedToroidalRollerBearingElement
    from ._2057 import LoadedToroidalRollerBearingResults
    from ._2058 import LoadedToroidalRollerBearingRow
    from ._2059 import LoadedToroidalRollerBearingStripLoadResults
    from ._2060 import MaximumStaticContactStress
    from ._2061 import MaximumStaticContactStressDutyCycle
    from ._2062 import MaximumStaticContactStressResultsAbstract
    from ._2063 import MaxStripLoadStressObject
    from ._2064 import PermissibleContinuousAxialLoadResults
    from ._2065 import PowerRatingF1EstimationMethod
    from ._2066 import PreloadFactorLookupTable
    from ._2067 import ResultsAtRollerOffset
    from ._2068 import RingForceAndDisplacement
    from ._2069 import RollerAnalysisMethod
    from ._2070 import RollingBearingFrictionCoefficients
    from ._2071 import RollingBearingSpeedResults
    from ._2072 import SMTRibStressResults
    from ._2073 import StressAtPosition
    from ._2074 import ThreePointContactInternalClearance
    from ._2075 import TrackTruncationSafetyFactorResults
else:
    import_structure = {
        "_1966": ["BallBearingAnalysisMethod"],
        "_1967": ["BallBearingContactCalculation"],
        "_1968": ["BallBearingRaceContactGeometry"],
        "_1969": ["DIN7322010Results"],
        "_1970": ["ForceAtLaminaGroupReportable"],
        "_1971": ["ForceAtLaminaReportable"],
        "_1972": ["FrictionModelForGyroscopicMoment"],
        "_1973": ["InternalClearance"],
        "_1974": ["ISO14179Settings"],
        "_1975": ["ISO14179SettingsDatabase"],
        "_1976": ["ISO14179SettingsPerBearingType"],
        "_1977": ["ISO153122018Results"],
        "_1978": ["ISOTR1417912001Results"],
        "_1979": ["ISOTR141792001Results"],
        "_1980": ["ISOTR1417922001Results"],
        "_1981": ["LoadedAbstractSphericalRollerBearingStripLoadResults"],
        "_1982": ["LoadedAngularContactBallBearingElement"],
        "_1983": ["LoadedAngularContactBallBearingResults"],
        "_1984": ["LoadedAngularContactBallBearingRow"],
        "_1985": ["LoadedAngularContactThrustBallBearingElement"],
        "_1986": ["LoadedAngularContactThrustBallBearingResults"],
        "_1987": ["LoadedAngularContactThrustBallBearingRow"],
        "_1988": ["LoadedAsymmetricSphericalRollerBearingElement"],
        "_1989": ["LoadedAsymmetricSphericalRollerBearingResults"],
        "_1990": ["LoadedAsymmetricSphericalRollerBearingRow"],
        "_1991": ["LoadedAsymmetricSphericalRollerBearingStripLoadResults"],
        "_1992": ["LoadedAxialThrustCylindricalRollerBearingDutyCycle"],
        "_1993": ["LoadedAxialThrustCylindricalRollerBearingElement"],
        "_1994": ["LoadedAxialThrustCylindricalRollerBearingResults"],
        "_1995": ["LoadedAxialThrustCylindricalRollerBearingRow"],
        "_1996": ["LoadedAxialThrustNeedleRollerBearingElement"],
        "_1997": ["LoadedAxialThrustNeedleRollerBearingResults"],
        "_1998": ["LoadedAxialThrustNeedleRollerBearingRow"],
        "_1999": ["LoadedBallBearingDutyCycle"],
        "_2000": ["LoadedBallBearingElement"],
        "_2001": ["LoadedBallBearingRaceResults"],
        "_2002": ["LoadedBallBearingResults"],
        "_2003": ["LoadedBallBearingRow"],
        "_2004": ["LoadedCrossedRollerBearingElement"],
        "_2005": ["LoadedCrossedRollerBearingResults"],
        "_2006": ["LoadedCrossedRollerBearingRow"],
        "_2007": ["LoadedCylindricalRollerBearingDutyCycle"],
        "_2008": ["LoadedCylindricalRollerBearingElement"],
        "_2009": ["LoadedCylindricalRollerBearingResults"],
        "_2010": ["LoadedCylindricalRollerBearingRow"],
        "_2011": ["LoadedDeepGrooveBallBearingElement"],
        "_2012": ["LoadedDeepGrooveBallBearingResults"],
        "_2013": ["LoadedDeepGrooveBallBearingRow"],
        "_2014": ["LoadedElement"],
        "_2015": ["LoadedFourPointContactBallBearingElement"],
        "_2016": ["LoadedFourPointContactBallBearingRaceResults"],
        "_2017": ["LoadedFourPointContactBallBearingResults"],
        "_2018": ["LoadedFourPointContactBallBearingRow"],
        "_2019": ["LoadedMultiPointContactBallBearingElement"],
        "_2020": ["LoadedNeedleRollerBearingElement"],
        "_2021": ["LoadedNeedleRollerBearingResults"],
        "_2022": ["LoadedNeedleRollerBearingRow"],
        "_2023": ["LoadedNonBarrelRollerBearingDutyCycle"],
        "_2024": ["LoadedNonBarrelRollerBearingResults"],
        "_2025": ["LoadedNonBarrelRollerBearingRow"],
        "_2026": ["LoadedNonBarrelRollerBearingStripLoadResults"],
        "_2027": ["LoadedNonBarrelRollerElement"],
        "_2028": ["LoadedRollerBearingElement"],
        "_2029": ["LoadedRollerBearingResults"],
        "_2030": ["LoadedRollerBearingRow"],
        "_2031": ["LoadedRollerStripLoadResults"],
        "_2032": ["LoadedRollingBearingRaceResults"],
        "_2033": ["LoadedRollingBearingResults"],
        "_2034": ["LoadedRollingBearingRow"],
        "_2035": ["LoadedSelfAligningBallBearingElement"],
        "_2036": ["LoadedSelfAligningBallBearingResults"],
        "_2037": ["LoadedSelfAligningBallBearingRow"],
        "_2038": ["LoadedSphericalRadialRollerBearingElement"],
        "_2039": ["LoadedSphericalRollerBearingElement"],
        "_2040": ["LoadedSphericalRollerRadialBearingResults"],
        "_2041": ["LoadedSphericalRollerRadialBearingRow"],
        "_2042": ["LoadedSphericalRollerRadialBearingStripLoadResults"],
        "_2043": ["LoadedSphericalRollerThrustBearingResults"],
        "_2044": ["LoadedSphericalRollerThrustBearingRow"],
        "_2045": ["LoadedSphericalThrustRollerBearingElement"],
        "_2046": ["LoadedTaperRollerBearingDutyCycle"],
        "_2047": ["LoadedTaperRollerBearingElement"],
        "_2048": ["LoadedTaperRollerBearingResults"],
        "_2049": ["LoadedTaperRollerBearingRow"],
        "_2050": ["LoadedThreePointContactBallBearingElement"],
        "_2051": ["LoadedThreePointContactBallBearingResults"],
        "_2052": ["LoadedThreePointContactBallBearingRow"],
        "_2053": ["LoadedThrustBallBearingElement"],
        "_2054": ["LoadedThrustBallBearingResults"],
        "_2055": ["LoadedThrustBallBearingRow"],
        "_2056": ["LoadedToroidalRollerBearingElement"],
        "_2057": ["LoadedToroidalRollerBearingResults"],
        "_2058": ["LoadedToroidalRollerBearingRow"],
        "_2059": ["LoadedToroidalRollerBearingStripLoadResults"],
        "_2060": ["MaximumStaticContactStress"],
        "_2061": ["MaximumStaticContactStressDutyCycle"],
        "_2062": ["MaximumStaticContactStressResultsAbstract"],
        "_2063": ["MaxStripLoadStressObject"],
        "_2064": ["PermissibleContinuousAxialLoadResults"],
        "_2065": ["PowerRatingF1EstimationMethod"],
        "_2066": ["PreloadFactorLookupTable"],
        "_2067": ["ResultsAtRollerOffset"],
        "_2068": ["RingForceAndDisplacement"],
        "_2069": ["RollerAnalysisMethod"],
        "_2070": ["RollingBearingFrictionCoefficients"],
        "_2071": ["RollingBearingSpeedResults"],
        "_2072": ["SMTRibStressResults"],
        "_2073": ["StressAtPosition"],
        "_2074": ["ThreePointContactInternalClearance"],
        "_2075": ["TrackTruncationSafetyFactorResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallBearingAnalysisMethod",
    "BallBearingContactCalculation",
    "BallBearingRaceContactGeometry",
    "DIN7322010Results",
    "ForceAtLaminaGroupReportable",
    "ForceAtLaminaReportable",
    "FrictionModelForGyroscopicMoment",
    "InternalClearance",
    "ISO14179Settings",
    "ISO14179SettingsDatabase",
    "ISO14179SettingsPerBearingType",
    "ISO153122018Results",
    "ISOTR1417912001Results",
    "ISOTR141792001Results",
    "ISOTR1417922001Results",
    "LoadedAbstractSphericalRollerBearingStripLoadResults",
    "LoadedAngularContactBallBearingElement",
    "LoadedAngularContactBallBearingResults",
    "LoadedAngularContactBallBearingRow",
    "LoadedAngularContactThrustBallBearingElement",
    "LoadedAngularContactThrustBallBearingResults",
    "LoadedAngularContactThrustBallBearingRow",
    "LoadedAsymmetricSphericalRollerBearingElement",
    "LoadedAsymmetricSphericalRollerBearingResults",
    "LoadedAsymmetricSphericalRollerBearingRow",
    "LoadedAsymmetricSphericalRollerBearingStripLoadResults",
    "LoadedAxialThrustCylindricalRollerBearingDutyCycle",
    "LoadedAxialThrustCylindricalRollerBearingElement",
    "LoadedAxialThrustCylindricalRollerBearingResults",
    "LoadedAxialThrustCylindricalRollerBearingRow",
    "LoadedAxialThrustNeedleRollerBearingElement",
    "LoadedAxialThrustNeedleRollerBearingResults",
    "LoadedAxialThrustNeedleRollerBearingRow",
    "LoadedBallBearingDutyCycle",
    "LoadedBallBearingElement",
    "LoadedBallBearingRaceResults",
    "LoadedBallBearingResults",
    "LoadedBallBearingRow",
    "LoadedCrossedRollerBearingElement",
    "LoadedCrossedRollerBearingResults",
    "LoadedCrossedRollerBearingRow",
    "LoadedCylindricalRollerBearingDutyCycle",
    "LoadedCylindricalRollerBearingElement",
    "LoadedCylindricalRollerBearingResults",
    "LoadedCylindricalRollerBearingRow",
    "LoadedDeepGrooveBallBearingElement",
    "LoadedDeepGrooveBallBearingResults",
    "LoadedDeepGrooveBallBearingRow",
    "LoadedElement",
    "LoadedFourPointContactBallBearingElement",
    "LoadedFourPointContactBallBearingRaceResults",
    "LoadedFourPointContactBallBearingResults",
    "LoadedFourPointContactBallBearingRow",
    "LoadedMultiPointContactBallBearingElement",
    "LoadedNeedleRollerBearingElement",
    "LoadedNeedleRollerBearingResults",
    "LoadedNeedleRollerBearingRow",
    "LoadedNonBarrelRollerBearingDutyCycle",
    "LoadedNonBarrelRollerBearingResults",
    "LoadedNonBarrelRollerBearingRow",
    "LoadedNonBarrelRollerBearingStripLoadResults",
    "LoadedNonBarrelRollerElement",
    "LoadedRollerBearingElement",
    "LoadedRollerBearingResults",
    "LoadedRollerBearingRow",
    "LoadedRollerStripLoadResults",
    "LoadedRollingBearingRaceResults",
    "LoadedRollingBearingResults",
    "LoadedRollingBearingRow",
    "LoadedSelfAligningBallBearingElement",
    "LoadedSelfAligningBallBearingResults",
    "LoadedSelfAligningBallBearingRow",
    "LoadedSphericalRadialRollerBearingElement",
    "LoadedSphericalRollerBearingElement",
    "LoadedSphericalRollerRadialBearingResults",
    "LoadedSphericalRollerRadialBearingRow",
    "LoadedSphericalRollerRadialBearingStripLoadResults",
    "LoadedSphericalRollerThrustBearingResults",
    "LoadedSphericalRollerThrustBearingRow",
    "LoadedSphericalThrustRollerBearingElement",
    "LoadedTaperRollerBearingDutyCycle",
    "LoadedTaperRollerBearingElement",
    "LoadedTaperRollerBearingResults",
    "LoadedTaperRollerBearingRow",
    "LoadedThreePointContactBallBearingElement",
    "LoadedThreePointContactBallBearingResults",
    "LoadedThreePointContactBallBearingRow",
    "LoadedThrustBallBearingElement",
    "LoadedThrustBallBearingResults",
    "LoadedThrustBallBearingRow",
    "LoadedToroidalRollerBearingElement",
    "LoadedToroidalRollerBearingResults",
    "LoadedToroidalRollerBearingRow",
    "LoadedToroidalRollerBearingStripLoadResults",
    "MaximumStaticContactStress",
    "MaximumStaticContactStressDutyCycle",
    "MaximumStaticContactStressResultsAbstract",
    "MaxStripLoadStressObject",
    "PermissibleContinuousAxialLoadResults",
    "PowerRatingF1EstimationMethod",
    "PreloadFactorLookupTable",
    "ResultsAtRollerOffset",
    "RingForceAndDisplacement",
    "RollerAnalysisMethod",
    "RollingBearingFrictionCoefficients",
    "RollingBearingSpeedResults",
    "SMTRibStressResults",
    "StressAtPosition",
    "ThreePointContactInternalClearance",
    "TrackTruncationSafetyFactorResults",
)

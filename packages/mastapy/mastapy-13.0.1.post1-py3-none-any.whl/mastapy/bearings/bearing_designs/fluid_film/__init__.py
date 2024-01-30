"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2181 import AxialFeedJournalBearing
    from ._2182 import AxialGrooveJournalBearing
    from ._2183 import AxialHoleJournalBearing
    from ._2184 import CircumferentialFeedJournalBearing
    from ._2185 import CylindricalHousingJournalBearing
    from ._2186 import MachineryEncasedJournalBearing
    from ._2187 import PadFluidFilmBearing
    from ._2188 import PedestalJournalBearing
    from ._2189 import PlainGreaseFilledJournalBearing
    from ._2190 import PlainGreaseFilledJournalBearingHousingType
    from ._2191 import PlainJournalBearing
    from ._2192 import PlainJournalHousing
    from ._2193 import PlainOilFedJournalBearing
    from ._2194 import TiltingPadJournalBearing
    from ._2195 import TiltingPadThrustBearing
else:
    import_structure = {
        "_2181": ["AxialFeedJournalBearing"],
        "_2182": ["AxialGrooveJournalBearing"],
        "_2183": ["AxialHoleJournalBearing"],
        "_2184": ["CircumferentialFeedJournalBearing"],
        "_2185": ["CylindricalHousingJournalBearing"],
        "_2186": ["MachineryEncasedJournalBearing"],
        "_2187": ["PadFluidFilmBearing"],
        "_2188": ["PedestalJournalBearing"],
        "_2189": ["PlainGreaseFilledJournalBearing"],
        "_2190": ["PlainGreaseFilledJournalBearingHousingType"],
        "_2191": ["PlainJournalBearing"],
        "_2192": ["PlainJournalHousing"],
        "_2193": ["PlainOilFedJournalBearing"],
        "_2194": ["TiltingPadJournalBearing"],
        "_2195": ["TiltingPadThrustBearing"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AxialFeedJournalBearing",
    "AxialGrooveJournalBearing",
    "AxialHoleJournalBearing",
    "CircumferentialFeedJournalBearing",
    "CylindricalHousingJournalBearing",
    "MachineryEncasedJournalBearing",
    "PadFluidFilmBearing",
    "PedestalJournalBearing",
    "PlainGreaseFilledJournalBearing",
    "PlainGreaseFilledJournalBearingHousingType",
    "PlainJournalBearing",
    "PlainJournalHousing",
    "PlainOilFedJournalBearing",
    "TiltingPadJournalBearing",
    "TiltingPadThrustBearing",
)

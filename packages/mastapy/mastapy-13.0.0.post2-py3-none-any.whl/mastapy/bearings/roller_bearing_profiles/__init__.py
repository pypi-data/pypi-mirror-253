"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1927 import ProfileDataToUse
    from ._1928 import ProfileSet
    from ._1929 import ProfileToFit
    from ._1930 import RollerBearingConicalProfile
    from ._1931 import RollerBearingCrownedProfile
    from ._1932 import RollerBearingDinLundbergProfile
    from ._1933 import RollerBearingFlatProfile
    from ._1934 import RollerBearingJohnsGoharProfile
    from ._1935 import RollerBearingLundbergProfile
    from ._1936 import RollerBearingProfile
    from ._1937 import RollerBearingUserSpecifiedProfile
    from ._1938 import RollerRaceProfilePoint
    from ._1939 import UserSpecifiedProfilePoint
    from ._1940 import UserSpecifiedRollerRaceProfilePoint
else:
    import_structure = {
        "_1927": ["ProfileDataToUse"],
        "_1928": ["ProfileSet"],
        "_1929": ["ProfileToFit"],
        "_1930": ["RollerBearingConicalProfile"],
        "_1931": ["RollerBearingCrownedProfile"],
        "_1932": ["RollerBearingDinLundbergProfile"],
        "_1933": ["RollerBearingFlatProfile"],
        "_1934": ["RollerBearingJohnsGoharProfile"],
        "_1935": ["RollerBearingLundbergProfile"],
        "_1936": ["RollerBearingProfile"],
        "_1937": ["RollerBearingUserSpecifiedProfile"],
        "_1938": ["RollerRaceProfilePoint"],
        "_1939": ["UserSpecifiedProfilePoint"],
        "_1940": ["UserSpecifiedRollerRaceProfilePoint"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProfileDataToUse",
    "ProfileSet",
    "ProfileToFit",
    "RollerBearingConicalProfile",
    "RollerBearingCrownedProfile",
    "RollerBearingDinLundbergProfile",
    "RollerBearingFlatProfile",
    "RollerBearingJohnsGoharProfile",
    "RollerBearingLundbergProfile",
    "RollerBearingProfile",
    "RollerBearingUserSpecifiedProfile",
    "RollerRaceProfilePoint",
    "UserSpecifiedProfilePoint",
    "UserSpecifiedRollerRaceProfilePoint",
)

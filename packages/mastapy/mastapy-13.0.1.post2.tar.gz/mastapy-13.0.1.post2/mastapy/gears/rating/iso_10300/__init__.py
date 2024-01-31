"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._420 import GeneralLoadFactorCalculationMethod
    from ._421 import Iso10300FinishingMethods
    from ._422 import ISO10300MeshSingleFlankRating
    from ._423 import ISO10300MeshSingleFlankRatingBevelMethodB2
    from ._424 import ISO10300MeshSingleFlankRatingHypoidMethodB2
    from ._425 import ISO10300MeshSingleFlankRatingMethodB1
    from ._426 import ISO10300MeshSingleFlankRatingMethodB2
    from ._427 import ISO10300RateableMesh
    from ._428 import ISO10300RatingMethod
    from ._429 import ISO10300SingleFlankRating
    from ._430 import ISO10300SingleFlankRatingBevelMethodB2
    from ._431 import ISO10300SingleFlankRatingHypoidMethodB2
    from ._432 import ISO10300SingleFlankRatingMethodB1
    from ._433 import ISO10300SingleFlankRatingMethodB2
    from ._434 import MountingConditionsOfPinionAndWheel
    from ._435 import PittingFactorCalculationMethod
    from ._436 import ProfileCrowningSetting
    from ._437 import VerificationOfContactPattern
else:
    import_structure = {
        "_420": ["GeneralLoadFactorCalculationMethod"],
        "_421": ["Iso10300FinishingMethods"],
        "_422": ["ISO10300MeshSingleFlankRating"],
        "_423": ["ISO10300MeshSingleFlankRatingBevelMethodB2"],
        "_424": ["ISO10300MeshSingleFlankRatingHypoidMethodB2"],
        "_425": ["ISO10300MeshSingleFlankRatingMethodB1"],
        "_426": ["ISO10300MeshSingleFlankRatingMethodB2"],
        "_427": ["ISO10300RateableMesh"],
        "_428": ["ISO10300RatingMethod"],
        "_429": ["ISO10300SingleFlankRating"],
        "_430": ["ISO10300SingleFlankRatingBevelMethodB2"],
        "_431": ["ISO10300SingleFlankRatingHypoidMethodB2"],
        "_432": ["ISO10300SingleFlankRatingMethodB1"],
        "_433": ["ISO10300SingleFlankRatingMethodB2"],
        "_434": ["MountingConditionsOfPinionAndWheel"],
        "_435": ["PittingFactorCalculationMethod"],
        "_436": ["ProfileCrowningSetting"],
        "_437": ["VerificationOfContactPattern"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "GeneralLoadFactorCalculationMethod",
    "Iso10300FinishingMethods",
    "ISO10300MeshSingleFlankRating",
    "ISO10300MeshSingleFlankRatingBevelMethodB2",
    "ISO10300MeshSingleFlankRatingHypoidMethodB2",
    "ISO10300MeshSingleFlankRatingMethodB1",
    "ISO10300MeshSingleFlankRatingMethodB2",
    "ISO10300RateableMesh",
    "ISO10300RatingMethod",
    "ISO10300SingleFlankRating",
    "ISO10300SingleFlankRatingBevelMethodB2",
    "ISO10300SingleFlankRatingHypoidMethodB2",
    "ISO10300SingleFlankRatingMethodB1",
    "ISO10300SingleFlankRatingMethodB2",
    "MountingConditionsOfPinionAndWheel",
    "PittingFactorCalculationMethod",
    "ProfileCrowningSetting",
    "VerificationOfContactPattern",
)

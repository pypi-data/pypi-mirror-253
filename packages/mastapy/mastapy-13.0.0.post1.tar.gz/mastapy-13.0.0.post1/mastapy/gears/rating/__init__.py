"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._353 import AbstractGearMeshRating
    from ._354 import AbstractGearRating
    from ._355 import AbstractGearSetRating
    from ._356 import BendingAndContactReportingObject
    from ._357 import FlankLoadingState
    from ._358 import GearDutyCycleRating
    from ._359 import GearFlankRating
    from ._360 import GearMeshRating
    from ._361 import GearRating
    from ._362 import GearSetDutyCycleRating
    from ._363 import GearSetRating
    from ._364 import GearSingleFlankRating
    from ._365 import MeshDutyCycleRating
    from ._366 import MeshSingleFlankRating
    from ._367 import RateableMesh
    from ._368 import SafetyFactorResults
else:
    import_structure = {
        "_353": ["AbstractGearMeshRating"],
        "_354": ["AbstractGearRating"],
        "_355": ["AbstractGearSetRating"],
        "_356": ["BendingAndContactReportingObject"],
        "_357": ["FlankLoadingState"],
        "_358": ["GearDutyCycleRating"],
        "_359": ["GearFlankRating"],
        "_360": ["GearMeshRating"],
        "_361": ["GearRating"],
        "_362": ["GearSetDutyCycleRating"],
        "_363": ["GearSetRating"],
        "_364": ["GearSingleFlankRating"],
        "_365": ["MeshDutyCycleRating"],
        "_366": ["MeshSingleFlankRating"],
        "_367": ["RateableMesh"],
        "_368": ["SafetyFactorResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractGearMeshRating",
    "AbstractGearRating",
    "AbstractGearSetRating",
    "BendingAndContactReportingObject",
    "FlankLoadingState",
    "GearDutyCycleRating",
    "GearFlankRating",
    "GearMeshRating",
    "GearRating",
    "GearSetDutyCycleRating",
    "GearSetRating",
    "GearSingleFlankRating",
    "MeshDutyCycleRating",
    "MeshSingleFlankRating",
    "RateableMesh",
    "SafetyFactorResults",
)

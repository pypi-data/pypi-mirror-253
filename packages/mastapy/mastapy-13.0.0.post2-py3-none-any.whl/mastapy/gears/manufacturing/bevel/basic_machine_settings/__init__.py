"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._821 import BasicConicalGearMachineSettings
    from ._822 import BasicConicalGearMachineSettingsFormate
    from ._823 import BasicConicalGearMachineSettingsGenerated
    from ._824 import CradleStyleConicalMachineSettingsGenerated
else:
    import_structure = {
        "_821": ["BasicConicalGearMachineSettings"],
        "_822": ["BasicConicalGearMachineSettingsFormate"],
        "_823": ["BasicConicalGearMachineSettingsGenerated"],
        "_824": ["CradleStyleConicalMachineSettingsGenerated"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BasicConicalGearMachineSettings",
    "BasicConicalGearMachineSettingsFormate",
    "BasicConicalGearMachineSettingsGenerated",
    "CradleStyleConicalMachineSettingsGenerated",
)

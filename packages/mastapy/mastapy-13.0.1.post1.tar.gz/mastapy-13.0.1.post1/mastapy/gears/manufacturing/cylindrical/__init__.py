"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._609 import CutterFlankSections
    from ._610 import CylindricalCutterDatabase
    from ._611 import CylindricalGearBlank
    from ._612 import CylindricalGearManufacturingConfig
    from ._613 import CylindricalGearSpecifiedMicroGeometry
    from ._614 import CylindricalGearSpecifiedProfile
    from ._615 import CylindricalHobDatabase
    from ._616 import CylindricalManufacturedGearDutyCycle
    from ._617 import CylindricalManufacturedGearLoadCase
    from ._618 import CylindricalManufacturedGearMeshDutyCycle
    from ._619 import CylindricalManufacturedGearMeshLoadCase
    from ._620 import CylindricalManufacturedGearSetDutyCycle
    from ._621 import CylindricalManufacturedGearSetLoadCase
    from ._622 import CylindricalMeshManufacturingConfig
    from ._623 import CylindricalMftFinishingMethods
    from ._624 import CylindricalMftRoughingMethods
    from ._625 import CylindricalSetManufacturingConfig
    from ._626 import CylindricalShaperDatabase
    from ._627 import Flank
    from ._628 import GearManufacturingConfigurationViewModel
    from ._629 import GearManufacturingConfigurationViewModelPlaceholder
    from ._630 import GearSetConfigViewModel
    from ._631 import HobEdgeTypes
    from ._632 import LeadModificationSegment
    from ._633 import MicroGeometryInputs
    from ._634 import MicroGeometryInputsLead
    from ._635 import MicroGeometryInputsProfile
    from ._636 import ModificationSegment
    from ._637 import ProfileModificationSegment
    from ._638 import SuitableCutterSetup
else:
    import_structure = {
        "_609": ["CutterFlankSections"],
        "_610": ["CylindricalCutterDatabase"],
        "_611": ["CylindricalGearBlank"],
        "_612": ["CylindricalGearManufacturingConfig"],
        "_613": ["CylindricalGearSpecifiedMicroGeometry"],
        "_614": ["CylindricalGearSpecifiedProfile"],
        "_615": ["CylindricalHobDatabase"],
        "_616": ["CylindricalManufacturedGearDutyCycle"],
        "_617": ["CylindricalManufacturedGearLoadCase"],
        "_618": ["CylindricalManufacturedGearMeshDutyCycle"],
        "_619": ["CylindricalManufacturedGearMeshLoadCase"],
        "_620": ["CylindricalManufacturedGearSetDutyCycle"],
        "_621": ["CylindricalManufacturedGearSetLoadCase"],
        "_622": ["CylindricalMeshManufacturingConfig"],
        "_623": ["CylindricalMftFinishingMethods"],
        "_624": ["CylindricalMftRoughingMethods"],
        "_625": ["CylindricalSetManufacturingConfig"],
        "_626": ["CylindricalShaperDatabase"],
        "_627": ["Flank"],
        "_628": ["GearManufacturingConfigurationViewModel"],
        "_629": ["GearManufacturingConfigurationViewModelPlaceholder"],
        "_630": ["GearSetConfigViewModel"],
        "_631": ["HobEdgeTypes"],
        "_632": ["LeadModificationSegment"],
        "_633": ["MicroGeometryInputs"],
        "_634": ["MicroGeometryInputsLead"],
        "_635": ["MicroGeometryInputsProfile"],
        "_636": ["ModificationSegment"],
        "_637": ["ProfileModificationSegment"],
        "_638": ["SuitableCutterSetup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterFlankSections",
    "CylindricalCutterDatabase",
    "CylindricalGearBlank",
    "CylindricalGearManufacturingConfig",
    "CylindricalGearSpecifiedMicroGeometry",
    "CylindricalGearSpecifiedProfile",
    "CylindricalHobDatabase",
    "CylindricalManufacturedGearDutyCycle",
    "CylindricalManufacturedGearLoadCase",
    "CylindricalManufacturedGearMeshDutyCycle",
    "CylindricalManufacturedGearMeshLoadCase",
    "CylindricalManufacturedGearSetDutyCycle",
    "CylindricalManufacturedGearSetLoadCase",
    "CylindricalMeshManufacturingConfig",
    "CylindricalMftFinishingMethods",
    "CylindricalMftRoughingMethods",
    "CylindricalSetManufacturingConfig",
    "CylindricalShaperDatabase",
    "Flank",
    "GearManufacturingConfigurationViewModel",
    "GearManufacturingConfigurationViewModelPlaceholder",
    "GearSetConfigViewModel",
    "HobEdgeTypes",
    "LeadModificationSegment",
    "MicroGeometryInputs",
    "MicroGeometryInputsLead",
    "MicroGeometryInputsProfile",
    "ModificationSegment",
    "ProfileModificationSegment",
    "SuitableCutterSetup",
)

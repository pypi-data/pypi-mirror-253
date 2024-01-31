"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._569 import BiasModification
    from ._570 import FlankMicroGeometry
    from ._571 import FlankSide
    from ._572 import LeadModification
    from ._573 import LocationOfEvaluationLowerLimit
    from ._574 import LocationOfEvaluationUpperLimit
    from ._575 import LocationOfRootReliefEvaluation
    from ._576 import LocationOfTipReliefEvaluation
    from ._577 import MainProfileReliefEndsAtTheStartOfRootReliefOption
    from ._578 import MainProfileReliefEndsAtTheStartOfTipReliefOption
    from ._579 import Modification
    from ._580 import ParabolicRootReliefStartsTangentToMainProfileRelief
    from ._581 import ParabolicTipReliefStartsTangentToMainProfileRelief
    from ._582 import ProfileModification
else:
    import_structure = {
        "_569": ["BiasModification"],
        "_570": ["FlankMicroGeometry"],
        "_571": ["FlankSide"],
        "_572": ["LeadModification"],
        "_573": ["LocationOfEvaluationLowerLimit"],
        "_574": ["LocationOfEvaluationUpperLimit"],
        "_575": ["LocationOfRootReliefEvaluation"],
        "_576": ["LocationOfTipReliefEvaluation"],
        "_577": ["MainProfileReliefEndsAtTheStartOfRootReliefOption"],
        "_578": ["MainProfileReliefEndsAtTheStartOfTipReliefOption"],
        "_579": ["Modification"],
        "_580": ["ParabolicRootReliefStartsTangentToMainProfileRelief"],
        "_581": ["ParabolicTipReliefStartsTangentToMainProfileRelief"],
        "_582": ["ProfileModification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BiasModification",
    "FlankMicroGeometry",
    "FlankSide",
    "LeadModification",
    "LocationOfEvaluationLowerLimit",
    "LocationOfEvaluationUpperLimit",
    "LocationOfRootReliefEvaluation",
    "LocationOfTipReliefEvaluation",
    "MainProfileReliefEndsAtTheStartOfRootReliefOption",
    "MainProfileReliefEndsAtTheStartOfTipReliefOption",
    "Modification",
    "ParabolicRootReliefStartsTangentToMainProfileRelief",
    "ParabolicTipReliefStartsTangentToMainProfileRelief",
    "ProfileModification",
)

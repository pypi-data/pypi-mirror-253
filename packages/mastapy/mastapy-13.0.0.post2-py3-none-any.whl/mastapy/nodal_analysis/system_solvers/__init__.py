"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._100 import BackwardEulerAccelerationStepHalvingTransientSolver
    from ._101 import BackwardEulerTransientSolver
    from ._102 import DenseStiffnessSolver
    from ._103 import DynamicSolver
    from ._104 import InternalTransientSolver
    from ._105 import LobattoIIIATransientSolver
    from ._106 import LobattoIIICTransientSolver
    from ._107 import NewmarkAccelerationTransientSolver
    from ._108 import NewmarkTransientSolver
    from ._109 import SemiImplicitTransientSolver
    from ._110 import SimpleAccelerationBasedStepHalvingTransientSolver
    from ._111 import SimpleVelocityBasedStepHalvingTransientSolver
    from ._112 import SingularDegreeOfFreedomAnalysis
    from ._113 import SingularValuesAnalysis
    from ._114 import SingularVectorAnalysis
    from ._115 import Solver
    from ._116 import StepHalvingTransientSolver
    from ._117 import StiffnessSolver
    from ._118 import TransientSolver
    from ._119 import WilsonThetaTransientSolver
else:
    import_structure = {
        "_100": ["BackwardEulerAccelerationStepHalvingTransientSolver"],
        "_101": ["BackwardEulerTransientSolver"],
        "_102": ["DenseStiffnessSolver"],
        "_103": ["DynamicSolver"],
        "_104": ["InternalTransientSolver"],
        "_105": ["LobattoIIIATransientSolver"],
        "_106": ["LobattoIIICTransientSolver"],
        "_107": ["NewmarkAccelerationTransientSolver"],
        "_108": ["NewmarkTransientSolver"],
        "_109": ["SemiImplicitTransientSolver"],
        "_110": ["SimpleAccelerationBasedStepHalvingTransientSolver"],
        "_111": ["SimpleVelocityBasedStepHalvingTransientSolver"],
        "_112": ["SingularDegreeOfFreedomAnalysis"],
        "_113": ["SingularValuesAnalysis"],
        "_114": ["SingularVectorAnalysis"],
        "_115": ["Solver"],
        "_116": ["StepHalvingTransientSolver"],
        "_117": ["StiffnessSolver"],
        "_118": ["TransientSolver"],
        "_119": ["WilsonThetaTransientSolver"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BackwardEulerAccelerationStepHalvingTransientSolver",
    "BackwardEulerTransientSolver",
    "DenseStiffnessSolver",
    "DynamicSolver",
    "InternalTransientSolver",
    "LobattoIIIATransientSolver",
    "LobattoIIICTransientSolver",
    "NewmarkAccelerationTransientSolver",
    "NewmarkTransientSolver",
    "SemiImplicitTransientSolver",
    "SimpleAccelerationBasedStepHalvingTransientSolver",
    "SimpleVelocityBasedStepHalvingTransientSolver",
    "SingularDegreeOfFreedomAnalysis",
    "SingularValuesAnalysis",
    "SingularVectorAnalysis",
    "Solver",
    "StepHalvingTransientSolver",
    "StiffnessSolver",
    "TransientSolver",
    "WilsonThetaTransientSolver",
)

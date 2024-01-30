"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._46 import AbstractLinearConnectionProperties
    from ._47 import AbstractNodalMatrix
    from ._48 import AnalysisSettings
    from ._49 import AnalysisSettingsDatabase
    from ._50 import AnalysisSettingsItem
    from ._51 import BarGeometry
    from ._52 import BarModelAnalysisType
    from ._53 import BarModelExportType
    from ._54 import CouplingType
    from ._55 import CylindricalMisalignmentCalculator
    from ._56 import DampingScalingTypeForInitialTransients
    from ._57 import DiagonalNonLinearStiffness
    from ._58 import ElementOrder
    from ._59 import FEMeshElementEntityOption
    from ._60 import FEMeshingOperation
    from ._61 import FEMeshingOptions
    from ._62 import FEMeshingProblem
    from ._63 import FEMeshingProblems
    from ._64 import FEModalFrequencyComparison
    from ._65 import FENodeOption
    from ._66 import FEStiffness
    from ._67 import FEStiffnessNode
    from ._68 import FEUserSettings
    from ._69 import GearMeshContactStatus
    from ._70 import GravityForceSource
    from ._71 import IntegrationMethod
    from ._72 import LinearDampingConnectionProperties
    from ._73 import LinearStiffnessProperties
    from ._74 import LoadingStatus
    from ._75 import LocalNodeInfo
    from ._76 import MeshingDiameterForGear
    from ._77 import MeshingOptions
    from ._78 import ModeInputType
    from ._79 import NodalMatrix
    from ._80 import NodalMatrixRow
    from ._81 import RatingTypeForBearingReliability
    from ._82 import RatingTypeForShaftReliability
    from ._83 import ResultLoggingFrequency
    from ._84 import SectionEnd
    from ._85 import ShaftFEMeshingOptions
    from ._86 import SparseNodalMatrix
    from ._87 import StressResultsType
    from ._88 import TransientSolverOptions
    from ._89 import TransientSolverStatus
    from ._90 import TransientSolverToleranceInputMethod
    from ._91 import ValueInputOption
    from ._92 import VolumeElementShape
else:
    import_structure = {
        "_46": ["AbstractLinearConnectionProperties"],
        "_47": ["AbstractNodalMatrix"],
        "_48": ["AnalysisSettings"],
        "_49": ["AnalysisSettingsDatabase"],
        "_50": ["AnalysisSettingsItem"],
        "_51": ["BarGeometry"],
        "_52": ["BarModelAnalysisType"],
        "_53": ["BarModelExportType"],
        "_54": ["CouplingType"],
        "_55": ["CylindricalMisalignmentCalculator"],
        "_56": ["DampingScalingTypeForInitialTransients"],
        "_57": ["DiagonalNonLinearStiffness"],
        "_58": ["ElementOrder"],
        "_59": ["FEMeshElementEntityOption"],
        "_60": ["FEMeshingOperation"],
        "_61": ["FEMeshingOptions"],
        "_62": ["FEMeshingProblem"],
        "_63": ["FEMeshingProblems"],
        "_64": ["FEModalFrequencyComparison"],
        "_65": ["FENodeOption"],
        "_66": ["FEStiffness"],
        "_67": ["FEStiffnessNode"],
        "_68": ["FEUserSettings"],
        "_69": ["GearMeshContactStatus"],
        "_70": ["GravityForceSource"],
        "_71": ["IntegrationMethod"],
        "_72": ["LinearDampingConnectionProperties"],
        "_73": ["LinearStiffnessProperties"],
        "_74": ["LoadingStatus"],
        "_75": ["LocalNodeInfo"],
        "_76": ["MeshingDiameterForGear"],
        "_77": ["MeshingOptions"],
        "_78": ["ModeInputType"],
        "_79": ["NodalMatrix"],
        "_80": ["NodalMatrixRow"],
        "_81": ["RatingTypeForBearingReliability"],
        "_82": ["RatingTypeForShaftReliability"],
        "_83": ["ResultLoggingFrequency"],
        "_84": ["SectionEnd"],
        "_85": ["ShaftFEMeshingOptions"],
        "_86": ["SparseNodalMatrix"],
        "_87": ["StressResultsType"],
        "_88": ["TransientSolverOptions"],
        "_89": ["TransientSolverStatus"],
        "_90": ["TransientSolverToleranceInputMethod"],
        "_91": ["ValueInputOption"],
        "_92": ["VolumeElementShape"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractLinearConnectionProperties",
    "AbstractNodalMatrix",
    "AnalysisSettings",
    "AnalysisSettingsDatabase",
    "AnalysisSettingsItem",
    "BarGeometry",
    "BarModelAnalysisType",
    "BarModelExportType",
    "CouplingType",
    "CylindricalMisalignmentCalculator",
    "DampingScalingTypeForInitialTransients",
    "DiagonalNonLinearStiffness",
    "ElementOrder",
    "FEMeshElementEntityOption",
    "FEMeshingOperation",
    "FEMeshingOptions",
    "FEMeshingProblem",
    "FEMeshingProblems",
    "FEModalFrequencyComparison",
    "FENodeOption",
    "FEStiffness",
    "FEStiffnessNode",
    "FEUserSettings",
    "GearMeshContactStatus",
    "GravityForceSource",
    "IntegrationMethod",
    "LinearDampingConnectionProperties",
    "LinearStiffnessProperties",
    "LoadingStatus",
    "LocalNodeInfo",
    "MeshingDiameterForGear",
    "MeshingOptions",
    "ModeInputType",
    "NodalMatrix",
    "NodalMatrixRow",
    "RatingTypeForBearingReliability",
    "RatingTypeForShaftReliability",
    "ResultLoggingFrequency",
    "SectionEnd",
    "ShaftFEMeshingOptions",
    "SparseNodalMatrix",
    "StressResultsType",
    "TransientSolverOptions",
    "TransientSolverStatus",
    "TransientSolverToleranceInputMethod",
    "ValueInputOption",
    "VolumeElementShape",
)

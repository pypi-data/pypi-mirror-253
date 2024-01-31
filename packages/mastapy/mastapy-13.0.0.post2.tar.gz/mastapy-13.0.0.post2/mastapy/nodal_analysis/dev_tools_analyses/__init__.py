"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._178 import DrawStyleForFE
    from ._179 import EigenvalueOptions
    from ._180 import ElementFaceGroup
    from ._181 import ElementGroup
    from ._182 import FEEntityGroup
    from ._183 import FEEntityGroupInteger
    from ._184 import FEModel
    from ._185 import FEModelComponentDrawStyle
    from ._186 import FEModelHarmonicAnalysisDrawStyle
    from ._187 import FEModelInstanceDrawStyle
    from ._188 import FEModelModalAnalysisDrawStyle
    from ._189 import FEModelPart
    from ._190 import FEModelSetupViewType
    from ._191 import FEModelStaticAnalysisDrawStyle
    from ._192 import FEModelTabDrawStyle
    from ._193 import FEModelTransparencyDrawStyle
    from ._194 import FENodeSelectionDrawStyle
    from ._195 import FESelectionMode
    from ._196 import FESurfaceAndNonDeformedDrawingOption
    from ._197 import FESurfaceDrawingOption
    from ._198 import MassMatrixType
    from ._199 import ModelSplittingMethod
    from ._200 import NodeGroup
    from ._201 import NoneSelectedAllOption
    from ._202 import RigidCouplingType
else:
    import_structure = {
        "_178": ["DrawStyleForFE"],
        "_179": ["EigenvalueOptions"],
        "_180": ["ElementFaceGroup"],
        "_181": ["ElementGroup"],
        "_182": ["FEEntityGroup"],
        "_183": ["FEEntityGroupInteger"],
        "_184": ["FEModel"],
        "_185": ["FEModelComponentDrawStyle"],
        "_186": ["FEModelHarmonicAnalysisDrawStyle"],
        "_187": ["FEModelInstanceDrawStyle"],
        "_188": ["FEModelModalAnalysisDrawStyle"],
        "_189": ["FEModelPart"],
        "_190": ["FEModelSetupViewType"],
        "_191": ["FEModelStaticAnalysisDrawStyle"],
        "_192": ["FEModelTabDrawStyle"],
        "_193": ["FEModelTransparencyDrawStyle"],
        "_194": ["FENodeSelectionDrawStyle"],
        "_195": ["FESelectionMode"],
        "_196": ["FESurfaceAndNonDeformedDrawingOption"],
        "_197": ["FESurfaceDrawingOption"],
        "_198": ["MassMatrixType"],
        "_199": ["ModelSplittingMethod"],
        "_200": ["NodeGroup"],
        "_201": ["NoneSelectedAllOption"],
        "_202": ["RigidCouplingType"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "DrawStyleForFE",
    "EigenvalueOptions",
    "ElementFaceGroup",
    "ElementGroup",
    "FEEntityGroup",
    "FEEntityGroupInteger",
    "FEModel",
    "FEModelComponentDrawStyle",
    "FEModelHarmonicAnalysisDrawStyle",
    "FEModelInstanceDrawStyle",
    "FEModelModalAnalysisDrawStyle",
    "FEModelPart",
    "FEModelSetupViewType",
    "FEModelStaticAnalysisDrawStyle",
    "FEModelTabDrawStyle",
    "FEModelTransparencyDrawStyle",
    "FENodeSelectionDrawStyle",
    "FESelectionMode",
    "FESurfaceAndNonDeformedDrawingOption",
    "FESurfaceDrawingOption",
    "MassMatrixType",
    "ModelSplittingMethod",
    "NodeGroup",
    "NoneSelectedAllOption",
    "RigidCouplingType",
)

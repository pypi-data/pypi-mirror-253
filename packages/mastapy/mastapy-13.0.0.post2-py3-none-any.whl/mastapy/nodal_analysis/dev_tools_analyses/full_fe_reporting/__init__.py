"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._203 import ContactPairReporting
    from ._204 import CoordinateSystemReporting
    from ._205 import DegreeOfFreedomType
    from ._206 import ElasticModulusOrthotropicComponents
    from ._207 import ElementDetailsForFEModel
    from ._208 import ElementPropertiesBase
    from ._209 import ElementPropertiesBeam
    from ._210 import ElementPropertiesInterface
    from ._211 import ElementPropertiesMass
    from ._212 import ElementPropertiesRigid
    from ._213 import ElementPropertiesShell
    from ._214 import ElementPropertiesSolid
    from ._215 import ElementPropertiesSpringDashpot
    from ._216 import ElementPropertiesWithMaterial
    from ._217 import MaterialPropertiesReporting
    from ._218 import NodeDetailsForFEModel
    from ._219 import PoissonRatioOrthotropicComponents
    from ._220 import RigidElementNodeDegreesOfFreedom
    from ._221 import ShearModulusOrthotropicComponents
    from ._222 import ThermalExpansionOrthotropicComponents
else:
    import_structure = {
        "_203": ["ContactPairReporting"],
        "_204": ["CoordinateSystemReporting"],
        "_205": ["DegreeOfFreedomType"],
        "_206": ["ElasticModulusOrthotropicComponents"],
        "_207": ["ElementDetailsForFEModel"],
        "_208": ["ElementPropertiesBase"],
        "_209": ["ElementPropertiesBeam"],
        "_210": ["ElementPropertiesInterface"],
        "_211": ["ElementPropertiesMass"],
        "_212": ["ElementPropertiesRigid"],
        "_213": ["ElementPropertiesShell"],
        "_214": ["ElementPropertiesSolid"],
        "_215": ["ElementPropertiesSpringDashpot"],
        "_216": ["ElementPropertiesWithMaterial"],
        "_217": ["MaterialPropertiesReporting"],
        "_218": ["NodeDetailsForFEModel"],
        "_219": ["PoissonRatioOrthotropicComponents"],
        "_220": ["RigidElementNodeDegreesOfFreedom"],
        "_221": ["ShearModulusOrthotropicComponents"],
        "_222": ["ThermalExpansionOrthotropicComponents"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ContactPairReporting",
    "CoordinateSystemReporting",
    "DegreeOfFreedomType",
    "ElasticModulusOrthotropicComponents",
    "ElementDetailsForFEModel",
    "ElementPropertiesBase",
    "ElementPropertiesBeam",
    "ElementPropertiesInterface",
    "ElementPropertiesMass",
    "ElementPropertiesRigid",
    "ElementPropertiesShell",
    "ElementPropertiesSolid",
    "ElementPropertiesSpringDashpot",
    "ElementPropertiesWithMaterial",
    "MaterialPropertiesReporting",
    "NodeDetailsForFEModel",
    "PoissonRatioOrthotropicComponents",
    "RigidElementNodeDegreesOfFreedom",
    "ShearModulusOrthotropicComponents",
    "ThermalExpansionOrthotropicComponents",
)

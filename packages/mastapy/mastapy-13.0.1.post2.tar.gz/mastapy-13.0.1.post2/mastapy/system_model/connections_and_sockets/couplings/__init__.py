"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2342 import ClutchConnection
    from ._2343 import ClutchSocket
    from ._2344 import ConceptCouplingConnection
    from ._2345 import ConceptCouplingSocket
    from ._2346 import CouplingConnection
    from ._2347 import CouplingSocket
    from ._2348 import PartToPartShearCouplingConnection
    from ._2349 import PartToPartShearCouplingSocket
    from ._2350 import SpringDamperConnection
    from ._2351 import SpringDamperSocket
    from ._2352 import TorqueConverterConnection
    from ._2353 import TorqueConverterPumpSocket
    from ._2354 import TorqueConverterTurbineSocket
else:
    import_structure = {
        "_2342": ["ClutchConnection"],
        "_2343": ["ClutchSocket"],
        "_2344": ["ConceptCouplingConnection"],
        "_2345": ["ConceptCouplingSocket"],
        "_2346": ["CouplingConnection"],
        "_2347": ["CouplingSocket"],
        "_2348": ["PartToPartShearCouplingConnection"],
        "_2349": ["PartToPartShearCouplingSocket"],
        "_2350": ["SpringDamperConnection"],
        "_2351": ["SpringDamperSocket"],
        "_2352": ["TorqueConverterConnection"],
        "_2353": ["TorqueConverterPumpSocket"],
        "_2354": ["TorqueConverterTurbineSocket"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ClutchConnection",
    "ClutchSocket",
    "ConceptCouplingConnection",
    "ConceptCouplingSocket",
    "CouplingConnection",
    "CouplingSocket",
    "PartToPartShearCouplingConnection",
    "PartToPartShearCouplingSocket",
    "SpringDamperConnection",
    "SpringDamperSocket",
    "TorqueConverterConnection",
    "TorqueConverterPumpSocket",
    "TorqueConverterTurbineSocket",
)

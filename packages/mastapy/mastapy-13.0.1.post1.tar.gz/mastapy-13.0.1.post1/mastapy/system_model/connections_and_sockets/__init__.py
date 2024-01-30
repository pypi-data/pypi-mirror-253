"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2265 import AbstractShaftToMountableComponentConnection
    from ._2266 import BearingInnerSocket
    from ._2267 import BearingOuterSocket
    from ._2268 import BeltConnection
    from ._2269 import CoaxialConnection
    from ._2270 import ComponentConnection
    from ._2271 import ComponentMeasurer
    from ._2272 import Connection
    from ._2273 import CVTBeltConnection
    from ._2274 import CVTPulleySocket
    from ._2275 import CylindricalComponentConnection
    from ._2276 import CylindricalSocket
    from ._2277 import DatumMeasurement
    from ._2278 import ElectricMachineStatorSocket
    from ._2279 import InnerShaftSocket
    from ._2280 import InnerShaftSocketBase
    from ._2281 import InterMountableComponentConnection
    from ._2282 import MountableComponentInnerSocket
    from ._2283 import MountableComponentOuterSocket
    from ._2284 import MountableComponentSocket
    from ._2285 import OuterShaftSocket
    from ._2286 import OuterShaftSocketBase
    from ._2287 import PlanetaryConnection
    from ._2288 import PlanetarySocket
    from ._2289 import PlanetarySocketBase
    from ._2290 import PulleySocket
    from ._2291 import RealignmentResult
    from ._2292 import RollingRingConnection
    from ._2293 import RollingRingSocket
    from ._2294 import ShaftSocket
    from ._2295 import ShaftToMountableComponentConnection
    from ._2296 import Socket
    from ._2297 import SocketConnectionOptions
    from ._2298 import SocketConnectionSelection
else:
    import_structure = {
        "_2265": ["AbstractShaftToMountableComponentConnection"],
        "_2266": ["BearingInnerSocket"],
        "_2267": ["BearingOuterSocket"],
        "_2268": ["BeltConnection"],
        "_2269": ["CoaxialConnection"],
        "_2270": ["ComponentConnection"],
        "_2271": ["ComponentMeasurer"],
        "_2272": ["Connection"],
        "_2273": ["CVTBeltConnection"],
        "_2274": ["CVTPulleySocket"],
        "_2275": ["CylindricalComponentConnection"],
        "_2276": ["CylindricalSocket"],
        "_2277": ["DatumMeasurement"],
        "_2278": ["ElectricMachineStatorSocket"],
        "_2279": ["InnerShaftSocket"],
        "_2280": ["InnerShaftSocketBase"],
        "_2281": ["InterMountableComponentConnection"],
        "_2282": ["MountableComponentInnerSocket"],
        "_2283": ["MountableComponentOuterSocket"],
        "_2284": ["MountableComponentSocket"],
        "_2285": ["OuterShaftSocket"],
        "_2286": ["OuterShaftSocketBase"],
        "_2287": ["PlanetaryConnection"],
        "_2288": ["PlanetarySocket"],
        "_2289": ["PlanetarySocketBase"],
        "_2290": ["PulleySocket"],
        "_2291": ["RealignmentResult"],
        "_2292": ["RollingRingConnection"],
        "_2293": ["RollingRingSocket"],
        "_2294": ["ShaftSocket"],
        "_2295": ["ShaftToMountableComponentConnection"],
        "_2296": ["Socket"],
        "_2297": ["SocketConnectionOptions"],
        "_2298": ["SocketConnectionSelection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractShaftToMountableComponentConnection",
    "BearingInnerSocket",
    "BearingOuterSocket",
    "BeltConnection",
    "CoaxialConnection",
    "ComponentConnection",
    "ComponentMeasurer",
    "Connection",
    "CVTBeltConnection",
    "CVTPulleySocket",
    "CylindricalComponentConnection",
    "CylindricalSocket",
    "DatumMeasurement",
    "ElectricMachineStatorSocket",
    "InnerShaftSocket",
    "InnerShaftSocketBase",
    "InterMountableComponentConnection",
    "MountableComponentInnerSocket",
    "MountableComponentOuterSocket",
    "MountableComponentSocket",
    "OuterShaftSocket",
    "OuterShaftSocketBase",
    "PlanetaryConnection",
    "PlanetarySocket",
    "PlanetarySocketBase",
    "PulleySocket",
    "RealignmentResult",
    "RollingRingConnection",
    "RollingRingSocket",
    "ShaftSocket",
    "ShaftToMountableComponentConnection",
    "Socket",
    "SocketConnectionOptions",
    "SocketConnectionSelection",
)

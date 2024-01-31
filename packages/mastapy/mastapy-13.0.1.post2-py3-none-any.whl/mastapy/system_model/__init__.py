"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2200 import Design
    from ._2201 import ComponentDampingOption
    from ._2202 import ConceptCouplingSpeedRatioSpecificationMethod
    from ._2203 import DesignEntity
    from ._2204 import DesignEntityId
    from ._2205 import DesignSettings
    from ._2206 import DutyCycleImporter
    from ._2207 import DutyCycleImporterDesignEntityMatch
    from ._2208 import ElectricMachineGroup
    from ._2209 import ExternalFullFELoader
    from ._2210 import HypoidWindUpRemovalMethod
    from ._2211 import IncludeDutyCycleOption
    from ._2212 import MASTASettings
    from ._2213 import MemorySummary
    from ._2214 import MeshStiffnessModel
    from ._2215 import PlanetPinManufacturingErrorsCoordinateSystem
    from ._2216 import PowerLoadDragTorqueSpecificationMethod
    from ._2217 import PowerLoadInputTorqueSpecificationMethod
    from ._2218 import PowerLoadPIDControlSpeedInputType
    from ._2219 import PowerLoadType
    from ._2220 import RelativeComponentAlignment
    from ._2221 import RelativeOffsetOption
    from ._2222 import SystemReporting
    from ._2223 import ThermalExpansionOptionForGroundedNodes
    from ._2224 import TransmissionTemperatureSet
else:
    import_structure = {
        "_2200": ["Design"],
        "_2201": ["ComponentDampingOption"],
        "_2202": ["ConceptCouplingSpeedRatioSpecificationMethod"],
        "_2203": ["DesignEntity"],
        "_2204": ["DesignEntityId"],
        "_2205": ["DesignSettings"],
        "_2206": ["DutyCycleImporter"],
        "_2207": ["DutyCycleImporterDesignEntityMatch"],
        "_2208": ["ElectricMachineGroup"],
        "_2209": ["ExternalFullFELoader"],
        "_2210": ["HypoidWindUpRemovalMethod"],
        "_2211": ["IncludeDutyCycleOption"],
        "_2212": ["MASTASettings"],
        "_2213": ["MemorySummary"],
        "_2214": ["MeshStiffnessModel"],
        "_2215": ["PlanetPinManufacturingErrorsCoordinateSystem"],
        "_2216": ["PowerLoadDragTorqueSpecificationMethod"],
        "_2217": ["PowerLoadInputTorqueSpecificationMethod"],
        "_2218": ["PowerLoadPIDControlSpeedInputType"],
        "_2219": ["PowerLoadType"],
        "_2220": ["RelativeComponentAlignment"],
        "_2221": ["RelativeOffsetOption"],
        "_2222": ["SystemReporting"],
        "_2223": ["ThermalExpansionOptionForGroundedNodes"],
        "_2224": ["TransmissionTemperatureSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Design",
    "ComponentDampingOption",
    "ConceptCouplingSpeedRatioSpecificationMethod",
    "DesignEntity",
    "DesignEntityId",
    "DesignSettings",
    "DutyCycleImporter",
    "DutyCycleImporterDesignEntityMatch",
    "ElectricMachineGroup",
    "ExternalFullFELoader",
    "HypoidWindUpRemovalMethod",
    "IncludeDutyCycleOption",
    "MASTASettings",
    "MemorySummary",
    "MeshStiffnessModel",
    "PlanetPinManufacturingErrorsCoordinateSystem",
    "PowerLoadDragTorqueSpecificationMethod",
    "PowerLoadInputTorqueSpecificationMethod",
    "PowerLoadPIDControlSpeedInputType",
    "PowerLoadType",
    "RelativeComponentAlignment",
    "RelativeOffsetOption",
    "SystemReporting",
    "ThermalExpansionOptionForGroundedNodes",
    "TransmissionTemperatureSet",
)

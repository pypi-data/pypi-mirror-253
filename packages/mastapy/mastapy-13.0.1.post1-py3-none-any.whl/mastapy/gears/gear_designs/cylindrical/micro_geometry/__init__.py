"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1093 import CylindricalGearBiasModification
    from ._1094 import CylindricalGearCommonFlankMicroGeometry
    from ._1095 import CylindricalGearFlankMicroGeometry
    from ._1096 import CylindricalGearLeadModification
    from ._1097 import CylindricalGearLeadModificationAtProfilePosition
    from ._1098 import CylindricalGearMeshMicroGeometry
    from ._1099 import CylindricalGearMeshMicroGeometryDutyCycle
    from ._1100 import CylindricalGearMicroGeometry
    from ._1101 import CylindricalGearMicroGeometryBase
    from ._1102 import CylindricalGearMicroGeometryDutyCycle
    from ._1103 import CylindricalGearMicroGeometryMap
    from ._1104 import CylindricalGearMicroGeometryPerTooth
    from ._1105 import CylindricalGearProfileModification
    from ._1106 import CylindricalGearProfileModificationAtFaceWidthPosition
    from ._1107 import CylindricalGearSetMicroGeometry
    from ._1108 import CylindricalGearSetMicroGeometryDutyCycle
    from ._1109 import CylindricalGearToothMicroGeometry
    from ._1110 import CylindricalGearTriangularEndModification
    from ._1111 import CylindricalGearTriangularEndModificationAtOrientation
    from ._1112 import DrawDefiningGearOrBoth
    from ._1113 import GearAlignment
    from ._1114 import LeadFormReliefWithDeviation
    from ._1115 import LeadReliefWithDeviation
    from ._1116 import LeadSlopeReliefWithDeviation
    from ._1117 import LinearCylindricalGearTriangularEndModification
    from ._1118 import MeasuredMapDataTypes
    from ._1119 import MeshAlignment
    from ._1120 import MeshedCylindricalGearFlankMicroGeometry
    from ._1121 import MeshedCylindricalGearMicroGeometry
    from ._1122 import MicroGeometryLeadToleranceChartView
    from ._1123 import MicroGeometryViewingOptions
    from ._1124 import ParabolicCylindricalGearTriangularEndModification
    from ._1125 import ProfileFormReliefWithDeviation
    from ._1126 import ProfileReliefWithDeviation
    from ._1127 import ProfileSlopeReliefWithDeviation
    from ._1128 import ReliefWithDeviation
    from ._1129 import SingleCylindricalGearTriangularEndModification
    from ._1130 import TotalLeadReliefWithDeviation
    from ._1131 import TotalProfileReliefWithDeviation
else:
    import_structure = {
        "_1093": ["CylindricalGearBiasModification"],
        "_1094": ["CylindricalGearCommonFlankMicroGeometry"],
        "_1095": ["CylindricalGearFlankMicroGeometry"],
        "_1096": ["CylindricalGearLeadModification"],
        "_1097": ["CylindricalGearLeadModificationAtProfilePosition"],
        "_1098": ["CylindricalGearMeshMicroGeometry"],
        "_1099": ["CylindricalGearMeshMicroGeometryDutyCycle"],
        "_1100": ["CylindricalGearMicroGeometry"],
        "_1101": ["CylindricalGearMicroGeometryBase"],
        "_1102": ["CylindricalGearMicroGeometryDutyCycle"],
        "_1103": ["CylindricalGearMicroGeometryMap"],
        "_1104": ["CylindricalGearMicroGeometryPerTooth"],
        "_1105": ["CylindricalGearProfileModification"],
        "_1106": ["CylindricalGearProfileModificationAtFaceWidthPosition"],
        "_1107": ["CylindricalGearSetMicroGeometry"],
        "_1108": ["CylindricalGearSetMicroGeometryDutyCycle"],
        "_1109": ["CylindricalGearToothMicroGeometry"],
        "_1110": ["CylindricalGearTriangularEndModification"],
        "_1111": ["CylindricalGearTriangularEndModificationAtOrientation"],
        "_1112": ["DrawDefiningGearOrBoth"],
        "_1113": ["GearAlignment"],
        "_1114": ["LeadFormReliefWithDeviation"],
        "_1115": ["LeadReliefWithDeviation"],
        "_1116": ["LeadSlopeReliefWithDeviation"],
        "_1117": ["LinearCylindricalGearTriangularEndModification"],
        "_1118": ["MeasuredMapDataTypes"],
        "_1119": ["MeshAlignment"],
        "_1120": ["MeshedCylindricalGearFlankMicroGeometry"],
        "_1121": ["MeshedCylindricalGearMicroGeometry"],
        "_1122": ["MicroGeometryLeadToleranceChartView"],
        "_1123": ["MicroGeometryViewingOptions"],
        "_1124": ["ParabolicCylindricalGearTriangularEndModification"],
        "_1125": ["ProfileFormReliefWithDeviation"],
        "_1126": ["ProfileReliefWithDeviation"],
        "_1127": ["ProfileSlopeReliefWithDeviation"],
        "_1128": ["ReliefWithDeviation"],
        "_1129": ["SingleCylindricalGearTriangularEndModification"],
        "_1130": ["TotalLeadReliefWithDeviation"],
        "_1131": ["TotalProfileReliefWithDeviation"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CylindricalGearBiasModification",
    "CylindricalGearCommonFlankMicroGeometry",
    "CylindricalGearFlankMicroGeometry",
    "CylindricalGearLeadModification",
    "CylindricalGearLeadModificationAtProfilePosition",
    "CylindricalGearMeshMicroGeometry",
    "CylindricalGearMeshMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometry",
    "CylindricalGearMicroGeometryBase",
    "CylindricalGearMicroGeometryDutyCycle",
    "CylindricalGearMicroGeometryMap",
    "CylindricalGearMicroGeometryPerTooth",
    "CylindricalGearProfileModification",
    "CylindricalGearProfileModificationAtFaceWidthPosition",
    "CylindricalGearSetMicroGeometry",
    "CylindricalGearSetMicroGeometryDutyCycle",
    "CylindricalGearToothMicroGeometry",
    "CylindricalGearTriangularEndModification",
    "CylindricalGearTriangularEndModificationAtOrientation",
    "DrawDefiningGearOrBoth",
    "GearAlignment",
    "LeadFormReliefWithDeviation",
    "LeadReliefWithDeviation",
    "LeadSlopeReliefWithDeviation",
    "LinearCylindricalGearTriangularEndModification",
    "MeasuredMapDataTypes",
    "MeshAlignment",
    "MeshedCylindricalGearFlankMicroGeometry",
    "MeshedCylindricalGearMicroGeometry",
    "MicroGeometryLeadToleranceChartView",
    "MicroGeometryViewingOptions",
    "ParabolicCylindricalGearTriangularEndModification",
    "ProfileFormReliefWithDeviation",
    "ProfileReliefWithDeviation",
    "ProfileSlopeReliefWithDeviation",
    "ReliefWithDeviation",
    "SingleCylindricalGearTriangularEndModification",
    "TotalLeadReliefWithDeviation",
    "TotalProfileReliefWithDeviation",
)

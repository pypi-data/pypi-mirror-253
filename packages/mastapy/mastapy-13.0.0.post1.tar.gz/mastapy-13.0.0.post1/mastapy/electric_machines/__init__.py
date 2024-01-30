"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1243 import AbstractStator
    from ._1244 import AbstractToothAndSlot
    from ._1245 import AirGapPartition
    from ._1246 import CADConductor
    from ._1247 import CADElectricMachineDetail
    from ._1248 import CADMagnetsForLayer
    from ._1249 import CADRotor
    from ._1250 import CADStator
    from ._1251 import CADToothAndSlot
    from ._1252 import Coil
    from ._1253 import CoilPositionInSlot
    from ._1254 import CoolingDuctLayerSpecification
    from ._1255 import CoolingDuctShape
    from ._1256 import CoreLossBuildFactorSpecificationMethod
    from ._1257 import CoreLossCoefficients
    from ._1258 import DoubleLayerWindingSlotPositions
    from ._1259 import DQAxisConvention
    from ._1260 import Eccentricity
    from ._1261 import ElectricMachineDetail
    from ._1262 import ElectricMachineDetailInitialInformation
    from ._1263 import ElectricMachineMechanicalAnalysisMeshingOptions
    from ._1264 import ElectricMachineMeshingOptions
    from ._1265 import ElectricMachineMeshingOptionsBase
    from ._1266 import ElectricMachineSetup
    from ._1267 import ElectricMachineType
    from ._1268 import FillFactorSpecificationMethod
    from ._1269 import FluxBarrierOrWeb
    from ._1270 import FluxBarrierStyle
    from ._1271 import HairpinConductor
    from ._1272 import HarmonicLoadDataControlExcitationOptionForElectricMachineMode
    from ._1273 import IndividualConductorSpecificationSource
    from ._1274 import InteriorPermanentMagnetAndSynchronousReluctanceRotor
    from ._1275 import InteriorPermanentMagnetMachine
    from ._1276 import IronLossCoefficientSpecificationMethod
    from ._1277 import MagnetClearance
    from ._1278 import MagnetConfiguration
    from ._1279 import MagnetData
    from ._1280 import MagnetDesign
    from ._1281 import MagnetForLayer
    from ._1282 import MagnetMaterial
    from ._1283 import MagnetMaterialDatabase
    from ._1284 import MotorRotorSideFaceDetail
    from ._1285 import NonCADElectricMachineDetail
    from ._1286 import NotchShape
    from ._1287 import NotchSpecification
    from ._1288 import PermanentMagnetAssistedSynchronousReluctanceMachine
    from ._1289 import PermanentMagnetRotor
    from ._1290 import Phase
    from ._1291 import RegionID
    from ._1292 import Rotor
    from ._1293 import RotorInternalLayerSpecification
    from ._1294 import RotorSkewSlice
    from ._1295 import RotorType
    from ._1296 import SingleOrDoubleLayerWindings
    from ._1297 import SlotSectionDetail
    from ._1298 import Stator
    from ._1299 import StatorCutOutSpecification
    from ._1300 import StatorRotorMaterial
    from ._1301 import StatorRotorMaterialDatabase
    from ._1302 import SurfacePermanentMagnetMachine
    from ._1303 import SurfacePermanentMagnetRotor
    from ._1304 import SynchronousReluctanceMachine
    from ._1305 import ToothAndSlot
    from ._1306 import ToothSlotStyle
    from ._1307 import ToothTaperSpecification
    from ._1308 import TwoDimensionalFEModelForAnalysis
    from ._1309 import UShapedLayerSpecification
    from ._1310 import VShapedMagnetLayerSpecification
    from ._1311 import WindingConductor
    from ._1312 import WindingConnection
    from ._1313 import WindingMaterial
    from ._1314 import WindingMaterialDatabase
    from ._1315 import Windings
    from ._1316 import WindingsViewer
    from ._1317 import WindingType
    from ._1318 import WireSizeSpecificationMethod
    from ._1319 import WoundFieldSynchronousMachine
else:
    import_structure = {
        "_1243": ["AbstractStator"],
        "_1244": ["AbstractToothAndSlot"],
        "_1245": ["AirGapPartition"],
        "_1246": ["CADConductor"],
        "_1247": ["CADElectricMachineDetail"],
        "_1248": ["CADMagnetsForLayer"],
        "_1249": ["CADRotor"],
        "_1250": ["CADStator"],
        "_1251": ["CADToothAndSlot"],
        "_1252": ["Coil"],
        "_1253": ["CoilPositionInSlot"],
        "_1254": ["CoolingDuctLayerSpecification"],
        "_1255": ["CoolingDuctShape"],
        "_1256": ["CoreLossBuildFactorSpecificationMethod"],
        "_1257": ["CoreLossCoefficients"],
        "_1258": ["DoubleLayerWindingSlotPositions"],
        "_1259": ["DQAxisConvention"],
        "_1260": ["Eccentricity"],
        "_1261": ["ElectricMachineDetail"],
        "_1262": ["ElectricMachineDetailInitialInformation"],
        "_1263": ["ElectricMachineMechanicalAnalysisMeshingOptions"],
        "_1264": ["ElectricMachineMeshingOptions"],
        "_1265": ["ElectricMachineMeshingOptionsBase"],
        "_1266": ["ElectricMachineSetup"],
        "_1267": ["ElectricMachineType"],
        "_1268": ["FillFactorSpecificationMethod"],
        "_1269": ["FluxBarrierOrWeb"],
        "_1270": ["FluxBarrierStyle"],
        "_1271": ["HairpinConductor"],
        "_1272": ["HarmonicLoadDataControlExcitationOptionForElectricMachineMode"],
        "_1273": ["IndividualConductorSpecificationSource"],
        "_1274": ["InteriorPermanentMagnetAndSynchronousReluctanceRotor"],
        "_1275": ["InteriorPermanentMagnetMachine"],
        "_1276": ["IronLossCoefficientSpecificationMethod"],
        "_1277": ["MagnetClearance"],
        "_1278": ["MagnetConfiguration"],
        "_1279": ["MagnetData"],
        "_1280": ["MagnetDesign"],
        "_1281": ["MagnetForLayer"],
        "_1282": ["MagnetMaterial"],
        "_1283": ["MagnetMaterialDatabase"],
        "_1284": ["MotorRotorSideFaceDetail"],
        "_1285": ["NonCADElectricMachineDetail"],
        "_1286": ["NotchShape"],
        "_1287": ["NotchSpecification"],
        "_1288": ["PermanentMagnetAssistedSynchronousReluctanceMachine"],
        "_1289": ["PermanentMagnetRotor"],
        "_1290": ["Phase"],
        "_1291": ["RegionID"],
        "_1292": ["Rotor"],
        "_1293": ["RotorInternalLayerSpecification"],
        "_1294": ["RotorSkewSlice"],
        "_1295": ["RotorType"],
        "_1296": ["SingleOrDoubleLayerWindings"],
        "_1297": ["SlotSectionDetail"],
        "_1298": ["Stator"],
        "_1299": ["StatorCutOutSpecification"],
        "_1300": ["StatorRotorMaterial"],
        "_1301": ["StatorRotorMaterialDatabase"],
        "_1302": ["SurfacePermanentMagnetMachine"],
        "_1303": ["SurfacePermanentMagnetRotor"],
        "_1304": ["SynchronousReluctanceMachine"],
        "_1305": ["ToothAndSlot"],
        "_1306": ["ToothSlotStyle"],
        "_1307": ["ToothTaperSpecification"],
        "_1308": ["TwoDimensionalFEModelForAnalysis"],
        "_1309": ["UShapedLayerSpecification"],
        "_1310": ["VShapedMagnetLayerSpecification"],
        "_1311": ["WindingConductor"],
        "_1312": ["WindingConnection"],
        "_1313": ["WindingMaterial"],
        "_1314": ["WindingMaterialDatabase"],
        "_1315": ["Windings"],
        "_1316": ["WindingsViewer"],
        "_1317": ["WindingType"],
        "_1318": ["WireSizeSpecificationMethod"],
        "_1319": ["WoundFieldSynchronousMachine"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractStator",
    "AbstractToothAndSlot",
    "AirGapPartition",
    "CADConductor",
    "CADElectricMachineDetail",
    "CADMagnetsForLayer",
    "CADRotor",
    "CADStator",
    "CADToothAndSlot",
    "Coil",
    "CoilPositionInSlot",
    "CoolingDuctLayerSpecification",
    "CoolingDuctShape",
    "CoreLossBuildFactorSpecificationMethod",
    "CoreLossCoefficients",
    "DoubleLayerWindingSlotPositions",
    "DQAxisConvention",
    "Eccentricity",
    "ElectricMachineDetail",
    "ElectricMachineDetailInitialInformation",
    "ElectricMachineMechanicalAnalysisMeshingOptions",
    "ElectricMachineMeshingOptions",
    "ElectricMachineMeshingOptionsBase",
    "ElectricMachineSetup",
    "ElectricMachineType",
    "FillFactorSpecificationMethod",
    "FluxBarrierOrWeb",
    "FluxBarrierStyle",
    "HairpinConductor",
    "HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
    "IndividualConductorSpecificationSource",
    "InteriorPermanentMagnetAndSynchronousReluctanceRotor",
    "InteriorPermanentMagnetMachine",
    "IronLossCoefficientSpecificationMethod",
    "MagnetClearance",
    "MagnetConfiguration",
    "MagnetData",
    "MagnetDesign",
    "MagnetForLayer",
    "MagnetMaterial",
    "MagnetMaterialDatabase",
    "MotorRotorSideFaceDetail",
    "NonCADElectricMachineDetail",
    "NotchShape",
    "NotchSpecification",
    "PermanentMagnetAssistedSynchronousReluctanceMachine",
    "PermanentMagnetRotor",
    "Phase",
    "RegionID",
    "Rotor",
    "RotorInternalLayerSpecification",
    "RotorSkewSlice",
    "RotorType",
    "SingleOrDoubleLayerWindings",
    "SlotSectionDetail",
    "Stator",
    "StatorCutOutSpecification",
    "StatorRotorMaterial",
    "StatorRotorMaterialDatabase",
    "SurfacePermanentMagnetMachine",
    "SurfacePermanentMagnetRotor",
    "SynchronousReluctanceMachine",
    "ToothAndSlot",
    "ToothSlotStyle",
    "ToothTaperSpecification",
    "TwoDimensionalFEModelForAnalysis",
    "UShapedLayerSpecification",
    "VShapedMagnetLayerSpecification",
    "WindingConductor",
    "WindingConnection",
    "WindingMaterial",
    "WindingMaterialDatabase",
    "Windings",
    "WindingsViewer",
    "WindingType",
    "WireSizeSpecificationMethod",
    "WoundFieldSynchronousMachine",
)

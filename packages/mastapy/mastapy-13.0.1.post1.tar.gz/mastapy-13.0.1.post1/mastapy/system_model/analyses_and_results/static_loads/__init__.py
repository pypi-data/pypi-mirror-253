"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6804 import LoadCase
    from ._6805 import StaticLoadCase
    from ._6806 import TimeSeriesLoadCase
    from ._6807 import AbstractAssemblyLoadCase
    from ._6808 import AbstractShaftLoadCase
    from ._6809 import AbstractShaftOrHousingLoadCase
    from ._6810 import AbstractShaftToMountableComponentConnectionLoadCase
    from ._6811 import AdditionalAccelerationOptions
    from ._6812 import AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
    from ._6813 import AdvancedTimeSteppingAnalysisForModulationType
    from ._6814 import AGMAGleasonConicalGearLoadCase
    from ._6815 import AGMAGleasonConicalGearMeshLoadCase
    from ._6816 import AGMAGleasonConicalGearSetLoadCase
    from ._6817 import AllRingPinsManufacturingError
    from ._6818 import AnalysisType
    from ._6819 import AssemblyLoadCase
    from ._6820 import BearingLoadCase
    from ._6821 import BeltConnectionLoadCase
    from ._6822 import BeltDriveLoadCase
    from ._6823 import BevelDifferentialGearLoadCase
    from ._6824 import BevelDifferentialGearMeshLoadCase
    from ._6825 import BevelDifferentialGearSetLoadCase
    from ._6826 import BevelDifferentialPlanetGearLoadCase
    from ._6827 import BevelDifferentialSunGearLoadCase
    from ._6828 import BevelGearLoadCase
    from ._6829 import BevelGearMeshLoadCase
    from ._6830 import BevelGearSetLoadCase
    from ._6831 import BoltedJointLoadCase
    from ._6832 import BoltLoadCase
    from ._6833 import ClutchConnectionLoadCase
    from ._6834 import ClutchHalfLoadCase
    from ._6835 import ClutchLoadCase
    from ._6836 import CMSElementFaceGroupWithSelectionOption
    from ._6837 import CoaxialConnectionLoadCase
    from ._6838 import ComponentLoadCase
    from ._6839 import ConceptCouplingConnectionLoadCase
    from ._6840 import ConceptCouplingHalfLoadCase
    from ._6841 import ConceptCouplingLoadCase
    from ._6842 import ConceptGearLoadCase
    from ._6843 import ConceptGearMeshLoadCase
    from ._6844 import ConceptGearSetLoadCase
    from ._6845 import ConicalGearLoadCase
    from ._6846 import ConicalGearManufactureError
    from ._6847 import ConicalGearMeshLoadCase
    from ._6848 import ConicalGearSetHarmonicLoadData
    from ._6849 import ConicalGearSetLoadCase
    from ._6850 import ConnectionLoadCase
    from ._6851 import ConnectorLoadCase
    from ._6852 import CouplingConnectionLoadCase
    from ._6853 import CouplingHalfLoadCase
    from ._6854 import CouplingLoadCase
    from ._6855 import CVTBeltConnectionLoadCase
    from ._6856 import CVTLoadCase
    from ._6857 import CVTPulleyLoadCase
    from ._6858 import CycloidalAssemblyLoadCase
    from ._6859 import CycloidalDiscCentralBearingConnectionLoadCase
    from ._6860 import CycloidalDiscLoadCase
    from ._6861 import CycloidalDiscPlanetaryBearingConnectionLoadCase
    from ._6862 import CylindricalGearLoadCase
    from ._6863 import CylindricalGearManufactureError
    from ._6864 import CylindricalGearMeshLoadCase
    from ._6865 import CylindricalGearSetHarmonicLoadData
    from ._6866 import CylindricalGearSetLoadCase
    from ._6867 import CylindricalPlanetGearLoadCase
    from ._6868 import DataFromMotorPackagePerMeanTorque
    from ._6869 import DataFromMotorPackagePerSpeed
    from ._6870 import DatumLoadCase
    from ._6871 import ElectricMachineDataImportType
    from ._6872 import ElectricMachineHarmonicLoadData
    from ._6873 import ElectricMachineHarmonicLoadDataFromExcel
    from ._6874 import ElectricMachineHarmonicLoadDataFromFlux
    from ._6875 import ElectricMachineHarmonicLoadDataFromJMAG
    from ._6876 import ElectricMachineHarmonicLoadDataFromMASTA
    from ._6877 import ElectricMachineHarmonicLoadDataFromMotorCAD
    from ._6878 import ElectricMachineHarmonicLoadDataFromMotorPackages
    from ._6879 import ElectricMachineHarmonicLoadExcelImportOptions
    from ._6880 import ElectricMachineHarmonicLoadFluxImportOptions
    from ._6881 import ElectricMachineHarmonicLoadImportOptionsBase
    from ._6882 import ElectricMachineHarmonicLoadJMAGImportOptions
    from ._6883 import ElectricMachineHarmonicLoadMotorCADImportOptions
    from ._6884 import ExternalCADModelLoadCase
    from ._6885 import FaceGearLoadCase
    from ._6886 import FaceGearMeshLoadCase
    from ._6887 import FaceGearSetLoadCase
    from ._6888 import FEPartLoadCase
    from ._6889 import FlexiblePinAssemblyLoadCase
    from ._6890 import ForceAndTorqueScalingFactor
    from ._6891 import GearLoadCase
    from ._6892 import GearManufactureError
    from ._6893 import GearMeshLoadCase
    from ._6894 import GearMeshTEOrderType
    from ._6895 import GearSetHarmonicLoadData
    from ._6896 import GearSetLoadCase
    from ._6897 import GuideDxfModelLoadCase
    from ._6898 import HarmonicExcitationType
    from ._6899 import HarmonicLoadDataCSVImport
    from ._6900 import HarmonicLoadDataExcelImport
    from ._6901 import HarmonicLoadDataFluxImport
    from ._6902 import HarmonicLoadDataImportBase
    from ._6903 import HarmonicLoadDataImportFromMotorPackages
    from ._6904 import HarmonicLoadDataJMAGImport
    from ._6905 import HarmonicLoadDataMotorCADImport
    from ._6906 import HypoidGearLoadCase
    from ._6907 import HypoidGearMeshLoadCase
    from ._6908 import HypoidGearSetLoadCase
    from ._6909 import ImportType
    from ._6910 import InformationAtRingPinToDiscContactPointFromGeometry
    from ._6911 import InnerDiameterReference
    from ._6912 import InterMountableComponentConnectionLoadCase
    from ._6913 import KlingelnbergCycloPalloidConicalGearLoadCase
    from ._6914 import KlingelnbergCycloPalloidConicalGearMeshLoadCase
    from ._6915 import KlingelnbergCycloPalloidConicalGearSetLoadCase
    from ._6916 import KlingelnbergCycloPalloidHypoidGearLoadCase
    from ._6917 import KlingelnbergCycloPalloidHypoidGearMeshLoadCase
    from ._6918 import KlingelnbergCycloPalloidHypoidGearSetLoadCase
    from ._6919 import KlingelnbergCycloPalloidSpiralBevelGearLoadCase
    from ._6920 import KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
    from ._6921 import KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
    from ._6922 import MassDiscLoadCase
    from ._6923 import MeasurementComponentLoadCase
    from ._6924 import MeshStiffnessSource
    from ._6925 import MountableComponentLoadCase
    from ._6926 import NamedSpeed
    from ._6927 import OilSealLoadCase
    from ._6928 import ParametricStudyType
    from ._6929 import PartLoadCase
    from ._6930 import PartToPartShearCouplingConnectionLoadCase
    from ._6931 import PartToPartShearCouplingHalfLoadCase
    from ._6932 import PartToPartShearCouplingLoadCase
    from ._6933 import PlanetaryConnectionLoadCase
    from ._6934 import PlanetaryGearSetLoadCase
    from ._6935 import PlanetarySocketManufactureError
    from ._6936 import PlanetCarrierLoadCase
    from ._6937 import PlanetManufactureError
    from ._6938 import PointLoadHarmonicLoadData
    from ._6939 import PointLoadLoadCase
    from ._6940 import PowerLoadLoadCase
    from ._6941 import PulleyLoadCase
    from ._6942 import ResetMicroGeometryOptions
    from ._6943 import RingPinManufacturingError
    from ._6944 import RingPinsLoadCase
    from ._6945 import RingPinsToDiscConnectionLoadCase
    from ._6946 import RollingRingAssemblyLoadCase
    from ._6947 import RollingRingConnectionLoadCase
    from ._6948 import RollingRingLoadCase
    from ._6949 import RootAssemblyLoadCase
    from ._6950 import ShaftHubConnectionLoadCase
    from ._6951 import ShaftLoadCase
    from ._6952 import ShaftToMountableComponentConnectionLoadCase
    from ._6953 import SpecialisedAssemblyLoadCase
    from ._6954 import SpiralBevelGearLoadCase
    from ._6955 import SpiralBevelGearMeshLoadCase
    from ._6956 import SpiralBevelGearSetLoadCase
    from ._6957 import SpringDamperConnectionLoadCase
    from ._6958 import SpringDamperHalfLoadCase
    from ._6959 import SpringDamperLoadCase
    from ._6960 import StraightBevelDiffGearLoadCase
    from ._6961 import StraightBevelDiffGearMeshLoadCase
    from ._6962 import StraightBevelDiffGearSetLoadCase
    from ._6963 import StraightBevelGearLoadCase
    from ._6964 import StraightBevelGearMeshLoadCase
    from ._6965 import StraightBevelGearSetLoadCase
    from ._6966 import StraightBevelPlanetGearLoadCase
    from ._6967 import StraightBevelSunGearLoadCase
    from ._6968 import SynchroniserHalfLoadCase
    from ._6969 import SynchroniserLoadCase
    from ._6970 import SynchroniserPartLoadCase
    from ._6971 import SynchroniserSleeveLoadCase
    from ._6972 import TEExcitationType
    from ._6973 import TorqueConverterConnectionLoadCase
    from ._6974 import TorqueConverterLoadCase
    from ._6975 import TorqueConverterPumpLoadCase
    from ._6976 import TorqueConverterTurbineLoadCase
    from ._6977 import TorqueRippleInputType
    from ._6978 import TorqueSpecificationForSystemDeflection
    from ._6979 import TransmissionEfficiencySettings
    from ._6980 import UnbalancedMassHarmonicLoadData
    from ._6981 import UnbalancedMassLoadCase
    from ._6982 import VirtualComponentLoadCase
    from ._6983 import WormGearLoadCase
    from ._6984 import WormGearMeshLoadCase
    from ._6985 import WormGearSetLoadCase
    from ._6986 import ZerolBevelGearLoadCase
    from ._6987 import ZerolBevelGearMeshLoadCase
    from ._6988 import ZerolBevelGearSetLoadCase
else:
    import_structure = {
        "_6804": ["LoadCase"],
        "_6805": ["StaticLoadCase"],
        "_6806": ["TimeSeriesLoadCase"],
        "_6807": ["AbstractAssemblyLoadCase"],
        "_6808": ["AbstractShaftLoadCase"],
        "_6809": ["AbstractShaftOrHousingLoadCase"],
        "_6810": ["AbstractShaftToMountableComponentConnectionLoadCase"],
        "_6811": ["AdditionalAccelerationOptions"],
        "_6812": ["AdvancedTimeSteppingAnalysisForModulationStaticLoadCase"],
        "_6813": ["AdvancedTimeSteppingAnalysisForModulationType"],
        "_6814": ["AGMAGleasonConicalGearLoadCase"],
        "_6815": ["AGMAGleasonConicalGearMeshLoadCase"],
        "_6816": ["AGMAGleasonConicalGearSetLoadCase"],
        "_6817": ["AllRingPinsManufacturingError"],
        "_6818": ["AnalysisType"],
        "_6819": ["AssemblyLoadCase"],
        "_6820": ["BearingLoadCase"],
        "_6821": ["BeltConnectionLoadCase"],
        "_6822": ["BeltDriveLoadCase"],
        "_6823": ["BevelDifferentialGearLoadCase"],
        "_6824": ["BevelDifferentialGearMeshLoadCase"],
        "_6825": ["BevelDifferentialGearSetLoadCase"],
        "_6826": ["BevelDifferentialPlanetGearLoadCase"],
        "_6827": ["BevelDifferentialSunGearLoadCase"],
        "_6828": ["BevelGearLoadCase"],
        "_6829": ["BevelGearMeshLoadCase"],
        "_6830": ["BevelGearSetLoadCase"],
        "_6831": ["BoltedJointLoadCase"],
        "_6832": ["BoltLoadCase"],
        "_6833": ["ClutchConnectionLoadCase"],
        "_6834": ["ClutchHalfLoadCase"],
        "_6835": ["ClutchLoadCase"],
        "_6836": ["CMSElementFaceGroupWithSelectionOption"],
        "_6837": ["CoaxialConnectionLoadCase"],
        "_6838": ["ComponentLoadCase"],
        "_6839": ["ConceptCouplingConnectionLoadCase"],
        "_6840": ["ConceptCouplingHalfLoadCase"],
        "_6841": ["ConceptCouplingLoadCase"],
        "_6842": ["ConceptGearLoadCase"],
        "_6843": ["ConceptGearMeshLoadCase"],
        "_6844": ["ConceptGearSetLoadCase"],
        "_6845": ["ConicalGearLoadCase"],
        "_6846": ["ConicalGearManufactureError"],
        "_6847": ["ConicalGearMeshLoadCase"],
        "_6848": ["ConicalGearSetHarmonicLoadData"],
        "_6849": ["ConicalGearSetLoadCase"],
        "_6850": ["ConnectionLoadCase"],
        "_6851": ["ConnectorLoadCase"],
        "_6852": ["CouplingConnectionLoadCase"],
        "_6853": ["CouplingHalfLoadCase"],
        "_6854": ["CouplingLoadCase"],
        "_6855": ["CVTBeltConnectionLoadCase"],
        "_6856": ["CVTLoadCase"],
        "_6857": ["CVTPulleyLoadCase"],
        "_6858": ["CycloidalAssemblyLoadCase"],
        "_6859": ["CycloidalDiscCentralBearingConnectionLoadCase"],
        "_6860": ["CycloidalDiscLoadCase"],
        "_6861": ["CycloidalDiscPlanetaryBearingConnectionLoadCase"],
        "_6862": ["CylindricalGearLoadCase"],
        "_6863": ["CylindricalGearManufactureError"],
        "_6864": ["CylindricalGearMeshLoadCase"],
        "_6865": ["CylindricalGearSetHarmonicLoadData"],
        "_6866": ["CylindricalGearSetLoadCase"],
        "_6867": ["CylindricalPlanetGearLoadCase"],
        "_6868": ["DataFromMotorPackagePerMeanTorque"],
        "_6869": ["DataFromMotorPackagePerSpeed"],
        "_6870": ["DatumLoadCase"],
        "_6871": ["ElectricMachineDataImportType"],
        "_6872": ["ElectricMachineHarmonicLoadData"],
        "_6873": ["ElectricMachineHarmonicLoadDataFromExcel"],
        "_6874": ["ElectricMachineHarmonicLoadDataFromFlux"],
        "_6875": ["ElectricMachineHarmonicLoadDataFromJMAG"],
        "_6876": ["ElectricMachineHarmonicLoadDataFromMASTA"],
        "_6877": ["ElectricMachineHarmonicLoadDataFromMotorCAD"],
        "_6878": ["ElectricMachineHarmonicLoadDataFromMotorPackages"],
        "_6879": ["ElectricMachineHarmonicLoadExcelImportOptions"],
        "_6880": ["ElectricMachineHarmonicLoadFluxImportOptions"],
        "_6881": ["ElectricMachineHarmonicLoadImportOptionsBase"],
        "_6882": ["ElectricMachineHarmonicLoadJMAGImportOptions"],
        "_6883": ["ElectricMachineHarmonicLoadMotorCADImportOptions"],
        "_6884": ["ExternalCADModelLoadCase"],
        "_6885": ["FaceGearLoadCase"],
        "_6886": ["FaceGearMeshLoadCase"],
        "_6887": ["FaceGearSetLoadCase"],
        "_6888": ["FEPartLoadCase"],
        "_6889": ["FlexiblePinAssemblyLoadCase"],
        "_6890": ["ForceAndTorqueScalingFactor"],
        "_6891": ["GearLoadCase"],
        "_6892": ["GearManufactureError"],
        "_6893": ["GearMeshLoadCase"],
        "_6894": ["GearMeshTEOrderType"],
        "_6895": ["GearSetHarmonicLoadData"],
        "_6896": ["GearSetLoadCase"],
        "_6897": ["GuideDxfModelLoadCase"],
        "_6898": ["HarmonicExcitationType"],
        "_6899": ["HarmonicLoadDataCSVImport"],
        "_6900": ["HarmonicLoadDataExcelImport"],
        "_6901": ["HarmonicLoadDataFluxImport"],
        "_6902": ["HarmonicLoadDataImportBase"],
        "_6903": ["HarmonicLoadDataImportFromMotorPackages"],
        "_6904": ["HarmonicLoadDataJMAGImport"],
        "_6905": ["HarmonicLoadDataMotorCADImport"],
        "_6906": ["HypoidGearLoadCase"],
        "_6907": ["HypoidGearMeshLoadCase"],
        "_6908": ["HypoidGearSetLoadCase"],
        "_6909": ["ImportType"],
        "_6910": ["InformationAtRingPinToDiscContactPointFromGeometry"],
        "_6911": ["InnerDiameterReference"],
        "_6912": ["InterMountableComponentConnectionLoadCase"],
        "_6913": ["KlingelnbergCycloPalloidConicalGearLoadCase"],
        "_6914": ["KlingelnbergCycloPalloidConicalGearMeshLoadCase"],
        "_6915": ["KlingelnbergCycloPalloidConicalGearSetLoadCase"],
        "_6916": ["KlingelnbergCycloPalloidHypoidGearLoadCase"],
        "_6917": ["KlingelnbergCycloPalloidHypoidGearMeshLoadCase"],
        "_6918": ["KlingelnbergCycloPalloidHypoidGearSetLoadCase"],
        "_6919": ["KlingelnbergCycloPalloidSpiralBevelGearLoadCase"],
        "_6920": ["KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase"],
        "_6921": ["KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"],
        "_6922": ["MassDiscLoadCase"],
        "_6923": ["MeasurementComponentLoadCase"],
        "_6924": ["MeshStiffnessSource"],
        "_6925": ["MountableComponentLoadCase"],
        "_6926": ["NamedSpeed"],
        "_6927": ["OilSealLoadCase"],
        "_6928": ["ParametricStudyType"],
        "_6929": ["PartLoadCase"],
        "_6930": ["PartToPartShearCouplingConnectionLoadCase"],
        "_6931": ["PartToPartShearCouplingHalfLoadCase"],
        "_6932": ["PartToPartShearCouplingLoadCase"],
        "_6933": ["PlanetaryConnectionLoadCase"],
        "_6934": ["PlanetaryGearSetLoadCase"],
        "_6935": ["PlanetarySocketManufactureError"],
        "_6936": ["PlanetCarrierLoadCase"],
        "_6937": ["PlanetManufactureError"],
        "_6938": ["PointLoadHarmonicLoadData"],
        "_6939": ["PointLoadLoadCase"],
        "_6940": ["PowerLoadLoadCase"],
        "_6941": ["PulleyLoadCase"],
        "_6942": ["ResetMicroGeometryOptions"],
        "_6943": ["RingPinManufacturingError"],
        "_6944": ["RingPinsLoadCase"],
        "_6945": ["RingPinsToDiscConnectionLoadCase"],
        "_6946": ["RollingRingAssemblyLoadCase"],
        "_6947": ["RollingRingConnectionLoadCase"],
        "_6948": ["RollingRingLoadCase"],
        "_6949": ["RootAssemblyLoadCase"],
        "_6950": ["ShaftHubConnectionLoadCase"],
        "_6951": ["ShaftLoadCase"],
        "_6952": ["ShaftToMountableComponentConnectionLoadCase"],
        "_6953": ["SpecialisedAssemblyLoadCase"],
        "_6954": ["SpiralBevelGearLoadCase"],
        "_6955": ["SpiralBevelGearMeshLoadCase"],
        "_6956": ["SpiralBevelGearSetLoadCase"],
        "_6957": ["SpringDamperConnectionLoadCase"],
        "_6958": ["SpringDamperHalfLoadCase"],
        "_6959": ["SpringDamperLoadCase"],
        "_6960": ["StraightBevelDiffGearLoadCase"],
        "_6961": ["StraightBevelDiffGearMeshLoadCase"],
        "_6962": ["StraightBevelDiffGearSetLoadCase"],
        "_6963": ["StraightBevelGearLoadCase"],
        "_6964": ["StraightBevelGearMeshLoadCase"],
        "_6965": ["StraightBevelGearSetLoadCase"],
        "_6966": ["StraightBevelPlanetGearLoadCase"],
        "_6967": ["StraightBevelSunGearLoadCase"],
        "_6968": ["SynchroniserHalfLoadCase"],
        "_6969": ["SynchroniserLoadCase"],
        "_6970": ["SynchroniserPartLoadCase"],
        "_6971": ["SynchroniserSleeveLoadCase"],
        "_6972": ["TEExcitationType"],
        "_6973": ["TorqueConverterConnectionLoadCase"],
        "_6974": ["TorqueConverterLoadCase"],
        "_6975": ["TorqueConverterPumpLoadCase"],
        "_6976": ["TorqueConverterTurbineLoadCase"],
        "_6977": ["TorqueRippleInputType"],
        "_6978": ["TorqueSpecificationForSystemDeflection"],
        "_6979": ["TransmissionEfficiencySettings"],
        "_6980": ["UnbalancedMassHarmonicLoadData"],
        "_6981": ["UnbalancedMassLoadCase"],
        "_6982": ["VirtualComponentLoadCase"],
        "_6983": ["WormGearLoadCase"],
        "_6984": ["WormGearMeshLoadCase"],
        "_6985": ["WormGearSetLoadCase"],
        "_6986": ["ZerolBevelGearLoadCase"],
        "_6987": ["ZerolBevelGearMeshLoadCase"],
        "_6988": ["ZerolBevelGearSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LoadCase",
    "StaticLoadCase",
    "TimeSeriesLoadCase",
    "AbstractAssemblyLoadCase",
    "AbstractShaftLoadCase",
    "AbstractShaftOrHousingLoadCase",
    "AbstractShaftToMountableComponentConnectionLoadCase",
    "AdditionalAccelerationOptions",
    "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
    "AdvancedTimeSteppingAnalysisForModulationType",
    "AGMAGleasonConicalGearLoadCase",
    "AGMAGleasonConicalGearMeshLoadCase",
    "AGMAGleasonConicalGearSetLoadCase",
    "AllRingPinsManufacturingError",
    "AnalysisType",
    "AssemblyLoadCase",
    "BearingLoadCase",
    "BeltConnectionLoadCase",
    "BeltDriveLoadCase",
    "BevelDifferentialGearLoadCase",
    "BevelDifferentialGearMeshLoadCase",
    "BevelDifferentialGearSetLoadCase",
    "BevelDifferentialPlanetGearLoadCase",
    "BevelDifferentialSunGearLoadCase",
    "BevelGearLoadCase",
    "BevelGearMeshLoadCase",
    "BevelGearSetLoadCase",
    "BoltedJointLoadCase",
    "BoltLoadCase",
    "ClutchConnectionLoadCase",
    "ClutchHalfLoadCase",
    "ClutchLoadCase",
    "CMSElementFaceGroupWithSelectionOption",
    "CoaxialConnectionLoadCase",
    "ComponentLoadCase",
    "ConceptCouplingConnectionLoadCase",
    "ConceptCouplingHalfLoadCase",
    "ConceptCouplingLoadCase",
    "ConceptGearLoadCase",
    "ConceptGearMeshLoadCase",
    "ConceptGearSetLoadCase",
    "ConicalGearLoadCase",
    "ConicalGearManufactureError",
    "ConicalGearMeshLoadCase",
    "ConicalGearSetHarmonicLoadData",
    "ConicalGearSetLoadCase",
    "ConnectionLoadCase",
    "ConnectorLoadCase",
    "CouplingConnectionLoadCase",
    "CouplingHalfLoadCase",
    "CouplingLoadCase",
    "CVTBeltConnectionLoadCase",
    "CVTLoadCase",
    "CVTPulleyLoadCase",
    "CycloidalAssemblyLoadCase",
    "CycloidalDiscCentralBearingConnectionLoadCase",
    "CycloidalDiscLoadCase",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
    "CylindricalGearLoadCase",
    "CylindricalGearManufactureError",
    "CylindricalGearMeshLoadCase",
    "CylindricalGearSetHarmonicLoadData",
    "CylindricalGearSetLoadCase",
    "CylindricalPlanetGearLoadCase",
    "DataFromMotorPackagePerMeanTorque",
    "DataFromMotorPackagePerSpeed",
    "DatumLoadCase",
    "ElectricMachineDataImportType",
    "ElectricMachineHarmonicLoadData",
    "ElectricMachineHarmonicLoadDataFromExcel",
    "ElectricMachineHarmonicLoadDataFromFlux",
    "ElectricMachineHarmonicLoadDataFromJMAG",
    "ElectricMachineHarmonicLoadDataFromMASTA",
    "ElectricMachineHarmonicLoadDataFromMotorCAD",
    "ElectricMachineHarmonicLoadDataFromMotorPackages",
    "ElectricMachineHarmonicLoadExcelImportOptions",
    "ElectricMachineHarmonicLoadFluxImportOptions",
    "ElectricMachineHarmonicLoadImportOptionsBase",
    "ElectricMachineHarmonicLoadJMAGImportOptions",
    "ElectricMachineHarmonicLoadMotorCADImportOptions",
    "ExternalCADModelLoadCase",
    "FaceGearLoadCase",
    "FaceGearMeshLoadCase",
    "FaceGearSetLoadCase",
    "FEPartLoadCase",
    "FlexiblePinAssemblyLoadCase",
    "ForceAndTorqueScalingFactor",
    "GearLoadCase",
    "GearManufactureError",
    "GearMeshLoadCase",
    "GearMeshTEOrderType",
    "GearSetHarmonicLoadData",
    "GearSetLoadCase",
    "GuideDxfModelLoadCase",
    "HarmonicExcitationType",
    "HarmonicLoadDataCSVImport",
    "HarmonicLoadDataExcelImport",
    "HarmonicLoadDataFluxImport",
    "HarmonicLoadDataImportBase",
    "HarmonicLoadDataImportFromMotorPackages",
    "HarmonicLoadDataJMAGImport",
    "HarmonicLoadDataMotorCADImport",
    "HypoidGearLoadCase",
    "HypoidGearMeshLoadCase",
    "HypoidGearSetLoadCase",
    "ImportType",
    "InformationAtRingPinToDiscContactPointFromGeometry",
    "InnerDiameterReference",
    "InterMountableComponentConnectionLoadCase",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    "MassDiscLoadCase",
    "MeasurementComponentLoadCase",
    "MeshStiffnessSource",
    "MountableComponentLoadCase",
    "NamedSpeed",
    "OilSealLoadCase",
    "ParametricStudyType",
    "PartLoadCase",
    "PartToPartShearCouplingConnectionLoadCase",
    "PartToPartShearCouplingHalfLoadCase",
    "PartToPartShearCouplingLoadCase",
    "PlanetaryConnectionLoadCase",
    "PlanetaryGearSetLoadCase",
    "PlanetarySocketManufactureError",
    "PlanetCarrierLoadCase",
    "PlanetManufactureError",
    "PointLoadHarmonicLoadData",
    "PointLoadLoadCase",
    "PowerLoadLoadCase",
    "PulleyLoadCase",
    "ResetMicroGeometryOptions",
    "RingPinManufacturingError",
    "RingPinsLoadCase",
    "RingPinsToDiscConnectionLoadCase",
    "RollingRingAssemblyLoadCase",
    "RollingRingConnectionLoadCase",
    "RollingRingLoadCase",
    "RootAssemblyLoadCase",
    "ShaftHubConnectionLoadCase",
    "ShaftLoadCase",
    "ShaftToMountableComponentConnectionLoadCase",
    "SpecialisedAssemblyLoadCase",
    "SpiralBevelGearLoadCase",
    "SpiralBevelGearMeshLoadCase",
    "SpiralBevelGearSetLoadCase",
    "SpringDamperConnectionLoadCase",
    "SpringDamperHalfLoadCase",
    "SpringDamperLoadCase",
    "StraightBevelDiffGearLoadCase",
    "StraightBevelDiffGearMeshLoadCase",
    "StraightBevelDiffGearSetLoadCase",
    "StraightBevelGearLoadCase",
    "StraightBevelGearMeshLoadCase",
    "StraightBevelGearSetLoadCase",
    "StraightBevelPlanetGearLoadCase",
    "StraightBevelSunGearLoadCase",
    "SynchroniserHalfLoadCase",
    "SynchroniserLoadCase",
    "SynchroniserPartLoadCase",
    "SynchroniserSleeveLoadCase",
    "TEExcitationType",
    "TorqueConverterConnectionLoadCase",
    "TorqueConverterLoadCase",
    "TorqueConverterPumpLoadCase",
    "TorqueConverterTurbineLoadCase",
    "TorqueRippleInputType",
    "TorqueSpecificationForSystemDeflection",
    "TransmissionEfficiencySettings",
    "UnbalancedMassHarmonicLoadData",
    "UnbalancedMassLoadCase",
    "VirtualComponentLoadCase",
    "WormGearLoadCase",
    "WormGearMeshLoadCase",
    "WormGearSetLoadCase",
    "ZerolBevelGearLoadCase",
    "ZerolBevelGearMeshLoadCase",
    "ZerolBevelGearSetLoadCase",
)

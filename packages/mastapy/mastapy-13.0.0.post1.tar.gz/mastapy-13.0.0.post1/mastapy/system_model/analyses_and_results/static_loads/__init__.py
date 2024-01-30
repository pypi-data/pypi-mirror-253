"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6803 import LoadCase
    from ._6804 import StaticLoadCase
    from ._6805 import TimeSeriesLoadCase
    from ._6806 import AbstractAssemblyLoadCase
    from ._6807 import AbstractShaftLoadCase
    from ._6808 import AbstractShaftOrHousingLoadCase
    from ._6809 import AbstractShaftToMountableComponentConnectionLoadCase
    from ._6810 import AdditionalAccelerationOptions
    from ._6811 import AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
    from ._6812 import AdvancedTimeSteppingAnalysisForModulationType
    from ._6813 import AGMAGleasonConicalGearLoadCase
    from ._6814 import AGMAGleasonConicalGearMeshLoadCase
    from ._6815 import AGMAGleasonConicalGearSetLoadCase
    from ._6816 import AllRingPinsManufacturingError
    from ._6817 import AnalysisType
    from ._6818 import AssemblyLoadCase
    from ._6819 import BearingLoadCase
    from ._6820 import BeltConnectionLoadCase
    from ._6821 import BeltDriveLoadCase
    from ._6822 import BevelDifferentialGearLoadCase
    from ._6823 import BevelDifferentialGearMeshLoadCase
    from ._6824 import BevelDifferentialGearSetLoadCase
    from ._6825 import BevelDifferentialPlanetGearLoadCase
    from ._6826 import BevelDifferentialSunGearLoadCase
    from ._6827 import BevelGearLoadCase
    from ._6828 import BevelGearMeshLoadCase
    from ._6829 import BevelGearSetLoadCase
    from ._6830 import BoltedJointLoadCase
    from ._6831 import BoltLoadCase
    from ._6832 import ClutchConnectionLoadCase
    from ._6833 import ClutchHalfLoadCase
    from ._6834 import ClutchLoadCase
    from ._6835 import CMSElementFaceGroupWithSelectionOption
    from ._6836 import CoaxialConnectionLoadCase
    from ._6837 import ComponentLoadCase
    from ._6838 import ConceptCouplingConnectionLoadCase
    from ._6839 import ConceptCouplingHalfLoadCase
    from ._6840 import ConceptCouplingLoadCase
    from ._6841 import ConceptGearLoadCase
    from ._6842 import ConceptGearMeshLoadCase
    from ._6843 import ConceptGearSetLoadCase
    from ._6844 import ConicalGearLoadCase
    from ._6845 import ConicalGearManufactureError
    from ._6846 import ConicalGearMeshLoadCase
    from ._6847 import ConicalGearSetHarmonicLoadData
    from ._6848 import ConicalGearSetLoadCase
    from ._6849 import ConnectionLoadCase
    from ._6850 import ConnectorLoadCase
    from ._6851 import CouplingConnectionLoadCase
    from ._6852 import CouplingHalfLoadCase
    from ._6853 import CouplingLoadCase
    from ._6854 import CVTBeltConnectionLoadCase
    from ._6855 import CVTLoadCase
    from ._6856 import CVTPulleyLoadCase
    from ._6857 import CycloidalAssemblyLoadCase
    from ._6858 import CycloidalDiscCentralBearingConnectionLoadCase
    from ._6859 import CycloidalDiscLoadCase
    from ._6860 import CycloidalDiscPlanetaryBearingConnectionLoadCase
    from ._6861 import CylindricalGearLoadCase
    from ._6862 import CylindricalGearManufactureError
    from ._6863 import CylindricalGearMeshLoadCase
    from ._6864 import CylindricalGearSetHarmonicLoadData
    from ._6865 import CylindricalGearSetLoadCase
    from ._6866 import CylindricalPlanetGearLoadCase
    from ._6867 import DataFromMotorPackagePerMeanTorque
    from ._6868 import DataFromMotorPackagePerSpeed
    from ._6869 import DatumLoadCase
    from ._6870 import ElectricMachineDataImportType
    from ._6871 import ElectricMachineHarmonicLoadData
    from ._6872 import ElectricMachineHarmonicLoadDataFromExcel
    from ._6873 import ElectricMachineHarmonicLoadDataFromFlux
    from ._6874 import ElectricMachineHarmonicLoadDataFromJMAG
    from ._6875 import ElectricMachineHarmonicLoadDataFromMASTA
    from ._6876 import ElectricMachineHarmonicLoadDataFromMotorCAD
    from ._6877 import ElectricMachineHarmonicLoadDataFromMotorPackages
    from ._6878 import ElectricMachineHarmonicLoadExcelImportOptions
    from ._6879 import ElectricMachineHarmonicLoadFluxImportOptions
    from ._6880 import ElectricMachineHarmonicLoadImportOptionsBase
    from ._6881 import ElectricMachineHarmonicLoadJMAGImportOptions
    from ._6882 import ElectricMachineHarmonicLoadMotorCADImportOptions
    from ._6883 import ExternalCADModelLoadCase
    from ._6884 import FaceGearLoadCase
    from ._6885 import FaceGearMeshLoadCase
    from ._6886 import FaceGearSetLoadCase
    from ._6887 import FEPartLoadCase
    from ._6888 import FlexiblePinAssemblyLoadCase
    from ._6889 import ForceAndTorqueScalingFactor
    from ._6890 import GearLoadCase
    from ._6891 import GearManufactureError
    from ._6892 import GearMeshLoadCase
    from ._6893 import GearMeshTEOrderType
    from ._6894 import GearSetHarmonicLoadData
    from ._6895 import GearSetLoadCase
    from ._6896 import GuideDxfModelLoadCase
    from ._6897 import HarmonicExcitationType
    from ._6898 import HarmonicLoadDataCSVImport
    from ._6899 import HarmonicLoadDataExcelImport
    from ._6900 import HarmonicLoadDataFluxImport
    from ._6901 import HarmonicLoadDataImportBase
    from ._6902 import HarmonicLoadDataImportFromMotorPackages
    from ._6903 import HarmonicLoadDataJMAGImport
    from ._6904 import HarmonicLoadDataMotorCADImport
    from ._6905 import HypoidGearLoadCase
    from ._6906 import HypoidGearMeshLoadCase
    from ._6907 import HypoidGearSetLoadCase
    from ._6908 import ImportType
    from ._6909 import InformationAtRingPinToDiscContactPointFromGeometry
    from ._6910 import InnerDiameterReference
    from ._6911 import InterMountableComponentConnectionLoadCase
    from ._6912 import KlingelnbergCycloPalloidConicalGearLoadCase
    from ._6913 import KlingelnbergCycloPalloidConicalGearMeshLoadCase
    from ._6914 import KlingelnbergCycloPalloidConicalGearSetLoadCase
    from ._6915 import KlingelnbergCycloPalloidHypoidGearLoadCase
    from ._6916 import KlingelnbergCycloPalloidHypoidGearMeshLoadCase
    from ._6917 import KlingelnbergCycloPalloidHypoidGearSetLoadCase
    from ._6918 import KlingelnbergCycloPalloidSpiralBevelGearLoadCase
    from ._6919 import KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
    from ._6920 import KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
    from ._6921 import MassDiscLoadCase
    from ._6922 import MeasurementComponentLoadCase
    from ._6923 import MeshStiffnessSource
    from ._6924 import MountableComponentLoadCase
    from ._6925 import NamedSpeed
    from ._6926 import OilSealLoadCase
    from ._6927 import ParametricStudyType
    from ._6928 import PartLoadCase
    from ._6929 import PartToPartShearCouplingConnectionLoadCase
    from ._6930 import PartToPartShearCouplingHalfLoadCase
    from ._6931 import PartToPartShearCouplingLoadCase
    from ._6932 import PlanetaryConnectionLoadCase
    from ._6933 import PlanetaryGearSetLoadCase
    from ._6934 import PlanetarySocketManufactureError
    from ._6935 import PlanetCarrierLoadCase
    from ._6936 import PlanetManufactureError
    from ._6937 import PointLoadHarmonicLoadData
    from ._6938 import PointLoadLoadCase
    from ._6939 import PowerLoadLoadCase
    from ._6940 import PulleyLoadCase
    from ._6941 import ResetMicroGeometryOptions
    from ._6942 import RingPinManufacturingError
    from ._6943 import RingPinsLoadCase
    from ._6944 import RingPinsToDiscConnectionLoadCase
    from ._6945 import RollingRingAssemblyLoadCase
    from ._6946 import RollingRingConnectionLoadCase
    from ._6947 import RollingRingLoadCase
    from ._6948 import RootAssemblyLoadCase
    from ._6949 import ShaftHubConnectionLoadCase
    from ._6950 import ShaftLoadCase
    from ._6951 import ShaftToMountableComponentConnectionLoadCase
    from ._6952 import SpecialisedAssemblyLoadCase
    from ._6953 import SpiralBevelGearLoadCase
    from ._6954 import SpiralBevelGearMeshLoadCase
    from ._6955 import SpiralBevelGearSetLoadCase
    from ._6956 import SpringDamperConnectionLoadCase
    from ._6957 import SpringDamperHalfLoadCase
    from ._6958 import SpringDamperLoadCase
    from ._6959 import StraightBevelDiffGearLoadCase
    from ._6960 import StraightBevelDiffGearMeshLoadCase
    from ._6961 import StraightBevelDiffGearSetLoadCase
    from ._6962 import StraightBevelGearLoadCase
    from ._6963 import StraightBevelGearMeshLoadCase
    from ._6964 import StraightBevelGearSetLoadCase
    from ._6965 import StraightBevelPlanetGearLoadCase
    from ._6966 import StraightBevelSunGearLoadCase
    from ._6967 import SynchroniserHalfLoadCase
    from ._6968 import SynchroniserLoadCase
    from ._6969 import SynchroniserPartLoadCase
    from ._6970 import SynchroniserSleeveLoadCase
    from ._6971 import TEExcitationType
    from ._6972 import TorqueConverterConnectionLoadCase
    from ._6973 import TorqueConverterLoadCase
    from ._6974 import TorqueConverterPumpLoadCase
    from ._6975 import TorqueConverterTurbineLoadCase
    from ._6976 import TorqueRippleInputType
    from ._6977 import TorqueSpecificationForSystemDeflection
    from ._6978 import TransmissionEfficiencySettings
    from ._6979 import UnbalancedMassHarmonicLoadData
    from ._6980 import UnbalancedMassLoadCase
    from ._6981 import VirtualComponentLoadCase
    from ._6982 import WormGearLoadCase
    from ._6983 import WormGearMeshLoadCase
    from ._6984 import WormGearSetLoadCase
    from ._6985 import ZerolBevelGearLoadCase
    from ._6986 import ZerolBevelGearMeshLoadCase
    from ._6987 import ZerolBevelGearSetLoadCase
else:
    import_structure = {
        "_6803": ["LoadCase"],
        "_6804": ["StaticLoadCase"],
        "_6805": ["TimeSeriesLoadCase"],
        "_6806": ["AbstractAssemblyLoadCase"],
        "_6807": ["AbstractShaftLoadCase"],
        "_6808": ["AbstractShaftOrHousingLoadCase"],
        "_6809": ["AbstractShaftToMountableComponentConnectionLoadCase"],
        "_6810": ["AdditionalAccelerationOptions"],
        "_6811": ["AdvancedTimeSteppingAnalysisForModulationStaticLoadCase"],
        "_6812": ["AdvancedTimeSteppingAnalysisForModulationType"],
        "_6813": ["AGMAGleasonConicalGearLoadCase"],
        "_6814": ["AGMAGleasonConicalGearMeshLoadCase"],
        "_6815": ["AGMAGleasonConicalGearSetLoadCase"],
        "_6816": ["AllRingPinsManufacturingError"],
        "_6817": ["AnalysisType"],
        "_6818": ["AssemblyLoadCase"],
        "_6819": ["BearingLoadCase"],
        "_6820": ["BeltConnectionLoadCase"],
        "_6821": ["BeltDriveLoadCase"],
        "_6822": ["BevelDifferentialGearLoadCase"],
        "_6823": ["BevelDifferentialGearMeshLoadCase"],
        "_6824": ["BevelDifferentialGearSetLoadCase"],
        "_6825": ["BevelDifferentialPlanetGearLoadCase"],
        "_6826": ["BevelDifferentialSunGearLoadCase"],
        "_6827": ["BevelGearLoadCase"],
        "_6828": ["BevelGearMeshLoadCase"],
        "_6829": ["BevelGearSetLoadCase"],
        "_6830": ["BoltedJointLoadCase"],
        "_6831": ["BoltLoadCase"],
        "_6832": ["ClutchConnectionLoadCase"],
        "_6833": ["ClutchHalfLoadCase"],
        "_6834": ["ClutchLoadCase"],
        "_6835": ["CMSElementFaceGroupWithSelectionOption"],
        "_6836": ["CoaxialConnectionLoadCase"],
        "_6837": ["ComponentLoadCase"],
        "_6838": ["ConceptCouplingConnectionLoadCase"],
        "_6839": ["ConceptCouplingHalfLoadCase"],
        "_6840": ["ConceptCouplingLoadCase"],
        "_6841": ["ConceptGearLoadCase"],
        "_6842": ["ConceptGearMeshLoadCase"],
        "_6843": ["ConceptGearSetLoadCase"],
        "_6844": ["ConicalGearLoadCase"],
        "_6845": ["ConicalGearManufactureError"],
        "_6846": ["ConicalGearMeshLoadCase"],
        "_6847": ["ConicalGearSetHarmonicLoadData"],
        "_6848": ["ConicalGearSetLoadCase"],
        "_6849": ["ConnectionLoadCase"],
        "_6850": ["ConnectorLoadCase"],
        "_6851": ["CouplingConnectionLoadCase"],
        "_6852": ["CouplingHalfLoadCase"],
        "_6853": ["CouplingLoadCase"],
        "_6854": ["CVTBeltConnectionLoadCase"],
        "_6855": ["CVTLoadCase"],
        "_6856": ["CVTPulleyLoadCase"],
        "_6857": ["CycloidalAssemblyLoadCase"],
        "_6858": ["CycloidalDiscCentralBearingConnectionLoadCase"],
        "_6859": ["CycloidalDiscLoadCase"],
        "_6860": ["CycloidalDiscPlanetaryBearingConnectionLoadCase"],
        "_6861": ["CylindricalGearLoadCase"],
        "_6862": ["CylindricalGearManufactureError"],
        "_6863": ["CylindricalGearMeshLoadCase"],
        "_6864": ["CylindricalGearSetHarmonicLoadData"],
        "_6865": ["CylindricalGearSetLoadCase"],
        "_6866": ["CylindricalPlanetGearLoadCase"],
        "_6867": ["DataFromMotorPackagePerMeanTorque"],
        "_6868": ["DataFromMotorPackagePerSpeed"],
        "_6869": ["DatumLoadCase"],
        "_6870": ["ElectricMachineDataImportType"],
        "_6871": ["ElectricMachineHarmonicLoadData"],
        "_6872": ["ElectricMachineHarmonicLoadDataFromExcel"],
        "_6873": ["ElectricMachineHarmonicLoadDataFromFlux"],
        "_6874": ["ElectricMachineHarmonicLoadDataFromJMAG"],
        "_6875": ["ElectricMachineHarmonicLoadDataFromMASTA"],
        "_6876": ["ElectricMachineHarmonicLoadDataFromMotorCAD"],
        "_6877": ["ElectricMachineHarmonicLoadDataFromMotorPackages"],
        "_6878": ["ElectricMachineHarmonicLoadExcelImportOptions"],
        "_6879": ["ElectricMachineHarmonicLoadFluxImportOptions"],
        "_6880": ["ElectricMachineHarmonicLoadImportOptionsBase"],
        "_6881": ["ElectricMachineHarmonicLoadJMAGImportOptions"],
        "_6882": ["ElectricMachineHarmonicLoadMotorCADImportOptions"],
        "_6883": ["ExternalCADModelLoadCase"],
        "_6884": ["FaceGearLoadCase"],
        "_6885": ["FaceGearMeshLoadCase"],
        "_6886": ["FaceGearSetLoadCase"],
        "_6887": ["FEPartLoadCase"],
        "_6888": ["FlexiblePinAssemblyLoadCase"],
        "_6889": ["ForceAndTorqueScalingFactor"],
        "_6890": ["GearLoadCase"],
        "_6891": ["GearManufactureError"],
        "_6892": ["GearMeshLoadCase"],
        "_6893": ["GearMeshTEOrderType"],
        "_6894": ["GearSetHarmonicLoadData"],
        "_6895": ["GearSetLoadCase"],
        "_6896": ["GuideDxfModelLoadCase"],
        "_6897": ["HarmonicExcitationType"],
        "_6898": ["HarmonicLoadDataCSVImport"],
        "_6899": ["HarmonicLoadDataExcelImport"],
        "_6900": ["HarmonicLoadDataFluxImport"],
        "_6901": ["HarmonicLoadDataImportBase"],
        "_6902": ["HarmonicLoadDataImportFromMotorPackages"],
        "_6903": ["HarmonicLoadDataJMAGImport"],
        "_6904": ["HarmonicLoadDataMotorCADImport"],
        "_6905": ["HypoidGearLoadCase"],
        "_6906": ["HypoidGearMeshLoadCase"],
        "_6907": ["HypoidGearSetLoadCase"],
        "_6908": ["ImportType"],
        "_6909": ["InformationAtRingPinToDiscContactPointFromGeometry"],
        "_6910": ["InnerDiameterReference"],
        "_6911": ["InterMountableComponentConnectionLoadCase"],
        "_6912": ["KlingelnbergCycloPalloidConicalGearLoadCase"],
        "_6913": ["KlingelnbergCycloPalloidConicalGearMeshLoadCase"],
        "_6914": ["KlingelnbergCycloPalloidConicalGearSetLoadCase"],
        "_6915": ["KlingelnbergCycloPalloidHypoidGearLoadCase"],
        "_6916": ["KlingelnbergCycloPalloidHypoidGearMeshLoadCase"],
        "_6917": ["KlingelnbergCycloPalloidHypoidGearSetLoadCase"],
        "_6918": ["KlingelnbergCycloPalloidSpiralBevelGearLoadCase"],
        "_6919": ["KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase"],
        "_6920": ["KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"],
        "_6921": ["MassDiscLoadCase"],
        "_6922": ["MeasurementComponentLoadCase"],
        "_6923": ["MeshStiffnessSource"],
        "_6924": ["MountableComponentLoadCase"],
        "_6925": ["NamedSpeed"],
        "_6926": ["OilSealLoadCase"],
        "_6927": ["ParametricStudyType"],
        "_6928": ["PartLoadCase"],
        "_6929": ["PartToPartShearCouplingConnectionLoadCase"],
        "_6930": ["PartToPartShearCouplingHalfLoadCase"],
        "_6931": ["PartToPartShearCouplingLoadCase"],
        "_6932": ["PlanetaryConnectionLoadCase"],
        "_6933": ["PlanetaryGearSetLoadCase"],
        "_6934": ["PlanetarySocketManufactureError"],
        "_6935": ["PlanetCarrierLoadCase"],
        "_6936": ["PlanetManufactureError"],
        "_6937": ["PointLoadHarmonicLoadData"],
        "_6938": ["PointLoadLoadCase"],
        "_6939": ["PowerLoadLoadCase"],
        "_6940": ["PulleyLoadCase"],
        "_6941": ["ResetMicroGeometryOptions"],
        "_6942": ["RingPinManufacturingError"],
        "_6943": ["RingPinsLoadCase"],
        "_6944": ["RingPinsToDiscConnectionLoadCase"],
        "_6945": ["RollingRingAssemblyLoadCase"],
        "_6946": ["RollingRingConnectionLoadCase"],
        "_6947": ["RollingRingLoadCase"],
        "_6948": ["RootAssemblyLoadCase"],
        "_6949": ["ShaftHubConnectionLoadCase"],
        "_6950": ["ShaftLoadCase"],
        "_6951": ["ShaftToMountableComponentConnectionLoadCase"],
        "_6952": ["SpecialisedAssemblyLoadCase"],
        "_6953": ["SpiralBevelGearLoadCase"],
        "_6954": ["SpiralBevelGearMeshLoadCase"],
        "_6955": ["SpiralBevelGearSetLoadCase"],
        "_6956": ["SpringDamperConnectionLoadCase"],
        "_6957": ["SpringDamperHalfLoadCase"],
        "_6958": ["SpringDamperLoadCase"],
        "_6959": ["StraightBevelDiffGearLoadCase"],
        "_6960": ["StraightBevelDiffGearMeshLoadCase"],
        "_6961": ["StraightBevelDiffGearSetLoadCase"],
        "_6962": ["StraightBevelGearLoadCase"],
        "_6963": ["StraightBevelGearMeshLoadCase"],
        "_6964": ["StraightBevelGearSetLoadCase"],
        "_6965": ["StraightBevelPlanetGearLoadCase"],
        "_6966": ["StraightBevelSunGearLoadCase"],
        "_6967": ["SynchroniserHalfLoadCase"],
        "_6968": ["SynchroniserLoadCase"],
        "_6969": ["SynchroniserPartLoadCase"],
        "_6970": ["SynchroniserSleeveLoadCase"],
        "_6971": ["TEExcitationType"],
        "_6972": ["TorqueConverterConnectionLoadCase"],
        "_6973": ["TorqueConverterLoadCase"],
        "_6974": ["TorqueConverterPumpLoadCase"],
        "_6975": ["TorqueConverterTurbineLoadCase"],
        "_6976": ["TorqueRippleInputType"],
        "_6977": ["TorqueSpecificationForSystemDeflection"],
        "_6978": ["TransmissionEfficiencySettings"],
        "_6979": ["UnbalancedMassHarmonicLoadData"],
        "_6980": ["UnbalancedMassLoadCase"],
        "_6981": ["VirtualComponentLoadCase"],
        "_6982": ["WormGearLoadCase"],
        "_6983": ["WormGearMeshLoadCase"],
        "_6984": ["WormGearSetLoadCase"],
        "_6985": ["ZerolBevelGearLoadCase"],
        "_6986": ["ZerolBevelGearMeshLoadCase"],
        "_6987": ["ZerolBevelGearSetLoadCase"],
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

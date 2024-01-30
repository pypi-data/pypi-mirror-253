"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3763 import AbstractAssemblyStabilityAnalysis
    from ._3764 import AbstractShaftOrHousingStabilityAnalysis
    from ._3765 import AbstractShaftStabilityAnalysis
    from ._3766 import AbstractShaftToMountableComponentConnectionStabilityAnalysis
    from ._3767 import AGMAGleasonConicalGearMeshStabilityAnalysis
    from ._3768 import AGMAGleasonConicalGearSetStabilityAnalysis
    from ._3769 import AGMAGleasonConicalGearStabilityAnalysis
    from ._3770 import AssemblyStabilityAnalysis
    from ._3771 import BearingStabilityAnalysis
    from ._3772 import BeltConnectionStabilityAnalysis
    from ._3773 import BeltDriveStabilityAnalysis
    from ._3774 import BevelDifferentialGearMeshStabilityAnalysis
    from ._3775 import BevelDifferentialGearSetStabilityAnalysis
    from ._3776 import BevelDifferentialGearStabilityAnalysis
    from ._3777 import BevelDifferentialPlanetGearStabilityAnalysis
    from ._3778 import BevelDifferentialSunGearStabilityAnalysis
    from ._3779 import BevelGearMeshStabilityAnalysis
    from ._3780 import BevelGearSetStabilityAnalysis
    from ._3781 import BevelGearStabilityAnalysis
    from ._3782 import BoltedJointStabilityAnalysis
    from ._3783 import BoltStabilityAnalysis
    from ._3784 import ClutchConnectionStabilityAnalysis
    from ._3785 import ClutchHalfStabilityAnalysis
    from ._3786 import ClutchStabilityAnalysis
    from ._3787 import CoaxialConnectionStabilityAnalysis
    from ._3788 import ComponentStabilityAnalysis
    from ._3789 import ConceptCouplingConnectionStabilityAnalysis
    from ._3790 import ConceptCouplingHalfStabilityAnalysis
    from ._3791 import ConceptCouplingStabilityAnalysis
    from ._3792 import ConceptGearMeshStabilityAnalysis
    from ._3793 import ConceptGearSetStabilityAnalysis
    from ._3794 import ConceptGearStabilityAnalysis
    from ._3795 import ConicalGearMeshStabilityAnalysis
    from ._3796 import ConicalGearSetStabilityAnalysis
    from ._3797 import ConicalGearStabilityAnalysis
    from ._3798 import ConnectionStabilityAnalysis
    from ._3799 import ConnectorStabilityAnalysis
    from ._3800 import CouplingConnectionStabilityAnalysis
    from ._3801 import CouplingHalfStabilityAnalysis
    from ._3802 import CouplingStabilityAnalysis
    from ._3803 import CriticalSpeed
    from ._3804 import CVTBeltConnectionStabilityAnalysis
    from ._3805 import CVTPulleyStabilityAnalysis
    from ._3806 import CVTStabilityAnalysis
    from ._3807 import CycloidalAssemblyStabilityAnalysis
    from ._3808 import CycloidalDiscCentralBearingConnectionStabilityAnalysis
    from ._3809 import CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
    from ._3810 import CycloidalDiscStabilityAnalysis
    from ._3811 import CylindricalGearMeshStabilityAnalysis
    from ._3812 import CylindricalGearSetStabilityAnalysis
    from ._3813 import CylindricalGearStabilityAnalysis
    from ._3814 import CylindricalPlanetGearStabilityAnalysis
    from ._3815 import DatumStabilityAnalysis
    from ._3816 import DynamicModelForStabilityAnalysis
    from ._3817 import ExternalCADModelStabilityAnalysis
    from ._3818 import FaceGearMeshStabilityAnalysis
    from ._3819 import FaceGearSetStabilityAnalysis
    from ._3820 import FaceGearStabilityAnalysis
    from ._3821 import FEPartStabilityAnalysis
    from ._3822 import FlexiblePinAssemblyStabilityAnalysis
    from ._3823 import GearMeshStabilityAnalysis
    from ._3824 import GearSetStabilityAnalysis
    from ._3825 import GearStabilityAnalysis
    from ._3826 import GuideDxfModelStabilityAnalysis
    from ._3827 import HypoidGearMeshStabilityAnalysis
    from ._3828 import HypoidGearSetStabilityAnalysis
    from ._3829 import HypoidGearStabilityAnalysis
    from ._3830 import InterMountableComponentConnectionStabilityAnalysis
    from ._3831 import KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
    from ._3832 import KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis
    from ._3833 import KlingelnbergCycloPalloidConicalGearStabilityAnalysis
    from ._3834 import KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
    from ._3835 import KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis
    from ._3836 import KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
    from ._3837 import KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
    from ._3838 import KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis
    from ._3839 import KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
    from ._3840 import MassDiscStabilityAnalysis
    from ._3841 import MeasurementComponentStabilityAnalysis
    from ._3842 import MountableComponentStabilityAnalysis
    from ._3843 import OilSealStabilityAnalysis
    from ._3844 import PartStabilityAnalysis
    from ._3845 import PartToPartShearCouplingConnectionStabilityAnalysis
    from ._3846 import PartToPartShearCouplingHalfStabilityAnalysis
    from ._3847 import PartToPartShearCouplingStabilityAnalysis
    from ._3848 import PlanetaryConnectionStabilityAnalysis
    from ._3849 import PlanetaryGearSetStabilityAnalysis
    from ._3850 import PlanetCarrierStabilityAnalysis
    from ._3851 import PointLoadStabilityAnalysis
    from ._3852 import PowerLoadStabilityAnalysis
    from ._3853 import PulleyStabilityAnalysis
    from ._3854 import RingPinsStabilityAnalysis
    from ._3855 import RingPinsToDiscConnectionStabilityAnalysis
    from ._3856 import RollingRingAssemblyStabilityAnalysis
    from ._3857 import RollingRingConnectionStabilityAnalysis
    from ._3858 import RollingRingStabilityAnalysis
    from ._3859 import RootAssemblyStabilityAnalysis
    from ._3860 import ShaftHubConnectionStabilityAnalysis
    from ._3861 import ShaftStabilityAnalysis
    from ._3862 import ShaftToMountableComponentConnectionStabilityAnalysis
    from ._3863 import SpecialisedAssemblyStabilityAnalysis
    from ._3864 import SpiralBevelGearMeshStabilityAnalysis
    from ._3865 import SpiralBevelGearSetStabilityAnalysis
    from ._3866 import SpiralBevelGearStabilityAnalysis
    from ._3867 import SpringDamperConnectionStabilityAnalysis
    from ._3868 import SpringDamperHalfStabilityAnalysis
    from ._3869 import SpringDamperStabilityAnalysis
    from ._3870 import StabilityAnalysis
    from ._3871 import StabilityAnalysisDrawStyle
    from ._3872 import StabilityAnalysisOptions
    from ._3873 import StraightBevelDiffGearMeshStabilityAnalysis
    from ._3874 import StraightBevelDiffGearSetStabilityAnalysis
    from ._3875 import StraightBevelDiffGearStabilityAnalysis
    from ._3876 import StraightBevelGearMeshStabilityAnalysis
    from ._3877 import StraightBevelGearSetStabilityAnalysis
    from ._3878 import StraightBevelGearStabilityAnalysis
    from ._3879 import StraightBevelPlanetGearStabilityAnalysis
    from ._3880 import StraightBevelSunGearStabilityAnalysis
    from ._3881 import SynchroniserHalfStabilityAnalysis
    from ._3882 import SynchroniserPartStabilityAnalysis
    from ._3883 import SynchroniserSleeveStabilityAnalysis
    from ._3884 import SynchroniserStabilityAnalysis
    from ._3885 import TorqueConverterConnectionStabilityAnalysis
    from ._3886 import TorqueConverterPumpStabilityAnalysis
    from ._3887 import TorqueConverterStabilityAnalysis
    from ._3888 import TorqueConverterTurbineStabilityAnalysis
    from ._3889 import UnbalancedMassStabilityAnalysis
    from ._3890 import VirtualComponentStabilityAnalysis
    from ._3891 import WormGearMeshStabilityAnalysis
    from ._3892 import WormGearSetStabilityAnalysis
    from ._3893 import WormGearStabilityAnalysis
    from ._3894 import ZerolBevelGearMeshStabilityAnalysis
    from ._3895 import ZerolBevelGearSetStabilityAnalysis
    from ._3896 import ZerolBevelGearStabilityAnalysis
else:
    import_structure = {
        "_3763": ["AbstractAssemblyStabilityAnalysis"],
        "_3764": ["AbstractShaftOrHousingStabilityAnalysis"],
        "_3765": ["AbstractShaftStabilityAnalysis"],
        "_3766": ["AbstractShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3767": ["AGMAGleasonConicalGearMeshStabilityAnalysis"],
        "_3768": ["AGMAGleasonConicalGearSetStabilityAnalysis"],
        "_3769": ["AGMAGleasonConicalGearStabilityAnalysis"],
        "_3770": ["AssemblyStabilityAnalysis"],
        "_3771": ["BearingStabilityAnalysis"],
        "_3772": ["BeltConnectionStabilityAnalysis"],
        "_3773": ["BeltDriveStabilityAnalysis"],
        "_3774": ["BevelDifferentialGearMeshStabilityAnalysis"],
        "_3775": ["BevelDifferentialGearSetStabilityAnalysis"],
        "_3776": ["BevelDifferentialGearStabilityAnalysis"],
        "_3777": ["BevelDifferentialPlanetGearStabilityAnalysis"],
        "_3778": ["BevelDifferentialSunGearStabilityAnalysis"],
        "_3779": ["BevelGearMeshStabilityAnalysis"],
        "_3780": ["BevelGearSetStabilityAnalysis"],
        "_3781": ["BevelGearStabilityAnalysis"],
        "_3782": ["BoltedJointStabilityAnalysis"],
        "_3783": ["BoltStabilityAnalysis"],
        "_3784": ["ClutchConnectionStabilityAnalysis"],
        "_3785": ["ClutchHalfStabilityAnalysis"],
        "_3786": ["ClutchStabilityAnalysis"],
        "_3787": ["CoaxialConnectionStabilityAnalysis"],
        "_3788": ["ComponentStabilityAnalysis"],
        "_3789": ["ConceptCouplingConnectionStabilityAnalysis"],
        "_3790": ["ConceptCouplingHalfStabilityAnalysis"],
        "_3791": ["ConceptCouplingStabilityAnalysis"],
        "_3792": ["ConceptGearMeshStabilityAnalysis"],
        "_3793": ["ConceptGearSetStabilityAnalysis"],
        "_3794": ["ConceptGearStabilityAnalysis"],
        "_3795": ["ConicalGearMeshStabilityAnalysis"],
        "_3796": ["ConicalGearSetStabilityAnalysis"],
        "_3797": ["ConicalGearStabilityAnalysis"],
        "_3798": ["ConnectionStabilityAnalysis"],
        "_3799": ["ConnectorStabilityAnalysis"],
        "_3800": ["CouplingConnectionStabilityAnalysis"],
        "_3801": ["CouplingHalfStabilityAnalysis"],
        "_3802": ["CouplingStabilityAnalysis"],
        "_3803": ["CriticalSpeed"],
        "_3804": ["CVTBeltConnectionStabilityAnalysis"],
        "_3805": ["CVTPulleyStabilityAnalysis"],
        "_3806": ["CVTStabilityAnalysis"],
        "_3807": ["CycloidalAssemblyStabilityAnalysis"],
        "_3808": ["CycloidalDiscCentralBearingConnectionStabilityAnalysis"],
        "_3809": ["CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis"],
        "_3810": ["CycloidalDiscStabilityAnalysis"],
        "_3811": ["CylindricalGearMeshStabilityAnalysis"],
        "_3812": ["CylindricalGearSetStabilityAnalysis"],
        "_3813": ["CylindricalGearStabilityAnalysis"],
        "_3814": ["CylindricalPlanetGearStabilityAnalysis"],
        "_3815": ["DatumStabilityAnalysis"],
        "_3816": ["DynamicModelForStabilityAnalysis"],
        "_3817": ["ExternalCADModelStabilityAnalysis"],
        "_3818": ["FaceGearMeshStabilityAnalysis"],
        "_3819": ["FaceGearSetStabilityAnalysis"],
        "_3820": ["FaceGearStabilityAnalysis"],
        "_3821": ["FEPartStabilityAnalysis"],
        "_3822": ["FlexiblePinAssemblyStabilityAnalysis"],
        "_3823": ["GearMeshStabilityAnalysis"],
        "_3824": ["GearSetStabilityAnalysis"],
        "_3825": ["GearStabilityAnalysis"],
        "_3826": ["GuideDxfModelStabilityAnalysis"],
        "_3827": ["HypoidGearMeshStabilityAnalysis"],
        "_3828": ["HypoidGearSetStabilityAnalysis"],
        "_3829": ["HypoidGearStabilityAnalysis"],
        "_3830": ["InterMountableComponentConnectionStabilityAnalysis"],
        "_3831": ["KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis"],
        "_3832": ["KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis"],
        "_3833": ["KlingelnbergCycloPalloidConicalGearStabilityAnalysis"],
        "_3834": ["KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis"],
        "_3835": ["KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis"],
        "_3836": ["KlingelnbergCycloPalloidHypoidGearStabilityAnalysis"],
        "_3837": ["KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis"],
        "_3838": ["KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis"],
        "_3839": ["KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis"],
        "_3840": ["MassDiscStabilityAnalysis"],
        "_3841": ["MeasurementComponentStabilityAnalysis"],
        "_3842": ["MountableComponentStabilityAnalysis"],
        "_3843": ["OilSealStabilityAnalysis"],
        "_3844": ["PartStabilityAnalysis"],
        "_3845": ["PartToPartShearCouplingConnectionStabilityAnalysis"],
        "_3846": ["PartToPartShearCouplingHalfStabilityAnalysis"],
        "_3847": ["PartToPartShearCouplingStabilityAnalysis"],
        "_3848": ["PlanetaryConnectionStabilityAnalysis"],
        "_3849": ["PlanetaryGearSetStabilityAnalysis"],
        "_3850": ["PlanetCarrierStabilityAnalysis"],
        "_3851": ["PointLoadStabilityAnalysis"],
        "_3852": ["PowerLoadStabilityAnalysis"],
        "_3853": ["PulleyStabilityAnalysis"],
        "_3854": ["RingPinsStabilityAnalysis"],
        "_3855": ["RingPinsToDiscConnectionStabilityAnalysis"],
        "_3856": ["RollingRingAssemblyStabilityAnalysis"],
        "_3857": ["RollingRingConnectionStabilityAnalysis"],
        "_3858": ["RollingRingStabilityAnalysis"],
        "_3859": ["RootAssemblyStabilityAnalysis"],
        "_3860": ["ShaftHubConnectionStabilityAnalysis"],
        "_3861": ["ShaftStabilityAnalysis"],
        "_3862": ["ShaftToMountableComponentConnectionStabilityAnalysis"],
        "_3863": ["SpecialisedAssemblyStabilityAnalysis"],
        "_3864": ["SpiralBevelGearMeshStabilityAnalysis"],
        "_3865": ["SpiralBevelGearSetStabilityAnalysis"],
        "_3866": ["SpiralBevelGearStabilityAnalysis"],
        "_3867": ["SpringDamperConnectionStabilityAnalysis"],
        "_3868": ["SpringDamperHalfStabilityAnalysis"],
        "_3869": ["SpringDamperStabilityAnalysis"],
        "_3870": ["StabilityAnalysis"],
        "_3871": ["StabilityAnalysisDrawStyle"],
        "_3872": ["StabilityAnalysisOptions"],
        "_3873": ["StraightBevelDiffGearMeshStabilityAnalysis"],
        "_3874": ["StraightBevelDiffGearSetStabilityAnalysis"],
        "_3875": ["StraightBevelDiffGearStabilityAnalysis"],
        "_3876": ["StraightBevelGearMeshStabilityAnalysis"],
        "_3877": ["StraightBevelGearSetStabilityAnalysis"],
        "_3878": ["StraightBevelGearStabilityAnalysis"],
        "_3879": ["StraightBevelPlanetGearStabilityAnalysis"],
        "_3880": ["StraightBevelSunGearStabilityAnalysis"],
        "_3881": ["SynchroniserHalfStabilityAnalysis"],
        "_3882": ["SynchroniserPartStabilityAnalysis"],
        "_3883": ["SynchroniserSleeveStabilityAnalysis"],
        "_3884": ["SynchroniserStabilityAnalysis"],
        "_3885": ["TorqueConverterConnectionStabilityAnalysis"],
        "_3886": ["TorqueConverterPumpStabilityAnalysis"],
        "_3887": ["TorqueConverterStabilityAnalysis"],
        "_3888": ["TorqueConverterTurbineStabilityAnalysis"],
        "_3889": ["UnbalancedMassStabilityAnalysis"],
        "_3890": ["VirtualComponentStabilityAnalysis"],
        "_3891": ["WormGearMeshStabilityAnalysis"],
        "_3892": ["WormGearSetStabilityAnalysis"],
        "_3893": ["WormGearStabilityAnalysis"],
        "_3894": ["ZerolBevelGearMeshStabilityAnalysis"],
        "_3895": ["ZerolBevelGearSetStabilityAnalysis"],
        "_3896": ["ZerolBevelGearStabilityAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyStabilityAnalysis",
    "AbstractShaftOrHousingStabilityAnalysis",
    "AbstractShaftStabilityAnalysis",
    "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    "AGMAGleasonConicalGearMeshStabilityAnalysis",
    "AGMAGleasonConicalGearSetStabilityAnalysis",
    "AGMAGleasonConicalGearStabilityAnalysis",
    "AssemblyStabilityAnalysis",
    "BearingStabilityAnalysis",
    "BeltConnectionStabilityAnalysis",
    "BeltDriveStabilityAnalysis",
    "BevelDifferentialGearMeshStabilityAnalysis",
    "BevelDifferentialGearSetStabilityAnalysis",
    "BevelDifferentialGearStabilityAnalysis",
    "BevelDifferentialPlanetGearStabilityAnalysis",
    "BevelDifferentialSunGearStabilityAnalysis",
    "BevelGearMeshStabilityAnalysis",
    "BevelGearSetStabilityAnalysis",
    "BevelGearStabilityAnalysis",
    "BoltedJointStabilityAnalysis",
    "BoltStabilityAnalysis",
    "ClutchConnectionStabilityAnalysis",
    "ClutchHalfStabilityAnalysis",
    "ClutchStabilityAnalysis",
    "CoaxialConnectionStabilityAnalysis",
    "ComponentStabilityAnalysis",
    "ConceptCouplingConnectionStabilityAnalysis",
    "ConceptCouplingHalfStabilityAnalysis",
    "ConceptCouplingStabilityAnalysis",
    "ConceptGearMeshStabilityAnalysis",
    "ConceptGearSetStabilityAnalysis",
    "ConceptGearStabilityAnalysis",
    "ConicalGearMeshStabilityAnalysis",
    "ConicalGearSetStabilityAnalysis",
    "ConicalGearStabilityAnalysis",
    "ConnectionStabilityAnalysis",
    "ConnectorStabilityAnalysis",
    "CouplingConnectionStabilityAnalysis",
    "CouplingHalfStabilityAnalysis",
    "CouplingStabilityAnalysis",
    "CriticalSpeed",
    "CVTBeltConnectionStabilityAnalysis",
    "CVTPulleyStabilityAnalysis",
    "CVTStabilityAnalysis",
    "CycloidalAssemblyStabilityAnalysis",
    "CycloidalDiscCentralBearingConnectionStabilityAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis",
    "CycloidalDiscStabilityAnalysis",
    "CylindricalGearMeshStabilityAnalysis",
    "CylindricalGearSetStabilityAnalysis",
    "CylindricalGearStabilityAnalysis",
    "CylindricalPlanetGearStabilityAnalysis",
    "DatumStabilityAnalysis",
    "DynamicModelForStabilityAnalysis",
    "ExternalCADModelStabilityAnalysis",
    "FaceGearMeshStabilityAnalysis",
    "FaceGearSetStabilityAnalysis",
    "FaceGearStabilityAnalysis",
    "FEPartStabilityAnalysis",
    "FlexiblePinAssemblyStabilityAnalysis",
    "GearMeshStabilityAnalysis",
    "GearSetStabilityAnalysis",
    "GearStabilityAnalysis",
    "GuideDxfModelStabilityAnalysis",
    "HypoidGearMeshStabilityAnalysis",
    "HypoidGearSetStabilityAnalysis",
    "HypoidGearStabilityAnalysis",
    "InterMountableComponentConnectionStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidConicalGearStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidHypoidGearStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetStabilityAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis",
    "MassDiscStabilityAnalysis",
    "MeasurementComponentStabilityAnalysis",
    "MountableComponentStabilityAnalysis",
    "OilSealStabilityAnalysis",
    "PartStabilityAnalysis",
    "PartToPartShearCouplingConnectionStabilityAnalysis",
    "PartToPartShearCouplingHalfStabilityAnalysis",
    "PartToPartShearCouplingStabilityAnalysis",
    "PlanetaryConnectionStabilityAnalysis",
    "PlanetaryGearSetStabilityAnalysis",
    "PlanetCarrierStabilityAnalysis",
    "PointLoadStabilityAnalysis",
    "PowerLoadStabilityAnalysis",
    "PulleyStabilityAnalysis",
    "RingPinsStabilityAnalysis",
    "RingPinsToDiscConnectionStabilityAnalysis",
    "RollingRingAssemblyStabilityAnalysis",
    "RollingRingConnectionStabilityAnalysis",
    "RollingRingStabilityAnalysis",
    "RootAssemblyStabilityAnalysis",
    "ShaftHubConnectionStabilityAnalysis",
    "ShaftStabilityAnalysis",
    "ShaftToMountableComponentConnectionStabilityAnalysis",
    "SpecialisedAssemblyStabilityAnalysis",
    "SpiralBevelGearMeshStabilityAnalysis",
    "SpiralBevelGearSetStabilityAnalysis",
    "SpiralBevelGearStabilityAnalysis",
    "SpringDamperConnectionStabilityAnalysis",
    "SpringDamperHalfStabilityAnalysis",
    "SpringDamperStabilityAnalysis",
    "StabilityAnalysis",
    "StabilityAnalysisDrawStyle",
    "StabilityAnalysisOptions",
    "StraightBevelDiffGearMeshStabilityAnalysis",
    "StraightBevelDiffGearSetStabilityAnalysis",
    "StraightBevelDiffGearStabilityAnalysis",
    "StraightBevelGearMeshStabilityAnalysis",
    "StraightBevelGearSetStabilityAnalysis",
    "StraightBevelGearStabilityAnalysis",
    "StraightBevelPlanetGearStabilityAnalysis",
    "StraightBevelSunGearStabilityAnalysis",
    "SynchroniserHalfStabilityAnalysis",
    "SynchroniserPartStabilityAnalysis",
    "SynchroniserSleeveStabilityAnalysis",
    "SynchroniserStabilityAnalysis",
    "TorqueConverterConnectionStabilityAnalysis",
    "TorqueConverterPumpStabilityAnalysis",
    "TorqueConverterStabilityAnalysis",
    "TorqueConverterTurbineStabilityAnalysis",
    "UnbalancedMassStabilityAnalysis",
    "VirtualComponentStabilityAnalysis",
    "WormGearMeshStabilityAnalysis",
    "WormGearSetStabilityAnalysis",
    "WormGearStabilityAnalysis",
    "ZerolBevelGearMeshStabilityAnalysis",
    "ZerolBevelGearSetStabilityAnalysis",
    "ZerolBevelGearStabilityAnalysis",
)

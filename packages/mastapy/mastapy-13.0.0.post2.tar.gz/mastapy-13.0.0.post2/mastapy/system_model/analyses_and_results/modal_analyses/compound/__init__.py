"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4727 import AbstractAssemblyCompoundModalAnalysis
    from ._4728 import AbstractShaftCompoundModalAnalysis
    from ._4729 import AbstractShaftOrHousingCompoundModalAnalysis
    from ._4730 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4731 import AGMAGleasonConicalGearCompoundModalAnalysis
    from ._4732 import AGMAGleasonConicalGearMeshCompoundModalAnalysis
    from ._4733 import AGMAGleasonConicalGearSetCompoundModalAnalysis
    from ._4734 import AssemblyCompoundModalAnalysis
    from ._4735 import BearingCompoundModalAnalysis
    from ._4736 import BeltConnectionCompoundModalAnalysis
    from ._4737 import BeltDriveCompoundModalAnalysis
    from ._4738 import BevelDifferentialGearCompoundModalAnalysis
    from ._4739 import BevelDifferentialGearMeshCompoundModalAnalysis
    from ._4740 import BevelDifferentialGearSetCompoundModalAnalysis
    from ._4741 import BevelDifferentialPlanetGearCompoundModalAnalysis
    from ._4742 import BevelDifferentialSunGearCompoundModalAnalysis
    from ._4743 import BevelGearCompoundModalAnalysis
    from ._4744 import BevelGearMeshCompoundModalAnalysis
    from ._4745 import BevelGearSetCompoundModalAnalysis
    from ._4746 import BoltCompoundModalAnalysis
    from ._4747 import BoltedJointCompoundModalAnalysis
    from ._4748 import ClutchCompoundModalAnalysis
    from ._4749 import ClutchConnectionCompoundModalAnalysis
    from ._4750 import ClutchHalfCompoundModalAnalysis
    from ._4751 import CoaxialConnectionCompoundModalAnalysis
    from ._4752 import ComponentCompoundModalAnalysis
    from ._4753 import ConceptCouplingCompoundModalAnalysis
    from ._4754 import ConceptCouplingConnectionCompoundModalAnalysis
    from ._4755 import ConceptCouplingHalfCompoundModalAnalysis
    from ._4756 import ConceptGearCompoundModalAnalysis
    from ._4757 import ConceptGearMeshCompoundModalAnalysis
    from ._4758 import ConceptGearSetCompoundModalAnalysis
    from ._4759 import ConicalGearCompoundModalAnalysis
    from ._4760 import ConicalGearMeshCompoundModalAnalysis
    from ._4761 import ConicalGearSetCompoundModalAnalysis
    from ._4762 import ConnectionCompoundModalAnalysis
    from ._4763 import ConnectorCompoundModalAnalysis
    from ._4764 import CouplingCompoundModalAnalysis
    from ._4765 import CouplingConnectionCompoundModalAnalysis
    from ._4766 import CouplingHalfCompoundModalAnalysis
    from ._4767 import CVTBeltConnectionCompoundModalAnalysis
    from ._4768 import CVTCompoundModalAnalysis
    from ._4769 import CVTPulleyCompoundModalAnalysis
    from ._4770 import CycloidalAssemblyCompoundModalAnalysis
    from ._4771 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
    from ._4772 import CycloidalDiscCompoundModalAnalysis
    from ._4773 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
    from ._4774 import CylindricalGearCompoundModalAnalysis
    from ._4775 import CylindricalGearMeshCompoundModalAnalysis
    from ._4776 import CylindricalGearSetCompoundModalAnalysis
    from ._4777 import CylindricalPlanetGearCompoundModalAnalysis
    from ._4778 import DatumCompoundModalAnalysis
    from ._4779 import ExternalCADModelCompoundModalAnalysis
    from ._4780 import FaceGearCompoundModalAnalysis
    from ._4781 import FaceGearMeshCompoundModalAnalysis
    from ._4782 import FaceGearSetCompoundModalAnalysis
    from ._4783 import FEPartCompoundModalAnalysis
    from ._4784 import FlexiblePinAssemblyCompoundModalAnalysis
    from ._4785 import GearCompoundModalAnalysis
    from ._4786 import GearMeshCompoundModalAnalysis
    from ._4787 import GearSetCompoundModalAnalysis
    from ._4788 import GuideDxfModelCompoundModalAnalysis
    from ._4789 import HypoidGearCompoundModalAnalysis
    from ._4790 import HypoidGearMeshCompoundModalAnalysis
    from ._4791 import HypoidGearSetCompoundModalAnalysis
    from ._4792 import InterMountableComponentConnectionCompoundModalAnalysis
    from ._4793 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
    from ._4794 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
    from ._4795 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
    from ._4796 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
    from ._4797 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
    from ._4798 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
    from ._4799 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
    from ._4800 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
    from ._4801 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
    from ._4802 import MassDiscCompoundModalAnalysis
    from ._4803 import MeasurementComponentCompoundModalAnalysis
    from ._4804 import MountableComponentCompoundModalAnalysis
    from ._4805 import OilSealCompoundModalAnalysis
    from ._4806 import PartCompoundModalAnalysis
    from ._4807 import PartToPartShearCouplingCompoundModalAnalysis
    from ._4808 import PartToPartShearCouplingConnectionCompoundModalAnalysis
    from ._4809 import PartToPartShearCouplingHalfCompoundModalAnalysis
    from ._4810 import PlanetaryConnectionCompoundModalAnalysis
    from ._4811 import PlanetaryGearSetCompoundModalAnalysis
    from ._4812 import PlanetCarrierCompoundModalAnalysis
    from ._4813 import PointLoadCompoundModalAnalysis
    from ._4814 import PowerLoadCompoundModalAnalysis
    from ._4815 import PulleyCompoundModalAnalysis
    from ._4816 import RingPinsCompoundModalAnalysis
    from ._4817 import RingPinsToDiscConnectionCompoundModalAnalysis
    from ._4818 import RollingRingAssemblyCompoundModalAnalysis
    from ._4819 import RollingRingCompoundModalAnalysis
    from ._4820 import RollingRingConnectionCompoundModalAnalysis
    from ._4821 import RootAssemblyCompoundModalAnalysis
    from ._4822 import ShaftCompoundModalAnalysis
    from ._4823 import ShaftHubConnectionCompoundModalAnalysis
    from ._4824 import ShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4825 import SpecialisedAssemblyCompoundModalAnalysis
    from ._4826 import SpiralBevelGearCompoundModalAnalysis
    from ._4827 import SpiralBevelGearMeshCompoundModalAnalysis
    from ._4828 import SpiralBevelGearSetCompoundModalAnalysis
    from ._4829 import SpringDamperCompoundModalAnalysis
    from ._4830 import SpringDamperConnectionCompoundModalAnalysis
    from ._4831 import SpringDamperHalfCompoundModalAnalysis
    from ._4832 import StraightBevelDiffGearCompoundModalAnalysis
    from ._4833 import StraightBevelDiffGearMeshCompoundModalAnalysis
    from ._4834 import StraightBevelDiffGearSetCompoundModalAnalysis
    from ._4835 import StraightBevelGearCompoundModalAnalysis
    from ._4836 import StraightBevelGearMeshCompoundModalAnalysis
    from ._4837 import StraightBevelGearSetCompoundModalAnalysis
    from ._4838 import StraightBevelPlanetGearCompoundModalAnalysis
    from ._4839 import StraightBevelSunGearCompoundModalAnalysis
    from ._4840 import SynchroniserCompoundModalAnalysis
    from ._4841 import SynchroniserHalfCompoundModalAnalysis
    from ._4842 import SynchroniserPartCompoundModalAnalysis
    from ._4843 import SynchroniserSleeveCompoundModalAnalysis
    from ._4844 import TorqueConverterCompoundModalAnalysis
    from ._4845 import TorqueConverterConnectionCompoundModalAnalysis
    from ._4846 import TorqueConverterPumpCompoundModalAnalysis
    from ._4847 import TorqueConverterTurbineCompoundModalAnalysis
    from ._4848 import UnbalancedMassCompoundModalAnalysis
    from ._4849 import VirtualComponentCompoundModalAnalysis
    from ._4850 import WormGearCompoundModalAnalysis
    from ._4851 import WormGearMeshCompoundModalAnalysis
    from ._4852 import WormGearSetCompoundModalAnalysis
    from ._4853 import ZerolBevelGearCompoundModalAnalysis
    from ._4854 import ZerolBevelGearMeshCompoundModalAnalysis
    from ._4855 import ZerolBevelGearSetCompoundModalAnalysis
else:
    import_structure = {
        "_4727": ["AbstractAssemblyCompoundModalAnalysis"],
        "_4728": ["AbstractShaftCompoundModalAnalysis"],
        "_4729": ["AbstractShaftOrHousingCompoundModalAnalysis"],
        "_4730": ["AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4731": ["AGMAGleasonConicalGearCompoundModalAnalysis"],
        "_4732": ["AGMAGleasonConicalGearMeshCompoundModalAnalysis"],
        "_4733": ["AGMAGleasonConicalGearSetCompoundModalAnalysis"],
        "_4734": ["AssemblyCompoundModalAnalysis"],
        "_4735": ["BearingCompoundModalAnalysis"],
        "_4736": ["BeltConnectionCompoundModalAnalysis"],
        "_4737": ["BeltDriveCompoundModalAnalysis"],
        "_4738": ["BevelDifferentialGearCompoundModalAnalysis"],
        "_4739": ["BevelDifferentialGearMeshCompoundModalAnalysis"],
        "_4740": ["BevelDifferentialGearSetCompoundModalAnalysis"],
        "_4741": ["BevelDifferentialPlanetGearCompoundModalAnalysis"],
        "_4742": ["BevelDifferentialSunGearCompoundModalAnalysis"],
        "_4743": ["BevelGearCompoundModalAnalysis"],
        "_4744": ["BevelGearMeshCompoundModalAnalysis"],
        "_4745": ["BevelGearSetCompoundModalAnalysis"],
        "_4746": ["BoltCompoundModalAnalysis"],
        "_4747": ["BoltedJointCompoundModalAnalysis"],
        "_4748": ["ClutchCompoundModalAnalysis"],
        "_4749": ["ClutchConnectionCompoundModalAnalysis"],
        "_4750": ["ClutchHalfCompoundModalAnalysis"],
        "_4751": ["CoaxialConnectionCompoundModalAnalysis"],
        "_4752": ["ComponentCompoundModalAnalysis"],
        "_4753": ["ConceptCouplingCompoundModalAnalysis"],
        "_4754": ["ConceptCouplingConnectionCompoundModalAnalysis"],
        "_4755": ["ConceptCouplingHalfCompoundModalAnalysis"],
        "_4756": ["ConceptGearCompoundModalAnalysis"],
        "_4757": ["ConceptGearMeshCompoundModalAnalysis"],
        "_4758": ["ConceptGearSetCompoundModalAnalysis"],
        "_4759": ["ConicalGearCompoundModalAnalysis"],
        "_4760": ["ConicalGearMeshCompoundModalAnalysis"],
        "_4761": ["ConicalGearSetCompoundModalAnalysis"],
        "_4762": ["ConnectionCompoundModalAnalysis"],
        "_4763": ["ConnectorCompoundModalAnalysis"],
        "_4764": ["CouplingCompoundModalAnalysis"],
        "_4765": ["CouplingConnectionCompoundModalAnalysis"],
        "_4766": ["CouplingHalfCompoundModalAnalysis"],
        "_4767": ["CVTBeltConnectionCompoundModalAnalysis"],
        "_4768": ["CVTCompoundModalAnalysis"],
        "_4769": ["CVTPulleyCompoundModalAnalysis"],
        "_4770": ["CycloidalAssemblyCompoundModalAnalysis"],
        "_4771": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysis"],
        "_4772": ["CycloidalDiscCompoundModalAnalysis"],
        "_4773": ["CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis"],
        "_4774": ["CylindricalGearCompoundModalAnalysis"],
        "_4775": ["CylindricalGearMeshCompoundModalAnalysis"],
        "_4776": ["CylindricalGearSetCompoundModalAnalysis"],
        "_4777": ["CylindricalPlanetGearCompoundModalAnalysis"],
        "_4778": ["DatumCompoundModalAnalysis"],
        "_4779": ["ExternalCADModelCompoundModalAnalysis"],
        "_4780": ["FaceGearCompoundModalAnalysis"],
        "_4781": ["FaceGearMeshCompoundModalAnalysis"],
        "_4782": ["FaceGearSetCompoundModalAnalysis"],
        "_4783": ["FEPartCompoundModalAnalysis"],
        "_4784": ["FlexiblePinAssemblyCompoundModalAnalysis"],
        "_4785": ["GearCompoundModalAnalysis"],
        "_4786": ["GearMeshCompoundModalAnalysis"],
        "_4787": ["GearSetCompoundModalAnalysis"],
        "_4788": ["GuideDxfModelCompoundModalAnalysis"],
        "_4789": ["HypoidGearCompoundModalAnalysis"],
        "_4790": ["HypoidGearMeshCompoundModalAnalysis"],
        "_4791": ["HypoidGearSetCompoundModalAnalysis"],
        "_4792": ["InterMountableComponentConnectionCompoundModalAnalysis"],
        "_4793": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis"],
        "_4794": ["KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"],
        "_4795": ["KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"],
        "_4796": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis"],
        "_4797": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis"],
        "_4798": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis"],
        "_4799": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis"],
        "_4800": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis"],
        "_4801": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis"],
        "_4802": ["MassDiscCompoundModalAnalysis"],
        "_4803": ["MeasurementComponentCompoundModalAnalysis"],
        "_4804": ["MountableComponentCompoundModalAnalysis"],
        "_4805": ["OilSealCompoundModalAnalysis"],
        "_4806": ["PartCompoundModalAnalysis"],
        "_4807": ["PartToPartShearCouplingCompoundModalAnalysis"],
        "_4808": ["PartToPartShearCouplingConnectionCompoundModalAnalysis"],
        "_4809": ["PartToPartShearCouplingHalfCompoundModalAnalysis"],
        "_4810": ["PlanetaryConnectionCompoundModalAnalysis"],
        "_4811": ["PlanetaryGearSetCompoundModalAnalysis"],
        "_4812": ["PlanetCarrierCompoundModalAnalysis"],
        "_4813": ["PointLoadCompoundModalAnalysis"],
        "_4814": ["PowerLoadCompoundModalAnalysis"],
        "_4815": ["PulleyCompoundModalAnalysis"],
        "_4816": ["RingPinsCompoundModalAnalysis"],
        "_4817": ["RingPinsToDiscConnectionCompoundModalAnalysis"],
        "_4818": ["RollingRingAssemblyCompoundModalAnalysis"],
        "_4819": ["RollingRingCompoundModalAnalysis"],
        "_4820": ["RollingRingConnectionCompoundModalAnalysis"],
        "_4821": ["RootAssemblyCompoundModalAnalysis"],
        "_4822": ["ShaftCompoundModalAnalysis"],
        "_4823": ["ShaftHubConnectionCompoundModalAnalysis"],
        "_4824": ["ShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4825": ["SpecialisedAssemblyCompoundModalAnalysis"],
        "_4826": ["SpiralBevelGearCompoundModalAnalysis"],
        "_4827": ["SpiralBevelGearMeshCompoundModalAnalysis"],
        "_4828": ["SpiralBevelGearSetCompoundModalAnalysis"],
        "_4829": ["SpringDamperCompoundModalAnalysis"],
        "_4830": ["SpringDamperConnectionCompoundModalAnalysis"],
        "_4831": ["SpringDamperHalfCompoundModalAnalysis"],
        "_4832": ["StraightBevelDiffGearCompoundModalAnalysis"],
        "_4833": ["StraightBevelDiffGearMeshCompoundModalAnalysis"],
        "_4834": ["StraightBevelDiffGearSetCompoundModalAnalysis"],
        "_4835": ["StraightBevelGearCompoundModalAnalysis"],
        "_4836": ["StraightBevelGearMeshCompoundModalAnalysis"],
        "_4837": ["StraightBevelGearSetCompoundModalAnalysis"],
        "_4838": ["StraightBevelPlanetGearCompoundModalAnalysis"],
        "_4839": ["StraightBevelSunGearCompoundModalAnalysis"],
        "_4840": ["SynchroniserCompoundModalAnalysis"],
        "_4841": ["SynchroniserHalfCompoundModalAnalysis"],
        "_4842": ["SynchroniserPartCompoundModalAnalysis"],
        "_4843": ["SynchroniserSleeveCompoundModalAnalysis"],
        "_4844": ["TorqueConverterCompoundModalAnalysis"],
        "_4845": ["TorqueConverterConnectionCompoundModalAnalysis"],
        "_4846": ["TorqueConverterPumpCompoundModalAnalysis"],
        "_4847": ["TorqueConverterTurbineCompoundModalAnalysis"],
        "_4848": ["UnbalancedMassCompoundModalAnalysis"],
        "_4849": ["VirtualComponentCompoundModalAnalysis"],
        "_4850": ["WormGearCompoundModalAnalysis"],
        "_4851": ["WormGearMeshCompoundModalAnalysis"],
        "_4852": ["WormGearSetCompoundModalAnalysis"],
        "_4853": ["ZerolBevelGearCompoundModalAnalysis"],
        "_4854": ["ZerolBevelGearMeshCompoundModalAnalysis"],
        "_4855": ["ZerolBevelGearSetCompoundModalAnalysis"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundModalAnalysis",
    "AbstractShaftCompoundModalAnalysis",
    "AbstractShaftOrHousingCompoundModalAnalysis",
    "AbstractShaftToMountableComponentConnectionCompoundModalAnalysis",
    "AGMAGleasonConicalGearCompoundModalAnalysis",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysis",
    "AGMAGleasonConicalGearSetCompoundModalAnalysis",
    "AssemblyCompoundModalAnalysis",
    "BearingCompoundModalAnalysis",
    "BeltConnectionCompoundModalAnalysis",
    "BeltDriveCompoundModalAnalysis",
    "BevelDifferentialGearCompoundModalAnalysis",
    "BevelDifferentialGearMeshCompoundModalAnalysis",
    "BevelDifferentialGearSetCompoundModalAnalysis",
    "BevelDifferentialPlanetGearCompoundModalAnalysis",
    "BevelDifferentialSunGearCompoundModalAnalysis",
    "BevelGearCompoundModalAnalysis",
    "BevelGearMeshCompoundModalAnalysis",
    "BevelGearSetCompoundModalAnalysis",
    "BoltCompoundModalAnalysis",
    "BoltedJointCompoundModalAnalysis",
    "ClutchCompoundModalAnalysis",
    "ClutchConnectionCompoundModalAnalysis",
    "ClutchHalfCompoundModalAnalysis",
    "CoaxialConnectionCompoundModalAnalysis",
    "ComponentCompoundModalAnalysis",
    "ConceptCouplingCompoundModalAnalysis",
    "ConceptCouplingConnectionCompoundModalAnalysis",
    "ConceptCouplingHalfCompoundModalAnalysis",
    "ConceptGearCompoundModalAnalysis",
    "ConceptGearMeshCompoundModalAnalysis",
    "ConceptGearSetCompoundModalAnalysis",
    "ConicalGearCompoundModalAnalysis",
    "ConicalGearMeshCompoundModalAnalysis",
    "ConicalGearSetCompoundModalAnalysis",
    "ConnectionCompoundModalAnalysis",
    "ConnectorCompoundModalAnalysis",
    "CouplingCompoundModalAnalysis",
    "CouplingConnectionCompoundModalAnalysis",
    "CouplingHalfCompoundModalAnalysis",
    "CVTBeltConnectionCompoundModalAnalysis",
    "CVTCompoundModalAnalysis",
    "CVTPulleyCompoundModalAnalysis",
    "CycloidalAssemblyCompoundModalAnalysis",
    "CycloidalDiscCentralBearingConnectionCompoundModalAnalysis",
    "CycloidalDiscCompoundModalAnalysis",
    "CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis",
    "CylindricalGearCompoundModalAnalysis",
    "CylindricalGearMeshCompoundModalAnalysis",
    "CylindricalGearSetCompoundModalAnalysis",
    "CylindricalPlanetGearCompoundModalAnalysis",
    "DatumCompoundModalAnalysis",
    "ExternalCADModelCompoundModalAnalysis",
    "FaceGearCompoundModalAnalysis",
    "FaceGearMeshCompoundModalAnalysis",
    "FaceGearSetCompoundModalAnalysis",
    "FEPartCompoundModalAnalysis",
    "FlexiblePinAssemblyCompoundModalAnalysis",
    "GearCompoundModalAnalysis",
    "GearMeshCompoundModalAnalysis",
    "GearSetCompoundModalAnalysis",
    "GuideDxfModelCompoundModalAnalysis",
    "HypoidGearCompoundModalAnalysis",
    "HypoidGearMeshCompoundModalAnalysis",
    "HypoidGearSetCompoundModalAnalysis",
    "InterMountableComponentConnectionCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis",
    "MassDiscCompoundModalAnalysis",
    "MeasurementComponentCompoundModalAnalysis",
    "MountableComponentCompoundModalAnalysis",
    "OilSealCompoundModalAnalysis",
    "PartCompoundModalAnalysis",
    "PartToPartShearCouplingCompoundModalAnalysis",
    "PartToPartShearCouplingConnectionCompoundModalAnalysis",
    "PartToPartShearCouplingHalfCompoundModalAnalysis",
    "PlanetaryConnectionCompoundModalAnalysis",
    "PlanetaryGearSetCompoundModalAnalysis",
    "PlanetCarrierCompoundModalAnalysis",
    "PointLoadCompoundModalAnalysis",
    "PowerLoadCompoundModalAnalysis",
    "PulleyCompoundModalAnalysis",
    "RingPinsCompoundModalAnalysis",
    "RingPinsToDiscConnectionCompoundModalAnalysis",
    "RollingRingAssemblyCompoundModalAnalysis",
    "RollingRingCompoundModalAnalysis",
    "RollingRingConnectionCompoundModalAnalysis",
    "RootAssemblyCompoundModalAnalysis",
    "ShaftCompoundModalAnalysis",
    "ShaftHubConnectionCompoundModalAnalysis",
    "ShaftToMountableComponentConnectionCompoundModalAnalysis",
    "SpecialisedAssemblyCompoundModalAnalysis",
    "SpiralBevelGearCompoundModalAnalysis",
    "SpiralBevelGearMeshCompoundModalAnalysis",
    "SpiralBevelGearSetCompoundModalAnalysis",
    "SpringDamperCompoundModalAnalysis",
    "SpringDamperConnectionCompoundModalAnalysis",
    "SpringDamperHalfCompoundModalAnalysis",
    "StraightBevelDiffGearCompoundModalAnalysis",
    "StraightBevelDiffGearMeshCompoundModalAnalysis",
    "StraightBevelDiffGearSetCompoundModalAnalysis",
    "StraightBevelGearCompoundModalAnalysis",
    "StraightBevelGearMeshCompoundModalAnalysis",
    "StraightBevelGearSetCompoundModalAnalysis",
    "StraightBevelPlanetGearCompoundModalAnalysis",
    "StraightBevelSunGearCompoundModalAnalysis",
    "SynchroniserCompoundModalAnalysis",
    "SynchroniserHalfCompoundModalAnalysis",
    "SynchroniserPartCompoundModalAnalysis",
    "SynchroniserSleeveCompoundModalAnalysis",
    "TorqueConverterCompoundModalAnalysis",
    "TorqueConverterConnectionCompoundModalAnalysis",
    "TorqueConverterPumpCompoundModalAnalysis",
    "TorqueConverterTurbineCompoundModalAnalysis",
    "UnbalancedMassCompoundModalAnalysis",
    "VirtualComponentCompoundModalAnalysis",
    "WormGearCompoundModalAnalysis",
    "WormGearMeshCompoundModalAnalysis",
    "WormGearSetCompoundModalAnalysis",
    "ZerolBevelGearCompoundModalAnalysis",
    "ZerolBevelGearMeshCompoundModalAnalysis",
    "ZerolBevelGearSetCompoundModalAnalysis",
)

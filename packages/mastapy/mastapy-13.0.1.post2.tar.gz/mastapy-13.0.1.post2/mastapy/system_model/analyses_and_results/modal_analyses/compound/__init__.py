"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._4728 import AbstractAssemblyCompoundModalAnalysis
    from ._4729 import AbstractShaftCompoundModalAnalysis
    from ._4730 import AbstractShaftOrHousingCompoundModalAnalysis
    from ._4731 import AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4732 import AGMAGleasonConicalGearCompoundModalAnalysis
    from ._4733 import AGMAGleasonConicalGearMeshCompoundModalAnalysis
    from ._4734 import AGMAGleasonConicalGearSetCompoundModalAnalysis
    from ._4735 import AssemblyCompoundModalAnalysis
    from ._4736 import BearingCompoundModalAnalysis
    from ._4737 import BeltConnectionCompoundModalAnalysis
    from ._4738 import BeltDriveCompoundModalAnalysis
    from ._4739 import BevelDifferentialGearCompoundModalAnalysis
    from ._4740 import BevelDifferentialGearMeshCompoundModalAnalysis
    from ._4741 import BevelDifferentialGearSetCompoundModalAnalysis
    from ._4742 import BevelDifferentialPlanetGearCompoundModalAnalysis
    from ._4743 import BevelDifferentialSunGearCompoundModalAnalysis
    from ._4744 import BevelGearCompoundModalAnalysis
    from ._4745 import BevelGearMeshCompoundModalAnalysis
    from ._4746 import BevelGearSetCompoundModalAnalysis
    from ._4747 import BoltCompoundModalAnalysis
    from ._4748 import BoltedJointCompoundModalAnalysis
    from ._4749 import ClutchCompoundModalAnalysis
    from ._4750 import ClutchConnectionCompoundModalAnalysis
    from ._4751 import ClutchHalfCompoundModalAnalysis
    from ._4752 import CoaxialConnectionCompoundModalAnalysis
    from ._4753 import ComponentCompoundModalAnalysis
    from ._4754 import ConceptCouplingCompoundModalAnalysis
    from ._4755 import ConceptCouplingConnectionCompoundModalAnalysis
    from ._4756 import ConceptCouplingHalfCompoundModalAnalysis
    from ._4757 import ConceptGearCompoundModalAnalysis
    from ._4758 import ConceptGearMeshCompoundModalAnalysis
    from ._4759 import ConceptGearSetCompoundModalAnalysis
    from ._4760 import ConicalGearCompoundModalAnalysis
    from ._4761 import ConicalGearMeshCompoundModalAnalysis
    from ._4762 import ConicalGearSetCompoundModalAnalysis
    from ._4763 import ConnectionCompoundModalAnalysis
    from ._4764 import ConnectorCompoundModalAnalysis
    from ._4765 import CouplingCompoundModalAnalysis
    from ._4766 import CouplingConnectionCompoundModalAnalysis
    from ._4767 import CouplingHalfCompoundModalAnalysis
    from ._4768 import CVTBeltConnectionCompoundModalAnalysis
    from ._4769 import CVTCompoundModalAnalysis
    from ._4770 import CVTPulleyCompoundModalAnalysis
    from ._4771 import CycloidalAssemblyCompoundModalAnalysis
    from ._4772 import CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
    from ._4773 import CycloidalDiscCompoundModalAnalysis
    from ._4774 import CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis
    from ._4775 import CylindricalGearCompoundModalAnalysis
    from ._4776 import CylindricalGearMeshCompoundModalAnalysis
    from ._4777 import CylindricalGearSetCompoundModalAnalysis
    from ._4778 import CylindricalPlanetGearCompoundModalAnalysis
    from ._4779 import DatumCompoundModalAnalysis
    from ._4780 import ExternalCADModelCompoundModalAnalysis
    from ._4781 import FaceGearCompoundModalAnalysis
    from ._4782 import FaceGearMeshCompoundModalAnalysis
    from ._4783 import FaceGearSetCompoundModalAnalysis
    from ._4784 import FEPartCompoundModalAnalysis
    from ._4785 import FlexiblePinAssemblyCompoundModalAnalysis
    from ._4786 import GearCompoundModalAnalysis
    from ._4787 import GearMeshCompoundModalAnalysis
    from ._4788 import GearSetCompoundModalAnalysis
    from ._4789 import GuideDxfModelCompoundModalAnalysis
    from ._4790 import HypoidGearCompoundModalAnalysis
    from ._4791 import HypoidGearMeshCompoundModalAnalysis
    from ._4792 import HypoidGearSetCompoundModalAnalysis
    from ._4793 import InterMountableComponentConnectionCompoundModalAnalysis
    from ._4794 import KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
    from ._4795 import KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
    from ._4796 import KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
    from ._4797 import KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
    from ._4798 import KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
    from ._4799 import KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
    from ._4800 import KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
    from ._4801 import KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
    from ._4802 import KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
    from ._4803 import MassDiscCompoundModalAnalysis
    from ._4804 import MeasurementComponentCompoundModalAnalysis
    from ._4805 import MountableComponentCompoundModalAnalysis
    from ._4806 import OilSealCompoundModalAnalysis
    from ._4807 import PartCompoundModalAnalysis
    from ._4808 import PartToPartShearCouplingCompoundModalAnalysis
    from ._4809 import PartToPartShearCouplingConnectionCompoundModalAnalysis
    from ._4810 import PartToPartShearCouplingHalfCompoundModalAnalysis
    from ._4811 import PlanetaryConnectionCompoundModalAnalysis
    from ._4812 import PlanetaryGearSetCompoundModalAnalysis
    from ._4813 import PlanetCarrierCompoundModalAnalysis
    from ._4814 import PointLoadCompoundModalAnalysis
    from ._4815 import PowerLoadCompoundModalAnalysis
    from ._4816 import PulleyCompoundModalAnalysis
    from ._4817 import RingPinsCompoundModalAnalysis
    from ._4818 import RingPinsToDiscConnectionCompoundModalAnalysis
    from ._4819 import RollingRingAssemblyCompoundModalAnalysis
    from ._4820 import RollingRingCompoundModalAnalysis
    from ._4821 import RollingRingConnectionCompoundModalAnalysis
    from ._4822 import RootAssemblyCompoundModalAnalysis
    from ._4823 import ShaftCompoundModalAnalysis
    from ._4824 import ShaftHubConnectionCompoundModalAnalysis
    from ._4825 import ShaftToMountableComponentConnectionCompoundModalAnalysis
    from ._4826 import SpecialisedAssemblyCompoundModalAnalysis
    from ._4827 import SpiralBevelGearCompoundModalAnalysis
    from ._4828 import SpiralBevelGearMeshCompoundModalAnalysis
    from ._4829 import SpiralBevelGearSetCompoundModalAnalysis
    from ._4830 import SpringDamperCompoundModalAnalysis
    from ._4831 import SpringDamperConnectionCompoundModalAnalysis
    from ._4832 import SpringDamperHalfCompoundModalAnalysis
    from ._4833 import StraightBevelDiffGearCompoundModalAnalysis
    from ._4834 import StraightBevelDiffGearMeshCompoundModalAnalysis
    from ._4835 import StraightBevelDiffGearSetCompoundModalAnalysis
    from ._4836 import StraightBevelGearCompoundModalAnalysis
    from ._4837 import StraightBevelGearMeshCompoundModalAnalysis
    from ._4838 import StraightBevelGearSetCompoundModalAnalysis
    from ._4839 import StraightBevelPlanetGearCompoundModalAnalysis
    from ._4840 import StraightBevelSunGearCompoundModalAnalysis
    from ._4841 import SynchroniserCompoundModalAnalysis
    from ._4842 import SynchroniserHalfCompoundModalAnalysis
    from ._4843 import SynchroniserPartCompoundModalAnalysis
    from ._4844 import SynchroniserSleeveCompoundModalAnalysis
    from ._4845 import TorqueConverterCompoundModalAnalysis
    from ._4846 import TorqueConverterConnectionCompoundModalAnalysis
    from ._4847 import TorqueConverterPumpCompoundModalAnalysis
    from ._4848 import TorqueConverterTurbineCompoundModalAnalysis
    from ._4849 import UnbalancedMassCompoundModalAnalysis
    from ._4850 import VirtualComponentCompoundModalAnalysis
    from ._4851 import WormGearCompoundModalAnalysis
    from ._4852 import WormGearMeshCompoundModalAnalysis
    from ._4853 import WormGearSetCompoundModalAnalysis
    from ._4854 import ZerolBevelGearCompoundModalAnalysis
    from ._4855 import ZerolBevelGearMeshCompoundModalAnalysis
    from ._4856 import ZerolBevelGearSetCompoundModalAnalysis
else:
    import_structure = {
        "_4728": ["AbstractAssemblyCompoundModalAnalysis"],
        "_4729": ["AbstractShaftCompoundModalAnalysis"],
        "_4730": ["AbstractShaftOrHousingCompoundModalAnalysis"],
        "_4731": ["AbstractShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4732": ["AGMAGleasonConicalGearCompoundModalAnalysis"],
        "_4733": ["AGMAGleasonConicalGearMeshCompoundModalAnalysis"],
        "_4734": ["AGMAGleasonConicalGearSetCompoundModalAnalysis"],
        "_4735": ["AssemblyCompoundModalAnalysis"],
        "_4736": ["BearingCompoundModalAnalysis"],
        "_4737": ["BeltConnectionCompoundModalAnalysis"],
        "_4738": ["BeltDriveCompoundModalAnalysis"],
        "_4739": ["BevelDifferentialGearCompoundModalAnalysis"],
        "_4740": ["BevelDifferentialGearMeshCompoundModalAnalysis"],
        "_4741": ["BevelDifferentialGearSetCompoundModalAnalysis"],
        "_4742": ["BevelDifferentialPlanetGearCompoundModalAnalysis"],
        "_4743": ["BevelDifferentialSunGearCompoundModalAnalysis"],
        "_4744": ["BevelGearCompoundModalAnalysis"],
        "_4745": ["BevelGearMeshCompoundModalAnalysis"],
        "_4746": ["BevelGearSetCompoundModalAnalysis"],
        "_4747": ["BoltCompoundModalAnalysis"],
        "_4748": ["BoltedJointCompoundModalAnalysis"],
        "_4749": ["ClutchCompoundModalAnalysis"],
        "_4750": ["ClutchConnectionCompoundModalAnalysis"],
        "_4751": ["ClutchHalfCompoundModalAnalysis"],
        "_4752": ["CoaxialConnectionCompoundModalAnalysis"],
        "_4753": ["ComponentCompoundModalAnalysis"],
        "_4754": ["ConceptCouplingCompoundModalAnalysis"],
        "_4755": ["ConceptCouplingConnectionCompoundModalAnalysis"],
        "_4756": ["ConceptCouplingHalfCompoundModalAnalysis"],
        "_4757": ["ConceptGearCompoundModalAnalysis"],
        "_4758": ["ConceptGearMeshCompoundModalAnalysis"],
        "_4759": ["ConceptGearSetCompoundModalAnalysis"],
        "_4760": ["ConicalGearCompoundModalAnalysis"],
        "_4761": ["ConicalGearMeshCompoundModalAnalysis"],
        "_4762": ["ConicalGearSetCompoundModalAnalysis"],
        "_4763": ["ConnectionCompoundModalAnalysis"],
        "_4764": ["ConnectorCompoundModalAnalysis"],
        "_4765": ["CouplingCompoundModalAnalysis"],
        "_4766": ["CouplingConnectionCompoundModalAnalysis"],
        "_4767": ["CouplingHalfCompoundModalAnalysis"],
        "_4768": ["CVTBeltConnectionCompoundModalAnalysis"],
        "_4769": ["CVTCompoundModalAnalysis"],
        "_4770": ["CVTPulleyCompoundModalAnalysis"],
        "_4771": ["CycloidalAssemblyCompoundModalAnalysis"],
        "_4772": ["CycloidalDiscCentralBearingConnectionCompoundModalAnalysis"],
        "_4773": ["CycloidalDiscCompoundModalAnalysis"],
        "_4774": ["CycloidalDiscPlanetaryBearingConnectionCompoundModalAnalysis"],
        "_4775": ["CylindricalGearCompoundModalAnalysis"],
        "_4776": ["CylindricalGearMeshCompoundModalAnalysis"],
        "_4777": ["CylindricalGearSetCompoundModalAnalysis"],
        "_4778": ["CylindricalPlanetGearCompoundModalAnalysis"],
        "_4779": ["DatumCompoundModalAnalysis"],
        "_4780": ["ExternalCADModelCompoundModalAnalysis"],
        "_4781": ["FaceGearCompoundModalAnalysis"],
        "_4782": ["FaceGearMeshCompoundModalAnalysis"],
        "_4783": ["FaceGearSetCompoundModalAnalysis"],
        "_4784": ["FEPartCompoundModalAnalysis"],
        "_4785": ["FlexiblePinAssemblyCompoundModalAnalysis"],
        "_4786": ["GearCompoundModalAnalysis"],
        "_4787": ["GearMeshCompoundModalAnalysis"],
        "_4788": ["GearSetCompoundModalAnalysis"],
        "_4789": ["GuideDxfModelCompoundModalAnalysis"],
        "_4790": ["HypoidGearCompoundModalAnalysis"],
        "_4791": ["HypoidGearMeshCompoundModalAnalysis"],
        "_4792": ["HypoidGearSetCompoundModalAnalysis"],
        "_4793": ["InterMountableComponentConnectionCompoundModalAnalysis"],
        "_4794": ["KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis"],
        "_4795": ["KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis"],
        "_4796": ["KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis"],
        "_4797": ["KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis"],
        "_4798": ["KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis"],
        "_4799": ["KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis"],
        "_4800": ["KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis"],
        "_4801": ["KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis"],
        "_4802": ["KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis"],
        "_4803": ["MassDiscCompoundModalAnalysis"],
        "_4804": ["MeasurementComponentCompoundModalAnalysis"],
        "_4805": ["MountableComponentCompoundModalAnalysis"],
        "_4806": ["OilSealCompoundModalAnalysis"],
        "_4807": ["PartCompoundModalAnalysis"],
        "_4808": ["PartToPartShearCouplingCompoundModalAnalysis"],
        "_4809": ["PartToPartShearCouplingConnectionCompoundModalAnalysis"],
        "_4810": ["PartToPartShearCouplingHalfCompoundModalAnalysis"],
        "_4811": ["PlanetaryConnectionCompoundModalAnalysis"],
        "_4812": ["PlanetaryGearSetCompoundModalAnalysis"],
        "_4813": ["PlanetCarrierCompoundModalAnalysis"],
        "_4814": ["PointLoadCompoundModalAnalysis"],
        "_4815": ["PowerLoadCompoundModalAnalysis"],
        "_4816": ["PulleyCompoundModalAnalysis"],
        "_4817": ["RingPinsCompoundModalAnalysis"],
        "_4818": ["RingPinsToDiscConnectionCompoundModalAnalysis"],
        "_4819": ["RollingRingAssemblyCompoundModalAnalysis"],
        "_4820": ["RollingRingCompoundModalAnalysis"],
        "_4821": ["RollingRingConnectionCompoundModalAnalysis"],
        "_4822": ["RootAssemblyCompoundModalAnalysis"],
        "_4823": ["ShaftCompoundModalAnalysis"],
        "_4824": ["ShaftHubConnectionCompoundModalAnalysis"],
        "_4825": ["ShaftToMountableComponentConnectionCompoundModalAnalysis"],
        "_4826": ["SpecialisedAssemblyCompoundModalAnalysis"],
        "_4827": ["SpiralBevelGearCompoundModalAnalysis"],
        "_4828": ["SpiralBevelGearMeshCompoundModalAnalysis"],
        "_4829": ["SpiralBevelGearSetCompoundModalAnalysis"],
        "_4830": ["SpringDamperCompoundModalAnalysis"],
        "_4831": ["SpringDamperConnectionCompoundModalAnalysis"],
        "_4832": ["SpringDamperHalfCompoundModalAnalysis"],
        "_4833": ["StraightBevelDiffGearCompoundModalAnalysis"],
        "_4834": ["StraightBevelDiffGearMeshCompoundModalAnalysis"],
        "_4835": ["StraightBevelDiffGearSetCompoundModalAnalysis"],
        "_4836": ["StraightBevelGearCompoundModalAnalysis"],
        "_4837": ["StraightBevelGearMeshCompoundModalAnalysis"],
        "_4838": ["StraightBevelGearSetCompoundModalAnalysis"],
        "_4839": ["StraightBevelPlanetGearCompoundModalAnalysis"],
        "_4840": ["StraightBevelSunGearCompoundModalAnalysis"],
        "_4841": ["SynchroniserCompoundModalAnalysis"],
        "_4842": ["SynchroniserHalfCompoundModalAnalysis"],
        "_4843": ["SynchroniserPartCompoundModalAnalysis"],
        "_4844": ["SynchroniserSleeveCompoundModalAnalysis"],
        "_4845": ["TorqueConverterCompoundModalAnalysis"],
        "_4846": ["TorqueConverterConnectionCompoundModalAnalysis"],
        "_4847": ["TorqueConverterPumpCompoundModalAnalysis"],
        "_4848": ["TorqueConverterTurbineCompoundModalAnalysis"],
        "_4849": ["UnbalancedMassCompoundModalAnalysis"],
        "_4850": ["VirtualComponentCompoundModalAnalysis"],
        "_4851": ["WormGearCompoundModalAnalysis"],
        "_4852": ["WormGearMeshCompoundModalAnalysis"],
        "_4853": ["WormGearSetCompoundModalAnalysis"],
        "_4854": ["ZerolBevelGearCompoundModalAnalysis"],
        "_4855": ["ZerolBevelGearMeshCompoundModalAnalysis"],
        "_4856": ["ZerolBevelGearSetCompoundModalAnalysis"],
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

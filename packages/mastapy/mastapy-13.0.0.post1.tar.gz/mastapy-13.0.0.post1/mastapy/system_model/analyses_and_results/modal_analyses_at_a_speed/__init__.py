"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5116 import AbstractAssemblyModalAnalysisAtASpeed
    from ._5117 import AbstractShaftModalAnalysisAtASpeed
    from ._5118 import AbstractShaftOrHousingModalAnalysisAtASpeed
    from ._5119 import AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5120 import AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
    from ._5121 import AGMAGleasonConicalGearModalAnalysisAtASpeed
    from ._5122 import AGMAGleasonConicalGearSetModalAnalysisAtASpeed
    from ._5123 import AssemblyModalAnalysisAtASpeed
    from ._5124 import BearingModalAnalysisAtASpeed
    from ._5125 import BeltConnectionModalAnalysisAtASpeed
    from ._5126 import BeltDriveModalAnalysisAtASpeed
    from ._5127 import BevelDifferentialGearMeshModalAnalysisAtASpeed
    from ._5128 import BevelDifferentialGearModalAnalysisAtASpeed
    from ._5129 import BevelDifferentialGearSetModalAnalysisAtASpeed
    from ._5130 import BevelDifferentialPlanetGearModalAnalysisAtASpeed
    from ._5131 import BevelDifferentialSunGearModalAnalysisAtASpeed
    from ._5132 import BevelGearMeshModalAnalysisAtASpeed
    from ._5133 import BevelGearModalAnalysisAtASpeed
    from ._5134 import BevelGearSetModalAnalysisAtASpeed
    from ._5135 import BoltedJointModalAnalysisAtASpeed
    from ._5136 import BoltModalAnalysisAtASpeed
    from ._5137 import ClutchConnectionModalAnalysisAtASpeed
    from ._5138 import ClutchHalfModalAnalysisAtASpeed
    from ._5139 import ClutchModalAnalysisAtASpeed
    from ._5140 import CoaxialConnectionModalAnalysisAtASpeed
    from ._5141 import ComponentModalAnalysisAtASpeed
    from ._5142 import ConceptCouplingConnectionModalAnalysisAtASpeed
    from ._5143 import ConceptCouplingHalfModalAnalysisAtASpeed
    from ._5144 import ConceptCouplingModalAnalysisAtASpeed
    from ._5145 import ConceptGearMeshModalAnalysisAtASpeed
    from ._5146 import ConceptGearModalAnalysisAtASpeed
    from ._5147 import ConceptGearSetModalAnalysisAtASpeed
    from ._5148 import ConicalGearMeshModalAnalysisAtASpeed
    from ._5149 import ConicalGearModalAnalysisAtASpeed
    from ._5150 import ConicalGearSetModalAnalysisAtASpeed
    from ._5151 import ConnectionModalAnalysisAtASpeed
    from ._5152 import ConnectorModalAnalysisAtASpeed
    from ._5153 import CouplingConnectionModalAnalysisAtASpeed
    from ._5154 import CouplingHalfModalAnalysisAtASpeed
    from ._5155 import CouplingModalAnalysisAtASpeed
    from ._5156 import CVTBeltConnectionModalAnalysisAtASpeed
    from ._5157 import CVTModalAnalysisAtASpeed
    from ._5158 import CVTPulleyModalAnalysisAtASpeed
    from ._5159 import CycloidalAssemblyModalAnalysisAtASpeed
    from ._5160 import CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
    from ._5161 import CycloidalDiscModalAnalysisAtASpeed
    from ._5162 import CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
    from ._5163 import CylindricalGearMeshModalAnalysisAtASpeed
    from ._5164 import CylindricalGearModalAnalysisAtASpeed
    from ._5165 import CylindricalGearSetModalAnalysisAtASpeed
    from ._5166 import CylindricalPlanetGearModalAnalysisAtASpeed
    from ._5167 import DatumModalAnalysisAtASpeed
    from ._5168 import ExternalCADModelModalAnalysisAtASpeed
    from ._5169 import FaceGearMeshModalAnalysisAtASpeed
    from ._5170 import FaceGearModalAnalysisAtASpeed
    from ._5171 import FaceGearSetModalAnalysisAtASpeed
    from ._5172 import FEPartModalAnalysisAtASpeed
    from ._5173 import FlexiblePinAssemblyModalAnalysisAtASpeed
    from ._5174 import GearMeshModalAnalysisAtASpeed
    from ._5175 import GearModalAnalysisAtASpeed
    from ._5176 import GearSetModalAnalysisAtASpeed
    from ._5177 import GuideDxfModelModalAnalysisAtASpeed
    from ._5178 import HypoidGearMeshModalAnalysisAtASpeed
    from ._5179 import HypoidGearModalAnalysisAtASpeed
    from ._5180 import HypoidGearSetModalAnalysisAtASpeed
    from ._5181 import InterMountableComponentConnectionModalAnalysisAtASpeed
    from ._5182 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
    from ._5183 import KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
    from ._5184 import KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
    from ._5185 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
    from ._5186 import KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
    from ._5187 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
    from ._5188 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5189 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
    from ._5190 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
    from ._5191 import MassDiscModalAnalysisAtASpeed
    from ._5192 import MeasurementComponentModalAnalysisAtASpeed
    from ._5193 import ModalAnalysisAtASpeed
    from ._5194 import MountableComponentModalAnalysisAtASpeed
    from ._5195 import OilSealModalAnalysisAtASpeed
    from ._5196 import PartModalAnalysisAtASpeed
    from ._5197 import PartToPartShearCouplingConnectionModalAnalysisAtASpeed
    from ._5198 import PartToPartShearCouplingHalfModalAnalysisAtASpeed
    from ._5199 import PartToPartShearCouplingModalAnalysisAtASpeed
    from ._5200 import PlanetaryConnectionModalAnalysisAtASpeed
    from ._5201 import PlanetaryGearSetModalAnalysisAtASpeed
    from ._5202 import PlanetCarrierModalAnalysisAtASpeed
    from ._5203 import PointLoadModalAnalysisAtASpeed
    from ._5204 import PowerLoadModalAnalysisAtASpeed
    from ._5205 import PulleyModalAnalysisAtASpeed
    from ._5206 import RingPinsModalAnalysisAtASpeed
    from ._5207 import RingPinsToDiscConnectionModalAnalysisAtASpeed
    from ._5208 import RollingRingAssemblyModalAnalysisAtASpeed
    from ._5209 import RollingRingConnectionModalAnalysisAtASpeed
    from ._5210 import RollingRingModalAnalysisAtASpeed
    from ._5211 import RootAssemblyModalAnalysisAtASpeed
    from ._5212 import ShaftHubConnectionModalAnalysisAtASpeed
    from ._5213 import ShaftModalAnalysisAtASpeed
    from ._5214 import ShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5215 import SpecialisedAssemblyModalAnalysisAtASpeed
    from ._5216 import SpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5217 import SpiralBevelGearModalAnalysisAtASpeed
    from ._5218 import SpiralBevelGearSetModalAnalysisAtASpeed
    from ._5219 import SpringDamperConnectionModalAnalysisAtASpeed
    from ._5220 import SpringDamperHalfModalAnalysisAtASpeed
    from ._5221 import SpringDamperModalAnalysisAtASpeed
    from ._5222 import StraightBevelDiffGearMeshModalAnalysisAtASpeed
    from ._5223 import StraightBevelDiffGearModalAnalysisAtASpeed
    from ._5224 import StraightBevelDiffGearSetModalAnalysisAtASpeed
    from ._5225 import StraightBevelGearMeshModalAnalysisAtASpeed
    from ._5226 import StraightBevelGearModalAnalysisAtASpeed
    from ._5227 import StraightBevelGearSetModalAnalysisAtASpeed
    from ._5228 import StraightBevelPlanetGearModalAnalysisAtASpeed
    from ._5229 import StraightBevelSunGearModalAnalysisAtASpeed
    from ._5230 import SynchroniserHalfModalAnalysisAtASpeed
    from ._5231 import SynchroniserModalAnalysisAtASpeed
    from ._5232 import SynchroniserPartModalAnalysisAtASpeed
    from ._5233 import SynchroniserSleeveModalAnalysisAtASpeed
    from ._5234 import TorqueConverterConnectionModalAnalysisAtASpeed
    from ._5235 import TorqueConverterModalAnalysisAtASpeed
    from ._5236 import TorqueConverterPumpModalAnalysisAtASpeed
    from ._5237 import TorqueConverterTurbineModalAnalysisAtASpeed
    from ._5238 import UnbalancedMassModalAnalysisAtASpeed
    from ._5239 import VirtualComponentModalAnalysisAtASpeed
    from ._5240 import WormGearMeshModalAnalysisAtASpeed
    from ._5241 import WormGearModalAnalysisAtASpeed
    from ._5242 import WormGearSetModalAnalysisAtASpeed
    from ._5243 import ZerolBevelGearMeshModalAnalysisAtASpeed
    from ._5244 import ZerolBevelGearModalAnalysisAtASpeed
    from ._5245 import ZerolBevelGearSetModalAnalysisAtASpeed
else:
    import_structure = {
        "_5116": ["AbstractAssemblyModalAnalysisAtASpeed"],
        "_5117": ["AbstractShaftModalAnalysisAtASpeed"],
        "_5118": ["AbstractShaftOrHousingModalAnalysisAtASpeed"],
        "_5119": ["AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5120": ["AGMAGleasonConicalGearMeshModalAnalysisAtASpeed"],
        "_5121": ["AGMAGleasonConicalGearModalAnalysisAtASpeed"],
        "_5122": ["AGMAGleasonConicalGearSetModalAnalysisAtASpeed"],
        "_5123": ["AssemblyModalAnalysisAtASpeed"],
        "_5124": ["BearingModalAnalysisAtASpeed"],
        "_5125": ["BeltConnectionModalAnalysisAtASpeed"],
        "_5126": ["BeltDriveModalAnalysisAtASpeed"],
        "_5127": ["BevelDifferentialGearMeshModalAnalysisAtASpeed"],
        "_5128": ["BevelDifferentialGearModalAnalysisAtASpeed"],
        "_5129": ["BevelDifferentialGearSetModalAnalysisAtASpeed"],
        "_5130": ["BevelDifferentialPlanetGearModalAnalysisAtASpeed"],
        "_5131": ["BevelDifferentialSunGearModalAnalysisAtASpeed"],
        "_5132": ["BevelGearMeshModalAnalysisAtASpeed"],
        "_5133": ["BevelGearModalAnalysisAtASpeed"],
        "_5134": ["BevelGearSetModalAnalysisAtASpeed"],
        "_5135": ["BoltedJointModalAnalysisAtASpeed"],
        "_5136": ["BoltModalAnalysisAtASpeed"],
        "_5137": ["ClutchConnectionModalAnalysisAtASpeed"],
        "_5138": ["ClutchHalfModalAnalysisAtASpeed"],
        "_5139": ["ClutchModalAnalysisAtASpeed"],
        "_5140": ["CoaxialConnectionModalAnalysisAtASpeed"],
        "_5141": ["ComponentModalAnalysisAtASpeed"],
        "_5142": ["ConceptCouplingConnectionModalAnalysisAtASpeed"],
        "_5143": ["ConceptCouplingHalfModalAnalysisAtASpeed"],
        "_5144": ["ConceptCouplingModalAnalysisAtASpeed"],
        "_5145": ["ConceptGearMeshModalAnalysisAtASpeed"],
        "_5146": ["ConceptGearModalAnalysisAtASpeed"],
        "_5147": ["ConceptGearSetModalAnalysisAtASpeed"],
        "_5148": ["ConicalGearMeshModalAnalysisAtASpeed"],
        "_5149": ["ConicalGearModalAnalysisAtASpeed"],
        "_5150": ["ConicalGearSetModalAnalysisAtASpeed"],
        "_5151": ["ConnectionModalAnalysisAtASpeed"],
        "_5152": ["ConnectorModalAnalysisAtASpeed"],
        "_5153": ["CouplingConnectionModalAnalysisAtASpeed"],
        "_5154": ["CouplingHalfModalAnalysisAtASpeed"],
        "_5155": ["CouplingModalAnalysisAtASpeed"],
        "_5156": ["CVTBeltConnectionModalAnalysisAtASpeed"],
        "_5157": ["CVTModalAnalysisAtASpeed"],
        "_5158": ["CVTPulleyModalAnalysisAtASpeed"],
        "_5159": ["CycloidalAssemblyModalAnalysisAtASpeed"],
        "_5160": ["CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed"],
        "_5161": ["CycloidalDiscModalAnalysisAtASpeed"],
        "_5162": ["CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed"],
        "_5163": ["CylindricalGearMeshModalAnalysisAtASpeed"],
        "_5164": ["CylindricalGearModalAnalysisAtASpeed"],
        "_5165": ["CylindricalGearSetModalAnalysisAtASpeed"],
        "_5166": ["CylindricalPlanetGearModalAnalysisAtASpeed"],
        "_5167": ["DatumModalAnalysisAtASpeed"],
        "_5168": ["ExternalCADModelModalAnalysisAtASpeed"],
        "_5169": ["FaceGearMeshModalAnalysisAtASpeed"],
        "_5170": ["FaceGearModalAnalysisAtASpeed"],
        "_5171": ["FaceGearSetModalAnalysisAtASpeed"],
        "_5172": ["FEPartModalAnalysisAtASpeed"],
        "_5173": ["FlexiblePinAssemblyModalAnalysisAtASpeed"],
        "_5174": ["GearMeshModalAnalysisAtASpeed"],
        "_5175": ["GearModalAnalysisAtASpeed"],
        "_5176": ["GearSetModalAnalysisAtASpeed"],
        "_5177": ["GuideDxfModelModalAnalysisAtASpeed"],
        "_5178": ["HypoidGearMeshModalAnalysisAtASpeed"],
        "_5179": ["HypoidGearModalAnalysisAtASpeed"],
        "_5180": ["HypoidGearSetModalAnalysisAtASpeed"],
        "_5181": ["InterMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5182": ["KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed"],
        "_5183": ["KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed"],
        "_5184": ["KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed"],
        "_5185": ["KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed"],
        "_5186": ["KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed"],
        "_5187": ["KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed"],
        "_5188": ["KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5189": ["KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed"],
        "_5190": ["KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5191": ["MassDiscModalAnalysisAtASpeed"],
        "_5192": ["MeasurementComponentModalAnalysisAtASpeed"],
        "_5193": ["ModalAnalysisAtASpeed"],
        "_5194": ["MountableComponentModalAnalysisAtASpeed"],
        "_5195": ["OilSealModalAnalysisAtASpeed"],
        "_5196": ["PartModalAnalysisAtASpeed"],
        "_5197": ["PartToPartShearCouplingConnectionModalAnalysisAtASpeed"],
        "_5198": ["PartToPartShearCouplingHalfModalAnalysisAtASpeed"],
        "_5199": ["PartToPartShearCouplingModalAnalysisAtASpeed"],
        "_5200": ["PlanetaryConnectionModalAnalysisAtASpeed"],
        "_5201": ["PlanetaryGearSetModalAnalysisAtASpeed"],
        "_5202": ["PlanetCarrierModalAnalysisAtASpeed"],
        "_5203": ["PointLoadModalAnalysisAtASpeed"],
        "_5204": ["PowerLoadModalAnalysisAtASpeed"],
        "_5205": ["PulleyModalAnalysisAtASpeed"],
        "_5206": ["RingPinsModalAnalysisAtASpeed"],
        "_5207": ["RingPinsToDiscConnectionModalAnalysisAtASpeed"],
        "_5208": ["RollingRingAssemblyModalAnalysisAtASpeed"],
        "_5209": ["RollingRingConnectionModalAnalysisAtASpeed"],
        "_5210": ["RollingRingModalAnalysisAtASpeed"],
        "_5211": ["RootAssemblyModalAnalysisAtASpeed"],
        "_5212": ["ShaftHubConnectionModalAnalysisAtASpeed"],
        "_5213": ["ShaftModalAnalysisAtASpeed"],
        "_5214": ["ShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5215": ["SpecialisedAssemblyModalAnalysisAtASpeed"],
        "_5216": ["SpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5217": ["SpiralBevelGearModalAnalysisAtASpeed"],
        "_5218": ["SpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5219": ["SpringDamperConnectionModalAnalysisAtASpeed"],
        "_5220": ["SpringDamperHalfModalAnalysisAtASpeed"],
        "_5221": ["SpringDamperModalAnalysisAtASpeed"],
        "_5222": ["StraightBevelDiffGearMeshModalAnalysisAtASpeed"],
        "_5223": ["StraightBevelDiffGearModalAnalysisAtASpeed"],
        "_5224": ["StraightBevelDiffGearSetModalAnalysisAtASpeed"],
        "_5225": ["StraightBevelGearMeshModalAnalysisAtASpeed"],
        "_5226": ["StraightBevelGearModalAnalysisAtASpeed"],
        "_5227": ["StraightBevelGearSetModalAnalysisAtASpeed"],
        "_5228": ["StraightBevelPlanetGearModalAnalysisAtASpeed"],
        "_5229": ["StraightBevelSunGearModalAnalysisAtASpeed"],
        "_5230": ["SynchroniserHalfModalAnalysisAtASpeed"],
        "_5231": ["SynchroniserModalAnalysisAtASpeed"],
        "_5232": ["SynchroniserPartModalAnalysisAtASpeed"],
        "_5233": ["SynchroniserSleeveModalAnalysisAtASpeed"],
        "_5234": ["TorqueConverterConnectionModalAnalysisAtASpeed"],
        "_5235": ["TorqueConverterModalAnalysisAtASpeed"],
        "_5236": ["TorqueConverterPumpModalAnalysisAtASpeed"],
        "_5237": ["TorqueConverterTurbineModalAnalysisAtASpeed"],
        "_5238": ["UnbalancedMassModalAnalysisAtASpeed"],
        "_5239": ["VirtualComponentModalAnalysisAtASpeed"],
        "_5240": ["WormGearMeshModalAnalysisAtASpeed"],
        "_5241": ["WormGearModalAnalysisAtASpeed"],
        "_5242": ["WormGearSetModalAnalysisAtASpeed"],
        "_5243": ["ZerolBevelGearMeshModalAnalysisAtASpeed"],
        "_5244": ["ZerolBevelGearModalAnalysisAtASpeed"],
        "_5245": ["ZerolBevelGearSetModalAnalysisAtASpeed"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyModalAnalysisAtASpeed",
    "AbstractShaftModalAnalysisAtASpeed",
    "AbstractShaftOrHousingModalAnalysisAtASpeed",
    "AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearMeshModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearModalAnalysisAtASpeed",
    "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
    "AssemblyModalAnalysisAtASpeed",
    "BearingModalAnalysisAtASpeed",
    "BeltConnectionModalAnalysisAtASpeed",
    "BeltDriveModalAnalysisAtASpeed",
    "BevelDifferentialGearMeshModalAnalysisAtASpeed",
    "BevelDifferentialGearModalAnalysisAtASpeed",
    "BevelDifferentialGearSetModalAnalysisAtASpeed",
    "BevelDifferentialPlanetGearModalAnalysisAtASpeed",
    "BevelDifferentialSunGearModalAnalysisAtASpeed",
    "BevelGearMeshModalAnalysisAtASpeed",
    "BevelGearModalAnalysisAtASpeed",
    "BevelGearSetModalAnalysisAtASpeed",
    "BoltedJointModalAnalysisAtASpeed",
    "BoltModalAnalysisAtASpeed",
    "ClutchConnectionModalAnalysisAtASpeed",
    "ClutchHalfModalAnalysisAtASpeed",
    "ClutchModalAnalysisAtASpeed",
    "CoaxialConnectionModalAnalysisAtASpeed",
    "ComponentModalAnalysisAtASpeed",
    "ConceptCouplingConnectionModalAnalysisAtASpeed",
    "ConceptCouplingHalfModalAnalysisAtASpeed",
    "ConceptCouplingModalAnalysisAtASpeed",
    "ConceptGearMeshModalAnalysisAtASpeed",
    "ConceptGearModalAnalysisAtASpeed",
    "ConceptGearSetModalAnalysisAtASpeed",
    "ConicalGearMeshModalAnalysisAtASpeed",
    "ConicalGearModalAnalysisAtASpeed",
    "ConicalGearSetModalAnalysisAtASpeed",
    "ConnectionModalAnalysisAtASpeed",
    "ConnectorModalAnalysisAtASpeed",
    "CouplingConnectionModalAnalysisAtASpeed",
    "CouplingHalfModalAnalysisAtASpeed",
    "CouplingModalAnalysisAtASpeed",
    "CVTBeltConnectionModalAnalysisAtASpeed",
    "CVTModalAnalysisAtASpeed",
    "CVTPulleyModalAnalysisAtASpeed",
    "CycloidalAssemblyModalAnalysisAtASpeed",
    "CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed",
    "CycloidalDiscModalAnalysisAtASpeed",
    "CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed",
    "CylindricalGearMeshModalAnalysisAtASpeed",
    "CylindricalGearModalAnalysisAtASpeed",
    "CylindricalGearSetModalAnalysisAtASpeed",
    "CylindricalPlanetGearModalAnalysisAtASpeed",
    "DatumModalAnalysisAtASpeed",
    "ExternalCADModelModalAnalysisAtASpeed",
    "FaceGearMeshModalAnalysisAtASpeed",
    "FaceGearModalAnalysisAtASpeed",
    "FaceGearSetModalAnalysisAtASpeed",
    "FEPartModalAnalysisAtASpeed",
    "FlexiblePinAssemblyModalAnalysisAtASpeed",
    "GearMeshModalAnalysisAtASpeed",
    "GearModalAnalysisAtASpeed",
    "GearSetModalAnalysisAtASpeed",
    "GuideDxfModelModalAnalysisAtASpeed",
    "HypoidGearMeshModalAnalysisAtASpeed",
    "HypoidGearModalAnalysisAtASpeed",
    "HypoidGearSetModalAnalysisAtASpeed",
    "InterMountableComponentConnectionModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed",
    "KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed",
    "MassDiscModalAnalysisAtASpeed",
    "MeasurementComponentModalAnalysisAtASpeed",
    "ModalAnalysisAtASpeed",
    "MountableComponentModalAnalysisAtASpeed",
    "OilSealModalAnalysisAtASpeed",
    "PartModalAnalysisAtASpeed",
    "PartToPartShearCouplingConnectionModalAnalysisAtASpeed",
    "PartToPartShearCouplingHalfModalAnalysisAtASpeed",
    "PartToPartShearCouplingModalAnalysisAtASpeed",
    "PlanetaryConnectionModalAnalysisAtASpeed",
    "PlanetaryGearSetModalAnalysisAtASpeed",
    "PlanetCarrierModalAnalysisAtASpeed",
    "PointLoadModalAnalysisAtASpeed",
    "PowerLoadModalAnalysisAtASpeed",
    "PulleyModalAnalysisAtASpeed",
    "RingPinsModalAnalysisAtASpeed",
    "RingPinsToDiscConnectionModalAnalysisAtASpeed",
    "RollingRingAssemblyModalAnalysisAtASpeed",
    "RollingRingConnectionModalAnalysisAtASpeed",
    "RollingRingModalAnalysisAtASpeed",
    "RootAssemblyModalAnalysisAtASpeed",
    "ShaftHubConnectionModalAnalysisAtASpeed",
    "ShaftModalAnalysisAtASpeed",
    "ShaftToMountableComponentConnectionModalAnalysisAtASpeed",
    "SpecialisedAssemblyModalAnalysisAtASpeed",
    "SpiralBevelGearMeshModalAnalysisAtASpeed",
    "SpiralBevelGearModalAnalysisAtASpeed",
    "SpiralBevelGearSetModalAnalysisAtASpeed",
    "SpringDamperConnectionModalAnalysisAtASpeed",
    "SpringDamperHalfModalAnalysisAtASpeed",
    "SpringDamperModalAnalysisAtASpeed",
    "StraightBevelDiffGearMeshModalAnalysisAtASpeed",
    "StraightBevelDiffGearModalAnalysisAtASpeed",
    "StraightBevelDiffGearSetModalAnalysisAtASpeed",
    "StraightBevelGearMeshModalAnalysisAtASpeed",
    "StraightBevelGearModalAnalysisAtASpeed",
    "StraightBevelGearSetModalAnalysisAtASpeed",
    "StraightBevelPlanetGearModalAnalysisAtASpeed",
    "StraightBevelSunGearModalAnalysisAtASpeed",
    "SynchroniserHalfModalAnalysisAtASpeed",
    "SynchroniserModalAnalysisAtASpeed",
    "SynchroniserPartModalAnalysisAtASpeed",
    "SynchroniserSleeveModalAnalysisAtASpeed",
    "TorqueConverterConnectionModalAnalysisAtASpeed",
    "TorqueConverterModalAnalysisAtASpeed",
    "TorqueConverterPumpModalAnalysisAtASpeed",
    "TorqueConverterTurbineModalAnalysisAtASpeed",
    "UnbalancedMassModalAnalysisAtASpeed",
    "VirtualComponentModalAnalysisAtASpeed",
    "WormGearMeshModalAnalysisAtASpeed",
    "WormGearModalAnalysisAtASpeed",
    "WormGearSetModalAnalysisAtASpeed",
    "ZerolBevelGearMeshModalAnalysisAtASpeed",
    "ZerolBevelGearModalAnalysisAtASpeed",
    "ZerolBevelGearSetModalAnalysisAtASpeed",
)

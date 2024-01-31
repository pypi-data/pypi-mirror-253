"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._5117 import AbstractAssemblyModalAnalysisAtASpeed
    from ._5118 import AbstractShaftModalAnalysisAtASpeed
    from ._5119 import AbstractShaftOrHousingModalAnalysisAtASpeed
    from ._5120 import AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5121 import AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
    from ._5122 import AGMAGleasonConicalGearModalAnalysisAtASpeed
    from ._5123 import AGMAGleasonConicalGearSetModalAnalysisAtASpeed
    from ._5124 import AssemblyModalAnalysisAtASpeed
    from ._5125 import BearingModalAnalysisAtASpeed
    from ._5126 import BeltConnectionModalAnalysisAtASpeed
    from ._5127 import BeltDriveModalAnalysisAtASpeed
    from ._5128 import BevelDifferentialGearMeshModalAnalysisAtASpeed
    from ._5129 import BevelDifferentialGearModalAnalysisAtASpeed
    from ._5130 import BevelDifferentialGearSetModalAnalysisAtASpeed
    from ._5131 import BevelDifferentialPlanetGearModalAnalysisAtASpeed
    from ._5132 import BevelDifferentialSunGearModalAnalysisAtASpeed
    from ._5133 import BevelGearMeshModalAnalysisAtASpeed
    from ._5134 import BevelGearModalAnalysisAtASpeed
    from ._5135 import BevelGearSetModalAnalysisAtASpeed
    from ._5136 import BoltedJointModalAnalysisAtASpeed
    from ._5137 import BoltModalAnalysisAtASpeed
    from ._5138 import ClutchConnectionModalAnalysisAtASpeed
    from ._5139 import ClutchHalfModalAnalysisAtASpeed
    from ._5140 import ClutchModalAnalysisAtASpeed
    from ._5141 import CoaxialConnectionModalAnalysisAtASpeed
    from ._5142 import ComponentModalAnalysisAtASpeed
    from ._5143 import ConceptCouplingConnectionModalAnalysisAtASpeed
    from ._5144 import ConceptCouplingHalfModalAnalysisAtASpeed
    from ._5145 import ConceptCouplingModalAnalysisAtASpeed
    from ._5146 import ConceptGearMeshModalAnalysisAtASpeed
    from ._5147 import ConceptGearModalAnalysisAtASpeed
    from ._5148 import ConceptGearSetModalAnalysisAtASpeed
    from ._5149 import ConicalGearMeshModalAnalysisAtASpeed
    from ._5150 import ConicalGearModalAnalysisAtASpeed
    from ._5151 import ConicalGearSetModalAnalysisAtASpeed
    from ._5152 import ConnectionModalAnalysisAtASpeed
    from ._5153 import ConnectorModalAnalysisAtASpeed
    from ._5154 import CouplingConnectionModalAnalysisAtASpeed
    from ._5155 import CouplingHalfModalAnalysisAtASpeed
    from ._5156 import CouplingModalAnalysisAtASpeed
    from ._5157 import CVTBeltConnectionModalAnalysisAtASpeed
    from ._5158 import CVTModalAnalysisAtASpeed
    from ._5159 import CVTPulleyModalAnalysisAtASpeed
    from ._5160 import CycloidalAssemblyModalAnalysisAtASpeed
    from ._5161 import CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed
    from ._5162 import CycloidalDiscModalAnalysisAtASpeed
    from ._5163 import CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed
    from ._5164 import CylindricalGearMeshModalAnalysisAtASpeed
    from ._5165 import CylindricalGearModalAnalysisAtASpeed
    from ._5166 import CylindricalGearSetModalAnalysisAtASpeed
    from ._5167 import CylindricalPlanetGearModalAnalysisAtASpeed
    from ._5168 import DatumModalAnalysisAtASpeed
    from ._5169 import ExternalCADModelModalAnalysisAtASpeed
    from ._5170 import FaceGearMeshModalAnalysisAtASpeed
    from ._5171 import FaceGearModalAnalysisAtASpeed
    from ._5172 import FaceGearSetModalAnalysisAtASpeed
    from ._5173 import FEPartModalAnalysisAtASpeed
    from ._5174 import FlexiblePinAssemblyModalAnalysisAtASpeed
    from ._5175 import GearMeshModalAnalysisAtASpeed
    from ._5176 import GearModalAnalysisAtASpeed
    from ._5177 import GearSetModalAnalysisAtASpeed
    from ._5178 import GuideDxfModelModalAnalysisAtASpeed
    from ._5179 import HypoidGearMeshModalAnalysisAtASpeed
    from ._5180 import HypoidGearModalAnalysisAtASpeed
    from ._5181 import HypoidGearSetModalAnalysisAtASpeed
    from ._5182 import InterMountableComponentConnectionModalAnalysisAtASpeed
    from ._5183 import KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
    from ._5184 import KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed
    from ._5185 import KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed
    from ._5186 import KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
    from ._5187 import KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
    from ._5188 import KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed
    from ._5189 import KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5190 import KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
    from ._5191 import KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed
    from ._5192 import MassDiscModalAnalysisAtASpeed
    from ._5193 import MeasurementComponentModalAnalysisAtASpeed
    from ._5194 import ModalAnalysisAtASpeed
    from ._5195 import MountableComponentModalAnalysisAtASpeed
    from ._5196 import OilSealModalAnalysisAtASpeed
    from ._5197 import PartModalAnalysisAtASpeed
    from ._5198 import PartToPartShearCouplingConnectionModalAnalysisAtASpeed
    from ._5199 import PartToPartShearCouplingHalfModalAnalysisAtASpeed
    from ._5200 import PartToPartShearCouplingModalAnalysisAtASpeed
    from ._5201 import PlanetaryConnectionModalAnalysisAtASpeed
    from ._5202 import PlanetaryGearSetModalAnalysisAtASpeed
    from ._5203 import PlanetCarrierModalAnalysisAtASpeed
    from ._5204 import PointLoadModalAnalysisAtASpeed
    from ._5205 import PowerLoadModalAnalysisAtASpeed
    from ._5206 import PulleyModalAnalysisAtASpeed
    from ._5207 import RingPinsModalAnalysisAtASpeed
    from ._5208 import RingPinsToDiscConnectionModalAnalysisAtASpeed
    from ._5209 import RollingRingAssemblyModalAnalysisAtASpeed
    from ._5210 import RollingRingConnectionModalAnalysisAtASpeed
    from ._5211 import RollingRingModalAnalysisAtASpeed
    from ._5212 import RootAssemblyModalAnalysisAtASpeed
    from ._5213 import ShaftHubConnectionModalAnalysisAtASpeed
    from ._5214 import ShaftModalAnalysisAtASpeed
    from ._5215 import ShaftToMountableComponentConnectionModalAnalysisAtASpeed
    from ._5216 import SpecialisedAssemblyModalAnalysisAtASpeed
    from ._5217 import SpiralBevelGearMeshModalAnalysisAtASpeed
    from ._5218 import SpiralBevelGearModalAnalysisAtASpeed
    from ._5219 import SpiralBevelGearSetModalAnalysisAtASpeed
    from ._5220 import SpringDamperConnectionModalAnalysisAtASpeed
    from ._5221 import SpringDamperHalfModalAnalysisAtASpeed
    from ._5222 import SpringDamperModalAnalysisAtASpeed
    from ._5223 import StraightBevelDiffGearMeshModalAnalysisAtASpeed
    from ._5224 import StraightBevelDiffGearModalAnalysisAtASpeed
    from ._5225 import StraightBevelDiffGearSetModalAnalysisAtASpeed
    from ._5226 import StraightBevelGearMeshModalAnalysisAtASpeed
    from ._5227 import StraightBevelGearModalAnalysisAtASpeed
    from ._5228 import StraightBevelGearSetModalAnalysisAtASpeed
    from ._5229 import StraightBevelPlanetGearModalAnalysisAtASpeed
    from ._5230 import StraightBevelSunGearModalAnalysisAtASpeed
    from ._5231 import SynchroniserHalfModalAnalysisAtASpeed
    from ._5232 import SynchroniserModalAnalysisAtASpeed
    from ._5233 import SynchroniserPartModalAnalysisAtASpeed
    from ._5234 import SynchroniserSleeveModalAnalysisAtASpeed
    from ._5235 import TorqueConverterConnectionModalAnalysisAtASpeed
    from ._5236 import TorqueConverterModalAnalysisAtASpeed
    from ._5237 import TorqueConverterPumpModalAnalysisAtASpeed
    from ._5238 import TorqueConverterTurbineModalAnalysisAtASpeed
    from ._5239 import UnbalancedMassModalAnalysisAtASpeed
    from ._5240 import VirtualComponentModalAnalysisAtASpeed
    from ._5241 import WormGearMeshModalAnalysisAtASpeed
    from ._5242 import WormGearModalAnalysisAtASpeed
    from ._5243 import WormGearSetModalAnalysisAtASpeed
    from ._5244 import ZerolBevelGearMeshModalAnalysisAtASpeed
    from ._5245 import ZerolBevelGearModalAnalysisAtASpeed
    from ._5246 import ZerolBevelGearSetModalAnalysisAtASpeed
else:
    import_structure = {
        "_5117": ["AbstractAssemblyModalAnalysisAtASpeed"],
        "_5118": ["AbstractShaftModalAnalysisAtASpeed"],
        "_5119": ["AbstractShaftOrHousingModalAnalysisAtASpeed"],
        "_5120": ["AbstractShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5121": ["AGMAGleasonConicalGearMeshModalAnalysisAtASpeed"],
        "_5122": ["AGMAGleasonConicalGearModalAnalysisAtASpeed"],
        "_5123": ["AGMAGleasonConicalGearSetModalAnalysisAtASpeed"],
        "_5124": ["AssemblyModalAnalysisAtASpeed"],
        "_5125": ["BearingModalAnalysisAtASpeed"],
        "_5126": ["BeltConnectionModalAnalysisAtASpeed"],
        "_5127": ["BeltDriveModalAnalysisAtASpeed"],
        "_5128": ["BevelDifferentialGearMeshModalAnalysisAtASpeed"],
        "_5129": ["BevelDifferentialGearModalAnalysisAtASpeed"],
        "_5130": ["BevelDifferentialGearSetModalAnalysisAtASpeed"],
        "_5131": ["BevelDifferentialPlanetGearModalAnalysisAtASpeed"],
        "_5132": ["BevelDifferentialSunGearModalAnalysisAtASpeed"],
        "_5133": ["BevelGearMeshModalAnalysisAtASpeed"],
        "_5134": ["BevelGearModalAnalysisAtASpeed"],
        "_5135": ["BevelGearSetModalAnalysisAtASpeed"],
        "_5136": ["BoltedJointModalAnalysisAtASpeed"],
        "_5137": ["BoltModalAnalysisAtASpeed"],
        "_5138": ["ClutchConnectionModalAnalysisAtASpeed"],
        "_5139": ["ClutchHalfModalAnalysisAtASpeed"],
        "_5140": ["ClutchModalAnalysisAtASpeed"],
        "_5141": ["CoaxialConnectionModalAnalysisAtASpeed"],
        "_5142": ["ComponentModalAnalysisAtASpeed"],
        "_5143": ["ConceptCouplingConnectionModalAnalysisAtASpeed"],
        "_5144": ["ConceptCouplingHalfModalAnalysisAtASpeed"],
        "_5145": ["ConceptCouplingModalAnalysisAtASpeed"],
        "_5146": ["ConceptGearMeshModalAnalysisAtASpeed"],
        "_5147": ["ConceptGearModalAnalysisAtASpeed"],
        "_5148": ["ConceptGearSetModalAnalysisAtASpeed"],
        "_5149": ["ConicalGearMeshModalAnalysisAtASpeed"],
        "_5150": ["ConicalGearModalAnalysisAtASpeed"],
        "_5151": ["ConicalGearSetModalAnalysisAtASpeed"],
        "_5152": ["ConnectionModalAnalysisAtASpeed"],
        "_5153": ["ConnectorModalAnalysisAtASpeed"],
        "_5154": ["CouplingConnectionModalAnalysisAtASpeed"],
        "_5155": ["CouplingHalfModalAnalysisAtASpeed"],
        "_5156": ["CouplingModalAnalysisAtASpeed"],
        "_5157": ["CVTBeltConnectionModalAnalysisAtASpeed"],
        "_5158": ["CVTModalAnalysisAtASpeed"],
        "_5159": ["CVTPulleyModalAnalysisAtASpeed"],
        "_5160": ["CycloidalAssemblyModalAnalysisAtASpeed"],
        "_5161": ["CycloidalDiscCentralBearingConnectionModalAnalysisAtASpeed"],
        "_5162": ["CycloidalDiscModalAnalysisAtASpeed"],
        "_5163": ["CycloidalDiscPlanetaryBearingConnectionModalAnalysisAtASpeed"],
        "_5164": ["CylindricalGearMeshModalAnalysisAtASpeed"],
        "_5165": ["CylindricalGearModalAnalysisAtASpeed"],
        "_5166": ["CylindricalGearSetModalAnalysisAtASpeed"],
        "_5167": ["CylindricalPlanetGearModalAnalysisAtASpeed"],
        "_5168": ["DatumModalAnalysisAtASpeed"],
        "_5169": ["ExternalCADModelModalAnalysisAtASpeed"],
        "_5170": ["FaceGearMeshModalAnalysisAtASpeed"],
        "_5171": ["FaceGearModalAnalysisAtASpeed"],
        "_5172": ["FaceGearSetModalAnalysisAtASpeed"],
        "_5173": ["FEPartModalAnalysisAtASpeed"],
        "_5174": ["FlexiblePinAssemblyModalAnalysisAtASpeed"],
        "_5175": ["GearMeshModalAnalysisAtASpeed"],
        "_5176": ["GearModalAnalysisAtASpeed"],
        "_5177": ["GearSetModalAnalysisAtASpeed"],
        "_5178": ["GuideDxfModelModalAnalysisAtASpeed"],
        "_5179": ["HypoidGearMeshModalAnalysisAtASpeed"],
        "_5180": ["HypoidGearModalAnalysisAtASpeed"],
        "_5181": ["HypoidGearSetModalAnalysisAtASpeed"],
        "_5182": ["InterMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5183": ["KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed"],
        "_5184": ["KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed"],
        "_5185": ["KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtASpeed"],
        "_5186": ["KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed"],
        "_5187": ["KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed"],
        "_5188": ["KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtASpeed"],
        "_5189": ["KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5190": ["KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed"],
        "_5191": ["KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5192": ["MassDiscModalAnalysisAtASpeed"],
        "_5193": ["MeasurementComponentModalAnalysisAtASpeed"],
        "_5194": ["ModalAnalysisAtASpeed"],
        "_5195": ["MountableComponentModalAnalysisAtASpeed"],
        "_5196": ["OilSealModalAnalysisAtASpeed"],
        "_5197": ["PartModalAnalysisAtASpeed"],
        "_5198": ["PartToPartShearCouplingConnectionModalAnalysisAtASpeed"],
        "_5199": ["PartToPartShearCouplingHalfModalAnalysisAtASpeed"],
        "_5200": ["PartToPartShearCouplingModalAnalysisAtASpeed"],
        "_5201": ["PlanetaryConnectionModalAnalysisAtASpeed"],
        "_5202": ["PlanetaryGearSetModalAnalysisAtASpeed"],
        "_5203": ["PlanetCarrierModalAnalysisAtASpeed"],
        "_5204": ["PointLoadModalAnalysisAtASpeed"],
        "_5205": ["PowerLoadModalAnalysisAtASpeed"],
        "_5206": ["PulleyModalAnalysisAtASpeed"],
        "_5207": ["RingPinsModalAnalysisAtASpeed"],
        "_5208": ["RingPinsToDiscConnectionModalAnalysisAtASpeed"],
        "_5209": ["RollingRingAssemblyModalAnalysisAtASpeed"],
        "_5210": ["RollingRingConnectionModalAnalysisAtASpeed"],
        "_5211": ["RollingRingModalAnalysisAtASpeed"],
        "_5212": ["RootAssemblyModalAnalysisAtASpeed"],
        "_5213": ["ShaftHubConnectionModalAnalysisAtASpeed"],
        "_5214": ["ShaftModalAnalysisAtASpeed"],
        "_5215": ["ShaftToMountableComponentConnectionModalAnalysisAtASpeed"],
        "_5216": ["SpecialisedAssemblyModalAnalysisAtASpeed"],
        "_5217": ["SpiralBevelGearMeshModalAnalysisAtASpeed"],
        "_5218": ["SpiralBevelGearModalAnalysisAtASpeed"],
        "_5219": ["SpiralBevelGearSetModalAnalysisAtASpeed"],
        "_5220": ["SpringDamperConnectionModalAnalysisAtASpeed"],
        "_5221": ["SpringDamperHalfModalAnalysisAtASpeed"],
        "_5222": ["SpringDamperModalAnalysisAtASpeed"],
        "_5223": ["StraightBevelDiffGearMeshModalAnalysisAtASpeed"],
        "_5224": ["StraightBevelDiffGearModalAnalysisAtASpeed"],
        "_5225": ["StraightBevelDiffGearSetModalAnalysisAtASpeed"],
        "_5226": ["StraightBevelGearMeshModalAnalysisAtASpeed"],
        "_5227": ["StraightBevelGearModalAnalysisAtASpeed"],
        "_5228": ["StraightBevelGearSetModalAnalysisAtASpeed"],
        "_5229": ["StraightBevelPlanetGearModalAnalysisAtASpeed"],
        "_5230": ["StraightBevelSunGearModalAnalysisAtASpeed"],
        "_5231": ["SynchroniserHalfModalAnalysisAtASpeed"],
        "_5232": ["SynchroniserModalAnalysisAtASpeed"],
        "_5233": ["SynchroniserPartModalAnalysisAtASpeed"],
        "_5234": ["SynchroniserSleeveModalAnalysisAtASpeed"],
        "_5235": ["TorqueConverterConnectionModalAnalysisAtASpeed"],
        "_5236": ["TorqueConverterModalAnalysisAtASpeed"],
        "_5237": ["TorqueConverterPumpModalAnalysisAtASpeed"],
        "_5238": ["TorqueConverterTurbineModalAnalysisAtASpeed"],
        "_5239": ["UnbalancedMassModalAnalysisAtASpeed"],
        "_5240": ["VirtualComponentModalAnalysisAtASpeed"],
        "_5241": ["WormGearMeshModalAnalysisAtASpeed"],
        "_5242": ["WormGearModalAnalysisAtASpeed"],
        "_5243": ["WormGearSetModalAnalysisAtASpeed"],
        "_5244": ["ZerolBevelGearMeshModalAnalysisAtASpeed"],
        "_5245": ["ZerolBevelGearModalAnalysisAtASpeed"],
        "_5246": ["ZerolBevelGearSetModalAnalysisAtASpeed"],
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

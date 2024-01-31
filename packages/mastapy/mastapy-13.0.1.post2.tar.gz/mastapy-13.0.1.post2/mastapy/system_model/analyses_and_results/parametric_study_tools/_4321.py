"""ComponentParametricStudyTool"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4393
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ComponentParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2444


__docformat__ = "restructuredtext en"
__all__ = ("ComponentParametricStudyTool",)


Self = TypeVar("Self", bound="ComponentParametricStudyTool")


class ComponentParametricStudyTool(_4393.PartParametricStudyTool):
    """ComponentParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COMPONENT_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentParametricStudyTool")

    class _Cast_ComponentParametricStudyTool:
        """Special nested class for casting ComponentParametricStudyTool to subclasses."""

        def __init__(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
            parent: "ComponentParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            return self._parent._cast(_4393.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4297,
            )

            return self._parent._cast(_4297.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(_4298.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4301,
            )

            return self._parent._cast(_4301.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(_4304.BearingParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4308,
            )

            return self._parent._cast(_4308.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(
                _4310.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4311,
            )

            return self._parent._cast(_4311.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4313,
            )

            return self._parent._cast(_4313.BevelGearParametricStudyTool)

        @property
        def bolt_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4316,
            )

            return self._parent._cast(_4316.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ConceptGearParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConicalGearParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.CouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4338,
            )

            return self._parent._cast(_4338.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4346,
            )

            return self._parent._cast(_4346.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4347,
            )

            return self._parent._cast(_4347.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4355,
            )

            return self._parent._cast(_4355.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4357,
            )

            return self._parent._cast(_4357.FaceGearParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.FEPartParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.GearParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(_4366.HypoidGearParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4370,
            )

            return self._parent._cast(
                _4370.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(
                _4376.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(_4378.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(_4379.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4382,
            )

            return self._parent._cast(_4382.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(
                _4395.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def planet_carrier_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4399,
            )

            return self._parent._cast(_4399.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4403,
            )

            return self._parent._cast(_4403.RingPinsParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.RollingRingParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.ShaftParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpiralBevelGearParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.SpringDamperHalfParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4427,
            )

            return self._parent._cast(_4427.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4433,
            )

            return self._parent._cast(_4433.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.WormGearParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ):
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.ZerolBevelGearParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
        ) -> "ComponentParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2444.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentParametricStudyTool._Cast_ComponentParametricStudyTool":
        return self._Cast_ComponentParametricStudyTool(self)

"""MountableComponentCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5013,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "MountableComponentCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4936,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="MountableComponentCompoundModalAnalysisAtAStiffness")


class MountableComponentCompoundModalAnalysisAtAStiffness(
    _5013.ComponentCompoundModalAnalysisAtAStiffness
):
    """MountableComponentCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_MountableComponentCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting MountableComponentCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
            parent: "MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_5013.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4992,
            )

            return self._parent._cast(
                _4992.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(_4996.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4999,
            )

            return self._parent._cast(
                _4999.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5002,
            )

            return self._parent._cast(
                _5002.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5003,
            )

            return self._parent._cast(
                _5003.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5004,
            )

            return self._parent._cast(_5004.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(_5011.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5016,
            )

            return self._parent._cast(
                _5016.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5017,
            )

            return self._parent._cast(
                _5017.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5020,
            )

            return self._parent._cast(
                _5020.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(_5024.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(
                _5027.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5030,
            )

            return self._parent._cast(_5030.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(
                _5035.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5038,
            )

            return self._parent._cast(
                _5038.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(_5041.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(_5046.GearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(_5050.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5054,
            )

            return self._parent._cast(
                _5054.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5057,
            )

            return self._parent._cast(
                _5057.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5060,
            )

            return self._parent._cast(
                _5060.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5063,
            )

            return self._parent._cast(_5063.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5070,
            )

            return self._parent._cast(
                _5070.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5073,
            )

            return self._parent._cast(
                _5073.PlanetCarrierCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(_5074.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(_5075.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(_5076.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5077,
            )

            return self._parent._cast(_5077.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5080,
            )

            return self._parent._cast(
                _5080.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(
                _5084.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5087,
            )

            return self._parent._cast(
                _5087.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5092,
            )

            return self._parent._cast(
                _5092.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5093,
            )

            return self._parent._cast(
                _5093.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5096,
            )

            return self._parent._cast(
                _5096.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5099,
            )

            return self._parent._cast(
                _5099.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5100,
            )

            return self._parent._cast(
                _5100.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5102,
            )

            return self._parent._cast(
                _5102.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5103,
            )

            return self._parent._cast(
                _5103.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5107,
            )

            return self._parent._cast(
                _5107.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5108,
            )

            return self._parent._cast(
                _5108.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(_5111.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5114,
            )

            return self._parent._cast(
                _5114.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
        ) -> "MountableComponentCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self,
        instance_to_wrap: "MountableComponentCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4936.MountableComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.MountableComponentModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4936.MountableComponentModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.MountableComponentModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentCompoundModalAnalysisAtAStiffness._Cast_MountableComponentCompoundModalAnalysisAtAStiffness":
        return self._Cast_MountableComponentCompoundModalAnalysisAtAStiffness(self)

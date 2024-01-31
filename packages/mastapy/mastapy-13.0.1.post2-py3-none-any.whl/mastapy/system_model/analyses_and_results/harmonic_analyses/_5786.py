"""MountableComponentHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "MountableComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464
    from mastapy.system_model.analyses_and_results.modal_analyses import _4658
    from mastapy.system_model.analyses_and_results.system_deflections import _2782


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentHarmonicAnalysis",)


Self = TypeVar("Self", bound="MountableComponentHarmonicAnalysis")


class MountableComponentHarmonicAnalysis(_5705.ComponentHarmonicAnalysis):
    """MountableComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentHarmonicAnalysis")

    class _Cast_MountableComponentHarmonicAnalysis:
        """Special nested class for casting MountableComponentHarmonicAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
            parent: "MountableComponentHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            return self._parent._cast(_5705.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5683,
            )

            return self._parent._cast(_5683.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.BearingHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5690,
            )

            return self._parent._cast(_5690.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5693,
            )

            return self._parent._cast(_5693.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5694,
            )

            return self._parent._cast(_5694.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BevelGearHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ConceptGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5712,
            )

            return self._parent._cast(_5712.ConicalGearHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.CouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.CVTPulleyHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5730,
            )

            return self._parent._cast(_5730.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5747,
            )

            return self._parent._cast(_5747.FaceGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.GearHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5771,
            )

            return self._parent._cast(_5771.HypoidGearHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5775,
            )

            return self._parent._cast(
                _5775.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5778,
            )

            return self._parent._cast(
                _5778.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5781,
            )

            return self._parent._cast(
                _5781.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5784,
            )

            return self._parent._cast(_5784.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.MeasurementComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.OilSealHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5795,
            )

            return self._parent._cast(_5795.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5797,
            )

            return self._parent._cast(_5797.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(_5804.RollingRingHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(_5807.ShaftHubConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.SpiralBevelGearHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.SpringDamperHalfHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5825,
            )

            return self._parent._cast(_5825.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5827,
            )

            return self._parent._cast(_5827.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5833,
            )

            return self._parent._cast(_5833.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.WormGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5841,
            )

            return self._parent._cast(_5841.ZerolBevelGearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
        ) -> "MountableComponentHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2464.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coupled_modal_analysis(self: Self) -> "_4658.MountableComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2782.MountableComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis":
        return self._Cast_MountableComponentHarmonicAnalysis(self)

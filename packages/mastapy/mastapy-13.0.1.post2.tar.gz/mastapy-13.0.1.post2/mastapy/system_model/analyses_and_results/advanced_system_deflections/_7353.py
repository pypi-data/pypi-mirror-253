"""MountableComponentAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "MountableComponentAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2464


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="MountableComponentAdvancedSystemDeflection")


class MountableComponentAdvancedSystemDeflection(
    _7298.ComponentAdvancedSystemDeflection
):
    """MountableComponentAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentAdvancedSystemDeflection"
    )

    class _Cast_MountableComponentAdvancedSystemDeflection:
        """Special nested class for casting MountableComponentAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
            parent: "MountableComponentAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7277,
            )

            return self._parent._cast(
                _7277.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def bearing_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7281,
            )

            return self._parent._cast(_7281.BearingAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7284,
            )

            return self._parent._cast(
                _7284.BevelDifferentialGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7287,
            )

            return self._parent._cast(
                _7287.BevelDifferentialPlanetGearAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7288,
            )

            return self._parent._cast(
                _7288.BevelDifferentialSunGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7289,
            )

            return self._parent._cast(_7289.BevelGearAdvancedSystemDeflection)

        @property
        def clutch_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.ClutchHalfAdvancedSystemDeflection)

        @property
        def concept_coupling_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7301,
            )

            return self._parent._cast(_7301.ConceptCouplingHalfAdvancedSystemDeflection)

        @property
        def concept_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.ConceptGearAdvancedSystemDeflection)

        @property
        def conical_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7305,
            )

            return self._parent._cast(_7305.ConicalGearAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7309,
            )

            return self._parent._cast(_7309.ConnectorAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7313,
            )

            return self._parent._cast(_7313.CouplingHalfAdvancedSystemDeflection)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.CVTPulleyAdvancedSystemDeflection)

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7321,
            )

            return self._parent._cast(_7321.CylindricalGearAdvancedSystemDeflection)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7325,
            )

            return self._parent._cast(
                _7325.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def face_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7328,
            )

            return self._parent._cast(_7328.FaceGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7333,
            )

            return self._parent._cast(_7333.GearAdvancedSystemDeflection)

        @property
        def hypoid_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(_7337.HypoidGearAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7341,
            )

            return self._parent._cast(
                _7341.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(
                _7344.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7347,
            )

            return self._parent._cast(
                _7347.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
            )

        @property
        def mass_disc_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.MassDiscAdvancedSystemDeflection)

        @property
        def measurement_component_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(
                _7352.MeasurementComponentAdvancedSystemDeflection
            )

        @property
        def oil_seal_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.OilSealAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7358,
            )

            return self._parent._cast(
                _7358.PartToPartShearCouplingHalfAdvancedSystemDeflection
            )

        @property
        def planet_carrier_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7361,
            )

            return self._parent._cast(_7361.PlanetCarrierAdvancedSystemDeflection)

        @property
        def point_load_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.PointLoadAdvancedSystemDeflection)

        @property
        def power_load_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7363,
            )

            return self._parent._cast(_7363.PowerLoadAdvancedSystemDeflection)

        @property
        def pulley_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(_7364.PulleyAdvancedSystemDeflection)

        @property
        def ring_pins_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7365,
            )

            return self._parent._cast(_7365.RingPinsAdvancedSystemDeflection)

        @property
        def rolling_ring_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7367,
            )

            return self._parent._cast(_7367.RollingRingAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7375,
            )

            return self._parent._cast(_7375.SpiralBevelGearAdvancedSystemDeflection)

        @property
        def spring_damper_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7380,
            )

            return self._parent._cast(_7380.SpringDamperHalfAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(
                _7381.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7384,
            )

            return self._parent._cast(_7384.StraightBevelGearAdvancedSystemDeflection)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7387,
            )

            return self._parent._cast(
                _7387.StraightBevelPlanetGearAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7388,
            )

            return self._parent._cast(
                _7388.StraightBevelSunGearAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7390,
            )

            return self._parent._cast(_7390.SynchroniserHalfAdvancedSystemDeflection)

        @property
        def synchroniser_part_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7391,
            )

            return self._parent._cast(_7391.SynchroniserPartAdvancedSystemDeflection)

        @property
        def synchroniser_sleeve_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(_7392.SynchroniserSleeveAdvancedSystemDeflection)

        @property
        def torque_converter_pump_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(_7395.TorqueConverterPumpAdvancedSystemDeflection)

        @property
        def torque_converter_turbine_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7396,
            )

            return self._parent._cast(
                _7396.TorqueConverterTurbineAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7398,
            )

            return self._parent._cast(_7398.UnbalancedMassAdvancedSystemDeflection)

        @property
        def virtual_component_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(_7399.VirtualComponentAdvancedSystemDeflection)

        @property
        def worm_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.WormGearAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7403,
            )

            return self._parent._cast(_7403.ZerolBevelGearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
        ) -> "MountableComponentAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "MountableComponentAdvancedSystemDeflection.TYPE"
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
    def cast_to(
        self: Self,
    ) -> "MountableComponentAdvancedSystemDeflection._Cast_MountableComponentAdvancedSystemDeflection":
        return self._Cast_MountableComponentAdvancedSystemDeflection(self)

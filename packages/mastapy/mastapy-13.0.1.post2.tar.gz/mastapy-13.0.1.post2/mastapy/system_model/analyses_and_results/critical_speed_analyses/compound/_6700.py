"""ComponentCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6754,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ComponentCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6568


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundCriticalSpeedAnalysis")


class ComponentCompoundCriticalSpeedAnalysis(_6754.PartCompoundCriticalSpeedAnalysis):
    """ComponentCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundCriticalSpeedAnalysis"
    )

    class _Cast_ComponentCompoundCriticalSpeedAnalysis:
        """Special nested class for casting ComponentCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
            parent: "ComponentCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6754.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6676,
            )

            return self._parent._cast(_6676.AbstractShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6677,
            )

            return self._parent._cast(
                _6677.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6679,
            )

            return self._parent._cast(
                _6679.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bearing_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6683,
            )

            return self._parent._cast(_6683.BearingCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6686,
            )

            return self._parent._cast(
                _6686.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6689,
            )

            return self._parent._cast(
                _6689.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6690,
            )

            return self._parent._cast(
                _6690.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6691,
            )

            return self._parent._cast(_6691.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def bolt_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6694,
            )

            return self._parent._cast(_6694.BoltCompoundCriticalSpeedAnalysis)

        @property
        def clutch_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6698,
            )

            return self._parent._cast(_6698.ClutchHalfCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6703,
            )

            return self._parent._cast(
                _6703.ConceptCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6704,
            )

            return self._parent._cast(_6704.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(_6707.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def connector_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6711,
            )

            return self._parent._cast(_6711.ConnectorCompoundCriticalSpeedAnalysis)

        @property
        def coupling_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(_6714.CouplingHalfCompoundCriticalSpeedAnalysis)

        @property
        def cvt_pulley_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6717,
            )

            return self._parent._cast(_6717.CVTPulleyCompoundCriticalSpeedAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6720,
            )

            return self._parent._cast(_6720.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(
                _6722.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6725,
            )

            return self._parent._cast(
                _6725.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def datum_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.DatumCompoundCriticalSpeedAnalysis)

        @property
        def external_cad_model_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(
                _6727.ExternalCADModelCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6728,
            )

            return self._parent._cast(_6728.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6731,
            )

            return self._parent._cast(_6731.FEPartCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6733,
            )

            return self._parent._cast(_6733.GearCompoundCriticalSpeedAnalysis)

        @property
        def guide_dxf_model_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6736,
            )

            return self._parent._cast(_6736.GuideDxfModelCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6737,
            )

            return self._parent._cast(_6737.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(
                _6741.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(
                _6744.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6747,
            )

            return self._parent._cast(
                _6747.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def mass_disc_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6750,
            )

            return self._parent._cast(_6750.MassDiscCompoundCriticalSpeedAnalysis)

        @property
        def measurement_component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6751,
            )

            return self._parent._cast(
                _6751.MeasurementComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def oil_seal_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6753,
            )

            return self._parent._cast(_6753.OilSealCompoundCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6757,
            )

            return self._parent._cast(
                _6757.PartToPartShearCouplingHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6760,
            )

            return self._parent._cast(_6760.PlanetCarrierCompoundCriticalSpeedAnalysis)

        @property
        def point_load_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(_6761.PointLoadCompoundCriticalSpeedAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6762,
            )

            return self._parent._cast(_6762.PowerLoadCompoundCriticalSpeedAnalysis)

        @property
        def pulley_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6763,
            )

            return self._parent._cast(_6763.PulleyCompoundCriticalSpeedAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6764,
            )

            return self._parent._cast(_6764.RingPinsCompoundCriticalSpeedAnalysis)

        @property
        def rolling_ring_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6767,
            )

            return self._parent._cast(_6767.RollingRingCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6770,
            )

            return self._parent._cast(_6770.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6771,
            )

            return self._parent._cast(
                _6771.ShaftHubConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6774,
            )

            return self._parent._cast(
                _6774.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6779,
            )

            return self._parent._cast(
                _6779.SpringDamperHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6783,
            )

            return self._parent._cast(
                _6783.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6786,
            )

            return self._parent._cast(
                _6786.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6787,
            )

            return self._parent._cast(
                _6787.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_half_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.SynchroniserHalfCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_part_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6790,
            )

            return self._parent._cast(
                _6790.SynchroniserPartCompoundCriticalSpeedAnalysis
            )

        @property
        def synchroniser_sleeve_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6791,
            )

            return self._parent._cast(
                _6791.SynchroniserSleeveCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_pump_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6794,
            )

            return self._parent._cast(
                _6794.TorqueConverterPumpCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_turbine_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6795,
            )

            return self._parent._cast(
                _6795.TorqueConverterTurbineCompoundCriticalSpeedAnalysis
            )

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6796,
            )

            return self._parent._cast(_6796.UnbalancedMassCompoundCriticalSpeedAnalysis)

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6797,
            )

            return self._parent._cast(
                _6797.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(_6798.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6801,
            )

            return self._parent._cast(_6801.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def component_compound_critical_speed_analysis(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
        ) -> "ComponentCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "ComponentCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6568.ComponentCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ComponentCriticalSpeedAnalysis]

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
    ) -> "List[_6568.ComponentCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ComponentCriticalSpeedAnalysis]

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
    ) -> "ComponentCompoundCriticalSpeedAnalysis._Cast_ComponentCompoundCriticalSpeedAnalysis":
        return self._Cast_ComponentCompoundCriticalSpeedAnalysis(self)

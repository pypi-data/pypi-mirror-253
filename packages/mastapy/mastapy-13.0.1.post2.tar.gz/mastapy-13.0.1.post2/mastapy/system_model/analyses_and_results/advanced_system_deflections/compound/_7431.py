"""ComponentCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7485,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ComponentCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7298,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ComponentCompoundAdvancedSystemDeflection")


class ComponentCompoundAdvancedSystemDeflection(
    _7485.PartCompoundAdvancedSystemDeflection
):
    """ComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundAdvancedSystemDeflection"
    )

    class _Cast_ComponentCompoundAdvancedSystemDeflection:
        """Special nested class for casting ComponentCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
            parent: "ComponentCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7485.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7407,
            )

            return self._parent._cast(
                _7407.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7410,
            )

            return self._parent._cast(
                _7410.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def bearing_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(_7414.BearingCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7417,
            )

            return self._parent._cast(
                _7417.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7420,
            )

            return self._parent._cast(
                _7420.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(
                _7421.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(_7422.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bolt_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7425,
            )

            return self._parent._cast(_7425.BoltCompoundAdvancedSystemDeflection)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(_7429.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(
                _7434.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7435,
            )

            return self._parent._cast(_7435.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(_7438.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def connector_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(_7442.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(
                _7445.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7448,
            )

            return self._parent._cast(_7448.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7453,
            )

            return self._parent._cast(
                _7453.CylindricalGearCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7456,
            )

            return self._parent._cast(
                _7456.CylindricalPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def datum_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7458,
            )

            return self._parent._cast(
                _7458.ExternalCADModelCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(_7459.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7462,
            )

            return self._parent._cast(_7462.FEPartCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.GearCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(
                _7467.GuideDxfModelCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(_7468.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(
                _7472.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7475,
            )

            return self._parent._cast(
                _7475.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7478,
            )

            return self._parent._cast(
                _7478.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(_7481.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(_7484.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def planet_carrier_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(
                _7491.PlanetCarrierCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(_7492.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(_7494.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7495,
            )

            return self._parent._cast(_7495.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7498,
            )

            return self._parent._cast(_7498.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def shaft_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7501,
            )

            return self._parent._cast(_7501.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(
                _7502.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(
                _7505.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(
                _7511.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(
                _7514.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7517,
            )

            return self._parent._cast(
                _7517.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(
                _7522.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7526,
            )

            return self._parent._cast(
                _7526.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7529,
            )

            return self._parent._cast(_7529.WormGearCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7532,
            )

            return self._parent._cast(
                _7532.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
        ) -> "ComponentCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ComponentCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7298.ComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ComponentAdvancedSystemDeflection]

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
    ) -> "List[_7298.ComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ComponentAdvancedSystemDeflection]

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
    ) -> "ComponentCompoundAdvancedSystemDeflection._Cast_ComponentCompoundAdvancedSystemDeflection":
        return self._Cast_ComponentCompoundAdvancedSystemDeflection(self)

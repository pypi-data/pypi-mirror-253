"""ComponentCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5608
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ComponentCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5404


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ComponentCompoundMultibodyDynamicsAnalysis")


class ComponentCompoundMultibodyDynamicsAnalysis(
    _5608.PartCompoundMultibodyDynamicsAnalysis
):
    """ComponentCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ComponentCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ComponentCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
            parent: "ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5530,
            )

            return self._parent._cast(
                _5530.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5531,
            )

            return self._parent._cast(
                _5531.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5533,
            )

            return self._parent._cast(
                _5533.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5537,
            )

            return self._parent._cast(_5537.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5540,
            )

            return self._parent._cast(
                _5540.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(
                _5544.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(_5545.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5548,
            )

            return self._parent._cast(_5548.BoltCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5552,
            )

            return self._parent._cast(_5552.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5558,
            )

            return self._parent._cast(
                _5558.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(
                _5561.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(_5565.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5571,
            )

            return self._parent._cast(_5571.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5576,
            )

            return self._parent._cast(
                _5576.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5579,
            )

            return self._parent._cast(
                _5579.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def datum_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(_5580.DatumCompoundMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.ExternalCADModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5582,
            )

            return self._parent._cast(_5582.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(
                _5590.GuideDxfModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5595,
            )

            return self._parent._cast(
                _5595.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5598,
            )

            return self._parent._cast(
                _5598.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5601,
            )

            return self._parent._cast(
                _5601.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(_5607.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5611,
            )

            return self._parent._cast(
                _5611.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(
                _5614.PlanetCarrierCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(_5615.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(_5617.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5618,
            )

            return self._parent._cast(_5618.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(_5624.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5625,
            )

            return self._parent._cast(
                _5625.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5628,
            )

            return self._parent._cast(
                _5628.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(
                _5634.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5637,
            )

            return self._parent._cast(
                _5637.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5649,
            )

            return self._parent._cast(
                _5649.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5652,
            )

            return self._parent._cast(_5652.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5655,
            )

            return self._parent._cast(
                _5655.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "ComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ComponentCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5404.ComponentMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ComponentMultibodyDynamicsAnalysis]

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
    ) -> "List[_5404.ComponentMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ComponentMultibodyDynamicsAnalysis]

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
    ) -> "ComponentCompoundMultibodyDynamicsAnalysis._Cast_ComponentCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ComponentCompoundMultibodyDynamicsAnalysis(self)

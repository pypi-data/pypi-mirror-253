"""PartCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7546
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "PartCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4662


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundModalAnalysis",)


Self = TypeVar("Self", bound="PartCompoundModalAnalysis")


class PartCompoundModalAnalysis(_7546.PartCompoundAnalysis):
    """PartCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundModalAnalysis")

    class _Cast_PartCompoundModalAnalysis:
        """Special nested class for casting PartCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
            parent: "PartCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4728,
            )

            return self._parent._cast(_4728.AbstractAssemblyCompoundModalAnalysis)

        @property
        def abstract_shaft_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4729,
            )

            return self._parent._cast(_4729.AbstractShaftCompoundModalAnalysis)

        @property
        def abstract_shaft_or_housing_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4730,
            )

            return self._parent._cast(_4730.AbstractShaftOrHousingCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4732,
            )

            return self._parent._cast(_4732.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(
                _4734.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4735,
            )

            return self._parent._cast(_4735.AssemblyCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(_4736.BearingCompoundModalAnalysis)

        @property
        def belt_drive_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(_4738.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4739,
            )

            return self._parent._cast(_4739.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(
                _4741.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4742,
            )

            return self._parent._cast(
                _4742.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4743,
            )

            return self._parent._cast(
                _4743.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4744,
            )

            return self._parent._cast(_4744.BevelGearCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BevelGearSetCompoundModalAnalysis)

        @property
        def bolt_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4747,
            )

            return self._parent._cast(_4747.BoltCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4748,
            )

            return self._parent._cast(_4748.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.ClutchCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.ClutchHalfCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ComponentCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(_4754.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4756,
            )

            return self._parent._cast(_4756.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(_4757.ConceptGearCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.ConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConicalGearSetCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(_4764.ConnectorCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.CouplingCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4767,
            )

            return self._parent._cast(_4767.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.CVTCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4770,
            )

            return self._parent._cast(_4770.CVTPulleyCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cycloidal_disc_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4773,
            )

            return self._parent._cast(_4773.CycloidalDiscCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.CylindricalGearSetCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4778,
            )

            return self._parent._cast(_4778.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def datum_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4779,
            )

            return self._parent._cast(_4779.DatumCompoundModalAnalysis)

        @property
        def external_cad_model_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.ExternalCADModelCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4781,
            )

            return self._parent._cast(_4781.FaceGearCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.FaceGearSetCompoundModalAnalysis)

        @property
        def fe_part_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4784,
            )

            return self._parent._cast(_4784.FEPartCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4786,
            )

            return self._parent._cast(_4786.GearCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.GearSetCompoundModalAnalysis)

        @property
        def guide_dxf_model_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4789,
            )

            return self._parent._cast(_4789.GuideDxfModelCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4790,
            )

            return self._parent._cast(_4790.HypoidGearCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(
                _4794.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4797,
            )

            return self._parent._cast(
                _4797.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4800,
            )

            return self._parent._cast(
                _4800.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.MeasurementComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MountableComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.OilSealCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(
                _4808.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4810,
            )

            return self._parent._cast(
                _4810.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def planet_carrier_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(_4814.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(_4816.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(_4817.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4820,
            )

            return self._parent._cast(_4820.RollingRingCompoundModalAnalysis)

        @property
        def root_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.RootAssemblyCompoundModalAnalysis)

        @property
        def shaft_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4823,
            )

            return self._parent._cast(_4823.ShaftCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(_4824.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4827,
            )

            return self._parent._cast(_4827.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.SpringDamperCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4833,
            )

            return self._parent._cast(_4833.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(
                _4835.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4836,
            )

            return self._parent._cast(_4836.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4839,
            )

            return self._parent._cast(
                _4839.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4840,
            )

            return self._parent._cast(_4840.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.SynchroniserCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4843,
            )

            return self._parent._cast(_4843.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.TorqueConverterCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(_4847.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.WormGearCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4854,
            )

            return self._parent._cast(_4854.ZerolBevelGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis",
        ) -> "PartCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4662.PartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis]

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
    def component_analysis_cases_ready(self: Self) -> "List[_4662.PartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis]

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
    ) -> "PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis":
        return self._Cast_PartCompoundModalAnalysis(self)

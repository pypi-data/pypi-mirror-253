"""PartCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7546
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "PartCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5467


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PartCompoundMultibodyDynamicsAnalysis")


class PartCompoundMultibodyDynamicsAnalysis(_7546.PartCompoundAnalysis):
    """PartCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_PartCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting PartCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
            parent: "PartCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5530,
            )

            return self._parent._cast(
                _5530.AbstractShaftCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5531,
            )

            return self._parent._cast(
                _5531.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5533,
            )

            return self._parent._cast(
                _5533.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5535,
            )

            return self._parent._cast(
                _5535.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5536,
            )

            return self._parent._cast(_5536.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5537,
            )

            return self._parent._cast(_5537.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(_5539.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5540,
            )

            return self._parent._cast(
                _5540.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5543,
            )

            return self._parent._cast(
                _5543.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5544,
            )

            return self._parent._cast(
                _5544.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(_5545.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(
                _5547.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolt_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5548,
            )

            return self._parent._cast(_5548.BoltCompoundMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5549,
            )

            return self._parent._cast(
                _5549.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5552,
            )

            return self._parent._cast(_5552.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5557,
            )

            return self._parent._cast(
                _5557.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5558,
            )

            return self._parent._cast(
                _5558.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5561,
            )

            return self._parent._cast(
                _5561.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5565,
            )

            return self._parent._cast(_5565.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(_5566.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5568,
            )

            return self._parent._cast(
                _5568.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(_5570.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5571,
            )

            return self._parent._cast(_5571.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(
                _5572.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5574,
            )

            return self._parent._cast(
                _5574.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5576,
            )

            return self._parent._cast(
                _5576.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(
                _5578.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5579,
            )

            return self._parent._cast(
                _5579.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def datum_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(_5580.DatumCompoundMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.ExternalCADModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5582,
            )

            return self._parent._cast(_5582.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(
                _5584.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def fe_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(_5585.FEPartCompoundMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(
                _5586.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(_5589.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(
                _5590.GuideDxfModelCompoundMultibodyDynamicsAnalysis
            )

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5591,
            )

            return self._parent._cast(_5591.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5595,
            )

            return self._parent._cast(
                _5595.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(
                _5597.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5598,
            )

            return self._parent._cast(
                _5598.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5601,
            )

            return self._parent._cast(
                _5601.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(_5607.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(
                _5609.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5611,
            )

            return self._parent._cast(
                _5611.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(
                _5614.PlanetCarrierCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5615,
            )

            return self._parent._cast(_5615.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(_5616.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(_5617.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5618,
            )

            return self._parent._cast(_5618.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(
                _5620.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.RootAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5624,
            )

            return self._parent._cast(_5624.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5625,
            )

            return self._parent._cast(
                _5625.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5628,
            )

            return self._parent._cast(
                _5628.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5631,
            )

            return self._parent._cast(
                _5631.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5633,
            )

            return self._parent._cast(
                _5633.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(
                _5634.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5637,
            )

            return self._parent._cast(
                _5637.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5640,
            )

            return self._parent._cast(
                _5640.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5641,
            )

            return self._parent._cast(
                _5641.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5644,
            )

            return self._parent._cast(
                _5644.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5649,
            )

            return self._parent._cast(
                _5649.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5652,
            )

            return self._parent._cast(_5652.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(
                _5654.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5655,
            )

            return self._parent._cast(
                _5655.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
        ) -> "PartCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "PartCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5467.PartMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PartMultibodyDynamicsAnalysis]

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
    ) -> "List[_5467.PartMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PartMultibodyDynamicsAnalysis]

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
    ) -> "PartCompoundMultibodyDynamicsAnalysis._Cast_PartCompoundMultibodyDynamicsAnalysis":
        return self._Cast_PartCompoundMultibodyDynamicsAnalysis(self)

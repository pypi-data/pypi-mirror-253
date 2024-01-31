"""SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5529
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5489


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis")


class SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis(
    _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
):
    """SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
            parent: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5535,
            )

            return self._parent._cast(
                _5535.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(_5539.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(
                _5547.BevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5549,
            )

            return self._parent._cast(
                _5549.BoltedJointCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.ClutchCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.ConceptCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConceptGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.ConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(_5566.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(_5570.CVTCompoundMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(
                _5572.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(
                _5578.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(
                _5584.FaceGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def flexible_pin_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5586,
            )

            return self._parent._cast(
                _5586.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(_5589.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.HypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(
                _5597.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(
                _5609.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(
                _5620.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5631,
            )

            return self._parent._cast(
                _5631.SpringDamperCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.SynchroniserCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.TorqueConverterCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(
                _5654.WormGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
            )

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5489.SpecialisedAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpecialisedAssemblyMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5489.SpecialisedAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpecialisedAssemblyMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis(self)

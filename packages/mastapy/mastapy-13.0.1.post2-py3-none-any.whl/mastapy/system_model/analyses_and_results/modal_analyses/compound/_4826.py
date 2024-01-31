"""SpecialisedAssemblyCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4728
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SpecialisedAssemblyCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4682


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundModalAnalysis")


class SpecialisedAssemblyCompoundModalAnalysis(
    _4728.AbstractAssemblyCompoundModalAnalysis
):
    """SpecialisedAssemblyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundModalAnalysis"
    )

    class _Cast_SpecialisedAssemblyCompoundModalAnalysis:
        """Special nested class for casting SpecialisedAssemblyCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
            parent: "SpecialisedAssemblyCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            return self._parent._cast(_4728.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4807,
            )

            return self._parent._cast(_4807.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(
                _4734.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def belt_drive_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(_4738.BeltDriveCompoundModalAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(
                _4741.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BevelGearSetCompoundModalAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4748,
            )

            return self._parent._cast(_4748.BoltedJointCompoundModalAnalysis)

        @property
        def clutch_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4749,
            )

            return self._parent._cast(_4749.ClutchCompoundModalAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(_4754.ConceptCouplingCompoundModalAnalysis)

        @property
        def concept_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConceptGearSetCompoundModalAnalysis)

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConicalGearSetCompoundModalAnalysis)

        @property
        def coupling_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4765,
            )

            return self._parent._cast(_4765.CouplingCompoundModalAnalysis)

        @property
        def cvt_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.CVTCompoundModalAnalysis)

        @property
        def cycloidal_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.CycloidalAssemblyCompoundModalAnalysis)

        @property
        def cylindrical_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.CylindricalGearSetCompoundModalAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.FaceGearSetCompoundModalAnalysis)

        @property
        def flexible_pin_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.FlexiblePinAssemblyCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.GearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.HypoidGearSetCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(
                _4808.PartToPartShearCouplingCompoundModalAnalysis
            )

        @property
        def planetary_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(_4812.PlanetaryGearSetCompoundModalAnalysis)

        @property
        def rolling_ring_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.RollingRingAssemblyCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def spring_damper_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.SpringDamperCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(
                _4835.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def synchroniser_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.SynchroniserCompoundModalAnalysis)

        @property
        def torque_converter_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.TorqueConverterCompoundModalAnalysis)

        @property
        def worm_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.WormGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
        ) -> "SpecialisedAssemblyCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SpecialisedAssemblyCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4682.SpecialisedAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis]

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
    ) -> "List[_4682.SpecialisedAssemblyModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpecialisedAssemblyModalAnalysis]

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
    ) -> "SpecialisedAssemblyCompoundModalAnalysis._Cast_SpecialisedAssemblyCompoundModalAnalysis":
        return self._Cast_SpecialisedAssemblyCompoundModalAnalysis(self)

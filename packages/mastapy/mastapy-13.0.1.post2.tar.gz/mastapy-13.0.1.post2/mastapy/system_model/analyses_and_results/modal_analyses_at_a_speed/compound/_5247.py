"""AbstractAssemblyCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5326,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AbstractAssemblyCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5117,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundModalAnalysisAtASpeed")


class AbstractAssemblyCompoundModalAnalysisAtASpeed(
    _5326.PartCompoundModalAnalysisAtASpeed
):
    """AbstractAssemblyCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed"
    )

    class _Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AbstractAssemblyCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
            parent: "AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5326.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5253,
            )

            return self._parent._cast(
                _5253.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5254,
            )

            return self._parent._cast(_5254.AssemblyCompoundModalAnalysisAtASpeed)

        @property
        def belt_drive_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5257,
            )

            return self._parent._cast(_5257.BeltDriveCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5260,
            )

            return self._parent._cast(
                _5260.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5265,
            )

            return self._parent._cast(_5265.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def bolted_joint_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5267,
            )

            return self._parent._cast(_5267.BoltedJointCompoundModalAnalysisAtASpeed)

        @property
        def clutch_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5268,
            )

            return self._parent._cast(_5268.ClutchCompoundModalAnalysisAtASpeed)

        @property
        def concept_coupling_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5273,
            )

            return self._parent._cast(
                _5273.ConceptCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5278,
            )

            return self._parent._cast(_5278.ConceptGearSetCompoundModalAnalysisAtASpeed)

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5281,
            )

            return self._parent._cast(_5281.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def coupling_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5284,
            )

            return self._parent._cast(_5284.CouplingCompoundModalAnalysisAtASpeed)

        @property
        def cvt_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5288,
            )

            return self._parent._cast(_5288.CVTCompoundModalAnalysisAtASpeed)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(
                _5290.CycloidalAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5296,
            )

            return self._parent._cast(
                _5296.CylindricalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5302,
            )

            return self._parent._cast(_5302.FaceGearSetCompoundModalAnalysisAtASpeed)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(
                _5304.FlexiblePinAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(_5311.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5315,
            )

            return self._parent._cast(
                _5315.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5318,
            )

            return self._parent._cast(
                _5318.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5321,
            )

            return self._parent._cast(
                _5321.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5327,
            )

            return self._parent._cast(
                _5327.PartToPartShearCouplingCompoundModalAnalysisAtASpeed
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(
                _5331.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5338,
            )

            return self._parent._cast(
                _5338.RollingRingAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(_5341.RootAssemblyCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5348,
            )

            return self._parent._cast(
                _5348.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.SpringDamperCompoundModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(
                _5357.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5360,
            )

            return self._parent._cast(_5360.SynchroniserCompoundModalAnalysisAtASpeed)

        @property
        def torque_converter_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5364,
            )

            return self._parent._cast(
                _5364.TorqueConverterCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5372,
            )

            return self._parent._cast(_5372.WormGearSetCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(
                _5375.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
        ) -> "AbstractAssemblyCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AbstractAssemblyCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5117.AbstractAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractAssemblyModalAnalysisAtASpeed]

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
    ) -> "List[_5117.AbstractAssemblyModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AbstractAssemblyModalAnalysisAtASpeed]

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
    ) -> "AbstractAssemblyCompoundModalAnalysisAtASpeed._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed":
        return self._Cast_AbstractAssemblyCompoundModalAnalysisAtASpeed(self)

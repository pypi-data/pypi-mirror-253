"""AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5281,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5123,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed")


class AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed(
    _5281.ConicalGearSetCompoundModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5281.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5307,
            )

            return self._parent._cast(_5307.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5345,
            )

            return self._parent._cast(
                _5345.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5247,
            )

            return self._parent._cast(
                _5247.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5260,
            )

            return self._parent._cast(
                _5260.BevelDifferentialGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5265,
            )

            return self._parent._cast(_5265.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5311,
            )

            return self._parent._cast(_5311.HypoidGearSetCompoundModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5348,
            )

            return self._parent._cast(
                _5348.SpiralBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.StraightBevelDiffGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5357,
            )

            return self._parent._cast(
                _5357.StraightBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5375,
            )

            return self._parent._cast(
                _5375.ZerolBevelGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5123.AGMAGleasonConicalGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearSetModalAnalysisAtASpeed]

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
    ) -> "List[_5123.AGMAGleasonConicalGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.AGMAGleasonConicalGearSetModalAnalysisAtASpeed]

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
    ) -> "AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed(self)

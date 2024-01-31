"""SynchroniserHalfCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5362,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SynchroniserHalfCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2604
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5231,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundModalAnalysisAtASpeed")


class SynchroniserHalfCompoundModalAnalysisAtASpeed(
    _5362.SynchroniserPartCompoundModalAnalysisAtASpeed
):
    """SynchroniserHalfCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SynchroniserHalfCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
            parent: "SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5362.SynchroniserPartCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5286,
            )

            return self._parent._cast(_5286.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5324,
            )

            return self._parent._cast(
                _5324.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5272,
            )

            return self._parent._cast(_5272.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5326,
            )

            return self._parent._cast(_5326.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
        ) -> "SynchroniserHalfCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SynchroniserHalfCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2604.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5231.SynchroniserHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SynchroniserHalfModalAnalysisAtASpeed]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5231.SynchroniserHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SynchroniserHalfModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfCompoundModalAnalysisAtASpeed._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed":
        return self._Cast_SynchroniserHalfCompoundModalAnalysisAtASpeed(self)

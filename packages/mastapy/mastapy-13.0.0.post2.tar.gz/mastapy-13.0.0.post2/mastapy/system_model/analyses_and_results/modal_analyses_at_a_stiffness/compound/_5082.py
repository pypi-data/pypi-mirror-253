"""ShaftCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _4988,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "ShaftCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2482
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4954,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ShaftCompoundModalAnalysisAtAStiffness")


class ShaftCompoundModalAnalysisAtAStiffness(
    _4988.AbstractShaftCompoundModalAnalysisAtAStiffness
):
    """ShaftCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_ShaftCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting ShaftCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
            parent: "ShaftCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4988.AbstractShaftCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4989,
            )

            return self._parent._cast(
                _4989.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
            )

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5012,
            )

            return self._parent._cast(_5012.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(_5066.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
        ) -> "ShaftCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ShaftCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

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
    ) -> "List[_4954.ShaftModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ShaftModalAnalysisAtAStiffness]

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
    def planetaries(self: Self) -> "List[ShaftCompoundModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound.ShaftCompoundModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4954.ShaftModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ShaftModalAnalysisAtAStiffness]

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
    ) -> "ShaftCompoundModalAnalysisAtAStiffness._Cast_ShaftCompoundModalAnalysisAtAStiffness":
        return self._Cast_ShaftCompoundModalAnalysisAtAStiffness(self)

"""ExternalCADModelCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5271,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ExternalCADModelCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5168,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ExternalCADModelCompoundModalAnalysisAtASpeed")


class ExternalCADModelCompoundModalAnalysisAtASpeed(
    _5271.ComponentCompoundModalAnalysisAtASpeed
):
    """ExternalCADModelCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ExternalCADModelCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ExternalCADModelCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundModalAnalysisAtASpeed._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed",
            parent: "ExternalCADModelCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "ExternalCADModelCompoundModalAnalysisAtASpeed._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5271.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "ExternalCADModelCompoundModalAnalysisAtASpeed._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5325,
            )

            return self._parent._cast(_5325.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundModalAnalysisAtASpeed._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundModalAnalysisAtASpeed._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundModalAnalysisAtASpeed._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_modal_analysis_at_a_speed(
            self: "ExternalCADModelCompoundModalAnalysisAtASpeed._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed",
        ) -> "ExternalCADModelCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundModalAnalysisAtASpeed._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "ExternalCADModelCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2452.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

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
    ) -> "List[_5168.ExternalCADModelModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ExternalCADModelModalAnalysisAtASpeed]

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
    ) -> "List[_5168.ExternalCADModelModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ExternalCADModelModalAnalysisAtASpeed]

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
    ) -> "ExternalCADModelCompoundModalAnalysisAtASpeed._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed":
        return self._Cast_ExternalCADModelCompoundModalAnalysisAtASpeed(self)

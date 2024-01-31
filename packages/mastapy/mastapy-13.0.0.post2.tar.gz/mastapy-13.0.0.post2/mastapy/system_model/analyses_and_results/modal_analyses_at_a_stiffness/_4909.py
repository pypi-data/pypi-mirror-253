"""ExternalCADModelModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4881,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ExternalCADModelModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.static_loads import _6883


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ExternalCADModelModalAnalysisAtAStiffness")


class ExternalCADModelModalAnalysisAtAStiffness(
    _4881.ComponentModalAnalysisAtAStiffness
):
    """ExternalCADModelModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelModalAnalysisAtAStiffness"
    )

    class _Cast_ExternalCADModelModalAnalysisAtAStiffness:
        """Special nested class for casting ExternalCADModelModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
            parent: "ExternalCADModelModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4881.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def external_cad_model_modal_analysis_at_a_stiffness(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
        ) -> "ExternalCADModelModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "ExternalCADModelModalAnalysisAtAStiffness.TYPE"
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
    def component_load_case(self: Self) -> "_6883.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ExternalCADModelModalAnalysisAtAStiffness._Cast_ExternalCADModelModalAnalysisAtAStiffness":
        return self._Cast_ExternalCADModelModalAnalysisAtAStiffness(self)

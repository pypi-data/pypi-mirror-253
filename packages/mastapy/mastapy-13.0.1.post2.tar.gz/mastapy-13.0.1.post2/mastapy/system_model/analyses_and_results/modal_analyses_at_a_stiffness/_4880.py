"""ClutchModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4896,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ClutchModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578
    from mastapy.system_model.analyses_and_results.static_loads import _6835


__docformat__ = "restructuredtext en"
__all__ = ("ClutchModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="ClutchModalAnalysisAtAStiffness")


class ClutchModalAnalysisAtAStiffness(_4896.CouplingModalAnalysisAtAStiffness):
    """ClutchModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CLUTCH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchModalAnalysisAtAStiffness")

    class _Cast_ClutchModalAnalysisAtAStiffness:
        """Special nested class for casting ClutchModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
            parent: "ClutchModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_modal_analysis_at_a_stiffness(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4896.CouplingModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4957,
            )

            return self._parent._cast(
                _4957.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(_4857.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_modal_analysis_at_a_stiffness(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
        ) -> "ClutchModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchModalAnalysisAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2578.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6835.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchModalAnalysisAtAStiffness._Cast_ClutchModalAnalysisAtAStiffness":
        return self._Cast_ClutchModalAnalysisAtAStiffness(self)

"""RootAssemblyModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4863,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "RootAssemblyModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4934,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="RootAssemblyModalAnalysisAtAStiffness")


class RootAssemblyModalAnalysisAtAStiffness(_4863.AssemblyModalAnalysisAtAStiffness):
    """RootAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyModalAnalysisAtAStiffness"
    )

    class _Cast_RootAssemblyModalAnalysisAtAStiffness:
        """Special nested class for casting RootAssemblyModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
            parent: "RootAssemblyModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def assembly_modal_analysis_at_a_stiffness(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4863.AssemblyModalAnalysisAtAStiffness)

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4856,
            )

            return self._parent._cast(_4856.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def root_assembly_modal_analysis_at_a_stiffness(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
        ) -> "RootAssemblyModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "RootAssemblyModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2474.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis_at_a_stiffness_inputs(
        self: Self,
    ) -> "_4934.ModalAnalysisAtAStiffness":
        """mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ModalAnalysisAtAStiffness

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysisAtAStiffnessInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyModalAnalysisAtAStiffness._Cast_RootAssemblyModalAnalysisAtAStiffness":
        return self._Cast_RootAssemblyModalAnalysisAtAStiffness(self)

"""UnbalancedMassCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4849
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "UnbalancedMassCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2477
    from mastapy.system_model.analyses_and_results.modal_analyses import _4704


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundModalAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundModalAnalysis")


class UnbalancedMassCompoundModalAnalysis(_4849.VirtualComponentCompoundModalAnalysis):
    """UnbalancedMassCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassCompoundModalAnalysis")

    class _Cast_UnbalancedMassCompoundModalAnalysis:
        """Special nested class for casting UnbalancedMassCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
            parent: "UnbalancedMassCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
        ):
            return self._parent._cast(_4849.VirtualComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
        ) -> "UnbalancedMassCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "UnbalancedMassCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2477.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_4704.UnbalancedMassModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.UnbalancedMassModalAnalysis]

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
    ) -> "List[_4704.UnbalancedMassModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.UnbalancedMassModalAnalysis]

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
    ) -> (
        "UnbalancedMassCompoundModalAnalysis._Cast_UnbalancedMassCompoundModalAnalysis"
    ):
        return self._Cast_UnbalancedMassCompoundModalAnalysis(self)

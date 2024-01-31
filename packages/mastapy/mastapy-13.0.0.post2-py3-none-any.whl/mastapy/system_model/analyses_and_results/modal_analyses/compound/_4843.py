"""SynchroniserSleeveCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4842
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SynchroniserSleeveCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.modal_analyses import _4699


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundModalAnalysis")


class SynchroniserSleeveCompoundModalAnalysis(
    _4842.SynchroniserPartCompoundModalAnalysis
):
    """SynchroniserSleeveCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCompoundModalAnalysis"
    )

    class _Cast_SynchroniserSleeveCompoundModalAnalysis:
        """Special nested class for casting SynchroniserSleeveCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
            parent: "SynchroniserSleeveCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
        ):
            return self._parent._cast(_4842.SynchroniserPartCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.CouplingHalfCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
        ) -> "SynchroniserSleeveCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_4699.SynchroniserSleeveModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserSleeveModalAnalysis]

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
    ) -> "List[_4699.SynchroniserSleeveModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserSleeveModalAnalysis]

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
    ) -> "SynchroniserSleeveCompoundModalAnalysis._Cast_SynchroniserSleeveCompoundModalAnalysis":
        return self._Cast_SynchroniserSleeveCompoundModalAnalysis(self)

"""DatumCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "DatumCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2448
    from mastapy.system_model.analyses_and_results.modal_analyses import _4623


__docformat__ = "restructuredtext en"
__all__ = ("DatumCompoundModalAnalysis",)


Self = TypeVar("Self", bound="DatumCompoundModalAnalysis")


class DatumCompoundModalAnalysis(_4752.ComponentCompoundModalAnalysis):
    """DatumCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumCompoundModalAnalysis")

    class _Cast_DatumCompoundModalAnalysis:
        """Special nested class for casting DatumCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis",
            parent: "DatumCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis(
            self: "DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis",
        ):
            return self._parent._cast(_4752.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def datum_compound_modal_analysis(
            self: "DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis",
        ) -> "DatumCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2448.Datum":
        """mastapy.system_model.part_model.Datum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4623.DatumModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.DatumModalAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_4623.DatumModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.DatumModalAnalysis]

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
    ) -> "DatumCompoundModalAnalysis._Cast_DatumCompoundModalAnalysis":
        return self._Cast_DatumCompoundModalAnalysis(self)

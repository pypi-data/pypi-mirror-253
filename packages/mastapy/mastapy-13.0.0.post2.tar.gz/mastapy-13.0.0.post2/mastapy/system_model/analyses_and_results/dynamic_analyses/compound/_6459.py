"""ExternalCADModelCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ExternalCADModelCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelCompoundDynamicAnalysis")


class ExternalCADModelCompoundDynamicAnalysis(_6432.ComponentCompoundDynamicAnalysis):
    """ExternalCADModelCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ExternalCADModelCompoundDynamicAnalysis"
    )

    class _Cast_ExternalCADModelCompoundDynamicAnalysis:
        """Special nested class for casting ExternalCADModelCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelCompoundDynamicAnalysis._Cast_ExternalCADModelCompoundDynamicAnalysis",
            parent: "ExternalCADModelCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_dynamic_analysis(
            self: "ExternalCADModelCompoundDynamicAnalysis._Cast_ExternalCADModelCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6432.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ExternalCADModelCompoundDynamicAnalysis._Cast_ExternalCADModelCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ExternalCADModelCompoundDynamicAnalysis._Cast_ExternalCADModelCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ExternalCADModelCompoundDynamicAnalysis._Cast_ExternalCADModelCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelCompoundDynamicAnalysis._Cast_ExternalCADModelCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def external_cad_model_compound_dynamic_analysis(
            self: "ExternalCADModelCompoundDynamicAnalysis._Cast_ExternalCADModelCompoundDynamicAnalysis",
        ) -> "ExternalCADModelCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelCompoundDynamicAnalysis._Cast_ExternalCADModelCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ExternalCADModelCompoundDynamicAnalysis.TYPE"
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
    ) -> "List[_6330.ExternalCADModelDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ExternalCADModelDynamicAnalysis]

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
    ) -> "List[_6330.ExternalCADModelDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ExternalCADModelDynamicAnalysis]

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
    ) -> "ExternalCADModelCompoundDynamicAnalysis._Cast_ExternalCADModelCompoundDynamicAnalysis":
        return self._Cast_ExternalCADModelCompoundDynamicAnalysis(self)

"""GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7166,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7072,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7166.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def guide_dxf_model_compound_advanced_time_stepping_analysis_for_modulation(
            self: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

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
    ) -> "List[_7072.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7072.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )

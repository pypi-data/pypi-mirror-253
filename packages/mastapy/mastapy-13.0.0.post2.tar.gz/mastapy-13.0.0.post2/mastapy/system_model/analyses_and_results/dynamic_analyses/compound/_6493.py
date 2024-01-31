"""PointLoadCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6529
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PointLoadCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PointLoadCompoundDynamicAnalysis")


class PointLoadCompoundDynamicAnalysis(_6529.VirtualComponentCompoundDynamicAnalysis):
    """PointLoadCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadCompoundDynamicAnalysis")

    class _Cast_PointLoadCompoundDynamicAnalysis:
        """Special nested class for casting PointLoadCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
            parent: "PointLoadCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_dynamic_analysis(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6529.VirtualComponentCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(_6484.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6432,
            )

            return self._parent._cast(_6432.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6486,
            )

            return self._parent._cast(_6486.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def point_load_compound_dynamic_analysis(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
        ) -> "PointLoadCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PointLoad":
        """mastapy.system_model.part_model.PointLoad

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
    ) -> "List[_6364.PointLoadDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PointLoadDynamicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_6364.PointLoadDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PointLoadDynamicAnalysis]

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
    ) -> "PointLoadCompoundDynamicAnalysis._Cast_PointLoadCompoundDynamicAnalysis":
        return self._Cast_PointLoadCompoundDynamicAnalysis(self)

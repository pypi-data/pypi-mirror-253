"""PointLoadCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4849
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "PointLoadCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.modal_analyses import _4668


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundModalAnalysis",)


Self = TypeVar("Self", bound="PointLoadCompoundModalAnalysis")


class PointLoadCompoundModalAnalysis(_4849.VirtualComponentCompoundModalAnalysis):
    """PointLoadCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadCompoundModalAnalysis")

    class _Cast_PointLoadCompoundModalAnalysis:
        """Special nested class for casting PointLoadCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
            parent: "PointLoadCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_modal_analysis(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
        ):
            return self._parent._cast(_4849.VirtualComponentCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4804,
            )

            return self._parent._cast(_4804.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
        ) -> "PointLoadCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadCompoundModalAnalysis.TYPE"):
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
    ) -> "List[_4668.PointLoadModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PointLoadModalAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_4668.PointLoadModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PointLoadModalAnalysis]

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
    ) -> "PointLoadCompoundModalAnalysis._Cast_PointLoadCompoundModalAnalysis":
        return self._Cast_PointLoadCompoundModalAnalysis(self)

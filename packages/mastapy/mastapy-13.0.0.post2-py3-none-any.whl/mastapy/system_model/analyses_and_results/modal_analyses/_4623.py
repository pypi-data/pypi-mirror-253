"""DatumModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4596
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "DatumModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2448
    from mastapy.system_model.analyses_and_results.static_loads import _6869
    from mastapy.system_model.analyses_and_results.system_deflections import _2751


__docformat__ = "restructuredtext en"
__all__ = ("DatumModalAnalysis",)


Self = TypeVar("Self", bound="DatumModalAnalysis")


class DatumModalAnalysis(_4596.ComponentModalAnalysis):
    """DatumModalAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumModalAnalysis")

    class _Cast_DatumModalAnalysis:
        """Special nested class for casting DatumModalAnalysis to subclasses."""

        def __init__(
            self: "DatumModalAnalysis._Cast_DatumModalAnalysis",
            parent: "DatumModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_modal_analysis(
            self: "DatumModalAnalysis._Cast_DatumModalAnalysis",
        ):
            return self._parent._cast(_4596.ComponentModalAnalysis)

        @property
        def part_modal_analysis(self: "DatumModalAnalysis._Cast_DatumModalAnalysis"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4661

            return self._parent._cast(_4661.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "DatumModalAnalysis._Cast_DatumModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "DatumModalAnalysis._Cast_DatumModalAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "DatumModalAnalysis._Cast_DatumModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumModalAnalysis._Cast_DatumModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "DatumModalAnalysis._Cast_DatumModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def datum_modal_analysis(
            self: "DatumModalAnalysis._Cast_DatumModalAnalysis",
        ) -> "DatumModalAnalysis":
            return self._parent

        def __getattr__(self: "DatumModalAnalysis._Cast_DatumModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumModalAnalysis.TYPE"):
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
    def component_load_case(self: Self) -> "_6869.DatumLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2751.DatumSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "DatumModalAnalysis._Cast_DatumModalAnalysis":
        return self._Cast_DatumModalAnalysis(self)

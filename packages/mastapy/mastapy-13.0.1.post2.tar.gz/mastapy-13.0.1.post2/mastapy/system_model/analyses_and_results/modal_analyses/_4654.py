"""ModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "ModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4657, _4655
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329


__docformat__ = "restructuredtext en"
__all__ = ("ModalAnalysis",)


Self = TypeVar("Self", bound="ModalAnalysis")


class ModalAnalysis(_7550.StaticLoadAnalysisCase):
    """ModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalAnalysis")

    class _Cast_ModalAnalysis:
        """Special nested class for casting ModalAnalysis to subclasses."""

        def __init__(
            self: "ModalAnalysis._Cast_ModalAnalysis", parent: "ModalAnalysis"
        ):
            self._parent = parent

        @property
        def static_load_analysis_case(self: "ModalAnalysis._Cast_ModalAnalysis"):
            return self._parent._cast(_7550.StaticLoadAnalysisCase)

        @property
        def analysis_case(self: "ModalAnalysis._Cast_ModalAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.AnalysisCase)

        @property
        def context(self: "ModalAnalysis._Cast_ModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "ModalAnalysis._Cast_ModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.ModalAnalysisForHarmonicAnalysis)

        @property
        def modal_analysis(
            self: "ModalAnalysis._Cast_ModalAnalysis",
        ) -> "ModalAnalysis":
            return self._parent

        def __getattr__(self: "ModalAnalysis._Cast_ModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_settings(self: Self) -> "_4657.ModalAnalysisOptions":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bar_model_export(self: Self) -> "_4655.ModalAnalysisBarModelFEExportOptions":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysisBarModelFEExportOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BarModelExport

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis_results(self: Self) -> "_6329.DynamicAnalysis":
        """mastapy.system_model.analyses_and_results.dynamic_analyses.DynamicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysisResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ModalAnalysis._Cast_ModalAnalysis":
        return self._Cast_ModalAnalysis(self)

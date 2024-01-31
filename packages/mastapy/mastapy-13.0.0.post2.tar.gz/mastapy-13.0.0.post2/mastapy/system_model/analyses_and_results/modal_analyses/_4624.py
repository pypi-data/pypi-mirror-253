"""DynamicModelForModalAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "DynamicModelForModalAnalysis",
)


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelForModalAnalysis",)


Self = TypeVar("Self", bound="DynamicModelForModalAnalysis")


class DynamicModelForModalAnalysis(_6328.DynamicAnalysis):
    """DynamicModelForModalAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelForModalAnalysis")

    class _Cast_DynamicModelForModalAnalysis:
        """Special nested class for casting DynamicModelForModalAnalysis to subclasses."""

        def __init__(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
            parent: "DynamicModelForModalAnalysis",
        ):
            self._parent = parent

        @property
        def dynamic_analysis(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ):
            return self._parent._cast(_6328.DynamicAnalysis)

        @property
        def fe_analysis(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.AnalysisCase)

        @property
        def context(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def dynamic_model_for_modal_analysis(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
        ) -> "DynamicModelForModalAnalysis":
            return self._parent

        def __getattr__(
            self: "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelForModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelForModalAnalysis._Cast_DynamicModelForModalAnalysis":
        return self._Cast_DynamicModelForModalAnalysis(self)

"""DynamicModelAtAStiffness"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "DynamicModelAtAStiffness",
)


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelAtAStiffness",)


Self = TypeVar("Self", bound="DynamicModelAtAStiffness")


class DynamicModelAtAStiffness(_6329.DynamicAnalysis):
    """DynamicModelAtAStiffness

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelAtAStiffness")

    class _Cast_DynamicModelAtAStiffness:
        """Special nested class for casting DynamicModelAtAStiffness to subclasses."""

        def __init__(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
            parent: "DynamicModelAtAStiffness",
        ):
            self._parent = parent

        @property
        def dynamic_analysis(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ):
            return self._parent._cast(_6329.DynamicAnalysis)

        @property
        def fe_analysis(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.AnalysisCase)

        @property
        def context(self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness"):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def dynamic_model_at_a_stiffness(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "DynamicModelAtAStiffness":
            return self._parent

        def __getattr__(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness":
        return self._Cast_DynamicModelAtAStiffness(self)

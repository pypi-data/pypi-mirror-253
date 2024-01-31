"""DynamicModelAtAStiffnessAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results import _2620
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_AT_A_STIFFNESS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "DynamicModelAtAStiffnessAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelAtAStiffnessAnalysis",)


Self = TypeVar("Self", bound="DynamicModelAtAStiffnessAnalysis")


class DynamicModelAtAStiffnessAnalysis(_2620.SingleAnalysis):
    """DynamicModelAtAStiffnessAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_AT_A_STIFFNESS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelAtAStiffnessAnalysis")

    class _Cast_DynamicModelAtAStiffnessAnalysis:
        """Special nested class for casting DynamicModelAtAStiffnessAnalysis to subclasses."""

        def __init__(
            self: "DynamicModelAtAStiffnessAnalysis._Cast_DynamicModelAtAStiffnessAnalysis",
            parent: "DynamicModelAtAStiffnessAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "DynamicModelAtAStiffnessAnalysis._Cast_DynamicModelAtAStiffnessAnalysis",
        ):
            return self._parent._cast(_2620.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "DynamicModelAtAStiffnessAnalysis._Cast_DynamicModelAtAStiffnessAnalysis",
        ):
            from mastapy import _7552

            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def dynamic_model_at_a_stiffness_analysis(
            self: "DynamicModelAtAStiffnessAnalysis._Cast_DynamicModelAtAStiffnessAnalysis",
        ) -> "DynamicModelAtAStiffnessAnalysis":
            return self._parent

        def __getattr__(
            self: "DynamicModelAtAStiffnessAnalysis._Cast_DynamicModelAtAStiffnessAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelAtAStiffnessAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelAtAStiffnessAnalysis._Cast_DynamicModelAtAStiffnessAnalysis":
        return self._Cast_DynamicModelAtAStiffnessAnalysis(self)

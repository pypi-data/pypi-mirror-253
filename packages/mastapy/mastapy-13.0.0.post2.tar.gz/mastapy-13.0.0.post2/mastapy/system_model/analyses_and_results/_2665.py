"""CompoundDynamicModelForModalAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results import _2619
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPOUND_DYNAMIC_MODEL_FOR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults",
    "CompoundDynamicModelForModalAnalysis",
)


__docformat__ = "restructuredtext en"
__all__ = ("CompoundDynamicModelForModalAnalysis",)


Self = TypeVar("Self", bound="CompoundDynamicModelForModalAnalysis")


class CompoundDynamicModelForModalAnalysis(_2619.CompoundAnalysis):
    """CompoundDynamicModelForModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_DYNAMIC_MODEL_FOR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CompoundDynamicModelForModalAnalysis")

    class _Cast_CompoundDynamicModelForModalAnalysis:
        """Special nested class for casting CompoundDynamicModelForModalAnalysis to subclasses."""

        def __init__(
            self: "CompoundDynamicModelForModalAnalysis._Cast_CompoundDynamicModelForModalAnalysis",
            parent: "CompoundDynamicModelForModalAnalysis",
        ):
            self._parent = parent

        @property
        def compound_analysis(
            self: "CompoundDynamicModelForModalAnalysis._Cast_CompoundDynamicModelForModalAnalysis",
        ):
            return self._parent._cast(_2619.CompoundAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "CompoundDynamicModelForModalAnalysis._Cast_CompoundDynamicModelForModalAnalysis",
        ):
            from mastapy import _7552

            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def compound_dynamic_model_for_modal_analysis(
            self: "CompoundDynamicModelForModalAnalysis._Cast_CompoundDynamicModelForModalAnalysis",
        ) -> "CompoundDynamicModelForModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CompoundDynamicModelForModalAnalysis._Cast_CompoundDynamicModelForModalAnalysis",
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
        self: Self, instance_to_wrap: "CompoundDynamicModelForModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CompoundDynamicModelForModalAnalysis._Cast_CompoundDynamicModelForModalAnalysis":
        return self._Cast_CompoundDynamicModelForModalAnalysis(self)

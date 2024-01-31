"""StabilityAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results import _2620
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "StabilityAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("StabilityAnalysis",)


Self = TypeVar("Self", bound="StabilityAnalysis")


class StabilityAnalysis(_2620.SingleAnalysis):
    """StabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StabilityAnalysis")

    class _Cast_StabilityAnalysis:
        """Special nested class for casting StabilityAnalysis to subclasses."""

        def __init__(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
            parent: "StabilityAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(self: "StabilityAnalysis._Cast_StabilityAnalysis"):
            return self._parent._cast(_2620.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
        ):
            from mastapy import _7552

            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def stability_analysis(
            self: "StabilityAnalysis._Cast_StabilityAnalysis",
        ) -> "StabilityAnalysis":
            return self._parent

        def __getattr__(self: "StabilityAnalysis._Cast_StabilityAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StabilityAnalysis._Cast_StabilityAnalysis":
        return self._Cast_StabilityAnalysis(self)

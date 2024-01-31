"""ModalAnalysisForHarmonicAnalysis"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results import _2620
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "ModalAnalysisForHarmonicAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("ModalAnalysisForHarmonicAnalysis",)


Self = TypeVar("Self", bound="ModalAnalysisForHarmonicAnalysis")


class ModalAnalysisForHarmonicAnalysis(_2620.SingleAnalysis):
    """ModalAnalysisForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModalAnalysisForHarmonicAnalysis")

    class _Cast_ModalAnalysisForHarmonicAnalysis:
        """Special nested class for casting ModalAnalysisForHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ModalAnalysisForHarmonicAnalysis._Cast_ModalAnalysisForHarmonicAnalysis",
            parent: "ModalAnalysisForHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def single_analysis(
            self: "ModalAnalysisForHarmonicAnalysis._Cast_ModalAnalysisForHarmonicAnalysis",
        ):
            return self._parent._cast(_2620.SingleAnalysis)

        @property
        def marshal_by_ref_object_permanent(
            self: "ModalAnalysisForHarmonicAnalysis._Cast_ModalAnalysisForHarmonicAnalysis",
        ):
            from mastapy import _7552

            return self._parent._cast(_7552.MarshalByRefObjectPermanent)

        @property
        def modal_analysis_for_harmonic_analysis(
            self: "ModalAnalysisForHarmonicAnalysis._Cast_ModalAnalysisForHarmonicAnalysis",
        ) -> "ModalAnalysisForHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ModalAnalysisForHarmonicAnalysis._Cast_ModalAnalysisForHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModalAnalysisForHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ModalAnalysisForHarmonicAnalysis._Cast_ModalAnalysisForHarmonicAnalysis":
        return self._Cast_ModalAnalysisForHarmonicAnalysis(self)

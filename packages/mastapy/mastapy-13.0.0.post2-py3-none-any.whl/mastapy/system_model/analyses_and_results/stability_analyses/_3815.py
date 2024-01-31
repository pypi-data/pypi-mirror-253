"""DatumStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "DatumStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2448
    from mastapy.system_model.analyses_and_results.static_loads import _6869


__docformat__ = "restructuredtext en"
__all__ = ("DatumStabilityAnalysis",)


Self = TypeVar("Self", bound="DatumStabilityAnalysis")


class DatumStabilityAnalysis(_3788.ComponentStabilityAnalysis):
    """DatumStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumStabilityAnalysis")

    class _Cast_DatumStabilityAnalysis:
        """Special nested class for casting DatumStabilityAnalysis to subclasses."""

        def __init__(
            self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis",
            parent: "DatumStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_stability_analysis(
            self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis",
        ):
            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def datum_stability_analysis(
            self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis",
        ) -> "DatumStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumStabilityAnalysis.TYPE"):
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
    def cast_to(self: Self) -> "DatumStabilityAnalysis._Cast_DatumStabilityAnalysis":
        return self._Cast_DatumStabilityAnalysis(self)

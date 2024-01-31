"""ClutchHalfHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5717
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ClutchHalfHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6833
    from mastapy.system_model.analyses_and_results.system_deflections import _2712


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfHarmonicAnalysis",)


Self = TypeVar("Self", bound="ClutchHalfHarmonicAnalysis")


class ClutchHalfHarmonicAnalysis(_5717.CouplingHalfHarmonicAnalysis):
    """ClutchHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfHarmonicAnalysis")

    class _Cast_ClutchHalfHarmonicAnalysis:
        """Special nested class for casting ClutchHalfHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
            parent: "ClutchHalfHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ):
            return self._parent._cast(_5717.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
        ) -> "ClutchHalfHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2579.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6833.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2712.ClutchHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchHalfHarmonicAnalysis._Cast_ClutchHalfHarmonicAnalysis":
        return self._Cast_ClutchHalfHarmonicAnalysis(self)

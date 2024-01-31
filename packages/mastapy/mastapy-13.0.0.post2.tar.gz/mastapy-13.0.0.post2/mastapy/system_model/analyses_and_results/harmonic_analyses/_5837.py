"""WormGearHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "WormGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.static_loads import _6982
    from mastapy.system_model.analyses_and_results.system_deflections import _2838


__docformat__ = "restructuredtext en"
__all__ = ("WormGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="WormGearHarmonicAnalysis")


class WormGearHarmonicAnalysis(_5752.GearHarmonicAnalysis):
    """WormGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearHarmonicAnalysis")

    class _Cast_WormGearHarmonicAnalysis:
        """Special nested class for casting WormGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
            parent: "WormGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_harmonic_analysis(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ):
            return self._parent._cast(_5752.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis",
        ) -> "WormGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6982.WormGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2838.WormGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.WormGearSystemDeflection

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
    ) -> "WormGearHarmonicAnalysis._Cast_WormGearHarmonicAnalysis":
        return self._Cast_WormGearHarmonicAnalysis(self)

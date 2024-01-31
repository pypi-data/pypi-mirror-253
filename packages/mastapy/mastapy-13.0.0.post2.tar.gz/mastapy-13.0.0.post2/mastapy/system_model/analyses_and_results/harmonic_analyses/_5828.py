"""SynchroniserPartHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5717
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "SynchroniserPartHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.system_deflections import _2822


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartHarmonicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartHarmonicAnalysis")


class SynchroniserPartHarmonicAnalysis(_5717.CouplingHalfHarmonicAnalysis):
    """SynchroniserPartHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartHarmonicAnalysis")

    class _Cast_SynchroniserPartHarmonicAnalysis:
        """Special nested class for casting SynchroniserPartHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
            parent: "SynchroniserPartHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_harmonic_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            return self._parent._cast(_5717.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.SynchroniserSleeveHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
        ) -> "SynchroniserPartHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2822.SynchroniserPartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserPartSystemDeflection

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
    ) -> "SynchroniserPartHarmonicAnalysis._Cast_SynchroniserPartHarmonicAnalysis":
        return self._Cast_SynchroniserPartHarmonicAnalysis(self)

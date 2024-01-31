"""CVTHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CVTHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.system_deflections import _2734


__docformat__ = "restructuredtext en"
__all__ = ("CVTHarmonicAnalysis",)


Self = TypeVar("Self", bound="CVTHarmonicAnalysis")


class CVTHarmonicAnalysis(_5688.BeltDriveHarmonicAnalysis):
    """CVTHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTHarmonicAnalysis")

    class _Cast_CVTHarmonicAnalysis:
        """Special nested class for casting CVTHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
            parent: "CVTHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            return self._parent._cast(_5688.BeltDriveHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5677,
            )

            return self._parent._cast(_5677.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "CVTHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2734.CVTSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis":
        return self._Cast_CVTHarmonicAnalysis(self)

"""ClutchHalfCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5918
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ClutchHalfCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5701


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ClutchHalfCompoundHarmonicAnalysis")


class ClutchHalfCompoundHarmonicAnalysis(_5918.CouplingHalfCompoundHarmonicAnalysis):
    """ClutchHalfCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfCompoundHarmonicAnalysis")

    class _Cast_ClutchHalfCompoundHarmonicAnalysis:
        """Special nested class for casting ClutchHalfCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
            parent: "ClutchHalfCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5918.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
        ) -> "ClutchHalfCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ClutchHalfCompoundHarmonicAnalysis.TYPE"
    ):
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5701.ClutchHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ClutchHalfHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5701.ClutchHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ClutchHalfHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchHalfCompoundHarmonicAnalysis._Cast_ClutchHalfCompoundHarmonicAnalysis":
        return self._Cast_ClutchHalfCompoundHarmonicAnalysis(self)

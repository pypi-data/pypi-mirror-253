"""CVTPulleyCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5967
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CVTPulleyCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5722


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CVTPulleyCompoundHarmonicAnalysis")


class CVTPulleyCompoundHarmonicAnalysis(_5967.PulleyCompoundHarmonicAnalysis):
    """CVTPulleyCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyCompoundHarmonicAnalysis")

    class _Cast_CVTPulleyCompoundHarmonicAnalysis:
        """Special nested class for casting CVTPulleyCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
            parent: "CVTPulleyCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def pulley_compound_harmonic_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5967.PulleyCompoundHarmonicAnalysis)

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5918,
            )

            return self._parent._cast(_5918.CouplingHalfCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
        ) -> "CVTPulleyCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CVTPulleyCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5722.CVTPulleyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CVTPulleyHarmonicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_5722.CVTPulleyHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CVTPulleyHarmonicAnalysis]

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
    ) -> "CVTPulleyCompoundHarmonicAnalysis._Cast_CVTPulleyCompoundHarmonicAnalysis":
        return self._Cast_CVTPulleyCompoundHarmonicAnalysis(self)

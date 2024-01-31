"""SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6178,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6125,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation"
)


class SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation(
    _6178.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
):
    """SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6178.CouplingHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6216,
            )

            return self._parent._cast(
                _6216.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6164,
            )

            return self._parent._cast(
                _6164.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6253,
            )

            return self._parent._cast(
                _6253.SynchroniserHalfCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6255,
            )

            return self._parent._cast(
                _6255.SynchroniserSleeveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_compound_harmonic_analysis_of_single_excitation(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation",
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
        self: Self,
        instance_to_wrap: "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6125.SynchroniserPartHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SynchroniserPartHarmonicAnalysisOfSingleExcitation]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_6125.SynchroniserPartHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SynchroniserPartHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_SynchroniserPartCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )

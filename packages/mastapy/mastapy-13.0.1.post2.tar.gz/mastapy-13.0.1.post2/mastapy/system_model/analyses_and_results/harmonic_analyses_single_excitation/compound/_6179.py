"""CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6148,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6048,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation"
)


class CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6148.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6148.BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6204,
            )

            return self._parent._cast(
                _6204.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6174,
            )

            return self._parent._cast(
                _6174.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6048.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6048.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )

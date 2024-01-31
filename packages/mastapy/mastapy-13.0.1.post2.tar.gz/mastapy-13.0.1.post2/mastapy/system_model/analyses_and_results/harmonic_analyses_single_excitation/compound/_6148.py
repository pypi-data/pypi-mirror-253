"""BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6204,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2268
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6017,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation")


class BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6204.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6204.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6174,
            )

            return self._parent._cast(
                _6174.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6179,
            )

            return self._parent._cast(
                _6179.CVTBeltConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def belt_connection_compound_harmonic_analysis_of_single_excitation(
            self: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2268.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6017.BeltConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BeltConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6017.BeltConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BeltConnectionHarmonicAnalysisOfSingleExcitation]

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
    ) -> "BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BeltConnectionCompoundHarmonicAnalysisOfSingleExcitation(self)

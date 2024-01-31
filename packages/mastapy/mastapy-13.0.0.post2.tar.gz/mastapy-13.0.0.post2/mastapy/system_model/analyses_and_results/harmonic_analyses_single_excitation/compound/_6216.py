"""OilSealCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6174,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "OilSealCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6087,
    )


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="OilSealCompoundHarmonicAnalysisOfSingleExcitation")


class OilSealCompoundHarmonicAnalysisOfSingleExcitation(
    _6174.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
):
    """OilSealCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting OilSealCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "OilSealCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6174.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6215,
            )

            return self._parent._cast(
                _6215.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6217,
            )

            return self._parent._cast(
                _6217.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis_of_single_excitation(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "OilSealCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "OilSealCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.OilSeal":
        """mastapy.system_model.part_model.OilSeal

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
    ) -> "List[_6087.OilSealHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.OilSealHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6087.OilSealHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.OilSealHarmonicAnalysisOfSingleExcitation]

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
    ) -> "OilSealCompoundHarmonicAnalysisOfSingleExcitation._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_OilSealCompoundHarmonicAnalysisOfSingleExcitation(self)

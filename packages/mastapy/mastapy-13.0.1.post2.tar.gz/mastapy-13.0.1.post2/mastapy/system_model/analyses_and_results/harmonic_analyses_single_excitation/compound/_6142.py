"""AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6174,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6011,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


class AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6174.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6174.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6163,
            )

            return self._parent._cast(
                _6163.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6183,
            )

            return self._parent._cast(
                _6183.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.CycloidalDiscPlanetaryBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6222,
            )

            return self._parent._cast(
                _6222.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6236,
            )

            return self._parent._cast(
                _6236.ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6011.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6011.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )

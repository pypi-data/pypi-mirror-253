"""ShaftHubConnectionCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5915
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ShaftHubConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5807


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ShaftHubConnectionCompoundHarmonicAnalysis")


class ShaftHubConnectionCompoundHarmonicAnalysis(
    _5915.ConnectorCompoundHarmonicAnalysis
):
    """ShaftHubConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionCompoundHarmonicAnalysis"
    )

    class _Cast_ShaftHubConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting ShaftHubConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
            parent: "ShaftHubConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connector_compound_harmonic_analysis(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5915.ConnectorCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(_5956.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
        ) -> "ShaftHubConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

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
    ) -> "List[_5807.ShaftHubConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftHubConnectionHarmonicAnalysis]

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
    def planetaries(self: Self) -> "List[ShaftHubConnectionCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.ShaftHubConnectionCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5807.ShaftHubConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftHubConnectionHarmonicAnalysis]

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
    ) -> "ShaftHubConnectionCompoundHarmonicAnalysis._Cast_ShaftHubConnectionCompoundHarmonicAnalysis":
        return self._Cast_ShaftHubConnectionCompoundHarmonicAnalysis(self)

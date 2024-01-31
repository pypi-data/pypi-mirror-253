"""OilSealCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3933
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "OilSealCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.stability_analyses import _3843


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="OilSealCompoundStabilityAnalysis")


class OilSealCompoundStabilityAnalysis(_3933.ConnectorCompoundStabilityAnalysis):
    """OilSealCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealCompoundStabilityAnalysis")

    class _Cast_OilSealCompoundStabilityAnalysis:
        """Special nested class for casting OilSealCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
            parent: "OilSealCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connector_compound_stability_analysis(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3933.ConnectorCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(_3922.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def oil_seal_compound_stability_analysis(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
        ) -> "OilSealCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealCompoundStabilityAnalysis.TYPE"):
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
    ) -> "List[_3843.OilSealStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.OilSealStabilityAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_3843.OilSealStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.OilSealStabilityAnalysis]

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
    ) -> "OilSealCompoundStabilityAnalysis._Cast_OilSealCompoundStabilityAnalysis":
        return self._Cast_OilSealCompoundStabilityAnalysis(self)

"""ClutchHalfCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3936
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ClutchHalfCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.stability_analyses import _3785


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ClutchHalfCompoundStabilityAnalysis")


class ClutchHalfCompoundStabilityAnalysis(_3936.CouplingHalfCompoundStabilityAnalysis):
    """ClutchHalfCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfCompoundStabilityAnalysis")

    class _Cast_ClutchHalfCompoundStabilityAnalysis:
        """Special nested class for casting ClutchHalfCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
            parent: "ClutchHalfCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_stability_analysis(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3936.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3922,
            )

            return self._parent._cast(_3922.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
        ) -> "ClutchHalfCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ClutchHalfCompoundStabilityAnalysis.TYPE"
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
    ) -> "List[_3785.ClutchHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ClutchHalfStabilityAnalysis]

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
    ) -> "List[_3785.ClutchHalfStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ClutchHalfStabilityAnalysis]

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
    ) -> (
        "ClutchHalfCompoundStabilityAnalysis._Cast_ClutchHalfCompoundStabilityAnalysis"
    ):
        return self._Cast_ClutchHalfCompoundStabilityAnalysis(self)

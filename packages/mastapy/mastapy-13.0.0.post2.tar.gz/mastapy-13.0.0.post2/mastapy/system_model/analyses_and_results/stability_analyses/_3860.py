"""ShaftHubConnectionStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3799
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ShaftHubConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6949


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="ShaftHubConnectionStabilityAnalysis")


class ShaftHubConnectionStabilityAnalysis(_3799.ConnectorStabilityAnalysis):
    """ShaftHubConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnectionStabilityAnalysis")

    class _Cast_ShaftHubConnectionStabilityAnalysis:
        """Special nested class for casting ShaftHubConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
            parent: "ShaftHubConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connector_stability_analysis(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ):
            return self._parent._cast(_3799.ConnectorStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3788,
            )

            return self._parent._cast(_3788.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
        ) -> "ShaftHubConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionStabilityAnalysis.TYPE"
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
    def component_load_case(self: Self) -> "_6949.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ShaftHubConnectionStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> (
        "ShaftHubConnectionStabilityAnalysis._Cast_ShaftHubConnectionStabilityAnalysis"
    ):
        return self._Cast_ShaftHubConnectionStabilityAnalysis(self)

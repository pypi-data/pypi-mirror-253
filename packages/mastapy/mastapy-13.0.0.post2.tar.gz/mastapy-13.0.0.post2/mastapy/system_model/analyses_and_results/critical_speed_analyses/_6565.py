"""ClutchHalfCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6581
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ClutchHalfCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2579
    from mastapy.system_model.analyses_and_results.static_loads import _6833


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ClutchHalfCriticalSpeedAnalysis")


class ClutchHalfCriticalSpeedAnalysis(_6581.CouplingHalfCriticalSpeedAnalysis):
    """ClutchHalfCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfCriticalSpeedAnalysis")

    class _Cast_ClutchHalfCriticalSpeedAnalysis:
        """Special nested class for casting ClutchHalfCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
            parent: "ClutchHalfCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_critical_speed_analysis(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6581.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
        ) -> "ClutchHalfCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfCriticalSpeedAnalysis.TYPE"):
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
    def component_load_case(self: Self) -> "_6833.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchHalfCriticalSpeedAnalysis._Cast_ClutchHalfCriticalSpeedAnalysis":
        return self._Cast_ClutchHalfCriticalSpeedAnalysis(self)

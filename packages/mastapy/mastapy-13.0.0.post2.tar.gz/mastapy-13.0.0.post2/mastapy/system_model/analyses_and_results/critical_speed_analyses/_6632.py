"""PowerLoadCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6667
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PowerLoadCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6939


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PowerLoadCriticalSpeedAnalysis")


class PowerLoadCriticalSpeedAnalysis(_6667.VirtualComponentCriticalSpeedAnalysis):
    """PowerLoadCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadCriticalSpeedAnalysis")

    class _Cast_PowerLoadCriticalSpeedAnalysis:
        """Special nested class for casting PowerLoadCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
            parent: "PowerLoadCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6667.VirtualComponentCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(_6622.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6567,
            )

            return self._parent._cast(_6567.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
        ) -> "PowerLoadCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PowerLoadCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6939.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

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
    ) -> "PowerLoadCriticalSpeedAnalysis._Cast_PowerLoadCriticalSpeedAnalysis":
        return self._Cast_PowerLoadCriticalSpeedAnalysis(self)

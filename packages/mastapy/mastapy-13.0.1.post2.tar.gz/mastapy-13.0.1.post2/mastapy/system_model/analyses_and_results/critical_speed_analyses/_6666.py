"""TorqueConverterTurbineCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "TorqueConverterTurbineCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6976


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCriticalSpeedAnalysis")


class TorqueConverterTurbineCriticalSpeedAnalysis(
    _6582.CouplingHalfCriticalSpeedAnalysis
):
    """TorqueConverterTurbineCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineCriticalSpeedAnalysis"
    )

    class _Cast_TorqueConverterTurbineCriticalSpeedAnalysis:
        """Special nested class for casting TorqueConverterTurbineCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
            parent: "TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6582.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
        ) -> "TorqueConverterTurbineCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6976.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

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
    ) -> "TorqueConverterTurbineCriticalSpeedAnalysis._Cast_TorqueConverterTurbineCriticalSpeedAnalysis":
        return self._Cast_TorqueConverterTurbineCriticalSpeedAnalysis(self)

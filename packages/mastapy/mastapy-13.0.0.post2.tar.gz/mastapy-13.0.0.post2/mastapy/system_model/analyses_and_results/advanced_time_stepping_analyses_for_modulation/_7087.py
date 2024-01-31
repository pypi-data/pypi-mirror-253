"""MeasurementComponentAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7133,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2463
    from mastapy.system_model.analyses_and_results.static_loads import _6922
    from mastapy.system_model.analyses_and_results.system_deflections import _2780


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="MeasurementComponentAdvancedTimeSteppingAnalysisForModulation"
)


class MeasurementComponentAdvancedTimeSteppingAnalysisForModulation(
    _7133.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
):
    """MeasurementComponentAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting MeasurementComponentAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
            parent: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7133.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2463.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6922.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2780.MeasurementComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MeasurementComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_MeasurementComponentAdvancedTimeSteppingAnalysisForModulation(
            self
        )

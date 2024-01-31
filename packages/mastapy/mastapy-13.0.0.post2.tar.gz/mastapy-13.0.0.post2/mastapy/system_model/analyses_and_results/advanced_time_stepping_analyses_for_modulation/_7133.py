"""VirtualComponentAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7088,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.system_deflections import _2835


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="VirtualComponentAdvancedTimeSteppingAnalysisForModulation"
)


class VirtualComponentAdvancedTimeSteppingAnalysisForModulation(
    _7088.MountableComponentAdvancedTimeSteppingAnalysisForModulation
):
    """VirtualComponentAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting VirtualComponentAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
            parent: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7088.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7087,
            )

            return self._parent._cast(
                _7087.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7098,
            )

            return self._parent._cast(
                _7098.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7132,
            )

            return self._parent._cast(
                _7132.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "VirtualComponentAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2835.VirtualComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection

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
    ) -> "VirtualComponentAdvancedTimeSteppingAnalysisForModulation._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_VirtualComponentAdvancedTimeSteppingAnalysisForModulation(
            self
        )

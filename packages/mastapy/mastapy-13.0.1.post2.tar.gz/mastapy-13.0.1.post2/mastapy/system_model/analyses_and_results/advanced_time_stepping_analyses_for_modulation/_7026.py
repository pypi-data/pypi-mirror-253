"""BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7022,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2518
    from mastapy.system_model.analyses_and_results.system_deflections import _2705


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation"
)


class BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation(
    _7022.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
):
    """BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7022.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7014,
            )

            return self._parent._cast(
                _7014.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7043,
            )

            return self._parent._cast(
                _7043.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7069,
            )

            return self._parent._cast(
                _7069.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2518.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

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
    ) -> "_2705.BevelDifferentialSunGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection

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
    ) -> "BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation(
            self
        )

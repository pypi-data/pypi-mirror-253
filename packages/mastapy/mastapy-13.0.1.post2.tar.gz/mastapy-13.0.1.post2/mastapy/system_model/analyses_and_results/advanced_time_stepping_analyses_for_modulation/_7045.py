"""ConicalGearSetAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7071,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2524
    from mastapy.system_model.analyses_and_results.system_deflections import _2725


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ConicalGearSetAdvancedTimeSteppingAnalysisForModulation")


class ConicalGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7071.GearSetAdvancedTimeSteppingAnalysisForModulation
):
    """ConicalGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ConicalGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7071.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7016,
            )

            return self._parent._cast(
                _7016.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7024,
            )

            return self._parent._cast(
                _7024.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7029,
            )

            return self._parent._cast(
                _7029.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7080,
            )

            return self._parent._cast(
                _7080.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7083,
            )

            return self._parent._cast(
                _7083.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7140,
            )

            return self._parent._cast(
                _7140.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2524.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2725.ConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection

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
    ) -> "ConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ConicalGearSetAdvancedTimeSteppingAnalysisForModulation(self)

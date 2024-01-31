"""AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7045,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514
    from mastapy.system_model.analyses_and_results.system_deflections import _2690


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation"
)


class AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7045.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
):
    """AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7045.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7071,
            )

            return self._parent._cast(
                _7071.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7024,
            )

            return self._parent._cast(
                _7024.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7029,
            )

            return self._parent._cast(
                _7029.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7140,
            )

            return self._parent._cast(
                _7140.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2514.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2690.AGMAGleasonConicalGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection

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
    ) -> "AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation(
            self
        )

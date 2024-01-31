"""ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7029,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.static_loads import _6988
    from mastapy.system_model.analyses_and_results.system_deflections import _2840
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7138,
        _7139,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation"
)


class ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation(
    _7029.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
):
    """ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
            parent: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7029.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7016,
            )

            return self._parent._cast(
                _7016.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7071,
            )

            return self._parent._cast(
                _7071.GearSetAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2554.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6988.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2840.ZerolBevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gears_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7138.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "List[_7139.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation(
            self
        )

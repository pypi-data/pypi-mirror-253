"""MassDiscAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7133,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "MassDiscAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.static_loads import _6921
    from mastapy.system_model.analyses_and_results.system_deflections import _2779


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="MassDiscAdvancedTimeSteppingAnalysisForModulation")


class MassDiscAdvancedTimeSteppingAnalysisForModulation(
    _7133.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
):
    """MassDiscAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting MassDiscAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
            parent: "MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7133.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7088,
            )

            return self._parent._cast(
                _7088.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
        ) -> "MassDiscAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "MassDiscAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6921.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2779.MassDiscSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[MassDiscAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.MassDiscAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "MassDiscAdvancedTimeSteppingAnalysisForModulation._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_MassDiscAdvancedTimeSteppingAnalysisForModulation(self)

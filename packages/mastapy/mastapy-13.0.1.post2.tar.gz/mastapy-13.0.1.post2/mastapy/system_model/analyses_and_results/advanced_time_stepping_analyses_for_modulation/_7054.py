"""CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7110,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2568
    from mastapy.system_model.analyses_and_results.static_loads import _6858
    from mastapy.system_model.analyses_and_results.system_deflections import _2735


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation"
)


class CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation(
    _7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
):
    """CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
            parent: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7110.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7006,
            )

            return self._parent._cast(
                _7006.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2568.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6858.CycloidalAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

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
    ) -> "_2735.CycloidalAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalAssemblySystemDeflection

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
    ) -> "CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation(
            self
        )

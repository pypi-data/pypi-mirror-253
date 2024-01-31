"""RollingRingAssemblyAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "RollingRingAssemblyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6946
    from mastapy.system_model.analyses_and_results.system_deflections import _2797


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="RollingRingAssemblyAdvancedSystemDeflection")


class RollingRingAssemblyAdvancedSystemDeflection(
    _7374.SpecialisedAssemblyAdvancedSystemDeflection
):
    """RollingRingAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyAdvancedSystemDeflection"
    )

    class _Cast_RollingRingAssemblyAdvancedSystemDeflection:
        """Special nested class for casting RollingRingAssemblyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
            parent: "RollingRingAssemblyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7374.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7270,
            )

            return self._parent._cast(_7270.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_advanced_system_deflection(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
        ) -> "RollingRingAssemblyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2597.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6946.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2797.RollingRingAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingAssemblyAdvancedSystemDeflection._Cast_RollingRingAssemblyAdvancedSystemDeflection":
        return self._Cast_RollingRingAssemblyAdvancedSystemDeflection(self)

"""SynchroniserAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "SynchroniserAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.static_loads import _6968
    from mastapy.system_model.analyses_and_results.system_deflections import _2824


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserAdvancedSystemDeflection")


class SynchroniserAdvancedSystemDeflection(
    _7373.SpecialisedAssemblyAdvancedSystemDeflection
):
    """SynchroniserAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserAdvancedSystemDeflection")

    class _Cast_SynchroniserAdvancedSystemDeflection:
        """Special nested class for casting SynchroniserAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
            parent: "SynchroniserAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7373.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7269,
            )

            return self._parent._cast(_7269.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_advanced_system_deflection(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
        ) -> "SynchroniserAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "SynchroniserAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2602.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6968.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

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
    ) -> "List[_2824.SynchroniserSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection]

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
    ) -> "SynchroniserAdvancedSystemDeflection._Cast_SynchroniserAdvancedSystemDeflection":
        return self._Cast_SynchroniserAdvancedSystemDeflection(self)

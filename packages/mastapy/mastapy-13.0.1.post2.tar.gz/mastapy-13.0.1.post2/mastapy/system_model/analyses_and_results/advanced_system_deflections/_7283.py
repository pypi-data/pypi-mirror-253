"""BeltDriveAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BeltDriveAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6822
    from mastapy.system_model.analyses_and_results.system_deflections import _2700


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BeltDriveAdvancedSystemDeflection")


class BeltDriveAdvancedSystemDeflection(
    _7374.SpecialisedAssemblyAdvancedSystemDeflection
):
    """BeltDriveAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveAdvancedSystemDeflection")

    class _Cast_BeltDriveAdvancedSystemDeflection:
        """Special nested class for casting BeltDriveAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
            parent: "BeltDriveAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7374.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7270,
            )

            return self._parent._cast(_7270.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_advanced_system_deflection(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(_7314.CVTAdvancedSystemDeflection)

        @property
        def belt_drive_advanced_system_deflection(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
        ) -> "BeltDriveAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BeltDriveAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2576.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6822.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

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
    ) -> "List[_2700.BeltDriveSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection]

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
    ) -> "BeltDriveAdvancedSystemDeflection._Cast_BeltDriveAdvancedSystemDeflection":
        return self._Cast_BeltDriveAdvancedSystemDeflection(self)

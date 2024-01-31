"""CVTAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7282
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CVTAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586


__docformat__ = "restructuredtext en"
__all__ = ("CVTAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CVTAdvancedSystemDeflection")


class CVTAdvancedSystemDeflection(_7282.BeltDriveAdvancedSystemDeflection):
    """CVTAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTAdvancedSystemDeflection")

    class _Cast_CVTAdvancedSystemDeflection:
        """Special nested class for casting CVTAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
            parent: "CVTAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def belt_drive_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7282.BeltDriveAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7269,
            )

            return self._parent._cast(_7269.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "CVTAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection":
        return self._Cast_CVTAdvancedSystemDeflection(self)

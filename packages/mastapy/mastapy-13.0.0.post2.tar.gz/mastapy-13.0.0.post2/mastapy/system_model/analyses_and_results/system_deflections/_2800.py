"""RootAssemblySystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2692
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "RootAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.power_flows import _4130
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2825,
        _2716,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblySystemDeflection",)


Self = TypeVar("Self", bound="RootAssemblySystemDeflection")


class RootAssemblySystemDeflection(_2692.AssemblySystemDeflection):
    """RootAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblySystemDeflection")

    class _Cast_RootAssemblySystemDeflection:
        """Special nested class for casting RootAssemblySystemDeflection to subclasses."""

        def __init__(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
            parent: "RootAssemblySystemDeflection",
        ):
            self._parent = parent

        @property
        def assembly_system_deflection(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ):
            return self._parent._cast(_2692.AssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(_2685.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def root_assembly_system_deflection(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
        ) -> "RootAssemblySystemDeflection":
            return self._parent

        def __getattr__(
            self: "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblySystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2474.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4130.RootAssemblyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.RootAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_inputs(self: Self) -> "_2825.SystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_deflection_results(
        self: Self,
    ) -> "List[_2716.ConcentricPartGroupCombinationSystemDeflectionResults]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConcentricPartGroupCombinationSystemDeflectionResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblySystemDeflection._Cast_RootAssemblySystemDeflection":
        return self._Cast_RootAssemblySystemDeflection(self)

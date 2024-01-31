"""CycloidalAssemblySystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CycloidalAssemblySystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2568
    from mastapy.system_model.analyses_and_results.static_loads import _6857
    from mastapy.system_model.analyses_and_results.power_flows import _4075
    from mastapy.system_model.analyses_and_results.system_deflections import _2795


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblySystemDeflection",)


Self = TypeVar("Self", bound="CycloidalAssemblySystemDeflection")


class CycloidalAssemblySystemDeflection(_2806.SpecialisedAssemblySystemDeflection):
    """CycloidalAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalAssemblySystemDeflection")

    class _Cast_CycloidalAssemblySystemDeflection:
        """Special nested class for casting CycloidalAssemblySystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
            parent: "CycloidalAssemblySystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ):
            return self._parent._cast(_2806.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(_2685.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_system_deflection(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
        ) -> "CycloidalAssemblySystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection",
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
        self: Self, instance_to_wrap: "CycloidalAssemblySystemDeflection.TYPE"
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
    def assembly_load_case(self: Self) -> "_6857.CycloidalAssemblyLoadCase":
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
    def power_flow_results(self: Self) -> "_4075.CycloidalAssemblyPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CycloidalAssemblyPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_pins_to_disc_connections(
        self: Self,
    ) -> "List[_2795.RingPinsToDiscConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RingPinsToDiscConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPinsToDiscConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalAssemblySystemDeflection._Cast_CycloidalAssemblySystemDeflection":
        return self._Cast_CycloidalAssemblySystemDeflection(self)

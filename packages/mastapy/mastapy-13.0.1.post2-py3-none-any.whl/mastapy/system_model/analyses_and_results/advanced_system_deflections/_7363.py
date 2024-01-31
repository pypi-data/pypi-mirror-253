"""PowerLoadAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7399
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PowerLoadAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.static_loads import _6940
    from mastapy.system_model.analyses_and_results.system_deflections import _2792
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7397,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PowerLoadAdvancedSystemDeflection")


class PowerLoadAdvancedSystemDeflection(_7399.VirtualComponentAdvancedSystemDeflection):
    """PowerLoadAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadAdvancedSystemDeflection")

    class _Cast_PowerLoadAdvancedSystemDeflection:
        """Special nested class for casting PowerLoadAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
            parent: "PowerLoadAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_advanced_system_deflection(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7399.VirtualComponentAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7353,
            )

            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def power_load_advanced_system_deflection(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
        ) -> "PowerLoadAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "PowerLoadAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6940.PowerLoadLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_system_deflection_results(
        self: Self,
    ) -> "List[_2792.PowerLoadSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def transmission_error_to_other_power_loads(
        self: Self,
    ) -> "List[_7397.TransmissionErrorToOtherPowerLoad]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.TransmissionErrorToOtherPowerLoad]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransmissionErrorToOtherPowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PowerLoadAdvancedSystemDeflection._Cast_PowerLoadAdvancedSystemDeflection":
        return self._Cast_PowerLoadAdvancedSystemDeflection(self)

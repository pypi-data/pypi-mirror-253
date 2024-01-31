"""ShaftHubConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ShaftHubConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6949
    from mastapy.system_model.analyses_and_results.system_deflections import _2801


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ShaftHubConnectionAdvancedSystemDeflection")


class ShaftHubConnectionAdvancedSystemDeflection(
    _7308.ConnectorAdvancedSystemDeflection
):
    """ShaftHubConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionAdvancedSystemDeflection"
    )

    class _Cast_ShaftHubConnectionAdvancedSystemDeflection:
        """Special nested class for casting ShaftHubConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
            parent: "ShaftHubConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connector_advanced_system_deflection(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7308.ConnectorAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7352,
            )

            return self._parent._cast(_7352.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7297,
            )

            return self._parent._cast(_7297.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
        ) -> "ShaftHubConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6949.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

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
    ) -> "List[_2801.ShaftHubConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection]

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
    def planetaries(self: Self) -> "List[ShaftHubConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ShaftHubConnectionAdvancedSystemDeflection]

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
    ) -> "ShaftHubConnectionAdvancedSystemDeflection._Cast_ShaftHubConnectionAdvancedSystemDeflection":
        return self._Cast_ShaftHubConnectionAdvancedSystemDeflection(self)

"""ConnectorAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7353
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConnectorAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConnectorAdvancedSystemDeflection")


class ConnectorAdvancedSystemDeflection(
    _7353.MountableComponentAdvancedSystemDeflection
):
    """ConnectorAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorAdvancedSystemDeflection")

    class _Cast_ConnectorAdvancedSystemDeflection:
        """Special nested class for casting ConnectorAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
            parent: "ConnectorAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7353.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7298,
            )

            return self._parent._cast(_7298.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7281,
            )

            return self._parent._cast(_7281.BearingAdvancedSystemDeflection)

        @property
        def oil_seal_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7354,
            )

            return self._parent._cast(_7354.OilSealAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.ShaftHubConnectionAdvancedSystemDeflection)

        @property
        def connector_advanced_system_deflection(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
        ) -> "ConnectorAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectorAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2447.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorAdvancedSystemDeflection._Cast_ConnectorAdvancedSystemDeflection":
        return self._Cast_ConnectorAdvancedSystemDeflection(self)

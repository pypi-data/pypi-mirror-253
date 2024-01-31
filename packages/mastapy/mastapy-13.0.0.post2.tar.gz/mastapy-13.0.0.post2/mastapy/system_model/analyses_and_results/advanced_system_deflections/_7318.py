"""CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
        "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2335


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection"
)


class CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection(
    _7296.CoaxialConnectionAdvancedSystemDeflection
):
    """CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
            parent: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7296.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(
                _7372.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7272,
            )

            return self._parent._cast(
                _7272.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7307,
            )

            return self._parent._cast(_7307.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
        ) -> "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2335.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection":
        return self._Cast_CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection(
            self
        )

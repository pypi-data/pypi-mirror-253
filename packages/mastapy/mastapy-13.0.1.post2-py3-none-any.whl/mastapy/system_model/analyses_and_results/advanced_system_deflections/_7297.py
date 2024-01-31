"""CoaxialConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CoaxialConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2269
    from mastapy.system_model.analyses_and_results.static_loads import _6837
    from mastapy.system_model.analyses_and_results.system_deflections import _2714


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CoaxialConnectionAdvancedSystemDeflection")


class CoaxialConnectionAdvancedSystemDeflection(
    _7373.ShaftToMountableComponentConnectionAdvancedSystemDeflection
):
    """CoaxialConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionAdvancedSystemDeflection"
    )

    class _Cast_CoaxialConnectionAdvancedSystemDeflection:
        """Special nested class for casting CoaxialConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
            parent: "CoaxialConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7373.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7273,
            )

            return self._parent._cast(
                _7273.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(_7308.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7319,
            )

            return self._parent._cast(
                _7319.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
            )

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
        ) -> "CoaxialConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CoaxialConnectionAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2269.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6837.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2714.CoaxialConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionAdvancedSystemDeflection._Cast_CoaxialConnectionAdvancedSystemDeflection":
        return self._Cast_CoaxialConnectionAdvancedSystemDeflection(self)

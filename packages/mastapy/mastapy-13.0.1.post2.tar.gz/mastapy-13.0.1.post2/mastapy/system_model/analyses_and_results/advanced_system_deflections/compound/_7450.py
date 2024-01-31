"""CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7430,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7319,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
)


class CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection(
    _7430.CoaxialConnectionCompoundAdvancedSystemDeflection
):
    """CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = (
        _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
            parent: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7430.CoaxialConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(
                _7503.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7409,
            )

            return self._parent._cast(
                _7409.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7441,
            )

            return self._parent._cast(_7441.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7319.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7319.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection(
            self
        )

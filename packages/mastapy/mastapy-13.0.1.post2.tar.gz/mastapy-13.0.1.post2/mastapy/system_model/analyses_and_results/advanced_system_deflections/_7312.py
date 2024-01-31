"""CouplingConnectionAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7340
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CouplingConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingConnectionAdvancedSystemDeflection")


class CouplingConnectionAdvancedSystemDeflection(
    _7340.InterMountableComponentConnectionAdvancedSystemDeflection
):
    """CouplingConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionAdvancedSystemDeflection"
    )

    class _Cast_CouplingConnectionAdvancedSystemDeflection:
        """Special nested class for casting CouplingConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
            parent: "CouplingConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7340.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(_7308.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7295,
            )

            return self._parent._cast(_7295.ClutchConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(
                _7300.ConceptCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(
                _7357.PartToPartShearCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def spring_damper_connection_advanced_system_deflection(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.SpringDamperConnectionAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7394,
            )

            return self._parent._cast(
                _7394.TorqueConverterConnectionAdvancedSystemDeflection
            )

        @property
        def coupling_connection_advanced_system_deflection(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
        ) -> "CouplingConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingConnectionAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2346.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

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
    ) -> "CouplingConnectionAdvancedSystemDeflection._Cast_CouplingConnectionAdvancedSystemDeflection":
        return self._Cast_CouplingConnectionAdvancedSystemDeflection(self)

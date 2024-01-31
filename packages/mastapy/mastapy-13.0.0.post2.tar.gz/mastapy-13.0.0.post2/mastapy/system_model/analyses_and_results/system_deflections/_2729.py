"""CouplingConnectionSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2767
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CouplingConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.power_flows import _4069


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionSystemDeflection",)


Self = TypeVar("Self", bound="CouplingConnectionSystemDeflection")


class CouplingConnectionSystemDeflection(
    _2767.InterMountableComponentConnectionSystemDeflection
):
    """CouplingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionSystemDeflection")

    class _Cast_CouplingConnectionSystemDeflection:
        """Special nested class for casting CouplingConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
            parent: "CouplingConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            return self._parent._cast(
                _2767.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def clutch_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.ClutchConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ConceptCouplingConnectionSystemDeflection)

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(
                _2786.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def spring_damper_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpringDamperConnectionSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(_2828.TorqueConverterConnectionSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
        ) -> "CouplingConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingConnectionSystemDeflection.TYPE"
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
    def power_flow_results(self: Self) -> "_4069.CouplingConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CouplingConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionSystemDeflection._Cast_CouplingConnectionSystemDeflection":
        return self._Cast_CouplingConnectionSystemDeflection(self)

"""TorqueConverterTurbineCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4206
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "TorqueConverterTurbineCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.power_flows import _4158


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCompoundPowerFlow")


class TorqueConverterTurbineCompoundPowerFlow(_4206.CouplingHalfCompoundPowerFlow):
    """TorqueConverterTurbineCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineCompoundPowerFlow"
    )

    class _Cast_TorqueConverterTurbineCompoundPowerFlow:
        """Special nested class for casting TorqueConverterTurbineCompoundPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
            parent: "TorqueConverterTurbineCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ):
            return self._parent._cast(_4206.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ) -> "TorqueConverterTurbineCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4158.TorqueConverterTurbinePowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterTurbinePowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4158.TorqueConverterTurbinePowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterTurbinePowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow":
        return self._Cast_TorqueConverterTurbineCompoundPowerFlow(self)

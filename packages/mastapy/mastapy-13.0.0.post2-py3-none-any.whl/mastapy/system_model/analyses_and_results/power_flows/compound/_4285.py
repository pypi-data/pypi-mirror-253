"""TorqueConverterPumpCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4205
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "TorqueConverterPumpCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.power_flows import _4156


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterPumpCompoundPowerFlow")


class TorqueConverterPumpCompoundPowerFlow(_4205.CouplingHalfCompoundPowerFlow):
    """TorqueConverterPumpCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterPumpCompoundPowerFlow")

    class _Cast_TorqueConverterPumpCompoundPowerFlow:
        """Special nested class for casting TorqueConverterPumpCompoundPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
            parent: "TorqueConverterPumpCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
        ):
            return self._parent._cast(_4205.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4243,
            )

            return self._parent._cast(_4243.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4191,
            )

            return self._parent._cast(_4191.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
        ) -> "TorqueConverterPumpCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "TorqueConverterPumpCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

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
    ) -> "List[_4156.TorqueConverterPumpPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterPumpPowerFlow]

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
    ) -> "List[_4156.TorqueConverterPumpPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterPumpPowerFlow]

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
    ) -> "TorqueConverterPumpCompoundPowerFlow._Cast_TorqueConverterPumpCompoundPowerFlow":
        return self._Cast_TorqueConverterPumpCompoundPowerFlow(self)

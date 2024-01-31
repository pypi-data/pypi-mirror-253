"""PulleyPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4070
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "PulleyPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2590
    from mastapy.system_model.analyses_and_results.static_loads import _6940


__docformat__ = "restructuredtext en"
__all__ = ("PulleyPowerFlow",)


Self = TypeVar("Self", bound="PulleyPowerFlow")


class PulleyPowerFlow(_4070.CouplingHalfPowerFlow):
    """PulleyPowerFlow

    This is a mastapy class.
    """

    TYPE = _PULLEY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyPowerFlow")

    class _Cast_PulleyPowerFlow:
        """Special nested class for casting PulleyPowerFlow to subclasses."""

        def __init__(
            self: "PulleyPowerFlow._Cast_PulleyPowerFlow", parent: "PulleyPowerFlow"
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(self: "PulleyPowerFlow._Cast_PulleyPowerFlow"):
            return self._parent._cast(_4070.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "PulleyPowerFlow._Cast_PulleyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def component_power_flow(self: "PulleyPowerFlow._Cast_PulleyPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(self: "PulleyPowerFlow._Cast_PulleyPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "PulleyPowerFlow._Cast_PulleyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "PulleyPowerFlow._Cast_PulleyPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "PulleyPowerFlow._Cast_PulleyPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyPowerFlow._Cast_PulleyPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "PulleyPowerFlow._Cast_PulleyPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_pulley_power_flow(self: "PulleyPowerFlow._Cast_PulleyPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4074

            return self._parent._cast(_4074.CVTPulleyPowerFlow)

        @property
        def pulley_power_flow(
            self: "PulleyPowerFlow._Cast_PulleyPowerFlow",
        ) -> "PulleyPowerFlow":
            return self._parent

        def __getattr__(self: "PulleyPowerFlow._Cast_PulleyPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2590.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6940.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PulleyPowerFlow._Cast_PulleyPowerFlow":
        return self._Cast_PulleyPowerFlow(self)

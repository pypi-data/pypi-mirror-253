"""CycloidalDiscPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CycloidalDiscPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2569
    from mastapy.system_model.analyses_and_results.static_loads import _6859


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPowerFlow",)


Self = TypeVar("Self", bound="CycloidalDiscPowerFlow")


class CycloidalDiscPowerFlow(_4034.AbstractShaftPowerFlow):
    """CycloidalDiscPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalDiscPowerFlow")

    class _Cast_CycloidalDiscPowerFlow:
        """Special nested class for casting CycloidalDiscPowerFlow to subclasses."""

        def __init__(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
            parent: "CycloidalDiscPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ):
            return self._parent._cast(_4034.AbstractShaftPowerFlow)

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4033

            return self._parent._cast(_4033.AbstractShaftOrHousingPowerFlow)

        @property
        def component_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cycloidal_disc_power_flow(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow",
        ) -> "CycloidalDiscPowerFlow":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalDiscPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2569.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6859.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CycloidalDiscPowerFlow._Cast_CycloidalDiscPowerFlow":
        return self._Cast_CycloidalDiscPowerFlow(self)

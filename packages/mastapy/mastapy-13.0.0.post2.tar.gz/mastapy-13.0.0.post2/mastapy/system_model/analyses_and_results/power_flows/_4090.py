"""FEPartPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4033
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "FEPartPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.static_loads import _6887


__docformat__ = "restructuredtext en"
__all__ = ("FEPartPowerFlow",)


Self = TypeVar("Self", bound="FEPartPowerFlow")


class FEPartPowerFlow(_4033.AbstractShaftOrHousingPowerFlow):
    """FEPartPowerFlow

    This is a mastapy class.
    """

    TYPE = _FE_PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartPowerFlow")

    class _Cast_FEPartPowerFlow:
        """Special nested class for casting FEPartPowerFlow to subclasses."""

        def __init__(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow", parent: "FEPartPowerFlow"
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ):
            return self._parent._cast(_4033.AbstractShaftOrHousingPowerFlow)

        @property
        def component_power_flow(self: "FEPartPowerFlow._Cast_FEPartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(self: "FEPartPowerFlow._Cast_FEPartPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "FEPartPowerFlow._Cast_FEPartPowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "FEPartPowerFlow._Cast_FEPartPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "FEPartPowerFlow._Cast_FEPartPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def fe_part_power_flow(
            self: "FEPartPowerFlow._Cast_FEPartPowerFlow",
        ) -> "FEPartPowerFlow":
            return self._parent

        def __getattr__(self: "FEPartPowerFlow._Cast_FEPartPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_parts_are_not_used_in_power_flow(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEPartsAreNotUsedInPowerFlow

        if temp is None:
            return ""

        return temp

    @property
    def fe_parts_are_not_used_in_power_flow_select_component_replaced_by_this_fe(
        self: Self,
    ) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEPartsAreNotUsedInPowerFlowSelectComponentReplacedByThisFE

        if temp is None:
            return ""

        return temp

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2453.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6887.FEPartLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FEPartPowerFlow._Cast_FEPartPowerFlow":
        return self._Cast_FEPartPowerFlow(self)

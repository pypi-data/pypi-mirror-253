"""SynchroniserPartPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4070
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "SynchroniserPartPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartPowerFlow",)


Self = TypeVar("Self", bound="SynchroniserPartPowerFlow")


class SynchroniserPartPowerFlow(_4070.CouplingHalfPowerFlow):
    """SynchroniserPartPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartPowerFlow")

    class _Cast_SynchroniserPartPowerFlow:
        """Special nested class for casting SynchroniserPartPowerFlow to subclasses."""

        def __init__(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
            parent: "SynchroniserPartPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            return self._parent._cast(_4070.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4111

            return self._parent._cast(_4111.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4057

            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4149

            return self._parent._cast(_4149.SynchroniserHalfPowerFlow)

        @property
        def synchroniser_sleeve_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4152

            return self._parent._cast(_4152.SynchroniserSleevePowerFlow)

        @property
        def synchroniser_part_power_flow(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow",
        ) -> "SynchroniserPartPowerFlow":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartPowerFlow._Cast_SynchroniserPartPowerFlow":
        return self._Cast_SynchroniserPartPowerFlow(self)

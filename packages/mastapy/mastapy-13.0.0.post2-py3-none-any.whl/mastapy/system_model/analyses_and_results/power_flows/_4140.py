"""SpringDamperPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4071
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "SpringDamperPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.static_loads import _6958


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperPowerFlow",)


Self = TypeVar("Self", bound="SpringDamperPowerFlow")


class SpringDamperPowerFlow(_4071.CouplingPowerFlow):
    """SpringDamperPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperPowerFlow")

    class _Cast_SpringDamperPowerFlow:
        """Special nested class for casting SpringDamperPowerFlow to subclasses."""

        def __init__(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow",
            parent: "SpringDamperPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_power_flow(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow",
        ):
            return self._parent._cast(_4071.CouplingPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4134

            return self._parent._cast(_4134.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spring_damper_power_flow(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow",
        ) -> "SpringDamperPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2600.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6958.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SpringDamperPowerFlow._Cast_SpringDamperPowerFlow":
        return self._Cast_SpringDamperPowerFlow(self)

"""BeltDrivePowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4134
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "BeltDrivePowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576
    from mastapy.system_model.analyses_and_results.static_loads import _6821


__docformat__ = "restructuredtext en"
__all__ = ("BeltDrivePowerFlow",)


Self = TypeVar("Self", bound="BeltDrivePowerFlow")


class BeltDrivePowerFlow(_4134.SpecialisedAssemblyPowerFlow):
    """BeltDrivePowerFlow

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDrivePowerFlow")

    class _Cast_BeltDrivePowerFlow:
        """Special nested class for casting BeltDrivePowerFlow to subclasses."""

        def __init__(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
            parent: "BeltDrivePowerFlow",
        ):
            self._parent = parent

        @property
        def specialised_assembly_power_flow(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ):
            return self._parent._cast(_4134.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4032

            return self._parent._cast(_4032.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_power_flow(self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow"):
            from mastapy.system_model.analyses_and_results.power_flows import _4073

            return self._parent._cast(_4073.CVTPowerFlow)

        @property
        def belt_drive_power_flow(
            self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow",
        ) -> "BeltDrivePowerFlow":
            return self._parent

        def __getattr__(self: "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDrivePowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2576.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6821.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BeltDrivePowerFlow._Cast_BeltDrivePowerFlow":
        return self._Cast_BeltDrivePowerFlow(self)

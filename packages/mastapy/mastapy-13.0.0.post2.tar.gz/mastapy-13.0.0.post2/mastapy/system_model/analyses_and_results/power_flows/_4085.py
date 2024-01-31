"""ExternalCADModelPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4057
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "ExternalCADModelPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2452
    from mastapy.system_model.analyses_and_results.static_loads import _6883


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelPowerFlow",)


Self = TypeVar("Self", bound="ExternalCADModelPowerFlow")


class ExternalCADModelPowerFlow(_4057.ComponentPowerFlow):
    """ExternalCADModelPowerFlow

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalCADModelPowerFlow")

    class _Cast_ExternalCADModelPowerFlow:
        """Special nested class for casting ExternalCADModelPowerFlow to subclasses."""

        def __init__(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow",
            parent: "ExternalCADModelPowerFlow",
        ):
            self._parent = parent

        @property
        def component_power_flow(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow",
        ):
            return self._parent._cast(_4057.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows import _4113

            return self._parent._cast(_4113.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def external_cad_model_power_flow(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow",
        ) -> "ExternalCADModelPowerFlow":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalCADModelPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def component_design(self: Self) -> "_2452.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6883.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ExternalCADModelPowerFlow._Cast_ExternalCADModelPowerFlow":
        return self._Cast_ExternalCADModelPowerFlow(self)

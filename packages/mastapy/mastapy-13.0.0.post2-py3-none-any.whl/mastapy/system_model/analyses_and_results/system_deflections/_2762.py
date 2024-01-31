"""GuideDxfModelSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2715
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "GuideDxfModelSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.static_loads import _6896
    from mastapy.system_model.analyses_and_results.power_flows import _4095


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelSystemDeflection",)


Self = TypeVar("Self", bound="GuideDxfModelSystemDeflection")


class GuideDxfModelSystemDeflection(_2715.ComponentSystemDeflection):
    """GuideDxfModelSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideDxfModelSystemDeflection")

    class _Cast_GuideDxfModelSystemDeflection:
        """Special nested class for casting GuideDxfModelSystemDeflection to subclasses."""

        def __init__(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
            parent: "GuideDxfModelSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ):
            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def guide_dxf_model_system_deflection(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
        ) -> "GuideDxfModelSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideDxfModelSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6896.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4095.GuideDxfModelPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.GuideDxfModelPowerFlow

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
    ) -> "GuideDxfModelSystemDeflection._Cast_GuideDxfModelSystemDeflection":
        return self._Cast_GuideDxfModelSystemDeflection(self)

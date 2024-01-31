"""TorqueConverterTurbineSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2730
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "TorqueConverterTurbineSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6975
    from mastapy.system_model.analyses_and_results.power_flows import _4157


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterTurbineSystemDeflection")


class TorqueConverterTurbineSystemDeflection(_2730.CouplingHalfSystemDeflection):
    """TorqueConverterTurbineSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineSystemDeflection"
    )

    class _Cast_TorqueConverterTurbineSystemDeflection:
        """Special nested class for casting TorqueConverterTurbineSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
            parent: "TorqueConverterTurbineSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            return self._parent._cast(_2730.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_system_deflection(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
        ) -> "TorqueConverterTurbineSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineSystemDeflection.TYPE"
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
    def component_load_case(self: Self) -> "_6975.TorqueConverterTurbineLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4157.TorqueConverterTurbinePowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.TorqueConverterTurbinePowerFlow

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
    ) -> "TorqueConverterTurbineSystemDeflection._Cast_TorqueConverterTurbineSystemDeflection":
        return self._Cast_TorqueConverterTurbineSystemDeflection(self)

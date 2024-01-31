"""VirtualComponentSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "VirtualComponentSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.power_flows import _4159


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentSystemDeflection")


class VirtualComponentSystemDeflection(_2782.MountableComponentSystemDeflection):
    """VirtualComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentSystemDeflection")

    class _Cast_VirtualComponentSystemDeflection:
        """Special nested class for casting VirtualComponentSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
            parent: "VirtualComponentSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            return self._parent._cast(_2782.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def mass_disc_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(_2779.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2780,
            )

            return self._parent._cast(_2780.MeasurementComponentSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(_2791.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.PowerLoadSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2834,
            )

            return self._parent._cast(_2834.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
        ) -> "VirtualComponentSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4159.VirtualComponentPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.VirtualComponentPowerFlow

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
    ) -> "VirtualComponentSystemDeflection._Cast_VirtualComponentSystemDeflection":
        return self._Cast_VirtualComponentSystemDeflection(self)

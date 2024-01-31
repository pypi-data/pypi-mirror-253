"""TorqueConverterSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2731
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "TorqueConverterSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.power_flows import _4155


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterSystemDeflection")


class TorqueConverterSystemDeflection(_2731.CouplingSystemDeflection):
    """TorqueConverterSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterSystemDeflection")

    class _Cast_TorqueConverterSystemDeflection:
        """Special nested class for casting TorqueConverterSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
            parent: "TorqueConverterSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_system_deflection(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            return self._parent._cast(_2731.CouplingSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(_2685.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_system_deflection(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
        ) -> "TorqueConverterSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2607.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6973.TorqueConverterLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4155.TorqueConverterPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.TorqueConverterPowerFlow

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
    ) -> "TorqueConverterSystemDeflection._Cast_TorqueConverterSystemDeflection":
        return self._Cast_TorqueConverterSystemDeflection(self)

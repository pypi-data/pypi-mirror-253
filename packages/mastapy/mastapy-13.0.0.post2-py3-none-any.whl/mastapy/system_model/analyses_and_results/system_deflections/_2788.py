"""PartToPartShearCouplingSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2731
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PartToPartShearCouplingSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.static_loads import _6931
    from mastapy.system_model.analyses_and_results.system_deflections import _2786
    from mastapy.system_model.analyses_and_results.power_flows import _4116


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingSystemDeflection",)


Self = TypeVar("Self", bound="PartToPartShearCouplingSystemDeflection")


class PartToPartShearCouplingSystemDeflection(_2731.CouplingSystemDeflection):
    """PartToPartShearCouplingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingSystemDeflection"
    )

    class _Cast_PartToPartShearCouplingSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingSystemDeflection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
            parent: "PartToPartShearCouplingSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_system_deflection(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            return self._parent._cast(_2731.CouplingSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2685,
            )

            return self._parent._cast(_2685.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
        ) -> "PartToPartShearCouplingSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2588.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6931.PartToPartShearCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def part_to_part_shear_coupling_connection(
        self: Self,
    ) -> "_2786.PartToPartShearCouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartToPartShearCouplingConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4116.PartToPartShearCouplingPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingPowerFlow

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
    ) -> "PartToPartShearCouplingSystemDeflection._Cast_PartToPartShearCouplingSystemDeflection":
        return self._Cast_PartToPartShearCouplingSystemDeflection(self)

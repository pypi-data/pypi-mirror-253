"""PartToPartShearCouplingCompoundPowerFlow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4203
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PartToPartShearCouplingCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.power_flows import _4116


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCompoundPowerFlow",)


Self = TypeVar("Self", bound="PartToPartShearCouplingCompoundPowerFlow")


class PartToPartShearCouplingCompoundPowerFlow(_4203.CouplingCompoundPowerFlow):
    """PartToPartShearCouplingCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingCompoundPowerFlow"
    )

    class _Cast_PartToPartShearCouplingCompoundPowerFlow:
        """Special nested class for casting PartToPartShearCouplingCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
            parent: "PartToPartShearCouplingCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_compound_power_flow(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
        ):
            return self._parent._cast(_4203.CouplingCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4264,
            )

            return self._parent._cast(_4264.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4166,
            )

            return self._parent._cast(_4166.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_power_flow(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
        ) -> "PartToPartShearCouplingCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4116.PartToPartShearCouplingPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4116.PartToPartShearCouplingPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PartToPartShearCouplingPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingCompoundPowerFlow._Cast_PartToPartShearCouplingCompoundPowerFlow":
        return self._Cast_PartToPartShearCouplingCompoundPowerFlow(self)

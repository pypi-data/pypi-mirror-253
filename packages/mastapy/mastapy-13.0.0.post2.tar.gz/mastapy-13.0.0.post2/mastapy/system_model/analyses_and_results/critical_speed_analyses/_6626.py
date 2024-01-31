"""PartToPartShearCouplingCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6580
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PartToPartShearCouplingCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.static_loads import _6931


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingCriticalSpeedAnalysis")


class PartToPartShearCouplingCriticalSpeedAnalysis(_6580.CouplingCriticalSpeedAnalysis):
    """PartToPartShearCouplingCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingCriticalSpeedAnalysis"
    )

    class _Cast_PartToPartShearCouplingCriticalSpeedAnalysis:
        """Special nested class for casting PartToPartShearCouplingCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
            parent: "PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6580.CouplingCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6643,
            )

            return self._parent._cast(_6643.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6542,
            )

            return self._parent._cast(_6542.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_critical_speed_analysis(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
        ) -> "PartToPartShearCouplingCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis",
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
        self: Self,
        instance_to_wrap: "PartToPartShearCouplingCriticalSpeedAnalysis.TYPE",
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
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingCriticalSpeedAnalysis._Cast_PartToPartShearCouplingCriticalSpeedAnalysis":
        return self._Cast_PartToPartShearCouplingCriticalSpeedAnalysis(self)

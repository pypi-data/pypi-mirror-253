"""RootAssemblyStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3770
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "RootAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.stability_analyses import _3870


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyStabilityAnalysis")


class RootAssemblyStabilityAnalysis(_3770.AssemblyStabilityAnalysis):
    """RootAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyStabilityAnalysis")

    class _Cast_RootAssemblyStabilityAnalysis:
        """Special nested class for casting RootAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
            parent: "RootAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_stability_analysis(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
        ):
            return self._parent._cast(_3770.AssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3763,
            )

            return self._parent._cast(_3763.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def root_assembly_stability_analysis(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
        ) -> "RootAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblyStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2474.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stability_analysis_inputs(self: Self) -> "_3870.StabilityAnalysis":
        """mastapy.system_model.analyses_and_results.stability_analyses.StabilityAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StabilityAnalysisInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyStabilityAnalysis._Cast_RootAssemblyStabilityAnalysis":
        return self._Cast_RootAssemblyStabilityAnalysis(self)

"""TorqueConverterStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3802
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "TorqueConverterStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.static_loads import _6973


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterStabilityAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterStabilityAnalysis")


class TorqueConverterStabilityAnalysis(_3802.CouplingStabilityAnalysis):
    """TorqueConverterStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterStabilityAnalysis")

    class _Cast_TorqueConverterStabilityAnalysis:
        """Special nested class for casting TorqueConverterStabilityAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
            parent: "TorqueConverterStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            return self._parent._cast(_3802.CouplingStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3763,
            )

            return self._parent._cast(_3763.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_stability_analysis(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
        ) -> "TorqueConverterStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterStabilityAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "TorqueConverterStabilityAnalysis._Cast_TorqueConverterStabilityAnalysis":
        return self._Cast_TorqueConverterStabilityAnalysis(self)

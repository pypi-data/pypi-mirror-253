"""PlanetCarrierDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "PlanetCarrierDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2469
    from mastapy.system_model.analyses_and_results.static_loads import _6935


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierDynamicAnalysis",)


Self = TypeVar("Self", bound="PlanetCarrierDynamicAnalysis")


class PlanetCarrierDynamicAnalysis(_6355.MountableComponentDynamicAnalysis):
    """PlanetCarrierDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierDynamicAnalysis")

    class _Cast_PlanetCarrierDynamicAnalysis:
        """Special nested class for casting PlanetCarrierDynamicAnalysis to subclasses."""

        def __init__(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
            parent: "PlanetCarrierDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ):
            return self._parent._cast(_6355.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
        ) -> "PlanetCarrierDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2469.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6935.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

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
    ) -> "PlanetCarrierDynamicAnalysis._Cast_PlanetCarrierDynamicAnalysis":
        return self._Cast_PlanetCarrierDynamicAnalysis(self)

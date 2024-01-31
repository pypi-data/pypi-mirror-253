"""ConceptGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConceptGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.static_loads import _6842


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearDynamicAnalysis",)


Self = TypeVar("Self", bound="ConceptGearDynamicAnalysis")


class ConceptGearDynamicAnalysis(_6337.GearDynamicAnalysis):
    """ConceptGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearDynamicAnalysis")

    class _Cast_ConceptGearDynamicAnalysis:
        """Special nested class for casting ConceptGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
            parent: "ConceptGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_dynamic_analysis(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            return self._parent._cast(_6337.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
        ) -> "ConceptGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2521.ConceptGear":
        """mastapy.system_model.part_model.gears.ConceptGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6842.ConceptGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase

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
    ) -> "ConceptGearDynamicAnalysis._Cast_ConceptGearDynamicAnalysis":
        return self._Cast_ConceptGearDynamicAnalysis(self)

"""SynchroniserPartDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SynchroniserPartDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartDynamicAnalysis")


class SynchroniserPartDynamicAnalysis(_6316.CouplingHalfDynamicAnalysis):
    """SynchroniserPartDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserPartDynamicAnalysis")

    class _Cast_SynchroniserPartDynamicAnalysis:
        """Special nested class for casting SynchroniserPartDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
            parent: "SynchroniserPartDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            return self._parent._cast(_6316.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.SynchroniserSleeveDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
        ) -> "SynchroniserPartDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserPartDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2605.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartDynamicAnalysis._Cast_SynchroniserPartDynamicAnalysis":
        return self._Cast_SynchroniserPartDynamicAnalysis(self)

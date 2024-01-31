"""AbstractShaftOrHousingDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractShaftOrHousingDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingDynamicAnalysis")


class AbstractShaftOrHousingDynamicAnalysis(_6302.ComponentDynamicAnalysis):
    """AbstractShaftOrHousingDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingDynamicAnalysis"
    )

    class _Cast_AbstractShaftOrHousingDynamicAnalysis:
        """Special nested class for casting AbstractShaftOrHousingDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
            parent: "AbstractShaftOrHousingDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            return self._parent._cast(_6302.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6278

            return self._parent._cast(_6278.AbstractShaftDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CycloidalDiscDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.FEPartDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.ShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
        ) -> "AbstractShaftOrHousingDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2436.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingDynamicAnalysis._Cast_AbstractShaftOrHousingDynamicAnalysis":
        return self._Cast_AbstractShaftOrHousingDynamicAnalysis(self)

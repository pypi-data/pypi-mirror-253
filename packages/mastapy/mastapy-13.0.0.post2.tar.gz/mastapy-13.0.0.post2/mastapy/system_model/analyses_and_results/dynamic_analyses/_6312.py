"""ConnectorDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConnectorDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorDynamicAnalysis",)


Self = TypeVar("Self", bound="ConnectorDynamicAnalysis")


class ConnectorDynamicAnalysis(_6355.MountableComponentDynamicAnalysis):
    """ConnectorDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorDynamicAnalysis")

    class _Cast_ConnectorDynamicAnalysis:
        """Special nested class for casting ConnectorDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
            parent: "ConnectorDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            return self._parent._cast(_6355.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.BearingDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.OilSealDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.ShaftHubConnectionDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis",
        ) -> "ConnectorDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2447.Connector":
        """mastapy.system_model.part_model.Connector

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
    ) -> "ConnectorDynamicAnalysis._Cast_ConnectorDynamicAnalysis":
        return self._Cast_ConnectorDynamicAnalysis(self)

"""ConnectorMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5463
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConnectorMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2447


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConnectorMultibodyDynamicsAnalysis")


class ConnectorMultibodyDynamicsAnalysis(
    _5463.MountableComponentMultibodyDynamicsAnalysis
):
    """ConnectorMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorMultibodyDynamicsAnalysis")

    class _Cast_ConnectorMultibodyDynamicsAnalysis:
        """Special nested class for casting ConnectorMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
            parent: "ConnectorMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5463.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(_5384.BearingMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(_5465.OilSealMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5484

            return self._parent._cast(_5484.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
        ) -> "ConnectorMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConnectorMultibodyDynamicsAnalysis.TYPE"
    ):
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
    ) -> "ConnectorMultibodyDynamicsAnalysis._Cast_ConnectorMultibodyDynamicsAnalysis":
        return self._Cast_ConnectorMultibodyDynamicsAnalysis(self)

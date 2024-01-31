"""ShaftHubConnectionMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5414
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ShaftHubConnectionMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6949
    from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import (
        _5524,
        _5526,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ShaftHubConnectionMultibodyDynamicsAnalysis")


class ShaftHubConnectionMultibodyDynamicsAnalysis(
    _5414.ConnectorMultibodyDynamicsAnalysis
):
    """ShaftHubConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHubConnectionMultibodyDynamicsAnalysis"
    )

    class _Cast_ShaftHubConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting ShaftHubConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
            parent: "ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connector_multibody_dynamics_analysis(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5414.ConnectorMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
        ) -> "ShaftHubConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ShaftHubConnectionMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Force

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def force_angular(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def relative_angular_displacement(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeAngularDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def relative_linear_displacement(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeLinearDisplacement

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2598.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6949.ShaftHubConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def peak_dynamic_force(self: Self) -> "_5524.DynamicForceVector3DResult":
        """mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicForceVector3DResult

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakDynamicForce

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def peak_dynamic_force_angular(self: Self) -> "_5526.DynamicTorqueVector3DResult":
        """mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicTorqueVector3DResult

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakDynamicForceAngular

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHubConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ShaftHubConnectionMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftHubConnectionMultibodyDynamicsAnalysis._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis":
        return self._Cast_ShaftHubConnectionMultibodyDynamicsAnalysis(self)

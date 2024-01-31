"""SpiralBevelGearMeshMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5394
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SpiralBevelGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.static_loads import _6955


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshMultibodyDynamicsAnalysis")


class SpiralBevelGearMeshMultibodyDynamicsAnalysis(
    _5394.BevelGearMeshMultibodyDynamicsAnalysis
):
    """SpiralBevelGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting SpiralBevelGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
            parent: "SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5394.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380

            return self._parent._cast(
                _5380.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SpiralBevelGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6955.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshMultibodyDynamicsAnalysis._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_SpiralBevelGearMeshMultibodyDynamicsAnalysis(self)

"""ConicalGearMeshDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConicalGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2307


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshDynamicAnalysis")


class ConicalGearMeshDynamicAnalysis(_6338.GearMeshDynamicAnalysis):
    """ConicalGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshDynamicAnalysis")

    class _Cast_ConicalGearMeshDynamicAnalysis:
        """Special nested class for casting ConicalGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
            parent: "ConicalGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            return self._parent._cast(_6338.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BevelGearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.HypoidGearMeshDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
        ) -> "ConicalGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2307.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearMeshDynamicAnalysis]

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
    ) -> "ConicalGearMeshDynamicAnalysis._Cast_ConicalGearMeshDynamicAnalysis":
        return self._Cast_ConicalGearMeshDynamicAnalysis(self)

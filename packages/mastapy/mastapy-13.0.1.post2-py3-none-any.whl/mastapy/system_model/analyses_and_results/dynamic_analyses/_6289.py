"""BevelDifferentialGearMeshDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "BevelDifferentialGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301
    from mastapy.system_model.analyses_and_results.static_loads import _6824


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshDynamicAnalysis")


class BevelDifferentialGearMeshDynamicAnalysis(_6294.BevelGearMeshDynamicAnalysis):
    """BevelDifferentialGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshDynamicAnalysis"
    )

    class _Cast_BevelDifferentialGearMeshDynamicAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
            parent: "BevelDifferentialGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            return self._parent._cast(_6294.BevelGearMeshDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6282

            return self._parent._cast(_6282.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(
                _6344.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
        ) -> "BevelDifferentialGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearMeshDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2301.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6824.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

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
    ) -> "BevelDifferentialGearMeshDynamicAnalysis._Cast_BevelDifferentialGearMeshDynamicAnalysis":
        return self._Cast_BevelDifferentialGearMeshDynamicAnalysis(self)

"""SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6692,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6646


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundCriticalSpeedAnalysis")


class SpiralBevelGearMeshCompoundCriticalSpeedAnalysis(
    _6692.BevelGearMeshCompoundCriticalSpeedAnalysis
):
    """SpiralBevelGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting SpiralBevelGearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
            parent: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6692.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6680,
            )

            return self._parent._cast(
                _6680.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(
                _6708.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(_6734.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6740,
            )

            return self._parent._cast(
                _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
        ) -> "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2323.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6646.SpiralBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpiralBevelGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6646.SpiralBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.SpiralBevelGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshCompoundCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_SpiralBevelGearMeshCompoundCriticalSpeedAnalysis(self)

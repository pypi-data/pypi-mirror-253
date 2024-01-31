"""SpiralBevelGearMeshCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SpiralBevelGearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundDynamicAnalysis")


class SpiralBevelGearMeshCompoundDynamicAnalysis(
    _6425.BevelGearMeshCompoundDynamicAnalysis
):
    """SpiralBevelGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundDynamicAnalysis"
    )

    class _Cast_SpiralBevelGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting SpiralBevelGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
            parent: "SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6425.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6413,
            )

            return self._parent._cast(
                _6413.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6473,
            )

            return self._parent._cast(
                _6473.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
        ) -> "SpiralBevelGearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshCompoundDynamicAnalysis.TYPE"
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
    ) -> "List[_6379.SpiralBevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearMeshDynamicAnalysis]

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
    ) -> "List[_6379.SpiralBevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SpiralBevelGearMeshDynamicAnalysis]

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
    ) -> "SpiralBevelGearMeshCompoundDynamicAnalysis._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis":
        return self._Cast_SpiralBevelGearMeshCompoundDynamicAnalysis(self)

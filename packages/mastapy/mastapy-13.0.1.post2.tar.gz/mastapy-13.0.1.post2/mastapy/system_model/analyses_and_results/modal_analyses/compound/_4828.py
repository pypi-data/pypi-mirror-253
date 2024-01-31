"""SpiralBevelGearMeshCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4745
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SpiralBevelGearMeshCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.modal_analyses import _4683


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundModalAnalysis")


class SpiralBevelGearMeshCompoundModalAnalysis(
    _4745.BevelGearMeshCompoundModalAnalysis
):
    """SpiralBevelGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundModalAnalysis"
    )

    class _Cast_SpiralBevelGearMeshCompoundModalAnalysis:
        """Special nested class for casting SpiralBevelGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
            parent: "SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            return self._parent._cast(_4745.BevelGearMeshCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4733,
            )

            return self._parent._cast(
                _4733.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ConicalGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4787,
            )

            return self._parent._cast(_4787.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4793,
            )

            return self._parent._cast(
                _4793.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
        ) -> "SpiralBevelGearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshCompoundModalAnalysis.TYPE"
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
    ) -> "List[_4683.SpiralBevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearMeshModalAnalysis]

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
    ) -> "List[_4683.SpiralBevelGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpiralBevelGearMeshModalAnalysis]

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
    ) -> "SpiralBevelGearMeshCompoundModalAnalysis._Cast_SpiralBevelGearMeshCompoundModalAnalysis":
        return self._Cast_SpiralBevelGearMeshCompoundModalAnalysis(self)

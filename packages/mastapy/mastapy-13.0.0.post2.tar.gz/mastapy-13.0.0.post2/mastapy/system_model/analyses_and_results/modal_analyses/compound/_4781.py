"""FaceGearMeshCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4786
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "FaceGearMeshCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2311
    from mastapy.system_model.analyses_and_results.modal_analyses import _4628


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshCompoundModalAnalysis",)


Self = TypeVar("Self", bound="FaceGearMeshCompoundModalAnalysis")


class FaceGearMeshCompoundModalAnalysis(_4786.GearMeshCompoundModalAnalysis):
    """FaceGearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshCompoundModalAnalysis")

    class _Cast_FaceGearMeshCompoundModalAnalysis:
        """Special nested class for casting FaceGearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis",
            parent: "FaceGearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_modal_analysis(
            self: "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis",
        ):
            return self._parent._cast(_4786.GearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(
                _4792.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(
            self: "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis",
        ) -> "FaceGearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "FaceGearMeshCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2311.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2311.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

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
    ) -> "List[_4628.FaceGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.FaceGearMeshModalAnalysis]

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
    ) -> "List[_4628.FaceGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.FaceGearMeshModalAnalysis]

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
    ) -> "FaceGearMeshCompoundModalAnalysis._Cast_FaceGearMeshCompoundModalAnalysis":
        return self._Cast_FaceGearMeshCompoundModalAnalysis(self)

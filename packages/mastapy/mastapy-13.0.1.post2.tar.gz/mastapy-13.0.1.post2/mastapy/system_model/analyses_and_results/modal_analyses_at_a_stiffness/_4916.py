"""GearMeshModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4923,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "GearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2313


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="GearMeshModalAnalysisAtAStiffness")


class GearMeshModalAnalysisAtAStiffness(
    _4923.InterMountableComponentConnectionModalAnalysisAtAStiffness
):
    """GearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshModalAnalysisAtAStiffness")

    class _Cast_GearMeshModalAnalysisAtAStiffness:
        """Special nested class for casting GearMeshModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
            parent: "GearMeshModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4923.InterMountableComponentConnectionModalAnalysisAtAStiffness
            )

        @property
        def connection_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4892,
            )

            return self._parent._cast(_4892.ConnectionModalAnalysisAtAStiffness)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4861,
            )

            return self._parent._cast(
                _4861.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4868,
            )

            return self._parent._cast(
                _4868.BevelDifferentialGearMeshModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4873,
            )

            return self._parent._cast(_4873.BevelGearMeshModalAnalysisAtAStiffness)

        @property
        def concept_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4886,
            )

            return self._parent._cast(_4886.ConceptGearMeshModalAnalysisAtAStiffness)

        @property
        def conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4889,
            )

            return self._parent._cast(_4889.ConicalGearMeshModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4904,
            )

            return self._parent._cast(
                _4904.CylindricalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4911,
            )

            return self._parent._cast(_4911.FaceGearMeshModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4920,
            )

            return self._parent._cast(_4920.HypoidGearMeshModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4924,
            )

            return self._parent._cast(
                _4924.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4927,
            )

            return self._parent._cast(
                _4927.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4930,
            )

            return self._parent._cast(
                _4930.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4958,
            )

            return self._parent._cast(
                _4958.SpiralBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4964,
            )

            return self._parent._cast(
                _4964.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4967,
            )

            return self._parent._cast(
                _4967.StraightBevelGearMeshModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4982,
            )

            return self._parent._cast(_4982.WormGearMeshModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4985,
            )

            return self._parent._cast(_4985.ZerolBevelGearMeshModalAnalysisAtAStiffness)

        @property
        def gear_mesh_modal_analysis_at_a_stiffness(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
        ) -> "GearMeshModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "GearMeshModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2313.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshModalAnalysisAtAStiffness._Cast_GearMeshModalAnalysisAtAStiffness":
        return self._Cast_GearMeshModalAnalysisAtAStiffness(self)

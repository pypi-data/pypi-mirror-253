"""GearMeshCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5312,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "GearMeshCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5175,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="GearMeshCompoundModalAnalysisAtASpeed")


class GearMeshCompoundModalAnalysisAtASpeed(
    _5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
):
    """GearMeshCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshCompoundModalAnalysisAtASpeed"
    )

    class _Cast_GearMeshCompoundModalAnalysisAtASpeed:
        """Special nested class for casting GearMeshCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
            parent: "GearMeshCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(
                _5312.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(_5282.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5252,
            )

            return self._parent._cast(
                _5252.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(
                _5259.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5264,
            )

            return self._parent._cast(_5264.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(
                _5277.ConceptGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(
                _5280.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(
                _5295.CylindricalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(_5301.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5310,
            )

            return self._parent._cast(_5310.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(
                _5356.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(_5371.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
        ) -> "GearMeshCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "GearMeshCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5175.GearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.GearMeshModalAnalysisAtASpeed]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5175.GearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.GearMeshModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "GearMeshCompoundModalAnalysisAtASpeed._Cast_GearMeshCompoundModalAnalysisAtASpeed":
        return self._Cast_GearMeshCompoundModalAnalysisAtASpeed(self)

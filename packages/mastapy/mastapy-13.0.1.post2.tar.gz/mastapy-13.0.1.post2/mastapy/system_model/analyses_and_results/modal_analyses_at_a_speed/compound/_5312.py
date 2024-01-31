"""InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5282,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5182,
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"
)


class InterMountableComponentConnectionCompoundModalAnalysisAtASpeed(
    _5282.ConnectionCompoundModalAnalysisAtASpeed
):
    """InterMountableComponentConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )

    class _Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
            parent: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5282.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5252,
            )

            return self._parent._cast(
                _5252.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5256,
            )

            return self._parent._cast(_5256.BeltConnectionCompoundModalAnalysisAtASpeed)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5259,
            )

            return self._parent._cast(
                _5259.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5264,
            )

            return self._parent._cast(_5264.BevelGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5269,
            )

            return self._parent._cast(
                _5269.ClutchConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5274,
            )

            return self._parent._cast(
                _5274.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(
                _5277.ConceptGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(
                _5280.ConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5285,
            )

            return self._parent._cast(
                _5285.CouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5287,
            )

            return self._parent._cast(
                _5287.CVTBeltConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5295,
            )

            return self._parent._cast(
                _5295.CylindricalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5301,
            )

            return self._parent._cast(_5301.FaceGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5306,
            )

            return self._parent._cast(_5306.GearMeshCompoundModalAnalysisAtASpeed)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5310,
            )

            return self._parent._cast(_5310.HypoidGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5314,
            )

            return self._parent._cast(
                _5314.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5317,
            )

            return self._parent._cast(
                _5317.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5320,
            )

            return self._parent._cast(
                _5320.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5328,
            )

            return self._parent._cast(
                _5328.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5337,
            )

            return self._parent._cast(
                _5337.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5340,
            )

            return self._parent._cast(
                _5340.RollingRingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5347,
            )

            return self._parent._cast(
                _5347.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5350,
            )

            return self._parent._cast(
                _5350.SpringDamperConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5353,
            )

            return self._parent._cast(
                _5353.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5356,
            )

            return self._parent._cast(
                _5356.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5365,
            )

            return self._parent._cast(
                _5365.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(_5371.WormGearMeshCompoundModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5374,
            )

            return self._parent._cast(
                _5374.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
        ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5182.InterMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.InterMountableComponentConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5182.InterMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.InterMountableComponentConnectionModalAnalysisAtASpeed]

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
    ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
        return (
            self._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed(
                self
            )
        )

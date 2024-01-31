"""InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5564
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5449


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
)


class InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
    _5564.ConnectionCompoundMultibodyDynamicsAnalysis
):
    """InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5564.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5534,
            )

            return self._parent._cast(
                _5534.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(
                _5538.BeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(
                _5541.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(
                _5546.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(
                _5551.ClutchConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(
                _5556.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ConceptGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(
                _5569.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.FaceGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(_5588.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5592,
            )

            return self._parent._cast(
                _5592.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(
                _5610.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(
                _5619.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5622,
            )

            return self._parent._cast(
                _5622.RollingRingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.WormGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.InterMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5449.InterMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.InterMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )

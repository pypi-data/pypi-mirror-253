"""ConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5414


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundMultibodyDynamicsAnalysis")


class ConnectionCompoundMultibodyDynamicsAnalysis(_7539.ConnectionCompoundAnalysis):
    """ConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5532,
            )

            return self._parent._cast(
                _5532.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5534,
            )

            return self._parent._cast(
                _5534.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5538,
            )

            return self._parent._cast(
                _5538.BeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5541,
            )

            return self._parent._cast(
                _5541.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(
                _5546.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5551,
            )

            return self._parent._cast(
                _5551.ClutchConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(
                _5553.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5556,
            )

            return self._parent._cast(
                _5556.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ConceptGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5562,
            )

            return self._parent._cast(
                _5562.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(
                _5569.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5573,
            )

            return self._parent._cast(
                _5573.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5575,
            )

            return self._parent._cast(
                _5575.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5583,
            )

            return self._parent._cast(
                _5583.FaceGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(_5588.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5592,
            )

            return self._parent._cast(
                _5592.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(
                _5610.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5612,
            )

            return self._parent._cast(
                _5612.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(
                _5619.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5622,
            )

            return self._parent._cast(
                _5622.RollingRingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(
                _5626.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5629,
            )

            return self._parent._cast(
                _5629.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.WormGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5656,
            )

            return self._parent._cast(
                _5656.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "ConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5414.ConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5414.ConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConnectionMultibodyDynamicsAnalysis]

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
    ) -> "ConnectionCompoundMultibodyDynamicsAnalysis._Cast_ConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ConnectionCompoundMultibodyDynamicsAnalysis(self)

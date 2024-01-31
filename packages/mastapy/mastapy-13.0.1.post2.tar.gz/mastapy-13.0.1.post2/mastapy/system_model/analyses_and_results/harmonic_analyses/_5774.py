"""InterMountableComponentConnectionHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "InterMountableComponentConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2281
    from mastapy.system_model.analyses_and_results.system_deflections import _2767


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionHarmonicAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionHarmonicAnalysis")


class InterMountableComponentConnectionHarmonicAnalysis(
    _5715.ConnectionHarmonicAnalysis
):
    """InterMountableComponentConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionHarmonicAnalysis"
    )

    class _Cast_InterMountableComponentConnectionHarmonicAnalysis:
        """Special nested class for casting InterMountableComponentConnectionHarmonicAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
            parent: "InterMountableComponentConnectionHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            return self._parent._cast(_5715.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5684,
            )

            return self._parent._cast(_5684.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def belt_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5688,
            )

            return self._parent._cast(_5688.BeltConnectionHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5696,
            )

            return self._parent._cast(_5696.BevelGearMeshHarmonicAnalysis)

        @property
        def clutch_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.ClutchConnectionHarmonicAnalysis)

        @property
        def concept_coupling_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5706,
            )

            return self._parent._cast(_5706.ConceptCouplingConnectionHarmonicAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConceptGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ConicalGearMeshHarmonicAnalysis)

        @property
        def coupling_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5717,
            )

            return self._parent._cast(_5717.CouplingConnectionHarmonicAnalysis)

        @property
        def cvt_belt_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.CVTBeltConnectionHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.CylindricalGearMeshHarmonicAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.FaceGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.GearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5772,
            )

            return self._parent._cast(_5772.HypoidGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(
                _5776.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(
                _5779.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(
                _5782.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5789,
            )

            return self._parent._cast(
                _5789.PartToPartShearCouplingConnectionHarmonicAnalysis
            )

        @property
        def ring_pins_to_disc_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5801,
            )

            return self._parent._cast(_5801.RingPinsToDiscConnectionHarmonicAnalysis)

        @property
        def rolling_ring_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5803,
            )

            return self._parent._cast(_5803.RollingRingConnectionHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def spring_damper_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5815,
            )

            return self._parent._cast(_5815.SpringDamperConnectionHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def torque_converter_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5831,
            )

            return self._parent._cast(_5831.TorqueConverterConnectionHarmonicAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.WormGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
        ) -> "InterMountableComponentConnectionHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2281.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2767.InterMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionHarmonicAnalysis._Cast_InterMountableComponentConnectionHarmonicAnalysis":
        return self._Cast_InterMountableComponentConnectionHarmonicAnalysis(self)

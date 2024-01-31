"""GearMeshHarmonicAnalysisOfSingleExcitation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6074,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "GearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2313


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GearMeshHarmonicAnalysisOfSingleExcitation")


class GearMeshHarmonicAnalysisOfSingleExcitation(
    _6074.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
):
    """GearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            return self._parent._cast(
                _6074.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6013,
            )

            return self._parent._cast(
                _6013.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6020,
            )

            return self._parent._cast(
                _6020.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6025,
            )

            return self._parent._cast(
                _6025.BevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6038,
            )

            return self._parent._cast(
                _6038.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6041,
            )

            return self._parent._cast(
                _6041.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6056,
            )

            return self._parent._cast(
                _6056.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(
                _6062.FaceGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6072,
            )

            return self._parent._cast(
                _6072.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6079,
            )

            return self._parent._cast(
                _6079.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6082,
            )

            return self._parent._cast(
                _6082.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(
                _6110.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6116,
            )

            return self._parent._cast(
                _6116.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6119,
            )

            return self._parent._cast(
                _6119.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.WormGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6137,
            )

            return self._parent._cast(
                _6137.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "GearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "GearMeshHarmonicAnalysisOfSingleExcitation.TYPE"
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
    ) -> "GearMeshHarmonicAnalysisOfSingleExcitation._Cast_GearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GearMeshHarmonicAnalysisOfSingleExcitation(self)

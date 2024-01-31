"""GearMeshHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "GearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2313
    from mastapy.system_model.analyses_and_results.power_flows import _4154
    from mastapy.system_model.analyses_and_results.system_deflections import _2759


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="GearMeshHarmonicAnalysis")


class GearMeshHarmonicAnalysis(_5774.InterMountableComponentConnectionHarmonicAnalysis):
    """GearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshHarmonicAnalysis")

    class _Cast_GearMeshHarmonicAnalysis:
        """Special nested class for casting GearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
            parent: "GearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            return self._parent._cast(
                _5774.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5715,
            )

            return self._parent._cast(_5715.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2649

            return self._parent._cast(_2649.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5684,
            )

            return self._parent._cast(_5684.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5696,
            )

            return self._parent._cast(_5696.BevelGearMeshHarmonicAnalysis)

        @property
        def concept_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConceptGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ConicalGearMeshHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.CylindricalGearMeshHarmonicAnalysis)

        @property
        def face_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.FaceGearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5772,
            )

            return self._parent._cast(_5772.HypoidGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5776,
            )

            return self._parent._cast(
                _5776.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(
                _5779.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(
                _5782.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5813,
            )

            return self._parent._cast(_5813.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5820,
            )

            return self._parent._cast(_5820.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.WormGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis",
        ) -> "GearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def set_user_specified_te_from_file(self: Self) -> "str":
        """str"""
        temp = self.wrapped.SetUserSpecifiedTEFromFile

        if temp is None:
            return ""

        return temp

    @set_user_specified_te_from_file.setter
    @enforce_parameter_types
    def set_user_specified_te_from_file(self: Self, value: "str"):
        self.wrapped.SetUserSpecifiedTEFromFile = (
            str(value) if value is not None else ""
        )

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
    def tooth_passing_harmonics(self: Self) -> "List[_4154.ToothPassingHarmonic]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ToothPassingHarmonic]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothPassingHarmonics

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2759.GearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection

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
    ) -> "GearMeshHarmonicAnalysis._Cast_GearMeshHarmonicAnalysis":
        return self._Cast_GearMeshHarmonicAnalysis(self)

"""GearMeshCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6740,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "GearMeshCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6605


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundCriticalSpeedAnalysis")


class GearMeshCompoundCriticalSpeedAnalysis(
    _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
):
    """GearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMeshCompoundCriticalSpeedAnalysis"
    )

    class _Cast_GearMeshCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GearMeshCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
            parent: "GearMeshCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6740.InterMountableComponentConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def connection_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6710,
            )

            return self._parent._cast(_6710.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6680,
            )

            return self._parent._cast(
                _6680.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6687,
            )

            return self._parent._cast(
                _6687.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6692,
            )

            return self._parent._cast(_6692.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6705,
            )

            return self._parent._cast(
                _6705.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6708,
            )

            return self._parent._cast(
                _6708.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6723,
            )

            return self._parent._cast(
                _6723.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6729,
            )

            return self._parent._cast(_6729.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6738,
            )

            return self._parent._cast(_6738.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6742,
            )

            return self._parent._cast(
                _6742.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6745,
            )

            return self._parent._cast(
                _6745.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6748,
            )

            return self._parent._cast(
                _6748.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6775,
            )

            return self._parent._cast(
                _6775.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6784,
            )

            return self._parent._cast(
                _6784.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(_6799.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(
                _6802.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
        ) -> "GearMeshCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "GearMeshCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6605.GearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearMeshCriticalSpeedAnalysis]

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
    ) -> "List[_6605.GearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearMeshCriticalSpeedAnalysis]

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
    ) -> "GearMeshCompoundCriticalSpeedAnalysis._Cast_GearMeshCompoundCriticalSpeedAnalysis":
        return self._Cast_GearMeshCompoundCriticalSpeedAnalysis(self)

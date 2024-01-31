"""GearMeshCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4793
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "GearMeshCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4635


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundModalAnalysis",)


Self = TypeVar("Self", bound="GearMeshCompoundModalAnalysis")


class GearMeshCompoundModalAnalysis(
    _4793.InterMountableComponentConnectionCompoundModalAnalysis
):
    """GearMeshCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundModalAnalysis")

    class _Cast_GearMeshCompoundModalAnalysis:
        """Special nested class for casting GearMeshCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
            parent: "GearMeshCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            return self._parent._cast(
                _4793.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4763,
            )

            return self._parent._cast(_4763.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4733,
            )

            return self._parent._cast(
                _4733.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(
                _4740.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4745,
            )

            return self._parent._cast(_4745.BevelGearMeshCompoundModalAnalysis)

        @property
        def concept_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.ConceptGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ConicalGearMeshCompoundModalAnalysis)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4782,
            )

            return self._parent._cast(_4782.FaceGearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4791,
            )

            return self._parent._cast(_4791.HypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4795,
            )

            return self._parent._cast(
                _4795.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(
                _4798.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(
                _4801.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4828,
            )

            return self._parent._cast(_4828.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(
                _4834.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4837,
            )

            return self._parent._cast(_4837.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def worm_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.WormGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4855,
            )

            return self._parent._cast(_4855.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
        ) -> "GearMeshCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_4635.GearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis]

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
    ) -> "List[_4635.GearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.GearMeshModalAnalysis]

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
    ) -> "GearMeshCompoundModalAnalysis._Cast_GearMeshCompoundModalAnalysis":
        return self._Cast_GearMeshCompoundModalAnalysis(self)

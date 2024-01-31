"""AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5021,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4861,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness"
)


class AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness(
    _5021.ConicalGearMeshCompoundModalAnalysisAtAStiffness
):
    """AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
            parent: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5021.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(_5047.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5053,
            )

            return self._parent._cast(
                _5053.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5023,
            )

            return self._parent._cast(_5023.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(
                _5000.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(
                _5005.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.HypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4861.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness]

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
    ) -> "List[_4861.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness(
            self
        )

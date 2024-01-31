"""GearSetCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5086,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "GearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4918,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="GearSetCompoundModalAnalysisAtAStiffness")


class GearSetCompoundModalAnalysisAtAStiffness(
    _5086.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
):
    """GearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_GearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting GearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
            parent: "GearSetCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _5086.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4988,
            )

            return self._parent._cast(
                _4988.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(_5067.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4994,
            )

            return self._parent._cast(
                _4994.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5001,
            )

            return self._parent._cast(
                _5001.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5006,
            )

            return self._parent._cast(
                _5006.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5019,
            )

            return self._parent._cast(
                _5019.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(
                _5037.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(
                _5043.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(
                _5052.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(
                _5056.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5059,
            )

            return self._parent._cast(
                _5059.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(
                _5062.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5072,
            )

            return self._parent._cast(
                _5072.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5095,
            )

            return self._parent._cast(
                _5095.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(
                _5098.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(
                _5113.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5116,
            )

            return self._parent._cast(
                _5116.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
        ) -> "GearSetCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "GearSetCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4918.GearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.GearSetModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4918.GearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.GearSetModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetCompoundModalAnalysisAtAStiffness._Cast_GearSetCompoundModalAnalysisAtAStiffness":
        return self._Cast_GearSetCompoundModalAnalysisAtAStiffness(self)

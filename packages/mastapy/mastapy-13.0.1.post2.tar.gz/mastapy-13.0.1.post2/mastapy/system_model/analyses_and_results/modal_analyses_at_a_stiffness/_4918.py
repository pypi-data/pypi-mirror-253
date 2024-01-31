"""GearSetModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4957,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "GearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532


__docformat__ = "restructuredtext en"
__all__ = ("GearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="GearSetModalAnalysisAtAStiffness")


class GearSetModalAnalysisAtAStiffness(
    _4957.SpecialisedAssemblyModalAnalysisAtAStiffness
):
    """GearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetModalAnalysisAtAStiffness")

    class _Cast_GearSetModalAnalysisAtAStiffness:
        """Special nested class for casting GearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
            parent: "GearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(
                _4957.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4857,
            )

            return self._parent._cast(_4857.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4863,
            )

            return self._parent._cast(
                _4863.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4870,
            )

            return self._parent._cast(
                _4870.BevelDifferentialGearSetModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4875,
            )

            return self._parent._cast(_4875.BevelGearSetModalAnalysisAtAStiffness)

        @property
        def concept_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4888,
            )

            return self._parent._cast(_4888.ConceptGearSetModalAnalysisAtAStiffness)

        @property
        def conical_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4891,
            )

            return self._parent._cast(_4891.ConicalGearSetModalAnalysisAtAStiffness)

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4906,
            )

            return self._parent._cast(_4906.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def face_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4913,
            )

            return self._parent._cast(_4913.FaceGearSetModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4922,
            )

            return self._parent._cast(_4922.HypoidGearSetModalAnalysisAtAStiffness)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4926,
            )

            return self._parent._cast(
                _4926.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4929,
            )

            return self._parent._cast(
                _4929.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4932,
            )

            return self._parent._cast(
                _4932.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4943,
            )

            return self._parent._cast(_4943.PlanetaryGearSetModalAnalysisAtAStiffness)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4960,
            )

            return self._parent._cast(_4960.SpiralBevelGearSetModalAnalysisAtAStiffness)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4966,
            )

            return self._parent._cast(
                _4966.StraightBevelDiffGearSetModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4969,
            )

            return self._parent._cast(
                _4969.StraightBevelGearSetModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4984,
            )

            return self._parent._cast(_4984.WormGearSetModalAnalysisAtAStiffness)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4987,
            )

            return self._parent._cast(_4987.ZerolBevelGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
        ) -> "GearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetModalAnalysisAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2532.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetModalAnalysisAtAStiffness._Cast_GearSetModalAnalysisAtAStiffness":
        return self._Cast_GearSetModalAnalysisAtAStiffness(self)

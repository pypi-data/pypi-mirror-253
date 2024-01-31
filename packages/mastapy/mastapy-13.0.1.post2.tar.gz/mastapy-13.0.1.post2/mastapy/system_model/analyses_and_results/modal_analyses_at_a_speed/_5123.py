"""AGMAGleasonConicalGearSetModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5151
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2514


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetModalAnalysisAtASpeed")


class AGMAGleasonConicalGearSetModalAnalysisAtASpeed(
    _5151.ConicalGearSetModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed"
    )

    class _Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5151.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(_5117.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5130,
            )

            return self._parent._cast(
                _5130.BevelDifferentialGearSetModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5135,
            )

            return self._parent._cast(_5135.BevelGearSetModalAnalysisAtASpeed)

        @property
        def hypoid_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5181,
            )

            return self._parent._cast(_5181.HypoidGearSetModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5219,
            )

            return self._parent._cast(_5219.SpiralBevelGearSetModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5225,
            )

            return self._parent._cast(
                _5225.StraightBevelDiffGearSetModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5228,
            )

            return self._parent._cast(_5228.StraightBevelGearSetModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5246,
            )

            return self._parent._cast(_5246.ZerolBevelGearSetModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2514.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

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
    ) -> "AGMAGleasonConicalGearSetModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearSetModalAnalysisAtASpeed(self)

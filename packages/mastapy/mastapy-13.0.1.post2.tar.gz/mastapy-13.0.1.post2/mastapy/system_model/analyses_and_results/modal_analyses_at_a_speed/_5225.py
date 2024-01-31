"""StraightBevelDiffGearSetModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5135
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "StraightBevelDiffGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546
    from mastapy.system_model.analyses_and_results.static_loads import _6962
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5224,
        _5223,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetModalAnalysisAtASpeed")


class StraightBevelDiffGearSetModalAnalysisAtASpeed(
    _5135.BevelGearSetModalAnalysisAtASpeed
):
    """StraightBevelDiffGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelDiffGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
            parent: "StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5135.BevelGearSetModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5123,
            )

            return self._parent._cast(
                _5123.AGMAGleasonConicalGearSetModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5151,
            )

            return self._parent._cast(_5151.ConicalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(_5117.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis_at_a_speed(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
        ) -> "StraightBevelDiffGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed",
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
        instance_to_wrap: "StraightBevelDiffGearSetModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2546.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6962.StraightBevelDiffGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5224.StraightBevelDiffGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelDiffGearModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5223.StraightBevelDiffGearMeshModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.StraightBevelDiffGearMeshModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetModalAnalysisAtASpeed._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed":
        return self._Cast_StraightBevelDiffGearSetModalAnalysisAtASpeed(self)

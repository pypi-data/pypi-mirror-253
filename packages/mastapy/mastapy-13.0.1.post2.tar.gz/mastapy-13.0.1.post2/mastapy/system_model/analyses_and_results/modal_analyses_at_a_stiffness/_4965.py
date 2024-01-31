"""StraightBevelDiffGearModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4874,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "StraightBevelDiffGearModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import _6960


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="StraightBevelDiffGearModalAnalysisAtAStiffness")


class StraightBevelDiffGearModalAnalysisAtAStiffness(
    _4874.BevelGearModalAnalysisAtAStiffness
):
    """StraightBevelDiffGearModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearModalAnalysisAtAStiffness"
    )

    class _Cast_StraightBevelDiffGearModalAnalysisAtAStiffness:
        """Special nested class for casting StraightBevelDiffGearModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
            parent: "StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def bevel_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4874.BevelGearModalAnalysisAtAStiffness)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4862,
            )

            return self._parent._cast(
                _4862.AGMAGleasonConicalGearModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4890,
            )

            return self._parent._cast(_4890.ConicalGearModalAnalysisAtAStiffness)

        @property
        def gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.GearModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4936,
            )

            return self._parent._cast(_4936.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4882,
            )

            return self._parent._cast(_4882.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4938,
            )

            return self._parent._cast(_4938.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4970,
            )

            return self._parent._cast(
                _4970.StraightBevelPlanetGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4971,
            )

            return self._parent._cast(
                _4971.StraightBevelSunGearModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_stiffness(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
        ) -> "StraightBevelDiffGearModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness",
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
        instance_to_wrap: "StraightBevelDiffGearModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6960.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearModalAnalysisAtAStiffness._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness":
        return self._Cast_StraightBevelDiffGearModalAnalysisAtAStiffness(self)

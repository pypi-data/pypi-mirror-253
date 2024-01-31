"""PlanetaryGearSetModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5166
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "PlanetaryGearSetModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PlanetaryGearSetModalAnalysisAtASpeed")


class PlanetaryGearSetModalAnalysisAtASpeed(
    _5166.CylindricalGearSetModalAnalysisAtASpeed
):
    """PlanetaryGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetModalAnalysisAtASpeed"
    )

    class _Cast_PlanetaryGearSetModalAnalysisAtASpeed:
        """Special nested class for casting PlanetaryGearSetModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
            parent: "PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5166.CylindricalGearSetModalAnalysisAtASpeed)

        @property
        def gear_set_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5177,
            )

            return self._parent._cast(_5177.GearSetModalAnalysisAtASpeed)

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5216,
            )

            return self._parent._cast(_5216.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5117,
            )

            return self._parent._cast(_5117.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_modal_analysis_at_a_speed(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
        ) -> "PlanetaryGearSetModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetModalAnalysisAtASpeed._Cast_PlanetaryGearSetModalAnalysisAtASpeed":
        return self._Cast_PlanetaryGearSetModalAnalysisAtASpeed(self)

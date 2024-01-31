"""PlanetaryGearSetModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4905,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "PlanetaryGearSetModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PlanetaryGearSetModalAnalysisAtAStiffness")


class PlanetaryGearSetModalAnalysisAtAStiffness(
    _4905.CylindricalGearSetModalAnalysisAtAStiffness
):
    """PlanetaryGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetModalAnalysisAtAStiffness"
    )

    class _Cast_PlanetaryGearSetModalAnalysisAtAStiffness:
        """Special nested class for casting PlanetaryGearSetModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
            parent: "PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_4905.CylindricalGearSetModalAnalysisAtAStiffness)

        @property
        def gear_set_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4917,
            )

            return self._parent._cast(_4917.GearSetModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4956,
            )

            return self._parent._cast(
                _4956.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4856,
            )

            return self._parent._cast(_4856.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def planetary_gear_set_modal_analysis_at_a_stiffness(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
        ) -> "PlanetaryGearSetModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetModalAnalysisAtAStiffness.TYPE"
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
    ) -> "PlanetaryGearSetModalAnalysisAtAStiffness._Cast_PlanetaryGearSetModalAnalysisAtAStiffness":
        return self._Cast_PlanetaryGearSetModalAnalysisAtAStiffness(self)

"""CylindricalPlanetGearModalAnalysisAtASpeed"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5164
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "CylindricalPlanetGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CylindricalPlanetGearModalAnalysisAtASpeed")


class CylindricalPlanetGearModalAnalysisAtASpeed(
    _5164.CylindricalGearModalAnalysisAtASpeed
):
    """CylindricalPlanetGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearModalAnalysisAtASpeed"
    )

    class _Cast_CylindricalPlanetGearModalAnalysisAtASpeed:
        """Special nested class for casting CylindricalPlanetGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
            parent: "CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_modal_analysis_at_a_speed(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            return self._parent._cast(_5164.CylindricalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5175,
            )

            return self._parent._cast(_5175.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5194,
            )

            return self._parent._cast(_5194.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5141,
            )

            return self._parent._cast(_5141.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5196,
            )

            return self._parent._cast(_5196.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis_at_a_speed(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
        ) -> "CylindricalPlanetGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "CylindricalPlanetGearModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2527.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearModalAnalysisAtASpeed._Cast_CylindricalPlanetGearModalAnalysisAtASpeed":
        return self._Cast_CylindricalPlanetGearModalAnalysisAtASpeed(self)

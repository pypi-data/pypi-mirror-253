"""CylindricalPlanetGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6861
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalPlanetGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearLoadCase",)


Self = TypeVar("Self", bound="CylindricalPlanetGearLoadCase")


class CylindricalPlanetGearLoadCase(_6861.CylindricalGearLoadCase):
    """CylindricalPlanetGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalPlanetGearLoadCase")

    class _Cast_CylindricalPlanetGearLoadCase:
        """Special nested class for casting CylindricalPlanetGearLoadCase to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
            parent: "CylindricalPlanetGearLoadCase",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ):
            return self._parent._cast(_6861.CylindricalGearLoadCase)

        @property
        def gear_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_load_case(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
        ) -> "CylindricalPlanetGearLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalPlanetGearLoadCase.TYPE"):
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
    ) -> "CylindricalPlanetGearLoadCase._Cast_CylindricalPlanetGearLoadCase":
        return self._Cast_CylindricalPlanetGearLoadCase(self)

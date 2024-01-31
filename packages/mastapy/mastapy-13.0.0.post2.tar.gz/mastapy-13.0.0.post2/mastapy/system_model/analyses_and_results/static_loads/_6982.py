"""WormGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6890
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551


__docformat__ = "restructuredtext en"
__all__ = ("WormGearLoadCase",)


Self = TypeVar("Self", bound="WormGearLoadCase")


class WormGearLoadCase(_6890.GearLoadCase):
    """WormGearLoadCase

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearLoadCase")

    class _Cast_WormGearLoadCase:
        """Special nested class for casting WormGearLoadCase to subclasses."""

        def __init__(
            self: "WormGearLoadCase._Cast_WormGearLoadCase", parent: "WormGearLoadCase"
        ):
            self._parent = parent

        @property
        def gear_load_case(self: "WormGearLoadCase._Cast_WormGearLoadCase"):
            return self._parent._cast(_6890.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def component_load_case(self: "WormGearLoadCase._Cast_WormGearLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(self: "WormGearLoadCase._Cast_WormGearLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(self: "WormGearLoadCase._Cast_WormGearLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "WormGearLoadCase._Cast_WormGearLoadCase"):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def worm_gear_load_case(
            self: "WormGearLoadCase._Cast_WormGearLoadCase",
        ) -> "WormGearLoadCase":
            return self._parent

        def __getattr__(self: "WormGearLoadCase._Cast_WormGearLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.WormGear":
        """mastapy.system_model.part_model.gears.WormGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "WormGearLoadCase._Cast_WormGearLoadCase":
        return self._Cast_WormGearLoadCase(self)

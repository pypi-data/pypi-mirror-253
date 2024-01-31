"""ZerolBevelGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6827
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ZerolBevelGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearLoadCase",)


Self = TypeVar("Self", bound="ZerolBevelGearLoadCase")


class ZerolBevelGearLoadCase(_6827.BevelGearLoadCase):
    """ZerolBevelGearLoadCase

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearLoadCase")

    class _Cast_ZerolBevelGearLoadCase:
        """Special nested class for casting ZerolBevelGearLoadCase to subclasses."""

        def __init__(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase",
            parent: "ZerolBevelGearLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_load_case(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase",
        ):
            return self._parent._cast(_6827.BevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6813

            return self._parent._cast(_6813.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.ConicalGearLoadCase)

        @property
        def gear_load_case(self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase"):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_load_case(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase",
        ) -> "ZerolBevelGearLoadCase":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ZerolBevelGearLoadCase._Cast_ZerolBevelGearLoadCase":
        return self._Cast_ZerolBevelGearLoadCase(self)

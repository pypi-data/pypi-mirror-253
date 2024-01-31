"""AGMAGleasonConicalGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearLoadCase",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearLoadCase")


class AGMAGleasonConicalGearLoadCase(_6844.ConicalGearLoadCase):
    """AGMAGleasonConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearLoadCase")

    class _Cast_AGMAGleasonConicalGearLoadCase:
        """Special nested class for casting AGMAGleasonConicalGearLoadCase to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            parent: "AGMAGleasonConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            return self._parent._cast(_6844.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ComponentLoadCase)

        @property
        def part_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartLoadCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelGearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6905

            return self._parent._cast(_6905.HypoidGearLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.ZerolBevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
        ) -> "AGMAGleasonConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2513.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearLoadCase._Cast_AGMAGleasonConicalGearLoadCase":
        return self._Cast_AGMAGleasonConicalGearLoadCase(self)

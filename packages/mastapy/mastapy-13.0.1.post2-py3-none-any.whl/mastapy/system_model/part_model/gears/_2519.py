"""BevelGear"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1180


__docformat__ = "restructuredtext en"
__all__ = ("BevelGear",)


Self = TypeVar("Self", bound="BevelGear")


class BevelGear(_2513.AGMAGleasonConicalGear):
    """BevelGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGear")

    class _Cast_BevelGear:
        """Special nested class for casting BevelGear to subclasses."""

        def __init__(self: "BevelGear._Cast_BevelGear", parent: "BevelGear"):
            self._parent = parent

        @property
        def agma_gleason_conical_gear(self: "BevelGear._Cast_BevelGear"):
            return self._parent._cast(_2513.AGMAGleasonConicalGear)

        @property
        def conical_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.ConicalGear)

        @property
        def gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.Gear)

        @property
        def mountable_component(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def bevel_differential_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelDifferentialSunGear)

        @property
        def spiral_bevel_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(self: "BevelGear._Cast_BevelGear"):
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.ZerolBevelGear)

        @property
        def bevel_gear(self: "BevelGear._Cast_BevelGear") -> "BevelGear":
            return self._parent

        def __getattr__(self: "BevelGear._Cast_BevelGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(self: Self) -> "_1180.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_design(self: Self) -> "_1180.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGear._Cast_BevelGear":
        return self._Cast_BevelGear(self)

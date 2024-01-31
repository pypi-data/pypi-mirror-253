"""AGMAGleasonConicalGear"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.gears import _2523
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGear",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGear")


class AGMAGleasonConicalGear(_2523.ConicalGear):
    """AGMAGleasonConicalGear

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGear")

    class _Cast_AGMAGleasonConicalGear:
        """Special nested class for casting AGMAGleasonConicalGear to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
            parent: "AGMAGleasonConicalGear",
        ):
            self._parent = parent

        @property
        def conical_gear(self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear"):
            return self._parent._cast(_2523.ConicalGear)

        @property
        def gear(self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.Gear)

        @property
        def mountable_component(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def bevel_differential_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear"):
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.BevelGear)

        @property
        def hypoid_gear(self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear"):
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.HypoidGear)

        @property
        def spiral_bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.ZerolBevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "AGMAGleasonConicalGear":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear":
        return self._Cast_AGMAGleasonConicalGear(self)

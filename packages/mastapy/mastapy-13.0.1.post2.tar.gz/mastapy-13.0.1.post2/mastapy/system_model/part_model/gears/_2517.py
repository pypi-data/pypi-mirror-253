"""BevelDifferentialPlanetGear"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.part_model.gears import _2515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialPlanetGear"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGear",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGear")


class BevelDifferentialPlanetGear(_2515.BevelDifferentialGear):
    """BevelDifferentialPlanetGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialPlanetGear")

    class _Cast_BevelDifferentialPlanetGear:
        """Special nested class for casting BevelDifferentialPlanetGear to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
            parent: "BevelDifferentialPlanetGear",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
        ):
            return self._parent._cast(_2515.BevelDifferentialGear)

        @property
        def bevel_gear(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
        ):
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
        ):
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
        ):
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.ConicalGear)

        @property
        def gear(self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear"):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.Gear)

        @property
        def mountable_component(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
        ):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
        ):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
        ):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def bevel_differential_planet_gear(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
        ) -> "BevelDifferentialPlanetGear":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialPlanetGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_planets(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPlanets

        if temp is None:
            return 0

        return temp

    @number_of_planets.setter
    @enforce_parameter_types
    def number_of_planets(self: Self, value: "int"):
        self.wrapped.NumberOfPlanets = int(value) if value is not None else 0

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGear._Cast_BevelDifferentialPlanetGear":
        return self._Cast_BevelDifferentialPlanetGear(self)

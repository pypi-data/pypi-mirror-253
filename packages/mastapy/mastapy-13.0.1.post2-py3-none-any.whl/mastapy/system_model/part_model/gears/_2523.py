"""ConicalGear"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.gears.gear_designs.conical import _1154


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGear",)


Self = TypeVar("Self", bound="ConicalGear")


class ConicalGear(_2530.Gear):
    """ConicalGear

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGear")

    class _Cast_ConicalGear:
        """Special nested class for casting ConicalGear to subclasses."""

        def __init__(self: "ConicalGear._Cast_ConicalGear", parent: "ConicalGear"):
            self._parent = parent

        @property
        def gear(self: "ConicalGear._Cast_ConicalGear"):
            return self._parent._cast(_2530.Gear)

        @property
        def mountable_component(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def agma_gleason_conical_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2518

            return self._parent._cast(_2518.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.BevelGear)

        @property
        def hypoid_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(self: "ConicalGear._Cast_ConicalGear"):
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.ZerolBevelGear)

        @property
        def conical_gear(self: "ConicalGear._Cast_ConicalGear") -> "ConicalGear":
            return self._parent

        def __getattr__(self: "ConicalGear._Cast_ConicalGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @property
    def orientation(self: Self) -> "_2531.GearOrientations":
        """mastapy.system_model.part_model.gears.GearOrientations"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.gears._2531", "GearOrientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: Self, value: "_2531.GearOrientations"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self: Self) -> "_1154.ConicalGearDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_design(self: Self) -> "_1154.ConicalGearDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGear._Cast_ConicalGear":
        return self._Cast_ConicalGear(self)

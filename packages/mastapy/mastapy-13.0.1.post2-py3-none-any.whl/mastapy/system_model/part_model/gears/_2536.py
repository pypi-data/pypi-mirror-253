"""KlingelnbergCycloPalloidConicalGear"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.gears import _2523
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGear"
)


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGear",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGear")


class KlingelnbergCycloPalloidConicalGear(_2523.ConicalGear):
    """KlingelnbergCycloPalloidConicalGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGear")

    class _Cast_KlingelnbergCycloPalloidConicalGear:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGear to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
            parent: "KlingelnbergCycloPalloidConicalGear",
        ):
            self._parent = parent

        @property
        def conical_gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ):
            return self._parent._cast(_2523.ConicalGear)

        @property
        def gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.Gear)

        @property
        def mountable_component(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ):
            from mastapy.system_model.part_model import _2464

            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ):
            from mastapy.system_model.part_model.gears import _2540

            return self._parent._cast(_2540.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
        ) -> "KlingelnbergCycloPalloidConicalGear":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidConicalGear.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "KlingelnbergCycloPalloidConicalGear._Cast_KlingelnbergCycloPalloidConicalGear"
    ):
        return self._Cast_KlingelnbergCycloPalloidConicalGear(self)

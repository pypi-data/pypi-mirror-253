"""KlingelnbergCycloPalloidConicalGearSetRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.conical import _542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergConical",
    "KlingelnbergCycloPalloidConicalGearSetRating",
)


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetRating")


class KlingelnbergCycloPalloidConicalGearSetRating(_542.ConicalGearSetRating):
    """KlingelnbergCycloPalloidConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSetRating"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetRating:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating",
            parent: "KlingelnbergCycloPalloidConicalGearSetRating",
        ):
            self._parent = parent

        @property
        def conical_gear_set_rating(
            self: "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating",
        ):
            return self._parent._cast(_542.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating",
        ):
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating",
        ):
            from mastapy.gears.rating import _355

            return self._parent._cast(_355.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _407

            return self._parent._cast(
                _407.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _410

            return self._parent._cast(_410.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating",
        ) -> "KlingelnbergCycloPalloidConicalGearSetRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetRating._Cast_KlingelnbergCycloPalloidConicalGearSetRating":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetRating(self)

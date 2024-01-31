"""KlingelnbergCycloPalloidSpiralBevelGearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.klingelnberg_conical import _412
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergSpiralBevel",
    "KlingelnbergCycloPalloidSpiralBevelGearRating",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _973


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearRating")


class KlingelnbergCycloPalloidSpiralBevelGearRating(
    _412.KlingelnbergCycloPalloidConicalGearRating
):
    """KlingelnbergCycloPalloidSpiralBevelGearRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearRating"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearRating:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ):
            return self._parent._cast(_412.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def conical_gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ):
            from mastapy.gears.rating.conical import _540

            return self._parent._cast(_540.ConicalGearRating)

        @property
        def gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ):
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.GearRating)

        @property
        def abstract_gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ):
            from mastapy.gears.rating import _354

            return self._parent._cast(_354.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: Self,
    ) -> "_973.KlingelnbergCycloPalloidSpiralBevelGearDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearRating(self)

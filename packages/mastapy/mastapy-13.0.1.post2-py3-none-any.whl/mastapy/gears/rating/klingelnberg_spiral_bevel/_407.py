"""KlingelnbergCycloPalloidSpiralBevelGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.klingelnberg_conical import _413
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergSpiralBevel",
    "KlingelnbergCycloPalloidSpiralBevelGearSetRating",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _975
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _406, _405


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetRating")


class KlingelnbergCycloPalloidSpiralBevelGearSetRating(
    _413.KlingelnbergCycloPalloidConicalGearSetRating
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating",
        ):
            return self._parent._cast(_413.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating",
        ):
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating",
        ):
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating",
        ):
            from mastapy.gears.rating import _355

            return self._parent._cast(_355.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: Self,
    ) -> "_975.KlingelnbergCycloPalloidSpiralBevelGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_ratings(
        self: Self,
    ) -> "List[_406.KlingelnbergCycloPalloidSpiralBevelGearRating]":
        """List[mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_mesh_ratings(
        self: Self,
    ) -> "List[_405.KlingelnbergCycloPalloidSpiralBevelGearMeshRating]":
        """List[mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetRating._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetRating(self)

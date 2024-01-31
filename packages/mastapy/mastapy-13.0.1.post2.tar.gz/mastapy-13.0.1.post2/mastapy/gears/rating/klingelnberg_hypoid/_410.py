"""KlingelnbergCycloPalloidHypoidGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.klingelnberg_conical import _413
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergHypoid",
    "KlingelnbergCycloPalloidHypoidGearSetRating",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _979
    from mastapy.gears.rating.klingelnberg_hypoid import _409, _408


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetRating",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetRating")


class KlingelnbergCycloPalloidHypoidGearSetRating(
    _413.KlingelnbergCycloPalloidConicalGearSetRating
):
    """KlingelnbergCycloPalloidHypoidGearSetRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetRating"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetRating:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetRating to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
            parent: "KlingelnbergCycloPalloidHypoidGearSetRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ):
            return self._parent._cast(_413.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ):
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ):
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ):
            from mastapy.gears.rating import _355

            return self._parent._cast(_355.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self,
    ) -> "_979.KlingelnbergCycloPalloidHypoidGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_ratings(
        self: Self,
    ) -> "List[_409.KlingelnbergCycloPalloidHypoidGearRating]":
        """List[mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_mesh_ratings(
        self: Self,
    ) -> "List[_408.KlingelnbergCycloPalloidHypoidGearMeshRating]":
        """List[mastapy.gears.rating.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetRating._Cast_KlingelnbergCycloPalloidHypoidGearSetRating":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetRating(self)

"""HypoidGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy.gears.rating.agma_gleason_conical import _567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Hypoid", "HypoidGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _987
    from mastapy.gears.rating.hypoid import _439, _438


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetRating",)


Self = TypeVar("Self", bound="HypoidGearSetRating")


class HypoidGearSetRating(_567.AGMAGleasonConicalGearSetRating):
    """HypoidGearSetRating

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetRating")

    class _Cast_HypoidGearSetRating:
        """Special nested class for casting HypoidGearSetRating to subclasses."""

        def __init__(
            self: "HypoidGearSetRating._Cast_HypoidGearSetRating",
            parent: "HypoidGearSetRating",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "HypoidGearSetRating._Cast_HypoidGearSetRating",
        ):
            return self._parent._cast(_567.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "HypoidGearSetRating._Cast_HypoidGearSetRating",
        ):
            from mastapy.gears.rating.conical import _542

            return self._parent._cast(_542.ConicalGearSetRating)

        @property
        def gear_set_rating(self: "HypoidGearSetRating._Cast_HypoidGearSetRating"):
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "HypoidGearSetRating._Cast_HypoidGearSetRating",
        ):
            from mastapy.gears.rating import _355

            return self._parent._cast(_355.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "HypoidGearSetRating._Cast_HypoidGearSetRating",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def hypoid_gear_set_rating(
            self: "HypoidGearSetRating._Cast_HypoidGearSetRating",
        ) -> "HypoidGearSetRating":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetRating._Cast_HypoidGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetRating.TYPE"):
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
    def size_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def size_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def hypoid_gear_set(self: Self) -> "_987.HypoidGearSetDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_ratings(self: Self) -> "List[_439.HypoidGearRating]":
        """List[mastapy.gears.rating.hypoid.HypoidGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_mesh_ratings(self: Self) -> "List[_438.HypoidGearMeshRating]":
        """List[mastapy.gears.rating.hypoid.HypoidGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "HypoidGearSetRating._Cast_HypoidGearSetRating":
        return self._Cast_HypoidGearSetRating(self)

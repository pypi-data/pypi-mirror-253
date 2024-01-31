"""StraightBevelDiffGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.conical import _542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.StraightBevelDiff", "StraightBevelDiffGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _967
    from mastapy.gears.rating.straight_bevel_diff import _399, _398


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetRating",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetRating")


class StraightBevelDiffGearSetRating(_542.ConicalGearSetRating):
    """StraightBevelDiffGearSetRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearSetRating")

    class _Cast_StraightBevelDiffGearSetRating:
        """Special nested class for casting StraightBevelDiffGearSetRating to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetRating._Cast_StraightBevelDiffGearSetRating",
            parent: "StraightBevelDiffGearSetRating",
        ):
            self._parent = parent

        @property
        def conical_gear_set_rating(
            self: "StraightBevelDiffGearSetRating._Cast_StraightBevelDiffGearSetRating",
        ):
            return self._parent._cast(_542.ConicalGearSetRating)

        @property
        def gear_set_rating(
            self: "StraightBevelDiffGearSetRating._Cast_StraightBevelDiffGearSetRating",
        ):
            from mastapy.gears.rating import _363

            return self._parent._cast(_363.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "StraightBevelDiffGearSetRating._Cast_StraightBevelDiffGearSetRating",
        ):
            from mastapy.gears.rating import _355

            return self._parent._cast(_355.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "StraightBevelDiffGearSetRating._Cast_StraightBevelDiffGearSetRating",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "StraightBevelDiffGearSetRating._Cast_StraightBevelDiffGearSetRating",
        ) -> "StraightBevelDiffGearSetRating":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetRating._Cast_StraightBevelDiffGearSetRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearSetRating.TYPE"):
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
    def straight_bevel_diff_gear_set(
        self: Self,
    ) -> "_967.StraightBevelDiffGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gear_ratings(
        self: Self,
    ) -> "List[_399.StraightBevelDiffGearRating]":
        """List[mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_mesh_ratings(
        self: Self,
    ) -> "List[_398.StraightBevelDiffGearMeshRating]":
        """List[mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetRating._Cast_StraightBevelDiffGearSetRating":
        return self._Cast_StraightBevelDiffGearSetRating(self)

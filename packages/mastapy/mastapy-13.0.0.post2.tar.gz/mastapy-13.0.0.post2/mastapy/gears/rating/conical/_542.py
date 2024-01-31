"""ConicalGearSetRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearSetRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs import _943


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetRating",)


Self = TypeVar("Self", bound="ConicalGearSetRating")


class ConicalGearSetRating(_363.GearSetRating):
    """ConicalGearSetRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetRating")

    class _Cast_ConicalGearSetRating:
        """Special nested class for casting ConicalGearSetRating to subclasses."""

        def __init__(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
            parent: "ConicalGearSetRating",
        ):
            self._parent = parent

        @property
        def gear_set_rating(self: "ConicalGearSetRating._Cast_ConicalGearSetRating"):
            return self._parent._cast(_363.GearSetRating)

        @property
        def abstract_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating import _355

            return self._parent._cast(_355.AbstractGearSetRating)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearSetAnalysis)

        @property
        def zerol_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.zerol_bevel import _371

            return self._parent._cast(_371.ZerolBevelGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.straight_bevel import _397

            return self._parent._cast(_397.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _400

            return self._parent._cast(_400.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.spiral_bevel import _404

            return self._parent._cast(_404.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _407

            return self._parent._cast(
                _407.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _410

            return self._parent._cast(_410.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _413

            return self._parent._cast(_413.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.hypoid import _440

            return self._parent._cast(_440.HypoidGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.bevel import _556

            return self._parent._cast(_556.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _567

            return self._parent._cast(_567.AGMAGleasonConicalGearSetRating)

        @property
        def conical_gear_set_rating(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating",
        ) -> "ConicalGearSetRating":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetRating._Cast_ConicalGearSetRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating_settings(self: Self) -> "_943.BevelHypoidGearRatingSettingsItem":
        """mastapy.gears.gear_designs.BevelHypoidGearRatingSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearSetRating._Cast_ConicalGearSetRating":
        return self._Cast_ConicalGearSetRating(self)

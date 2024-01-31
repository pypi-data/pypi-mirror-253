"""ConicalGearSingleFlankRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating import _364
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearSingleFlankRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSingleFlankRating",)


Self = TypeVar("Self", bound="ConicalGearSingleFlankRating")


class ConicalGearSingleFlankRating(_364.GearSingleFlankRating):
    """ConicalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSingleFlankRating")

    class _Cast_ConicalGearSingleFlankRating:
        """Special nested class for casting ConicalGearSingleFlankRating to subclasses."""

        def __init__(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
            parent: "ConicalGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            return self._parent._cast(_364.GearSingleFlankRating)

        @property
        def iso10300_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _429

            return self._parent._cast(_429.ISO10300SingleFlankRating)

        @property
        def iso10300_single_flank_rating_bevel_method_b2(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _430

            return self._parent._cast(_430.ISO10300SingleFlankRatingBevelMethodB2)

        @property
        def iso10300_single_flank_rating_hypoid_method_b2(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _431

            return self._parent._cast(_431.ISO10300SingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_single_flank_rating_method_b1(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _432

            return self._parent._cast(_432.ISO10300SingleFlankRatingMethodB1)

        @property
        def iso10300_single_flank_rating_method_b2(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            from mastapy.gears.rating.iso_10300 import _433

            return self._parent._cast(_433.ISO10300SingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            from mastapy.gears.rating.hypoid.standards import _442

            return self._parent._cast(_442.GleasonHypoidGearSingleFlankRating)

        @property
        def agma_spiral_bevel_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _557

            return self._parent._cast(_557.AGMASpiralBevelGearSingleFlankRating)

        @property
        def gleason_spiral_bevel_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _559

            return self._parent._cast(_559.GleasonSpiralBevelGearSingleFlankRating)

        @property
        def spiral_bevel_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _561

            return self._parent._cast(_561.SpiralBevelGearSingleFlankRating)

        @property
        def conical_gear_single_flank_rating(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
        ) -> "ConicalGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSingleFlankRating._Cast_ConicalGearSingleFlankRating":
        return self._Cast_ConicalGearSingleFlankRating(self)

"""AGMAGleasonConicalGearRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.conical import _540
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.AGMAGleasonConical", "AGMAGleasonConicalGearRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearRating",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearRating")


class AGMAGleasonConicalGearRating(_540.ConicalGearRating):
    """AGMAGleasonConicalGearRating

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearRating")

    class _Cast_AGMAGleasonConicalGearRating:
        """Special nested class for casting AGMAGleasonConicalGearRating to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
            parent: "AGMAGleasonConicalGearRating",
        ):
            self._parent = parent

        @property
        def conical_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ):
            return self._parent._cast(_540.ConicalGearRating)

        @property
        def gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ):
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.GearRating)

        @property
        def abstract_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ):
            from mastapy.gears.rating import _354

            return self._parent._cast(_354.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ):
            from mastapy.gears.rating.zerol_bevel import _370

            return self._parent._cast(_370.ZerolBevelGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ):
            from mastapy.gears.rating.straight_bevel import _396

            return self._parent._cast(_396.StraightBevelGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ):
            from mastapy.gears.rating.spiral_bevel import _403

            return self._parent._cast(_403.SpiralBevelGearRating)

        @property
        def hypoid_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ):
            from mastapy.gears.rating.hypoid import _439

            return self._parent._cast(_439.HypoidGearRating)

        @property
        def bevel_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ):
            from mastapy.gears.rating.bevel import _555

            return self._parent._cast(_555.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
        ) -> "AGMAGleasonConicalGearRating":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearRating._Cast_AGMAGleasonConicalGearRating":
        return self._Cast_AGMAGleasonConicalGearRating(self)

"""ZerolBevelGearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.bevel import _555
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.ZerolBevel", "ZerolBevelGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _952


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearRating",)


Self = TypeVar("Self", bound="ZerolBevelGearRating")


class ZerolBevelGearRating(_555.BevelGearRating):
    """ZerolBevelGearRating

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearRating")

    class _Cast_ZerolBevelGearRating:
        """Special nested class for casting ZerolBevelGearRating to subclasses."""

        def __init__(
            self: "ZerolBevelGearRating._Cast_ZerolBevelGearRating",
            parent: "ZerolBevelGearRating",
        ):
            self._parent = parent

        @property
        def bevel_gear_rating(self: "ZerolBevelGearRating._Cast_ZerolBevelGearRating"):
            return self._parent._cast(_555.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "ZerolBevelGearRating._Cast_ZerolBevelGearRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _566

            return self._parent._cast(_566.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(
            self: "ZerolBevelGearRating._Cast_ZerolBevelGearRating",
        ):
            from mastapy.gears.rating.conical import _540

            return self._parent._cast(_540.ConicalGearRating)

        @property
        def gear_rating(self: "ZerolBevelGearRating._Cast_ZerolBevelGearRating"):
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.GearRating)

        @property
        def abstract_gear_rating(
            self: "ZerolBevelGearRating._Cast_ZerolBevelGearRating",
        ):
            from mastapy.gears.rating import _354

            return self._parent._cast(_354.AbstractGearRating)

        @property
        def abstract_gear_analysis(
            self: "ZerolBevelGearRating._Cast_ZerolBevelGearRating",
        ):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(
            self: "ZerolBevelGearRating._Cast_ZerolBevelGearRating",
        ) -> "ZerolBevelGearRating":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearRating._Cast_ZerolBevelGearRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear(self: Self) -> "_952.ZerolBevelGearDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ZerolBevelGearRating._Cast_ZerolBevelGearRating":
        return self._Cast_ZerolBevelGearRating(self)

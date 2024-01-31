"""ISO63362019GearSingleFlankRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.cylindrical.iso6336 import _513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO63362019_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336", "ISO63362019GearSingleFlankRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("ISO63362019GearSingleFlankRating",)


Self = TypeVar("Self", bound="ISO63362019GearSingleFlankRating")


class ISO63362019GearSingleFlankRating(_513.ISO63362006GearSingleFlankRating):
    """ISO63362019GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO63362019_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO63362019GearSingleFlankRating")

    class _Cast_ISO63362019GearSingleFlankRating:
        """Special nested class for casting ISO63362019GearSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating",
            parent: "ISO63362019GearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso63362006_gear_single_flank_rating(
            self: "ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating",
        ):
            return self._parent._cast(_513.ISO63362006GearSingleFlankRating)

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(
            self: "ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _519

            return self._parent._cast(_519.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(
            self: "ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical.iso6336 import _517

            return self._parent._cast(_517.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(
            self: "ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating",
        ):
            from mastapy.gears.rating.cylindrical import _465

            return self._parent._cast(_465.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating",
        ):
            from mastapy.gears.rating import _364

            return self._parent._cast(_364.GearSingleFlankRating)

        @property
        def iso63362019_gear_single_flank_rating(
            self: "ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating",
        ) -> "ISO63362019GearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO63362019GearSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_distribution_influence_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionInfluenceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO63362019GearSingleFlankRating._Cast_ISO63362019GearSingleFlankRating":
        return self._Cast_ISO63362019GearSingleFlankRating(self)

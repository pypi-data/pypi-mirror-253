"""ConicalGearRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _361
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Conical", "ConicalGearRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _359


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearRating",)


Self = TypeVar("Self", bound="ConicalGearRating")


class ConicalGearRating(_361.GearRating):
    """ConicalGearRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearRating")

    class _Cast_ConicalGearRating:
        """Special nested class for casting ConicalGearRating to subclasses."""

        def __init__(
            self: "ConicalGearRating._Cast_ConicalGearRating",
            parent: "ConicalGearRating",
        ):
            self._parent = parent

        @property
        def gear_rating(self: "ConicalGearRating._Cast_ConicalGearRating"):
            return self._parent._cast(_361.GearRating)

        @property
        def abstract_gear_rating(self: "ConicalGearRating._Cast_ConicalGearRating"):
            from mastapy.gears.rating import _354

            return self._parent._cast(_354.AbstractGearRating)

        @property
        def abstract_gear_analysis(self: "ConicalGearRating._Cast_ConicalGearRating"):
            from mastapy.gears.analysis import _1215

            return self._parent._cast(_1215.AbstractGearAnalysis)

        @property
        def zerol_bevel_gear_rating(self: "ConicalGearRating._Cast_ConicalGearRating"):
            from mastapy.gears.rating.zerol_bevel import _370

            return self._parent._cast(_370.ZerolBevelGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ):
            from mastapy.gears.rating.straight_bevel import _396

            return self._parent._cast(_396.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ):
            from mastapy.gears.rating.straight_bevel_diff import _399

            return self._parent._cast(_399.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(self: "ConicalGearRating._Cast_ConicalGearRating"):
            from mastapy.gears.rating.spiral_bevel import _403

            return self._parent._cast(_403.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ):
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _406

            return self._parent._cast(
                _406.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ):
            from mastapy.gears.rating.klingelnberg_hypoid import _409

            return self._parent._cast(_409.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ):
            from mastapy.gears.rating.klingelnberg_conical import _412

            return self._parent._cast(_412.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(self: "ConicalGearRating._Cast_ConicalGearRating"):
            from mastapy.gears.rating.hypoid import _439

            return self._parent._cast(_439.HypoidGearRating)

        @property
        def bevel_gear_rating(self: "ConicalGearRating._Cast_ConicalGearRating"):
            from mastapy.gears.rating.bevel import _555

            return self._parent._cast(_555.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ):
            from mastapy.gears.rating.agma_gleason_conical import _566

            return self._parent._cast(_566.AGMAGleasonConicalGearRating)

        @property
        def conical_gear_rating(
            self: "ConicalGearRating._Cast_ConicalGearRating",
        ) -> "ConicalGearRating":
            return self._parent

        def __getattr__(self: "ConicalGearRating._Cast_ConicalGearRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concave_flank_rating(self: Self) -> "_359.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConcaveFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def convex_flank_rating(self: Self) -> "_359.GearFlankRating":
        """mastapy.gears.rating.GearFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConvexFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGearRating._Cast_ConicalGearRating":
        return self._Cast_ConicalGearRating(self)

"""SpiralBevelGearSingleFlankRating"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.conical import _543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Bevel.Standards", "SpiralBevelGearSingleFlankRating"
)


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSingleFlankRating",)


Self = TypeVar("Self", bound="SpiralBevelGearSingleFlankRating")


class SpiralBevelGearSingleFlankRating(_543.ConicalGearSingleFlankRating):
    """SpiralBevelGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSingleFlankRating")

    class _Cast_SpiralBevelGearSingleFlankRating:
        """Special nested class for casting SpiralBevelGearSingleFlankRating to subclasses."""

        def __init__(
            self: "SpiralBevelGearSingleFlankRating._Cast_SpiralBevelGearSingleFlankRating",
            parent: "SpiralBevelGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def conical_gear_single_flank_rating(
            self: "SpiralBevelGearSingleFlankRating._Cast_SpiralBevelGearSingleFlankRating",
        ):
            return self._parent._cast(_543.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "SpiralBevelGearSingleFlankRating._Cast_SpiralBevelGearSingleFlankRating",
        ):
            from mastapy.gears.rating import _364

            return self._parent._cast(_364.GearSingleFlankRating)

        @property
        def agma_spiral_bevel_gear_single_flank_rating(
            self: "SpiralBevelGearSingleFlankRating._Cast_SpiralBevelGearSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _557

            return self._parent._cast(_557.AGMASpiralBevelGearSingleFlankRating)

        @property
        def gleason_spiral_bevel_gear_single_flank_rating(
            self: "SpiralBevelGearSingleFlankRating._Cast_SpiralBevelGearSingleFlankRating",
        ):
            from mastapy.gears.rating.bevel.standards import _559

            return self._parent._cast(_559.GleasonSpiralBevelGearSingleFlankRating)

        @property
        def spiral_bevel_gear_single_flank_rating(
            self: "SpiralBevelGearSingleFlankRating._Cast_SpiralBevelGearSingleFlankRating",
        ) -> "SpiralBevelGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSingleFlankRating._Cast_SpiralBevelGearSingleFlankRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_strength_geometry_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStrengthGeometryFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistanceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def durability_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DurabilityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_j(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorJ

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def life_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_condition_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceConditionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSingleFlankRating._Cast_SpiralBevelGearSingleFlankRating":
        return self._Cast_SpiralBevelGearSingleFlankRating(self)

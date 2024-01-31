"""WormMeshDutyCycleRating"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.gears.rating import _365
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_MESH_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Worm", "WormMeshDutyCycleRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.worm import _373


__docformat__ = "restructuredtext en"
__all__ = ("WormMeshDutyCycleRating",)


Self = TypeVar("Self", bound="WormMeshDutyCycleRating")


class WormMeshDutyCycleRating(_365.MeshDutyCycleRating):
    """WormMeshDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _WORM_MESH_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormMeshDutyCycleRating")

    class _Cast_WormMeshDutyCycleRating:
        """Special nested class for casting WormMeshDutyCycleRating to subclasses."""

        def __init__(
            self: "WormMeshDutyCycleRating._Cast_WormMeshDutyCycleRating",
            parent: "WormMeshDutyCycleRating",
        ):
            self._parent = parent

        @property
        def mesh_duty_cycle_rating(
            self: "WormMeshDutyCycleRating._Cast_WormMeshDutyCycleRating",
        ):
            return self._parent._cast(_365.MeshDutyCycleRating)

        @property
        def abstract_gear_mesh_rating(
            self: "WormMeshDutyCycleRating._Cast_WormMeshDutyCycleRating",
        ):
            from mastapy.gears.rating import _353

            return self._parent._cast(_353.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "WormMeshDutyCycleRating._Cast_WormMeshDutyCycleRating",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "WormMeshDutyCycleRating._Cast_WormMeshDutyCycleRating",
        ) -> "WormMeshDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "WormMeshDutyCycleRating._Cast_WormMeshDutyCycleRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormMeshDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_mesh_ratings(self: Self) -> "List[_373.WormGearMeshRating]":
        """List[mastapy.gears.rating.worm.WormGearMeshRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "WormMeshDutyCycleRating._Cast_WormMeshDutyCycleRating":
        return self._Cast_WormMeshDutyCycleRating(self)

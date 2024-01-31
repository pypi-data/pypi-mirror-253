"""SphericalRollerBearing"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_designs.rolling import _2142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPHERICAL_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "SphericalRollerBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("SphericalRollerBearing",)


Self = TypeVar("Self", bound="SphericalRollerBearing")


class SphericalRollerBearing(_2142.BarrelRollerBearing):
    """SphericalRollerBearing

    This is a mastapy class.
    """

    TYPE = _SPHERICAL_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SphericalRollerBearing")

    class _Cast_SphericalRollerBearing:
        """Special nested class for casting SphericalRollerBearing to subclasses."""

        def __init__(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
            parent: "SphericalRollerBearing",
        ):
            self._parent = parent

        @property
        def barrel_roller_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ):
            return self._parent._cast(_2142.BarrelRollerBearing)

        @property
        def roller_bearing(self: "SphericalRollerBearing._Cast_SphericalRollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2162

            return self._parent._cast(_2162.RollerBearing)

        @property
        def rolling_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2165

            return self._parent._cast(_2165.RollingBearing)

        @property
        def detailed_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ):
            from mastapy.bearings.bearing_designs import _2131

            return self._parent._cast(_2131.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ):
            from mastapy.bearings.bearing_designs import _2134

            return self._parent._cast(_2134.NonLinearBearing)

        @property
        def bearing_design(self: "SphericalRollerBearing._Cast_SphericalRollerBearing"):
            from mastapy.bearings.bearing_designs import _2130

            return self._parent._cast(_2130.BearingDesign)

        @property
        def spherical_roller_bearing(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing",
        ) -> "SphericalRollerBearing":
            return self._parent

        def __getattr__(
            self: "SphericalRollerBearing._Cast_SphericalRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SphericalRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SphericalRollerBearing._Cast_SphericalRollerBearing":
        return self._Cast_SphericalRollerBearing(self)

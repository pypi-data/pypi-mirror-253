"""AngularContactBallBearing"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_designs.rolling import _2140
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_CONTACT_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "AngularContactBallBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("AngularContactBallBearing",)


Self = TypeVar("Self", bound="AngularContactBallBearing")


class AngularContactBallBearing(_2140.BallBearing):
    """AngularContactBallBearing

    This is a mastapy class.
    """

    TYPE = _ANGULAR_CONTACT_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngularContactBallBearing")

    class _Cast_AngularContactBallBearing:
        """Special nested class for casting AngularContactBallBearing to subclasses."""

        def __init__(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
            parent: "AngularContactBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ):
            return self._parent._cast(_2140.BallBearing)

        @property
        def rolling_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2165

            return self._parent._cast(_2165.RollingBearing)

        @property
        def detailed_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs import _2131

            return self._parent._cast(_2131.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs import _2134

            return self._parent._cast(_2134.NonLinearBearing)

        @property
        def bearing_design(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs import _2130

            return self._parent._cast(_2130.BearingDesign)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2136

            return self._parent._cast(_2136.AngularContactThrustBallBearing)

        @property
        def angular_contact_ball_bearing(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing",
        ) -> "AngularContactBallBearing":
            return self._parent

        def __getattr__(
            self: "AngularContactBallBearing._Cast_AngularContactBallBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngularContactBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AngularContactBallBearing._Cast_AngularContactBallBearing":
        return self._Cast_AngularContactBallBearing(self)

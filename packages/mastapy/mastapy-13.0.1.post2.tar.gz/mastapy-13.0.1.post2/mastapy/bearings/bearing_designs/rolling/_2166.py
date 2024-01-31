"""SelfAligningBallBearing"""
from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.rolling import _2140
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SELF_ALIGNING_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "SelfAligningBallBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("SelfAligningBallBearing",)


Self = TypeVar("Self", bound="SelfAligningBallBearing")


class SelfAligningBallBearing(_2140.BallBearing):
    """SelfAligningBallBearing

    This is a mastapy class.
    """

    TYPE = _SELF_ALIGNING_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SelfAligningBallBearing")

    class _Cast_SelfAligningBallBearing:
        """Special nested class for casting SelfAligningBallBearing to subclasses."""

        def __init__(
            self: "SelfAligningBallBearing._Cast_SelfAligningBallBearing",
            parent: "SelfAligningBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(self: "SelfAligningBallBearing._Cast_SelfAligningBallBearing"):
            return self._parent._cast(_2140.BallBearing)

        @property
        def rolling_bearing(
            self: "SelfAligningBallBearing._Cast_SelfAligningBallBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2165

            return self._parent._cast(_2165.RollingBearing)

        @property
        def detailed_bearing(
            self: "SelfAligningBallBearing._Cast_SelfAligningBallBearing",
        ):
            from mastapy.bearings.bearing_designs import _2131

            return self._parent._cast(_2131.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "SelfAligningBallBearing._Cast_SelfAligningBallBearing",
        ):
            from mastapy.bearings.bearing_designs import _2134

            return self._parent._cast(_2134.NonLinearBearing)

        @property
        def bearing_design(
            self: "SelfAligningBallBearing._Cast_SelfAligningBallBearing",
        ):
            from mastapy.bearings.bearing_designs import _2130

            return self._parent._cast(_2130.BearingDesign)

        @property
        def self_aligning_ball_bearing(
            self: "SelfAligningBallBearing._Cast_SelfAligningBallBearing",
        ) -> "SelfAligningBallBearing":
            return self._parent

        def __getattr__(
            self: "SelfAligningBallBearing._Cast_SelfAligningBallBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SelfAligningBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_ring_shoulder_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerRingShoulderDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_ring_shoulder_diameter.setter
    @enforce_parameter_types
    def inner_ring_shoulder_diameter(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerRingShoulderDiameter = value

    @property
    def inner_ring_shoulder_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerRingShoulderHeight

        if temp is None:
            return 0.0

        return temp

    @inner_ring_shoulder_height.setter
    @enforce_parameter_types
    def inner_ring_shoulder_height(self: Self, value: "float"):
        self.wrapped.InnerRingShoulderHeight = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "SelfAligningBallBearing._Cast_SelfAligningBallBearing":
        return self._Cast_SelfAligningBallBearing(self)

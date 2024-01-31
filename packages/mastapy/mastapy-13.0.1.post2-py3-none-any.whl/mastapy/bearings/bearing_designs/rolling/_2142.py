"""BarrelRollerBearing"""
from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.bearings.bearing_designs.rolling import _2162
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BARREL_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "BarrelRollerBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("BarrelRollerBearing",)


Self = TypeVar("Self", bound="BarrelRollerBearing")


class BarrelRollerBearing(_2162.RollerBearing):
    """BarrelRollerBearing

    This is a mastapy class.
    """

    TYPE = _BARREL_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BarrelRollerBearing")

    class _Cast_BarrelRollerBearing:
        """Special nested class for casting BarrelRollerBearing to subclasses."""

        def __init__(
            self: "BarrelRollerBearing._Cast_BarrelRollerBearing",
            parent: "BarrelRollerBearing",
        ):
            self._parent = parent

        @property
        def roller_bearing(self: "BarrelRollerBearing._Cast_BarrelRollerBearing"):
            return self._parent._cast(_2162.RollerBearing)

        @property
        def rolling_bearing(self: "BarrelRollerBearing._Cast_BarrelRollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2165

            return self._parent._cast(_2165.RollingBearing)

        @property
        def detailed_bearing(self: "BarrelRollerBearing._Cast_BarrelRollerBearing"):
            from mastapy.bearings.bearing_designs import _2131

            return self._parent._cast(_2131.DetailedBearing)

        @property
        def non_linear_bearing(self: "BarrelRollerBearing._Cast_BarrelRollerBearing"):
            from mastapy.bearings.bearing_designs import _2134

            return self._parent._cast(_2134.NonLinearBearing)

        @property
        def bearing_design(self: "BarrelRollerBearing._Cast_BarrelRollerBearing"):
            from mastapy.bearings.bearing_designs import _2130

            return self._parent._cast(_2130.BearingDesign)

        @property
        def spherical_roller_bearing(
            self: "BarrelRollerBearing._Cast_BarrelRollerBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "BarrelRollerBearing._Cast_BarrelRollerBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2170

            return self._parent._cast(_2170.SphericalRollerThrustBearing)

        @property
        def toroidal_roller_bearing(
            self: "BarrelRollerBearing._Cast_BarrelRollerBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2174

            return self._parent._cast(_2174.ToroidalRollerBearing)

        @property
        def barrel_roller_bearing(
            self: "BarrelRollerBearing._Cast_BarrelRollerBearing",
        ) -> "BarrelRollerBearing":
            return self._parent

        def __getattr__(
            self: "BarrelRollerBearing._Cast_BarrelRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BarrelRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_profile_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementProfileRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_profile_radius.setter
    @enforce_parameter_types
    def element_profile_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementProfileRadius = value

    @property
    def groove_radius_inner(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.GrooveRadiusInner

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @groove_radius_inner.setter
    @enforce_parameter_types
    def groove_radius_inner(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.GrooveRadiusInner = value

    @property
    def groove_radius_outer(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.GrooveRadiusOuter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @groove_radius_outer.setter
    @enforce_parameter_types
    def groove_radius_outer(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.GrooveRadiusOuter = value

    @property
    def roller_race_radius_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RollerRaceRadiusRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @roller_race_radius_ratio.setter
    @enforce_parameter_types
    def roller_race_radius_ratio(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RollerRaceRadiusRatio = value

    @property
    def cast_to(self: Self) -> "BarrelRollerBearing._Cast_BarrelRollerBearing":
        return self._Cast_BarrelRollerBearing(self)

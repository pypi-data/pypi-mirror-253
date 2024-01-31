"""SphericalRollerThrustBearing"""
from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPHERICAL_ROLLER_THRUST_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "SphericalRollerThrustBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("SphericalRollerThrustBearing",)


Self = TypeVar("Self", bound="SphericalRollerThrustBearing")


class SphericalRollerThrustBearing(_2142.BarrelRollerBearing):
    """SphericalRollerThrustBearing

    This is a mastapy class.
    """

    TYPE = _SPHERICAL_ROLLER_THRUST_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SphericalRollerThrustBearing")

    class _Cast_SphericalRollerThrustBearing:
        """Special nested class for casting SphericalRollerThrustBearing to subclasses."""

        def __init__(
            self: "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing",
            parent: "SphericalRollerThrustBearing",
        ):
            self._parent = parent

        @property
        def barrel_roller_bearing(
            self: "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing",
        ):
            return self._parent._cast(_2142.BarrelRollerBearing)

        @property
        def roller_bearing(
            self: "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2162

            return self._parent._cast(_2162.RollerBearing)

        @property
        def rolling_bearing(
            self: "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2165

            return self._parent._cast(_2165.RollingBearing)

        @property
        def detailed_bearing(
            self: "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing",
        ):
            from mastapy.bearings.bearing_designs import _2131

            return self._parent._cast(_2131.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing",
        ):
            from mastapy.bearings.bearing_designs import _2134

            return self._parent._cast(_2134.NonLinearBearing)

        @property
        def bearing_design(
            self: "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing",
        ):
            from mastapy.bearings.bearing_designs import _2130

            return self._parent._cast(_2130.BearingDesign)

        @property
        def spherical_roller_thrust_bearing(
            self: "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing",
        ) -> "SphericalRollerThrustBearing":
            return self._parent

        def __getattr__(
            self: "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SphericalRollerThrustBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_roller_end_and_bearing_axis(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleBetweenRollerEndAndBearingAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_to_pressure_point_from_left_face(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceToPressurePointFromLeftFace

        if temp is None:
            return 0.0

        return temp

    @distance_to_pressure_point_from_left_face.setter
    @enforce_parameter_types
    def distance_to_pressure_point_from_left_face(self: Self, value: "float"):
        self.wrapped.DistanceToPressurePointFromLeftFace = (
            float(value) if value is not None else 0.0
        )

    @property
    def effective_taper_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveTaperAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def element_centre_point_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementCentrePointDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def major_diameter_offset_from_roller_centre(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MajorDiameterOffsetFromRollerCentre

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @major_diameter_offset_from_roller_centre.setter
    @enforce_parameter_types
    def major_diameter_offset_from_roller_centre(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MajorDiameterOffsetFromRollerCentre = value

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "SphericalRollerThrustBearing._Cast_SphericalRollerThrustBearing":
        return self._Cast_SphericalRollerThrustBearing(self)

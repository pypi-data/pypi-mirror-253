"""RollerBearing"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings import _1891
from mastapy.bearings.bearing_designs.rolling import _2165
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "RollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.roller_bearing_profiles import _1928, _1938


__docformat__ = "restructuredtext en"
__all__ = ("RollerBearing",)


Self = TypeVar("Self", bound="RollerBearing")


class RollerBearing(_2165.RollingBearing):
    """RollerBearing

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerBearing")

    class _Cast_RollerBearing:
        """Special nested class for casting RollerBearing to subclasses."""

        def __init__(
            self: "RollerBearing._Cast_RollerBearing", parent: "RollerBearing"
        ):
            self._parent = parent

        @property
        def rolling_bearing(self: "RollerBearing._Cast_RollerBearing"):
            return self._parent._cast(_2165.RollingBearing)

        @property
        def detailed_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs import _2131

            return self._parent._cast(_2131.DetailedBearing)

        @property
        def non_linear_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs import _2134

            return self._parent._cast(_2134.NonLinearBearing)

        @property
        def bearing_design(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs import _2130

            return self._parent._cast(_2130.BearingDesign)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "RollerBearing._Cast_RollerBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2137

            return self._parent._cast(_2137.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "RollerBearing._Cast_RollerBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2138

            return self._parent._cast(_2138.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "RollerBearing._Cast_RollerBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2139

            return self._parent._cast(_2139.AxialThrustNeedleRollerBearing)

        @property
        def barrel_roller_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2142

            return self._parent._cast(_2142.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2148

            return self._parent._cast(_2148.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2149

            return self._parent._cast(_2149.CylindricalRollerBearing)

        @property
        def needle_roller_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2160

            return self._parent._cast(_2160.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2161

            return self._parent._cast(_2161.NonBarrelRollerBearing)

        @property
        def spherical_roller_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2170

            return self._parent._cast(_2170.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2171

            return self._parent._cast(_2171.TaperRollerBearing)

        @property
        def toroidal_roller_bearing(self: "RollerBearing._Cast_RollerBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2174

            return self._parent._cast(_2174.ToroidalRollerBearing)

        @property
        def roller_bearing(
            self: "RollerBearing._Cast_RollerBearing",
        ) -> "RollerBearing":
            return self._parent

        def __getattr__(self: "RollerBearing._Cast_RollerBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def corner_radii(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CornerRadii

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @corner_radii.setter
    @enforce_parameter_types
    def corner_radii(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CornerRadii = value

    @property
    def effective_roller_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveRollerLength

        if temp is None:
            return 0.0

        return temp

    @property
    def element_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_diameter.setter
    @enforce_parameter_types
    def element_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementDiameter = value

    @property
    def kl(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.KL

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @kl.setter
    @enforce_parameter_types
    def kl(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.KL = value

    @property
    def roller_length(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RollerLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @roller_length.setter
    @enforce_parameter_types
    def roller_length(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RollerLength = value

    @property
    def roller_profile(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RollerBearingProfileTypes":
        """EnumWithSelectedValue[mastapy.bearings.RollerBearingProfileTypes]"""
        temp = self.wrapped.RollerProfile

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RollerBearingProfileTypes.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @roller_profile.setter
    @enforce_parameter_types
    def roller_profile(self: Self, value: "_1891.RollerBearingProfileTypes"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RollerBearingProfileTypes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RollerProfile = value

    @property
    def inner_race_profile_set(self: Self) -> "_1928.ProfileSet":
        """mastapy.bearings.roller_bearing_profiles.ProfileSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRaceProfileSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_race_profile_set(self: Self) -> "_1928.ProfileSet":
        """mastapy.bearings.roller_bearing_profiles.ProfileSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRaceProfileSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def roller_profile_set(self: Self) -> "_1928.ProfileSet":
        """mastapy.bearings.roller_bearing_profiles.ProfileSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollerProfileSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_race_and_roller_profiles(
        self: Self,
    ) -> "List[_1938.RollerRaceProfilePoint]":
        """List[mastapy.bearings.roller_bearing_profiles.RollerRaceProfilePoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRaceAndRollerProfiles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def inner_race_and_roller_profiles_for_first_row(
        self: Self,
    ) -> "List[_1938.RollerRaceProfilePoint]":
        """List[mastapy.bearings.roller_bearing_profiles.RollerRaceProfilePoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRaceAndRollerProfilesForFirstRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def inner_race_and_roller_profiles_for_second_row(
        self: Self,
    ) -> "List[_1938.RollerRaceProfilePoint]":
        """List[mastapy.bearings.roller_bearing_profiles.RollerRaceProfilePoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerRaceAndRollerProfilesForSecondRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def outer_race_and_roller_profiles(
        self: Self,
    ) -> "List[_1938.RollerRaceProfilePoint]":
        """List[mastapy.bearings.roller_bearing_profiles.RollerRaceProfilePoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRaceAndRollerProfiles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def outer_race_and_roller_profiles_for_first_row(
        self: Self,
    ) -> "List[_1938.RollerRaceProfilePoint]":
        """List[mastapy.bearings.roller_bearing_profiles.RollerRaceProfilePoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRaceAndRollerProfilesForFirstRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def outer_race_and_roller_profiles_for_second_row(
        self: Self,
    ) -> "List[_1938.RollerRaceProfilePoint]":
        """List[mastapy.bearings.roller_bearing_profiles.RollerRaceProfilePoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterRaceAndRollerProfilesForSecondRow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "RollerBearing._Cast_RollerBearing":
        return self._Cast_RollerBearing(self)

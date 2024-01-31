"""RollerBearingProfile"""
from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_PROFILE = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "RollerBearingProfile"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollerBearingProfile",)


Self = TypeVar("Self", bound="RollerBearingProfile")


class RollerBearingProfile(_0.APIBase):
    """RollerBearingProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerBearingProfile")

    class _Cast_RollerBearingProfile:
        """Special nested class for casting RollerBearingProfile to subclasses."""

        def __init__(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
            parent: "RollerBearingProfile",
        ):
            self._parent = parent

        @property
        def roller_bearing_conical_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ):
            from mastapy.bearings.roller_bearing_profiles import _1930

            return self._parent._cast(_1930.RollerBearingConicalProfile)

        @property
        def roller_bearing_crowned_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ):
            from mastapy.bearings.roller_bearing_profiles import _1931

            return self._parent._cast(_1931.RollerBearingCrownedProfile)

        @property
        def roller_bearing_din_lundberg_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ):
            from mastapy.bearings.roller_bearing_profiles import _1932

            return self._parent._cast(_1932.RollerBearingDinLundbergProfile)

        @property
        def roller_bearing_flat_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ):
            from mastapy.bearings.roller_bearing_profiles import _1933

            return self._parent._cast(_1933.RollerBearingFlatProfile)

        @property
        def roller_bearing_johns_gohar_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ):
            from mastapy.bearings.roller_bearing_profiles import _1934

            return self._parent._cast(_1934.RollerBearingJohnsGoharProfile)

        @property
        def roller_bearing_lundberg_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ):
            from mastapy.bearings.roller_bearing_profiles import _1935

            return self._parent._cast(_1935.RollerBearingLundbergProfile)

        @property
        def roller_bearing_user_specified_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ):
            from mastapy.bearings.roller_bearing_profiles import _1937

            return self._parent._cast(_1937.RollerBearingUserSpecifiedProfile)

        @property
        def roller_bearing_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "RollerBearingProfile":
            return self._parent

        def __getattr__(
            self: "RollerBearingProfile._Cast_RollerBearingProfile", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerBearingProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def covers_two_rows_of_elements(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CoversTwoRowsOfElements

        if temp is None:
            return False

        return temp

    @covers_two_rows_of_elements.setter
    @enforce_parameter_types
    def covers_two_rows_of_elements(self: Self, value: "bool"):
        self.wrapped.CoversTwoRowsOfElements = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "RollerBearingProfile._Cast_RollerBearingProfile":
        return self._Cast_RollerBearingProfile(self)

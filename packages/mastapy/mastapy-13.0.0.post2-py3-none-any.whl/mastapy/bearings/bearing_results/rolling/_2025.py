"""LoadedNonBarrelRollerBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2030
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedNonBarrelRollerBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2024


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedNonBarrelRollerBearingRow")


class LoadedNonBarrelRollerBearingRow(_2030.LoadedRollerBearingRow):
    """LoadedNonBarrelRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNonBarrelRollerBearingRow")

    class _Cast_LoadedNonBarrelRollerBearingRow:
        """Special nested class for casting LoadedNonBarrelRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
            parent: "LoadedNonBarrelRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ):
            return self._parent._cast(_2030.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedRollingBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _1995

            return self._parent._cast(
                _1995.LoadedAxialThrustCylindricalRollerBearingRow
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _1998

            return self._parent._cast(_1998.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2010

            return self._parent._cast(_2010.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_needle_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2022

            return self._parent._cast(_2022.LoadedNeedleRollerBearingRow)

        @property
        def loaded_taper_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2049

            return self._parent._cast(_2049.LoadedTaperRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ) -> "LoadedNonBarrelRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedNonBarrelRollerBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rib_normal_contact_stress_inner_left(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressInnerLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def rib_normal_contact_stress_inner_right(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressInnerRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def rib_normal_contact_stress_outer_left(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressOuterLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def rib_normal_contact_stress_outer_right(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressOuterRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def loaded_bearing(self: Self) -> "_2024.LoadedNonBarrelRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedNonBarrelRollerBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow":
        return self._Cast_LoadedNonBarrelRollerBearingRow(self)

"""LoadedTaperRollerBearingRow"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2025
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TAPER_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedTaperRollerBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2048


__docformat__ = "restructuredtext en"
__all__ = ("LoadedTaperRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedTaperRollerBearingRow")


class LoadedTaperRollerBearingRow(_2025.LoadedNonBarrelRollerBearingRow):
    """LoadedTaperRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_TAPER_ROLLER_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedTaperRollerBearingRow")

    class _Cast_LoadedTaperRollerBearingRow:
        """Special nested class for casting LoadedTaperRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedTaperRollerBearingRow._Cast_LoadedTaperRollerBearingRow",
            parent: "LoadedTaperRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedTaperRollerBearingRow._Cast_LoadedTaperRollerBearingRow",
        ):
            return self._parent._cast(_2025.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(
            self: "LoadedTaperRollerBearingRow._Cast_LoadedTaperRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedTaperRollerBearingRow._Cast_LoadedTaperRollerBearingRow",
        ):
            from mastapy.bearings.bearing_results.rolling import _2034

            return self._parent._cast(_2034.LoadedRollingBearingRow)

        @property
        def loaded_taper_roller_bearing_row(
            self: "LoadedTaperRollerBearingRow._Cast_LoadedTaperRollerBearingRow",
        ) -> "LoadedTaperRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedTaperRollerBearingRow._Cast_LoadedTaperRollerBearingRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedTaperRollerBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self: Self) -> "_2048.LoadedTaperRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedTaperRollerBearingResults

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
    ) -> "LoadedTaperRollerBearingRow._Cast_LoadedTaperRollerBearingRow":
        return self._Cast_LoadedTaperRollerBearingRow(self)

"""LoadedTaperRollerBearingDutyCycle"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2023
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TAPER_ROLLER_BEARING_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedTaperRollerBearingDutyCycle"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedTaperRollerBearingDutyCycle",)


Self = TypeVar("Self", bound="LoadedTaperRollerBearingDutyCycle")


class LoadedTaperRollerBearingDutyCycle(_2023.LoadedNonBarrelRollerBearingDutyCycle):
    """LoadedTaperRollerBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_TAPER_ROLLER_BEARING_DUTY_CYCLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedTaperRollerBearingDutyCycle")

    class _Cast_LoadedTaperRollerBearingDutyCycle:
        """Special nested class for casting LoadedTaperRollerBearingDutyCycle to subclasses."""

        def __init__(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
            parent: "LoadedTaperRollerBearingDutyCycle",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ):
            return self._parent._cast(_2023.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ):
            from mastapy.bearings.bearing_results import _1959

            return self._parent._cast(_1959.LoadedRollingBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ):
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ):
            from mastapy.bearings.bearing_results import _1948

            return self._parent._cast(_1948.LoadedBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
        ) -> "LoadedTaperRollerBearingDutyCycle":
            return self._parent

        def __getattr__(
            self: "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "LoadedTaperRollerBearingDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedTaperRollerBearingDutyCycle._Cast_LoadedTaperRollerBearingDutyCycle":
        return self._Cast_LoadedTaperRollerBearingDutyCycle(self)

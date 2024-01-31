"""LoadedToroidalRollerBearingResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2029
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TOROIDAL_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedToroidalRollerBearingResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedToroidalRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedToroidalRollerBearingResults")


class LoadedToroidalRollerBearingResults(_2029.LoadedRollerBearingResults):
    """LoadedToroidalRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_TOROIDAL_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedToroidalRollerBearingResults")

    class _Cast_LoadedToroidalRollerBearingResults:
        """Special nested class for casting LoadedToroidalRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults",
            parent: "LoadedToroidalRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_results(
            self: "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults",
        ):
            return self._parent._cast(_2029.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults",
        ):
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults",
        ) -> "LoadedToroidalRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults",
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
        self: Self, instance_to_wrap: "LoadedToroidalRollerBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedToroidalRollerBearingResults._Cast_LoadedToroidalRollerBearingResults":
        return self._Cast_LoadedToroidalRollerBearingResults(self)

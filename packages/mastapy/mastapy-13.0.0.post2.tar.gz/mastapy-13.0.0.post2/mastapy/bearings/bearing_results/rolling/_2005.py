"""LoadedCrossedRollerBearingResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2029
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CROSSED_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedCrossedRollerBearingResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCrossedRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedCrossedRollerBearingResults")


class LoadedCrossedRollerBearingResults(_2029.LoadedRollerBearingResults):
    """LoadedCrossedRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_CROSSED_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedCrossedRollerBearingResults")

    class _Cast_LoadedCrossedRollerBearingResults:
        """Special nested class for casting LoadedCrossedRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
            parent: "LoadedCrossedRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_results(
            self: "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
        ):
            return self._parent._cast(_2029.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
        ):
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
        ) -> "LoadedCrossedRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults",
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
        self: Self, instance_to_wrap: "LoadedCrossedRollerBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedCrossedRollerBearingResults._Cast_LoadedCrossedRollerBearingResults":
        return self._Cast_LoadedCrossedRollerBearingResults(self)

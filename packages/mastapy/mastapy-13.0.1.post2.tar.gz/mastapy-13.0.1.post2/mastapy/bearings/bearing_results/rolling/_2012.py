"""LoadedDeepGrooveBallBearingResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_DEEP_GROOVE_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedDeepGrooveBallBearingResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedDeepGrooveBallBearingResults",)


Self = TypeVar("Self", bound="LoadedDeepGrooveBallBearingResults")


class LoadedDeepGrooveBallBearingResults(_2002.LoadedBallBearingResults):
    """LoadedDeepGrooveBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_DEEP_GROOVE_BALL_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedDeepGrooveBallBearingResults")

    class _Cast_LoadedDeepGrooveBallBearingResults:
        """Special nested class for casting LoadedDeepGrooveBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults",
            parent: "LoadedDeepGrooveBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(
            self: "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults",
        ):
            return self._parent._cast(_2002.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults",
        ):
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults",
        ) -> "LoadedDeepGrooveBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults",
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
        self: Self, instance_to_wrap: "LoadedDeepGrooveBallBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedDeepGrooveBallBearingResults._Cast_LoadedDeepGrooveBallBearingResults":
        return self._Cast_LoadedDeepGrooveBallBearingResults(self)

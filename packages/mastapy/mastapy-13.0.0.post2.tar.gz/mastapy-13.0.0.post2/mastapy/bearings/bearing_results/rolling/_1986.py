"""LoadedAngularContactThrustBallBearingResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _1983
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAngularContactThrustBallBearingResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAngularContactThrustBallBearingResults",)


Self = TypeVar("Self", bound="LoadedAngularContactThrustBallBearingResults")


class LoadedAngularContactThrustBallBearingResults(
    _1983.LoadedAngularContactBallBearingResults
):
    """LoadedAngularContactThrustBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_THRUST_BALL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAngularContactThrustBallBearingResults"
    )

    class _Cast_LoadedAngularContactThrustBallBearingResults:
        """Special nested class for casting LoadedAngularContactThrustBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
            parent: "LoadedAngularContactThrustBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ):
            return self._parent._cast(_1983.LoadedAngularContactBallBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2002

            return self._parent._cast(_2002.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ):
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
        ) -> "LoadedAngularContactThrustBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults",
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
        self: Self,
        instance_to_wrap: "LoadedAngularContactThrustBallBearingResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAngularContactThrustBallBearingResults._Cast_LoadedAngularContactThrustBallBearingResults":
        return self._Cast_LoadedAngularContactThrustBallBearingResults(self)

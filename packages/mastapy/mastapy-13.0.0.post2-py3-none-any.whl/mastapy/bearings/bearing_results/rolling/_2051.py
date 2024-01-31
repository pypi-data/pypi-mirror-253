"""LoadedThreePointContactBallBearingResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2002
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_THREE_POINT_CONTACT_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedThreePointContactBallBearingResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedThreePointContactBallBearingResults",)


Self = TypeVar("Self", bound="LoadedThreePointContactBallBearingResults")


class LoadedThreePointContactBallBearingResults(_2002.LoadedBallBearingResults):
    """LoadedThreePointContactBallBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_THREE_POINT_CONTACT_BALL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedThreePointContactBallBearingResults"
    )

    class _Cast_LoadedThreePointContactBallBearingResults:
        """Special nested class for casting LoadedThreePointContactBallBearingResults to subclasses."""

        def __init__(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
            parent: "LoadedThreePointContactBallBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ):
            return self._parent._cast(_2002.LoadedBallBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ):
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
        ) -> "LoadedThreePointContactBallBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults",
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
        self: Self, instance_to_wrap: "LoadedThreePointContactBallBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedThreePointContactBallBearingResults._Cast_LoadedThreePointContactBallBearingResults":
        return self._Cast_LoadedThreePointContactBallBearingResults(self)

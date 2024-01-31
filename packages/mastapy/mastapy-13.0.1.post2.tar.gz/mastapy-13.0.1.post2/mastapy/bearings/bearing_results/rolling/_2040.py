"""LoadedSphericalRollerRadialBearingResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2029
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalRollerRadialBearingResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalRollerRadialBearingResults",)


Self = TypeVar("Self", bound="LoadedSphericalRollerRadialBearingResults")


class LoadedSphericalRollerRadialBearingResults(_2029.LoadedRollerBearingResults):
    """LoadedSphericalRollerRadialBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_RADIAL_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedSphericalRollerRadialBearingResults"
    )

    class _Cast_LoadedSphericalRollerRadialBearingResults:
        """Special nested class for casting LoadedSphericalRollerRadialBearingResults to subclasses."""

        def __init__(
            self: "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults",
            parent: "LoadedSphericalRollerRadialBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_results(
            self: "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults",
        ):
            return self._parent._cast(_2029.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults",
        ):
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults",
        ) -> "LoadedSphericalRollerRadialBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults",
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
        self: Self, instance_to_wrap: "LoadedSphericalRollerRadialBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedSphericalRollerRadialBearingResults._Cast_LoadedSphericalRollerRadialBearingResults":
        return self._Cast_LoadedSphericalRollerRadialBearingResults(self)

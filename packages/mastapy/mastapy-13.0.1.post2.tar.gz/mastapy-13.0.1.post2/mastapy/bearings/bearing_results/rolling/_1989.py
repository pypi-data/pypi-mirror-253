"""LoadedAsymmetricSphericalRollerBearingResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2029
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedAsymmetricSphericalRollerBearingResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedAsymmetricSphericalRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedAsymmetricSphericalRollerBearingResults")


class LoadedAsymmetricSphericalRollerBearingResults(_2029.LoadedRollerBearingResults):
    """LoadedAsymmetricSphericalRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ASYMMETRIC_SPHERICAL_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedAsymmetricSphericalRollerBearingResults"
    )

    class _Cast_LoadedAsymmetricSphericalRollerBearingResults:
        """Special nested class for casting LoadedAsymmetricSphericalRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults",
            parent: "LoadedAsymmetricSphericalRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_results(
            self: "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults",
        ):
            return self._parent._cast(_2029.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults",
        ):
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults",
        ) -> "LoadedAsymmetricSphericalRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults",
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
        instance_to_wrap: "LoadedAsymmetricSphericalRollerBearingResults.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedAsymmetricSphericalRollerBearingResults._Cast_LoadedAsymmetricSphericalRollerBearingResults":
        return self._Cast_LoadedAsymmetricSphericalRollerBearingResults(self)

"""LoadedNonBarrelRollerBearingResults"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _2029
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedNonBarrelRollerBearingResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2072


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedNonBarrelRollerBearingResults")


class LoadedNonBarrelRollerBearingResults(_2029.LoadedRollerBearingResults):
    """LoadedNonBarrelRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNonBarrelRollerBearingResults")

    class _Cast_LoadedNonBarrelRollerBearingResults:
        """Special nested class for casting LoadedNonBarrelRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
            parent: "LoadedNonBarrelRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            return self._parent._cast(_2029.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2033

            return self._parent._cast(_2033.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1957

            return self._parent._cast(_1957.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1949

            return self._parent._cast(_1949.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings import _1875

            return self._parent._cast(_1875.BearingLoadCaseResultsLightweight)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1994

            return self._parent._cast(
                _1994.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1997

            return self._parent._cast(_1997.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(_2009.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedNeedleRollerBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2048

            return self._parent._cast(_2048.LoadedTaperRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
        ) -> "LoadedNonBarrelRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
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
        self: Self, instance_to_wrap: "LoadedNonBarrelRollerBearingResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def smt_rib_stress(self: Self) -> "_2072.SMTRibStressResults":
        """mastapy.bearings.bearing_results.rolling.SMTRibStressResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SMTRibStress

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults"
    ):
        return self._Cast_LoadedNonBarrelRollerBearingResults(self)
